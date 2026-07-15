Status: recorded
Created: 2026-07-14
Updated: 2026-07-14
Relates-To: .10x/tickets/done/2026-07-14-add-namespace-discovery-command.md, .10x/specs/turbopuffer-namespace-discovery.md

# Namespace Discovery Command Validation

## What was observed

`buoy namespaces [SEARCH]` now performs only the Turbopuffer namespace-list operation, consumes the returned auto-paginating iterable, deduplicates and sorts IDs, and optionally filters them by case-insensitive substring. Text output is one ID per line or `No namespaces matched.`; JSON reports command, region, search, count, and IDs.

The API key is checked at command execution before SDK/client work. Region precedence is CLI, environment, then the existing default. SDK failures are converted to a user-actionable discovery error. The implementation does not instantiate an embedder, namespace content resource, query operation, or mutation operation.

## Procedure

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_namespaces -q
Ran 7 tests; OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 260 tests; OK

uv lock --check
Resolved 130 packages

uv build --out-dir /tmp/buoy-namespace-discovery-build
Built wheel and sdist

git diff --check
OK

git diff --cached --name-only
empty
```

Focused tests use a fake SDK/client and paginated iterable. They prove all pages are consumed, filtering is case-insensitive, duplicate IDs are removed, sorting is deterministic, CLI/environment region precedence works, missing credentials fail before client calls, empty output succeeds, JSON is structured, and API errors are friendly.

## What this supports

The focused specification is implemented without live account access, credentials in evidence, content retrieval, embedding, or namespace mutation.

## Limits

Validation uses the installed SDK's documented auto-paginating iterable contract and deterministic fakes; no live Turbopuffer namespace listing was authorized or run. Remote authorization, latency, and account-specific pagination were not observed.
