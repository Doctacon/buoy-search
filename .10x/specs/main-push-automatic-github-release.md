Status: draft
Created: 2026-07-21
Updated: 2026-07-21

# Main-Push Automatic GitHub Release

## Purpose and scope

Replace manual annotated-tag creation and protected-environment approval with one fully automatic GitHub Action on every push to `main`. Successful validation of a new project version creates its annotated tag, provenance, and GitHub Release without a manual gate.

## Trigger and permissions

`.github/workflows/release.yml` MUST trigger only on pushes to `main`, never on tags or manual dispatch.

Validation jobs MUST use read-only contents permissions and no secrets. The final publication job MAY use only the repository `GITHUB_TOKEN` with the minimum required permissions:

- `contents: write` for annotated tag and GitHub Release;
- `id-token: write` and `attestations: write` for provenance;
- `actions: read` only if artifact retrieval requires it.

It MUST NOT access repository service credentials or contact Turbopuffer.

## Validation and build

Before any tag or Release mutation, the workflow MUST:

1. verify project, module, lock, and pending changelog version agreement;
2. run the same locked Python 3.11 and 3.13 validation commands as release readiness;
3. build wheel and sdist exactly once;
4. verify exact asset names, metadata, inventory, entry points, bundled data, normal clean installation, CLI smoke checks, and bundled-tokenizer loading;
5. inspect authoritative remote tag and GitHub Release state for `v<version>`.

No publication job may start unless every validation/build job passes.

## Collision and idempotency contract

The user selected **No-op or fail**:

- **Neither tag nor Release exists:** create the annotated tag at exact `GITHUB_SHA`, attest the built assets, and create the GitHub Release.
- **Both tag and Release exist and the annotated tag peels to exact `GITHUB_SHA`:** verify the Release's exact expected asset names/digests and provenance, then succeed as an idempotent no-op without rewriting anything.
- **Only one exists, the tag is lightweight, the tag peels elsewhere, the Release targets conflicting state, assets differ, or provenance is absent/mismatched:** fail closed without create, overwrite, move, delete, or cleanup.

A new release therefore requires a new version in the main commit. Existing tags and releases are immutable.

## Automatic publication

For the create path, the workflow MUST:

1. create an annotated `v<version>` tag object whose peeled commit is exact `GITHUB_SHA`;
2. push only that new tag with no branch mutation;
3. attest the already-built wheel and sdist with SLSA provenance;
4. create a non-draft, non-prerelease GitHub Release named `Buoy v<version>` with generated notes and exactly those two assets;
5. verify authoritative tag metadata, Release identity, downloaded/API asset digests, and provenance before reporting success.

There is no environment, deployment approval, wait timer, or manual approval step.

## Failure and retry behavior

- Validation failure performs no release mutation.
- A failure after tag creation but before complete Release publication leaves partial immutable evidence and MUST fail. A rerun may continue only when the collision contract can prove the exact same commit/artifacts and complete missing state without overwriting; otherwise it fails for operator repair.
- The workflow MUST never delete a tag/Release, move a tag, overwrite assets, force push, publish to PyPI, or mutate Turbopuffer/user state.
- Diagnostics MUST identify the exact version, commit, observed tag/Release state, and failed stage without exposing tokens.

## Existing v0.4.0 transition

The workflow will first land on `develop`, not `main`. Because v0.4.0 already exists at released main `c49dc0582bf3f06a16eafdcca0707d1e64e1c58d`, any future PR that attempts to merge unchanged version 0.4.0 into a different main commit MUST fail readiness. The next automatic release requires an explicit version bump; this specification does not choose that version.

The old `release` environment becomes unused. After the new main-push workflow is integrated and a dry/state test proves no environment reference remains, implementation SHOULD delete that unused GitHub environment. Deletion MUST occur only under the executable implementation ticket and be recorded; it MUST NOT affect an active deployment.

## Required tests

Static and deterministic tests MUST cover:

- exact trigger/permissions/check commands/action pins;
- valid absent-state creation planning;
- exact existing-state no-op;
- every partial/mismatched collision;
- annotated versus lightweight tags;
- version/changelog disagreement;
- asset and provenance mismatch;
- no PyPI/Turbopuffer/environment/manual-dispatch/tag-trigger behavior;
- no overwrite/delete/move/force-push commands.

A local dry harness MUST exercise the state machine without GitHub mutation.

## Open-source and portability boundary

GitHub Actions is used because the user explicitly required it and release hosting already resides on GitHub. State-machine/version/asset validation MUST remain repository-local standard Python or shell logic with deterministic tests. Full-SHA-pinned open-source actions are preferred; artifacts remain standard wheel/sdist files and no proprietary package registry is introduced.

## Explicit exclusions

Choosing the next version; product changes; PyPI; Turbopuffer; release-environment approval; manual tag push; tag-triggered workflow; tag/Release replacement; main/develop force push; ancestry-sync procedure.
