"""Fish Audio Drama-3 through SGLang Omni's streaming speech endpoint."""

from __future__ import annotations

import base64
import os
from collections.abc import Callable, Iterator
from math import isfinite
from pathlib import Path
from threading import Event
from typing import Any

import numpy as np
import soxr

from ai_speech_agents_framework.pipeline.cancel_scope import CancelScope
from ai_speech_agents_framework.pipeline.speculative_turns import SpeculativeTurnTracker
from ai_speech_agents_framework.TTS.openai_compatible_handler import PIPELINE_SAMPLE_RATE, OpenAICompatibleTTSHandler


class Drama3TTSHandler(OpenAICompatibleTTSHandler):
    pass  # TODO: implement
    def setup(  # type: ignore[override]
        pass  # TODO: implement

    def _request_payload(
        pass  # TODO: implement

    def _resample_to_blocks(
        pass  # TODO: implement

        def converted_chunks() -> Iterator[np.ndarray]:
            pass  # TODO: implement

