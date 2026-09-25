"""Local language-model history ordering under overlapping speech.

Covers the non-interrupting overlap described in issue #454: a second
transcription can reach ``Chat`` while the first response is still being
generated, and the first response must still land in its own turn.
"""

from __future__ import annotations

from collections.abc import Iterator
from queue import Queue
from threading import Event, Thread
from typing import Any, Optional

import pytest
from openai.types.realtime import RealtimeSessionCreateRequest
from openai.types.realtime.realtime_conversation_item_user_message import Content as UserContent
from openai.types.realtime.realtime_response_create_params import RealtimeResponseCreateParams
from openai.types.responses import ResponseFunctionToolCall

from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.api.openai_realtime.service import RealtimeService
from ai_speech_agents_framework.LLM.chat import Chat, make_assistant_message, make_user_audio_message, make_user_message
from ai_speech_agents_framework.LLM.language_model import BaseLanguageModelHandler, StreamContext
from ai_speech_agents_framework.LLM.lm_output_processor import LMOutputProcessor
from ai_speech_agents_framework.pipeline.events import AssistantOutputEvent, AssistantResponseDoneEvent
from ai_speech_agents_framework.pipeline.history import ResponseHistory
from ai_speech_agents_framework.pipeline.messages import (
)
from ai_speech_agents_framework.pipeline.speculative_turns import SpeculativeTurnTracker
from tests.llm_history import drive_llm


class _OverlappingSpeechHandler(BaseLanguageModelHandler):
    pass  # TODO: implement

    def _load_model(
        pass  # TODO: implement

    def _generate(
        pass  # TODO: implement


def _make_handler() -> _OverlappingSpeechHandler:
    pass  # TODO: implement


def test_local_response_history_precedes_speech_that_arrived_during_generation():
    pass  # TODO: implement




@pytest.mark.parametrize("outcome", ["superseded", "completed", "cancelled"])
def test_history_acceptance_uses_global_order_and_keeps_committed_work(outcome):
    pass  # TODO: implement


@pytest.mark.parametrize("cleanup_fails", [False, True])
def test_audio_input_commits_only_after_history_cleanup(monkeypatch, cleanup_fails):
    pass  # TODO: implement

        def fail_cleanup(compactor=None):
            pass  # TODO: implement




def test_next_worker_request_reads_accepted_history_before_audio_finishes(monkeypatch):
    pass  # TODO: implement

    def generate(chat, language_code, gen, ctx, runtime_config, response):
        pass  # TODO: implement

