# Agent answering workflow for Jellyfish docs

Use this workflow before answering user questions that ask what Jellyfish says, documents, recommends, or defines.

## 1. Retrieve context first

Dry-run planning is safe and does not read credentials or call turbopuffer:

```bash
PYTHONPATH=src uv run --no-sync python -m turbo_search retrieve \
  "<user question>" \
  --dry-run \
  --top-k 5 \
  --candidates 100 \
  --json
```

Live retrieval is the command to run when credentials are approved and the Jellyfish namespace has been indexed:

```bash
TURBOPUFFER_REGION=gcp-us-central1 \
TURBOPUFFER_NAMESPACE=jellyfish-site-docs-v1 \
uv run turbo-search retrieve \
  "<user question>" \
  --live \
  --top-k 5 \
  --candidates 100 \
  --json
```

Optional filter:

```bash
uv run turbo-search retrieve "<user question>" --live --doc-kind blog --json
```

Required live environment:

- `TURBOPUFFER_API_KEY`: required only for `--live`; read from the environment at runtime.
- `TURBOPUFFER_REGION`: default is `gcp-us-central1`.
- `TURBOPUFFER_NAMESPACE`: default is `jellyfish-site-docs-v1`.
- `TURBO_SEARCH_EMBEDDING_MODEL`: optional; default is `BAAI/bge-small-en-v1.5`.

Safe Proton Pass note: do not access secrets unless live retrieval is approved. If approved, verify the Proton Pass session first, then export the key into shell memory only; do not print it, write it to `.env`, or commit it.

Known working command shape for this project:

```bash
export PROTON_PASS_SESSION_DIR="/tmp/pass-agent-turbo-search-jellyfish"
pass-cli info >/dev/null || {
  echo "Proton Pass session is not authenticated; re-authenticate before live retrieval." >&2
  exit 2
}
export TURBOPUFFER_API_KEY="$(PROTON_PASS_AGENT_REASON="Retrieve Jellyfish docs context for an approved answer" \
  pass-cli item view --vault-name "<private Proton Pass vault>" --item-title "<private turbopuffer credential item>" --field "API Key")"
```

Important: `pass-cli item view --item-title "<private turbopuffer credential item>"` fails without `--vault-name "<private Proton Pass vault>"` in this setup. If `pass-cli info` fails, re-authenticate in the isolated session directory using the Proton Pass agent instructions; do not paste or log token values.

## 2. Read the retrieval output

Live JSON output includes:

- Top-level: `query`, `region`, `namespace`, `embedding_model`, `top_k`, `candidates`, `doc_kind`, `fusion`, `dry_run`, `turbopuffer_api_calls`, `api_calls_occurred`.
- `hits[]`: one retrieved chunk per item.
- Each hit: `id`, `title`, `url`, `section_path`, `content`, `path`, `score_info`, and optionally `doc_kind` and `chunk_index`.
- Vectors are not requested or returned by default.

Use `content` as the answer source. Use `title`, `url`, and, when helpful, `section_path` as citations.

## 3. Decide whether to answer

- Retrieval failure: if the command exits non-zero, reports missing env vars, or cannot reach/query the namespace, do not answer from memory. State that retrieval failed and name the non-secret fix, such as setting `TURBOPUFFER_API_KEY` or confirming region/namespace/indexing.
- Weak retrieval: if there are no hits, hits lack `content`, hits lack `title`/`url`, or the returned chunks do not directly address the question, say the retrieved Jellyfish context is insufficient and ask for permission to broaden or retry retrieval.
- Answerable: if retrieved chunks directly address the question, answer only from those chunks.

## 4. Answer with citations and guardrails

- Base material claims only on retrieved `content`.
- Cite every material claim with the source `title` and `url`.
- Prefer concise synthesis over copying long passages.
- Do not use outside knowledge to fill gaps.
- If retrieved chunks disagree or are incomplete, say so and cite the relevant sources.
- If the answer needs unstated current/product details not in the retrieved chunks, say the retrieved context is insufficient.

Citation format:

```text
...claim... (Source: <title>, <url>)
```

## Example

Question:

```text
What are DORA metrics according to Jellyfish?
```

Retrieval reference: `.loom/evidence/2026-06-20-jellyfish-live-retrieval.md`, Query 1. The top hit was `DORA Metrics 101 | Jellyfish Blog` at `https://jellyfish.co/blog/dora-metrics-101/`, section `What are DORA metrics?`; the evidence notes that it directly listed Change Lead Time, Deployment Frequency, Change Failure Rate, and Mean Time To Recovery.

Answer sketch:

```text
According to Jellyfish, DORA metrics are four DevOps performance metrics: Change Lead Time, Deployment Frequency, Change Failure Rate, and Mean Time To Recovery. They are used to evaluate and improve software delivery performance. (Source: DORA Metrics 101 | Jellyfish Blog, https://jellyfish.co/blog/dora-metrics-101/)
```
