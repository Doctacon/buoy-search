Status: done
Created: 2026-07-12
Updated: 2026-07-12
Parent: None
Depends-On: .10x/tickets/done/2026-07-02-cli-one-line-plan-progress.md

# Approved Apply One-Line Progress

## Scope

Extend the existing interactive `OneLineProgress` convention to `turbo-search apply --approve` so large local embedding/upsert jobs expose live progress without changing machine-readable output.

## Acceptance criteria

- Interactive text-mode approved apply renders one updating stderr line with clear phases: verification, lock/preparation, embedding/upserting, local-state commit, and plan cleanup.
- The embedding/upsert phase reports completed/total batches and rows; it updates after each successfully written batch.
- Progress is suppressed for `--json`, non-TTY stderr, and `--no-progress`; add `--no-progress` to `apply` using the established CLI convention.
- Preflight remains local-only and may show verification progress but never reports embedding/upsert work.
- JSON stdout schema, approved-apply semantics, locking, state commit, and cleanup behavior remain unchanged.

## Explicit exclusions

- ETA calculations, rich/full-screen UI, parallel batch processing, retry policy changes, and remote API behavior changes.

## References

- `.10x/tickets/done/2026-07-02-cli-one-line-plan-progress.md`
- `src/turbo_search/cli.py`
- `src/turbo_search/apply.py`
- `tests/test_apply_cli.py`

## Evidence expectations

Focused progress-rendering/suppression tests, apply regression tests, full suite result, and review.

## Progress and notes

- 2026-07-12: Implementation authorized; assigned to a single worker.
- 2026-07-12: Added interactive one-line approved-apply progress, batch counters after successful writes, `apply --no-progress`, and TTY/JSON/non-TTY/preflight regression coverage. Evidence: `.10x/evidence/2026-07-12-approved-apply-progress.md`.
- 2026-07-12: Independent review found a significant semantic-safety defect: a progress callback could fail after a successful remote upsert and before the DuckDB state commit. Repaired it by making callback and stderr rendering failures best-effort; regression coverage proves state commits after failing progress and genuine upsert errors still propagate. Focused tests: 57 passed; full suite: 201 passed.
- 2026-07-12: Re-review confirmed callback safety but found that a regular stderr error print can still mask an actual apply failure. Repaired the approved-apply error diagnostic to be best-effort and added a failing-TTY-stderr plus failing-upsert regression; command returns 2 without raising. Focused tests: 58 passed; full suite: 202 passed.
- 2026-07-12: Final independent review passed. Parent re-ran the full suite: 202 passed. Closure evidence: `.10x/evidence/2026-07-12-approved-apply-progress.md`; review: `.10x/reviews/2026-07-12-approved-apply-progress-review.md`.

## Blockers

- None.
