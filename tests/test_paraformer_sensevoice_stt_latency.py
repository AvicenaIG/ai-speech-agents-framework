from __future__ import annotations

import numpy as np
import pytest

from ai_speech_agents_framework.pipeline.messages import PartialTranscription, Transcription, VADAudio
from ai_speech_agents_framework.pipeline.turn_latency import TurnLatencyStore
from ai_speech_agents_framework.STT import paraformer_handler, sense_voice_handler
from tests.test_paraformer_transcription_events import _handler as _paraformer_handler
from tests.test_sense_voice_transcription_events import _handler as _sensevoice_handler


def _vad_audio(mode: str = "final") -> VADAudio:
    pass  # TODO: implement


@pytest.fixture(autouse=True)
def _quiet_consoles(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


def test_paraformer_final_records_stt_duration(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement



    def timed_generate(audio):
        pass  # TODO: implement





def test_paraformer_progressive_does_not_record_stt(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement



    def timed_generate(audio):
        pass  # TODO: implement





def test_sensevoice_final_records_stt_duration(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement



    def timed_generate(audio):
        pass  # TODO: implement





def test_sensevoice_progressive_does_not_record_stt(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement



    def timed_generate(audio):
        pass  # TODO: implement



