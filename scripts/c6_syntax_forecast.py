#!/usr/bin/env python3
"""Reconstruct and validate the checked-in C6 syntax forecast checkpoint.

Generation consumes explicit pinned source and plan roots; no temporary path is
built in or treated as authority. Validation is offline and uses only checked-in
artifacts. The optional tokenizer preflight loads only the pinned local tokenizer
and never constructs a model or performs inference.
"""

from __future__ import annotations

import argparse
import ast
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import warnings
from typing import Any, Iterable

FORECAST_PATH = Path(".10x/evidence/.storage/2026-07-20-c6-python-syntax-pilot-forecast.json")
TOKEN_REPORT_PATH = Path(".10x/evidence/.storage/2026-07-20-c6-python-syntax-tokenizer-preflight.json.gz")
MODEL = "BAAI/bge-small-en-v1.5"
MODEL_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
MODEL_MAX_TOKENS = 512
ARMS = ("current-default", "fixed-80-python-breadcrumbs", "python-ast")
TREATMENT_ARMS = ARMS[1:]
REPOSITORIES = ("buoy", "pytest", "ruff")
VECTOR_BYTES_PER_ROW = 384 * 2

JsonObject = dict[str, Any]


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def artifact_sha256(payload: JsonObject) -> str:
    unhashed = dict(payload)
    unhashed.pop("artifact_sha256", None)
    return canonical_sha256(unhashed)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_forecast(payload: JsonObject) -> None:
    """Recompute checkpoint identity, row classes, writes, and storage totals."""

    _require(payload.get("artifact_sha256") == artifact_sha256(payload), "forecast artifact hash mismatch")
    _require(tuple(payload.get("repositories", {})) == REPOSITORIES, "forecast repository order mismatch")

    totals = {arm: {"rows": 0, "writes": 0, "requests": 0, "content": 0, "raw": 0, "jsonl": 0} for arm in ARMS}
    for repository in REPOSITORIES:
        repo = payload["repositories"][repository]
        selected_files = repo["selected_files"]
        _require(repo["selected_file_count"] == len(selected_files), f"{repository}: selected-file count mismatch")
        paths = [entry["repo_path"] for entry in selected_files]
        _require(paths == sorted(paths), f"{repository}: selected paths are not ordered")
        _require(repo["selected_paths_sha256"] == canonical_sha256(paths), f"{repository}: selected-path hash mismatch")
        _require(repo["selected_corpus_sha256"] == canonical_sha256(selected_files), f"{repository}: selected-corpus hash mismatch")

        for arm in ARMS:
            summary = repo["arms"][arm]
            rows = summary["final_rows"]
            _require(rows == summary["header_rows"] + summary["source_rows"] + summary["prose_rows"], f"{repository}/{arm}: row classes do not sum")
            _require(summary["estimated_row_writes"] == rows, f"{repository}/{arm}: write count mismatch")
            _require(summary["estimated_deletes"] == 0, f"{repository}/{arm}: deletes are nonzero")
            _require(summary["estimated_upsert_requests_at_batch_64"] == math.ceil(rows / 64), f"{repository}/{arm}: request count mismatch")
            storage = summary["storage_estimates_bytes"]
            _require(storage["raw_384_dim_f16_vectors"] == rows * VECTOR_BYTES_PER_ROW, f"{repository}/{arm}: raw vector storage mismatch")
            _require(storage["serialized_plan_rows_plus_raw_vectors"] == storage["serialized_plan_chunks_jsonl"] + storage["raw_384_dim_f16_vectors"], f"{repository}/{arm}: storage sum mismatch")
            diff = summary["diff_summary"]
            _require(diff["first_apply"] is True and diff["rows_to_upsert"] == rows, f"{repository}/{arm}: first-apply rows mismatch")
            _require(diff["stale_rows"] == diff["retained_stale_rows"] == diff["chunks_unchanged"] == 0, f"{repository}/{arm}: first-apply diff is not empty-state")
            for key, value in (
                ("rows", rows),
                ("writes", summary["estimated_row_writes"]),
                ("requests", summary["estimated_upsert_requests_at_batch_64"]),
                ("content", storage["content_utf8"]),
                ("raw", storage["raw_384_dim_f16_vectors"]),
                ("jsonl", storage["serialized_plan_chunks_jsonl"]),
            ):
                totals[arm][key] += value

    for arm in ARMS:
        recorded = payload["totals"][arm]
        computed = totals[arm]
        _require(recorded["final_rows"] == computed["rows"], f"{arm}: total rows mismatch")
        _require(recorded["estimated_row_writes"] == computed["writes"], f"{arm}: total writes mismatch")
        _require(recorded["estimated_upsert_requests_at_batch_64"] == computed["requests"], f"{arm}: total requests mismatch")
        _require(recorded["content_utf8_bytes"] == computed["content"], f"{arm}: total content bytes mismatch")
        _require(recorded["raw_vector_bytes"] == computed["raw"], f"{arm}: total raw-vector bytes mismatch")
        _require(recorded["serialized_plan_chunks_jsonl_bytes"] == computed["jsonl"], f"{arm}: total JSONL bytes mismatch")
        _require(recorded["serialized_plan_rows_plus_raw_vectors_bytes"] == computed["jsonl"] + computed["raw"], f"{arm}: total storage mismatch")

    approval = payload["approval_checkpoint"]
    all_rows = sum(totals[arm]["rows"] for arm in ARMS)
    all_requests = sum(totals[arm]["requests"] for arm in ARMS)
    all_storage = sum(totals[arm]["jsonl"] + totals[arm]["raw"] for arm in ARMS)
    _require(approval["maximum_rows_and_estimated_row_writes"] == all_rows, "approval row envelope mismatch")
    _require(approval["estimated_upsert_requests_at_batch_64"] == all_requests, "approval request envelope mismatch")
    _require(approval["serialized_plan_rows_plus_raw_vectors_bytes"] == all_storage, "approval storage envelope mismatch")

    citation_paths = payload["preflight_findings"]["ruff_current_default_affected_paths"]
    _require(payload["preflight_findings"]["ruff_current_default_affected_file_count"] == len(citation_paths), "citation affected-file count mismatch")
    _require(payload["preflight_findings"]["ruff_current_default_affected_paths_sha256"] == canonical_sha256(citation_paths), "citation affected-path hash mismatch")


