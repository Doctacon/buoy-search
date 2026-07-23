Status: active
Created: 2026-07-22
Updated: 2026-07-22

# BigQuery and Snowflake Relation Adapters

## BigQuery behavior

Buoy MUST lazily import official `google-cloud-bigquery`, construct `bigquery.Client(project=optional_query_project, location=optional_location)` through ADC, inspect table/view schema, validate mappings, and generate read-only Standard SQL with safely backtick-quoted identifiers and text conversion. It MUST run an official dry run of exact generated source queries before execution, report estimated bytes, enforce `--bigquery-maximum-bytes-billed` before execution and on actual job configuration where supported, attach Buoy operation labels, honor `--source-query-timeout`, return at most `max_pages` ordered nonblank documents, and avoid downloading all rows. It MUST report non-secret available bytes/cache/job diagnostics without putting volatile diagnostics, billing project, location, ADC source, or credentials into deterministic artifacts. `max_pages` is not guaranteed to cap scan cost. Missing SDK error MUST direct `uv sync --extra bigquery`.

## Snowflake behavior

Buoy MUST lazily import official `snowflake.connector`, connect only via `connection_name`, apply a Buoy/source query tag and supported statement timeout, inspect tables/views without mutation, validate/canonicalize relation and mappings, and generate read-only SQL with uppercase double-quoted ordinary identifiers and text conversion. Acquisition MUST validate IDs/count blanks globally, order by converted ID, limit rows returned, use bounded `fetchmany()`, report non-secret query ID/elapsed time, and close cursor/connection on every path. Connection profile, account, user, role, warehouse, tokens, passwords, and key paths MUST never serialize. Missing SDK error MUST direct `uv sync --extra snowflake`.

## Authentication and operations

Remote `plan` and `crawl` authenticate only to the selected source warehouse and make source API calls. They MUST NOT read turbopuffer credentials, load embeddings from a remote service, or write turbopuffer. BigQuery accepts only optional billing/query project, location, bytes cap, and timeout controls. Snowflake accepts only required named connection and timeout. No password/token/private-key/account/user CLI controls are permitted.

## Failure scenarios

Schema/relation/mapping validation, null/blank IDs, duplicate converted IDs, all-empty content, dry-run cap breach, timeout, and backend diagnostics MUST fail clearly before a successful plan. Generated SQL MUST contain no DDL/DML. Tests MUST use fake lazy modules/clients/jobs/connectors/cursors and MUST prove apply does not construct/import/connect to adapters.
