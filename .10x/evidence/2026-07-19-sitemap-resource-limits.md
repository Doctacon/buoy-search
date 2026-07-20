Status: recorded
Created: 2026-07-19
Updated: 2026-07-19
Relates-To: .10x/tickets/2026-07-18-bound-sitemap-resource-usage.md, .10x/specs/sitemap-resource-limits.md, .10x/specs/website-exact-host-crawl-boundary.md

# Sitemap Resource-Limit Validation

## What was observed

- `fetch_url_bytes()` reads at most 64 KiB per call and accepts exactly 512 KiB robots bodies and 10 MiB sitemap transfers while rejecting one byte over either ceiling.
- Sitemap gzip expansion reads incrementally, accepts exactly 50 MiB decompressed output, and rejects a compressed expansion-bomb fixture at 50 MiB + 1 byte.
- URL-, content-type-, content-encoding-, and magic-byte-declared malformed gzip raises `SitemapResourceError` rather than becoming empty sitemap discovery.
- Multiple queued sitemaps propagate a late resource-limit error; sitemap resource errors do not enter link fallback.
- Bounded discovery remains exact-host constrained. The existing exact-host fixture suite still proves blocked declarations/redirects receive zero requests and redirected robots rules remain effective.
- Sitemap crawling now uses page URLs returned by bounded discovery rather than asking Scrapling to download sitemap bodies independently. Robots are placed into Scrapling's parser cache only after the bounded exact-host reader succeeds.

## Procedure

All commands were non-live and made no remote-service writes:

```text
PYTHONDONTWRITEBYTECODE=1 uv run --python 3.11 python -m unittest tests.test_crawler tests.test_crawler_exact_host -q
# Ran 58 tests in 5.988s — OK

PYTHONDONTWRITEBYTECODE=1 uv run --python 3.11 python -m unittest discover -s tests -p 'test_*.py' -q
# Ran 428 tests in 21.295s — OK

PYTHONDONTWRITEBYTECODE=1 uv run --python 3.13 python -m unittest tests.test_crawler tests.test_crawler_exact_host -q
# Ran 58 tests in 6.005s — OK

PYTHONDONTWRITEBYTECODE=1 uv run --python 3.13 python -m unittest discover -s tests -p 'test_*.py' -q
# Ran 428 tests in 21.088s — OK

git diff --check
# passed with no output
```

The full suites emitted only existing best-effort temporary plan-artifact cleanup warnings. The exact-host focused suites emitted an upstream lxml `strip_cdata` deprecation warning.

## What this supports

The implementation and tests support the behavioral and acceptance scenarios in `.10x/specs/sitemap-resource-limits.md` without changing the exact hostname rule, 20-hop redirect boundary, sitemap/page count caps, include/exclude path filtering, robots enforcement, crawl strategies, or trusted-local SSRF exclusion.

## Limits

- Transfer-boundary tests use mocked incremental response streams. Existing exact-host integration tests use loopback fixture servers; no live website was crawled.
- Page-body limits and service-grade DNS/IP/private-network SSRF controls remain explicitly excluded.
- Independent review is still required before ticket closure; the ticket remains active.
