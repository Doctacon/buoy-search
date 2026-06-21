from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import json
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

from turbo_search.cli import build_parser, main
from turbo_search.crawler import CrawlOptions


class CliTests(unittest.TestCase):
    def test_help_mentions_safe_index_options(self) -> None:
        help_text = build_parser().format_help()

        self.assertIn("dry-run", help_text)
        self.assertIn("index", help_text)
        self.assertIn("crawl", help_text)
        self.assertIn("retrieve", help_text)
        self.assertIn("evals", help_text)

    def test_index_command_is_dry_run_and_needs_no_credentials(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp)
            (corpus / "page.md").write_text(
                "---\nurl: https://jellyfish.co/blog/test/\ntitle: Test\n---\n\n"
                "## Section\nThis is useful page text.\n",
                encoding="utf-8",
            )
            stdout = StringIO()
            with redirect_stdout(stdout):
                result = main(["index", "--corpus-dir", str(corpus)])

        payload = json.loads(stdout.getvalue())
        self.assertEqual(result, 0)
        self.assertTrue(payload["dry_run"])
        self.assertFalse(payload["credentials_required"])
        self.assertFalse(payload["turbopuffer_api_calls"])
        self.assertFalse(payload["api_calls_occurred"])
        self.assertEqual(payload["files_seen"], 1)
        self.assertEqual(payload["chunks_generated"], 1)
        self.assertEqual(payload["rows_written"], 0)
        self.assertEqual(payload["region"], "gcp-us-central1")
        self.assertEqual(payload["namespace"], "jellyfish-site-docs-v1")

    def test_index_command_supports_limits(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp)
            for index in range(3):
                (corpus / f"page-{index}.md").write_text(
                    f"---\ntitle: Page {index}\n---\n\nBody {index}.\n",
                    encoding="utf-8",
                )
            stdout = StringIO()
            with redirect_stdout(stdout):
                result = main(
                    [
                        "index",
                        "--corpus-dir",
                        str(corpus),
                        "--max-files",
                        "2",
                        "--limit-chunks",
                        "1",
                        "--batch-size",
                        "10",
                    ]
                )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(result, 0)
        self.assertEqual(payload["files_discovered"], 3)
        self.assertEqual(payload["files_seen"], 2)
        self.assertEqual(payload["chunks_generated"], 1)
        self.assertEqual(payload["max_files"], 2)
        self.assertEqual(payload["limit_chunks"], 1)
        self.assertEqual(payload["batch_size"], 10)

    def test_index_command_missing_corpus_exits_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing-corpus"
            stdout = StringIO()
            stderr = StringIO()
            with redirect_stdout(stdout), redirect_stderr(stderr):
                result = main(["index", "--corpus-dir", str(missing)])

        self.assertEqual(result, 2)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("Corpus directory not found", stderr.getvalue())
        self.assertIn("missing-corpus", stderr.getvalue())

    def test_crawl_command_validates_base_url_before_crawling(self) -> None:
        stdout = StringIO()
        stderr = StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["crawl", "--base-url", "/relative", "--json"])

        self.assertEqual(result, 2)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("base URL must be an absolute http(s) URL", stderr.getvalue())

    def test_crawl_command_is_dry_run_and_needs_no_credentials(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "crawl"
            fake_summary = {
                "command": "crawl",
                "dry_run": True,
                "credentials_required": False,
                "turbopuffer_api_calls": False,
                "api_calls_occurred": False,
                "base_url": "https://scrapling.readthedocs.io/en/latest/",
                "allowed_host": "scrapling.readthedocs.io",
                "namespace_candidate": "site-scrapling-readthedocs-io-v1",
                "crawl_strategy": "sitemap",
                "out_dir": str(out_dir),
                "pages_dir": str(out_dir / "pages"),
                "max_pages": 3,
                "max_chunks": 5,
                "css_selector": ".md-content__inner",
                "pages_scraped": 2,
                "requests_count": 4,
                "robots_disallowed_count": 0,
                "blocked_requests_count": 0,
                "failed_requests_count": 0,
                "chunks_generated": 5,
                "files_error": 0,
                "limit_reached": True,
                "sample_chunks": [
                    {
                        "id": "chunk-1",
                        "title": "Intro",
                        "url": "https://scrapling.readthedocs.io/en/latest/",
                        "section_path": "",
                        "content_preview": "Scrapling docs",
                    }
                ],
            }
            stdout = StringIO()
            with patch("turbo_search.cli.crawl_site", return_value=fake_summary) as crawl_mock:
                with redirect_stdout(stdout):
                    result = main(
                        [
                            "crawl",
                            "--base-url",
                            "https://scrapling.readthedocs.io/en/latest/",
                            "--out-dir",
                            str(out_dir),
                            "--max-pages",
                            "3",
                            "--max-chunks",
                            "5",
                            "--css-selector",
                            ".md-content__inner",
                            "--json",
                        ]
                    )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(result, 0)
        self.assertTrue(payload["dry_run"])
        self.assertFalse(payload["credentials_required"])
        self.assertFalse(payload["turbopuffer_api_calls"])
        self.assertFalse(payload["api_calls_occurred"])
        self.assertEqual(payload["namespace_candidate"], "site-scrapling-readthedocs-io-v1")
        self.assertEqual(payload["sample_chunks"][0]["title"], "Intro")
        crawl_mock.assert_called_once()
        options = crawl_mock.call_args.args[0]
        self.assertIsInstance(options, CrawlOptions)
        self.assertEqual(options.max_pages, 3)
        self.assertEqual(options.max_chunks, 5)
        self.assertEqual(options.css_selector, ".md-content__inner")

    def test_retrieve_command_dry_run_plan_needs_no_credentials(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            result = main(
                [
                    "retrieve",
                    "What are DORA metrics?",
                    "--dry-run",
                    "--top-k",
                    "3",
                    "--candidates",
                    "20",
                    "--doc-kind",
                    "library",
                    "--json",
                ]
            )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(result, 0)
        self.assertTrue(payload["dry_run"])
        self.assertFalse(payload["credentials_required"])
        self.assertFalse(payload["turbopuffer_api_calls"])
        self.assertEqual(payload["top_k"], 3)
        self.assertEqual(payload["candidates"], 20)
        self.assertEqual(payload["doc_kind"], "library")
        self.assertEqual(payload["retrieval"]["rerank_by"], ["RRF"])
        include_attributes = payload["retrieval"]["subqueries"][0]["include_attributes"]
        self.assertNotIn("vector", include_attributes)

    def test_evals_command_dry_run_lists_cases_without_credentials(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            result = main(["evals", "--dry-run", "--top-k", "3", "--candidates", "30", "--json"])

        payload = json.loads(stdout.getvalue())
        self.assertEqual(result, 0)
        self.assertTrue(payload["dry_run"])
        self.assertFalse(payload["credentials_required"])
        self.assertFalse(payload["turbopuffer_api_calls"])
        self.assertGreaterEqual(payload["total"], 5)
        self.assertEqual(payload["top_k"], 3)
        self.assertEqual(payload["candidates"], 30)
        first_case = payload["cases"][0]
        self.assertIn("question", first_case)
        self.assertIn("expected_urls", first_case)
        self.assertEqual(first_case["status"], "not_run")
        self.assertEqual(first_case["top_hits"], [])


if __name__ == "__main__":
    unittest.main()
