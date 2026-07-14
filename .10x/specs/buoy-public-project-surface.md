Status: active
Created: 2026-07-14
Updated: 2026-07-14

# Buoy Public Project Surface

## Purpose and scope

Add the minimal governance, release documentation, metadata, and truthful badges expected from a public showcase repository without bloating the README.

## Behavior

- README MUST preserve details-on-demand and approximately 100 lines or fewer.
- Before the first release, README MUST show a working CI badge linked to `ci.yml` and an Apache-2.0 license badge. It MUST NOT show PyPI, downloads, stars, coverage, latest-release, or security badges without backing systems.
- After `v0.2.0` exists, the release ticket MAY add a latest-GitHub-release badge if README remains within the policy.
- Add `CHANGELOG.md` using a concise Keep-a-Changelog/SemVer structure with an Unreleased section and 0.2.0 rebrand entry.
- Add `CONTRIBUTING.md` with setup, test, style/scope, pull-request, and safety expectations that match current repository mechanics.
- Add `SECURITY.md` directing private vulnerability reports through GitHub Security Advisories and defining supported versions without inventing an email address.
- Add `docs/releasing.md` as the canonical maintainer release procedure; README links to detailed contributor/release material only if it remains concise.
- Package metadata SHOULD include accurate development status, audience, license, Python-version, and topic classifiers/keywords appropriate to the current project.
- Current docs MUST state that 0.2 is GitHub-only and not available from PyPI.

## Constraints

- No Code of Conduct contact identity is invented; adding one requires a separate ratified contact path.
- No issue templates, funding links, domain, social handles, or dependency bot are added unless separately requested.
- No badge may imply branch protection, coverage measurement, package publication, or security scanning that does not exist.

## Verification

Validate local links, README limits, badge targets, changelog/version coherence, package metadata, release-doc/workflow agreement, full tests, and independent editorial/technical review.