def validate_token_report(report: JsonObject, forecast: JsonObject) -> None:
    _require(report.get("artifact_sha256") == artifact_sha256(report), "token report artifact hash mismatch")
    tokenizer = report["tokenizer"]
    _require(tokenizer["model"] == MODEL, "token report model mismatch")
    _require(tokenizer["revision"] == MODEL_REVISION, "token report revision mismatch")
    _require(tokenizer["model_max_tokens"] == MODEL_MAX_TOKENS, "token report model maximum mismatch")
    incompatible = report["incompatible_rows"]
    _require(report["summary"]["incompatible_rows"] == len(incompatible), "token report incompatible-row count mismatch")
    _require(all(row["token_count"] > MODEL_MAX_TOKENS for row in incompatible), "token report contains a compatible row")
    _require(report["summary"]["incompatible_rows_sha256"] == canonical_sha256(incompatible), "token report incompatible-row hash mismatch")
    paths = sorted({row["repo_path"] for row in incompatible})
    _require(report["summary"]["incompatible_paths"] == len(paths), "token report incompatible-path count mismatch")
    _require(report["summary"]["incompatible_paths_sha256"] == canonical_sha256(paths), "token report incompatible-path hash mismatch")
    _require(report["summary"]["ready"] is False, "C6 tokenizer readiness must fail when incompatible rows exist")
    checkpoint = forecast["model_tokenizer_preflight"]
    _require(checkpoint["artifact_sha256"] == report["artifact_sha256"], "forecast/token report identity mismatch")
    _require(checkpoint["incompatible_rows"] == len(incompatible), "forecast/token report row-count mismatch")


def _embedding_text(chunk: JsonObject) -> str:
    values = []
    if chunk.get("title"):
        values.append(f"Title: {chunk['title']}")
    if chunk.get("section_path"):
        values.append(f"Section: {chunk['section_path']}")
    values.append(chunk["content"])
    return "\n\n".join(value for value in values if str(value).strip())


def _is_header(chunk: JsonObject) -> bool:
    metadata = chunk.get("source_metadata", {})
    expected = f"Repository file: `{metadata.get('repo_path', '')}`\nLanguage: `{metadata.get('language', '')}`"
    return chunk["content"] == expected


