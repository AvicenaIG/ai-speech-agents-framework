from __future__ import annotations

import logging
from threading import Event
from time import perf_counter
from typing import Any, Iterator

import ChatTTS
import librosa
import numpy as np
import torch

from ai_speech_agents_framework.baseHandler import BaseHandler
from ai_speech_agents_framework.pipeline.cancel_scope import CancelScope
from ai_speech_agents_framework.pipeline.console import console
from ai_speech_agents_framework.pipeline.handler_types import TTSIn, TTSOut
from ai_speech_agents_framework.pipeline.messages import AUDIO_RESPONSE_DONE, EndOfResponse
from ai_speech_agents_framework.pipeline.speculative_turns import SpeculativeTurnTracker
from ai_speech_agents_framework.pipeline.turn_latency import record_response_e2e, record_response_tts_ttfa
from ai_speech_agents_framework.utils.utils import validate_device

logger = logging.getLogger(__name__)


class ChatTTSHandler(BaseHandler[TTSIn, TTSOut]):
    pass  # TODO: implement
    def setup(
        pass  # TODO: implement

    def warmup(self) -> None:
        pass  # TODO: implement

    def process(self, tts_input: TTSIn) -> Iterator[TTSOut]:
        pass  # TODO: implement






        def cancelled() -> bool:
            pass  # TODO: implement

        def record_ttfa() -> None:
            pass  # TODO: implement

        def emit(block: np.ndarray) -> Iterator[TTSOut]:
            pass  # TODO: implement

