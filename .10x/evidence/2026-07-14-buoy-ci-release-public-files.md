Status: recorded
Created: 2026-07-14
Updated: 2026-07-14
Relates-To: .10x/tickets/done/2026-07-14-add-buoy-ci-release-and-public-files.md, .10x/specs/superseded/buoy-ci-and-github-releases.md, .10x/specs/buoy-public-project-surface.md

# Buoy CI, Release Workflow, and Public Files Validation

## What was observed

- `.github/workflows/ci.yml` runs on pull requests and pushes to `main`, has top-level `contents: read`, cancels superseded same-ref runs, tests Python 3.11/3.13 with `uv sync --locked`, and builds distributions once after tests.
- `.github/workflows/release.yml` triggers only for `v*` tags. It fetches tag objects and requires Git object type `tag` (rejecting lightweight tags), validates exact project/module/tag agreement, runs the complete suite, builds once, verifies/retains exact wheel and sdist artifacts, then gates the mutation job on the `release` environment.
- The release job refuses an existing release, uses explicit `contents: write`, `id-token: write`, and `attestations: write`, attests `dist/*`, and creates a GitHub-only release from the existing verified tag. It contains no PyPI/registry publishing path.
- All external actions are pinned to full 40-character commit SHAs with upstream major-version comments: checkout v4, setup-uv v6, upload/download-artifact v4, and attest-build-provenance v2.
- `scripts/release_checks.py` provides side-effect-free tag/version, annotated-tag-object, and exact asset validation. Nine focused tests cover workflow triggers/permissions/pins/matrix/gate/attestation/no-PyPI, annotated versus lightweight tags, positive and negative tag/assets, README badges/limits/links/SVG, pinned Hatchling, pending changelog state, and public package metadata.
- README is 98 lines / 434 words with only CI and Apache-2.0 badges before release.
- `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `docs/releasing.md` establish concise public contribution, private security-reporting, GitHub-only changelog, and exact release mechanics. Version 0.2.0 remains explicitly pending with no nonexistent release/compare link until downstream release verification.
- Package metadata includes Beta/console/developer/Apache/Python 3.11-3.13/search classifiers, focused keywords, and canonical changelog/documentation URLs.

## Procedure and results

```text
PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest tests.test_release_automation -v
Ran 9 tests; OK

PYTHONDONTWRITEBYTECODE=1 uv run --python 3.11 python -m unittest tests.test_release_automation -q
Initial implementation: 7 tests; OK
Repair validation uses the primary environment below.

PYTHONDONTWRITEBYTECODE=1 uv run python -m unittest discover -s tests -p 'test_*.py' -q
Initial implementation: 233 tests on Python 3.11; OK

Post-review repair complete suite
Ran 235 tests; OK

uv lock --check
PASS

uv build --out-dir /tmp/buoy-public-ci-build
Built buoy_search-0.2.0-py3-none-any.whl and buoy_search-0.2.0.tar.gz using exactly pinned hatchling==1.31.0

uv run --no-project python scripts/release_checks.py tag --tag v0.2.0
PASS

uv run --no-project python scripts/release_checks.py tag --tag v0.2.1
Exit 2: release tag mismatch; no Git tag changed

uv run --no-project python scripts/release_checks.py assets --dist /tmp/buoy-public-ci-build
PASS (uv's hidden dist .gitignore is deliberately ignored; exactly two public artifacts required)

Wheel METADATA inspection
PASS: name/version/license, Python classifier, and canonical project URLs

git diff --check
PASS

git diff --cached --name-only
empty; this worker did not stage or unstage files
```

Workflow YAML was parsed with the repository's PyYAML dependency. Automated assertions validate exact triggers, permissions, action pins, version checks, artifact names, and absence of a PyPI path. README/docs local-link validation and SVG XML parsing run inside `tests.test_release_automation`.

## What this supports or challenges

Supports both governing specifications without commit, push, tag, environment, release, branch-protection, PyPI, secret, or live-product mutation. The workflows have not yet run on GitHub; canonical workflow execution belongs to downstream validation/push/release tickets.

## Review-blocker repair

Independent review found two release-integrity blockers and one premature changelog claim. The repair:

- added `tag-object` validation backed by `git cat-file`, fetched full tag objects in both workflow jobs, and runs the check before any release mutation;
- added positive annotated-tag and negative lightweight-tag regressions in isolated temporary repositories;
- pinned the isolated build backend exactly to `hatchling==1.31.0` and added a deterministic metadata assertion;
- strengthened action-pin tests to require the approved action identities and matching major-version comments;
- kept 0.2.0 explicitly pending and removed nonexistent release/compare links, with downstream activation documented.

Focused 9 tests, full 235 tests, exact build/assets, lock, and diff checks pass after repair.

## Limits

- GitHub has not executed either workflow yet, so runner/environment/attestation behavior remains to be observed after push.
- External web links were not network-checked.
- No latest-release badge is present because v0.2.0 does not yet exist.
- Independent security/editorial/technical review is required before child closure.
