Status: recorded
Created: 2026-07-19
Updated: 2026-07-19
Relates-To: .10x/tickets/2026-07-19-research-code-aware-embedding-candidate.md, .10x/research/2026-07-19-code-aware-embedding-candidate.md, .10x/tickets/2026-07-19-evaluate-code-aware-embedding-pilot.md

# Code-Aware Embedding Feasibility Research Evidence

## What was observed

- Buoy source at `7c19b7c130549ada8221efdb4e5e2a2ad16eb3b8` fixes content vectors, namespace-card content dimensions, remote catalog compatibility, and catalog routing vectors at 384 dimensions. The current content/default plan model remains `BAAI/bge-small-en-v1.5`.
- The strongest retained upstream code-retrieval model that avoids remote code is `nomic-ai/nomic-embed-code@11114029805cee545ef111d5144b623787462a52`, but its immutable configs define 3,584-dimensional last-token normalized output and a 32,768-token maximum.
- Its immutable tree lists 28,282,512,976 bytes of float32 weights and 28,298,426,837 total listed bytes. It is not compatible with C4's 384-dimensional stop condition, and Buoy's shared encoder currently does not apply its required query-only prompt.
- The smaller credible screened artifacts were not eligible: BGE Code v1, CodeRankEmbed, and Jina Code are wrong-dimension and require remote code; the old DistilRoBERTa code-search artifact is wrong-dimension and lacks license provenance; Salesforce's 400M artifact is wrong-dimension, custom-code, and non-OSI; LateOn-Code is wrong-dimension and multi-vector/PyLate rather than the installed single-vector path.
- No fallback met the boundary. C4 remains blocked pending a separate decision on whether to shape dynamic content-vector dimensions.

## Procedure

1. Ran `git status --short --branch`, `git worktree list`, `git log -1`, and read the C2/C4/parent tickets plus governing research.
2. Inspected `src/buoy_search/chunker.py`, `apply.py`, `catalog.py`, `remote_catalog.py`, `config.py`, `plan_artifacts.py`, `retriever.py`, `pyproject.toml`, and `uv.lock` with bounded reads/searches.
3. Used public, read-only Hugging Face metadata/model-card/config/tree HTTP endpoints. The discovery query returned 100 SentenceTransformer-filtered results; 14 had explicit code/code-search dataset tags. Inspected authoritative upstream artifacts rather than third-party repacks.
4. Summed immutable tree metadata sizes with `jq`; did not fetch any weight/inference file.
5. Inspected the locked Hugging Face Hub `v1.20.1` source at commit `5efdca0b066740c911e59feba2f14e145ff3dbfb` for offline/telemetry environment controls.
6. Stored the normalized metadata snapshot at `.10x/research/.storage/2026-07-19-code-aware-embedding-source-snapshot.json` and the conclusions at `.10x/research/2026-07-19-code-aware-embedding-candidate.md`.

## What this supports or challenges

This supports the C2 conclusion that no retained candidate can enter C4 under the current 384-dimensional contract. It supports a stop, not a migration: dynamic dimensions, schema/card/routing changes, model download, resource verification, and namespaces remain unapproved.

## Safety observation

No model or dependency was downloaded/installed, no weight was loaded, no inference ran, no credentials were read, no live retrieval/service call occurred, and no namespace/catalog/source/test/lockfile mutation was performed. HTTP access was limited to public research metadata, model cards/configuration text, and authoritative package source.

## Limits

- RAM/device figures in the research record are analytical estimates from parameter/weight bytes and current precision behavior; they are not measured peaks.
- Metadata compatibility with locked packages does not prove runtime compatibility; the ticket explicitly forbids the model load needed to test it.
- Model-card quality claims were not reproduced.
- The search supports absence among the credible inspected upstream set, not a mathematical proof that no obscure model exists.
