"""``--language AUTO`` must behave like ``--language auto``.

Handlers compare against the literal ``"auto"`` to decide whether the user asked for
detection. Qwen3-ASR and faster-whisper normalize with ``.strip().lower()`` first; the
others did not, so a different spelling was treated as a language *name* and forwarded to
the model. On the transformers Whisper backend that is a hard failure on the first turn:


It also defeated the session reset added in #556, which restores ``start_language`` unless
it is the sentinel.
"""

from __future__ import annotations

import importlib
import sys
import types
from contextlib import ExitStack
from unittest import mock

import pytest

from ai_speech_agents_framework.STT.base_stt_handler import BaseSTTHandler

# Spellings a user can reasonably type for the same intent.
AUTO_SPELLINGS = ["auto", "AUTO", "Auto", " auto ", "\tAuto\n"]

_HANDLERS = [
]

_STUBS = {
}


def _load(module_name: str, class_name: str):
    pass  # TODO: implement


def _setup_handler(module_name: str, class_name: str, language: str):
    pass  # TODO: implement






# --- the canonicalizer --------------------------------------------------------------------


@pytest.mark.parametrize("spelling", AUTO_SPELLINGS)
def test_auto_spellings_canonicalize(spelling):
    pass  # TODO: implement


@pytest.mark.parametrize("value", ["de", "en", "yue", "fil"])
def test_real_codes_pass_through_untouched(value):
    pass  # TODO: implement


@pytest.mark.parametrize("value", [None, "", "  "])
def test_empty_values_pass_through(value):
    pass  # TODO: implement


def test_non_strings_pass_through():
    pass  # TODO: implement


def test_a_code_merely_containing_auto_is_not_the_sentinel():
    pass  # TODO: implement


# --- production setup treats every spelling as detection ----------------------------------


@pytest.mark.parametrize("spelling", AUTO_SPELLINGS)
@pytest.mark.parametrize(("module_name", "class_name"), _HANDLERS)
def test_setup_treats_every_auto_spelling_as_detection(module_name, class_name, spelling):
    pass  # TODO: implement





@pytest.mark.parametrize(("module_name", "class_name"), _HANDLERS)
def test_setup_preserves_a_real_language(module_name, class_name):
    pass  # TODO: implement


