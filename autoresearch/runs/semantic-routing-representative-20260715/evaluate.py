#!/usr/bin/env python3
"""One-shot, offline source-attribution evaluation for 13 public repositories."""

from __future__ import annotations

import argparse
import builtins
from contextlib import contextmanager
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import shutil
import socket
import sys
import time
import unicodedata
from typing import Callable, Iterable, Mapping, Sequence

from buoy_search.retriever import RRF_K

RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = RUN_DIR.parents[2]
CARD_PATH = RUN_DIR / "namespace_cards.json"
RESULT_PATH = RUN_DIR / "result.json"
PLAN_PATH = RUN_DIR / "plan.json"
REPORT_PATH = RUN_DIR / "report.md"
TEMP_DIR = RUN_DIR / ".semantic-routing-tmp"
MODEL_ID = "BAAI/bge-small-en-v1.5"
MODEL_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
EXPECTED_QUESTION_COUNT = 90
ROUTE_FAN_OUT = 5
OFFLINE_ENV = {
    "HF_HUB_OFFLINE": "1",
    "TRANSFORMERS_OFFLINE": "1",
    "HF_DATASETS_OFFLINE": "1",
    "HF_HUB_DISABLE_IMPLICIT_TOKEN": "1",
    "HF_HUB_DISABLE_TELEMETRY": "1",
}
CREDENTIAL_ENV = {
    "HF_TOKEN",
    "HUGGING_FACE_HUB_TOKEN",
    "TURBOPUFFER_API_KEY",
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "COHERE_API_KEY",
}
DATASETS = {
    "black": ("github-psf-black-v1", "src/buoy_search/data/black_repo_search_seed_evals.json", 5),
    "buoy": ("github-doctacon-buoy-search-v1", "src/buoy_search/data/buoy_search_repo_search_seed_evals.json", 10),
    "click": ("github-pallets-click-v1", "src/buoy_search/data/click_repo_search_seed_evals.json", 10),
    "django": ("github-django-django-v1", "src/buoy_search/data/django_repo_search_seed_evals.json", 5),
    "flask": ("github-pallets-flask-v1", "src/buoy_search/data/flask_repo_search_seed_evals.json", 5),
    "httpx": ("github-encode-httpx-v1", "src/buoy_search/data/httpx_repo_search_seed_evals.json", 5),
    "mkdocs": ("github-mkdocs-mkdocs-v1", "src/buoy_search/data/mkdocs_repo_search_seed_evals.json", 5),
    "pydantic": ("github-pydantic-pydantic-v1", "src/buoy_search/data/pydantic_repo_search_seed_evals.json", 5),
    "pytest": ("github-pytest-dev-pytest-v1", "src/buoy_search/data/pytest_repo_search_seed_evals.json", 10),
    "requests": ("github-psf-requests-v1", "src/buoy_search/data/requests_repo_search_seed_evals.json", 10),
    "rich": ("github-textualize-rich-v1", "src/buoy_search/data/rich_repo_search_seed_evals.json", 5),
    "ruff": ("github-astral-sh-ruff-v1", "src/buoy_search/data/ruff_repo_search_seed_evals.json", 5),
    "typer": ("github-fastapi-typer-v1", "src/buoy_search/data/typer_repo_search_seed_evals.json", 10),
}
EXPECTED_CONTRACT = {
    "model_id": MODEL_ID,
    "revision": MODEL_REVISION,
    "precision": "float32",
    "normalized": True,
    "dimensions": 384,
}


class ExperimentError(RuntimeError):
    """Raised when the experiment cannot honor its fail-closed contract."""


def normalize(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    normalized = re.sub(r"[^\w]+", " ", normalized, flags=re.UNICODE)
    normalized = re.sub(r"_+", " ", normalized)
    return " ".join(normalized.split())


def contains_phrase(text: str, phrase: str) -> bool:
    text_tokens = text.split()
    phrase_tokens = phrase.split()
    if not phrase_tokens:
        return False
    width = len(phrase_tokens)
    return any(text_tokens[index : index + width] == phrase_tokens for index in range(len(text_tokens) - width + 1))


def card_descriptors(card: Mapping[str, object]) -> set[str]:
    values: list[str] = [str(card["title"])]
    values.extend(str(value) for value in card.get("aliases", []))
    values.extend(str(value) for value in card.get("tags", []))
    return {descriptor for value in values if (descriptor := normalize(value))}


def lexical_rank(question: str, cards: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    normalized_question = normalize(question)
    matches: list[tuple[int, int, str, str, list[str]]] = []
    for card in cards:
        descriptors = sorted(
            descriptor for descriptor in card_descriptors(card) if contains_phrase(normalized_question, descriptor)
        )
        if descriptors:
            token_count = sum(len(descriptor.split()) for descriptor in descriptors)
            matches.append(
                (-len(descriptors), -token_count, str(card["repo_key"]), str(card["namespace"]), descriptors)
            )
    matches.sort(key=lambda item: item[:3])
    return [
        {
            "rank": rank,
            "repo_key": repo_key,
            "namespace": namespace,
            "raw_score": {
                "distinct_matched_descriptors": -descriptor_count,
                "total_matched_token_count": -token_count,
                "matched_descriptors": descriptors,
            },
        }
        for rank, (descriptor_count, token_count, repo_key, namespace, descriptors) in enumerate(matches, start=1)
    ]


def cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    if len(left) != len(right) or not left:
        raise ExperimentError("Semantic vectors must be non-empty and have equal dimensions.")
    left_norm = math.sqrt(sum(float(value) ** 2 for value in left))
    right_norm = math.sqrt(sum(float(value) ** 2 for value in right))
    if not left_norm or not right_norm:
        raise ExperimentError("Semantic vectors must have non-zero magnitude.")
    return sum(float(a) * float(b) for a, b in zip(left, right, strict=True)) / (left_norm * right_norm)


def semantic_rank(
    query_vector: Sequence[float],
    cards: Sequence[Mapping[str, object]],
    card_vectors: Mapping[str, Sequence[float]],
) -> list[dict[str, object]]:
    scored = [
        (
            cosine_similarity(query_vector, card_vectors[str(card["repo_key"])]),
            str(card["repo_key"]),
            str(card["namespace"]),
        )
        for card in cards
    ]
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [
        {"rank": rank, "repo_key": repo_key, "namespace": namespace, "raw_score": score}
        for rank, (score, repo_key, namespace) in enumerate(scored, start=1)
    ]


def hybrid_rank(
    lexical: Sequence[Mapping[str, object]], semantic: Sequence[Mapping[str, object]]
) -> list[dict[str, object]]:
    if RRF_K != 60:
        raise ExperimentError(f"Expected production RRF_K=60, found {RRF_K}.")
    scores: dict[tuple[str, str], float] = {}
    for ranking in (lexical, semantic):
        for item in ranking:
            key = (str(item["repo_key"]), str(item["namespace"]))
            scores[key] = scores.get(key, 0.0) + 1.0 / (RRF_K + int(item["rank"]))
    ordered = sorted(((score, *key) for key, score in scores.items()), key=lambda item: (-item[0], item[1]))
    return [
        {"rank": rank, "repo_key": repo_key, "namespace": namespace, "raw_score": score}
        for rank, (score, repo_key, namespace) in enumerate(ordered, start=1)
    ]


def home_rank(ranking: Sequence[Mapping[str, object]], namespace: str) -> int | None:
    for item in ranking:
        if item["namespace"] == namespace:
            return int(item["rank"])
    return None


def aggregate_metrics(cases: Sequence[Mapping[str, object]]) -> dict[str, object]:
    count = len(cases)
    ranks = [case.get("home_namespace_rank") for case in cases]
    integer_ranks = [int(rank) for rank in ranks if isinstance(rank, int)]
    return {
        "mrr": sum(1.0 / rank for rank in integer_ranks) / count if count else 0.0,
        "recall_at_1": sum(rank <= 1 for rank in integer_ranks) / count if count else 0.0,
        "recall_at_3": sum(rank <= 3 for rank in integer_ranks) / count if count else 0.0,
        "recall_at_5": sum(rank <= 5 for rank in integer_ranks) / count if count else 0.0,
        "unranked_count": count - len(integer_ranks),
        "evaluated_count": count,
    }


def metrics_for_cases(cases: Sequence[Mapping[str, object]]) -> dict[str, object]:
    aggregate = aggregate_metrics(cases)
    per_repository = {
        repo_key: aggregate_metrics([case for case in cases if case["repo_key"] == repo_key])
        for repo_key in DATASETS
    }
    return {"aggregate": aggregate, "per_repository": per_repository}


def load_cards(path: Path = CARD_PATH) -> list[dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping) or not isinstance(payload.get("cards"), list):
        raise ExperimentError("Card configuration must contain a cards array.")
    cards = payload["cards"]
    if not all(isinstance(card, Mapping) for card in cards):
        raise ExperimentError("Every namespace card must be an object.")
    return [dict(card) for card in cards]


def validate_cards(cards: Sequence[Mapping[str, object]]) -> None:
    required = {"repo_key", "namespace", "title", "summary", "aliases", "tags", "public", "embedding_contract"}
    for card in cards:
        missing = required - set(card)
        if missing:
            raise ExperimentError(f"Card {card.get('repo_key')!r} is missing fields: {sorted(missing)}.")
        if not all(isinstance(card[field], str) and str(card[field]).strip() for field in ("repo_key", "namespace", "title", "summary")):
            raise ExperimentError("Card identity, title, and summary fields must be non-empty strings.")
        if not isinstance(card["aliases"], list) or not all(isinstance(value, str) for value in card["aliases"]):
            raise ExperimentError(f"Card {card['repo_key']!r} aliases must be strings.")
        if not isinstance(card["tags"], list) or not all(isinstance(value, str) for value in card["tags"]):
            raise ExperimentError(f"Card {card['repo_key']!r} tags must be strings.")
        if card["public"] is not True:
            raise ExperimentError(f"Card {card['repo_key']!r} is not explicitly public.")
        if card["embedding_contract"] != EXPECTED_CONTRACT:
            raise ExperimentError(f"Card {card['repo_key']!r} has an incompatible embedding contract.")
    repo_keys = [str(card["repo_key"]) for card in cards]
    namespaces = [str(card["namespace"]) for card in cards]
    if repo_keys != sorted(DATASETS):
        raise ExperimentError("Cards must be ordered by and exactly match the 13 required repository keys.")
    if len(set(repo_keys)) != len(repo_keys) or len(set(namespaces)) != len(namespaces):
        raise ExperimentError("Card repository keys and namespaces must each be unique.")
    expected_namespaces = {repo_key: value[0] for repo_key, value in DATASETS.items()}
    if {str(card["repo_key"]): str(card["namespace"]) for card in cards} != expected_namespaces:
        raise ExperimentError("Card namespaces do not exactly match the input mapping.")


def load_questions() -> list[dict[str, str]]:
    questions: list[dict[str, str]] = []
    for repo_key, (namespace, relative_path, expected_count) in DATASETS.items():
        path = REPO_ROOT / relative_path
        payload = json.loads(path.read_text(encoding="utf-8"))
        cases = payload.get("cases") if isinstance(payload, Mapping) else None
        if not isinstance(cases, list) or len(cases) != expected_count:
            raise ExperimentError(f"Dataset {relative_path} must contain exactly {expected_count} cases.")
        seen: set[str] = set()
        for case in cases:
            if not isinstance(case, Mapping):
                raise ExperimentError(f"Dataset {relative_path} contains a non-object case.")
            case_id, question = case.get("id"), case.get("question")
            if not isinstance(case_id, str) or not case_id.strip() or not isinstance(question, str) or not question.strip():
                raise ExperimentError(f"Dataset {relative_path} contains an invalid id or question.")
            if case_id in seen:
                raise ExperimentError(f"Dataset {relative_path} contains duplicate case id {case_id!r}.")
            seen.add(case_id)
            questions.append(
                {
                    "identity": f"{repo_key}:{case_id}",
                    "repo_key": repo_key,
                    "case_id": case_id,
                    "question": question,
                    "home_namespace": namespace,
                }
            )
    if len(questions) != EXPECTED_QUESTION_COUNT:
        raise ExperimentError(f"Expected exactly 90 questions, found {len(questions)}.")
    return questions


def card_text(card: Mapping[str, object]) -> str:
    """Build deterministic passage text without benchmark cases or file judgments."""
    aliases = "; ".join(str(value) for value in card["aliases"]) or "none"
    tags = "; ".join(str(value) for value in card["tags"]) or "none"
    return f"Title: {card['title']}\nSummary: {card['summary']}\nAliases: {aliases}\nTags: {tags}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def model_snapshot_path() -> Path:
    return Path.home() / ".cache" / "huggingface" / "hub" / "models--BAAI--bge-small-en-v1.5" / "snapshots" / MODEL_REVISION


def model_manifest(snapshot: Path) -> list[dict[str, object]]:
    if not snapshot.is_dir():
        raise ExperimentError(
            f"Pinned model snapshot is not cached at {snapshot}; downloads and substitutions are forbidden."
        )
    manifest: list[dict[str, object]] = []
    for path in sorted(snapshot.rglob("*")):
        resolved = path.resolve()
        if resolved.is_file():
            manifest.append(
                {
                    "path": path.relative_to(snapshot).as_posix(),
                    "sha256": sha256_file(resolved),
                    "size_bytes": resolved.stat().st_size,
                }
            )
    if not manifest:
        raise ExperimentError(f"Pinned model snapshot at {snapshot} contains no regular files.")
    return manifest


def prepare_environment(temp_dir: Path, snapshot: Path) -> None:
    for name in CREDENTIAL_ENV:
        if name in os.environ:
            del os.environ[name]
    os.environ.update(OFFLINE_ENV)
    os.environ["HF_HOME"] = str(snapshot.parents[3])
    os.environ["HUGGINGFACE_HUB_CACHE"] = str(snapshot.parents[2])
    os.environ["TMPDIR"] = str(temp_dir)
    os.environ["TMP"] = str(temp_dir)
    os.environ["TEMP"] = str(temp_dir)
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    if any(name in os.environ for name in CREDENTIAL_ENV):
        raise ExperimentError("Credential environment sanitization failed.")


def _allowed_path(path: object, roots: Sequence[Path]) -> bool:
    candidate = Path(os.fsdecode(path))
    if not candidate.is_absolute():
        candidate = Path.cwd() / candidate
    resolved = candidate.resolve(strict=False)
    return any(resolved == root or resolved.is_relative_to(root) for root in roots)


@contextmanager
def execution_guards(run_dir: Path, temp_dir: Path) -> Iterable[None]:
    """Reject sockets and filesystem mutations outside the two allowed roots."""
    roots = (run_dir.resolve(), temp_dir.resolve())
    original_connect = socket.socket.connect
    original_connect_ex = socket.socket.connect_ex
    original_create_connection = socket.create_connection
    original_getaddrinfo = socket.getaddrinfo
    original_open = builtins.open
    original_io_open = io.open
    original_os_open = os.open
    originals = {
        "replace": os.replace,
        "rename": os.rename,
        "remove": os.remove,
        "unlink": os.unlink,
        "rmdir": os.rmdir,
        "mkdir": os.mkdir,
    }

    def reject_socket(*_args: object, **_kwargs: object) -> object:
        raise ExperimentError("Network access is forbidden by the semantic-routing experiment socket guard.")

    def check_path(path: object) -> None:
        if isinstance(path, int):
            return
        if not _allowed_path(path, roots):
            raise ExperimentError(f"Write outside experiment allowlist is forbidden: {path}")

    def guarded_open(file: object, mode: str = "r", *args: object, **kwargs: object) -> object:
        if any(marker in mode for marker in ("w", "a", "x", "+")):
            check_path(file)
        return original_open(file, mode, *args, **kwargs)

    def guarded_io_open(file: object, mode: str = "r", *args: object, **kwargs: object) -> object:
        if any(marker in mode for marker in ("w", "a", "x", "+")):
            check_path(file)
        return original_io_open(file, mode, *args, **kwargs)

    def guarded_os_open(path: object, flags: int, mode: int = 0o777, *, dir_fd: int | None = None) -> int:
        write_flags = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
        if flags & write_flags:
            if dir_fd is not None:
                raise ExperimentError("Write-mode os.open with dir_fd is forbidden by the path guard.")
            check_path(path)
        return original_os_open(path, flags, mode, dir_fd=dir_fd)

    def guarded_one_path(name: str) -> Callable[..., object]:
        original = originals[name]

        def call(path: object, *args: object, **kwargs: object) -> object:
            if kwargs.get("dir_fd") is not None:
                raise ExperimentError(f"{name} with dir_fd is forbidden by the path guard.")
            check_path(path)
            return original(path, *args, **kwargs)

        return call

    def guarded_two_paths(name: str) -> Callable[..., object]:
        original = originals[name]

        def call(source: object, destination: object, *args: object, **kwargs: object) -> object:
            if kwargs.get("src_dir_fd") is not None or kwargs.get("dst_dir_fd") is not None:
                raise ExperimentError(f"{name} with dir_fd is forbidden by the path guard.")
            check_path(source)
            check_path(destination)
            return original(source, destination, *args, **kwargs)

        return call

    socket.socket.connect = reject_socket  # type: ignore[method-assign]
    socket.socket.connect_ex = reject_socket  # type: ignore[method-assign]
    socket.create_connection = reject_socket
    socket.getaddrinfo = reject_socket
    builtins.open = guarded_open
    io.open = guarded_io_open
    os.open = guarded_os_open
    os.replace = guarded_two_paths("replace")
    os.rename = guarded_two_paths("rename")
    os.remove = guarded_one_path("remove")
    os.unlink = guarded_one_path("unlink")
    os.rmdir = guarded_one_path("rmdir")
    os.mkdir = guarded_one_path("mkdir")
    try:
        yield
    finally:
        socket.socket.connect = original_connect  # type: ignore[method-assign]
        socket.socket.connect_ex = original_connect_ex  # type: ignore[method-assign]
        socket.create_connection = original_create_connection
        socket.getaddrinfo = original_getaddrinfo
        builtins.open = original_open
        io.open = original_io_open
        os.open = original_os_open
        for name, original in originals.items():
            setattr(os, name, original)


def construct_model() -> object:
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(
        MODEL_ID,
        revision=MODEL_REVISION,
        local_files_only=True,
        cache_folder=str(model_snapshot_path().parents[2]),
    )


def encode_float32(model: object, texts: Sequence[str]) -> list[list[float]]:
    vectors = model.encode(  # type: ignore[attr-defined]
        list(texts),
        batch_size=32,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    dtype = getattr(vectors, "dtype", None)
    if str(dtype) != "float32":
        raise ExperimentError(f"Expected normalized float32 model output, found dtype {dtype!s}.")
    result = [[float(value) for value in row] for row in vectors]
    if len(result) != len(texts) or any(len(row) != 384 for row in result):
        raise ExperimentError("Model returned an unexpected number or dimension of embeddings.")
    return result


def input_manifest() -> list[dict[str, object]]:
    paths = [CARD_PATH, *(REPO_ROOT / value[1] for value in DATASETS.values())]
    return [
        {
            "path": path.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256_file(path),
            "size_bytes": path.stat().st_size,
        }
        for path in paths
    ]


def build_plan(model_files: Sequence[Mapping[str, object]]) -> dict[str, object]:
    return {
        "experiment_id": "semantic-routing-representative-20260715",
        "one_shot": True,
        "purpose": "Descriptive home-namespace source-attribution over 13 public repository seed datasets.",
        "inputs": input_manifest(),
        "dataset_mapping": {
            repo_key: {"namespace": namespace, "path": path, "cases": count}
            for repo_key, (namespace, path, count) in DATASETS.items()
        },
        "question_count": EXPECTED_QUESTION_COUNT,
        "card_count": len(DATASETS),
        "model": {
            "id": MODEL_ID,
            "revision": MODEL_REVISION,
            "precision": "float32",
            "normalized": True,
            "query_prefix": QUERY_PREFIX,
            "passage_format": "Title, Summary, Aliases, and Tags labeled on separate deterministic lines.",
            "local_files_only": True,
            "snapshot_files": list(model_files),
        },
        "strategies": ["oracle", "lexical", "semantic", "hybrid_rrf"],
        "rrf_k": RRF_K,
        "route_fan_out": ROUTE_FAN_OUT,
        "controls": {
            "network_allowed": False,
            "hosted_api_allowed": False,
            "turbopuffer_allowed": False,
            "credential_environment_removed": sorted(CREDENTIAL_ENV),
            "offline_environment": OFFLINE_ENV,
            "socket_connections_rejected": True,
            "write_roots": ["experiment directory", "process-owned ephemeral temporary directory"],
            "model_cache_writable": False,
            "temporary_directory": {"path": ".semantic-routing-tmp", "ephemeral": True, "removed_after_run": True},
            "result_overwrite_requires_flag": "--replace-result",
        },
        "limits": {
            "labels": "home source only; alternative namespaces are unlabeled",
            "file_judgments_used": False,
            "cross_namespace_hits_fabricated": False,
            "downstream_retrieval_run": False,
            "precision_reported": False,
            "production_readiness_claimed": False,
        },
    }


def evaluate(
    cards: Sequence[Mapping[str, object]],
    questions: Sequence[Mapping[str, str]],
    model: object,
) -> dict[str, object]:
    card_vectors_list = encode_float32(model, [card_text(card) for card in cards])
    card_vectors = {
        str(card["repo_key"]): vector for card, vector in zip(cards, card_vectors_list, strict=True)
    }
    question_vectors = encode_float32(model, [QUERY_PREFIX + question["question"] for question in questions])
    strategy_cases: dict[str, list[dict[str, object]]] = {
        "oracle": [],
        "lexical": [],
        "semantic": [],
        "hybrid_rrf": [],
    }
    for question, vector in zip(questions, question_vectors, strict=True):
        oracle = [
            {
                "rank": 1,
                "repo_key": question["repo_key"],
                "namespace": question["home_namespace"],
                "raw_score": 1.0,
            }
        ]
        lexical = lexical_rank(question["question"], cards)
        semantic = semantic_rank(vector, cards, card_vectors)
        hybrid = hybrid_rank(lexical, semantic)
        for strategy, ranking in (
            ("oracle", oracle),
            ("lexical", lexical),
            ("semantic", semantic),
            ("hybrid_rrf", hybrid),
        ):
            strategy_cases[strategy].append(
                {
                    **question,
                    "rankings": ranking,
                    "home_namespace_rank": home_rank(ranking, question["home_namespace"]),
                }
            )
    return {
        strategy: {"cases": cases, "metrics": metrics_for_cases(cases)}
        for strategy, cases in strategy_cases.items()
    }


def render_report(result: Mapping[str, object]) -> str:
    strategies = result["strategies"]
    assert isinstance(strategies, Mapping)
    lines = [
        "# Representative Semantic Namespace Routing Experiment",
        "",
        "## Result",
        "",
        "This run measures whether each assistant-drafted public-project question routes to its dataset's home namespace. It is descriptive source-attribution evidence, not product ground truth.",
        "",
        "| Strategy | MRR | Recall@1 | Recall@3 | Recall@5 | Unranked | Evaluated |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for strategy in ("oracle", "lexical", "semantic", "hybrid_rrf"):
        payload = strategies[strategy]
        assert isinstance(payload, Mapping)
        metrics = payload["metrics"]
        assert isinstance(metrics, Mapping)
        aggregate = metrics["aggregate"]
        assert isinstance(aggregate, Mapping)
        lines.append(
            f"| {strategy} | {float(aggregate['mrr']):.6f} | {float(aggregate['recall_at_1']):.6f} | "
            f"{float(aggregate['recall_at_3']):.6f} | {float(aggregate['recall_at_5']):.6f} | "
            f"{aggregate['unranked_count']} | {aggregate['evaluated_count']} |"
        )
    lines.extend(["", "Route fan-out is fixed at five for reporting; no promotion threshold is defined.", ""])
    for strategy in ("oracle", "lexical", "semantic", "hybrid_rrf"):
        payload = strategies[strategy]
        metrics = payload["metrics"]  # type: ignore[index]
        per_repository = metrics["per_repository"]  # type: ignore[index]
        lines.extend(
            [
                f"## {strategy} per repository",
                "",
                "| Repository | MRR | R@1 | R@3 | R@5 | Unranked | Evaluated |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for repo_key in DATASETS:
            item = per_repository[repo_key]
            lines.append(
                f"| {repo_key} | {item['mrr']:.6f} | {item['recall_at_1']:.6f} | {item['recall_at_3']:.6f} | "
                f"{item['recall_at_5']:.6f} | {item['unranked_count']} | {item['evaluated_count']} |"
            )
        lines.append("")
    lines.extend(
        [
            "## Safety and provenance",
            "",
            f"- Model: `{MODEL_ID}` at immutable revision `{MODEL_REVISION}`, loaded with `local_files_only=True`.",
            "- Socket connection calls were blocked, credential variables were removed, offline controls were set, and writes were limited to this run directory plus an ephemeral process-owned temporary directory.",
            "- No Turbopuffer, hosted API, model download, production-state mutation, or downstream cross-namespace retrieval ran.",
            "- The model snapshot SHA-256 manifest and immutable input hashes are recorded in `plan.json`.",
            "",
            "## Limitations",
            "",
            "- The 90 questions and their original file judgments were assistant-drafted and are not human-approved product ground truth.",
            "- Dataset membership supplies only the home-source label. Other namespaces are unlabeled, not known negatives, so route precision is intentionally not reported.",
            "- The run does not measure answer quality, same-query cross-namespace hit quality, ACL behavior, production latency, or production readiness.",
            "- Cached home-namespace hits were not used and absent cross-namespace hits were not fabricated.",
            "- Independent review must inspect benchmark provenance and materially ambiguous home-source questions before ticket closure.",
            "",
        ]
    )
    return "\n".join(lines)


def write_json(path: Path, payload: Mapping[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def refuse_result_overwrite(path: Path, *, replace: bool) -> None:
    if path.exists() and not replace:
        raise ExperimentError(
            f"Refusing to overwrite existing final result {path}; pass --replace-result for an explicit experiment-local replacement."
        )


def run(*, replace_result: bool = False) -> dict[str, object]:
    refuse_result_overwrite(RESULT_PATH, replace=replace_result)
    cards = load_cards()
    validate_cards(cards)
    questions = load_questions()
    snapshot = model_snapshot_path()
    if TEMP_DIR.exists():
        raise ExperimentError(f"Ephemeral run directory already exists and will not be reused: {TEMP_DIR}")
    TEMP_DIR.mkdir()
    started = time.monotonic()
    try:
        prepare_environment(TEMP_DIR, snapshot)
        with execution_guards(RUN_DIR, TEMP_DIR):
            manifest = model_manifest(snapshot)
            model = construct_model()
            plan = build_plan(manifest)
            write_json(PLAN_PATH, plan)
            strategies = evaluate(cards, questions, model)
            result = {
                "experiment_id": "semantic-routing-representative-20260715",
                "status": "completed",
                "model": {"id": MODEL_ID, "revision": MODEL_REVISION},
                "question_count": len(questions),
                "card_count": len(cards),
                "route_fan_out": ROUTE_FAN_OUT,
                "rrf_k": RRF_K,
                "strategies": strategies,
                "runtime": {"duration_seconds": time.monotonic() - started},
                "safety": {
                    "network_calls": 0,
                    "turbopuffer_calls": 0,
                    "hosted_api_calls": 0,
                    "credentials_used": False,
                    "model_downloads": 0,
                    "external_writes": 0,
                    "model_cache_writes": 0,
                    "cross_namespace_hits_fabricated": False,
                },
            }
            write_json(RESULT_PATH, result)
            REPORT_PATH.write_text(render_report(result), encoding="utf-8")
            return result
    finally:
        if TEMP_DIR.exists():
            shutil.rmtree(TEMP_DIR)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--replace-result",
        action="store_true",
        help="Explicitly replace this experiment's existing result, plan, and report artifacts.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = run(replace_result=args.replace_result)
    except (ExperimentError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"semantic routing experiment failed: {exc}", file=sys.stderr)
        return 2
    aggregate = result["strategies"]
    print(json.dumps({name: payload["metrics"]["aggregate"] for name, payload in aggregate.items()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
