Status: recorded
Created: 2026-07-23
Updated: 2026-07-23
Relates-To: .10x/tickets/done/2026-07-22-add-database-relation-sources.md, .10x/specs/database-document-relation-indexing.md, .10x/specs/warehouse-relation-adapters.md

# Database relation sources validation

## What was observed

The completed DuckDB/BigQuery/Snowflake relation implementation passed the required default-environment contract and build checks after independent-review repairs.

- `git diff --check`: passed.
- `uv sync --locked`: resolved 154 and checked 106 packages.
- `PYTHONDONTWRITEBYTECODE=1 uv run python scripts/validate_ranking_contract.py`: passed; 13 datasets, 369 judgments, bundle SHA `5a79f58aaca87a2d4f7cbec68fdcfbbcbf041131821587f8aba74a86daca99d9`.
- `PYTHONDONTWRITEBYTECODE=1 uv run python scripts/c6_syntax_forecast.py validate`: passed; forecast SHA `d5199276c19ae89779287eaa90824ce1e1cc684a3f060899f02f65d976016243`.
- `PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q`: 600 tests passed in 66.205s. Output contained two established best-effort cleanup warnings and one upstream lxml deprecation warning.
- `uv build --out-dir /tmp/buoy-database-build`: built sdist and wheel successfully.
- `uv sync --extra bigquery`: succeeded with `google-cloud-bigquery==3.42.2`.
- `uv sync --extra snowflake`: succeeded with `snowflake-connector-python==4.7.1`.
- Final `uv sync --locked`: restored the 106-package default environment.

Focused development evidence recorded in child tickets includes 52-test repair, 259-test expanded, and 600-test full runs. Review confirmed official BigQuery 3.42.2 serializes the configured `jobTimeoutMs`.

## Procedure

Commands were run from `/Users/crlough/Code/personal/turbo-search.worktrees/database-relation-sources` on branch `work/database-relation-sources`, after all review repairs. Optional environments were resolved separately and the default locked environment restored afterward.

## What this supports

This supports source compatibility, fake-backed cloud adapters without default extras, CLI/catalog/ranking/provenance integration, lockfile resolution, packaging, and regression acceptance criteria.

## Limits

No live BigQuery, Snowflake, or turbopuffer call was made. Fake clients/connectors establish generated request and lifecycle behavior but cannot prove live service/account policy behavior. Cloud validation/acquisition uses separate read-only statements and can observe concurrent source changes; snapshot isolation across cloud statements is not claimed or required by the v1 specifications.
