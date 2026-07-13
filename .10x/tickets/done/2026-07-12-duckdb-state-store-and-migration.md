Status: done
Created: 2026-07-12
Updated: 2026-07-12
Parent: .10x/tickets/done/2026-07-12-compact-duckdb-applied-state-plan.md
Depends-On: None

# DuckDB State Store and Migration

## Scope

Implement the per-namespace DuckDB applied-state store and archive-and-reset migration from legacy JSON state.

## Acceptance criteria

- Add the local open-source DuckDB dependency and a versioned schema at `<state-root>/state/<site-id>/<namespace>/state.duckdb`.
- Implement current-row reads/writes and lightweight append-only apply summaries without full row snapshots.
- Preserve existing `AppliedState`/diff semantics at the domain boundary or make equivalent callers/tests explicit.
- When legacy `last-applied.json` exists and no DuckDB state exists, archive JSON without importing it; active DuckDB state is empty and behaves as first apply.
- Migration is local-only and idempotent.

## Explicit exclusions

- Apply locking, remote writer integration, Quack, plan artifact compaction, and remote operations.

## References

- `.10x/specs/compact-duckdb-applied-state.md`
- `.10x/decisions/superseded/duckdb-applied-state-concurrency.md`
- `src/turbo_search/applied_state.py`
- `src/turbo_search/plan_diff.py`
- `tests/test_applied_state.py`
- `tests/test_plan_diff.py`

## Evidence expectations

Unit tests covering first apply, legacy archive/reset, idempotent migration, state validation, and diff parity against representative fixtures.

## Progress and notes

- 2026-07-12: Opened from ratified storage contract; not yet authorized for implementation.
- 2026-07-12: Implementation authorized; assigned to a single worker.
- 2026-07-12: Added `duckdb==1.5.4`; replaced JSON persistence with a per-namespace `state.duckdb` store, current-row ledger, optional append-only apply summaries, and local archive-and-reset legacy migration. Updated state-path metadata and focused tests. Validation is recorded in `.10x/evidence/2026-07-12-duckdb-state-store-and-migration.md`.
- 2026-07-12: Independent review raised two state-integrity findings; both were repaired and passed re-review in `.10x/reviews/2026-07-12-duckdb-state-store-rereview.md`. Focused tests: 78 passed. Full suite: 182 passed.
- 2026-07-12: Addressed independent-review integrity findings: apply summaries must match `last_apply_id`, and nonempty row tables without exactly one metadata row now fail instead of being treated as first apply. Targeted, focused, and full suites passed; evidence updated.

## Blockers

- None.
