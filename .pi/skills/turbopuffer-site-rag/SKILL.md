---
name: turbopuffer-site-rag
description: Build, operate, or query turbopuffer-backed RAG indexes for websites. Use for the existing Jellyfish docs namespace, future Scrapling crawls, dry-run crawl/index validation, namespace planning, retrieval with citations, and cost-safe guardrails around turbopuffer writes.
---

# Turbopuffer Site RAG

This skill captures the working Jellyfish/turbopuffer RAG workflow and the planned generic Scrapling-based website workflow.

## Non-negotiable guardrails

- Do **not** persist API keys, Proton Pass output, tokens, private vault names, private item titles, or share IDs to disk.
- Do **not** run live turbopuffer writes, namespace deletion, namespace replacement, or live evals unless the user explicitly approves that action in the current conversation.
- Default all crawl/index commands to dry-run/local-only.
- Use open-source/local components where practical:
  - local embeddings: `BAAI/bge-small-en-v1.5`
  - scraper/crawler: Scrapling
  - package manager: `uv`
- Respect crawl ethics by default: same-site only, `robots_txt_obey = True`, conservative concurrency, crawl delay, and no paywall/auth/protection bypass unless explicitly authorized.
- When answering from a site index, retrieve context first and cite retrieved page titles/URLs.

## Existing Jellyfish namespace

Use this when the user asks Jellyfish questions or asks about the current live prototype.

- Turbopuffer region: `gcp-us-central1`
- Namespace: `jellyfish-site-docs-v1`
- Rows/chunks indexed: `12,721`
- Embedding model: `BAAI/bge-small-en-v1.5`
- Vector type: `[384]f16`
- Retrieval: local query embedding + turbopuffer hybrid `multi_query` with ANN + boosted BM25 + RRF.
- Corpus source: `jellyfish-site-docs/`

See [Jellyfish namespace reference](references/jellyfish-namespace.md) for exact credential and retrieval workflow.

## Generic Scrapling site workflow

Use this when building or testing the “base URL → crawl → chunks → namespace → search” workflow.

1. Start with a base URL.
2. Derive a stable namespace slug from the URL.
3. Crawl same-site pages with Scrapling:
   - prefer `robots.txt` / sitemap discovery first
   - fall back to same-domain link crawling when needed
   - obey robots.txt and apply low concurrency/delay
4. Extract clean Markdown/text plus metadata:
   - `url`, canonical URL when known
   - `title`
   - crawl timestamp
   - source hash
   - content type/status
5. Chunk using the existing Markdown chunking path.
6. Dry-run by default: print counts, sample chunks, and a namespace candidate.
7. Only with explicit approval: embed locally and write chunks to the planned namespace.
8. Search with the same hybrid retrieval/citation pattern as Jellyfish.

See [Scrapling site workflow](references/scrapling-site-workflow.md) for commands and design notes.

## Dry-run Scrapling crawler

Prefer the first-class CLI from the repository root:

```bash
uv run turbo-search crawl \
  --base-url "https://scrapling.readthedocs.io/en/latest/" \
  --max-pages 10 \
  --max-chunks 100 \
  --css-selector ".md-content__inner" \
  --json
```

This command must report `dry_run: true` and `turbopuffer_api_calls: false`.

The older local-only helper remains at `scripts/scrapling_dry_crawl.py` for skill-level experimentation, but production workflow should use `turbo-search crawl`.

## Live write checklist

Only proceed if the user explicitly asks for a live namespace/index write.

1. Confirm base URL, namespace name, crawl cap, and write cap.
2. Confirm whether existing namespace deletion/replacement is allowed. Default: no deletion.
3. Retrieve turbopuffer API key into shell memory only.
4. Set env vars in the current shell only:

```bash
export TURBOPUFFER_REGION=gcp-us-central1
export TURBOPUFFER_NAMESPACE=<approved-namespace>
export TURBOPUFFER_API_KEY=<from Proton Pass, do not print>
```

5. Run a dry-run first and inspect counts/samples.
6. Run the explicit write command only after the dry-run looks correct.
7. Record evidence with counts and command shape, never secret values.
