Status: recorded
Created: 2026-07-21
Updated: 2026-07-21
Relates-To: .10x/tickets/2026-07-21-validate-buoy-v0-4-0-release-candidate.md, .10x/tickets/2026-07-21-buoy-v0-4-0-release-plan.md

# Buoy v0.4.0 Release Candidate Validation

## What was observed

Release candidate source began at integrated `develop` commit `a2142205cae8ccfce9ed5f4d3b4785413621812b`. Project, module, lock, wheel, and sdist metadata identify 0.4.0. The candidate moves the complete release notes from Unreleased to `## [0.4.0] - pending`, leaves Unreleased empty, and adds focused static assertions for the pending version and newly documented behavior.

Both complete locked source suites passed 518 tests. The frozen ranking contract and intentionally blocked C6 forecast validators passed on both Python versions. Clean candidate artifacts, clean installation, and digest-verified released-0.3.0 same-environment upgrade validation passed.

## Procedure and results

### Locked source validation

Using separate disposable environments:

- CPython 3.11.5: `uv sync --locked --python 3.11`, ranking validation, C6 validation, and `python -m unittest discover -s tests -p 'test_*.py' -q` passed 518 tests in 74.025 seconds.
- CPython 3.13.0: `uv sync --locked --python 3.13`, ranking validation, C6 validation, and the same complete suite passed 518 tests in 66.515 seconds.
- Ranking identity remained 90 composite identities, 13 datasets/folds, 369 judgments, dataset bundle `5a79f58aaca87a2d4f7cbec68fdcfbbcbf041131821587f8aba74a86daca99d9`.
- C6 validator remained valid and readiness false at forecast `d5199276c19ae89779287eaa90824ce1e1cc684a3f060899f02f65d976016243` and tokenizer checkpoint `c3a1560e611114760909c110a118a3ce1a60f0527de08c769a85a20b263f4e0f`.
- Each complete suite emitted the two known mocked temporary plan-artifact cleanup warnings and passed. Python 3.13 also emitted the existing lxml `strip_cdata` deprecation warning.
- `uv lock --check` and `git diff --check` passed.

### Build and artifact inspection

`uv build --out-dir /tmp/buoy-v040-release-dist` built once from the candidate:

- `buoy_search-0.4.0-py3-none-any.whl`: SHA-256 `9ef34c54f9bab924890bd48496e87755c135e1a22a5fe526768f206fb7786cbd`, 52 members.
- `buoy_search-0.4.0.tar.gz`: SHA-256 `bb50cb08d216892107b0db04c69be0ab6990ffef7306e37b94f5beec43ec0625`, 109 members.

Inspection proved:

- exact 0.4.0 metadata and names;
- wheel entry points are exactly `[console_scripts]` plus `buoy = buoy_search.cli:main`;
- no `.10x/**` member exists in either artifact;
- the wheel contains package code, bundled evaluation data, and the exact bundled offline treatment tokenizer files;
- `scripts/release_checks.py tag --tag v0.4.0` and `assets --dist /tmp/buoy-v040-release-dist` passed.

### Clean installation

A fresh CPython 3.13 environment normally installed the candidate wheel. Installed metadata reported 0.4.0 and exactly one package console entry point, `buoy_search.cli:main`. `buoy --version` returned `buoy 0.4.0`; `buoy --help` and `python -m buoy_search --help` passed. The `buoy` launcher existed and `turbo-search` did not.

### Released 0.3.0 upgrade

Downloaded only `https://github.com/Doctacon/buoy-search/releases/download/v0.3.0/buoy_search-0.3.0-py3-none-any.whl`. Its SHA-256 matched the immutable required value `048dba11df692a7efcd7ab7269fc2eec82f6b53e57573a3de113bbd051750bab` before installation.

A fresh CPython 3.13 environment installed 0.3.0 and proved version 0.3.0 plus both package-owned `buoy` and `turbo-search` launchers. A normal same-environment upgrade to the candidate wheel produced version 0.4.0, retained working `buoy` and module help, exposed exactly the one `buoy` entry point, and removed the package-owned `turbo-search` launcher.

## What this supports

This supports the code-level 0.4.0 candidate criteria in `.10x/specs/buoy-release-validation.md`, including complete supported-Python tests, exact version/artifact/launcher behavior, preserved blocked-experiment truth, clean install, and released-wheel upgrade behavior. Existing tests cover CLI parser/help/version, removed-variable ordering/streams/non-dispatch, retained state roots, dual-root refusal, explicit roots, DuckDB loading, old-plan preflight, fixture autoresearch, repository eval datasets, documentation links, workflow/static release policy, and distribution exclusions.

## Limits and side effects

This evidence does not authorize or prove branch promotion, tag creation, GitHub Release publication, provenance, or changelog finalization. All environments and artifacts were disposable under `/tmp`. Network reads were dependency resolution and the immutable GitHub 0.3.0 wheel. No credential was read; no Turbopuffer/provider call, namespace operation, live retrieval/apply/eval, user-state discovery/mutation, PyPI publication, tag, Release, branch protection change, or cleanup of user-owned state occurred.
