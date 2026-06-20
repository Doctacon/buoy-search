Status: blocked
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-turbopuffer-jellyfish-rag-plan.md
Depends-On: .loom/tickets/2026-06-20-python-prototype-scaffold.md, .loom/tickets/2026-06-20-proton-pass-turbopuffer-config.md, .loom/specs/turbopuffer-jellyfish-rag.md, .loom/research/2026-06-20-turbopuffer-markdown-rag-research.md, .loom/evidence/2026-06-20-jellyfish-site-docs-inventory.md

# Implement Jellyfish Markdown indexer

## Scope

Implement the pipeline that reads `jellyfish-site-docs/`, chunks pages, embeds chunks, and writes them to turbopuffer.

In scope:

- Recursive Markdown discovery.
- YAML frontmatter parsing for `url`, `title`, and future metadata if present.
- Content normalization to reduce repeated site chrome/boilerplate.
- Markdown-aware chunking with title/heading context and overlap.
- Deterministic chunk ID generation.
- Local BGE embeddings with `BAAI/bge-small-en-v1.5` unless user chooses otherwise.
- Turbopuffer batched upserts with schema for vector + BM25 + citation/debug attributes.
- Dry-run mode that reports files/chunks without writing.
- Index summary output: files seen, files skipped, chunks generated, rows written, errors.

Out of scope:

- Answer synthesis.
- Production continuous sync.
- Proprietary embedding providers.
- Reranking.

## Acceptance criteria

- Dry run can process all 1124 observed Markdown files and report a chunk count.
- Real run can write chunks to the configured namespace using `TURBOPUFFER_API_KEY` without exposing the key.
- Namespace schema enables ANN on `vector` and full-text search on `content`, `title`, and `section_path`.
- Chunk rows include citation fields `title`, `url`, `section_path`, and local `path`.
- Re-running the indexer is deterministic and does not create duplicate logical chunks.
- The indexer handles empty/malformed files gracefully and reports them.

## Implementation notes

Recommended row attributes:

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

Start with approximately 300-token chunks and two-sentence overlap, respecting Markdown headings and avoiding splits inside obvious blocks where practical.

## Progress and notes

- 2026-06-20: Ticket created only. No indexing run. No turbopuffer writes.

## Blockers

- User approval to implement and execute.
- Scaffold ticket complete.
- Config/credential ticket complete for real writes; dry-run can proceed after scaffold if approved.
