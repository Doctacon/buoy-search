Status: done
Created: 2026-07-02
Updated: 2026-07-02
Depends-On: .10x/tickets/done/2026-07-02-cli-one-line-plan-progress.md

# Sitemap Progress Estimates

## Scope

Improve website `crawl`/`plan` progress text so page caps are not presented as known totals and sitemap crawls expose a sitemap-derived estimate when available.

In scope:

- Change link and unknown-total progress messages from `pages=N/MAX` or `queued=N/MAX` to explicit `pages=N`, `queued=N`, `cap=MAX` wording.
- During sitemap discovery, count unique same-host/path-filtered sitemap page URLs before the page cap is applied.
- Display the sitemap-derived attempted total in sitemap page progress, using the cap only when the sitemap estimate exceeds the cap.
- Add tests for estimate/count behavior and progress wording.

Out of scope:

- Live turbopuffer writes.
- Pre-fetching or crawling additional sitemap URLs outside the existing Scrapling sitemap flow.
- Estimating link-only crawl totals, which are not known upfront.

## Acceptance criteria

- Starting a website plan no longer shows `1/3000` solely because `3000` is the cap.
- Sitemap progress includes a sitemap-derived estimate after sitemap URLs are discovered.
- Link progress continues to show dynamic pages/queued counts plus cap.
- Unit tests pass.

## Progress and notes

- 2026-07-02: User requested sitemap-derived attempted page estimate for website plan progress.
- 2026-07-02: Implemented explicit `cap=` progress wording for unknown/link totals and sitemap URL estimate tracking for sitemap progress. Added tests and validation evidence.

## Blockers

- None.

## Evidence

- `.10x/evidence/2026-07-02-sitemap-progress-estimates-validation.md`
