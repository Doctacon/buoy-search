Status: active
Created: 2026-07-18
Updated: 2026-07-19
Parent: .10x/tickets/2026-07-18-repository-cleanup-plan.md
Depends-On: .10x/tickets/done/2026-07-18-enforce-website-exact-host-crawl-boundary.md

# Remove Unreachable Local-Catalog Persistence

## Scope

Remove the production-unreachable local JSON catalog persistence cluster from `src/buoy_search/catalog.py` and its obsolete tests:

- `document_to_dict`
- `empty_catalog`
- `resolve_catalog_path`
- `load_catalog`
- `catalog_lock`
- `_atomic_write`
- `save_catalog`
- `commit_system_card`
- `mutate_catalog`

Preserve production-reachable card models, schema parsing/validation, semantic projection, generated semantics, routing helpers, remote catalog operations, pending recovery, and `catalog migrate-local` source parsing/validation.

## Acceptance criteria

- AST/source-reference inspection confirms each removed symbol has no production caller before deletion.
- No local catalog path, lock, or atomic persistence implementation remains solely for tests.
- `catalog migrate-local`, remote catalog list/mutation/reconcile/abandon, apply registration, automatic routing, and generated card behavior remain unchanged.
- Tests for removed private persistence behavior are deleted rather than preserving dead implementation; protective parser/card/remote tests remain.
- Focused/full Python 3.11/3.13 tests, distribution build, source search, independent review, and hosted checks pass.

## Evidence expectations

Before/after production reachability report, exact deleted symbols/tests, focused/full/build outputs, and no-write/no-remote attestation.

## Blockers

Complete the preceding exact-host crawler safety repair and incorporate current `develop` before execution.

## Explicit exclusions

Removing `catalog migrate-local`; changing card schema, semantic projection, remote catalog behavior, pending recovery, routing, compatibility aliases, or user data; deleting catalog files from disk.

## References

- `.10x/tickets/2026-07-18-repository-cleanup-plan.md`
- `.10x/research/2026-07-18-repository-dead-end-inventory.md`
- `.10x/decisions/production-routing-remote-catalog.md`
- `.10x/specs/remote-routing-catalog-cli.md`

## Progress and notes

- 2026-07-19: Pre-execution blocker revalidation confirmed the exact-host predecessor is done. Fetched `origin/develop`; task HEAD and current `origin/develop` both resolved to `25aafee398f78761d3638becd7bd452d00e14927`, so no integration commit was needed.
- 2026-07-19: Recomputed production reachability with Python AST across `src/**/*.py`. None of the nine scoped symbols is imported or referenced from another production module. Intra-cluster edges are only `save_catalog -> document_to_dict/_atomic_write`, `load_catalog -> empty_catalog`, and `commit_system_card`/`mutate_catalog -> catalog_lock/load_catalog/save_catalog`; `resolve_catalog_path`, `commit_system_card`, and `mutate_catalog` have no production callers.
- 2026-07-19: Removed exactly the nine scoped definitions and ten persistence-only tests. Preserved parser/card/generated merge coverage without persistence helpers. AST comparison found all 38 retained `catalog.py` definitions identical and no removed-symbol production import. Focused suites passed 151 tests and full suites passed 414 tests on both locked Python 3.11 and 3.13; wheel/sdist build and source/diff checks passed. No live Buoy, Turbopuffer, crawl, user-data, or local-catalog operation occurred. Evidence: `.10x/evidence/2026-07-19-remove-unreachable-local-catalog-persistence.md`. Independent review and closure remain pending.
