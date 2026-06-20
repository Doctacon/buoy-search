# turbo-search

Local Python prototype for testing turbopuffer-backed RAG over exported Jellyfish site docs.

## Scope

Implemented so far:

- Safe Markdown indexing CLI, dry-run by default.
- Recursive `*.md` discovery under `jellyfish-site-docs/`.
- Frontmatter parsing for `url` and `title`.
- Conservative site-chrome normalization.
- Heading-aware Markdown chunking with ~300-token target chunks and sentence overlap.
- Deterministic chunk IDs and citation/debug metadata.
- Explicit `--write` mode that embeds locally with `BAAI/bge-small-en-v1.5` and upserts batches to turbopuffer.
- Hybrid retrieval CLI/library with query embedding, turbopuffer multi-query ANN + boosted BM25, server RRF, and client-side RRF fallback.

## Setup

Install dependencies with `uv`:

```bash
uv sync
```

Non-secret defaults used by the prototype:

```bash
export TURBOPUFFER_REGION=gcp-us-central1
export TURBOPUFFER_NAMESPACE=jellyfish-site-docs-v1
```

Do not store `TURBOPUFFER_API_KEY` in this repository. Write mode and live retrieval read it from the environment at runtime only.

## Safe commands

Show CLI help without credentials:

```bash
PYTHONPATH=src uv run --no-sync python -m turbo_search --help
```

Dry-run the full local corpus. This parses and chunks files only; it does not load embeddings, read secrets, or contact turbopuffer:

```bash
PYTHONPATH=src uv run --no-sync python -m turbo_search index --corpus-dir jellyfish-site-docs
```

Optional dry-run limits:

```bash
PYTHONPATH=src uv run --no-sync python -m turbo_search index \
  --corpus-dir jellyfish-site-docs \
  --max-files 25 \
  --limit-chunks 100
```

Plan retrieval without credentials. This is the default for `retrieve`; it does not load the embedding model or contact turbopuffer:

```bash
PYTHONPATH=src uv run --no-sync python -m turbo_search retrieve \
  "What are DORA metrics?" \
  --dry-run \
  --top-k 5 \
  --candidates 100 \
  --json
```

List the built-in retrieval smoke eval questions and expected URL/topic hints without credentials:

```bash
PYTHONPATH=src uv run --no-sync python -m turbo_search evals \
  --dry-run \
  --top-k 5 \
  --candidates 100 \
  --json
```

## Explicit write mode

Only run this after credentials are approved and `TURBOPUFFER_API_KEY` is already present in the environment:

```bash
uv run turbo-search index --corpus-dir jellyfish-site-docs --write --batch-size 64
```

Write mode uses local open-source BGE embeddings by default:

- Model: `BAAI/bge-small-en-v1.5`
- Override: `TURBO_SEARCH_EMBEDDING_MODEL`

Rows contain:

- `id`
- `vector`
- `content`
- `title`
- `url`
- `path`
- `section_path`
- `chunk_index`
- `doc_kind`
- `tags`
- `source_hash`

The turbopuffer schema enables ANN on `vector` and BM25 full-text search on `content`, `title`, and `section_path`.

## Agent answering workflow

Before answering user questions from Jellyfish docs, retrieve context and follow the citation/insufficient-context guardrails in [`docs/agent-answering-workflow.md`](docs/agent-answering-workflow.md).

## Explicit live retrieval and smoke evals

Only run these after indexing has completed and credentials are approved in the shell environment:

```bash
uv run turbo-search retrieve "What does Jellyfish say about developer productivity?" --live --top-k 5 --candidates 100 --json
```

Run the lightweight smoke/eval harness against the indexed namespace:

```bash
uv run turbo-search evals --live --top-k 5 --candidates 30 --json
```

The built-in eval dataset lives at `src/turbo_search/data/retrieval_smoke_evals.json` and covers five representative Jellyfish questions with expected URL/topic hints for developer productivity, DORA metrics, DevFinOps, Claude Code/Cursor integrations, and AI coding tool adoption.

Live retrieval:

- Reads `TURBOPUFFER_API_KEY` from the environment only when `--live` is passed.
- Embeds the query with the same local `BAAI/bge-small-en-v1.5` model used by the indexer.
- Sends one turbopuffer `multi_query` containing an ANN vector subquery and a boosted BM25 subquery over `title`, `section_path`, and `content`.
- Prefers server-side `rerank_by=("RRF",)` and falls back to local reciprocal-rank fusion when needed.
- Returns citation fields (`title`, `url`, `section_path`, `content`, `path`) and score info. Vectors are not requested or returned by default.
- Supports `--doc-kind` filters such as `blog`, `library`, `platform`, or `integrations`.

## Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m compileall src tests
```
