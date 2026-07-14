from __future__ import annotations

import os
from unittest.mock import patch
import unittest

from buoy_search.config import (
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_EMBEDDING_PRECISION,
    RuntimeConfigError,
    load_config,
)


class RuntimeConfigTests(unittest.TestCase):
    def test_default_embedding_model_uses_no_branded_environment(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            config = load_config(warning_callback=lambda _message: self.fail("unexpected warning"))

        self.assertEqual(config.embedding_model, DEFAULT_EMBEDDING_MODEL)

    def test_current_embedding_model_environment_wins(self) -> None:
        warnings: list[str] = []
        with patch.dict(os.environ, {"BUOY_EMBEDDING_MODEL": "current/model"}, clear=True):
            config = load_config(warning_callback=warnings.append)

        self.assertEqual(config.embedding_model, "current/model")
        self.assertEqual(warnings, [])

    def test_legacy_embedding_model_environment_warns_and_falls_back(self) -> None:
        warnings: list[str] = []
        with patch.dict(os.environ, {"TURBO_SEARCH_EMBEDDING_MODEL": "legacy/model"}, clear=True):
            config = load_config(warning_callback=warnings.append)

        self.assertEqual(config.embedding_model, "legacy/model")
        self.assertEqual(len(warnings), 1)
        self.assertIn("TURBO_SEARCH_EMBEDDING_MODEL is deprecated", warnings[0])
        self.assertIn("BUOY_EMBEDDING_MODEL", warnings[0])

    def test_matching_current_and_legacy_values_use_current_without_warning(self) -> None:
        warnings: list[str] = []
        with patch.dict(
            os.environ,
            {"BUOY_EMBEDDING_MODEL": "same/model", "TURBO_SEARCH_EMBEDDING_MODEL": "same/model"},
            clear=True,
        ):
            config = load_config(warning_callback=warnings.append)

        self.assertEqual(config.embedding_model, "same/model")
        self.assertEqual(warnings, [])

    def test_conflicting_current_and_legacy_values_fail(self) -> None:
        with patch.dict(
            os.environ,
            {"BUOY_EMBEDDING_MODEL": "current/model", "TURBO_SEARCH_EMBEDDING_MODEL": "legacy/model"},
            clear=True,
        ):
            with self.assertRaisesRegex(RuntimeConfigError, "conflicting BUOY_EMBEDDING_MODEL"):
                load_config(warning_callback=lambda _message: None)

    def test_embedding_precision_defaults_to_float32(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            config = load_config(warning_callback=lambda _message: self.fail("unexpected warning"))
        self.assertEqual(config.embedding_precision, DEFAULT_EMBEDDING_PRECISION)

    def test_current_and_legacy_embedding_precision_environment(self) -> None:
        warnings: list[str] = []
        with patch.dict(os.environ, {"TURBO_SEARCH_EMBEDDING_PRECISION": "float16"}, clear=True):
            config = load_config(warning_callback=warnings.append)
        self.assertEqual(config.embedding_precision, "float16")
        self.assertIn("TURBO_SEARCH_EMBEDDING_PRECISION is deprecated", warnings[0])

        with patch.dict(os.environ, {"BUOY_EMBEDDING_PRECISION": "float16"}, clear=True):
            config = load_config(warning_callback=lambda _message: self.fail("unexpected warning"))
        self.assertEqual(config.embedding_precision, "float16")

    def test_embedding_precision_conflict_and_invalid_value_fail(self) -> None:
        with patch.dict(os.environ, {
            "BUOY_EMBEDDING_PRECISION": "float16",
            "TURBO_SEARCH_EMBEDDING_PRECISION": "float32",
        }, clear=True):
            with self.assertRaisesRegex(RuntimeConfigError, "conflicting BUOY_EMBEDDING_PRECISION"):
                load_config(warning_callback=lambda _message: None)
        with patch.dict(os.environ, {"BUOY_EMBEDDING_PRECISION": "int8"}, clear=True):
            with self.assertRaisesRegex(RuntimeConfigError, "float32, float16"):
                load_config(warning_callback=lambda _message: None)

    def test_turbopuffer_environment_names_remain_unchanged(self) -> None:
        with patch.dict(
            os.environ,
            {"TURBOPUFFER_REGION": "local-region", "TURBOPUFFER_NAMESPACE": "site-preserved-v1"},
            clear=True,
        ):
            config = load_config(warning_callback=lambda _message: None)

        self.assertEqual(config.region, "local-region")
        self.assertEqual(config.namespace, "site-preserved-v1")


if __name__ == "__main__":
    unittest.main()
