Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/repo-ranking-promotion-policy.md, .10x/knowledge/repo-search-ranking-defaults.md

# Repo Conventional Entrypoint Routing Validation

## What was observed

A new repo-ranking candidate exceeded the user's requested `+2.0` new average-score target without concentrating the gain in one namespace.

Promoted default `repo_code` changes:

1. Boost Rust crate root entrypoints `crates/<crate>/src/lib.rs` and `crates/<crate>/src/main.rs` by `1.35x` when query tokens match the crate name.
2. Do not apply nested-private demotion to `_internal` package segments when the full path has at least two query-token matches.
3. Add query-aware conventional Python module routing:
   - `core.py` gets `1.20x` for command/runtime queries;
   - `models.py` gets `1.20x` for parameter/field/model metadata queries;
   - `utils.py` gets `0.75x` for parameter metadata queries that are not asking for utility helpers.
4. Demote non-public `__init__.py` files by `0.82x` unless the query asks for public API, exports, module entrypoints, initialization, or top-level behavior.
5. Demote `docs/source/` pages by an additional `0.80x` for non-documentation queries.

This is retrieval/ranking-only. It does not change indexing schema, embeddings, namespaces, row contents, stale rows, or namespace state.

## Procedure

Baseline was the prior distributed source/fixture routing default from `.10x/evidence/2026-06-28-repo-source-fixture-routing-validation.md`:

```text
13-repo baseline average score: 72.762
13-repo baseline average P@5:   0.452
```

Hypotheses were tested first with final-ranker replay over saved live raw candidates from `autoresearch/runs/repo-expanded-basket-20260628/raw-expanded-basket-hits-c200.json`.

| Hypothesis | Replay Δ avg score | Result |
|---|---:|---|
| Source stem boost | +1.497 | Rejected: regressed turbo-search, Typer, and Ruff |
| Path component boost | +1.435 | Rejected: regressed multiple repos |
| Generic test demotion | +1.322 | Rejected: score/P@5 regressions |
| Rust crate root boost alone | +0.744 | Kept only as one part; single-repo gain is insufficient |
| Query-matched `_internal` exemption alone | +0.575 | Kept only as one part; single-repo gain is insufficient |
| `core.py`/`models.py`/`utils.py` conventional routing alone | +0.300 | Kept only as one part; Typer-focused alone is insufficient |
| Combined conventional entrypoint routing | +2.112 | Passed replay distribution gate |

Replay artifacts:

- `autoresearch/runs/repo-conventional-entrypoint-routing-20260701/replay-summary.json`
- `autoresearch/runs/repo-conventional-entrypoint-routing-20260701/replay-report.md`

Validation commands:

```bash
uv run python -m unittest discover -s tests
```

Live validation used direct retrieval-only evals against the existing 13 repo namespaces with `top_k=10`, `candidates=200`, `ranking_mode=file`, `ranking_profile=repo_code`, `ranking_pool=100`, and `ranking_aggregation=adaptive_sum_3`.

No plan/apply command, row write, stale deletion, namespace creation, or namespace deletion was run for final validation.

Live artifacts:

- `autoresearch/runs/repo-conventional-entrypoint-routing-20260701/live-eval/live-summary.json`
- `autoresearch/runs/repo-conventional-entrypoint-routing-20260701/live-eval/live-report.md`
- per-repo live eval JSON files under `autoresearch/runs/repo-conventional-entrypoint-routing-20260701/live-eval/`

## Live result

| Repo | Family | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---|---:|---:|---:|---:|---:|---:|
| turbo-search | original | 87.830 | 87.830 | +0.000 | 0.540 | 0.540 | +0.000 |
| Requests | original | 84.426 | 84.426 | +0.000 | 0.420 | 0.420 | +0.000 |
| Click | original | 72.816 | 72.988 | +0.172 | 0.420 | 0.420 | +0.000 |
| pytest | original | 89.191 | 90.215 | +1.024 | 0.720 | 0.720 | +0.000 |
| Typer | original | 67.719 | 72.673 | +4.954 | 0.500 | 0.520 | +0.020 |
| Black | expanded | 74.499 | 74.499 | +0.000 | 0.400 | 0.400 | +0.000 |
| Ruff | expanded | 41.622 | 51.290 | +9.669 | 0.200 | 0.320 | +0.120 |
| Flask | expanded | 78.831 | 79.291 | +0.460 | 0.480 | 0.520 | +0.040 |
| Django | expanded | 61.515 | 62.068 | +0.553 | 0.320 | 0.360 | +0.040 |
| Pydantic | expanded | 68.686 | 76.885 | +8.199 | 0.320 | 0.400 | +0.080 |
| HTTPX | expanded | 68.221 | 69.584 | +1.363 | 0.480 | 0.480 | +0.000 |
| MkDocs | expanded | 79.322 | 79.414 | +0.092 | 0.560 | 0.560 | +0.000 |
| Rich | expanded | 71.221 | 72.199 | +0.977 | 0.520 | 0.560 | +0.040 |

Aggregate:

```text
Average score: 72.762 -> 74.874 (+2.112)
Average P@5:   0.452  -> 0.478  (+0.026)
Positive repos: 10
Largest gain share: 35.2%
Score regressions: none
P@5 regressions: none
```

The candidate passes `.10x/decisions/repo-ranking-promotion-policy.md`.

Unit validation:

```text
uv run python -m unittest discover -s tests
Ran 147 tests in 2.271s
OK
```

## What this supports or challenges

Supports:

- Distributed improvements can come from several small conventional path priors rather than from a single namespace.
- Rust monorepos need crate-aware root-entrypoint routing; `src/lib.rs` and `src/main.rs` are too generic unless the parent crate name participates in ranking.
- Python `_internal` packages can be authoritative when the full internal path clearly matches the query; demoting them unconditionally loses relevant Pydantic results.
- Conventional `core.py`, `models.py`, and `utils.py` need different treatment depending on whether the query asks for runtime command flow, parameter metadata, or utility helpers.
- Non-public `__init__.py` and `docs/source/` pages are often useful secondary context, but they should not outrank implementation files for ordinary implementation queries.

Challenges/limits:

- Labels are still assistant-drafted, not human-reviewed.
- Ruff remains low in absolute score (`51.290`) despite the large improvement.
- This validates final ranking only over the existing indexed namespaces. It does not validate a new indexing schema or new embeddings.
- The replay hypotheses are not exhaustive; they represent the tested candidates that materially affected the current raw-candidate basket.

## Conclusion

Promote conventional entrypoint routing in the default `repo_code` profile. The new 13-repo baseline is:

```text
average score = 74.874
average P@5   = 0.478
```
