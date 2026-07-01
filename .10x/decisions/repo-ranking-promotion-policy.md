Status: active
Created: 2026-06-28
Updated: 2026-06-28

# Repo Ranking Promotion Policy

## Context

A five-repo repo-ranking candidate reached the user's reset `+2.0` average-score target, but most of the gain came from Typer. That passed the older no-regression rule while still looking overfit to one corpus.

The user explicitly requested a broader validation basket and a stricter promotion rule that accounts for gain distribution, not just average score.

## Decision

General repo-ranking defaults MUST NOT be promoted solely because the average score improves. Promotion requires expanded-basket evidence and a distribution-aware gate:

1. no repo-level composite-score regression;
2. no repo-level Precision@5 regression;
3. positive composite-score gain on at least 3 repositories;
4. the largest single-repo positive contribution is at most 70% of total positive gain;
5. all-repo average composite score improves.

If a candidate improves average score but fails the distribution gate, treat it as a targeted or overfit candidate rather than a general default. Split and promote only the subset that passes the gate.

Seed labels remain assistant-drafted unless separately human-reviewed. This policy does not claim human approval of the labels.

## Alternatives considered

- Keep the old no-regression average target: rejected because it let a Typer-concentrated gain look like a general repo-search improvement.
- Require every repo to improve: rejected as too strict for ranking changes that are intentionally no-op on many repo shapes.
- Require only no single repo over 70%: rejected as insufficient without also requiring multiple positive repos and no P@5 regressions.

## Consequences

- The full private-module routing candidate is not a general default even though it improves average score without repo-level regressions.
- Ranking improvements may be smaller but better distributed.
- Future default promotions need expanded-basket evidence, not only the original five repos.

## Evidence

- `.10x/evidence/2026-06-28-expanded-repo-ranking-basket-validation.md`
- `.10x/evidence/2026-06-28-repo-source-fixture-routing-validation.md`
- `autoresearch/runs/repo-expanded-basket-20260628/expanded-basket-variant-report.md`
