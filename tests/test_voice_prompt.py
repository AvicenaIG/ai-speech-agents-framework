import json
from threading import Event
from types import MethodType, SimpleNamespace

from openai.types.realtime.conversation_item import (
)
from openai.types.realtime.realtime_response_create_params import RealtimeResponseCreateParams
from openai.types.responses import ResponseFunctionToolCall

from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.LLM.chat import Chat, make_user_message
from ai_speech_agents_framework.LLM.language_model import LanguageModelHandler, StreamContext
from ai_speech_agents_framework.LLM.tool_call.function_tool import FunctionTool
from ai_speech_agents_framework.LLM.tool_call.tool_prompt import END_CODE, ENTER_CODE, build_block_regex, build_tool_system_prompt
from ai_speech_agents_framework.LLM.voice_prompt import VOICE_SYSTEM_PROMPT, build_voice_system_prompt
from ai_speech_agents_framework.pipeline.messages import (
)
from tests.llm_history import drive_llm


def _tool(name="dance"):
    pass  # TODO: implement


def _stream_context(*tool_names, sentence_batch=None):
    pass  # TODO: implement


def _tool_call(name):
    pass  # TODO: implement


def test_voice_prompt_is_short_and_keeps_persona_in_session_prompt():
    pass  # TODO: implement



def test_voice_prompt_can_include_language_hint():
    pass  # TODO: implement



def test_voice_prompt_makes_speech_the_default_and_handles_noisy_stt():
    pass  # TODO: implement



def test_voice_prompt_requests_one_lead_in_and_silent_follow_up_tools():
    pass  # TODO: implement



def test_local_tool_prompt_preserves_multiple_tool_call_order():
    pass  # TODO: implement



def test_local_tool_prompt_leaves_voice_choreography_to_voice_prompt():
    pass  # TODO: implement



def test_local_tool_parser_flushes_lead_in_before_tool_even_with_large_sentence_batch():
    pass  # TODO: implement




def test_local_tool_parser_flushes_pending_batch_before_tool_with_empty_before_text():
    pass  # TODO: implement




def test_local_tool_parser_preserves_repeated_tool_blocks(monkeypatch):
    pass  # TODO: implement




def test_local_tool_parser_preserves_interleaved_text_and_tool_calls(monkeypatch):
    pass  # TODO: implement




def test_local_markdown_cleanup_does_not_modify_tool_block(monkeypatch):
    pass  # TODO: implement




def test_local_text_only_with_tools_preserves_markdown_verbatim():
    pass  # TODO: implement




def test_local_audio_strips_markdown_after_reassembling_streamed_deltas():
    pass  # TODO: implement




def test_local_audio_streaming_preserves_whitespace_across_chunks():
    pass  # TODO: implement




def test_local_text_only_tool_marker_can_span_tokens_without_losing_whitespace():
    pass  # TODO: implement




def _local_handler_with_chunks(chunks, *, cancelled=False):
    pass  # TODO: implement

    def generate(_self, _chat, _language_code, _generation, ctx, _runtime_config, _response):
        pass  # TODO: implement



def test_local_history_commits_text_and_tools_in_emitted_order():
    pass  # TODO: implement








def test_cancelled_local_generation_does_not_write_partial_history():
    pass  # TODO: implement




def test_local_tool_call_is_recorded_before_chunk_is_emitted():
    pass  # TODO: implement





def test_cancelled_local_tool_turn_rolls_back_fast_output():
    pass  # TODO: implement


