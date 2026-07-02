Status: recorded
Created: 2026-07-02
Updated: 2026-07-02
Relates-To: .10x/tickets/done/2026-07-02-sitemap-progress-estimates.md

# Sitemap Progress Estimates Validation

## What was observed

Website progress messages no longer use the page cap as an apparent known total for link/unknown-total crawl progress. Link crawl messages use explicit `cap=` wording.

Sitemap crawl progress tracks unique same-host, path-filtered sitemap URLs before applying the page cap. Once sitemap URLs are known, page progress can display an attempted sitemap total such as:

```text
crawl sitemap: pages=1/842; cap=3000; queued=842; https://example.com/docs/page
```

When the sitemap has more eligible URLs than the cap, the attempted total is capped and the raw sitemap estimate remains visible:

```text
crawl sitemap: pages=1/3000; sitemap=5231; cap=3000; queued=3000; https://example.com/docs/page
```

## Procedure

Commands run:

```bash
uv run python -m unittest tests.test_crawler
uv run python -m unittest tests.test_crawler tests.test_cli
uv run python -m unittest discover -s tests
```

Observed output:

```text
Ran 22 tests in 0.576s
OK

Ran 45 tests in 0.587s
OK

Ran 152 tests in 3.012s
OK
```

## What this supports or challenges

Supports:

- The sitemap estimate formatter uses the sitemap URL count when available and falls back to `cap=` when not available.
- Sitemap dispatch counts unique filtered URLs beyond the scheduling cap while only scheduling up to the cap.
- Link progress uses dynamic counts plus an explicit cap, not `N/cap` denominator wording.
- Existing CLI/crawler/full test coverage still passes.

Limits:

- This validation uses unit tests, not a live public-site crawl.
- Link-only totals remain unknowable upfront and are intentionally not estimated.
