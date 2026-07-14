Status: recorded
Created: 2026-07-14
Updated: 2026-07-14
Target: .10x/tickets/done/2026-07-14-index-and-brief-oscilar.md, .10x/evidence/2026-07-14-oscilar-site-index-and-recruiter-brief.md
Verdict: concerns

# Oscilar Site Index and Recruiter Brief Review

## Target

Closure readiness of `.10x/tickets/done/2026-07-14-index-and-brief-oscilar.md` and its evidence, including the user-ratified supersession from a new/apply path to read-only use of existing `site-oscilar-com-v1`.

## Findings

### Validated

- Plan counts and safety fields match the generated plan artifacts: 260 pages, 5,730 chunks, 413 upsert candidates, 5,317 unchanged chunks, and 1,446 stale rows.
- Read-only DuckDB inspection supports 6,763 active rows and one 2026-07-13 apply from `plan_cf309400646eac2c`, with zero deletions.
- All seven live retrieval outputs target `site-oscilar-com-v1` in `gcp-us-central1`, report live Turbopuffer calls, and return cited hits.
- Every cited Oscilar URL appears in retrieval results. The official Ashby page is correctly labeled as directly fetched outside the Turbopuffer corpus and absent from the Buoy index.
- Marketing and recruiting claims are qualified; the candidate pitch is labeled as a template.
- No credential or secret values appear in the records.
- The brief is recruiter-call useful and includes business context, role interpretation, positioning, likely topics, and questions.

### Significant — closure blocker

The ticket captured a reusable failure mode—absence of an active namespace record did not mean the deterministic namespace was new—but initially contained no retrospective or durable workflow extraction. `.10x/knowledge/buoy-site-planning-workflow.md` proceeded from plan inspection to preflight without stating that prior applied state requires reassessing write authorization.

Required resolution: record the retrospective and update the workflow knowledge so `first_apply: false` or equivalent prior-state evidence triggers an explicit choice among use-existing, refresh-existing, and a newly planned versioned namespace before preflight or live write.

## Verdict

Concerns. Factual and recruiter-brief content passed review, but closure was not supported until the retrospective and workflow lesson were recorded.

## Residual risk

- Retrieval uses the prior 6,763-row index, so it may omit 413 current chunks and retain 1,446 stale rows.
- Company, performance, culture, and customer-outcome statements remain company-authored unless otherwise labeled.

## Resolution status

The parent subsequently addressed the finding in `.10x/knowledge/buoy-site-planning-workflow.md` and the ticket retrospective. A focused re-review is required before closure; this review remains an immutable record of the original concerns verdict.
