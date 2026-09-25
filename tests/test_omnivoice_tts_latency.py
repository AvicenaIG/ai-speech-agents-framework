from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest

from ai_speech_agents_framework.pipeline.cancel_scope import CancelScope
from ai_speech_agents_framework.pipeline.messages import TTSInput
from ai_speech_agents_framework.pipeline.turn_latency import TurnLatencyStore
from ai_speech_agents_framework.TTS import omnivoice_handler as omnivoice_module
from ai_speech_agents_framework.TTS.omnivoice_handler import OmniVoiceTTSHandler


def _waveform(samples: int = 768) -> list[np.ndarray]:
    pass  # TODO: implement


def _handler(*, samples: int = 768, cancel_scope: CancelScope | None = None) -> OmniVoiceTTSHandler:
    pass  # TODO: implement


@pytest.fixture(autouse=True)
def _quiet_console(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


def test_records_ttfa_before_resample_and_e2e_on_first_yield(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement

    def slow_resample(chunk, up, down):
        pass  # TODO: implement



    def generate(**_kwargs):
        pass  # TODO: implement





def test_preserves_first_audio_across_later_segments(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement

    def first_generate(**_kwargs):
        pass  # TODO: implement




    def later_generate(**_kwargs):
        pass  # TODO: implement




@pytest.mark.parametrize("audios", [[], [np.array([], dtype=np.float32)]])
def test_empty_audio_leaves_latency_unset(monkeypatch: pytest.MonkeyPatch, audios: list[np.ndarray]) -> None:
    pass  # TODO: implement




@pytest.mark.parametrize("cancel_at", ["generation", "after_first", "discard"])
def test_cancelled_or_discarded_audio_cannot_record_another_response(
    pass  # TODO: implement
) -> None:

    def generate(**_kwargs):
        pass  # TODO: implement