def _row_class(chunk: JsonObject, code_paths: set[str]) -> str:
    if _is_header(chunk):
        return "header"
    return "source" if chunk["source_metadata"].get("repo_path", "") in code_paths else "prose"


def _load_tokenizer(snapshot: Path) -> tuple[object, JsonObject]:
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    from transformers import AutoTokenizer
    from transformers.utils import logging as transformers_logging

    transformers_logging.set_verbosity_error()
    resolved = snapshot.expanduser().resolve(strict=True)
    _require(resolved.name == MODEL_REVISION, "tokenizer snapshot revision mismatch")
    tokenizer = AutoTokenizer.from_pretrained(resolved, local_files_only=True, revision=MODEL_REVISION)
    _require(tokenizer.model_max_length == MODEL_MAX_TOKENS, "tokenizer model maximum mismatch")
    files = []
    for name in ("special_tokens_map.json", "tokenizer.json", "tokenizer_config.json", "vocab.txt"):
        path = resolved / name
        files.append({"path": name, "sha256": file_sha256(path), "size_bytes": path.stat().st_size})
    identity = {
        "model": MODEL,
        "revision": MODEL_REVISION,
        "implementation": f"{type(tokenizer).__module__}.{type(tokenizer).__name__}",
        "model_max_tokens": MODEL_MAX_TOKENS,
        "add_special_tokens": True,
        "truncation": False,
        "files": files,
        "files_sha256": canonical_sha256(files),
    }
    return tokenizer, identity


def reconstruct_plan_facts(plan_root: Path, forecast: JsonObject) -> JsonObject:
    """Reconstruct every plan's identity, row classes, counts, and byte storage."""

    facts: JsonObject = {}
    for repository in REPOSITORIES:
        facts[repository] = {}
        for arm in ARMS:
            directory = plan_root / repository / arm
            recorded = forecast["repositories"][repository]["arms"][arm]
            expected_files = recorded["local_artifact_file_sha256"]
            for name in ("plan.json", "manifest.json", "chunks.jsonl"):
                _require(file_sha256(directory / name) == expected_files[name], f"{repository}/{arm}: {name} hash mismatch")
            plan = read_json(directory / "plan.json")
            _require(plan["plan_id"] == recorded["plan_id"], f"{repository}/{arm}: plan ID mismatch")
            _require(plan["artifact_hash"] == recorded["artifact_hash"], f"{repository}/{arm}: artifact hash mismatch")
            _require(plan["namespace"] == recorded["namespace"], f"{repository}/{arm}: namespace mismatch")
            chunks: list[JsonObject] = []
            with (directory / "chunks.jsonl").open(encoding="utf-8") as handle:
                chunks.extend(json.loads(line) for line in handle)
            code_paths = {chunk["source_metadata"]["repo_path"] for chunk in chunks if _is_header(chunk)}
            classes = {row_class: 0 for row_class in ("header", "source", "prose")}
            for chunk in chunks:
                classes[_row_class(chunk, code_paths)] += 1
            content_bytes = sum(len(chunk["content"].encode("utf-8")) for chunk in chunks)
            jsonl_bytes = (directory / "chunks.jsonl").stat().st_size
            _require(classes["header"] == recorded["header_rows"], f"{repository}/{arm}: reconstructed header rows mismatch")
            _require(classes["source"] == recorded["source_rows"], f"{repository}/{arm}: reconstructed source rows mismatch")
            _require(classes["prose"] == recorded["prose_rows"], f"{repository}/{arm}: reconstructed prose rows mismatch")
            _require(len(chunks) == recorded["final_rows"], f"{repository}/{arm}: reconstructed final rows mismatch")
            storage = recorded["storage_estimates_bytes"]
            _require(content_bytes == storage["content_utf8"], f"{repository}/{arm}: reconstructed content bytes mismatch")
            _require(jsonl_bytes == storage["serialized_plan_chunks_jsonl"], f"{repository}/{arm}: reconstructed JSONL bytes mismatch")
            facts[repository][arm] = {
                "artifact_hash": plan["artifact_hash"],
                "content_utf8_bytes": content_bytes,
                "plan_id": plan["plan_id"],
                "row_classes": classes,
                "rows": len(chunks),
                "serialized_plan_chunks_jsonl_bytes": jsonl_bytes,
            }
    return facts


