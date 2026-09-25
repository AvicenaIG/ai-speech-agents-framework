import sys
from unittest.mock import MagicMock

import numpy as np
import pytest

from ai_speech_agents_framework.pipeline.messages import PartialTranscription, Transcription, VADAudio
from ai_speech_agents_framework.STT import paraformer_handler
from ai_speech_agents_framework.STT.paraformer_handler import ParaformerSTTHandler


class _FakeParaformerModel:
    pass  # TODO: implement
    def generate(self, audio):
        pass  # TODO: implement


def _handler(*, language: str = "zh", device: str = "cpu"):
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_setup_extracts_language_from_model_name(monkeypatch, model_name, expected):
    pass  # TODO: implement




def test_progressive_paraformer_transcription_is_partial(monkeypatch):
    pass  # TODO: implement




def test_final_paraformer_transcription_is_final(monkeypatch):
    pass  # TODO: implement




def test_final_paraformer_transcription_uses_english_checkpoint_language(monkeypatch):
    pass  # TODO: implement




def test_paraformer_skips_mps_cache_clear_on_cpu(monkeypatch):
    pass  # TODO: implement

    def fail_if_called():
        pass  # TODO: implement



