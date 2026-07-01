Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/namespace-ranking-defaults.md, .10x/knowledge/repo-search-ranking-defaults.md

# Repo Embedded Agent Artifact Demotion Validation

## What was observed

A fourth ranking-only hypothesis passed the five-repo no-regression policy after the nested-private path demotion baseline: demote agent/project-memory artifact directories even when they are embedded below another repository path segment.

Promoted behavior in the `repo_code` profile:

- Agent artifact directory segments are detected anywhere in the repo path, not only at the repository root.
- Demoted segments: `.10x`, `.agents`, `.claude`, `.cursor`, `.loom`, `.pi`, `.turbo-search`.
- Root-only run artifact directories `artifacts/` and `autoresearch/` remain demoted as before.

This catches paths such as `typer/.agents/skills/typer/SKILL.md`, which were not covered by the previous root-only artifact demotion.

This is retrieval/ranking-only. It does not change indexing, namespaces, row schema, embeddings, or live writes.

## Procedure

Exploration before the passing result:

- Continued ranking-profile hypotheses against cached live retrieval candidates from the baseline repo namespaces.
- Tested root package source boosts, top-level source-like boosts, filename/path overlap boosts, test/docs query boosts, dunder/internal file demotions, nested-private path demotion, and embedded agent-artifact demotion.
- Root package boosts were smaller; filename/path overlap and dunder/internal demotions regressed at least one repo; embedded agent-artifact demotion passed the no-regression policy and pushed the cumulative average-score improvement over the user's 2.0-point target.
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

- `autoresearch/runs/repo-embedded-agent-artifact-demotion-20260628/embedded-agent-artifact-demotion-summary.json`
- `autoresearch/runs/repo-embedded-agent-artifact-demotion-20260628/embedded-agent-artifact-demotion-report.md`
- per-repo eval JSON files under `autoresearch/runs/repo-embedded-agent-artifact-demotion-20260628/`

No plan/apply, row writes, stale deletion, or namespace deletion was run for this validation.

## Result

Baseline is the immediately previous promoted nested-private path demotion result from `autoresearch/runs/repo-nested-private-path-demotion-20260628/nested-private-path-demotion-summary.json`.

| Repo | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---:|---:|---:|---:|---:|---:|
| turbo-search | 87.760 | 87.760 | +0.000 | 0.540 | 0.540 | +0.000 |
| Requests | 84.426 | 84.426 | +0.000 | 0.420 | 0.420 | +0.000 |
| Click | 72.816 | 72.816 | +0.000 | 0.420 | 0.420 | +0.000 |
| pytest | 89.191 | 89.191 | +0.000 | 0.720 | 0.720 | +0.000 |
| Typer | 64.411 | 64.734 | +0.323 | 0.440 | 0.460 | +0.020 |

Averages across the five-repo basket:

- Score: `79.721 -> 79.785` (`+0.065`)
- P@5: `0.508 -> 0.512` (`+0.004`)

Cumulative average-score improvement from the pre-example-demotion baseline is now over the user's target:

- Score: `77.765 -> 79.785` (`+2.020`)

## What this supports or challenges

Supports:

- Repository ingest can encounter hidden agent/artifact directories nested below a package or project subdirectory, not just at the root.
- Treating agent artifact paths as path segments is safer than root-only prefix matching.
- The fix is hygiene-oriented and does not require reindexing; it is a ranking-only guardrail for existing and future namespaces.

Challenges/limits:

- The eval labels are still assistant-drafted.
- The improvement is concentrated in Typer, where an embedded `.agents/` path was present in retrieved candidates.
- This does not make metadata preambles, file cards, oversize indexing, or broad path/filename overlap boosts default-safe.

## Conclusion

Promote embedded agent-artifact path-segment demotion inside the default `repo_code` ranking profile. It is the next valid no-regression improvement after nested private path-segment demotion and brings the cumulative five-repo average-score gain above 2.0 points.
