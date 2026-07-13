Status: recorded
Created: 2026-07-12
Updated: 2026-07-12
Relates-To: .10x/tickets/done/2026-07-12-duckdb-state-apply-lock-integration.md, .10x/specs/compact-duckdb-applied-state.md

# DuckDB Apply Lock Integration Validation

## What was observed

- Approved apply now obtains a non-blocking cross-platform `portalocker` file lock at the matching per-namespace state path before constructing a writer, loading embeddings, or performing Turbopuffer work.
- A contended lock produces a clear error before `TurbopufferWriter` construction.
- Different namespace paths have independent lock files.
- After mocked remote success, the current DuckDB ledger and exactly one `ApplyRunSummary` are saved together; the summary uses the matching apply ID and actual write/delete/retained-row counts.
- Mocked upsert and deletion failures leave the existing state and compact history unchanged, including a seeded prior `ApplyRunSummary`.

## Procedure

1. Ran focused apply, state, and diff tests, including a cross-process same-namespace lock contention test through the cross-platform lock dependency.
2. Ran the full test suite.
3. Checked whitespace and verified no staged files.

## Results

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_apply_cli tests.test_applied_state tests.test_plan_diff -q
Ran 39 tests in 1.711s
OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 186 tests in 4.909s
OK

git diff --check
OK

git diff --cached --quiet
no staged files
```

## What this supports or challenges

Supports the ticket's cross-platform fail-fast lock and state-commit contract without contacting Turbopuffer. Existing plan/apply preflight tests remain local-only and pass.

## Limits

Mocked writer tests cannot prove behavior of a real network interruption after a successful remote write but before the local DuckDB transaction. The existing recovery model remains a later explicit apply safely repeating upserts.
