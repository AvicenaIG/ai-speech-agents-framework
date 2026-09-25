"""Handlers must not configure the root logger or write to stdout via print().

Library modules that call ``logging.basicConfig`` at import time reconfigure the
host application's logging (level, format, handlers). Secondary STT/TTS handlers
historically did this, and used ``print`` for setup/cleanup messages. These tests
pin the hygiene contract used by the rest of the package: module loggers only,
no import-time root configuration.
"""

from __future__ import annotations

import ast
import importlib
import logging
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

_SRC_ROOT = Path(__file__).resolve().parents[1] / "src"

_HANDLERS_WITH_FORMER_BASIC_CONFIG = [
]

_HANDLERS_WITH_FORMER_PRINT = [
]


def _module_source(relative_path: str) -> str:
    pass  # TODO: implement


def _calls_named(tree: ast.AST, qualname: tuple[str, ...]) -> list[ast.Call]:
    pass  # TODO: implement
        func = node.func
            pass  # TODO: implement
            func = func.value
                pass  # TODO: implement


def _top_level_print_calls(tree: ast.AST) -> list[ast.Call]:
    pass  # TODO: implement


@pytest.mark.parametrize("relative_path", _HANDLERS_WITH_FORMER_BASIC_CONFIG)
def test_handler_source_has_no_logging_basic_config(relative_path: str) -> None:
    pass  # TODO: implement


@pytest.mark.parametrize("relative_path", _HANDLERS_WITH_FORMER_PRINT)
def test_handler_source_has_no_print_calls(relative_path: str) -> None:
    pass  # TODO: implement


def test_paraformer_import_does_not_call_basic_config(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement




def test_facebookmms_import_does_not_call_basic_config(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement




def test_chattts_import_does_not_call_basic_config(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement




def test_paraformer_setup_logs_model_name_instead_of_printing(
    pass  # TODO: implement
) -> None:





def test_faster_whisper_cleanup_logs_instead_of_printing(
    pass  # TODO: implement
) -> None:



