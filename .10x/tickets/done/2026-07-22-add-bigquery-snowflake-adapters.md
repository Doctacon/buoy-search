Status: done
Created: 2026-07-22
Updated: 2026-07-22
Parent: .10x/tickets/done/2026-07-22-add-database-relation-sources.md
Depends-On: .10x/tickets/done/2026-07-22-refactor-shared-database-relation-core.md

# Add BigQuery and Snowflake adapters

## Scope

Implement lazy official BigQuery and Snowflake readers, identifier/schema safety, global aggregate validation, deterministic limited acquisition, dry-run/cost labels/timeout diagnostics, named Snowflake connections/query tags/timeouts/batched fetch/cleanup, backend models, plan/crawl CLI dispatch and validation, truthful source-vs-turbopuffer summaries, optional dependencies and fake-backed tests.

## Exclusions

Live calls, credential CLI fields, arbitrary SQL, catalog/ranking/docs, new apply source logic, non-goal databases/features.

## Acceptance criteria

Both remote table/view paths implement the shared contract; invalid combinations/identifiers fail; SDKs remain optional/lazy; no secret/connection leakage; saved-plan apply neither imports nor connects; focused fake-backed adapter and CLI tests pass.

## Evidence expectations

Run adapter/CLI/apply tests without optional SDKs or credentials and record exact results.

## Progress and notes

- 2026-07-22: Opened from ratified specs.
- 2026-07-22: Implemented lazy official-client BigQuery and Snowflake relation sources over the shared database materialization core. BigQuery now uses ADC-style client construction, schema inspection, strict three-part identifier validation, dry runs for all generated read-only queries, aggregate cost-cap enforcement plus actual job caps, operation labels, result timeouts, deterministic limited acquisition, and non-secret job statistics. Snowflake now uses named connections only, canonical uppercase identifiers, read-only schema/aggregate/limited queries, query tags, session and execute timeouts, bounded `fetchmany()`, and reliable rollback/cursor/connection cleanup.
- 2026-07-22: Added `--database-backend`, BigQuery billing/location/bytes controls, Snowflake named connection, remote query timeout, conditional local path rules, exact backend-flag validation, explicit-empty mapping rejection, lazy dispatch for both `plan` and `crawl`, remote source-vs-turbopuffer activity summaries, and source-independent logical plan metadata. Existing implicit and explicit DuckDB paths remain compatible. Extended internal database URI handling so BigQuery/Snowflake plans use stable site/namespace identities without changing apply source logic.
- 2026-07-22: Added optional `bigquery` and `snowflake` project extras and updated `uv.lock` through normal `uv run` resolution. Added fake-backed adapter and CLI tests for identities, safety, tables/views via schema inspection, mappings/title fallback, generated SQL, dry-run cap, labels/timeouts, query statistics, global failures, resource cleanup, missing dependencies, plan/crawl dispatch, invalid combinations, artifact leakage, truthful summaries, and verified saved-plan loading without source access.
- 2026-07-22: Final focused command `PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_bigquery_relation tests.test_snowflake_relation tests.test_database_relation_cli -q` passed 22 tests in 0.057s. Final expanded command `PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_database_relation tests.test_bigquery_relation tests.test_snowflake_relation tests.test_database_relation_cli tests.test_duckdb_relation tests.test_duckdb_relation_cli tests.test_cli tests.test_crawler tests.test_apply_cli -q` passed 192 tests in 8.753s with two pre-existing best-effort cleanup warnings. Targeted `py_compile`, `git diff --check`, and the no-staged-files check passed. The fake-backed BigQuery plan also verifies and completes `apply --dry-run` while both source loaders are configured to fail on access. Implementation is complete within this child scope; catalog/ranking/docs/full regression were completed by child 3. Parent evidence and passing re-review are recorded at `.10x/evidence/2026-07-23-database-relation-sources-validation.md` and `.10x/reviews/2026-07-23-database-relation-sources-review.md`; closed.

- 2026-07-22: Closure repair after independent review added BigQuery's official `job_timeout_ms` server-side job configuration plus client timeout cancellation, explicit client cleanup, and redacted SDK diagnostics; removed eager adapter imports from CLI/crawler so apply CLI import does not load any database adapter; made timeout validation finite; aligned Snowflake with the shared strict identifier subset, rejected quoted mixed-case schema columns, used explicit Python-strip-equivalent whitespace characters, and redacted SDK diagnostics. Focused fake-backed regressions cover each boundary.
- 2026-07-22: Repair validation passed 52 focused tests in 1.830s and full default discovery passed 600 tests in 70.008s after `uv sync --locked`; only two established cleanup warnings and one upstream lxml deprecation warning were emitted.

## Blockers

None.
