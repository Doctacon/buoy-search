Status: open
Created: 2026-07-19
Updated: 2026-07-19
Parent: None
Depends-On: None

# Reconcile Scrapling Site Workflow Direct-Command Guidance

## Scope

Perform a record/documentation-only correction to `.pi/skills/turbopuffer-site-rag/references/scrapling-site-workflow.md`: its retrieval-validation text currently says live retrieval and evals both require `--live`, but integrated authority says plain retrieval is live, retrieve `--live` is only a compatibility no-op, retrieve `--dry-run`/`--plan` preview, and evals `--live` still opts into live eval execution.

Update only that stale direct-command guidance and verify it agrees with the active direct-command decision/specification and current CLI help.

## Acceptance criteria

- The reference clearly distinguishes plain-live retrieval, retrieval preview flags, retrieve's compatibility `--live`, and evals' still-operative `--live`.
- Example commands and surrounding safety language remain explicit that live remote operations require user approval and credentials.
- No 0.4 alias-removal behavior, source, tests, package metadata, state/data, or remote resources change.
- Reference checks and a bounded source/help comparison pass; evidence and independent record-only review are recorded.

## Evidence expectations

Changed-lines diff, exact governing-record/source paths inspected, reference/link check output, and no-source/no-test/no-state/no-remote attestation.

## Blockers

None.

## Explicit exclusions

Buoy 0.4 console/environment alias implementation; changing direct-command behavior or flags; changing apply namespace/environment guidance; source/tests/package/version/release changes; live retrieval/evals.

## References

- `.10x/decisions/direct-commands-execute-by-default.md`
- `.10x/specs/default-remote-namespace-routing.md`
- `.10x/tickets/done/2026-07-18-make-retrieval-live-by-default.md`
- `.10x/research/2026-07-19-v0-4-compatibility-removal-inventory.md`

## Progress and notes

- 2026-07-19: Opened as the separate owner discovered during 0.4 compatibility inventory. It is not a child or implementation prerequisite of the 0.4 removal plan.
