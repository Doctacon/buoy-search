Status: done
Created: 2026-07-12
Updated: 2026-07-12
Parent: None
Depends-On: None

# Compact DuckDB Applied-State Plan

## Scope

Coordinate the replacement of JSON applied state with compact, per-namespace embedded DuckDB state according to `.10x/specs/compact-duckdb-applied-state.md` and `.10x/decisions/superseded/duckdb-applied-state-concurrency.md`.

## Child sequence

1. `.10x/tickets/done/2026-07-12-duckdb-state-store-and-migration.md`
2. `.10x/tickets/done/2026-07-12-duckdb-state-apply-lock-integration.md`
3. `.10x/tickets/done/2026-07-12-duckdb-state-validation-and-docs.md`

The state-store ticket must land before apply integration. Validation/docs follows both. Different namespace processes are an integration test concern, not a second writer implementation.

## Acceptance criteria

- Every child satisfies its governing specification criteria with recorded evidence.
- JSON state is no longer the active backend.
- The migration preserves archived legacy JSON while preventing absent remote rows from being treated as applied.
- No Quack service or remote mutation is introduced outside existing approved-apply behavior.

## Explicit exclusions

- Plan-artifact compaction.
- Turbopuffer namespace creation, restoration, deletion, or re-indexing.
- Quack, cross-machine state, and concurrent applies to one namespace.

## Evidence expectations

Focused tests for migration, diff parity, transaction failure behavior, and lock scoping; a full suite result; a size comparison on representative state; and an adversarial review.

## Progress and notes

- 2026-07-12: User ratified per-namespace embedded DuckDB, archive-and-reset migration, indefinite summary-only history, and fail-fast same-namespace locking.
- 2026-07-12: Completed state-store migration, apply lock integration, validation, documentation, and independent review/re-review gates. Final parent-observed suite: 186 tests passed; no Quack implementation references; `git diff --check` passed.

## Blockers

- None.
