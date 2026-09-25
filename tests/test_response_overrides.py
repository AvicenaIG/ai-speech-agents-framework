from __future__ import annotations

from collections.abc import Iterator
from types import SimpleNamespace
from typing import Any, Optional

from openai.types.realtime import RealtimeSessionCreateRequest
from openai.types.realtime.realtime_response_create_params import RealtimeResponseCreateParams

from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.LLM.chat import Chat, make_system_message, make_user_message
from ai_speech_agents_framework.LLM.language_model import BaseLanguageModelHandler, StreamContext
from ai_speech_agents_framework.pipeline.messages import GenerateResponseRequest, LLMResponseChunk


class _RecordingLocalHandler(BaseLanguageModelHandler):
    pass  # TODO: implement
    def _load_model(
        pass  # TODO: implement

    def _generate(
        pass  # TODO: implement


def test_local_backend_preserves_explicitly_empty_response_overrides():
    pass  # TODO: implement




def test_local_backend_preserves_response_creation_language():
    pass  # TODO: implement




def test_local_backend_keeps_injected_context_with_session_instructions():
    pass  # TODO: implement

