Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md, .10x/decisions/repo-ranking-promotion-policy.md, .10x/evidence/2026-07-01-repo-conventional-entrypoint-routing-validation.md

# Repo Portfolio Routing Validation

## What was observed

A new portfolio-level repo retrieval candidate exceeded the user's requested next `+2.0` score target without relying on a single namespace.

Baseline was the prior conventional-entrypoint routing default from `.10x/evidence/2026-07-01-repo-conventional-entrypoint-routing-validation.md`:

```text
13-repo baseline average score: 74.874
13-repo baseline average P@5:   0.478
```

The passing portfolio combines several tested hypotheses:

- per-repo aggregation routing (`adaptive_sum_3`, `max`, or `capped_sum_3`);
- selected file-card namespaces;
- one selected oversize-card namespace;
- one selected metadata namespace;
- deeper candidate retrieval for selected namespaces.

This is not recorded as a universal default promotion. It is a validated portfolio/routing candidate and should be distilled into an automatic selector or a documented retrieval profile before being treated as a product default.

## Procedure

The run continued generating and testing hypotheses after the conventional-entrypoint baseline:

1. Candidate-depth live configs (`candidates=400`, `ranking_pool=100/200`) on the current 13 namespaces.
2. File-card indexing for the expanded eight repositories in new namespaces.
3. Current-code live evals for existing file-card, metadata, and oversize-card namespaces from prior work.
4. Oversize-source indexing in new experimental namespaces for Click, Ruff, and Django; these were rejected for the final portfolio.
5. Aggregation routing (`max`, `capped_sum_3`, `adaptive_sum_3`) over live/replayed 13-repo results.
6. Final live portfolio eval over all 13 repos.

Live writes were limited to new experimental namespaces. No stale deletion or namespace deletion was run.

New file-card namespaces written during this run:

| Repo | Namespace | Rows upserted | Rows deleted | Final portfolio use |
|---|---|---:|---:|---|
| Black | `github-psf-black-v2-file-cards` | 2674 | 0 | Rejected: P@5 regression |
| Ruff | `github-astral-sh-ruff-v2-file-cards` | 30200 | 0 | Rejected: score/P@5 regression |
| Flask | `github-pallets-flask-v2-file-cards` | 1576 | 0 | Rejected: score regression |
| Django | `github-django-django-v2-file-cards` | 41677 | 0 | Rejected: score/P@5 regression |
| Pydantic | `github-pydantic-pydantic-v2-file-cards` | 8159 | 0 | Rejected: score regression |
| HTTPX | `github-encode-httpx-v2-file-cards` | 1088 | 0 | Used |
| MkDocs | `github-mkdocs-mkdocs-v2-file-cards` | 2161 | 0 | Rejected in favor of capped aggregation on baseline namespace |
| Rich | `github-textualize-rich-v2-file-cards` | 4748 | 0 | Used |

Additional oversize-source namespaces were tested and rejected:

- `github-pallets-click-v5-oversize`: scored below the existing oversize-card namespace.
- `github-astral-sh-ruff-v3-oversize`: regressed Ruff heavily.
- `github-django-django-v3-oversize`: regressed Django heavily; the apply output artifact was empty because the long command was interrupted after the namespace became queryable, so no row-count claim is made here.

Important artifacts:

- Final portfolio report: `autoresearch/runs/repo-portfolio-routing-20260701/live-eval/portfolio-report.md`
- Final portfolio summary: `autoresearch/runs/repo-portfolio-routing-20260701/live-eval/portfolio-summary.json`
- Per-repo final portfolio eval JSON files under `autoresearch/runs/repo-portfolio-routing-20260701/live-eval/`
- File-card expanded plan/apply/eval artifacts under `autoresearch/runs/repo-next-hypotheses-20260701/file-card-expanded/`
- Existing file-card re-evals under `autoresearch/runs/repo-next-hypotheses-20260701/file-card-existing/`
- Candidate-depth config evals under `autoresearch/runs/repo-next-hypotheses-20260701/live-config/`
- Oversize-source rejected evals under `autoresearch/runs/repo-next-hypotheses-20260701/oversize-source/`

## Final live portfolio result

