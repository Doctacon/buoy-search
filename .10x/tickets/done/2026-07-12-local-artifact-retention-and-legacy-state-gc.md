Status: done
Created: 2026-07-12
Updated: 2026-07-12
Parent: None
Depends-On: None

# Automatic Plan-Artifact Lifecycle Cleanup

## Scope

Implement prospective automatic deletion of plan artifact directories after successful approved apply or verified same-namespace supersession.

## Acceptance criteria

- Satisfy `.10x/specs/plan-artifact-lifecycle-cleanup.md` scenarios and constraints.
- Preserve pending, failed, contended, and preflight plan artifacts.
- Never delete active DuckDB state, legacy-state paths, other namespaces, malformed plan directories, symlink targets outside the artifact root, or remote data.
- Record test evidence and a review.

## Explicit exclusions

- Historical artifact backlog cleanup/reconciliation.
- Legacy JSON migration cleanup, owned by `.10x/tickets/done/2026-07-12-purge-legacy-json-during-duckdb-migration.md`.
- Plan-artifact format compaction, Quack, and Turbopuffer namespace lifecycle.

## References

- `.10x/specs/plan-artifact-lifecycle-cleanup.md`
- `.10x/decisions/plan-artifact-immediate-lifecycle-retention.md`
- `src/turbo_search/cli.py`
- `src/turbo_search/apply.py`
- `src/turbo_search/plan_artifacts.py`

## Evidence expectations

Focused lifecycle tests, full suite result, exact deleted/retained path assertions, and an adversarial review.

## Progress and notes

- 2026-07-12: Operator ratified immediate prospective cleanup after successful apply and same-namespace supersession; pending/failed plans remain.
- 2026-07-13: Implementation authorized; assigned to a single worker.
- 2026-07-13: Added verified, symlink-safe prospective plan cleanup after successful approved apply and same-namespace supersession. Failed/preflight/contended plans remain. Updated README, workflow docs, and the project skill. Evidence: `.10x/evidence/2026-07-13-plan-artifact-lifecycle-cleanup.md`. Focused tests: 53 passed; full suite: 192 passed.
- 2026-07-13: Independent review found that valid plan artifacts under a state root could be deleted. Cleanup now receives the configured state root and rejects any applied target or supersession scan under that full tree. Added default-style and custom-root regression coverage. Focused tests: 55 passed; full suite: 194 passed.
- 2026-07-13: Independent re-review passed.

## Blockers

- None.
