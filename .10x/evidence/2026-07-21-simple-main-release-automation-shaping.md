Status: recorded
Created: 2026-07-21
Updated: 2026-07-21
Relates-To: .10x/tickets/2026-07-21-shape-simple-main-release-automation.md

# Simple Main Release Automation Shaping

## Observed current state

- No release/merge/deploy skill exists under `.10x/skills`, `.pi/skills`, or `.agents/skills`.
- Release ceremony currently lives in `.github/workflows/release.yml`, `docs/releasing.md`, active release/branch specifications and decisions, and temporal release tickets/evidence.
- Current release workflow triggers on `v*` tags, validates/builds, waits on GitHub environment `release`, attests, and creates a GitHub Release.
- Current CI runs Python 3.11, Python 3.13, and one distribution build for every PR and pushes to main/develop.
- Main branch protection uses strict CI and last-push approval; develop uses strict CI. The user asked for release-specific develop-to-main readiness checks rather than conversational preflight.
- Published v0.4.0 tag/Release exists at commit `c49dc0582bf3f06a16eafdcca0707d1e64e1c58d`, so an unchanged 0.4.0 future main commit must fail under the selected collision contract.

## User choices

The user selected release-ceremony removal, exact-head matching no-op versus all-other-state failure, and fully automatic publication without environment approval.

## Proposed contract

- Four explicit main-PR checks: Policy, Python 3.11, Python 3.13, Distribution.
- Main protection requires those checks with strict freshness.
- Main-push release workflow repeats release-critical validation, builds once, creates annotated tag/provenance/Release only for absent state, and verifies exact matching state as a no-op.
- Partial/mismatched states fail without overwrite/delete/move/cleanup.
- The next release requires a version bump; no next version is invented.
- Active old ceremony is superseded/removed, historical evidence remains, and the unused release environment is deleted only after no workflow references it.

## Side effects and limits

This shaping turn changed only draft `.10x` records. It did not edit workflows, docs, scripts, tests, protection, environments, branches, tags, releases, registries, Turbopuffer, or user state. GitHub Actions remains an explicit user-required managed-platform exception; release logic is kept locally reproducible and open-source-action pinned.
