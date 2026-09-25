"""Tests for MLXAudioWhisperSTTHandler's MLX lock usage and language resolution.

`utils/mlx_lock.py` documents the global lock as mandatory for every MLX handler: MLX
models share one Metal command queue, so concurrent inference from the STT/LLM/TTS threads
aborts the process with


This handler was the only MLX inference path that did not acquire it. These tests pin the
lock down (including that it is actually *held* while `generate()` runs, not merely
imported) and cover the language-resolution edge cases around it. No MLX or mlx-audio
install is needed -- the model is faked.
"""

from __future__ import annotations

import sys
import threading
import types

import numpy as np
import pytest
from openai.types.realtime import RealtimeSessionCreateRequest

from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.pipeline.messages import VADAudio
from ai_speech_agents_framework.STT.mlx_audio_whisper_handler import MLXAudioWhisperSTTHandler
from ai_speech_agents_framework.utils import mlx_lock


class FakeResult:
    pass  # TODO: implement
    def __init__(self, text: str, language=None) -> None:
        pass  # TODO: implement


class FakeModel:
    pass  # TODO: implement

    def __init__(self, result) -> None:
        pass  # TODO: implement

    def generate(self, audio, verbose=False, **gen_kwargs):
        pass  # TODO: implement


def _lock_held_by_other_thread() -> bool:
    pass  # TODO: implement

    def probe():
        pass  # TODO: implement



def make_handler(*, start_language, result, last_language=...):
    pass  # TODO: implement


def vad_audio(runtime_config=None):
    pass  # TODO: implement


def run(handler):
    pass  # TODO: implement


# --- the MLX lock ------------------------------------------------------------------------


def test_process_holds_the_global_mlx_lock_during_generate():
    pass  # TODO: implement




def test_warmup_holds_the_global_mlx_lock_during_generate():
    pass  # TODO: implement




def test_mlx_lock_is_released_after_process():
    pass  # TODO: implement




def test_mlx_lock_is_released_when_inference_raises():
    pass  # TODO: implement




def test_mlx_lock_is_released_when_warmup_raises():
    pass  # TODO: implement




def test_concurrent_process_calls_are_serialized():
    pass  # TODO: implement

    class OverlapDetectingModel:
        pass  # TODO: implement
        def generate(self, audio, verbose=False, **gen_kwargs):
            pass  # TODO: implement





# --- language resolution -----------------------------------------------------------------


@pytest.mark.parametrize(
)
def test_setup_does_not_store_auto_as_last_language(monkeypatch, language, expected_last_language):
    pass  # TODO: implement





def test_auto_language_reports_the_detected_language():
    pass  # TODO: implement



def test_forced_language_is_authoritative_and_passed_to_generate():
    pass  # TODO: implement




def test_session_language_overrides_setup_without_mutating_it():
    pass  # TODO: implement




def test_session_auto_clears_setup_forced_language():
    pass  # TODO: implement




def test_missing_language_attribute_falls_back_without_warning_noise():
    pass  # TODO: implement



def test_none_language_attribute_is_treated_as_absent(caplog):
    pass  # TODO: implement




def test_unsupported_detected_language_falls_back_to_last_language():
    pass  # TODO: implement



def test_unsupported_detected_language_defaults_to_english_without_fallback():
    pass  # TODO: implement



@pytest.mark.parametrize("start_language", ["auto", None, "de"])
def test_language_code_is_always_a_string(start_language):
    pass  # TODO: implement

