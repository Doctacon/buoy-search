Status: recorded
Created: 2026-07-14
Updated: 2026-07-14
Relates-To: .10x/tickets/done/2026-07-14-validate-buoy-ci-release-automation.md, .10x/specs/buoy-ci-and-github-releases.md, .10x/specs/buoy-public-project-surface.md

# Buoy CI and Release Automation Integration Validation

## Raw evidence

Sanitized structured workflow, action-pin, package, public-surface, asset hash, and validation observations are stored at `.10x/evidence/.storage/2026-07-14-buoy-ci-release-integration-validation.json`. A raw 3.11/3.13 test/build/positive-and-negative-check/diff log is retained at `.10x/evidence/.storage/2026-07-14-buoy-ci-release-integration-validation-raw.txt`; complete 39-entry wheel and 268-entry sdist inventories plus extracted wheel metadata and hashes are retained at `.10x/evidence/.storage/2026-07-14-buoy-ci-release-package-inventory.json` and embedded in the structured record. These files contain no credentials.

## What was observed

- CI YAML parses with only pull-request and main-push triggers, workflow `contents: read`, same-ref cancellation, Python 3.11/3.13 matrix tests, locked sync, complete tests, and one build job gated on both test jobs.
- Release YAML parses with only `v*` tag pushes, read-only validation/build, exactly one build, immutable workflow artifact transfer, and a `release`-environment mutation job limited to contents/OIDC/attestation permissions.
- Release validation occurs both before and after approval. It enforces exact project/module/tag agreement, an annotated Git tag object, exact wheel/sdist filenames, and refusal to overwrite an existing release. No PyPI, registry publication, branch mutation, secret reference, or Turbopuffer path exists.
- All external actions use full 40-character SHAs with asserted upstream action identity and major-version comments. The prior implementation evidence independently mapped each SHA to its upstream tag.
- Hatchling is fixed to `1.31.0`; wheel/sdist metadata and contents are `buoy-search` / `0.2.0` / `Apache-2.0`, include `buoy_search`, and exclude an old implementation package.
- README is 98 lines and has only CI and Apache-2.0 badges. Changelog 0.2.0 remains explicitly pending; contributor, security, and release docs are present and locally linked. Release docs state GitHub-only/no-PyPI behavior and match portable workflow commands.
- No integration defect requiring source repair was found. The evidence repair independently reran and retained the focused 9 tests, complete 235-test suites under Python 3.11 and 3.13, build output, valid/mismatched tag checks, lightweight/annotated tag-object checks, exact/extra asset checks, lock/diff/index/tag outputs, complete archive inventories, extracted package metadata, and artifact SHA-256 hashes.

## Procedure and results

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_release_automation -q
Ran 9 tests; OK

Sequential complete suite on Python 3.11
Ran 235 tests; OK

Sequential complete suite on Python 3.13
Ran 235 tests; OK

uv build --out-dir /tmp/buoy-release-validate.54EREQ
built buoy_search-0.2.0.tar.gz and buoy_search-0.2.0-py3-none-any.whl

uv run --no-project python scripts/release_checks.py assets --dist <temporary>
PASS: exact two-asset set

uv run --no-project python scripts/release_checks.py tag --tag v0.2.0
PASS

uv run --no-project python scripts/release_checks.py tag --tag v0.2.1
exit 2: release tag mismatch

uv lock --check
git diff --check
git diff --cached --quiet
PASS; no staged files
```

The release automation tests also create isolated temporary Git repositories to prove lightweight tags are rejected and annotated tags are accepted. Missing/extra asset cases are rejected. Root repository tag refs were unchanged and remain empty.

Both full suites emitted the existing non-fatal temporary plan-cleanup warning and completed successfully.

## What this supports or challenges

Supports all local/static criteria before commit, push, hosted CI, environment configuration, tag, or release mutation. It supports advancing to the commit/push child after independent review.

## Limits

GitHub-hosted workflow execution, environment approval behavior, attestation creation, and GitHub Release creation cannot be proven until downstream external tickets run. No tag, commit, push, workflow, GitHub setting, release, PyPI, branch protection, credential, or Turbopuffer operation was created or changed.
