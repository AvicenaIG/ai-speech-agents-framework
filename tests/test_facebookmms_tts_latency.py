from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest
import torch

from ai_speech_agents_framework.pipeline.cancel_scope import CancelScope
from ai_speech_agents_framework.pipeline.messages import TTSInput
from ai_speech_agents_framework.pipeline.turn_latency import TurnLatencyStore
from ai_speech_agents_framework.TTS import facebookmms_handler
from ai_speech_agents_framework.TTS.facebookmms_handler import FacebookMMSTTSHandler


def _waveform(samples: int = 16000) -> torch.Tensor:
    pass  # TODO: implement


def _handler(*, stream: bool = True, waveform: torch.Tensor | None = None) -> FacebookMMSTTSHandler:
    pass  # TODO: implement


@pytest.fixture(autouse=True)
def _quiet_console(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


def test_records_ttfa_before_resample_and_e2e_on_first_yield(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement

    def slow_resample(chunk, *, orig_sr, target_sr):
        pass  # TODO: implement


    def generate(_text: str) -> torch.Tensor:
        pass  # TODO: implement





def test_preserves_first_audio_across_later_segments(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement

    def first_generate(_text: str) -> torch.Tensor:
        pass  # TODO: implement




    def later_generate(_text: str) -> torch.Tensor:
        pass  # TODO: implement




def test_language_reload_is_excluded_from_ttfa(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


    def reload(_language_code: str, _model_name: str | None = None) -> None:
        pass  # TODO: implement

    def generate(_text: str) -> torch.Tensor:
        pass  # TODO: implement





def test_empty_audio_leaves_latency_unset(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement




@pytest.mark.parametrize("device_type", ["cpu", "cuda", "mps", "xpu", "npu"])
@pytest.mark.parametrize("cancel_during_wait", [False, True])
def test_ttfa_waits_for_waveform_readiness_before_cpu_copy(
    pass  # TODO: implement
) -> None:

    def synchronize() -> None:
        pass  # TODO: implement

    def current_stream(actual_device):
        pass  # TODO: implement


    class DeferredWaveform:
        pass  # TODO: implement
        def __init__(self):
            pass  # TODO: implement

        def numel(self):
            pass  # TODO: implement

        def cpu(self):
            pass  # TODO: implement

    def resample(chunk, **kwargs):
        pass  # TODO: implement


    def generate(_text):
        pass  # TODO: implement




@pytest.mark.parametrize("cancel_at", ["generation", "resample", "after_first", "discard"])
def test_cancelled_or_discarded_audio_cannot_record_another_response(
    pass  # TODO: implement
) -> None:

    def generate(_text):
        pass  # TODO: implement

    def resample(chunk, **kwargs):
        pass  # TODO: implement

