Status: open
Created: 2026-06-20
Updated: 2026-06-20
Parent: .loom/tickets/2026-06-20-generic-site-rag-incremental-plan-apply.md
Depends-On: .loom/tickets/2026-06-20-plan-artifact-manifest-model.md, .loom/tickets/2026-06-20-generic-site-stable-row-ids-and-schema.md, .loom/tickets/2026-06-20-local-applied-state-store.md, .loom/specs/generic-site-rag-incremental-plan-apply.md

# Incremental Plan Diff Engine

## Scope

Implement the pure local diff engine that compares a desired plan manifest to local applied state.

In scope:

- First-apply diff when no previous state exists.
- Classify desired chunks as unchanged, new, or changed.
- Classify previous rows absent from desired manifest as stale.
- Preserve retained-stale rows in diff output until deleted.
- Produce page-level counts: added, changed, unchanged, removed.
- Produce chunk/row counts: unchanged, needs embedding, rows to upsert, stale rows, retained stale rows.
- Return enough structured detail for apply to embed/upsert/delete exact row IDs.
- Tests using hand-authored manifests and states.

Out of scope:

- Crawling/extraction.
- Embedding model calls.
- Turbopuffer API calls.
- CLI rendering beyond returning a structured summary.

## Implementation notes

The diff engine should not require network access. It should be deterministic and easy to test.

Suggested semantics:

- Desired row ID + same embedding text hash in active state => unchanged.
- Desired row not found in active state => needs embedding/upsert.
- Prior active row not found in desired rows => stale.
- Prior retained-stale row still not desired => retained stale.
- Prior retained-stale row becoming desired again should be handled deliberately, likely as active/upsert if hashes require it.

Changed chunks may appear as old row stale + new row upsert if row ID includes chunk hash. That is acceptable as long as the plan clearly reports changed/stale/upsert counts.

## Acceptance criteria

- First apply reports all desired chunks as needing embedding/upsert and zero stale rows.
- No-change second plan reports zero embeddings/upserts and zero stale rows.
- Changed chunk reports one upsert and the old row as stale or changed according to the implemented model.
- Removed page reports its rows as stale.
- Retained stale rows remain visible on future plans until deleted.
- Diff output includes both human summary counts and machine-readable row lists for apply.
- Tests cover the above scenarios.

## Progress and notes

- 2026-06-20: Ticket opened as Phase 1 foundation.

## Blockers

Depends on plan/manifest model, stable row IDs, and local state model.
