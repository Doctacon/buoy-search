Status: done
Created: 2026-07-12
Updated: 2026-07-13

# Approved Apply Throughput Options

## Question

What can shorten a large approved apply without weakening the local-state and remote-write safety contract?

## Sources and methods

- Inspected `src/turbo_search/apply.py`, `src/turbo_search/chunker.py`, and `src/turbo_search/cli.py`.
- Inspected the completed Dagster plan summary: 1,164 pages and 25,322 chunks/rows.
- Consulted Sentence Transformers `SentenceTransformer.encode` API documentation: https://sbert.net/docs/package_reference/sentence_transformer/model.html
- Attempted to retrieve Turbopuffer write/concurrency documentation; documentation fetch was unavailable (502), so no service concurrency limit is established.
- Ran the authorized Dagster benchmark recorded at `.10x/evidence/2026-07-13-live-dagster-throughput-benchmark.md`.
- Inspected the current host/runtime: Apple M2 Pro (10 CPU cores, 16 GPU cores, 16 GB RAM), PyTorch 2.12.1, Sentence Transformers using `mps:0`, and model parameters in float32.
- Ran a local no-write microbenchmark over 1,024 existing real site chunks, comparing MPS float32/float16 encoder batches and CPU float32. Compared float16 and float32 normalized vector outputs over 256 chunks.
- Consulted Sentence Transformers efficiency documentation for float16 and ONNX/OpenVINO backends: https://sbert.net/docs/sentence_transformer/usage/efficiency.html

## Findings

- Apply is serial: for every CLI `--batch-size` group it calls local `SentenceTransformer.encode`, then waits for one Turbopuffer upsert before starting the next group.
- The CLI default write batch is 64. Dagster's 25,322 rows therefore required 396 serial embed/write cycles.
- Independent batch controls and timing are now implemented. The 25,322-row Dagster 128-write/64-embedding benchmark took 707.575 seconds: 521.829 seconds embedding and 165.997 seconds writing. Embedding was 73.7% of elapsed time and 75.9% of measured embed-plus-write time.
- On 1,024 representative existing site chunks, MPS float32 at encoder batch 32 measured 61.9 rows/s and batch 64 measured 61.0 rows/s; batch 128 became severely unstable/slow under 16 GB unified memory. CPU float32 batch 64 measured 39.8 rows/s.
- MPS float16 at encoder batch 32 measured 76.8 rows/s, about 24% faster than MPS float32 batch 32 in this microbenchmark. Batch 64 provided no reliable benefit and batch 128 was much slower.
- Across 256 normalized embeddings, float16 versus float32 cosine similarity had mean 1.00015 (minor floating-point overshoot), minimum 0.99976, and maximum absolute component delta 0.000873. This supports numerical closeness, not retrieval-quality equivalence.
- The current model is automatically using the Apple GPU through MPS, but in float32.

## Conclusions

1. The best low-complexity next optimization on this host is MPS float16 with encoder batch 32. It needs a focused implementation, retrieval-parity evaluation, and benchmark; numerical closeness alone is insufficient acceptance evidence.
2. Do not increase the embedding batch above 32 by default on this 16 GB M2 Pro. The benchmark disproves the assumption that larger encoder batches necessarily improve throughput and shows severe batch-128 memory pressure.
3. Keep write batching independent. Increasing write batch reduced request count, but writes are only about 24% of measured work; write-only optimization cannot address the dominant cost.
4. Benchmark an open-source MLX or ONNX/CoreML backend only after the float16 path. Those paths may improve Apple Silicon throughput but add dependencies/model-export behavior and require vector/retrieval parity evidence.
5. A bounded embed/write pipeline could overlap up to roughly 166 seconds of writes with embedding in this run, but adds failure/state complexity and does not improve embedding itself.
6. Larger chunks would reduce embeddings approximately with chunk count but change retrieval granularity and require evals. Changing to a faster model likewise requires a new namespace and quality evaluation.

## Limits

The microbenchmark used existing non-Dagster site chunks because successful Dagster plan artifacts were cleaned up. Results are host/workload specific and not a full retrieval evaluation. No Turbopuffer concurrency/rate-limit source was established. Float16 must not become the default until retrieval parity and a bounded live benchmark are ratified and verified.
