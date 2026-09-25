from __future__ import annotations

import sys
from types import SimpleNamespace
from typing import Any

import numpy as np
import pytest

from ai_speech_agents_framework.pipeline.messages import TTSInput
from ai_speech_agents_framework.pipeline.turn_latency import TurnLatencyStore


class _FakeChat:
    pass  # TODO: implement
    class InferCodeParams:
        pass  # TODO: implement
        def __init__(self, **_kwargs: Any) -> None:
            pass  # TODO: implement


def _tone(samples: int = 24000) -> np.ndarray:
    pass  # TODO: implement


@pytest.fixture
def chattts_modules(monkeypatch: pytest.MonkeyPatch):
    pass  # TODO: implement



def _handler(ChatTTSHandler, *, stream: bool, chunks: list[Any]):
    pass  # TODO: implement


def test_stream_records_ttfa_before_resample_and_e2e_on_first_yield(monkeypatch, chattts_modules):
    pass  # TODO: implement

    def slow_resample(chunk, *, orig_sr, target_sr):
        pass  # TODO: implement


    def infer(*_a, **_k):
        pass  # TODO: implement





def test_stream_preserves_first_audio_across_later_segments(monkeypatch, chattts_modules):
    pass  # TODO: implement

    def first_infer(*_a, **_k):
        pass  # TODO: implement




    def later_infer(*_a, **_k):
        pass  # TODO: implement




def test_non_stream_records_ttfa_before_resample(monkeypatch, chattts_modules):
    pass  # TODO: implement

    def slow_resample(chunk, *, orig_sr, target_sr):
        pass  # TODO: implement


    def infer(*_a, **_k):
        pass  # TODO: implement





def test_empty_provider_chunk_leaves_latency_unset(monkeypatch, chattts_modules):
    pass  # TODO: implement


