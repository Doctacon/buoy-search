# Scrapling site workflow for turbopuffer RAG

## Goal

Turn an arbitrary public website into a cost-conscious searchable RAG namespace:

```text
base URL
  -> namespace candidate
  -> Scrapling crawl
  -> clean Markdown/text + metadata
  -> chunks
  -> local embeddings
  -> turbopuffer namespace
  -> hybrid retrieval with citations
```

## Default crawl policy

- Prefer sitemap discovery first.
- Fall back to same-domain link crawling if sitemaps are absent or incomplete.
- Obey robots.txt by default.
- Restrict to the base URL host/domain unless the user approves otherwise.
- Use conservative caps until the site shape is known:
  - `--max-pages 10` or `25` for smoke tests
  - `--max-chunks 100` or `200` for smoke tests
  - low concurrency, e.g. `2`
  - crawl delay, e.g. `0.25` to `1.0` seconds
- Use static HTTP fetching first. Escalate to browser rendering only when pages are empty or clearly JavaScript-dependent.

## Dry-run CLI

Run from the repository root:

```bash
uv run turbo-search crawl \
  --base-url "https://scrapling.readthedocs.io/en/latest/" \
  --max-pages 10 \
  --max-chunks 100 \
  --css-selector ".md-content__inner" \
  --json
```

Expected safety fields:

```json
{
  "dry_run": true,
  "turbopuffer_api_calls": false,
  "credentials_required": false
}
```

The CLI writes local generated Markdown pages under the requested `artifacts/...` output directory and chunks them with the existing `turbo_search.indexer` Markdown pipeline. `artifacts/` is gitignored. Use `--css-selector` when a docs site has clear main-content wrappers; this reduces nav/sponsor/sidebar noise before chunking.

## Metadata to preserve per page

At minimum:

- `url`
- `title`
- `status`
- `content_type`
- `source_hash`
- `crawl_timestamp`
- `fetcher` / crawl mode

Future production indexing should also consider:

- canonical URL
- final redirected URL
- HTTP headers relevant to cache validation, e.g. `etag` and `last-modified`
- sitemap source URL if discovered from sitemap
- crawl depth
- language

## Namespace naming

Use a deterministic, URL-derived candidate with a version suffix:

```text
site-<host-slug>-v1
```

Examples:

- `https://jellyfish.co/` -> `site-jellyfish-co-v1`
- `https://scrapling.readthedocs.io/en/latest/` -> `site-scrapling-readthedocs-io-v1`

Ask before creating/writing a namespace. Never delete or overwrite an existing namespace unless the user explicitly approves deletion/replacement.

## Live write sequence

Only after explicit user approval:

1. Run dry-run and inspect page/chunk counts.
2. Confirm namespace and write caps.
3. Retrieve `TURBOPUFFER_API_KEY` into shell memory only.
4. Set `TURBOPUFFER_REGION` and `TURBOPUFFER_NAMESPACE` in shell only.
5. Embed locally with `BAAI/bge-small-en-v1.5`.
6. Write batched rows with the same schema used by the Jellyfish prototype unless a cost-optimized schema has been approved.
7. Run one live retrieval smoke query, not a broad eval suite, unless approved.
8. Record evidence without secret values.

## Known gaps before productionizing

The current implementation is still dry-run only. A production generic site indexer still needs:

- live write workflow with explicit namespace approval and write caps
- resumable crawl manifests
- incremental recrawls based on source hash / HTTP cache metadata
- local content store for cost-optimized turbopuffer rows
- namespace lifecycle commands with explicit safety prompts
- retrieval config that can target arbitrary namespaces, not only Jellyfish defaults
