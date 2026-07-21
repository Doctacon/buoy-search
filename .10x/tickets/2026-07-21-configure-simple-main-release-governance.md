Status: blocked
Created: 2026-07-21
Updated: 2026-07-21
Parent: .10x/tickets/2026-07-21-simple-main-release-automation-plan.md
Depends-On: .10x/tickets/2026-07-21-implement-simple-main-release-automation.md

# Configure Simple Main Release Governance

## Scope

After reviewed repository automation integrates to develop:

- prove exact workflow files contain no release-environment reference and GitHub has zero active/pending deployments for `release`;
- delete the unused GitHub `release` environment and verify absence;
- update `main` protection to require exactly the four GitHub-Actions contexts, `strict=false`, last-push approval false, zero fixed approvals, administrator enforcement, deletion denial, PR requirement, and retained force-push allowance;
- leave `develop` protection unchanged and verify complete API readback;
- close obsolete unmerged PR #87 without deleting its branch until recorded evidence integrates;
- record all external mutations and no-product/no-release boundaries.

## Acceptance criteria

- Repository automation's integrated commit and hosted CI are exact and reviewed before mutation.
- No active/pending release deployment exists at environment deletion.
- Environment readback returns absent after deletion.
- Main/develop protection exactly matches active specs; no required context is added to develop.
- PR #87 closes unmerged as superseded; no branch force/deletion occurs.
- No version/tag/Release/asset/provenance/PyPI/Turbopuffer/user-state mutation occurs.
- Independent review verifies hosted state before closure.

## Explicit exclusions

Workflow/source edits; version bump; main merge; triggering a release; changing force-push allowance; develop protection mutation; tag/Release/PyPI/Turbopuffer operations.

## References

- `.10x/specs/develop-to-main-release-readiness.md`
- `.10x/specs/main-push-automatic-github-release.md`
- `.10x/specs/protected-github-branches.md`
- `.10x/decisions/simple-main-release-governance.md`

## Evidence expectations

Exact before/after environment/deployment/protection/PR API state, mutation requests, integrated workflow identity, no-live boundaries, and independent review.

## Blockers

Blocked on reviewed integration of `.10x/tickets/2026-07-21-implement-simple-main-release-automation.md`.
