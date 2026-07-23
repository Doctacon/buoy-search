from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

from buoy_search.bigquery_relation import (
    BigQueryRelationError,
    bigquery_relation_source,
    scan_bigquery_relation,
    validate_bigquery_relation,
)
from buoy_search.crawler import CrawlOptions
from buoy_search.bigquery_relation import crawl_bigquery_relation


class FakeField:
    def __init__(self, name: str) -> None:
        self.name = name


class FakeQueryJobConfig:
    def __init__(self, **kwargs: object) -> None:
        self.__dict__.update(kwargs)


class FakeJob:
    def __init__(
        self,
        rows: list[object],
        *,
        estimated: int = 0,
        actual: int = 0,
        cache_hit: bool = False,
        job_id: str = "job-123",
    ) -> None:
        self.rows = rows
        self.total_bytes_processed = estimated or actual
        self.cache_hit = cache_hit
        self.job_id = job_id
        self.result_timeouts: list[float] = []
        self.cancelled = False

    def result(self, *, timeout: float) -> list[object]:
        self.result_timeouts.append(timeout)
        return self.rows

    def cancel(self) -> None:
        self.cancelled = True


class FakeBigQueryClient:
    instances: list["FakeBigQueryClient"] = []
    schema = [FakeField("document_id"), FakeField("content"), FakeField("title")]
    validation = {
        "rows_discovered": 4,
        "invalid_ids": 0,
        "skipped_empty": 1,
        "nonblank_documents": 3,
    }
    duplicate: list[object] = []
    documents = [
        {"document_id": "a/1", "content": "Alpha body", "title": "Alpha"},
        {"document_id": "b", "content": "Beta body", "title": None},
    ]
    estimate = 100

    def __init__(self, *, project: str | None, location: str | None) -> None:
        self.project = project
        self.location = location
        self.queries: list[tuple[str, FakeQueryJobConfig]] = []
        self.jobs: list[FakeJob] = []
        self.get_table_calls: list[str] = []
        self.closed = False
        type(self).instances.append(self)

    def get_table(self, relation: str) -> object:
        self.get_table_calls.append(relation)
        return types.SimpleNamespace(schema=list(type(self).schema), table_type="VIEW")

    def close(self) -> None:
        self.closed = True

    def query(self, sql: str, *, job_config: FakeQueryJobConfig) -> FakeJob:
        self.queries.append((sql, job_config))
        if job_config.dry_run:
            job = FakeJob([], estimated=type(self).estimate)
        elif "AS rows_discovered" in sql:
            job = FakeJob([dict(type(self).validation)], actual=40)
        elif "HAVING COUNT(*) > 1" in sql:
            job = FakeJob(list(type(self).duplicate), actual=30)
        else:
            job = FakeJob(list(type(self).documents), actual=20, cache_hit=True)
        self.jobs.append(job)
        return job


