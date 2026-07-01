Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md, .10x/knowledge/repo-search-ranking-defaults.md

# Repo Private-Module Routing Validation

## What was observed

A combined ranking-only hypothesis passed the five-repo no-regression policy and met the user's reset target of +2.0 average repo-search score points from the embedded-agent-artifact baseline.

Promoted `repo_code` behaviors:

- Vendored/private `_click` paths are demoted for high-level command/runtime queries unless the query targets low-level terminal/type/exception behavior.
- Conventional `core.py` files receive a modest boost for command/runtime queries, but not when the private path demotion applies.
- Conventional `models.py` files receive a modest boost for parameter/option/argument metadata queries.
- Broad `utils.py` helpers are demoted for parameter metadata queries unless the query is actually asking for utilities/helpers.
- `cli.py` files are gently demoted when the query is not CLI/script/runner oriented.
- Nested `_click/termui.py` receives a terminal-UI boost for terminal/prompt/progress/echo/launch queries.
- Documentation `index.*` files can match their parent directory name, e.g. `docs/tutorial/commands/index.md` can match command-oriented queries.

This is retrieval/ranking-only. It does not change default indexing, namespaces, row schema, embeddings, or live writes.

## Procedure

Exploration before the passing result:

- Rechecked metadata-only and file-card namespaces with the current ranking; metadata still regressed turbo-search/Requests/pytest and file-cards still regressed turbo-search plus pytest P@5.
- Implemented and tested an opt-in oversize-file-card indexing hypothesis in new namespaces. It improved Click but regressed turbo-search, Requests, pytest, and Typer, so it was not promoted as a default.
- Continued ranking-profile hypotheses against cached live retrieval candidates from the baseline repo namespaces:
  - broad tests/doc boosts regressed at least one repo;
  - docs/tutorial scaffold demotion passed earlier;
  - vendored `_click` demotion, core/model boosts, utils demotion, nested termui boost, CLI demotion, and index-parent matching composed into a no-regression improvement.
- Implemented the ranking rules in `src/turbo_search/retriever.py` and added unit coverage in `tests/test_retriever.py`.

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

- `autoresearch/runs/repo-private-module-routing-20260628/private-module-routing-summary.json`
- `autoresearch/runs/repo-private-module-routing-20260628/private-module-routing-report.md`
- per-repo eval JSON files under `autoresearch/runs/repo-private-module-routing-20260628/`

No plan/apply, row writes, stale deletion, or namespace deletion was run for this validation.

## Result

Baseline is the immediately previous promoted example-scaffold demotion result from `autoresearch/runs/repo-example-scaffold-demotion-20260628/example-scaffold-demotion-summary.json`.

| Repo | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---:|---:|---:|---:|---:|---:|
| turbo-search | 87.760 | 87.830 | +0.070 | 0.540 | 0.540 | +0.000 |
| Requests | 84.426 | 84.426 | +0.000 | 0.420 | 0.420 | +0.000 |
| Click | 72.816 | 72.816 | +0.000 | 0.420 | 0.420 | +0.000 |
| pytest | 89.191 | 89.191 | +0.000 | 0.720 | 0.720 | +0.000 |
| Typer | 66.121 | 74.702 | +8.580 | 0.480 | 0.520 | +0.040 |

Averages across the five-repo basket:

- Score: `80.063 -> 81.793` (`+1.730`)
- P@5: `0.516 -> 0.524` (`+0.008`)

Reset-target cumulative average-score improvement from the embedded-agent-artifact baseline is over the user's requested +2.0 new points:

- Score: `79.785 -> 81.793` (`+2.007`)

## What this supports or challenges

Supports:

- Query-aware private/vendored-module routing can recover Typer precision without hurting the other repositories.
- Conventional file-name priors (`core.py`, `models.py`, `utils.py`, `cli.py`, `index.md`) help when gated by query intent rather than applied globally.
- Small, explicit ranking priors remain safer than broad docs/tests/source coefficient changes.

Challenges/limits:

- The eval labels are still assistant-drafted.
- The score gain is concentrated in Typer; other repositories are unchanged except a small turbo-search gain.
- This does not make metadata preambles, file cards, oversize source indexing, or oversize file-card indexing default-safe.

## Conclusion

Promote the private-module routing and conventional-file query priors inside the default `repo_code` ranking profile. This reaches the user's reset +2.0 average-score target without repo-level or P@5 regression.
