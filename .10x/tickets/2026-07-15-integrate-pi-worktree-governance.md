Status: open
Created: 2026-07-15
Updated: 2026-07-15
Parent: .10x/tickets/2026-07-15-establish-protected-development-workflow.md
Depends-On: .10x/tickets/2026-07-15-add-pi-worktree-governance.md

# Integrate Pi Worktree Governance

## Scope

Independently review the bounded governance pull request, verify remote branch protection and required GitHub checks, then squash-merge the task pull request into `develop` only if every governing criterion is supported.

After merge, update the local integration checkout safely to the resulting `develop` state without modifying `main`.

## Acceptance criteria

- Review maps the pull-request diff to both focused specifications and reports pass, concerns, or fail.
- GitHub API readback confirms both `main` and `develop` protections still match `.10x/specs/protected-github-branches.md`.
- The pull-request head incorporates current `develop`.
- `Python 3.11`, `Python 3.13`, and `Build distributions` all succeed for the pull request head.
- No unexpected files or behavior are included.
- Any significant review finding is resolved and revalidated before merge.
- The pull request is squash-merged into `develop`, not merged or rebased.
- Remote `develop` points to the resulting squash commit and remains protected.
- `main` remains unchanged.
- Durable review and evidence records support every criterion and state their limits.

## Explicit exclusions

- A `develop`-to-`main` release pull request.
- Version or changelog bump.
- Tag or GitHub Release creation.
- Protection policy changes.
- Product implementation.
- Launcher, Git hook, or Pi extension.
- Package publication, secret/environment changes, or Turbopuffer operations.

## References

- `.10x/decisions/protected-development-and-github-release-governance.md`
- `.10x/specs/pi-worktree-development-flow.md`
- `.10x/specs/protected-github-branches.md`
- `.10x/tickets/2026-07-15-establish-protected-development-workflow.md`
- `.10x/tickets/2026-07-15-add-pi-worktree-governance.md`
- Evidence produced by both dependency tickets.

## Evidence expectations

Record the reviewed pull-request URL and head, required check runs and conclusions, effective branch-protection readback, merge method, resulting `develop` commit, unchanged `main` commit, and local worktree/branch state. Never record tokens.

## Blockers

Depends on a complete, passing governance pull request.

## Progress and notes

- 2026-07-15: Ticket opened. Integration has not begun.