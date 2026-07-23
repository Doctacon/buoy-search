Status: done
Created: 2026-07-22
Updated: 2026-07-22
Parent: .10x/tickets/done/2026-07-22-add-database-relation-sources.md
Depends-On: None

# Refactor shared database relation core

## Scope

Inspect current DuckDB/source/plan pipeline; extract a small shared database relation materialization layer; preserve all public DuckDB names, commands, identities, saved-plan behavior, and legacy metadata; add fixed generic provenance through Markdown, manifests, chunks, and turbopuffer row whitelist; replace total-ID Python retention with consistent-transaction backend aggregate validation plus limited deterministic query.

## Exclusions

Cloud adapters/CLI, catalog/retrieval/docs, broad plugin architecture, plan schema bump, arbitrary metadata.

## Acceptance criteria

Existing DuckDB tests remain passing; new shared tests cover identities/filenames/frontmatter scalar fidelity/title fallback/provenance/caps/counts; DuckDB global validation/counts remain exact without total-ID memory; apply remains source-independent.

## Evidence expectations

Run focused DuckDB/shared/chunker/plan/apply tests; record exact results in progress.

## Progress and notes

- 2026-07-22: Opened from ratified specs.
- 2026-07-22: Extracted `database_relation.py` as the backend-independent identity, document/count model, Markdown materialization, summary, and `process_corpus()` handoff layer. DuckDB public entry points and legacy metadata remain compatible while new pages/summaries include fixed generic database provenance and source-vs-turbopuffer activity fields.
- 2026-07-22: Replaced DuckDB's full ordered row scan and Python ID set with aggregate global ID/content validation, one duplicate sample query, and a deterministic nonblank document query with backend `LIMIT`, all inside the existing single read-only transaction and safe connection configuration. Added a 5,000-row regression that observes the limited selection query and exact global counts.
- 2026-07-22: Added generic provenance to manifest/chunk propagation, the fixed turbopuffer schema, and `build_generic_site_row()` whitelist. Added shared backend identity, percent-encoding, stable filename, Unicode/scalar round-trip, count/cap, and schema tests; expanded DuckDB CLI coverage through generated manifests/chunks/content rows.
- 2026-07-22: Focused validation `PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_database_relation tests.test_duckdb_relation tests.test_duckdb_relation_cli tests.test_chunker tests.test_plan_artifacts tests.test_apply_cli -q` passed 98 tests in 2.217s. `PYTHONDONTWRITEBYTECODE=1 uv run python -m py_compile ...` and `git diff --check` passed. No files are staged. Implementation is complete within this child scope; parent evidence and passing re-review are recorded at `.10x/evidence/2026-07-23-database-relation-sources-validation.md` and `.10x/reviews/2026-07-23-database-relation-sources-review.md`; closed.

- 2026-07-22: Closure repair after independent review restored Python `str.strip()`-equivalent Unicode whitespace semantics in DuckDB aggregate validation using an explicit fixed character set, rejected trailing-slash database base URIs, and restored `DuckDBScanResult(rows_scanned=...)` constructor compatibility while retaining `rows_discovered`. Added actual DuckDB Unicode whitespace and compatibility regressions.

## Blockers

None.
