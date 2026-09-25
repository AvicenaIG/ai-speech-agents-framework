from contextlib import nullcontext
from threading import Event
from types import SimpleNamespace

import pytest
from openai.types.realtime import RealtimeSessionCreateRequest

import ai_speech_agents_framework.LLM.language_model as language_model
from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.LLM.chat import Chat, make_user_message
from ai_speech_agents_framework.LLM.language_model import LanguageModelHandler
from ai_speech_agents_framework.pipeline.messages import GenerateResponseRequest, LLMResponseChunk
from ai_speech_agents_framework.pipeline.turn_latency import TurnLatencyStore


@pytest.mark.parametrize("tail", [". How are you?", ""])
def test_local_ttft_precedes_sentence_batching_and_trailing_reply(monkeypatch, tail):
    pass  # TODO: implement

    def tokens(*args, **kwargs):
        pass  # TODO: implement



