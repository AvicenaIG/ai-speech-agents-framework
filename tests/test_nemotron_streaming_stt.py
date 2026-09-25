from __future__ import annotations

from typing import Any

import numpy as np
import pytest

from ai_speech_agents_framework.LLM.utils import language_name_for_prompt
from ai_speech_agents_framework.pipeline.messages import Transcription, VADAudio
from ai_speech_agents_framework.s2s_pipeline import parse_arguments
from ai_speech_agents_framework.STT import nemo_asr_handler
from ai_speech_agents_framework.STT.nemo_asr_handler import NemoASRSTTHandler
from tests.test_nemo_asr_handler import _install_fake_nemo


@pytest.fixture(autouse=True)
def _quiet_console(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


def _vad_audio(*, turn_id: str = "turn_1") -> VADAudio:
    pass  # TODO: implement


def test_cli_nemotron_streaming_defaults() -> None:
    pass  # TODO: implement



def test_cli_nemotron_streaming_model_name_override() -> None:
    pass  # TODO: implement



def test_multilingual_nemotron_uses_detected_language_per_utterance(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement

    class FakeASRModel:
        pass  # TODO: implement
        def from_pretrained(cls, *args: Any, **kwargs: Any) -> FakeASRModel:
            pass  # TODO: implement

        def to(self, device: str) -> FakeASRModel:
            pass  # TODO: implement

        def set_inference_prompt(self, lang: str) -> None:
            pass  # TODO: implement

        def transcribe(self, audio: Any, **kwargs: Any) -> list[str]:
            pass  # TODO: implement





def test_english_nemotron_keeps_configured_language(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement

    class FakeASRModel:
        pass  # TODO: implement
        def from_pretrained(cls, *args: Any, **kwargs: Any) -> FakeASRModel:
            pass  # TODO: implement

        def to(self, device: str) -> FakeASRModel:
            pass  # TODO: implement

        def transcribe(self, audio: Any, **kwargs: Any) -> list[str]:
            pass  # TODO: implement



