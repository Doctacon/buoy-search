Status: recorded
Created: 2026-07-21
Updated: 2026-07-21
Target: PR #88 pre-ratification head `a1e6519aee06e0e49bdd1521219c4cd44456e5a1`
Verdict: concerns

# Simple Main Release Automation Shaping Review

## Findings

Independent review confirmed the user's upstream choices and the feasibility of GitHub permissions, locked validation, build-once artifact checks, clean installation, tokenizer smoke, no-PyPI, and no-Turbopuffer boundaries.

It blocked the initial drafts on eight issues: strict freshness still implied ancestry ceremony; partial-state repair contradicted permanent failure; deterministic build/race/REST/provenance mechanics were incomplete; hosted last-push state conflicted with records and transition order was vague; supersession/open-v0.4 scope was incomplete; environment deletion was optional; stable-version/changelog/tag/release semantics remained inferred; and the managed-platform exception lacked a self-hosted migration path.

## Resolution checkpoint

The reviewer proposed dropping main strict freshness/main-ancestor enforcement, validating GitHub's prospective merge result, stable `MAJOR.MINOR.PATCH` only, deterministic serialized build/publish, exact REST/provenance mechanics, permanent failure for all partial/mismatched states, exact main/develop protection, mandatory environment deletion, complete supersession/record reconciliation, and a repository-local self-hosted migration path.

The user confirmed the repaired simplest-flow contract, explicitly disabling main last-push approval while retaining the previously selected main force-push allowance and prohibiting its use.

## Verdict

Initial head: concerns. The exact concerns and reviewer checkpoint became the user-ratified repair contract; active specifications incorporate them. No implementation or external mutation is authorized outside the bounded implementation tickets.

## Residual risk

The first end-to-end passing readiness run requires a future stable version bump and real develop-to-main PR. This work does not choose that version.
