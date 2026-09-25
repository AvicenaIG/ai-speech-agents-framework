from __future__ import annotations

import pytest

from ai_speech_agents_framework.pipeline.messages import PartialTranscription, Transcription
from ai_speech_agents_framework.pipeline.turn_latency import TurnLatencyStore
from ai_speech_agents_framework.STT import nemo_asr_handler
from tests.test_nemo_asr_handler import _handler, _vad_audio


@pytest.fixture(autouse=True)
def _quiet_console(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


def test_final_transcription_records_stt_duration(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement



    def timed_transcribe(audio):
        pass  # TODO: implement





def test_progressive_transcription_does_not_record_stt(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement



    def timed_transcribe(audio):
        pass  # TODO: implement





def test_farsi_final_path_records_stt_duration(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


    def fake_farsi(_audio):
        pass  # TODO: implement



