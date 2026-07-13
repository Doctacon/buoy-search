---
name: turbopuffer-site-rag
description: Build, operate, or query turbopuffer-backed RAG indexes for websites. Use for Scrapling crawls, local plan/apply validation, namespace planning, retrieval with citations, incremental updates, and cost-safe guardrails around turbopuffer writes.
---

# Turbopuffer Site RAG

This skill captures the generic Scrapling-based website-to-turbopuffer RAG workflow.

## Repository location

Run `uv run turbo-search ...` commands from the `turbo-search` repository root.

If this skill is installed globally by symlink, resolve the symlink target to find the repository clone. Otherwise, ask the user for the local clone path before running repo commands from another directory.

## Credentials from `.env`

`turbo-search` deliberately reads `TURBOPUFFER_API_KEY` from the process environment; it does not parse `.env` itself. When the repository `.env` is the intended credential source, load it only into the command subshell so an inherited key cannot silently override it:

```bash
(
  set -a
  . ./.env
  set +a
  uv run turbo-search <command>
)
```

Do not print, persist, or copy the key. `TURBOPUFFER_REGION`, `TURBOPUFFER_NAMESPACE`, and `TURBO_SEARCH_EMBEDDING_MODEL` remain optional non-secret environment overrides; CLI flags can override the first two per command.

## Compact applied state

Each `(site_id, namespace)` has an embedded local DuckDB ledger at:

```text
.turbo-search/state/<site-id>/<namespace>/state.duckdb
```

- The ledger stores current row state plus compact apply summaries, not full row snapshots.
- On first access, a legacy `last-applied.json` is deleted and active state starts empty. The next approved apply must therefore re-upsert the reviewed corpus; do not assume old local rows still exist remotely.
- `apply --approve` takes a non-blocking lock for that namespace before embeddings or Turbopuffer writes. A same-namespace contender fails with a busy error; different namespaces have independent databases and can apply concurrently.
- This is embedded local state: do not add or depend on Quack, a listener, or shared cross-machine state.

## Non-negotiable guardrails

- Do **not** persist API keys, Proton Pass output, tokens, private vault names, private item titles, or share IDs to disk.
- Do **not** run live turbopuffer writes, namespace deletion, namespace replacement, or live evals unless the user explicitly approves that action in the current conversation.
- Default crawl/plan/apply-preflight commands to dry-run/local-only.
- Use open-source/local components where practical:
  - local embeddings: `BAAI/bge-small-en-v1.5`
  - scraper/crawler: Scrapling
  - package manager: `uv`
- Respect crawl ethics by default: same-site only, `robots_txt_obey = True`, conservative concurrency, crawl delay, and no paywall/auth/protection bypass unless explicitly authorized.
- When answering from a site index, retrieve context first and cite retrieved page titles/URLs.

## Generic Scrapling site workflow

Use this when building or testing the “base URL → crawl → chunks → namespace → search” workflow.

The polished workflow is Terraform-like:

1. `turbo-search plan`: local-only preview. Crawl with Scrapling, extract Markdown, chunk, compare with local applied state, and write review artifacts. No credentials, embeddings, namespace creation, or turbopuffer calls. Interactive text-mode runs show default one-line stderr progress; use `--no-progress` to disable it. Versioned docs sites stop before page crawling by default with `--docs-version-policy warn`; use `latest`, `stable-latest`, `latest-nightly`, or `all` to make the policy explicit.
2. `turbo-search apply` without `--approve`: local-only preflight. Re-read the saved plan, verify artifacts, recompute the local diff, and report what would happen. No credentials, embeddings, or turbopuffer calls.
3. `turbo-search apply --approve`: explicit live path. Require `TURBOPUFFER_API_KEY` in the environment, embed/upsert only new or changed chunks, and update local applied state after success.
4. `--delete-stale`: extra delete guardrail. Stale rows are retained by default; live stale deletion requires both `--approve` and `--delete-stale`.

Plan artifacts are Markdown/JSON-first: `plan.json`, `summary.json`, `manifest.json`, `chunks.jsonl`, and `pages/*.md`. Pending, failed, and preflight plans remain for review/retry; successful approved apply removes its exact plan directory, and a new verified plan removes older same-namespace sibling plans. Copy artifacts elsewhere before approved apply when long-term audit/source retention is needed. Local applied state lives under `.turbo-search/state/.../state.duckdb` and is gitignored.

See [Scrapling site workflow](references/scrapling-site-workflow.md) for commands and design notes.

## Dry-run Scrapling crawler

Use the first-class CLI from the repository root:

```bash
uv run turbo-search crawl \
  --base-url "https://scrapling.readthedocs.io/en/latest/" \
  --max-pages 10 \
  --max-chunks 100 \
  --css-selector ".md-content__inner" \
  --json
```

This command must report `dry_run: true` and `turbopuffer_api_calls: false`.

## Live apply checklist

Only proceed if the user explicitly asks for a live generic site apply.

1. Run `turbo-search plan` first and inspect `summary.json`, `plan.json`, `manifest.json`, `chunks.jsonl`, and generated `pages/*.md`. Use `--include-path` / `--exclude-path` before apply when the crawl contains duplicate or unwanted paths such as `/llms-full.txt`.
2. Run apply preflight without approval:

```bash
uv run turbo-search apply
```

`apply` defaults to the newest `artifacts/site-crawls/**/plan.json` and the namespace recorded in that plan. Use `--json` for scripts/automation. Use `--plan` or `--namespace` only when overriding those defaults.

3. Confirm the namespace, rows to upsert, embeddings to generate, stale row counts, and whether stale deletion is desired. Default: retain stale rows; never delete namespaces here.
4. When the repository `.env` is the approved credential source, load it only in the command subshell; the CLI reads the resulting process environment and never prints or stores the key:

```bash
(
  set -a
  . ./.env
  set +a
  uv run turbo-search apply --approve
)
```

   Otherwise, set `TURBOPUFFER_API_KEY` only in the active shell and run the same approved command. Pass `--region` and `--namespace` when the reviewed plan requires non-default values.

5. Delete stale rows only when explicitly requested with both `--approve` and `--delete-stale`.
6. Record evidence with counts and command shape, never secret values, private vault names, item titles, share IDs, or token/API-key values.
