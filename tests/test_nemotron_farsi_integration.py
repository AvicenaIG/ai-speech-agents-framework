"""Opt-in real-model test. Set FARSI_ASR_TEST_AUDIO to a Persian audio file.

Run with the nemo extra installed. FARSI_ASR_TEST_MODEL can point to a local
.nemo checkpoint; otherwise the checkpoint downloads from AvicenaIG.
"""

from __future__ import annotations

import os

import numpy as np
import pytest

from ai_speech_agents_framework.backend_registry import create_backend_handler
from ai_speech_agents_framework.pipeline.messages import PartialTranscription, Transcription, VADAudio
from ai_speech_agents_framework.s2s_pipeline import parse_arguments
from ai_speech_agents_framework.STT.nemo_asr_handler import FARSI_MODEL, SAMPLE_RATE
from tests.test_nemo_asr_handler import _context


@pytest.mark.skipif(
)
def test_real_farsi_checkpoint_through_backend_factory(monkeypatch):
    pass  # TODO: implement


    def final():
        pass  # TODO: implement

