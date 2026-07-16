from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


SCRIPT = Path("autoresearch/runs/semantic-routing-representative-20260715/evaluate.py").resolve()
SPEC = importlib.util.spec_from_file_location("semantic_routing_representative", SCRIPT)
assert SPEC and SPEC.loader
routing = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(routing)


class RepresentativeSemanticRoutingTests(unittest.TestCase):
    def test_tracked_inputs_and_cards_validate_exact_13_by_90_contract(self) -> None:
        cards = routing.load_cards()
        routing.validate_cards(cards)
        questions = routing.load_questions()

        self.assertEqual([card["repo_key"] for card in cards], sorted(routing.DATASETS))
        self.assertEqual(len(cards), 13)
        self.assertEqual(len(questions), 90)
        self.assertEqual(len({question["identity"] for question in questions}), 90)
        self.assertTrue(all(question["identity"] == f"{question['repo_key']}:{question['case_id']}" for question in questions))

    def test_card_validation_fails_closed_for_bijection_public_and_contract_errors(self) -> None:
        cards = routing.load_cards()
        variants = []
        variants.append(cards[:-1])
        duplicate_key = [dict(card) for card in cards]
        duplicate_key[-1]["repo_key"] = duplicate_key[0]["repo_key"]
        variants.append(duplicate_key)
        duplicate_namespace = [dict(card) for card in cards]
        duplicate_namespace[-1]["namespace"] = duplicate_namespace[0]["namespace"]
        variants.append(duplicate_namespace)
        private = [dict(card) for card in cards]
        private[0]["public"] = False
        variants.append(private)
        incompatible = [dict(card) for card in cards]
        incompatible[0]["embedding_contract"] = {**routing.EXPECTED_CONTRACT, "revision": "mutable"}
        variants.append(incompatible)
        missing = [dict(card) for card in cards]
        del missing[0]["summary"]
        variants.append(missing)

        for variant in variants:
            with self.subTest(variant=variants.index(variant)):
                with self.assertRaises(routing.ExperimentError):
                    routing.validate_cards(variant)

    def test_card_descriptions_do_not_copy_questions_case_ids_or_file_judgments(self) -> None:
        cards = routing.load_cards()
        questions = routing.load_questions()
        descriptions = "\n".join(
            " ".join(
                [str(card["title"]), str(card["summary"]), *card["aliases"], *card["tags"]]
            ).casefold()
            for card in cards
        )
        datasets = [
            json.loads((routing.REPO_ROOT / details[1]).read_text(encoding="utf-8"))
            for details in routing.DATASETS.values()
        ]

        self.assertTrue(all(question["question"].casefold() not in descriptions for question in questions))
        self.assertTrue(all(question["case_id"].casefold() not in descriptions for question in questions))
        for dataset in datasets:
            for case in dataset["cases"]:
                for judgment in case.get("judgments", []):
                    for field in ("repo_path", "url", "section_path"):
                        locator = judgment.get(field)
                        if locator:
                            self.assertNotIn(str(locator).casefold(), descriptions)

    def test_normalization_and_complete_phrase_matching_are_canonical(self) -> None:
        self.assertEqual(routing.normalize("  ＣＬＩ___Café—TOOLS  "), "cli café tools")
        self.assertTrue(routing.contains_phrase("a click cli framework", "click cli"))
        self.assertFalse(routing.contains_phrase("a clicker cli framework", "click"))
        self.assertFalse(routing.contains_phrase("click advanced cli", "click cli"))

    def test_lexical_descriptors_are_deduplicated_and_frequency_does_not_inflate_score(self) -> None:
        cards = [
            {
                "repo_key": "alpha",
                "namespace": "n-alpha",
                "title": "Alpha",
                "aliases": ["ALPHA", "alpha tool"],
                "tags": ["tool", "tool"],
            },
            {
                "repo_key": "beta",
                "namespace": "n-beta",
                "title": "Beta",
                "aliases": [],
                "tags": [],
            },
        ]
        once = routing.lexical_rank("alpha tool", cards)
        repeated = routing.lexical_rank("alpha alpha tool alpha tool", cards)

        self.assertEqual(once[0]["raw_score"], repeated[0]["raw_score"])
        self.assertEqual(once[0]["raw_score"]["distinct_matched_descriptors"], 3)
        self.assertEqual(once[0]["raw_score"]["total_matched_token_count"], 4)
        self.assertEqual(len(once), 1)

    def test_lexical_ranking_uses_repo_key_as_final_tie_breaker(self) -> None:
        cards = [
            {"repo_key": "zeta", "namespace": "n-zeta", "title": "tool", "aliases": [], "tags": []},
            {"repo_key": "alpha", "namespace": "n-alpha", "title": "tool", "aliases": [], "tags": []},
        ]
        ranking = routing.lexical_rank("Which tool?", cards)
        self.assertEqual([item["repo_key"] for item in ranking], ["alpha", "zeta"])

    def test_semantic_ranking_with_injected_vectors_uses_cosine_and_tie_breaker(self) -> None:
        cards = [
            {"repo_key": "zeta", "namespace": "n-zeta"},
            {"repo_key": "alpha", "namespace": "n-alpha"},
            {"repo_key": "beta", "namespace": "n-beta"},
        ]
        ranking = routing.semantic_rank(
            [1.0, 0.0], cards, {"zeta": [1.0, 0.0], "alpha": [1.0, 0.0], "beta": [0.0, 1.0]}
        )
        self.assertEqual([item["repo_key"] for item in ranking], ["alpha", "zeta", "beta"])
        self.assertEqual(ranking[0]["raw_score"], 1.0)

    def test_hybrid_uses_equal_weight_production_rrf_and_deterministic_ties(self) -> None:
        lexical = [
            {"rank": 1, "repo_key": "alpha", "namespace": "n-alpha"},
            {"rank": 2, "repo_key": "beta", "namespace": "n-beta"},
        ]
        semantic = [
            {"rank": 1, "repo_key": "beta", "namespace": "n-beta"},
            {"rank": 2, "repo_key": "alpha", "namespace": "n-alpha"},
            {"rank": 3, "repo_key": "gamma", "namespace": "n-gamma"},
        ]
        ranking = routing.hybrid_rank(lexical, semantic)

        self.assertEqual(routing.RRF_K, 60)
        self.assertEqual([item["repo_key"] for item in ranking], ["alpha", "beta", "gamma"])
        self.assertAlmostEqual(ranking[0]["raw_score"], 1 / 61 + 1 / 62)
        self.assertAlmostEqual(ranking[1]["raw_score"], 1 / 62 + 1 / 61)

    def test_metrics_include_unranked_homes(self) -> None:
        metrics = routing.aggregate_metrics(
            [{"home_namespace_rank": 1}, {"home_namespace_rank": 3}, {"home_namespace_rank": None}]
        )
        self.assertAlmostEqual(metrics["mrr"], (1 + 1 / 3) / 3)
        self.assertEqual(metrics["recall_at_1"], 1 / 3)
        self.assertEqual(metrics["recall_at_3"], 2 / 3)
        self.assertEqual(metrics["recall_at_5"], 2 / 3)
        self.assertEqual(metrics["unranked_count"], 1)
        self.assertEqual(metrics["evaluated_count"], 3)

    def test_existing_final_result_requires_explicit_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = Path(tmp) / "result.json"
            result.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(routing.ExperimentError, "Refusing to overwrite"):
                routing.refuse_result_overwrite(result, replace=False)
            routing.refuse_result_overwrite(result, replace=True)

    def test_model_constructor_uses_exact_revision_and_local_files_only(self) -> None:
        captured = {}

        def fake_constructor(model_id: str, **kwargs: object) -> object:
            captured.update({"model_id": model_id, **kwargs})
            return object()

        with patch.dict(sys.modules, {"sentence_transformers": SimpleNamespace(SentenceTransformer=fake_constructor)}):
            routing.construct_model()

        self.assertEqual(captured["model_id"], routing.MODEL_ID)
        self.assertEqual(captured["revision"], routing.MODEL_REVISION)
        self.assertIs(captured["local_files_only"], True)

    def test_environment_controls_are_exact_and_credentials_are_removed(self) -> None:
        snapshot = routing.model_snapshot_path()
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            os.environ,
            {name: "must-not-be-read-or-used" for name in routing.CREDENTIAL_ENV},
            clear=True,
        ):
            routing.prepare_environment(Path(tmp), snapshot)
            self.assertTrue(all(os.environ[name] == "1" for name in routing.OFFLINE_ENV))
            self.assertTrue(all(name not in os.environ for name in routing.CREDENTIAL_ENV))
            self.assertEqual(os.environ["TMPDIR"], tmp)
            self.assertEqual(os.environ["HF_HOME"], str(snapshot.parents[3]))

    def test_socket_and_path_guards_reject_network_cache_mutation_and_external_writes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run_dir = root / "run"
            temp_dir = run_dir / "temp"
            outside = root / "outside.txt"
            cache_file = root / "model-cache" / "weights"
            run_dir.mkdir()
            temp_dir.mkdir()
            cache_file.parent.mkdir()
            cache_file.write_text("cached", encoding="utf-8")

            with routing.execution_guards(run_dir, temp_dir):
                with self.assertRaisesRegex(routing.ExperimentError, "Network access"):
                    socket.create_connection(("127.0.0.1", 9))
                with self.assertRaisesRegex(routing.ExperimentError, "Network access"):
                    socket.getaddrinfo("example.com", 443)
                with self.assertRaisesRegex(routing.ExperimentError, "outside experiment"):
                    outside.write_text("blocked", encoding="utf-8")
                with self.assertRaisesRegex(routing.ExperimentError, "outside experiment"):
                    cache_file.write_text("mutation", encoding="utf-8")
                (run_dir / "allowed.txt").write_text("ok", encoding="utf-8")
                (temp_dir / "allowed.txt").write_text("ok", encoding="utf-8")

            self.assertFalse(outside.exists())
            self.assertEqual(cache_file.read_text(encoding="utf-8"), "cached")

    def test_gitignore_exception_tracks_only_the_representative_run(self) -> None:
        target = "autoresearch/runs/semantic-routing-representative-20260715/evaluate.py"
        unrelated = "autoresearch/runs/unrelated-run/result.json"
        target_result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-q", target], cwd=routing.REPO_ROOT, check=False
        )
        unrelated_result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-q", unrelated], cwd=routing.REPO_ROOT, check=False
        )
        self.assertEqual(target_result.returncode, 1)
        self.assertEqual(unrelated_result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
