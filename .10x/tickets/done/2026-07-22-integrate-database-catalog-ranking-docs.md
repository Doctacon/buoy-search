Status: done
Created: 2026-07-22
Updated: 2026-07-22
Parent: .10x/tickets/done/2026-07-22-add-database-relation-sources.md
Depends-On: .10x/tickets/done/2026-07-22-refactor-shared-database-relation-core.md, .10x/tickets/done/2026-07-22-add-bigquery-snowflake-adapters.md

# Integrate database catalog, ranking, docs, and validation

## Scope

Extend database URI/catalog/generated semantics for all backends plus legacy DuckDB, add backend tags and manual precedence tests, make generated custom database namespaces receive page defaults via verified source kind while preserving prefix fallback/categories, update README/indexing/catalog/retrieval and upstream transformation examples, update lockfile, run/fix complete required validation.

## Exclusions

Live warehouse/turbopuffer calls, unrelated cleanup, changing existing non-database ranking defaults.

## Acceptance criteria

Catalog scheme/kind validation and deterministic semantics pass; custom namespace database defaults pass; docs cover all requested architecture/auth/cost/timeout/identity/provenance/non-goals; `uv sync --locked`, contract scripts, full unittest discovery, diff check, and build pass; optional extras are attempted when network permits and reported exactly.

## Evidence expectations

Record exact commands/counts/results and any environmental limitation. Request independent review before parent closure.

## Progress and notes

- 2026-07-22: Opened from ratified specs.
- 2026-07-22: Extended kind-aware catalog URI validation to the strict host-only `duckdb://`, `bigquery://`, and `snowflake://` forms. Generated semantics now accept all three verified low-level relation kinds, use fixed generic database metadata, retain legacy DuckDB-only metadata support, emit deterministic backend tags/summaries, and preserve manual semantics during later generated merges. Added catalog coverage for schemes, kind mismatches, malformed URIs, all backend semantics/tags, legacy DuckDB, and manual precedence.
- 2026-07-22: Added `bigquery-` and `snowflake-` prefix defaults and an optional verified `source_kind` input to ranking selection. Generated plan/apply/catalog paths pass the verified high-level kind, so custom database namespaces use page/none/pool20/max while explicit retrieval retains prefix fallback and GitHub/non-database behavior remains unchanged. Added focused ranking and custom-namespace plan tests.
- 2026-07-22: Updated README and indexing/catalog/retrieval guides for the shared relation contract, DuckDB/BigQuery/Snowflake commands, optional installation, ADC and named-connection authentication, BigQuery dry-run/cost limits, Snowflake tagging/timeouts, stable identity/provenance, saved-plan isolation, self-contained DuckDB views, upstream Gong transformations with backend syntax, ranking/catalog behavior, and v1 non-goals.
- 2026-07-22: Initial full discovery found two regressions: bare `crawl` no longer failed before the removed-environment gate, and README exceeded its enforced 100-line limit. Added conditional early crawl source validation without blocking pathless remote database commands and compressed README to 93 lines. Focused regression command `PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_environment_alias_removal tests.test_release_automation -q` passed 35 tests in 3.295s.
- 2026-07-22: Focused database/catalog/retrieval validations passed: 48 adapter/shared/CLI tests in 1.434s, 108 catalog/retriever/apply/database CLI tests in 2.007s, and the final catalog/retriever/database CLI set passed 54 tests in 0.081s. `git diff --check` passed and no files are staged.
- 2026-07-22: Required validation passed. `uv sync --locked` resolved 154 and checked 106 packages. Ranking-contract validation emitted 13 datasets, 369 judgments, and bundle SHA `5a79f58aaca87a2d4f7cbec68fdcfbbcbf041131821587f8aba74a86daca99d9`. C6 validation emitted valid forecast SHA `d5199276c19ae89779287eaa90824ce1e1cc684a3f060899f02f65d976016243`. Final default locked-environment discovery passed 591 tests in 66.567s; output contained only two established best-effort cleanup warnings and one upstream lxml deprecation warning. `uv build --out-dir dist` built the sdist and wheel successfully.
- 2026-07-22: Optional resolution succeeded without live service calls. `uv sync --extra bigquery` installed `google-cloud-bigquery==3.42.2` and dependencies; `uv sync --extra snowflake` installed `snowflake-connector-python==4.7.1` and dependencies. A final default `uv sync --locked` removed the optional packages and the complete default suite still passed. Implementation is complete within this child. Parent evidence and passing re-review are recorded at `.10x/evidence/2026-07-23-database-relation-sources-validation.md` and `.10x/reviews/2026-07-23-database-relation-sources-review.md`; closed.

- 2026-07-22: Closure repair reconciled Snowflake adapter identifiers with the catalog's strict shared v1 subset (no `$`) and made shared/database DuckDB URI validation match catalog host-only behavior by rejecting a trailing slash. Full default discovery passed 600 tests after repair.

## Blockers

None.
