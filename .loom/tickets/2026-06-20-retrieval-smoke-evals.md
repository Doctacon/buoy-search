Status: blocked
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-turbopuffer-jellyfish-rag-plan.md
Depends-On: .loom/tickets/2026-06-20-jellyfish-markdown-indexer.md, .loom/tickets/2026-06-20-turbopuffer-hybrid-retrieval-client.md, .loom/specs/turbopuffer-jellyfish-rag.md

# Add retrieval smoke tests and lightweight evals

## Scope

Create a lightweight evaluation harness to confirm that turbopuffer hybrid retrieval works for representative questions about the Jellyfish docs corpus.

In scope:

- A small set of hand-authored smoke/eval questions.
- Expected URL/topic hints for each question.
- A command to run retrieval for all evals and summarize whether expected sources appear in top-k.
- Evidence capture after eval execution.
- Optional comparison of vector-only, BM25-only, and hybrid/RRF results.

Out of scope:

- A full production relevance benchmark.
- Automated LLM grading.
- Proprietary reranking services.

## Acceptance criteria

- At least 5 smoke questions run successfully against the indexed namespace.
- Results include relevant Jellyfish source URLs/titles in top-k for most smoke questions.
- The eval report makes failures visible and actionable.
- Evidence is recorded under `.loom/evidence/` after running evals.

## Candidate smoke questions

- "What does Jellyfish say about measuring developer productivity?"
- "What are DORA metrics according to Jellyfish?"
- "What does Jellyfish DevFinOps do?"
- "What integrations does Jellyfish mention for Claude Code or Cursor?"
- "What does Jellyfish say about AI coding tool adoption?"

## Progress and notes

- 2026-06-20: Ticket created only. No evals run.

## Blockers

- User approval to implement and execute.
- Indexed namespace available.
- Retrieval client implemented.
