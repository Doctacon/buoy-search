Status: draft
Created: 2026-07-21
Updated: 2026-07-21

# Develop-to-Main Release Readiness

## Purpose and scope

Replace release-specific ancestry syncs and conversational release preflights with mechanically required GitHub checks on every pull request targeting `main`. The only supported release PR source is the repository's `develop` branch.

The user explicitly selected removing the old release ceremony, requiring a series of CI checks that answer whether `develop` can reasonably merge to `main`, and fully automatic publication after a successful main commit.

## Workflow

`.github/workflows/release-readiness.yml` MUST trigger only for pull requests targeting `main` and MUST expose exactly these required check names:

1. `Release readiness / Policy`
2. `Release readiness / Python 3.11`
3. `Release readiness / Python 3.13`
4. `Release readiness / Distribution`

GitHub `main` protection MUST require all four checks with strict freshness. Existing ordinary CI may continue to run, but these four checks are the release-specific merge contract.

## Policy check

The policy job MUST fail unless:

- the pull request head repository is `Doctacon/buoy-search` and head branch is exactly `develop`;
- project, module, and lock versions agree on one valid SemVer version;
- `CHANGELOG.md` contains exactly one pending section for that version and an empty `Unreleased` section;
- neither remote annotated tag `v<version>` nor GitHub Release `v<version>` exists;
- current `main` is an ancestor of `develop`; no ancestry-sync PR or merge topology beyond ordinary Git ancestry is prescribed;
- release workflow and package metadata retain the no-PyPI/no-Turbopuffer boundary.

A version already released from an earlier main commit MUST fail readiness. A new main release therefore requires a version bump in `develop` before merge.

## Python checks

The Python 3.11 and 3.13 jobs MUST independently:

- use locked dependencies;
- validate the frozen ranking contract;
- validate the intentionally blocked C6 forecast without claiming readiness;
- run the complete test and documentation suite;
- use read-only repository permissions and no secrets;
- perform no model download/inference, provider call, live retrieval/apply/eval, namespace operation, or external mutation.

## Distribution check

After both Python jobs pass, the distribution job MUST:

- build wheel and sdist once from the PR head;
- verify exact versioned asset names and package/module/lock metadata;
- prove no `.10x/**`, `turbo-search` entry point, package-owned `turbo-search` launcher, or `legacy_main` is shipped;
- inspect the exact single `buoy` entry point and required bundled data;
- normally install the wheel in a fresh environment;
- run `buoy --version`, `buoy --help`, and `python -m buoy_search --help`;
- load and smoke-test the exact bundled tokenizer when that feature is present, proving distributable dependency resolution rather than only lock resolution;
- retain no build artifact beyond the workflow run and publish nothing.

## Failure behavior

Any missing, skipped, cancelled, stale, or failed readiness check MUST block merge to `main`. Jobs MUST fail with user-legible diagnostics and MUST NOT modify tags, releases, branches, protection, environments, package registries, Turbopuffer, or user state.

## Branch protection transition

Implementation MUST replace obsolete main release requirements with the exact four checks only after a PR run proves all four names and behavior. It MUST retain PR requirement, strict freshness, administrator enforcement, deletion policy, and the user's separately ratified force-push/last-push settings unless the user changes them separately.

## Open-source and portability boundary

GitHub Actions is retained only because the user explicitly required a GitHub Action and the repository already uses GitHub as its public source/release host. Workflow logic MUST use repository scripts and full-SHA-pinned open-source actions where possible. Release artifacts and validation commands remain locally reproducible; no proprietary package registry is introduced.

## Acceptance scenarios

- Given a current `develop` PR with a new version and passing candidate, when all four checks complete, then GitHub reports all four required contexts successful.
- Given a non-`develop` PR to main, when Policy runs, then it fails before release validation.
- Given an existing version tag or Release, when readiness checks that unchanged version, then Policy fails without mutation.
- Given an artifact whose normal resolver selects an incompatible runtime dependency, when Distribution loads the installed feature, then readiness fails.

## Explicit exclusions

Product feature changes; version bump for an unspecified future release; main merge; tag/Release creation; PyPI; Turbopuffer; force push; branch deletion; release-environment approval; ancestry-sync mechanics.
