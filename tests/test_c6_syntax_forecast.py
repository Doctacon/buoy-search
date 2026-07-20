from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "c6_syntax_forecast", ROOT / "scripts" / "c6_syntax_forecast.py"
)
assert SPEC and SPEC.loader
forecast_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(forecast_module)


class C6SyntaxForecastTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.forecast = forecast_module.read_json(ROOT / forecast_module.FORECAST_PATH)
        cls.token_report = forecast_module.read_json(ROOT / forecast_module.TOKEN_REPORT_PATH)

    def test_checked_in_forecast_and_exact_token_checkpoint_validate(self) -> None:
        forecast_module.validate_forecast(self.forecast)
        forecast_module.validate_token_report(self.token_report, self.forecast)
        self.assertFalse(self.token_report["summary"]["ready"])
        self.assertGreater(self.token_report["summary"]["incompatible_rows"], 0)

    def test_validator_reconstructs_row_classes_instead_of_trusting_outer_hash(self) -> None:
        changed = copy.deepcopy(self.forecast)
        changed["repositories"]["buoy"]["arms"]["python-ast"]["source_rows"] += 1
        changed["artifact_sha256"] = forecast_module.artifact_sha256(changed)
        with self.assertRaisesRegex(ValueError, "row classes do not sum"):
            forecast_module.validate_forecast(changed)

    def test_validator_reconstructs_storage_instead_of_trusting_outer_hash(self) -> None:
        changed = copy.deepcopy(self.forecast)
        storage = changed["repositories"]["pytest"]["arms"]["current-default"]["storage_estimates_bytes"]
        storage["raw_384_dim_f16_vectors"] += 2
        changed["artifact_sha256"] = forecast_module.artifact_sha256(changed)
        with self.assertRaisesRegex(ValueError, "raw vector storage mismatch"):
            forecast_module.validate_forecast(changed)

    def test_token_report_rejects_a_row_at_or_below_the_model_maximum(self) -> None:
        changed = copy.deepcopy(self.token_report)
        changed["incompatible_rows"][0]["token_count"] = forecast_module.MODEL_MAX_TOKENS
        changed["summary"]["incompatible_rows_sha256"] = forecast_module.canonical_sha256(
            changed["incompatible_rows"]
        )
        changed["artifact_sha256"] = forecast_module.artifact_sha256(changed)
        with self.assertRaisesRegex(ValueError, "compatible row"):
            forecast_module.validate_token_report(changed, self.forecast)


if __name__ == "__main__":
    unittest.main()
