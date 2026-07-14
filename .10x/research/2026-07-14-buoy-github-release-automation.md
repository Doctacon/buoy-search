Status: done
Created: 2026-07-14
Updated: 2026-07-14

# Buoy GitHub Release Automation

## Question

What is the smallest credible public-repository CI, badge, and release system for Buoy while keeping releases reproducible, secure, and GitHub-only?

## Sources and methods

- Inspected the current public repository, package metadata, workflow/release files, release list, branch protection, and PyPI package-name availability.
- Confirmed the repository currently has no `.github` workflows, no GitHub releases, and no branch protection.
- Confirmed `buoy-search` currently returns 404 from the PyPI JSON API, but the user chose not to publish there.
- Consulted:
  - uv GitHub integration and package publishing guidance: https://docs.astral.sh/uv/guides/integration/github/ and https://docs.astral.sh/uv/guides/package/
  - GitHub artifact attestation guidance: https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
  - Python Packaging trusted publishing guidance: https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
  - PyPI pending trusted publisher guidance: https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/

## Findings

- CI and release badges are credible only after workflows/releases exist; PyPI and Python-version badges would be misleading without PyPI publication.
- A GitHub-only release can build wheel/sdist, attest their provenance, and attach them to a GitHub Release without any package-registry token.
- Artifact attestations require narrowly scoped `id-token: write`, `attestations: write`, and `contents: read`; creating the GitHub Release additionally requires `contents: write` for the release job.
- CI can remain portable by running repository-native `uv sync --locked`, unittest, docs/SVG validation, and `uv build` commands rather than delegating release logic to an opaque release-management service.
- Pinning third-party actions to full commit SHAs reduces mutable-tag supply-chain risk.
- A protected GitHub environment can pause the release job after a tag is pushed and before artifacts/Release publication. The user chose this approval boundary while declining branch protection on `main`.
- The current 0.2.0 code has not been committed/pushed, so workflow implementation and validation must precede the rebrand commit, CI run, tag, and first release.

## Conclusion

Use two workflows: read-only CI for pull requests/pushes and a tag-triggered GitHub-only release workflow gated by a `release` environment. Build/test with uv, build once, attest artifacts, and create the GitHub Release. Add only CI and license badges before the first release; add a latest-release badge after v0.2.0 exists. Do not configure PyPI or add PyPI/coverage/vanity badges.

## Limits

GitHub environment approval behavior and artifact-attestation availability depend on current repository/account capabilities and must be validated before the first tag. No external configuration or release was changed during research.
