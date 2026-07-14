Status: done
Created: 2026-07-14
Updated: 2026-07-14
Parent: None
Depends-On: None

# Index and Brief Oscilar for an Analytics Engineer Recruiter Call

## Scope

Create a searchable Turbopuffer index of the public English-language website at `https://oscilar.com/`, then use live retrieval from that index to produce a concise, cited recruiter-call brief for an analytics engineer candidate.

Use the deterministic namespace `site-oscilar-com-v1`. The original scope called for the reviewed Buoy plan/preflight/approved-apply workflow because the namespace was believed to be new. Fresh plan inspection established that local applied state already exists from 2026-07-13. The user then explicitly ratified using the existing `site-oscilar-com-v1` without preflight, live apply, stale deletion, or a v2 namespace. Preserve the fresh local plan only as inspection context and search the existing namespace.

The brief must cover:

- what Oscilar does, for whom, and how it appears to create business value;
- its main products/capabilities and differentiators supported by the indexed site;
- company, customer, technical, data, and analytics signals relevant to an analytics engineer;
- a recruiter-call preparation section with a short positioning pitch, likely recruiter topics, and high-value questions to ask;
- clear uncertainty where the website does not establish a fact.

## Acceptance criteria

- A local `buoy plan` for `https://oscilar.com/` is reviewed before any live write.
- The plan uses namespace `site-oscilar-com-v1`, obeys robots/same-site defaults, and indexes the intended English public corpus without obvious duplicate or irrelevant page families.
- Plan artifacts (`summary.json`, `plan.json`, `manifest.json`, `chunks.jsonl`, and representative generated pages) are inspected.
- **Superseded 2026-07-14 after state discovery:** `buoy apply` preflight confirms the reviewed namespace, upsert/embedding counts, stale-row count, and no live calls.
- **Superseded 2026-07-14 after state discovery:** one explicitly approved live apply completes without `--delete-stale`; no namespace deletion or replacement occurs.
- Instead, read-only inspection confirms the prior applied-state provenance and live retrieval runs against the existing `site-oscilar-com-v1` for the business overview and analytics-engineer/recruiter-call angles.
- The resulting brief cites retrieved Oscilar page titles/URLs and does not present unsupported inferences as facts. The official public Ashby role page directly fetched during execution may be cited as an explicitly labeled primary source outside the Turbopuffer corpus; it must never be included in the Buoy crawl or Turbopuffer index.
- Durable evidence records the non-secret command shapes, plan/state counts, retrieval validation, sources used, superseded apply path, and material limits.

## Explicit exclusions

- No stale-row deletion, namespace deletion, or namespace replacement.
- No crawling authenticated, paywalled, protected, or off-domain content.
- No application/source-code changes.
- No claims about compensation, team structure, role requirements, funding, customers, or technical architecture unless established by retrieved public pages or the directly fetched official public Ashby role page; unsupported items must be framed as questions or uncertainty.
- Do not modify or clean up unrelated existing working-tree changes.

## Assumption provenance

- `https://oscilar.com/` and the recruiter-call purpose are user-provided.
- Live creation/write permission and subsequent search permission are user-ratified in the current conversation.
- `site-oscilar-com-v1` is record-backed by the deterministic website namespace convention in `.pi/skills/turbopuffer-site-rag/references/scrapling-site-workflow.md` and `/Users/crlough/.pi/agent/skills/turbo-search-retrieve/SKILL.md`.
- English-only, same-site, robots-obeying sitemap-first crawling and no stale deletion are active project defaults.

## References

- `.pi/skills/turbopuffer-site-rag/SKILL.md`
- `.pi/skills/turbopuffer-site-rag/references/scrapling-site-workflow.md`
- `/Users/crlough/.pi/agent/skills/turbo-search-retrieve/SKILL.md`
- `.10x/knowledge/buoy-site-planning-workflow.md`
- `.10x/specs/website-crawl-strategy-default.md`
- `.10x/specs/website-language-policy.md`

## Evidence expectations

Record a new evidence file under `.10x/evidence/` related to this ticket. Include plan and prior applied-state counts, safety fields, the local state location, live retrieval validation fields, retrieved source URLs used in the brief, the separately labeled official Ashby posting provenance, the superseded apply path, and limitations. Never record credentials or secret values.

## Blockers

None. The target, namespace convention, live write authorization, retrieval authorization, safety boundaries, and expected output are concrete.

## Progress and notes

- 2026-07-14: Ticket opened after inspecting active website workflow records and confirming no existing Oscilar owner or namespace record.
- 2026-07-14: Fresh local plan completed successfully: 260 English pages, 5,730 chunks, 5,317 unchanged chunks, 413 upsert candidates, and 1,446 stale rows. English filtering excluded 638 Spanish/Portuguese localized URLs; no request errors or crawl limits were hit.
- 2026-07-14: Read-only DuckDB inspection established that `site-oscilar-com-v1` already had 6,763 active rows from one apply on 2026-07-13 (`plan_cf309400646eac2c`), contradicting the original new-namespace premise. Execution paused before preflight/live apply.
- 2026-07-14: The user ratified using the existing v1. The preflight/live-apply criteria were superseded; no v2, preflight, apply, stale deletion, namespace deletion, or replacement ran. Live retrieval used the existing 6,763-row v1, with the current unapplied plan retained only as freshness context.
- 2026-07-14: Seven narrow live retrievals completed successfully in `gcp-us-central1`; all reported live Turbopuffer API calls and returned cited hits. The resulting business and analytics-engineer recruiter brief, official off-index Ashby role provenance, commands, observations, and limits are recorded in `.10x/evidence/2026-07-14-oscilar-site-index-and-recruiter-brief.md`. Ticket remains active for parent review.
- 2026-07-14: Closure review validated plan/state/retrieval counts, citation provenance, secret safety, claim qualification, and recruiter usefulness, but raised a significant retrospective blocker: the reusable existing-namespace safety lesson had not been extracted. Review: `.10x/reviews/2026-07-14-oscilar-site-index-and-recruiter-brief-review.md`.
- 2026-07-14: Resolved the review finding by updating `.10x/knowledge/buoy-site-planning-workflow.md`: a plan reporting prior applied state now requires a pre-write checkpoint choosing use-existing, explicitly refresh-existing, or newly planned versioned namespace. No skill or always-on instruction change was needed because the existing workflow knowledge is the narrow durable owner.

## Retrospective

The key failure mode was premise drift: searching active records found no Oscilar owner, but local applied state proved the deterministic namespace was already populated. The plan-first guardrail prevented an unintended refresh; escalation converted the discovery into an explicit user choice before any write.

The durable lesson is now recorded in `.10x/knowledge/buoy-site-planning-workflow.md`. Future operators must treat `first_apply: false` or `state_first_apply: false` as a semantic write-authorization checkpoint, not merely an incremental-diff detail. No additional skill, specification, source change, or follow-up ticket is warranted: the operational workflow record is the correct narrow control point, and the residual stale-index limitation is accepted context for the user's explicit use-existing choice rather than unfinished work.

## Closure

Focused re-review passed with no blocker and explicitly supported closure: `.10x/reviews/2026-07-14-oscilar-site-index-and-recruiter-brief-rereview.md`. Every active acceptance criterion maps to `.10x/evidence/2026-07-14-oscilar-site-index-and-recruiter-brief.md`; the two apply criteria are visibly superseded by the user's use-existing choice. The ticket is complete and moved to `done`.
