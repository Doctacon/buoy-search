Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/repo-ranking-promotion-policy.md, .10x/decisions/namespace-ranking-defaults.md, .10x/knowledge/repo-search-ranking-defaults.md

# Repo Source and Fixture Routing Validation

## What was observed

A new distributed repo-ranking improvement passed the expanded 13-repo promotion policy and exceeded the user's requested `+2.0` new average-score target.

Promoted default `repo_code` changes:

1. Treat ordinary package-root source files as source paths, not only `src/` and `lib/` files.
   - Examples: `django/http/request.py`, `httpx/_models.py`, `rich/text.py`, `mkdocs/commands/build.py`, `pydantic/type_adapter.py`.
   - Documentation, tests, examples, benchmarks, agent artifacts, fixture/snapshot scaffolds, and resource test fixtures remain non-source.
2. Demote fixture/snapshot scaffold paths (`/fixtures/`, `/snapshots/`, `/resources/test/`, `/tests/data/`) by `0.80x` for queries that are not asking for fixtures, snapshots, or tests.

This is retrieval/ranking-only. It does not change indexing schema, embeddings, namespaces, or row contents.

## Procedure

Baseline was the distribution-validated `cli.py` / `_click/termui.py` / `index.*` subset from `.10x/evidence/2026-06-28-expanded-repo-ranking-basket-validation.md`:

```text
13-repo baseline average score: 70.545
13-repo baseline average P@5:   0.452
```

Hypotheses tested with final-ranker replay over saved live raw candidates from `autoresearch/runs/repo-expanded-basket-20260628/raw-expanded-basket-hits-c200.json`:

| Hypothesis | Avg score Δ | P@5 Δ | Distribution result |
|---|---:|---:|---|
| Broaden source-path recognition beyond `src/`/`lib/` | +1.608 | +0.000 | No regressions; positive on 8 repos; not enough alone for +2.0 |
| Fixture/snapshot scaffold demotion alone | +0.737 | +0.003 | No regressions; positive on 2 repos; not enough alone |
| Broad source + fixture demotion `0.80x` | +2.216 | +0.000 | Pass: no regressions, positive on 8 repos, largest gain share 23.5% |
| Broad source + fixture demotion `0.70x` | +2.438 | +0.003 | No regressions in replay, but stronger than needed; `0.80x` chosen as smaller sufficient change |
| Broad source + fixture demotion `0.60x`/`0.50x`/`0.40x` | +2.337 | +0.003 | No regressions in replay, but stronger than needed |
| Broad source + stronger path/symbol boosts | up to +3.929 | +0.009 | Regressed at least one repo, rejected |
| Broad source + docs/tests/fixture demotion combo | +4.144 | -0.017 | Regressed multiple repos/P@5, rejected |

After implementing the smaller sufficient hypothesis, final validation used direct live evals against the existing 13 repo namespaces:

```bash
uv run turbo-search evals --live --dataset <dataset> \
  --namespace <namespace> --top-k 10 --candidates 200 --json
```

No plan/apply, row writes, stale deletion, or namespace deletion was run for the final validation.

Artifacts:

- `autoresearch/runs/repo-source-fixture-routing-20260628/source-fixture-routing-summary.json`
- `autoresearch/runs/repo-source-fixture-routing-20260628/source-fixture-routing-report.md`
- `autoresearch/runs/repo-source-fixture-routing-20260628/live-eval/live-source-fixture-routing-summary.json`
- `autoresearch/runs/repo-source-fixture-routing-20260628/live-eval/live-source-fixture-routing-report.md`
- per-repo live eval JSON files under `autoresearch/runs/repo-source-fixture-routing-20260628/live-eval/`

## Live result

| Repo | Family | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---|---:|---:|---:|---:|---:|---:|
| turbo-search | original | 87.830 | 87.830 | +0.000 | 0.540 | 0.540 | +0.000 |
| Requests | original | 84.426 | 84.426 | +0.000 | 0.420 | 0.420 | +0.000 |
| Click | original | 72.816 | 72.816 | +0.000 | 0.420 | 0.420 | +0.000 |
| pytest | original | 89.191 | 89.191 | +0.000 | 0.720 | 0.720 | +0.000 |
| Typer | original | 67.280 | 67.719 | +0.440 | 0.500 | 0.500 | +0.000 |
| Black | expanded | 70.389 | 74.499 | +4.110 | 0.400 | 0.400 | +0.000 |
| Ruff | expanded | 36.248 | 41.622 | +5.373 | 0.200 | 0.200 | +0.000 |
| Flask | expanded | 78.831 | 78.831 | +0.000 | 0.480 | 0.480 | +0.000 |
| Django | expanded | 60.983 | 61.515 | +0.533 | 0.320 | 0.320 | +0.000 |
| Pydantic | expanded | 68.541 | 68.686 | +0.145 | 0.320 | 0.320 | +0.000 |
| HTTPX | expanded | 62.238 | 68.221 | +5.983 | 0.480 | 0.480 | +0.000 |
| MkDocs | expanded | 72.561 | 79.322 | +6.762 | 0.560 | 0.560 | +0.000 |
| Rich | expanded | 65.757 | 71.221 | +5.465 | 0.520 | 0.520 | +0.000 |

Aggregate:

```text
Average score: 70.545 -> 72.762 (+2.216)
Average P@5:   0.452  -> 0.452  (+0.000)
Positive repos: 8
Largest gain share: 23.5%
Score regressions: none
P@5 regressions: none
```

The candidate passes `.10x/decisions/repo-ranking-promotion-policy.md`.

## What this supports or challenges

Supports:

- The prior source-path heuristic was too narrow. Modern Python repos often use top-level package directories (`django/`, `httpx/`, `rich/`, `mkdocs/`, `pydantic/`) rather than `src/` or `lib/`.
- Fixture/snapshot scaffold demotion helps large repos such as Ruff and Black without broadly demoting ordinary tests.
- Distributed gains are possible without overfitting to one namespace: 8 of 13 repos improved, and the largest positive contribution was only 23.5% of total positive gain.

Challenges/limits:

- The expanded seed labels are still assistant-drafted.
- Ruff remains low in absolute score (`41.622`), suggesting remaining work around large Rust monorepo fixture/snapshot noise, authority file size, and crate-aware path priors.
- This does not validate stronger source/path-symbol boosts, broad docs demotion, or broad tests demotion; those regressed at least one target in hypothesis replay.

## Conclusion

Promote broad package-root source recognition and conservative fixture/snapshot scaffold demotion in the default `repo_code` ranking profile. The new 13-repo baseline is:

```text
average score = 72.762
average P@5   = 0.452
```
