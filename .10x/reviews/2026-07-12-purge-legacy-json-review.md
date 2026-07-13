Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Target: .10x/tickets/done/2026-07-12-purge-legacy-json-during-duckdb-migration.md
Verdict: concerns

# Purge Legacy JSON Migration Review

## Findings

1. **Significant — `src/turbo_search/applied_state.py` migration ordering:** legacy JSON is deleted before the empty DuckDB ledger is successfully initialized. A DuckDB initialization failure can leave neither active state nor legacy input. Initialize and validate the empty ledger before deleting legacy JSON; add a regression test for initialization failure.

## Verdict

Concerns raised. The destructive migration ticket cannot close until the no-loss ordering is repaired.

## Residual risk

No remote operation was run; existing historical `history/` snapshots remain outside this ticket.