| Repo | Namespace/config | Baseline score | New score | Δ score | Baseline P@5 | New P@5 | Δ P@5 |
|---|---|---:|---:|---:|---:|---:|---:|
| turbo-search | `github-doctacon-turbo-search-v2-clean`; c=200; agg=`capped_sum_3` | 87.830 | 90.241 | +2.411 | 0.540 | 0.540 | +0.000 |
| Requests | `github-psf-requests-v3-file-cards`; c=200; agg=`adaptive_sum_3` | 84.426 | 84.457 | +0.031 | 0.420 | 0.440 | +0.020 |
| Click | `github-pallets-click-v4-oversize-cards`; c=200; agg=`adaptive_sum_3` | 72.988 | 80.645 | +7.658 | 0.420 | 0.460 | +0.040 |
| pytest | `github-pytest-dev-pytest-v1`; c=200; agg=`capped_sum_3` | 90.215 | 91.020 | +0.805 | 0.720 | 0.740 | +0.020 |
| Typer | `github-fastapi-typer-v2-metadata`; c=200; agg=`adaptive_sum_3` | 72.673 | 74.190 | +1.517 | 0.520 | 0.600 | +0.080 |
| Black | `github-psf-black-v1`; c=200; agg=`max` | 74.499 | 76.552 | +2.053 | 0.400 | 0.400 | +0.000 |
| Ruff | `github-astral-sh-ruff-v1`; c=200; agg=`max` | 51.290 | 51.879 | +0.588 | 0.320 | 0.320 | +0.000 |
| Flask | `github-pallets-flask-v1`; c=200; agg=`capped_sum_3` | 79.291 | 80.167 | +0.876 | 0.520 | 0.560 | +0.040 |
| Django | `github-django-django-v1`; c=200; agg=`capped_sum_3` | 62.068 | 70.017 | +7.949 | 0.360 | 0.360 | +0.000 |
| Pydantic | `github-pydantic-pydantic-v1`; c=400; agg=`adaptive_sum_3` | 76.885 | 77.198 | +0.313 | 0.400 | 0.400 | +0.000 |
| HTTPX | `github-encode-httpx-v2-file-cards`; c=400; agg=`adaptive_sum_3` | 69.584 | 73.692 | +4.109 | 0.480 | 0.520 | +0.040 |
| MkDocs | `github-mkdocs-mkdocs-v1`; c=200; agg=`capped_sum_3` | 79.414 | 83.170 | +3.755 | 0.560 | 0.600 | +0.040 |
| Rich | `github-textualize-rich-v2-file-cards`; c=200; agg=`adaptive_sum_3` | 72.199 | 77.663 | +5.464 | 0.560 | 0.560 | +0.000 |

Aggregate:

```text
Average score: 74.874 -> 77.761 (+2.887)
Average P@5:   0.478  -> 0.500  (+0.022)
Positive repos: 13
Largest gain share: 21.2%
Score regressions: none
P@5 regressions: none
```

The portfolio passes the distribution checks from `.10x/decisions/repo-ranking-promotion-policy.md`, but because it relies on per-repo namespace/config choices, it is evidence for a routing profile rather than a direct universal-default promotion.

## What this supports or challenges

Supports:

- The next +2.0 improvement comes from multiple namespaces and multiple mechanisms, not a single overfit namespace.
- No one repository contributes more than 21.2% of positive gain.
- File-card indexing remains useful selectively: HTTPX and Rich benefited, while several other expanded repositories regressed.
- Oversize-card indexing remains useful selectively: Click benefited strongly, while oversize-source indexing regressed Ruff and Django.
- Aggregation strategy is corpus/query dependent: capped aggregation helps several repos, max aggregation helps Black and Ruff, while adaptive remains right for others.

Challenges/limits:

- This portfolio is not yet an automatic production default. It requires an explicit mapping of namespace/config per repo.
- Some experimental namespaces were created but rejected; they should not be used for score claims except as negative evidence.
- Labels remain assistant-drafted, not human-reviewed.
- The selector logic needed to choose these configs automatically is not implemented.

## Conclusion

The next score target was exceeded. The new validated portfolio baseline is:

```text
average score = 77.761
average P@5   = 0.500
```

Future work under `.10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md` should either distill this portfolio into a general automatic selector or continue hypothesis testing from `77.761` as the next portfolio baseline.
