Status: open
Created: 2026-07-15
Updated: 2026-07-15
Parent: None
Depends-On: None

# Run Representative Semantic Routing Experiment

## Outcome

Implement and run one bounded, read-only source-attribution experiment over the existing 13-repository/90-question basket. Compare oracle, lexical card aliases, semantic namespace cards, and equal-weight hybrid route RRF without adding production routing architecture.

## Governing records

- `.10x/specs/representative-semantic-namespace-routing-experiment.md`
- `.10x/reviews/2026-07-15-holistic-semantic-routing-workstream-review.md`
- `.10x/decisions/data-vault-is-analogy-not-architecture.md`
- `.10x/specs/repo-search-eval-autoresearch.md`
- `.10x/evidence/2026-06-28-cross-corpus-seed-eval-datasets.md`
- `.10x/decisions/namespace-ranking-defaults.md`
- the 13 tracked `src/buoy_search/data/*_repo_search_seed_evals.json` files enumerated by the active specification
- `src/buoy_search/retriever.py` for the established `RRF_K` constant and the boundary around downstream hit fusion

## Cold-start context

The superseded plan would have built five synthetic taxonomy/catalog/evaluator stages before any representative value evidence or product consumer existed. The user accepted the holistic review's smaller path on 2026-07-15.

The 13 tracked seed datasets enumerated by the active specification provide 90 source-backed, assistant-drafted questions. They are not human-approved product ground truth and do not contain the same question run against every other namespace. Use only case ID, question text, and the specification's home-namespace mapping for descriptive source attribution. Do not manufacture downstream cross-namespace results from missing data.

A read-only inspection on 2026-07-15 found open-source `BAAI/bge-small-en-v1.5` revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a` in the local Hugging Face cache. Execution must use that exact revision with the specification's offline/local-only environment, socket, credential, and path-write guards; fail rather than download, mutate cache, or substitute if loading fails.

## Scope

1. Narrow `.gitignore` so only `autoresearch/runs/semantic-routing-representative-20260715/` is newly tracked while unrelated run contents remain ignored.
2. Create that run directory with one experiment-specific evaluator and reviewed 13-card configuration.
3. Load the 13 tracked seed datasets and validate the exact dataset/mapping/card/90-question contract.
4. Implement the four routing strategies and exact offline/local-only guards as specified.
5. Add focused tests for validation, normalization, descriptor deduplication/frequency, deterministic ranking, injected-vector semantic ranking, RRF, metrics, overwrite safety, exact model revision/offline controls, socket/credential/write guards, and the narrow ignore exception.
6. Run the real semantic experiment with the pinned cached model and guards.
7. Commit `plan.json`, `result.json`, and `report.md` with explicit limitations and the model snapshot SHA-256 manifest.
8. Record reproducible evidence and obtain independent adversarial review before closure.

## Acceptance criteria

- The diff adds no production taxonomy, catalog, router, command, public API, persistence, graph, dependency, or behavior under `src/buoy_search/`.
- The experiment consumes exactly the 13 tracked dataset/mapping entries and all 90 questions enumerated by the active specification.
- Card validation is fail-closed and card text contains project-level descriptions rather than benchmark-question or expected-file leakage.
- Independent review inspects benchmark provenance and names materially ambiguous home-source questions rather than treating the assistant-drafted basket as product ground truth.
- Oracle, lexical, semantic, and hybrid route rankings follow the active specification exactly.
- Semantic execution uses `BAAI/bge-small-en-v1.5` revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, exact offline/local-only controls, a recorded model-file SHA-256 manifest, and fail-fast socket/credential/path-write guards.
- A narrow `.gitignore` exception makes this experiment's script/config/final artifacts reviewable while all unrelated untracked run directories remain ignored.
- Hybrid route fusion uses `RRF_K = 60` consistently with the existing runtime constant.
- Results include per-question rankings and aggregate/per-repository MRR, recall@1/3/5, unranked counts, and evaluated counts.
- The report distinguishes source-attribution evidence from unlabeled alternative relevance, downstream retrieval quality, and production readiness.
- The implementation does not misuse cached home-namespace hits as comparable cross-namespace results.
- Focused tests, the full test suite, and `git diff --check` pass.
- Independent review finds no unresolved significant issue and verifies the reported metrics from `result.json`.

## Explicit exclusions

- any production source change;
- live Turbopuffer access;
- downloads, hosted APIs, or credentials;
- production ACL, lifecycle, freshness, or compatibility policy;
- downstream same-query multi-namespace retrieval or `cross_namespace_rrf` execution without comparable hits;
- tag output/filtering changes owned by `.10x/tickets/2026-07-15-reconcile-retrieval-tag-output.md`;
- promotion thresholds or production integration choice;
- query decomposition, concepts, relationships, ontology, or graphs.

## Evidence expectations

Evidence must record:

- implementation commit and exact tracked input paths/mappings;
- model identifier, immutable revision, snapshot-file SHA-256 manifest, offline environment controls, and guard behavior;
- focused and full validation commands with exit status;
- machine-readable aggregate metrics checked against the committed result;
- confirmation that no network, Turbopuffer, credential, model-download, production-state, or external-write path ran;
- limitations caused by home-source-only labels and absent same-query cross-namespace hits.

## Dependencies

None. The model revision cache and all 13 tracked source datasets were inspected before opening this ticket. If the cached model cannot load under the offline and write guards, mark this ticket blocked; do not download, mutate cache, or substitute.

## Blockers

None.

## Progress and notes

- 2026-07-15: Opened after the user accepted the smaller representative-experiment path. This ticket replaces the cancelled five-stage synthetic pilot and is the only executable implementation owner for the first routing-value slice.
