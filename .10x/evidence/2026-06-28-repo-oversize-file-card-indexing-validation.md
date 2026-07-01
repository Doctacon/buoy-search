Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-28-repo-search-heavy-ranking-experiments.md

# Repo Oversize File-Card Indexing Validation

## What was observed

An opt-in indexing hypothesis was implemented and live-tested: add metadata-only file cards for oversize files that remain skipped for source chunking. The hypothesis improved Click but failed the no-regression policy and was not promoted as a default.

New opt-in flag:

```text
--repo-oversize-file-cards
```

The flag adds `oversize_file_card` pages for oversize UTF-8 text files using a bounded text sample for path/symbol metadata. It does not add full source chunks for oversize files.

## Procedure

Live writes were explicitly allowed by the user for new experimental namespaces. Plans and applies used new namespaces only, without stale deletion or namespace deletion.

Command shape:

```bash
uv run turbo-search plan <github-repo-url> \
  --namespace <new-namespace> \
  --out-dir artifacts/site-crawls/<new-namespace>-plan-20260628 \
  --repo-oversize-file-cards --json

uv run turbo-search apply \
  --plan artifacts/site-crawls/<new-namespace>-plan-20260628/plan.json \
  --approve --json

uv run turbo-search evals --live \
  --dataset <repo-seed-dataset> \
  --namespace <new-namespace> \
  --top-k 10 --candidates 200 --json
```

Namespaces written:

| Namespace | Rows upserted | Rows deleted |
|---|---:|---:|
| `github-doctacon-turbo-search-v5-oversize-cards` | 541 | 0 |
| `github-psf-requests-v4-oversize-cards` | 736 | 0 |
| `github-pallets-click-v4-oversize-cards` | 1215 | 0 |
| `github-pytest-dev-pytest-v4-oversize-cards` | 3582 | 0 |
| `github-fastapi-typer-v4-oversize-cards` | 2515 | 0 |

Artifacts:

- `autoresearch/runs/repo-oversize-file-cards-20260628/live-apply/`
- `autoresearch/runs/repo-oversize-file-cards-20260628/*-oversize-cards.json`

## Result

Compared against the example-scaffold baseline:

| Repo | Baseline score | Oversize-card score | Δ score | Baseline P@5 | Oversize-card P@5 | Δ P@5 |
|---|---:|---:|---:|---:|---:|---:|
| turbo-search | 87.760 | 84.619 | -3.141 | 0.540 | 0.520 | -0.020 |
| Requests | 84.426 | 84.273 | -0.153 | 0.420 | 0.420 | +0.000 |
| Click | 72.816 | 78.321 | +5.506 | 0.420 | 0.460 | +0.040 |
| pytest | 89.191 | 88.023 | -1.169 | 0.720 | 0.700 | -0.020 |
| Typer | 66.121 | 61.380 | -4.741 | 0.480 | 0.460 | -0.020 |

Averages:

- Score: `80.063 -> 79.323` (`-0.740`)
- P@5: `0.516 -> 0.512` (`-0.004`)

## What this supports or challenges

Supports:

- Oversize cards can recover missing authority files for Click, especially `src/click/core.py`.
- Metadata-only oversize cards are still strong enough to perturb ranking.

Challenges:

- The hypothesis regresses four of five repositories by composite score and three by P@5.
- Oversize-card indexing is not default-safe under the current five-repo no-regression policy.

## Conclusion

Keep `--repo-oversize-file-cards` opt-in only. Do not promote oversize file-card indexing as a default without a query-routed strategy or broader labels that explicitly require skipped authority files.