class BigQueryRelationTests(unittest.TestCase):
    def setUp(self) -> None:
        FakeBigQueryClient.instances.clear()
        FakeBigQueryClient.schema = [
            FakeField("document_id"),
            FakeField("content"),
            FakeField("title"),
        ]
        FakeBigQueryClient.validation = {
            "rows_discovered": 4,
            "invalid_ids": 0,
            "skipped_empty": 1,
            "nonblank_documents": 3,
        }
        FakeBigQueryClient.duplicate = []
        FakeBigQueryClient.documents = [
            {"document_id": "a/1", "content": "Alpha body", "title": "Alpha"},
            {"document_id": "b", "content": "Beta body", "title": None},
        ]
        FakeBigQueryClient.estimate = 100
        self.module = types.SimpleNamespace(
            Client=FakeBigQueryClient,
            QueryJobConfig=FakeQueryJobConfig,
        )

    def test_source_identity_and_identifier_validation(self) -> None:
        source = bigquery_relation_source(
            relation="source-project.corpus.documents",
            source_id="gong-calls",
            query_project="billing-project",
            location="US",
        )
        self.assertEqual(source.base_url, "bigquery://gong-calls")
        self.assertEqual(source.site_id, "bigquery-gong-calls")
        self.assertEqual(source.namespace_candidate, "bigquery-gong-calls-v1")
        self.assertEqual(source.document_url("call/a"), "bigquery://gong-calls/call%2Fa")
        self.assertNotIn("billing-project", repr(source))
        for invalid in (
            "project.dataset",
            "Project.dataset.table",
            "project.dataset.table;DROP",
            "project.data set.table",
            "project.dataset.*",
            "`project.dataset.table`",
        ):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                validate_bigquery_relation(invalid)
        with self.assertRaises(ValueError):
            bigquery_relation_source(
                relation="source-project.corpus.documents",
                source_id="docs",
                id_column="CAST(id AS STRING)",
            )

    def test_scan_uses_adc_client_schema_dry_runs_limits_labels_and_timeout(self) -> None:
        source = bigquery_relation_source(
            relation="source-project.corpus.documents",
            source_id="gong-calls",
            query_project="billing-project",
            location="US",
            maximum_bytes_billed=1000,
            query_timeout=17.5,
            operation="crawl",
        )
        with patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module):
            result = scan_bigquery_relation(source, max_documents=2)

        client = FakeBigQueryClient.instances[0]
        self.assertEqual((client.project, client.location), ("billing-project", "US"))
        self.assertEqual(client.get_table_calls, ["source-project.corpus.documents"])
        self.assertEqual(len(client.queries), 6)
        dry = [config for _, config in client.queries if config.dry_run]
        actual = [config for _, config in client.queries if not config.dry_run]
        self.assertEqual(len(dry), 3)
        self.assertTrue(all(config.maximum_bytes_billed == 1000 for config in dry + actual))
        self.assertTrue(all(config.labels["buoy"] == "database-relation" for config in dry + actual))
        self.assertTrue(all(config.labels["buoy-operation"] == "crawl" for config in dry + actual))
        self.assertTrue(all(config.job_timeout_ms == 17500 for config in actual))
        self.assertTrue(client.closed)
        self.assertEqual(
            [job.result_timeouts for job in client.jobs if job.result_timeouts],
            [[17.5], [17.5], [17.5]],
        )
        self.assertIn("ORDER BY document_id LIMIT 2", client.queries[-1][0])
        self.assertNotRegex("\n".join(sql for sql, _ in client.queries), r"(?i)\b(CREATE|INSERT|UPDATE|DELETE|MERGE|DROP|ALTER)\b")
        self.assertEqual([doc.document_id for doc in result.documents], ["a/1", "b"])
        self.assertEqual(result.documents[1].title, "b")
        self.assertEqual(result.rows_discovered, 4)
        self.assertEqual(result.documents_skipped_empty, 1)
        self.assertEqual(result.documents_skipped_limit, 1)
        self.assertEqual(result.diagnostics["bigquery_estimated_bytes_processed"], 300)
        self.assertEqual(result.diagnostics["bigquery_total_bytes_processed"], 90)
        self.assertEqual(result.diagnostics["bigquery_query_job_id"], "job-123")

    def test_custom_mapping_and_missing_title_auto_detection(self) -> None:
        FakeBigQueryClient.schema = [FakeField("call_id"), FakeField("transcript")]
        source = bigquery_relation_source(
            relation="source-project.corpus.calls",
            source_id="calls",
            id_column="call_id",
            content_column="transcript",
        )
        with patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module):
            result = scan_bigquery_relation(source, max_documents=2)
        self.assertIsNone(result.title_column)
        self.assertIn("CAST(NULL AS STRING) AS title", FakeBigQueryClient.instances[0].queries[-1][0])

    def test_dry_run_cap_fails_before_execution(self) -> None:
        FakeBigQueryClient.estimate = 500
        source = bigquery_relation_source(
            relation="source-project.corpus.documents",
            source_id="docs",
            maximum_bytes_billed=1000,
        )
        with patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module):
            with self.assertRaisesRegex(BigQueryRelationError, "estimated 1500 bytes; cap 1000"):
                scan_bigquery_relation(source, max_documents=2)
        self.assertTrue(all(config.dry_run for _, config in FakeBigQueryClient.instances[0].queries))

    def test_null_duplicate_and_all_empty_failures(self) -> None:
        source = bigquery_relation_source(
            relation="source-project.corpus.documents", source_id="docs"
        )
        FakeBigQueryClient.validation = {
            "rows_discovered": 1,
            "invalid_ids": 1,
            "skipped_empty": 0,
            "nonblank_documents": 1,
        }
        with patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module):
            with self.assertRaisesRegex(BigQueryRelationError, "null or blank"):
                scan_bigquery_relation(source, max_documents=1)
        FakeBigQueryClient.instances.clear()
        FakeBigQueryClient.validation["invalid_ids"] = 0
        FakeBigQueryClient.duplicate = [{"document_id": "1", "duplicate_count": 2}]
        with patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module):
            with self.assertRaisesRegex(BigQueryRelationError, "duplicate document ID '1'"):
                scan_bigquery_relation(source, max_documents=1)
        FakeBigQueryClient.instances.clear()
        FakeBigQueryClient.duplicate = []
        FakeBigQueryClient.validation["nonblank_documents"] = 0
        FakeBigQueryClient.validation["skipped_empty"] = 1
        with patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module):
            with self.assertRaisesRegex(BigQueryRelationError, "no nonblank documents"):
                scan_bigquery_relation(source, max_documents=1)

    def test_poll_timeout_requests_cancellation_and_closes_client(self) -> None:
        source = bigquery_relation_source(
            relation="source-project.corpus.documents", source_id="docs", query_timeout=2.5
        )
        original_query = FakeBigQueryClient.query

        def timeout_query(client, sql, *, job_config):
            job = original_query(client, sql, job_config=job_config)
            if not job_config.dry_run and "AS rows_discovered" in sql:
                def timeout_result(*, timeout):
                    job.result_timeouts.append(timeout)
                    raise TimeoutError("secret detail")
                job.result = timeout_result
            return job

        with (
            patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module),
            patch.object(FakeBigQueryClient, "query", new=timeout_query),
            self.assertRaisesRegex(BigQueryRelationError, "cancellation was requested"),
        ):
            scan_bigquery_relation(source, max_documents=1)
        client = FakeBigQueryClient.instances[0]
        timed_out = next(job for job in client.jobs if job.result_timeouts)
        self.assertTrue(timed_out.cancelled)
        self.assertTrue(client.closed)

    def test_nonfinite_timeout_is_rejected(self) -> None:
        for timeout in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(timeout=timeout), self.assertRaisesRegex(ValueError, "finite value"):
                bigquery_relation_source(
                    relation="source-project.corpus.documents",
                    source_id="docs",
                    query_timeout=timeout,
                )

    def test_sdk_error_details_are_not_forwarded_and_client_closes(self) -> None:
        source = bigquery_relation_source(
            relation="source-project.corpus.documents", source_id="docs"
        )
        with (
            patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module),
            patch.object(FakeBigQueryClient, "get_table", side_effect=RuntimeError("token=secret")),
        ):
            with self.assertRaises(BigQueryRelationError) as raised:
                scan_bigquery_relation(source, max_documents=1)
        self.assertNotIn("token=secret", str(raised.exception))
        self.assertIn("RuntimeError", str(raised.exception))
        self.assertTrue(FakeBigQueryClient.instances[0].closed)

    def test_missing_dependency_error(self) -> None:
        import buoy_search.bigquery_relation as module

        with patch.dict(sys.modules, {"google.cloud": None, "google.cloud.bigquery": None}):
            with self.assertRaisesRegex(BigQueryRelationError, "uv sync --extra bigquery"):
                module._load_bigquery()

    def test_crawl_summary_has_truthful_remote_activity_without_connection_details(self) -> None:
        source = bigquery_relation_source(
            relation="source-project.corpus.documents",
            source_id="docs",
            query_project="billing-secret",
            location="EU",
        )
        with tempfile.TemporaryDirectory() as tmp:
            options = CrawlOptions(base_url=source.base_url, out_dir=Path(tmp), max_pages=2, max_chunks=10)
            with patch("buoy_search.bigquery_relation._load_bigquery", return_value=self.module):
                summary = crawl_bigquery_relation(source, options)
            self.assertTrue(summary["credentials_required"])
            self.assertTrue(summary["api_calls_occurred"])
            self.assertTrue(summary["source_credentials_required"])
            self.assertFalse(summary["turbopuffer_credentials_required"])
            serialized = str(summary) + "".join(
                page.read_text(encoding="utf-8") for page in (Path(tmp) / "pages").glob("*.md")
            )
            self.assertNotIn("billing-secret", serialized)
            self.assertNotIn("EU", serialized)


if __name__ == "__main__":
    unittest.main()
