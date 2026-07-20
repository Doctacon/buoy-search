Status: done
Created: 2026-07-19
Updated: 2026-07-19

# Code-Aware Embedding Candidate

## Question

Is there a credible open-source, locally runnable, native 384-dimensional code-aware embedding model that can use Buoy's installed `sentence-transformers` path without `trust_remote_code`, and therefore unblock C4 without a vector-dimension migration?

## Conclusion

No. The authoritative model repositories screened did not yield a credible native 384-dimensional candidate satisfying all of the local/open-source/SentenceTransformer/no-remote-code boundaries. C4 MUST remain blocked under its existing stop condition. A separate user decision would be required before shaping dynamic content-vector dimensions; this research does not authorize or design that migration.

One primary is retained only as the strongest credible **dynamic-dimension decision candidate**, not as a C4-compatible or user-approved model: `nomic-ai/nomic-embed-code@11114029805cee545ef111d5144b623787462a52`. It is Apache-2.0, uses standard SentenceTransformer modules without remote code, and is code-retrieval-specific, but emits 3,584 dimensions and has a roughly 28.30 GB artifact set. No fallback is retained: the smaller credible alternatives either require remote code, lack clear open-license provenance, are non-OSI, or do not fit the current single-vector path.

## Sources and methods

- Inspected the immutable Buoy source snapshot `7c19b7c130549ada8221efdb4e5e2a2ad16eb3b8` and lockfile. No source, tests, dependencies, lockfiles, models, credentials, namespaces, catalogs, or live services were mutated or called.
- Queried the public Hugging Face model metadata endpoint for `code` models filtered to Sentence Transformers (100 returned; 14 carried explicit code/code-search dataset tags), then inspected authoritative model cards and small configuration/tree metadata for the credible upstream candidates. This was repository research, not a model download: no weight or inference asset was fetched.
- Durable observed metadata and immutable URLs are stored in `.10x/research/.storage/2026-07-19-code-aware-embedding-source-snapshot.json`.
- Apache-2.0 is on the [Open Source Initiative's approved license page](https://opensource.org/license/apache-2-0). The retained model's immutable card declares `license: apache-2.0`.

Authoritative retained-model sources, all pinned to revision `11114029805cee545ef111d5144b623787462a52`:

- [model card and usage](https://huggingface.co/nomic-ai/nomic-embed-code/blob/11114029805cee545ef111d5144b623787462a52/README.md)
- [base architecture/dimension config](https://huggingface.co/nomic-ai/nomic-embed-code/blob/11114029805cee545ef111d5144b623787462a52/config.json)
- [query prompt and similarity config](https://huggingface.co/nomic-ai/nomic-embed-code/blob/11114029805cee545ef111d5144b623787462a52/config_sentence_transformers.json)
- [maximum sequence length](https://huggingface.co/nomic-ai/nomic-embed-code/blob/11114029805cee545ef111d5144b623787462a52/sentence_bert_config.json)
- [pooling contract](https://huggingface.co/nomic-ai/nomic-embed-code/blob/11114029805cee545ef111d5144b623787462a52/1_Pooling/config.json)
- [standard SentenceTransformer modules, including Normalize](https://huggingface.co/nomic-ai/nomic-embed-code/blob/11114029805cee545ef111d5144b623787462a52/modules.json)
- [immutable artifact tree and byte sizes](https://huggingface.co/api/models/nomic-ai/nomic-embed-code/tree/11114029805cee545ef111d5144b623787462a52?recursive=true&expand=false)

## Compatibility and cost table

| Role | Model contract | License provenance | ST / remote-code boundary | Prefix, pooling, normalization | Dimension / max input | Download, RAM, device estimate | C4 compatible? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Primary, dynamic-dimension decision only | `nomic-ai/nomic-embed-code@11114029805cee545ef111d5144b623787462a52`; standard `Qwen2Model`; public and ungated | Immutable model card declares Apache-2.0; OSI approves Apache-2.0 | Card provides `SentenceTransformer("nomic-ai/nomic-embed-code")`; repository has standard Transformer/Pooling/Normalize modules, no `auto_map`, no custom-code tag, and usage does not enable `trust_remote_code` | Query prompt name `query`: `Represent this query for searching relevant code: `; documents have no prefix. Last-token pooling with prompt included, followed by Normalize. Buoy also requests normalized output. Current Buoy encoding does not pass a query prompt, so minimum experiment-only role-aware prefix plumbing would also be required. | 3,584; model and ST configs declare 32,768 tokens | 28,282,512,976 weight bytes; 28,298,426,837 listed repository bytes (28.30 GB / 26.35 GiB). Float32 parameters alone require 26.34 GiB; estimate at least 32 GiB available RAM and a 48 GiB host. Float16 steady weights are at least 13.17 GiB; estimate a 24 GiB accelerator, but Buoy's construct-then-`.half()` path may have materially higher transient need. No load was run, so peak RAM/device memory is unverified. | **No.** Native output is 3,584, not 384. |
| Fallback | None retained | — | — | — | — | — | **No.** |

The memory figures are analytical planning estimates, not measured benchmarks. A future checkpoint would need an exact approved resource bound and a permitted local load before claiming measured peak RAM/device use.

## Dependency and offline/telemetry contract

Buoy locks `sentence-transformers==5.6.0`, `transformers==5.12.1`, `torch==2.12.1`, and `huggingface-hub==1.20.1`. The retained artifact was authored with older SentenceTransformer/Transformers versions but uses only the standard `Qwen2Model` plus built-in Transformer, Pooling, and Normalize modules. The installed versions are therefore metadata-compatible; runtime compatibility remains unverified because this ticket forbids loading weights.

For an eventually approved pinned download, the constructor MUST receive the immutable revision. After the artifact is explicitly cached, set `HF_HUB_OFFLINE=1` so Hub HTTP requests fail rather than silently checking/downloading, and set `HF_HUB_DISABLE_TELEMETRY=1` (or `DO_NOT_TRACK=1`) to disable telemetry. The locked Hub implementation defines those controls and treats `TRANSFORMERS_OFFLINE` as an offline alias in [`constants.py`](https://github.com/huggingface/huggingface_hub/blob/5efdca0b066740c911e59feba2f14e145ff3dbfb/src/huggingface_hub/constants.py#L202-L243). `HF_HUB_DISABLE_UPDATE_CHECK=1` additionally suppresses the package's update-check request. The model is public and ungated; no credentials are required.

Current content embedding does not meet that pinned/offline/prefix contract: `SentenceTransformerEmbedder` calls `SentenceTransformer(model_name)` without `revision` or `local_files_only`, and its shared `encode` call supplies neither `prompt_name="query"` nor an explicit query prefix. C4 would need minimum experiment-only pin/offline and role-aware prefix plumbing even after any dimension decision; this research does not implement it.

## Current Buoy compatibility boundary

At source snapshot `7c19b7c130549ada8221efdb4e5e2a2ad16eb3b8`:

- `src/buoy_search/chunker.py` sets `VECTOR_DIMENSIONS = 384` and the content schema to `[384]f16`.
- `src/buoy_search/apply.py` previews content/catalog `vector_dimensions` as 384.
- `src/buoy_search/catalog.py` pins automatic routing itself to `BAAI/bge-small-en-v1.5@5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, normalized 384-dimensional vectors, and validates every card's `vector_dimensions` as exactly 384.
- `src/buoy_search/remote_catalog.py` fixes remote routing vectors and compatibility contracts at 384.
- `src/buoy_search/config.py` and `src/buoy_search/plan_artifacts.py` retain `BAAI/bge-small-en-v1.5` as the content/default plan model. No default changes are authorized.
- Retrieval can automatically select namespace cards, but selected namespaces must share one content embedding model and precision. A 3,584-dimensional content namespace cannot be represented honestly by the current 384-only card/compatibility contract, even though the independent catalog-routing vectors could remain 384.

Therefore the current hard-coded contracts do not permit C4 with the retained model. Solving that would be a content schema/card/compatibility migration decision, explicitly outside C2 and C4.

## Candidate screen and rejection reasons

| Candidate | Immutable revision | Observed boundary | Disposition |
| --- | --- | --- | --- |
| `BAAI/bge-code-v1` | `bd67852057c5d7ddcc7b8234d9d6c410117ed851` | Apache-2.0, 1,536 dimensions, roughly 6.17 GB weights; authoritative SentenceTransformer example enables `trust_remote_code=True` | Rejected: wrong dimension and remote code |
| `nomic-ai/CodeRankEmbed` | `3c4b60807d71f79b43f3c4363786d9493691f8b1` | MIT, 768 dimensions, model card and `auto_map` require remote code | Rejected: wrong dimension and remote code |
| `jinaai/jina-embeddings-v2-base-code` | `516f4baf13dec4ddddda8631e019b5737c8bc250` | Apache-2.0, 768 dimensions, model card and `auto_map` require remote code | Rejected: wrong dimension and remote code |
| `flax-sentence-embeddings/st-codesearch-distilroberta-base` | `65b0f39bfa41c59993f62b57447c942e371b7135` | Native ST/Roberta, 768 dimensions; immutable repository has no license field/file and card calls it preliminary and untested | Rejected: wrong dimension and unclear license/credibility |
| `Salesforce/SFR-Embedding-Code-400M_R` | `cb950dc80d677c6fdc00f56c8ddd20ca2642c59e` | 1,024 dimensions, custom code, CC-BY-NC-4.0 | Rejected: wrong dimension, remote code, and non-OSI license |
| `lightonai/LateOn-Code` | `734b659a57935ef50562d79581c3ff1f8d825c93` | Apache-2.0, 768-dimensional ColBERT/PyLate multi-vector output | Rejected: wrong dimension and incompatible retrieval shape/dependency path |

No third-party repack or quantization was promoted over an authoritative upstream artifact.

## Required decision and stop

C4 remains blocked. The next product/architecture checkpoint is:

> No credible native 384-dimensional code-aware candidate met the open-source/local/SentenceTransformer/no-remote-code boundary. Confirm or reject opening a separate shaping decision for dynamic **content-vector** dimensions, including content namespace schema, card compatibility, automatic routing, migration/isolation, and resource bounds. Until confirmed, C4 performs no model download, inference, source change, namespace write, catalog change, or live operation.

## Limits

- This is feasibility research, not a quality benchmark. Model-card benchmark claims were not independently reproduced.
- No model/dependency was downloaded or installed; no model was loaded; no inference, credential read, namespace/catalog operation, or live retrieval/write occurred.
- Search can never prove that no obscure 384-dimensional artifact exists. The conclusion is scoped to credible, authoritative, open-license candidates discoverable in the inspected upstream set; mutable-only, unclear-license, custom-code, multi-vector, and low-credibility repacks were intentionally excluded.
