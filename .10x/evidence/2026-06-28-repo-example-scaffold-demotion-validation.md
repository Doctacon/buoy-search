Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md, .10x/knowledge/repo-search-ranking-defaults.md

# Repo Example Scaffold Demotion Validation

## What was observed

A fifth ranking-only hypothesis passed the five-repo no-regression policy after the embedded agent-artifact demotion baseline: apply an extra demotion to example/tutorial scaffold paths for non-example queries.

Promoted behavior in the `repo_code` profile:

- Paths under `docs_src/` receive an additional `0.80` multiplier for non-example/tutorial queries.
- Paths under `tests/test_tutorial/` receive a `0.80` multiplier for non-example/tutorial queries.
- Existing example intent tokens (`example`, `examples`, `sample`, `samples`, `tutorial`, `tutorials`, `demo`, `demos`) exempt the added demotion.

`docs_src/` was already covered by the generic example-path demotion; this extra multiplier handles generated/example source snippets that still distract from implementation files. `tests/test_tutorial/` is treated as tutorial-example validation rather than general implementation test evidence unless the query asks for examples/tutorials.

This is retrieval/ranking-only. It does not change indexing, namespaces, row schema, embeddings, or live writes.

## Procedure

Exploration before the passing result:

- Continued ranking-profile hypotheses against cached live retrieval candidates from the current baseline repo namespaces.
- Tested root package source boosts, top-level source-like boosts, filename/path overlap boosts, test/docs query boosts, dunder/internal file demotions, embedded artifact demotion, `docs_src/` demotion, `tests/test_tutorial/` demotion, and combinations.
- `docs_src/` alone improved Typer by `+0.471`; `tests/test_tutorial/` alone improved Typer by `+0.917`; together they improved Typer by `+1.387` without moving the other validation repos.
- Implemented the demotion in `src/turbo_search/retriever.py` and added unit coverage in `tests/test_retriever.py`.

Live validation command shape:

```bash
uv run turbo-search evals --live --dataset <repo-seed-dataset> \
  --namespace <existing-baseline-namespace> \
  --top-k 10 --candidates 200 --json
```

Namespaces:

- `github-doctacon-turbo-search-v2-clean`
- `github-psf-requests-v1`
- `github-pallets-click-v1`
- `github-pytest-dev-pytest-v1`
- `github-fastapi-typer-v1`

Artifacts:

- `autoresearch/runs/repo-example-scaffold-demotion-20260628/example-scaffold-demotion-summary.json`
- `autoresearch/runs/repo-example-scaffold-demotion-20260628/example-scaffold-demotion-report.md`
- per-repo eval JSON files under `autoresearch/runs/repo-example-scaffold-demotion-20260628/`

No plan/apply, row writes, stale deletion, or namespace deletion was run for this validation.

## Result

Baseline is the immediately previous promoted embedded agent-artifact demotion result from `autoresearch/runs/repo-embedded-agent-artifact-demotion-20260628/embedded-agent-artifact-demotion-summary.json`.

| Repo | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---:|---:|---:|---:|---:|---:|
| turbo-search | 87.760 | 87.760 | +0.000 | 0.540 | 0.540 | +0.000 |
| Requests | 84.426 | 84.426 | +0.000 | 0.420 | 0.420 | +0.000 |
| Click | 72.816 | 72.816 | +0.000 | 0.420 | 0.420 | +0.000 |
| pytest | 89.191 | 89.191 | +0.000 | 0.720 | 0.720 | +0.000 |
| Typer | 64.734 | 66.121 | +1.387 | 0.460 | 0.480 | +0.020 |

Averages across the five-repo basket:

- Score: `79.785 -> 80.063` (`+0.277`)
- P@5: `0.512 -> 0.516` (`+0.004`)

New-target cumulative average-score improvement after the user's reset is:

- Score: `79.785 -> 80.063` (`+0.277`)

## What this supports or challenges

Supports:

- Generated tutorial/example source snippets and tutorial example tests can be strong distractors for implementation-oriented repo queries.
- Treating `tests/test_tutorial/` differently from ordinary tests is useful; ordinary tests retain the existing light boost.
- Query-aware exemption keeps explicit tutorial/example queries eligible to surface tutorial scaffold files.

Challenges/limits:

- The eval labels are still assistant-drafted.
- The improvement is concentrated in Typer; the other validation repos are unchanged.
- This does not make metadata preambles, file cards, oversize indexing, or broad path/filename overlap boosts default-safe.

## Conclusion

Promote example scaffold path demotion inside the default `repo_code` ranking profile. It is the next valid no-regression improvement after embedded agent-artifact path-segment demotion.
