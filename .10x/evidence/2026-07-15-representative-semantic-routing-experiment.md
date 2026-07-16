Status: recorded
Created: 2026-07-15
Updated: 2026-07-15
Relates-To: .10x/tickets/2026-07-15-run-representative-semantic-routing-experiment.md, .10x/specs/representative-semantic-namespace-routing-experiment.md

# Representative Semantic Routing Experiment

## What was observed

Commit `a15bc686a645d1081f78272058a8da02751ff479` implemented the bounded evaluator and committed the guarded run artifacts under `autoresearch/runs/semantic-routing-representative-20260715/`. No production file under `src/buoy_search/` changed.

The evaluator loaded the exact 13 tracked dataset paths and mappings listed in `.10x/specs/representative-semantic-namespace-routing-experiment.md` and `plan.json`: Black 5, Buoy 10, Click 10, Django 5, Flask 5, HTTPX 5, MkDocs 5, Pydantic 5, pytest 10, Requests 10, Rich 5, Ruff 5, and Typer 10, totaling 90 questions. Dataset-local identity is retained as separate `repo_key` and `case_id` fields and as the composite `repo_key:case_id` identity. File judgments were not loaded into evaluation cases.

Machine-readable aggregate source-attribution metrics, independently recalculated from the 90 per-question home ranks in `result.json`, were:

| Strategy | MRR | Recall@1 | Recall@3 | Recall@5 | Unranked | Evaluated |
|---|---:|---:|---:|---:|---:|---:|
| oracle | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0 | 90 |
| lexical | 0.864815 | 0.822222 | 0.911111 | 0.911111 | 8 | 90 |
| semantic | 0.913246 | 0.877778 | 0.933333 | 0.944444 | 0 | 90 |
| hybrid RRF | 0.933153 | 0.900000 | 0.955556 | 0.955556 | 0 | 90 |

## Model and controls

The successful run used open-source `BAAI/bge-small-en-v1.5` revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a` with `revision` and `local_files_only=True` passed to `SentenceTransformer`. It produced normalized float32 384-dimensional embeddings. Cards were encoded as deterministic labeled passages; questions used the documented BGE query prefix.

Before model import/construction, the process:

- set `HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`, `HF_DATASETS_OFFLINE=1`, `HF_HUB_DISABLE_IMPLICIT_TOKEN=1`, and `HF_HUB_DISABLE_TELEMETRY=1`;
- removed `HF_TOKEN`, `HUGGING_FACE_HUB_TOKEN`, `TURBOPUFFER_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, and `COHERE_API_KEY` from its environment;
- rejected socket connect, create-connection, and address-resolution calls;
- rejected creation, write-mode opens, replacement, rename, and deletion outside the experiment directory and `.semantic-routing-tmp`;
- kept the Hugging Face model cache outside the write allowlist;
- removed the process-owned temporary directory after execution.

The exact resolved snapshot-file SHA-256 manifest is committed in `plan.json`. It contains 12 regular files, including `model.safetensors` SHA-256 `3c9f31665447c8911517620762200d2245a2518d6e7208acc78cd9db317e21ad` and `onnx/model.onnx` SHA-256 `828e1496d7fabb79cfa4dcd84fa38625c0d3d21da474a00f08db0f559940cf35`. The plan also records SHA-256 hashes for the card file and all 13 dataset inputs.

The run's enforced and observed side-effect counters were zero network calls, Turbopuffer calls, hosted API calls, model downloads, model-cache writes, external writes, credentials used, and fabricated cross-namespace hits. No production state, local applied state, remote state, or model cache was mutated. The ephemeral temporary directory was absent after the run.

## Procedure

Focused tests:

```text
uv run python -m unittest tests.test_semantic_routing_representative
Ran 14 tests in 0.033s
OK
```

Initial guarded run and explicit guarded artifact replacement after a guard-only code hardening change:

```text
env -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN -u TURBOPUFFER_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY -u COHERE_API_KEY HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HUB_DISABLE_IMPLICIT_TOKEN=1 HF_HUB_DISABLE_TELEMETRY=1 PYTHONDONTWRITEBYTECODE=1 uv run python autoresearch/runs/semantic-routing-representative-20260715/evaluate.py
env -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN -u TURBOPUFFER_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY -u COHERE_API_KEY HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HUB_DISABLE_IMPLICIT_TOKEN=1 HF_HUB_DISABLE_TELEMETRY=1 PYTHONDONTWRITEBYTECODE=1 uv run python autoresearch/runs/semantic-routing-representative-20260715/evaluate.py --replace-result
exit 0; loaded 199/199 cached weights; emitted the aggregate metrics recorded above
```

Concrete overwrite refusal check against the committed final result:

```text
env -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN -u TURBOPUFFER_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY -u COHERE_API_KEY HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HUB_DISABLE_IMPLICIT_TOKEN=1 HF_HUB_DISABLE_TELEMETRY=1 PYTHONDONTWRITEBYTECODE=1 uv run python autoresearch/runs/semantic-routing-representative-20260715/evaluate.py
exit 2; Refusing to overwrite existing final result ...; pass --replace-result for an explicit experiment-local replacement.
```

Full suite and mechanical validation:

```text
uv run python -m unittest discover -s tests
Ran 288 tests in 8.453s
OK

git diff --check
exit 0; no output
```

A local recalculation command loaded `plan.json` and `result.json`, asserted 13 cards, 90 cases for every strategy, 14 input-manifest entries, 12 model-manifest entries, and recomputed each MRR/unranked/evaluated count from per-question ranks. It exited 0 and printed the same aggregate metrics. `git check-ignore --no-index` confirmed the representative run result is unignored while `autoresearch/runs/unrelated-run/result.json` remains ignored.

## What this supports or challenges

Supports:

- Exact lexical card aliases outperform an unranked baseline but leave eight home namespaces unranked.
- On this source-attribution proxy, semantic cards improve MRR and recall@1/3/5 over lexical cards.
- Equal-weight hybrid RRF using production `RRF_K = 60` gives the strongest measured non-oracle aggregate values.
- The evaluator can run the pinned cached model under concrete offline, credential, socket, and write guards.

Challenges and limits:

- Dataset membership labels only the originating repository namespace. Other namespaces are unlabeled, not known negatives.
- The assistant-drafted questions are not human-approved product ground truth; materially ambiguous home-source questions still require independent review.
- This experiment does not establish route precision, answer quality, downstream same-query multi-namespace retrieval quality, ACL correctness, latency, or production readiness.
- No comparable cross-namespace hit lists exist, so cached home-namespace hits were not reused and absent hits were not fabricated.

## Conclusion

The bounded implementation and run satisfy the experimental execution slice and produce reviewable evidence. The owning ticket remains active pending the separately required independent adversarial review; this evidence does not close it.
