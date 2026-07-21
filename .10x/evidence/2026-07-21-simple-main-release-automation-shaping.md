Status: recorded
Created: 2026-07-21
Updated: 2026-07-21
Relates-To: .10x/tickets/done/2026-07-21-shape-simple-main-release-automation.md

# Simple Main Release Automation Shaping

## Observed current state

- No release/merge/deploy skill exists under `.10x/skills`, `.pi/skills`, or `.agents/skills`.
- Release ceremony currently lives in `.github/workflows/release.yml`, `docs/releasing.md`, active release/branch specifications and decisions, and temporal release tickets/evidence.
- Current release workflow triggers on `v*` tags, validates/builds, waits on GitHub environment `release`, attests, and creates a GitHub Release.
- Current CI runs Python 3.11, Python 3.13, and one distribution build for every PR and pushes to main/develop.
- Initial records described main last-push approval, but independent shaping review's hosted API readback found current `require_last_push_approval=false`. Main still used strict ordinary CI at shaping start; develop used strict ordinary CI. The ratified contract keeps main last-push approval false and replaces main strictness/checks only through the hosted configuration child.
- Published v0.4.0 tag/Release exists at commit `c49dc0582bf3f06a16eafdcca0707d1e64e1c58d`, so an unchanged 0.4.0 future main commit must fail under the selected collision contract.

## User choices

The user selected release-ceremony removal, exact-head matching no-op versus all-other-state failure, and fully automatic publication without environment approval.

## Proposed contract

- Four explicit main-PR checks: Policy, Python 3.11, Python 3.13, Distribution.
- Main protection requires those checks with `strict=false`; they validate GitHub's prospective merge result, eliminating ancestry-sync ceremony.
- Main-push release workflow repeats release-critical validation, builds once, creates annotated tag/provenance/Release only for absent state, and verifies exact matching state as a no-op.
- Partial/mismatched states fail without overwrite/delete/move/cleanup.
- The next release requires a version bump; no next version is invented.
- Active old ceremony is superseded/removed, historical evidence remains, and the unused release environment is deleted only after no workflow references it.

## Side effects and limits

This shaping turn changed only draft `.10x` records. It did not edit workflows, docs, scripts, tests, protection, environments, branches, tags, releases, registries, Turbopuffer, or user state. GitHub Actions remains an explicit user-required managed-platform exception; release logic is kept locally reproducible and open-source-action pinned.
