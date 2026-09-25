"""End-to-end coverage for the ``--enable_lang_prompt`` language instruction.

When enabled, the resolved language name is passed into the system-prompt
builders (``build_voice_system_prompt`` / ``build_text_system_prompt``) for the
current turn. It never adds a second consecutive user message, which would break
strict chat templates (e.g. Ministral).

The OpenAI client is faked, so this runs with no network and no GPU.
"""

from __future__ import annotations

import queue
import threading
from types import SimpleNamespace

from openai.types.realtime.realtime_session_create_request import RealtimeSessionCreateRequest

import ai_speech_agents_framework.LLM.base_openai_compatible_language_model as base_mod
from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.LLM.chat import Chat, make_user_message
from ai_speech_agents_framework.LLM.chat_completions_language_model import ChatCompletionsApiModelHandler
from ai_speech_agents_framework.pipeline.messages import GenerateResponseRequest

LANGUAGE_INSTRUCTION_PREFIX = "Please reply to my message in "


class _FakeCompletions:
    pass  # TODO: implement
    def __init__(self):
        pass  # TODO: implement

    def create(self, **kwargs):
        pass  # TODO: implement


class _FakeClient:
    pass  # TODO: implement
    def __init__(self, *a, **k):
        pass  # TODO: implement

    def with_options(self, **kwargs):
        pass  # TODO: implement


def _make_handler(*, enable_lang_prompt):
    pass  # TODO: implement


def _sent_system_messages(handler, language_code, *, enable_lang_prompt=True):
    pass  # TODO: implement




def test_swedish_gets_a_language_instruction():
    pass  # TODO: implement




def test_no_instruction_when_the_flag_is_disabled():
    pass  # TODO: implement




def test_unknown_language_code_still_emits_no_instruction():
    pass  # TODO: implement


