Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/repo-ranking-promotion-policy.md, .10x/decisions/namespace-ranking-defaults.md, .10x/knowledge/repo-search-ranking-defaults.md

# Expanded Repo Ranking Basket Validation

## What was observed

The five-repo `+2.007` private-module routing candidate did not satisfy a distribution-aware promotion bar after adding eight more repositories. It still had no repo-level score/P@5 regressions, but most of the total gain remained concentrated in Typer.

A smaller subset did pass the expanded distribution gate and was kept as the default candidate:

- gently demote `cli.py` for non-CLI/script/runner queries;
- boost nested `_click/termui.py` for terminal UI queries such as prompt/progress/echo/launch;
- let `index.*` files match their parent directory name, e.g. `docs/.../commands/index.md` for command-oriented queries.

The following five-repo candidate pieces were rejected as general defaults because their gains remained one-repo concentrated:

- special vendored `_click` demotion unless low-level Click terms are present;
- `core.py` command/runtime boost;
- `models.py` parameter metadata boost;
- parameter-query `utils.py` demotion.

## Procedure

The user approved expanding validation, creating new namespaces, and rerunning the candidate/components.

New assistant-drafted repo eval datasets were added:

- `src/turbo_search/data/black_repo_search_seed_evals.json`
- `src/turbo_search/data/ruff_repo_search_seed_evals.json`
- `src/turbo_search/data/flask_repo_search_seed_evals.json`
- `src/turbo_search/data/django_repo_search_seed_evals.json`
- `src/turbo_search/data/pydantic_repo_search_seed_evals.json`
- `src/turbo_search/data/httpx_repo_search_seed_evals.json`
- `src/turbo_search/data/mkdocs_repo_search_seed_evals.json`
- `src/turbo_search/data/rich_repo_search_seed_evals.json`

Each dataset contains five source-backed cases. Judgments were verified against the generated default-indexing manifests so labels point to indexed files under the default 50 KiB file cap.

New repositories were planned locally, preflighted, then live-applied to new namespaces only. No stale deletion or namespace deletion was run.

| Namespace | Repository | Rows/embeddings upserted | Rows deleted |
|---|---|---:|---:|
| `github-psf-black-v1` | `psf/black` | 2,238 | 0 |
| `github-astral-sh-ruff-v1` | `astral-sh/ruff` | 56,407 | 0 |
| `github-pallets-flask-v1` | `pallets/flask` | 1,341 | 0 |
| `github-django-django-v1` | `django/django` | 36,447 | 0 |
| `github-pydantic-pydantic-v1` | `pydantic/pydantic` | 7,377 | 0 |
| `github-encode-httpx-v1` | `encode/httpx` | 963 | 0 |
| `github-mkdocs-mkdocs-v1` | `mkdocs/mkdocs` | 1,930 | 0 |
| `github-textualize-rich-v1` | `Textualize/rich` | 4,221 | 0 |

Artifacts:

- `autoresearch/runs/repo-expanded-basket-20260628/preflight/`
- `autoresearch/runs/repo-expanded-basket-20260628/live-apply/`
- `autoresearch/runs/repo-expanded-basket-20260628/raw-expanded-basket-hits-c200.json`
- `autoresearch/runs/repo-expanded-basket-20260628/evaluate_repo_ranking_variants.py`
- `autoresearch/runs/repo-expanded-basket-20260628/expanded-basket-variant-summary.json`
- `autoresearch/runs/repo-expanded-basket-20260628/expanded-basket-variant-report.md`

Variant evaluation used one live raw candidate retrieval pass (`top_k=200`, `candidates=200`, chunk mode) per case, then replayed final file-level ranking variants offline over the same raw candidates. After reverting the rejected pieces, a direct check confirmed current `src/turbo_search/retriever.py` ranking matches the accepted `cli_termui_index_only` variant on the saved expanded raw hits.

## Distribution policy

A candidate general default passes only if it has:

1. no repo-level composite-score regression;
2. no repo-level Precision@5 regression;
3. positive composite-score gain on at least 3 repositories;
4. largest single-repo positive contribution at most 70% of total positive gain;
5. all-repo average composite score improvement.

## Results

Baseline is the example-scaffold promoted baseline with private-module routing and conventional-file priors disabled.

| Variant | Avg score all | Δ all | Avg P@5 all | Δ P@5 all | Avg score original five | Avg score expanded eight | Positive repos | Largest gain share | Pass? |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| baseline example-scaffold | 70.310 | +0.000 | 0.448 | +0.000 | 80.063 | 64.214 | 0 | 0.0% | no |
| private `_click` only | 70.519 | +0.209 | 0.448 | +0.000 | 80.606 | 64.214 | 1 | 100.0% | no |
| `core.py`/`models.py`/`utils.py` only | 70.723 | +0.414 | 0.449 | +0.002 | 81.138 | 64.214 | 1 | 100.0% | no |
| `cli.py`/`termui.py`/`index.*` only | 70.545 | +0.235 | 0.452 | +0.005 | 80.309 | 64.443 | 3 | 59.9% | yes |
| full private-module candidate | 71.116 | +0.806 | 0.454 | +0.006 | 81.793 | 64.443 | 3 | 81.8% | no |

The full candidate's non-zero repo deltas were:

| Repo | Family | Baseline score | Full score | Δ score | Baseline P@5 | Full P@5 | Δ P@5 |
|---|---|---:|---:|---:|---:|---:|---:|
| turbo-search | original | 87.760 | 87.830 | +0.070 | 0.540 | 0.540 | +0.000 |
| Typer | original | 66.121 | 74.702 | +8.580 | 0.480 | 0.520 | +0.040 |
| Django | expanded | 59.150 | 60.983 | +1.833 | 0.280 | 0.320 | +0.040 |

The accepted subset's non-zero repo deltas were:

| Repo | Family | Baseline score | Accepted score | Δ score | Baseline P@5 | Accepted P@5 | Δ P@5 |
|---|---|---:|---:|---:|---:|---:|---:|
| turbo-search | original | 87.760 | 87.830 | +0.070 | 0.540 | 0.540 | +0.000 |
| Typer | original | 66.121 | 67.280 | +1.158 | 0.480 | 0.500 | +0.020 |
| Django | expanded | 59.150 | 60.983 | +1.833 | 0.280 | 0.320 | +0.040 |

## What this supports or challenges

Supports:

- The user's concern was valid: the prior `+2.007` target was too concentrated in Typer.
- A distribution-aware policy catches concentrated average-score wins that the previous no-regression gate missed.
- `cli.py`/`termui.py`/`index.*` routing appears broadly safer across 13 repos: three positive repos, no score/P@5 regressions, and largest gain share below 70%.

Challenges:

- New labels are still assistant-drafted and not human approved.
- The expanded basket's average score is lower than the original five-repo basket, especially for Ruff, partly because default indexing still skips oversize authority files and the Ruff corpus is large.
- The full private-module candidate remains useful as a targeted Typer improvement but is not justified as a general default.

## Conclusion

Do not keep the full private-module routing candidate as a general default. Reclassify it as overfit/targeted pending more evidence.

Keep only the smaller accepted subset (`cli.py` demotion for non-CLI queries, `_click/termui.py` terminal boost, `index.*` parent-directory matching) in the default `repo_code` ranking profile.
