Status: done
Created: 2026-07-22
Updated: 2026-07-22
Parent: None
Depends-On: None

# Add first-class database relation sources

## Aggregate scope

Implement `.10x/specs/database-document-relation-indexing.md` and `.10x/specs/warehouse-relation-adapters.md` in three sequential bounded children on `work/database-relation-sources`.

## Child sequence

1. `.10x/tickets/done/2026-07-22-refactor-shared-database-relation-core.md`
2. `.10x/tickets/done/2026-07-22-add-bigquery-snowflake-adapters.md`
3. `.10x/tickets/done/2026-07-22-integrate-database-catalog-ranking-docs.md`

One writer operates in the worktree at a time. Child 2 depends on child 1; child 3 depends on both.

## Aggregate acceptance

All spec acceptance criteria are mapped to tests/evidence; required validation commands pass; optional extras resolve when network permits; independent review has no unresolved critical/significant findings; no live warehouse or turbopuffer calls occur.

## Progress and notes

- 2026-07-22: User ratified a complete execution contract. Existing DuckDB spec/tickets and ranking decision inspected; focused extension specs and child graph opened.
- 2026-07-23: All three children completed. Initial independent review failed eight findings; bounded repairs resolved all findings and fresh independent re-review passed with no critical, significant, or minor findings. Parent validation passed 600 tests plus locked sync, ranking and syntax validators, package build, both optional-extra resolutions, and diff check. Evidence: `.10x/evidence/2026-07-23-database-relation-sources-validation.md`. Review: `.10x/reviews/2026-07-23-database-relation-sources-review.md`. Specifications, implementation, tests, documentation, and ticket graph agree; closed.

## Blockers

None.
