Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Relates-To: .10x/tickets/done/2026-07-12-duckdb-state-store-and-migration.md, .10x/specs/compact-duckdb-applied-state.md

# DuckDB State Store and Migration Validation

## What was observed

- `uv add duckdb` added the open-source `duckdb==1.5.4` dependency and updated `uv.lock`.
- `AppliedState` continues to be the in-memory domain boundary used by incremental diffing. Its persisted backend is now `<state-root>/state/<site-id>/<namespace>/state.duckdb`.
- A DuckDB state file contains `state_schema`, `state_metadata`, `applied_rows`, and `apply_runs`; current rows are replaced transactionally while apply summaries append only when supplied.
- A legacy `last-applied.json` is moved to `legacy-json/last-applied.json` and creates an empty DuckDB database. The first subsequent state load reports `first_apply=True` and no rows.
- No `history/` directory or per-apply full row snapshot is written by the new state store.
- Review follow-up: an apply summary now must use the exact `last_apply_id` recorded in the current state; mismatches are rejected before any write.
- Review follow-up: an empty or duplicated `state_metadata` table cannot cause a nonempty `applied_rows` table to be treated as first apply; it raises `AppliedStateError` instead.

## Procedure

1. Ran targeted state-integrity tests after the review follow-up.
2. Ran focused state/diff/artifact/CLI/apply tests.
3. Ran the complete unit suite.
4. Checked the diff for whitespace errors and verified the index contains no staged files.

## Results

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_applied_state -q
Ran 11 tests in 1.192s
OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_applied_state tests.test_plan_diff tests.test_plan_artifacts tests.test_cli tests.test_apply_cli -q
Ran 78 tests in 1.355s
OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 182 tests in 4.680s
OK

git diff --check
OK

git diff --cached --quiet
no staged files
```

## What this supports or challenges

Supports the storage/migration ticket's local-only acceptance criteria: compact per-namespace database paths, legacy archive-and-reset migration, current-row persistence, summary-only history support, unchanged domain-level diff inputs, apply-run/state identity integrity, and corruption-safe first-apply detection.

The apply path has not yet supplied exact `ApplyRunSummary` counts or a namespace lock. Those explicitly belong to `.10x/tickets/done/2026-07-12-duckdb-state-apply-lock-integration.md`.

## Limits

No Turbopuffer operation was invoked. This evidence does not prove remote/local transaction coordination, same-namespace contention behavior, or disk-size reduction against the existing 495 MB state corpus; those require the dependent integration/validation tickets.
