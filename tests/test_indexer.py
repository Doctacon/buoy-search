from __future__ import annotations

import tempfile
from pathlib import Path
import unittest

from turbo_search.indexer import (
    approximate_token_count,
    build_row,
    chunk_document,
    derive_doc_kind_and_tags,
    parse_markdown_file,
    process_corpus,
)


class MarkdownIndexerTests(unittest.TestCase):
    def test_frontmatter_normalization_and_doc_tags(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp)
            page = corpus / "page.md"
            page.write_text(
                "---\n"
                "url: \"https://jellyfish.co/blog/example-post/\"\n"
                "title: \"Example Post\"\n"
                "---\n\n"
                "[Skip to content](https://jellyfish.co/blog/example-post/#content)\n\n"
                "In this article\n\n"
                "Overview\n"
                "## Overview\n"
                "Actual body text about engineering metrics.\n",
                encoding="utf-8",
            )

            document = parse_markdown_file(page, corpus)
            doc_kind, tags = derive_doc_kind_and_tags(document.url, document.relative_path)

            self.assertEqual(document.url, "https://jellyfish.co/blog/example-post/")
            self.assertEqual(document.title, "Example Post")
            self.assertNotIn("Skip to content", document.normalized_body)
            self.assertNotIn("In this article", document.normalized_body)
            self.assertNotIn("Overview\n## Overview", document.normalized_body)
            self.assertEqual(doc_kind, "blog")
            self.assertIn("example-post", tags)

    def test_chunking_is_heading_aware_and_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp)
            page = corpus / "library.md"
            page.write_text(
                "---\nurl: https://jellyfish.co/library/dora-metrics/\ntitle: DORA Metrics\n---\n\n"
                "Intro sentence for the page. Another intro sentence.\n\n"
                "## Deployment Frequency\n"
                + " ".join(f"Deployment sentence {idx}." for idx in range(80))
                + "\n\n## Change Failure Rate\nStable releases matter.\n",
                encoding="utf-8",
            )

            document = parse_markdown_file(page, corpus)
            chunks_a = chunk_document(document, target_tokens=40, overlap_sentences=2)
            chunks_b = chunk_document(document, target_tokens=40, overlap_sentences=2)

            self.assertGreater(len(chunks_a), 2)
            self.assertEqual([chunk.id for chunk in chunks_a], [chunk.id for chunk in chunks_b])
            self.assertTrue(all(len(chunk.id) <= 64 for chunk in chunks_a))
            self.assertIn("Deployment Frequency", {chunk.section_path for chunk in chunks_a})
            self.assertIn("Title: DORA Metrics", chunks_a[0].embedding_text)
            self.assertTrue(all(approximate_token_count(chunk.content) <= 60 for chunk in chunks_a))

    def test_row_construction_contains_expected_attributes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp)
            page = corpus / "blog.md"
            page.write_text(
                "---\nurl: https://jellyfish.co/blog/test/\ntitle: Test\n---\n\nBody text.\n",
                encoding="utf-8",
            )
            chunk = chunk_document(parse_markdown_file(page, corpus))[0]
            row = build_row(chunk, [0.1, 0.2, 0.3])

            self.assertEqual(
                set(row),
                {
                    "id",
                    "vector",
                    "content",
                    "title",
                    "url",
                    "path",
                    "section_path",
                    "chunk_index",
                    "doc_kind",
                    "tags",
                    "source_hash",
                },
            )
            self.assertEqual(row["id"], chunk.id)
            self.assertEqual(row["vector"], [0.1, 0.2, 0.3])
            self.assertEqual(row["doc_kind"], "blog")

    def test_process_corpus_handles_empty_files_and_limits(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp)
            (corpus / "empty.md").write_text("---\ntitle: Empty\n---\n\n", encoding="utf-8")
            (corpus / "full.md").write_text(
                "---\nurl: https://jellyfish.co/platform/test/\ntitle: Full\n---\n\n"
                "## Section\nUseful text. More useful text.\n",
                encoding="utf-8",
            )

            plan = process_corpus(corpus, limit_chunks=1)

            self.assertEqual(plan.files_discovered, 2)
            self.assertEqual(plan.stats.files_seen, 2)
            self.assertEqual(plan.stats.files_skipped_empty, 1)
            self.assertEqual(plan.stats.files_error, 0)
            self.assertEqual(plan.stats.chunks_generated, 1)
            self.assertTrue(plan.limit_reached or plan.stats.chunks_generated == 1)


if __name__ == "__main__":
    unittest.main()
