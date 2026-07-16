Status: active
Created: 2026-07-15
Updated: 2026-07-15
Parent: .10x/tickets/2026-07-15-buoy-v0-3-0-release-plan.md
Depends-On: .10x/tickets/done/2026-07-15-prepare-buoy-v0-3-0.md

# Promote Develop to Main for v0.3.0

## Scope

- Verify release-prepared `develop`, current `main`, protection, no conflicting open release PR, and exact divergence.
- Open the release pull request `develop -> main` against exact current refs. Because current `main` has release merge commit `1fa9943` outside `develop`, call GitHub's pull-request update-branch endpoint with the observed expected head SHA so GitHub merges current `main` into protected `develop`. If GitHub refuses, block; do not direct-push, rebase, or substitute a squash path.
- Verify the update created a merge commit on `develop` whose ancestry contains both the prior release-ready develop head and exact current main, then require the release PR to rerun strict-freshness Python 3.11, Python 3.13, and Build distributions checks.
- Independently review the complete release diff and release metadata.
- Merge with a merge commit, never squash/rebase.
- Verify resulting `main` has `develop` as an ancestor and observe successful push CI.

## Acceptance criteria

- The release PR update-branch operation is bound to the observed head SHA and produces a develop merge commit containing exact prior main and develop ancestry.
- Current main ancestry is contained by release-ready develop before promotion.
- Release PR contains exactly reviewed develop changes and reports mergeable/clean.
- All required checks and independent review pass.
- GitHub records a merge commit on main with both prior main and release-ready develop ancestry.
- Local/remote main and develop refs plus release commit are recorded without source mutation after review.

## Explicit exclusions

Tag/release creation, version changes, branch-protection changes, force push, squash/rebase, PyPI, Turbopuffer.

## References

- `.10x/specs/protected-github-branches.md`
- `.10x/decisions/protected-development-and-github-release-governance.md`

## Evidence expectations

Pre/post commit graph, PR/check URLs, merge method/parents, main push CI, diff summary, and independent review.

## Blockers

None for sync-PR preparation. The user explicitly ratified this protection-compliant replacement mechanism: create `release/v0.3.0-sync` from exact remote develop `1441c142dae2f501fd8d7306ab3bf1a9db1532d2`, merge exact remote main `1fa99431de85b9de435250f273919bf2d247d1fc` into it with a merge commit, and open a passing PR from that branch to `develop`. This phase stops before merging either the sync PR or release PR #22. The prior failed update-branch evidence remains authoritative history.

## Progress and notes

- 2026-07-15: Promotion pre-merge execution started from release-prepared develop `1441c14`; no main merge is authorized in this phase.
- 2026-07-15: Preflight passed and release PR #22 was opened at exact head `1441c142dae2f501fd8d7306ab3bf1a9db1532d2` against exact main `1fa99431de85b9de435250f273919bf2d247d1fc`. The expected-head-bound update request failed HTTP 422 without moving either ref. Execution stopped per contract. Evidence: `.10x/evidence/2026-07-15-buoy-v0-3-0-promotion-update-branch-blocker.md`.
- 2026-07-15: User explicitly ratified a dedicated protected sync-PR mechanism. Fresh remote preflight confirmed the required exact refs and no existing sync branch/PR; execution resumed only through sync PR readiness, not merge.
