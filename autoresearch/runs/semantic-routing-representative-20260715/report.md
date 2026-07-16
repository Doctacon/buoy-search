# Representative Semantic Namespace Routing Experiment

## Result

This run measures whether each assistant-drafted public-project question routes to its dataset's home namespace. It is descriptive source-attribution evidence, not product ground truth.

| Strategy | MRR | Recall@1 | Recall@3 | Recall@5 | Unranked | Evaluated |
|---|---:|---:|---:|---:|---:|---:|
| oracle | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 90 |
| lexical | 0.864815 | 0.822222 | 0.911111 | 0.911111 | 8 | 90 |
| semantic | 0.913246 | 0.877778 | 0.933333 | 0.944444 | 0 | 90 |
| hybrid_rrf | 0.933153 | 0.900000 | 0.955556 | 0.955556 | 0 | 90 |

Route fan-out is fixed at five for reporting; no promotion threshold is defined.

## oracle per repository

| Repository | MRR | R@1 | R@3 | R@5 | Unranked | Evaluated |
|---|---:|---:|---:|---:|---:|---:|
| black | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| buoy | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |
| click | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |
| django | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| flask | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| httpx | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| mkdocs | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pydantic | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pytest | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |
| requests | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |
| rich | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| ruff | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| typer | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |

## lexical per repository

| Repository | MRR | R@1 | R@3 | R@5 | Unranked | Evaluated |
|---|---:|---:|---:|---:|---:|---:|
| black | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| buoy | 0.500000 | 0.500000 | 0.500000 | 0.500000 | 5 | 10 |
| click | 0.900000 | 0.900000 | 0.900000 | 0.900000 | 1 | 10 |
| django | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| flask | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| httpx | 0.900000 | 0.800000 | 1.000000 | 1.000000 | 0 | 5 |
| mkdocs | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pydantic | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pytest | 0.933333 | 0.900000 | 1.000000 | 1.000000 | 0 | 10 |
| requests | 0.800000 | 0.800000 | 0.800000 | 0.800000 | 2 | 10 |
| rich | 0.900000 | 0.800000 | 1.000000 | 1.000000 | 0 | 5 |
| ruff | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| typer | 0.750000 | 0.500000 | 1.000000 | 1.000000 | 0 | 10 |

## semantic per repository

| Repository | MRR | R@1 | R@3 | R@5 | Unranked | Evaluated |
|---|---:|---:|---:|---:|---:|---:|
| black | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| buoy | 0.506710 | 0.400000 | 0.500000 | 0.600000 | 0 | 10 |
| click | 0.900000 | 0.800000 | 1.000000 | 1.000000 | 0 | 10 |
| django | 0.900000 | 0.800000 | 1.000000 | 1.000000 | 0 | 5 |
| flask | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| httpx | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| mkdocs | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pydantic | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pytest | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |
| requests | 0.862500 | 0.800000 | 0.900000 | 0.900000 | 0 | 10 |
| rich | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| ruff | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| typer | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |

## hybrid_rrf per repository

| Repository | MRR | R@1 | R@3 | R@5 | Unranked | Evaluated |
|---|---:|---:|---:|---:|---:|---:|
| black | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| buoy | 0.685877 | 0.600000 | 0.700000 | 0.700000 | 0 | 10 |
| click | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 10 |
| django | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| flask | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| httpx | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| mkdocs | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pydantic | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| pytest | 0.950000 | 0.900000 | 1.000000 | 1.000000 | 0 | 10 |
| requests | 0.912500 | 0.900000 | 0.900000 | 0.900000 | 0 | 10 |
| rich | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| ruff | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 5 |
| typer | 0.850000 | 0.700000 | 1.000000 | 1.000000 | 0 | 10 |

## Safety and provenance

- Model: `BAAI/bge-small-en-v1.5` at immutable revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, loaded with `local_files_only=True`.
- Socket connection calls were blocked, credential variables were removed, offline controls were set, and writes were limited to this run directory plus an ephemeral process-owned temporary directory.
- No Turbopuffer, hosted API, model download, production-state mutation, or downstream cross-namespace retrieval ran.
- The model snapshot SHA-256 manifest and immutable input hashes are recorded in `plan.json`.

## Limitations

- The 90 questions and their original file judgments were assistant-drafted and are not human-approved product ground truth.
- Dataset membership supplies only the home-source label. Other namespaces are unlabeled, not known negatives, so route precision is intentionally not reported.
- The run does not measure answer quality, same-query cross-namespace hit quality, ACL behavior, production latency, or production readiness.
- Cached home-namespace hits were not used and absent cross-namespace hits were not fabricated.
- Independent review must inspect benchmark provenance and materially ambiguous home-source questions before ticket closure.