def generate_token_report(plan_root: Path, snapshot: Path, forecast: JsonObject) -> JsonObject:
    tokenizer, identity = _load_tokenizer(snapshot)
    incompatible: list[JsonObject] = []
    rows_scanned = 0
    class_counts = {row_class: 0 for row_class in ("header", "source", "prose")}
    per_plan: JsonObject = {}

    for repository in REPOSITORIES:
        per_plan[repository] = {}
        for arm in TREATMENT_ARMS:
            chunks_path = plan_root / repository / arm / "chunks.jsonl"
            expected_hash = forecast["repositories"][repository]["arms"][arm]["local_artifact_file_sha256"]["chunks.jsonl"]
            _require(file_sha256(chunks_path) == expected_hash, f"{repository}/{arm}: chunks artifact hash mismatch")
            chunks: list[JsonObject] = []
            with chunks_path.open(encoding="utf-8") as handle:
                for line in handle:
                    chunks.append(json.loads(line))
            code_paths = {chunk["source_metadata"]["repo_path"] for chunk in chunks if _is_header(chunk)}
            texts = [_embedding_text(chunk) for chunk in chunks]
            lengths = tokenizer(texts, add_special_tokens=True, truncation=False, return_length=True)["length"]
            plan_incompatible = 0
            for chunk, token_count in zip(chunks, lengths, strict=True):
                row_class = _row_class(chunk, code_paths)
                class_counts[row_class] += 1
                rows_scanned += 1
                if token_count <= MODEL_MAX_TOKENS:
                    continue
                plan_incompatible += 1
                incompatible.append({
                    "arm": arm,
                    "repo_path": chunk["source_metadata"].get("repo_path", ""),
                    "repository": repository,
                    "row_class": row_class,
                    "row_id": chunk["row_id"],
                    "section_path": chunk["section_path"],
                    "token_count": token_count,
                })
            per_plan[repository][arm] = {
                "incompatible_rows": plan_incompatible,
                "rows_scanned": len(chunks),
            }

    incompatible.sort(key=lambda row: (row["repository"], row["arm"], row["repo_path"], row["row_id"]))
    paths = sorted({row["repo_path"] for row in incompatible})
    report: JsonObject = {
        "schema_version": 1,
        "tokenizer": identity,
        "input": {
            "arms": list(TREATMENT_ARMS),
            "payload": "exact Buoy embedding text: Title, Section, and content joined by double LF",
            "plan_chunks_sha256_verified_against_forecast": True,
        },
        "summary": {
            "ready": not incompatible,
            "rows_scanned": rows_scanned,
            "row_classes": class_counts,
            "incompatible_rows": len(incompatible),
            "incompatible_rows_sha256": canonical_sha256(incompatible),
            "incompatible_paths": len(paths),
            "incompatible_paths_sha256": canonical_sha256(paths),
            "maximum_observed_tokens": max(row["token_count"] for row in incompatible) if incompatible else MODEL_MAX_TOKENS,
            "readiness_rule": "fail if any exact treatment embedding payload exceeds the pinned 512-token model maximum; no truncation or token subdivision",
        },
        "per_plan": per_plan,
        "incompatible_rows": incompatible,
        "safety": {
            "credentials_read": 0,
            "model_constructions": 0,
            "model_inference_calls": 0,
            "network_calls": 0,
            "provider_calls": 0,
            "remote_writes": 0,
        },
    }
    report["artifact_sha256"] = artifact_sha256(report)
    return report


