#!/usr/bin/env python3
"""Dry-run a Scrapling website crawl and chunk pages with turbo_search.

This helper intentionally does not read credentials, embed text, create namespaces,
or call turbopuffer. It is meant to smoke-test the generic site workflow before a
separate explicit live-write step.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import urlparse

from turbo_search.indexer import (
    DEFAULT_OVERLAP_SENTENCES,
    DEFAULT_TARGET_TOKENS,
    process_corpus,
    sha256_text,
)


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def nonnegative_float(value: str) -> float:
    parsed = float(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be zero or greater")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Crawl a public site with Scrapling, write a local Markdown corpus, "
            "and chunk it with turbo_search without turbopuffer API calls."
        )
    )
    parser.add_argument("--base-url", required=True, help="Website URL to start crawling.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("artifacts/scrapling-dry-crawl/site"),
        help="Local output directory. artifacts/ is gitignored in this repo.",
    )
    parser.add_argument("--max-pages", type=positive_int, default=10, help="Maximum URLs to schedule.")
    parser.add_argument("--max-chunks", type=positive_int, default=100, help="Maximum chunks to emit in dry-run.")
    parser.add_argument("--concurrent-requests", type=positive_int, default=2, help="Global crawl concurrency.")
    parser.add_argument(
        "--concurrent-requests-per-domain",
        type=positive_int,
        default=1,
        help="Per-domain crawl concurrency.",
    )
    parser.add_argument("--download-delay", type=nonnegative_float, default=0.25, help="Delay between requests.")
    parser.add_argument(
        "--css-selector",
        default=None,
        help="Optional CSS selector for main content extraction, e.g. 'article' or '.md-content__inner'.",
    )
    parser.add_argument("--target-tokens", type=positive_int, default=DEFAULT_TARGET_TOKENS)
    parser.add_argument("--overlap-sentences", type=positive_int, default=DEFAULT_OVERLAP_SENTENCES)
    return parser


def require_scrapling() -> None:
    try:
        import scrapling  # noqa: F401
        from scrapling.core.shell import Convertor  # noqa: F401
        from scrapling.spiders import LinkExtractor, Spider  # noqa: F401
    except ImportError as exc:
        raise SystemExit(
            "Missing Scrapling/Markdown dependencies. Run with:\n"
            "PYTHONPATH=src uv run --with 'scrapling[fetchers]>=0.4.9' "
            "--with 'markdownify>=1.2.0' python "
            ".pi/skills/turbopuffer-site-rag/scripts/scrapling_dry_crawl.py ..."
        ) from exc


def host_from_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise argparse.ArgumentTypeError("base URL must be an absolute http(s) URL")
    return parsed.hostname or parsed.netloc


def namespace_candidate(base_url: str) -> str:
    host = host_from_url(base_url).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", host).strip("-")
    return f"site-{slug}-v1"


def safe_slug(value: str, *, fallback: str = "page") -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:80] or fallback


def yaml_scalar(value: object) -> str:
    text = str(value if value is not None else "")
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def page_filename(url: str, title: str, index: int) -> str:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
    parsed = urlparse(url)
    path_slug = safe_slug(parsed.path.strip("/") or title or parsed.netloc, fallback=f"page-{index}")
    return f"{index:04d}-{path_slug}-{digest}.md"


def markdown_from_response(response: Any, *, css_selector: str | None = None) -> str:
    from scrapling.core.shell import Convertor

    try:
        parts = Convertor._extract_content(  # noqa: SLF001 - intentional helper use for dry-run smoke tooling.
            response,
            extraction_type="markdown",
            css_selector=css_selector,
            main_content_only=True,
        )
        return "".join(parts).strip()
    except Exception:
        text = response.get_all_text(strip=True, ignore_tags=("script", "style", "noscript", "svg", "iframe"))
        return str(text).strip()


def build_spider_class(
    *,
    base_url: str,
    allowed_host: str,
    max_pages: int,
    concurrent_requests: int,
    concurrent_requests_per_domain: int,
    download_delay: float,
    css_selector: str | None,
):
    from scrapling.spiders import LinkExtractor, Spider

    _base_url = base_url
    _allowed_host = allowed_host
    _max_pages = max_pages
    _concurrent_requests = concurrent_requests
    _concurrent_requests_per_domain = concurrent_requests_per_domain
    _download_delay = download_delay
    _css_selector = css_selector

    class SiteDryRunSpider(Spider):
        name = "site_dry_crawl"
        robots_txt_obey = True
        start_urls = [_base_url]
        allowed_domains = {_allowed_host}
        concurrent_requests = _concurrent_requests
        concurrent_requests_per_domain = _concurrent_requests_per_domain
        download_delay = _download_delay
        max_blocked_retries = 1
        logging_level = 30  # WARNING; keep helper output machine-readable.

        def __init__(self) -> None:
            self._scheduled_urls: set[str] = {_base_url}
            self._links = LinkExtractor(allow_domains=_allowed_host)
            super().__init__()

        async def parse(self, response):
            content_type = ""
            if response.headers:
                content_type = response.headers.get("content-type") or response.headers.get("Content-Type") or ""

            if response.status == 200:
                title = response.css("title::text").get() or response.css("h1::text").get() or response.url
                markdown = markdown_from_response(response, css_selector=_css_selector)
                if markdown:
                    yield {
                        "url": response.url,
                        "title": str(title).strip(),
                        "status": response.status,
                        "content_type": content_type,
                        "markdown": markdown,
                        "source_hash": sha256_text(markdown),
                    }

            if len(self._scheduled_urls) >= _max_pages:
                return

            for url in self._links.extract(response):
                if len(self._scheduled_urls) >= _max_pages:
                    break
                if url in self._scheduled_urls:
                    continue
                self._scheduled_urls.add(url)
                yield response.follow(url, callback=self.parse)

    return SiteDryRunSpider


def write_markdown_corpus(items: list[dict[str, Any]], pages_dir: Path) -> None:
    pages_dir.mkdir(parents=True, exist_ok=True)
    crawl_timestamp = datetime.now(timezone.utc).isoformat()
    for index, item in enumerate(items, start=1):
        filename = page_filename(str(item.get("url", "")), str(item.get("title", "")), index)
        path = pages_dir / filename
        frontmatter = {
            "url": item.get("url", ""),
            "title": item.get("title", ""),
            "status": item.get("status", ""),
            "content_type": item.get("content_type", ""),
            "source_hash": item.get("source_hash", ""),
            "crawl_timestamp": crawl_timestamp,
            "fetcher": "scrapling-static-spider",
        }
        body = str(item.get("markdown", "")).strip()
        lines = ["---"]
        lines.extend(f"{key}: {yaml_scalar(value)}" for key, value in frontmatter.items())
        lines.extend(["---", "", body, ""])
        path.write_text("\n".join(lines), encoding="utf-8")


def summarize_sample_chunks(plan, sample_size: int = 3) -> list[dict[str, object]]:
    samples = []
    for chunk in plan.chunks[:sample_size]:
        samples.append(
            {
                "id": chunk.id,
                "title": chunk.title,
                "url": chunk.url,
                "section_path": chunk.section_path,
                "content_preview": chunk.content[:240].replace("\n", " "),
            }
        )
    return samples


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    require_scrapling()
    allowed_host = host_from_url(args.base_url)

    spider_cls = build_spider_class(
        base_url=args.base_url,
        allowed_host=allowed_host,
        max_pages=args.max_pages,
        concurrent_requests=args.concurrent_requests,
        concurrent_requests_per_domain=args.concurrent_requests_per_domain,
        download_delay=args.download_delay,
        css_selector=args.css_selector,
    )
    result = spider_cls().start()

    items = list(result.items)
    pages_dir = args.out_dir / "pages"
    write_markdown_corpus(items, pages_dir)
    plan = process_corpus(
        pages_dir,
        limit_chunks=args.max_chunks,
        target_tokens=args.target_tokens,
        overlap_sentences=args.overlap_sentences,
    )

    summary = {
        "command": "scrapling-dry-crawl",
        "dry_run": True,
        "credentials_required": False,
        "turbopuffer_api_calls": False,
        "api_calls_occurred": False,
        "base_url": args.base_url,
        "allowed_host": allowed_host,
        "namespace_candidate": namespace_candidate(args.base_url),
        "out_dir": str(args.out_dir),
        "pages_dir": str(pages_dir),
        "max_pages": args.max_pages,
        "css_selector": args.css_selector,
        "pages_scraped": len(items),
        "requests_count": result.stats.requests_count,
        "robots_disallowed_count": result.stats.robots_disallowed_count,
        "blocked_requests_count": result.stats.blocked_requests_count,
        "failed_requests_count": result.stats.failed_requests_count,
        "chunks_generated": plan.stats.chunks_generated,
        "files_error": plan.stats.files_error,
        "limit_reached": plan.limit_reached,
        "sample_chunks": summarize_sample_chunks(plan),
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
