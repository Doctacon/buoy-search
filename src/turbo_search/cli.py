"""Command-line interface for the Jellyfish docs RAG prototype."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Sequence

from turbo_search import __version__
from turbo_search.config import load_config
from turbo_search.evals import (
    build_dry_run_eval_report,
    load_eval_cases,
    run_live_evals,
)
from turbo_search.indexer import (
    DEFAULT_OVERLAP_SENTENCES,
    DEFAULT_TARGET_TOKENS,
    IndexingPlan,
    process_corpus,
    write_chunks,
)
from turbo_search.retriever import (
    DEFAULT_CANDIDATES,
    DEFAULT_TOP_K,
    HybridRetriever,
    RetrievalOptions,
    RetrievalPlan,
    RetrievalResult,
    retrieval_plan,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="turbo-search",
        description="Local Jellyfish docs RAG utilities. Indexing is dry-run by default.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    index_parser = subparsers.add_parser(
        "index",
        help="parse and chunk Markdown docs; write only when --write is passed",
        description=(
            "Parse and chunk a Markdown corpus. Default mode is a safe dry-run: "
            "no credentials, embeddings, or turbopuffer API calls are used."
        ),
    )
    index_parser.add_argument(
        "--corpus-dir",
        default="jellyfish-site-docs",
        help="Markdown corpus directory to index.",
    )
    index_parser.add_argument(
        "--max-files",
        type=positive_int,
        default=None,
        help="Process at most this many Markdown files.",
    )
    index_parser.add_argument(
        "--limit-chunks",
        type=positive_int,
        default=None,
        help="Stop after generating this many chunks.",
    )
    index_parser.add_argument(
        "--batch-size",
        type=positive_int,
        default=64,
        help="Turbopuffer upsert batch size for --write mode.",
    )
    index_parser.add_argument(
        "--target-tokens",
        type=positive_int,
        default=DEFAULT_TARGET_TOKENS,
        help="Approximate target tokens per chunk.",
    )
    index_parser.add_argument(
        "--overlap-sentences",
        type=nonnegative_int,
        default=DEFAULT_OVERLAP_SENTENCES,
        help="Number of trailing sentences to overlap between adjacent chunks in a section.",
    )
    index_parser.add_argument(
        "--write",
        action="store_true",
        help="Explicitly embed chunks and write batched upserts to turbopuffer.",
    )
    index_parser.set_defaults(func=_run_index)

    retrieve_parser = subparsers.add_parser(
        "retrieve",
        help="retrieve relevant chunks; dry-run plan by default unless --live is passed",
        description=(
            "Plan or execute Jellyfish docs hybrid retrieval. Default mode is safe: "
            "it prints the multi-query plan without loading embeddings, reading credentials, "
            "or contacting turbopuffer. Pass --live to embed the query and query turbopuffer."
        ),
    )
    retrieve_parser.add_argument(
        "query",
        help="Question to retrieve relevant Jellyfish docs chunks for.",
    )
    retrieve_parser.add_argument(
        "--live",
        action="store_true",
        help="Execute live retrieval. Reads TURBOPUFFER_API_KEY from the environment and calls turbopuffer.",
    )
    retrieve_parser.add_argument(
        "--dry-run",
        "--plan",
        dest="dry_run",
        action="store_true",
        help="Print the retrieval plan without credentials, embeddings, or turbopuffer API calls (default).",
    )
    retrieve_parser.add_argument(
        "--top-k",
        type=positive_int,
        default=DEFAULT_TOP_K,
        help="Number of fused chunks to return.",
    )
    retrieve_parser.add_argument(
        "--candidates",
        type=positive_int,
        default=DEFAULT_CANDIDATES,
        help="Candidate limit for each ANN/BM25 subquery before RRF fusion.",
    )
    retrieve_parser.add_argument(
        "--doc-kind",
        default=None,
        help="Optional doc_kind filter, e.g. blog, library, platform, integrations.",
    )
    retrieve_parser.add_argument(
        "--json",
        action="store_true",
        help="Print JSON output. Text output is used by default for live results.",
    )
    retrieve_parser.set_defaults(func=_run_retrieve)

    evals_parser = subparsers.add_parser(
        "evals",
        help="list or run Jellyfish retrieval smoke evals",
        description=(
            "List or execute the hand-authored retrieval smoke evals. Default mode is safe: "
            "it lists eval questions and expected source hints without credentials, embeddings, "
            "or turbopuffer calls. Pass --live to run retrieval against turbopuffer."
        ),
    )
    evals_parser.add_argument(
        "--live",
        action="store_true",
        help="Execute live evals. Reads TURBOPUFFER_API_KEY from the environment and calls turbopuffer.",
    )
    evals_parser.add_argument(
        "--dry-run",
        "--list",
        dest="dry_run",
        action="store_true",
        help="List eval questions and expected hints without credentials or turbopuffer API calls (default).",
    )
    evals_parser.add_argument(
        "--top-k",
        type=positive_int,
        default=DEFAULT_TOP_K,
        help="Number of fused chunks to score for each eval question.",
    )
    evals_parser.add_argument(
        "--candidates",
        type=positive_int,
        default=DEFAULT_CANDIDATES,
        help="Candidate limit for each ANN/BM25 subquery before RRF fusion.",
    )
    evals_parser.add_argument(
        "--dataset",
        type=Path,
        default=None,
        help="Optional path to a JSON eval dataset. Defaults to the built-in Jellyfish smoke set.",
    )
    evals_parser.add_argument(
        "--json",
        action="store_true",
        help="Print JSON output. Text output is used by default.",
    )
    evals_parser.set_defaults(func=_run_evals)

    return parser


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def nonnegative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be zero or greater")
    return parsed


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def _run_index(args: argparse.Namespace) -> int:
    config = load_config()
    corpus_dir = Path(args.corpus_dir)
    try:
        plan = process_corpus(
            corpus_dir,
            max_files=args.max_files,
            limit_chunks=args.limit_chunks,
            target_tokens=args.target_tokens,
            overlap_sentences=args.overlap_sentences,
        )
    except FileNotFoundError as exc:
        print(f"Corpus directory not found: {exc}", file=sys.stderr)
        return 2
    except NotADirectoryError as exc:
        print(f"Corpus path is not a directory: {exc}", file=sys.stderr)
        return 2

    dry_run = not args.write
    rows_written = 0
    api_calls_occurred = False
    if args.write:
        try:
            rows_written = write_chunks(plan.chunks, config=config, batch_size=args.batch_size)
            plan.stats.rows_written = rows_written
            api_calls_occurred = rows_written > 0
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return 2

    _print_json(index_summary(plan, args=args, config=config, dry_run=dry_run, api_calls_occurred=api_calls_occurred))
    return 0


def index_summary(
    plan: IndexingPlan,
    *,
    args: argparse.Namespace,
    config: object,
    dry_run: bool,
    api_calls_occurred: bool,
) -> dict[str, object]:
    return {
        "command": "index",
        "dry_run": dry_run,
        "credentials_required": not dry_run,
        "turbopuffer_api_calls": api_calls_occurred,
        "api_calls_occurred": api_calls_occurred,
        "corpus_dir": str(plan.corpus_dir),
        "corpus_dir_exists": plan.corpus_dir.exists(),
        "files_discovered": plan.files_discovered,
        "files_seen": plan.stats.files_seen,
        "files_skipped_empty": plan.stats.files_skipped_empty,
        "files_error": plan.stats.files_error,
        "chunks_generated": plan.stats.chunks_generated,
        "rows_written": plan.stats.rows_written,
        "limit_reached": plan.limit_reached,
        "max_files": args.max_files,
        "limit_chunks": args.limit_chunks,
        "batch_size": args.batch_size,
        "target_tokens": args.target_tokens,
        "overlap_sentences": args.overlap_sentences,
        "region": config.region,
        "namespace": config.namespace,
        "embedding_model": config.embedding_model,
        "errors": [error.__dict__ for error in plan.stats.errors[:10]],
    }


def _run_retrieve(args: argparse.Namespace) -> int:
    config = load_config()
    options = RetrievalOptions(top_k=args.top_k, candidates=args.candidates, doc_kind=args.doc_kind)
    if args.dry_run and args.live:
        print("Choose either --live or --dry-run/--plan, not both.", file=sys.stderr)
        return 2
    if not args.live:
        plan = retrieval_plan(args.query, config=config, options=options)
        if args.json:
            _print_json(plan.to_dict())
        else:
            print_retrieval_text(plan)
        return 0

    try:
        result = HybridRetriever.from_config(config).retrieve(args.query, options)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if args.json:
        _print_json(result.to_dict())
    else:
        print_retrieval_text(result)
    return 0


def _run_evals(args: argparse.Namespace) -> int:
    config = load_config()
    options = RetrievalOptions(top_k=args.top_k, candidates=args.candidates)
    if args.dry_run and args.live:
        print("Choose either --live or --dry-run/--list, not both.", file=sys.stderr)
        return 2
    try:
        cases = load_eval_cases(args.dataset)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Could not load retrieval eval dataset: {exc}", file=sys.stderr)
        return 2

    if args.live:
        try:
            report = run_live_evals(cases, config=config, options=options)
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return 2
    else:
        report = build_dry_run_eval_report(cases, config=config, options=options)

    if args.json:
        _print_json(report.to_dict())
    else:
        print_eval_text(report.to_dict())
    return 0


def print_retrieval_text(output: RetrievalPlan | RetrievalResult) -> None:
    payload = output.to_dict()
    if payload.get("dry_run"):
        print("Retrieval plan (dry-run; no credentials, embeddings, or turbopuffer API calls):")
        print(f"  query: {payload['query']}")
        print(f"  namespace: {payload['namespace']} ({payload['region']})")
        print(f"  embedding_model: {payload['embedding_model']}")
        print(f"  top_k: {payload['top_k']}; candidates per subquery: {payload['candidates']}")
        print("  hybrid: ANN over vector + boosted BM25 over title/section_path/content + RRF")
        print("  live: pass --live to execute; TURBOPUFFER_API_KEY is read from the environment only")
        return

    hits = payload.get("hits", [])
    print(f"Retrieved {len(hits)} chunks using {payload.get('fusion')}:")
    for index, hit in enumerate(hits, start=1):
        if not isinstance(hit, dict):
            continue
        title = hit.get("title") or "Untitled"
        url = hit.get("url") or "no URL"
        section_path = hit.get("section_path") or ""
        print(f"\n{index}. {title}")
        print(f"   URL: {url}")
        if section_path:
            print(f"   Section: {section_path}")
        if hit.get("path"):
            print(f"   Path: {hit['path']}")
        print(f"   Score: {hit.get('score_info', {})}")
        content = str(hit.get("content") or "").strip()
        if content:
            preview = content if len(content) <= 600 else content[:597].rstrip() + "..."
            print(f"   Content: {preview}")


def print_eval_text(payload: dict[str, object]) -> None:
    if payload.get("dry_run"):
        print("Retrieval smoke evals (dry-run; no credentials, embeddings, or turbopuffer API calls):")
        print(f"  namespace: {payload['namespace']} ({payload['region']})")
        print(f"  evals: {payload['total']}; top_k: {payload['top_k']}; candidates: {payload['candidates']}")
        print("  live: pass --live to execute; TURBOPUFFER_API_KEY is read from the environment only")
    else:
        print(
            f"Retrieval smoke evals: {payload['passed']}/{payload['total']} passed "
            f"({float(payload['pass_rate']) * 100:.1f}%)"
        )
        print(f"  namespace: {payload['namespace']} ({payload['region']})")
    cases = payload.get("cases", [])
    if not isinstance(cases, list):
        return
    for case in cases:
        if not isinstance(case, dict):
            continue
        print(f"\n- {case.get('id')}: {case.get('question')}")
        if payload.get("dry_run"):
            print(f"  expected_urls: {case.get('expected_urls', [])}")
            print(f"  expected_topics: {case.get('expected_topics', [])}")
            continue
        score = case.get("score") if isinstance(case.get("score"), dict) else {}
        print(f"  status: {case.get('status')} (matched_rank={score.get('matched_rank')})")
        top_hits = case.get("top_hits", [])
        if not isinstance(top_hits, list):
            continue
        for hit in top_hits:
            if not isinstance(hit, dict):
                continue
            print(f"  {hit.get('rank')}. {hit.get('title') or 'Untitled'}")
            print(f"     URL: {hit.get('url') or 'no URL'}")
            if hit.get("section_path"):
                print(f"     Section: {hit['section_path']}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
