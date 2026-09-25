"""Parakeet reports detected languages with -auto and ignores configured preferences."""

from __future__ import annotations

import importlib
import sys
import types

import numpy as np
import pytest

from ai_speech_agents_framework.pipeline.messages import VADAudio


class FakeNanoParakeetModel:
    pass  # TODO: implement

    def __init__(self, text="Hello there"):
        pass  # TODO: implement

    def transcribe(self, audio):
        pass  # TODO: implement


@pytest.fixture
def handler_module(monkeypatch):
    pass  # TODO: implement





def make_handler(handler_module, *, language="en", model_text="Hello there"):
    pass  # TODO: implement


def test_configured_language_is_not_reported_when_detection_fails(handler_module, monkeypatch):
    pass  # TODO: implement




def test_detected_language_is_reported_with_the_auto_suffix(handler_module, monkeypatch):
    pass  # TODO: implement




def test_configured_language_does_not_override_detection(handler_module, monkeypatch):
    pass  # TODO: implement




@pytest.mark.parametrize("value", ["auto", "AUTO", " auto ", "", "  ", "none", "NONE", "null", "NULL", None, 123])
def test_auto_sentinels_are_normalized_to_none(handler_module, value):
    pass  # TODO: implement



def test_detection_failure_does_not_report_a_previous_turn_language(handler_module, monkeypatch):
    pass  # TODO: implement




def test_last_language_updates_from_tagged_detected_code(handler_module, monkeypatch):
    pass  # TODO: implement




def test_configured_language_whitespace_is_stripped(handler_module):
    pass  # TODO: implement

