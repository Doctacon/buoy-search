Status: open
Created: 2026-07-21
Updated: 2026-07-21
Parent: .10x/tickets/2026-07-21-simple-main-release-automation-plan.md
Depends-On: None

# Implement Simple Main Release Automation

## Scope

- Add `.github/workflows/release-readiness.yml` with the exact four check names and prospective-merge behavior.
- Replace `.github/workflows/release.yml` with serialized main-push automatic validation/build/state-machine/tag/attestation/Release behavior.
- Implement repository-local standard-Python/shell version, changelog, deterministic artifact, GitHub-state, collision, and dry-run helpers rather than burying logic in YAML.
- Add exhaustive deterministic tests for every active-spec branch, permissions/trigger/action pins, forbidden operations, and v0.4 transition.
- Update `docs/releasing.md` to the simple version-bump/develop-PR flow and self-hosted migration mapping.
- Finalize the already-published v0.4.0 changelog date/links from recorded hosted authority; close its finalization and aggregate release records truthfully.
- Supersede/remove active manual-tag/environment/ancestry ceremony while preserving historical evidence.

## Acceptance criteria

- Every criterion in both active simple-release specs has source/tests.
- Existing complete Python 3.11/3.13 suites, validators, workflow static checks, dry state-machine tests, deterministic two-build digest comparison, normal clean-wheel tokenizer smoke, and distribution inspection pass.
- Workflow write permissions exist only on the final publication job, which installs no dependency and executes no repository code.
- No workflow references `environment: release`, tag triggers, manual dispatch, PyPI, Turbopuffer, overwrite/delete/move/force-push operations, or ancestry sync.
- Existing v0.4.0 exact complete state dry-runs as no-op only at its exact released SHA; a different SHA with 0.4.0 fails.
- Exact-head hosted CI and independent review pass before squash integration to develop.

## Explicit exclusions

Hosted protection/environment/PR mutation; choosing or bumping a future version; main merge; live workflow release; tag/Release mutation; PyPI; Turbopuffer; product changes.

## References

- `.10x/specs/develop-to-main-release-readiness.md`
- `.10x/specs/main-push-automatic-github-release.md`
- `.10x/decisions/simple-main-release-governance.md`
- `.10x/evidence/2026-07-21-simple-main-release-automation-ratification.md`
- `.10x/tickets/2026-07-21-finalize-buoy-v0-4-0-changelog.md`
- `.10x/tickets/2026-07-21-buoy-v0-4-0-release-plan.md`

## Evidence expectations

Changed paths; exact workflow/check/state mechanics; deterministic artifacts; tests/validators/clean install; docs/migration; no-live attestation; hosted checks; independent review.

## Blockers

None.
