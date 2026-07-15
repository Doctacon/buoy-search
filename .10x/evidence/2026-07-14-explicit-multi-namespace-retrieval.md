Status: recorded
Created: 2026-07-14
Updated: 2026-07-14
Relates-To: .10x/tickets/done/2026-07-14-add-explicit-multi-namespace-retrieval.md, .10x/specs/explicit-multi-namespace-retrieval.md

# Explicit Multi-Namespace Retrieval Validation

## What was observed

- `buoy retrieve` accepts repeatable `--namespace`; CLI values replace the environment and preserve selection order. A non-empty `TURBOPUFFER_NAMESPACE` supplies one target only when no CLI namespace is present.
- Dry-run and live retrieval without either source fail before runtime config, model, credential, or API construction and point to `buoy namespaces [search]`.
- Multi-namespace live retrieval creates one embedder, normalizes/embeds the query once, reuses the vector for sequential existing per-namespace retrieval, and aborts without output when a namespace fails.
- Namespace-local final rankings are merged with equal-weight RRF using existing `RRF_K=60`. Distinct namespaces retain separate `(namespace, row ID)` identities; duplicate selected namespace IDs are rejected before config/model/API work so that identity cannot appear twice from repeated selection. Ties use namespace selection order then local rank, global `top_k` is enforced, and every merged hit carries its namespace.
- Both single- and multi-namespace live failures identify the selected failing namespace and emit no result payload.
- Single-namespace result and plan shapes retain the singular `namespace` contract. Multi invocations use explicit `namespaces`, per-namespace plan/result summaries, and no misleading singular namespace.
- Retrieval documentation now presents discover → explicitly select → retrieve, and states there is no demo fallback or automatic broad fan-out.

## Procedure and validation

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_multi_namespace_retrieval tests.test_retriever tests.test_cli -q
Ran 67 tests; OK

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Ran 268 tests; OK

uv lock --check
Resolved 130 packages

uv build --out-dir /tmp/buoy-multi-namespace-build
Built buoy_search-0.2.1 wheel and sdist

git diff --check
OK

git diff --cached --quiet
No staged files
```

Focused tests use deterministic fake embedders/namespaces. They prove one embedding call, sequential namespace call order, distinct-namespace duplicate row identity, duplicate namespace rejection before config, exact `RRF_K=60` score use, deterministic rank-order ties, environment fallback, CLI-over-environment precedence, actionable missing-selection failure, normalized query, explicit multi dry-run shape/text, live multi-hit namespace text attribution, and attributed single/multi failure with no result payload.

No Turbopuffer credential, namespace listing, content query, write, deletion, or other live operation occurred.

## What this supports

The active specification and ticket implementation criteria are met pending independent review. Existing within-namespace tests continue to pass after extracting the already-embedded query path.

## Limits

## Post-review repair validation

Independent review found that a single-namespace failure omitted its selected namespace and repeated identical namespace arguments could duplicate the same `(namespace, row ID)`. The repair wraps single live failures with namespace attribution and rejects repeated namespace IDs during explicit resolution. Three regressions additionally cover duplicate rejection, single failure attribution, and multi live text attribution; the existing fusion test now asserts `RRF_K == 60` and its exact first-rank score.

```text
Focused multi/retriever/CLI suite: 70 tests; OK
Full suite: 271 tests; OK
uv lock --check; wheel/sdist build; git diff --check; no staged files: OK
```

No live multi-namespace latency, account authorization, or schema combination was exercised. The selected namespaces are assumed to use the one operator-supplied/default model and precision; this version intentionally does not infer or validate per-namespace embedding configuration. Queries are sequential by specification.
