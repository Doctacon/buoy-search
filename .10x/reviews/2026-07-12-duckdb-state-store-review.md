Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Target: .10x/tickets/done/2026-07-12-duckdb-state-store-and-migration.md
Verdict: concerns

# DuckDB State Store Review

## Findings

1. **Significant — `src/turbo_search/applied_state.py` `_validate_apply_run`:** an apply summary's `apply_id` is not required to equal the current state's `last_apply_id`. This permits inconsistent current-state metadata and retained history.
2. **Significant — `src/turbo_search/applied_state.py` `load_applied_state`:** a schema-valid database with current rows but no metadata is treated as first apply. It must fail as corrupt state rather than suppressing the existing row ledger.

## Verdict

Concerns raised. The state-store ticket cannot close until both findings have targeted regression tests and are repaired.

## Residual risk

Legacy JSON archives deliberately remain recoverable and are not active state. Historical-artifact garbage collection is explicitly outside this ticket's scope.
