Status: open
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-generic-site-rag-incremental-plan-apply.md
Depends-On: .loom/tickets/2026-06-20-plan-artifact-manifest-model.md, .loom/tickets/2026-06-20-incremental-plan-diff-engine.md, .loom/specs/generic-site-rag-incremental-plan-apply.md, .loom/specs/generic-website-rag-dry-run-crawl.md

# Plan CLI Artifact Workflow

## Scope

Add the polished local-only plan command for generic website RAG indexing.

In scope:

- Add `turbo-search plan` or a clearly documented plan mode using the existing `crawl` implementation.
- Reuse Scrapling crawl/extract/chunk behavior from `turbo-search crawl`.
- Write `plan.json`, `manifest.json`, `chunks.jsonl`, `summary.json`, and `pages/*.md`.
- Load local state if present and include incremental diff output.
- Print JSON and text summaries.
- Keep all plan behavior credential-free and turbopuffer-free.
- Preserve existing `turbo-search crawl` behavior or provide a backwards-compatible alias.
- Tests for CLI validation, no credentials, no live calls, and artifact creation.

Out of scope:

- Live apply.
- Embeddings.
- Turbopuffer writes/deletes.
- Remote state.
- Browser-rendered crawling.

## Command sketch

```bash
turbo-search plan \
  --base-url "https://scrapling.readthedocs.io/en/latest/" \
  --out-dir artifacts/site-crawls/scrapling-readthedocs-io-plan \
  --max-pages 1000 \
  --max-chunks 10000 \
  --css-selector ".md-content__inner" \
  --json
```

Optional namespace override:

```bash
turbo-search plan --base-url <url> --namespace site-example-com-v1 --json
```

## Acceptance criteria

- `turbo-search plan --base-url <url> --json` exists.
- Invalid base URL exits with code 2 and a clear message.
- Plan writes all required artifacts.
- Plan output includes safety fields:
  - `dry_run: true`
  - `credentials_required: false`
  - `turbopuffer_api_calls: false`
  - `api_calls_occurred: false`
- Plan output includes page/chunk/diff counts.
- Plan uses local state if present and first-apply state if absent.
- Plan does not load embedding model or read `TURBOPUFFER_API_KEY`.
- Existing crawl tests continue to pass.
- Add mocked/no-network CLI tests for artifact mode.

## Progress and notes

- 2026-06-20: Ticket opened for Phase 2 CLI surface.

## Blockers

Depends on artifact/manifest model and diff engine.
