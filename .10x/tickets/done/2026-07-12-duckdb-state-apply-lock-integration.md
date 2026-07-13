Status: done
Created: 2026-07-12
Updated: 2026-07-12
Parent: .10x/tickets/done/2026-07-12-compact-duckdb-applied-state-plan.md
Depends-On: .10x/tickets/done/2026-07-12-duckdb-state-store-and-migration.md

# DuckDB State Apply Lock Integration

## Scope

Integrate the DuckDB state store into plan/apply paths and add fail-fast locks scoped to one `(site_id, namespace)` approved apply.

## Acceptance criteria

- Plan and apply preflight read DuckDB state and preserve local-only behavior.
- Approved apply acquires a non-blocking namespace-scoped exclusive lock before embedding or Turbopuffer writes.
- A contending same-namespace apply fails before writer construction/call and leaves local state unchanged.
- Different namespace paths use independent locks and can proceed concurrently.
- Only successful approved remote work commits current rows and one summary in an atomic local DuckDB transaction.
- Remote failure leaves current rows and apply-run history unchanged.

## Explicit exclusions

- Quack, global locks, same-namespace parallel writers, remote namespace lifecycle, and plan-artifact compaction.

## References

- `.10x/specs/compact-duckdb-applied-state.md`
- `.10x/decisions/superseded/duckdb-applied-state-concurrency.md`
- `src/turbo_search/cli.py`
- `src/turbo_search/apply.py`
- `tests/test_apply_cli.py`
- `tests/test_cli.py`

## Evidence expectations

Focused mocked remote success/failure tests, lock contention tests, different-namespace concurrency tests, and preflight regression tests.

## Progress and notes

- 2026-07-12: Opened from ratified concurrency contract; not yet authorized for implementation.
- 2026-07-12: Dependency completed and implementation authorized; assigned to a single worker.
- 2026-07-12: Added per-namespace non-blocking advisory locks around approved apply and populated atomic DuckDB apply summaries after mocked remote success. Added contention, namespace independence, summary, and failure-preservation tests. Evidence: `.10x/evidence/2026-07-12-duckdb-state-apply-lock-integration.md`. Focused tests: 38 passed; full suite: 185 passed.
- 2026-07-12: Independent review raised cross-platform lock portability and existing-history preservation concerns. Replaced the POSIX-only implementation with `portalocker`, added seeded-history failure coverage, and passed re-review. Focused tests: 39 passed; full suite: 186 passed.
- 2026-07-12: Review follow-up replaced POSIX-only `fcntl` with cross-platform `portalocker` and added a regression test proving a failed subsequent apply preserves a seeded current ledger and prior apply summary. Focused tests: 39 passed; full suite: 186 passed.

## Blockers

- None.
