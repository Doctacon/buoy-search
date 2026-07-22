Status: recorded
Created: 2026-07-21
Updated: 2026-07-21
Target: PR #98 label-driven automatic release shaping
Verdict: pass

# Label-Driven Release Automation Shaping Review

## Findings

Independent review confirmed label/SemVer calculations, hatch-vcs feasibility, v0.4 authority, bridge closure, hosted protection, and child sequencing. It identified four blockers:

1. Mutable post-merge PR labels could change target on workflow rerun and create another release for the same SHA.
2. A queued `pull_request_target` auto-merge adapter lacked race/revocation/concurrency and exact-permission semantics.
3. Historical records pointed to replacement active contracts instead of the static contracts under which they executed.
4. Active package/main-push specs inherited omitted normative guarantees from superseded records instead of being regeneration-grade.

## Response

- Replaced post-merge label authority with deterministic merge-commit trailers and required main-push recomputation/equality. Added rejection of any different stable tag/Release already associated with the same main SHA.
- Replaced mutable queued auto-merge/`pull_request_target` with a final job in the readiness workflow after all four checks. It uses per-PR canceling concurrency, no checkout, exact `contents: write`/`pull-requests: write`, current metadata/plan reinspection, `--match-head-commit`, method MERGE, and immutable trailers. Later PR metadata cannot change release identity.
- Repaired historical references to exact superseded static-version/package/release contracts and relabeled historical authority accurately.
- Restated retained package identity/compatibility, exact v0.4 legacy pins/digests, state machine, permissions, triggers, tests, protection, and portability in active specs.
- Added raw disposable hatch-vcs experiment configuration, commands, lock diff, versions, and artifact hashes to research.

## Final rereview findings and response

Final rereview confirmed the initial four blockers resolved, then found two narrow active-contract gaps: duplicate-per-SHA wording named only annotated tags, and protected-branch text still referred to mutable merged-PR labels. It also noted the disposable experiment had not tested the intended ignore rule.

The main-push contract now rejects every different stable tag ref—including lightweight—and every Release/partial state targeting the same SHA. Protected-branch authority now names exact associated PR identity plus immutable merge trailers and makes later labels diagnostic only. Research now states the ignore-rule limit truthfully; the package spec/ticket retain explicit implementation and verification.

## Final bounded rereview

Independent rereview confirmed all remaining blockers resolved: every different stable tag ref including lightweight plus Release/partial state is rejected per SHA; protected authority uses immutable trailers; and research accurately limits the untested ignore rule while active implementation records require it. Exact head `6a01e6f8372b2fefcd16c5be03b5ee166d5227d3` was clean/mergeable with all hosted checks passing.

## Verdict

Pass. PR #98 is eligible for ordinary squash integration to develop.

## Residual risk

The first implementation must prove the same-repository pull-request workflow token can merge through exact protection only after required jobs, and must fail closed if hosted permissions differ.
