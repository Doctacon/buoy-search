Status: blocked
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-turbopuffer-jellyfish-rag-plan.md
Depends-On: .loom/tickets/2026-06-20-python-prototype-scaffold.md, .loom/tickets/2026-06-20-proton-pass-turbopuffer-config.md, .loom/specs/turbopuffer-jellyfish-rag.md, .loom/research/2026-06-20-turbopuffer-markdown-rag-research.md

# Implement turbopuffer hybrid retrieval client

## Scope

Implement the query-side client/CLI that retrieves relevant Jellyfish docs chunks using turbopuffer hybrid search.

In scope:

- Load same local embedding model used by the indexer.
- Embed the user's query.
- Run `ns.multi_query(...)` with:
  - ANN vector subquery over `vector`.
  - BM25 subquery over boosted `title`, `section_path`, and `content`.
- Use turbopuffer RRF via `rerank_by=("RRF",)` where supported.
- Provide a local client-side RRF fallback if the installed SDK does not return the expected fused result shape.
- Return structured JSON/text with top chunks and citations.
- Support flags for top-k/candidate limits and optional filters such as `doc_kind`.

Out of scope:

- Index creation.
- LLM answer generation.
- Proprietary hosted rerankers.

## Acceptance criteria

- Retrieval command accepts a question string and prints top chunks with `title`, `url`, `section_path`, `content`, and score information.
- The command does not return vectors by default.
- The implementation performs both vector and BM25 retrieval in a single turbopuffer multi-query request.
- RRF fusion is used and verified in output or tests.
- Retrieval failures produce user-friendly messages with likely fixes, e.g. missing env vars or empty namespace.

## Implementation notes

Candidate BM25 expression:

```python
("Sum", [
    ("Product", 2.0, ("title", "BM25", query)),
    ("Product", 1.5, ("section_path", "BM25", query)),
    ("content", "BM25", query),
])
```

Candidate multi-query:

```python
response = ns.multi_query(
    queries=[
        {"rank_by": ("vector", "ANN", query_vector), "limit": candidates, "include_attributes": attrs},
        {"rank_by": bm25_rank_by, "limit": candidates, "include_attributes": attrs},
    ],
    rerank_by=("RRF",),
)
```

SDK response shape should be verified during implementation against installed `turbopuffer` version.

## Progress and notes

- 2026-06-20: Ticket created only. No retrieval run.

## Blockers

- User approval to implement and execute.
- Scaffold ticket complete.
- Config ticket complete for real queries.
- Indexed namespace needed for end-to-end validation.
