Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Target: .10x/tickets/done/2026-07-12-duckdb-state-apply-lock-integration.md
Verdict: concerns

# DuckDB Apply Lock Integration Review

## Findings

1. **Significant — `src/turbo_search/applied_state.py`:** the unconditional POSIX-only `fcntl` import prevents the CLI from importing on Windows despite the package declaring general Python support. Replace it with a cross-platform lock implementation or explicitly constrain supported platforms.
2. **Minor — `tests/test_apply_cli.py`:** failure tests check empty apply history but do not prove that a failed later apply preserves an existing compact apply summary. Add a seeded-history regression test.

## Verdict

Concerns raised. Do not close the integration ticket until the portability blocker and history-preservation test gap are resolved.

## Residual risk

No real Turbopuffer call was run. The designed crash-after-remote-write recovery remains an explicitly approved repeat-upsert path.