def fallback_path_categories(source_roots: dict[str, Path], plan_root: Path, forecast: JsonObject) -> JsonObject:
    result: JsonObject = {}
    for repository in REPOSITORIES:
        root = source_roots[repository].expanduser().resolve(strict=True)
        chunks_path = plan_root / repository / TREATMENT_ARMS[0] / "chunks.jsonl"
        with chunks_path.open(encoding="utf-8") as handle:
            code_paths = {
                chunk["source_metadata"]["repo_path"]
                for chunk in (json.loads(line) for line in handle)
                if _is_header(chunk)
            }
        parse_fallback: list[str] = []
        non_python: list[str] = []
        for selected in forecast["repositories"][repository]["selected_files"]:
            repo_path = selected["repo_path"]
            if repo_path not in code_paths:
                continue
            path = root / repo_path
            source = path.read_text(encoding="utf-8")
            _require(hashlib.sha256(source.encode("utf-8")).hexdigest() == selected["source_hash"], f"{repository}/{repo_path}: source hash mismatch")
            if selected["language"] != "python":
                non_python.append(repo_path)
                continue
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", SyntaxWarning)
                    ast.parse(source, filename=repo_path, mode="exec", type_comments=True, feature_version=(3, 11))
            except (SyntaxError, ValueError):
                parse_fallback.append(repo_path)
        result[repository] = {
            "python_parse_fallback": {"count": len(parse_fallback), "paths_sha256": canonical_sha256(parse_fallback)},
            "non_python_fallback": {"count": len(non_python), "paths_sha256": canonical_sha256(non_python)},
        }
    return result


def read_json(path: Path) -> JsonObject:
    if path.suffix == ".gz":
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            return json.load(handle)
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: JsonObject) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if path.suffix == ".gz":
        with path.open("wb") as raw:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as handle:
                handle.write(rendered)
        return
    path.write_bytes(rendered)


def parse_source_roots(values: Iterable[str]) -> dict[str, Path]:
    roots = {}
    for value in values:
        name, separator, path = value.partition("=")
        _require(bool(separator) and name in REPOSITORIES, f"invalid --source-root {value!r}")
        roots[name] = Path(path)
    _require(tuple(sorted(roots)) == tuple(sorted(REPOSITORIES)), "one --source-root is required for each repository")
    return roots


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forecast", type=Path, default=FORECAST_PATH)
    parser.add_argument("--token-report", type=Path, default=TOKEN_REPORT_PATH)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    generate = subparsers.add_parser("generate-preflight")
    generate.add_argument("--plan-root", type=Path, required=True)
    generate.add_argument("--tokenizer-snapshot", type=Path, required=True)
    generate.add_argument("--source-root", action="append", default=[])
    args = parser.parse_args()

    forecast = read_json(args.forecast)
    if args.command == "validate":
        validate_forecast(forecast)
        report = read_json(args.token_report)
        validate_token_report(report, forecast)
        print(f"C6 forecast valid: {forecast['artifact_sha256']}; tokenizer readiness=false exact checkpoint={report['artifact_sha256']}")
        return 0

    reconstruct_plan_facts(args.plan_root, forecast)
    report = generate_token_report(args.plan_root, args.tokenizer_snapshot, forecast)
    roots = parse_source_roots(args.source_root)
    forecast["fallback_path_categories"] = fallback_path_categories(roots, args.plan_root, forecast)
    write_json(args.token_report, report)
    forecast["model_tokenizer_preflight"] = {
        "artifact_path": str(args.token_report),
        "artifact_sha256": report["artifact_sha256"],
        "incompatible_paths": report["summary"]["incompatible_paths"],
        "incompatible_paths_sha256": report["summary"]["incompatible_paths_sha256"],
        "incompatible_rows": report["summary"]["incompatible_rows"],
        "incompatible_rows_sha256": report["summary"]["incompatible_rows_sha256"],
        "maximum_observed_tokens": report["summary"]["maximum_observed_tokens"],
        "model": MODEL,
        "model_max_tokens": MODEL_MAX_TOKENS,
        "ready": report["summary"]["ready"],
        "revision": MODEL_REVISION,
        "tokenizer_files_sha256": report["tokenizer"]["files_sha256"],
    }
    forecast["preflight_findings"]["approval_ready"] = False
    forecast["preflight_findings"]["blocking_interpretation"] = (
        "The citation correction preserves exact current-default parity. C6 readiness still fails because exact pinned-tokenizer preflight found treatment payloads above the model maximum; no truncation or token subdivision is authorized."
    )
    forecast["artifact_sha256"] = artifact_sha256(forecast)
    write_json(args.forecast, forecast)
    validate_forecast(forecast)
    validate_token_report(report, forecast)
    print(f"wrote exact blocked checkpoint {forecast['artifact_sha256']} and tokenizer report {report['artifact_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
