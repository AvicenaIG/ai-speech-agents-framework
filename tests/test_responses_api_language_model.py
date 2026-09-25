import json
import logging
from queue import Queue
from threading import BoundedSemaphore, Event, Lock, Thread
from time import sleep
from types import SimpleNamespace
from unittest.mock import MagicMock

import httpx
import numpy as np
import pytest
from openai import Stream
from openai.types.realtime.conversation_item import (
)
from openai.types.realtime.realtime_response_create_params import RealtimeResponseCreateParams
from openai.types.responses import (
)
from openai.types.responses.response_output_text import ResponseOutputText

import ai_speech_agents_framework.LLM.base_openai_compatible_language_model as base_openai_compatible_language_model
from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.LLM.base_openai_compatible_language_model import WARMUP_MAX_RETRIES, ToolCall, Usage
from ai_speech_agents_framework.LLM.chat import (
)
from ai_speech_agents_framework.LLM.responses_api_language_model import ResponsesApiModelHandler
from ai_speech_agents_framework.pipeline.cancel_scope import CancelScope
from ai_speech_agents_framework.pipeline.messages import (
)
from ai_speech_agents_framework.pipeline.turn_latency import TurnLatencyStore
from tests.llm_history import drive_llm


def _make_text_delta_event(text):
    pass  # TODO: implement


def _make_output_item_done_event(role="assistant", content="Hello.", item_type="message"):
    pass  # TODO: implement


def _make_stream(events):
    pass  # TODO: implement


def _make_function_call_done_event(name="camera", arguments="{}"):
    pass  # TODO: implement


def _make_response(output, usage=None):
    pass  # TODO: implement


@pytest.mark.parametrize("stream", [False, True])
def test_reasoning_tool_continuation_replays_original_provider_items(stream):
    pass  # TODO: implement

    def create(**kwargs):
        pass  # TODO: implement



def _make_runtime_config(chat_size=2, instructions="You are a helpful AI assistant."):
    pass  # TODO: implement



def _make_request(text="Hi", chat_size=2):
    pass  # TODO: implement


def _make_audio_request(cfg=None):
    pass  # TODO: implement


def _chat_chunk(*, content=None, tool_calls=None, usage=None, refusal=None):
    pass  # TODO: implement


def _chat_tool_delta(index, *, tool_id=None, name=None, arguments=None):
    pass  # TODO: implement


def _make_handler(*, disable_thinking=False, stream=True, cancel_scope=None, reasoning_effort="none"):
    pass  # TODO: implement


@pytest.mark.parametrize("with_tool_prefix", [False, True])
def test_discarded_prefetch_aborts_blocked_provider_stream(with_tool_prefix):
    pass  # TODO: implement
    class BlockingStream:
        pass  # TODO: implement
        def __init__(self):
            pass  # TODO: implement

        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement


    def run():
        pass  # TODO: implement





def test_failed_prefetch_is_discarded_before_terminal_is_yielded():
    pass  # TODO: implement

    def fail_create(**kwargs):
        pass  # TODO: implement





def test_claimed_failed_prefetch_emits_transactional_fallback():
    pass  # TODO: implement

    def fail_create(**kwargs):
        pass  # TODO: implement





def test_discarded_prefetch_does_not_block_on_provider_connect():
    pass  # TODO: implement

    class LateStream:
        pass  # TODO: implement
        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement

    def create(**kwargs):
        pass  # TODO: implement






def test_claimed_prefetch_cancel_does_not_block_on_provider_connect():
    pass  # TODO: implement

    class LateStream:
        pass  # TODO: implement
        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement

    def create(**kwargs):
        pass  # TODO: implement






def test_claimed_prefetch_cancel_aborts_blocked_provider_read():
    pass  # TODO: implement
    class BlockingStream:
        pass  # TODO: implement
        def __init__(self):
            pass  # TODO: implement

        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement





def test_repeated_prefetch_invalidation_bounds_provider_connect_workers():
    pass  # TODO: implement

    class LateStream:
        pass  # TODO: implement
        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement

    def create(**kwargs):
        pass  # TODO: implement












def test_prefetch_uses_one_worker_and_one_bounded_queue(monkeypatch):
    pass  # TODO: implement

    class TrackingQueue(Queue):
        pass  # TODO: implement
        def __init__(self, maxsize=0):
            pass  # TODO: implement


    def track_worker(target, *, name):
        pass  # TODO: implement





def test_warmup_uses_request_scoped_sdk_retries():
    pass  # TODO: implement




def test_compaction_uses_responses_reasoning_shape():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement




def test_warmup_failure_propagates_and_prevents_readiness():
    pass  # TODO: implement



def test_process_streams_text_from_response_events():
    pass  # TODO: implement







def test_process_records_hosted_llm_latency():
    pass  # TODO: implement

    def _events():
        pass  # TODO: implement





def test_text_only_streams_raw_deltas_without_sentence_trimming():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement






def test_audio_response_sentence_batches_streaming_call():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_process_flushes_tool_lead_in_before_function_call_with_sentence_batching():
    pass  # TODO: implement






def test_markdown_cleanup_does_not_modify_responses_api_tool_arguments():
    pass  # TODO: implement




def test_process_preserves_streamed_text_after_function_call_order():
    pass  # TODO: implement






def test_audio_streaming_preserves_provider_whitespace_across_chunks():
    pass  # TODO: implement





def test_process_preserves_nonstreaming_text_tool_text_order():
    pass  # TODO: implement







def test_process_handles_cancellation():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_cancelled_stream_emits_provider_usage_and_rolls_back_history():
    pass  # TODO: implement





def test_cancelled_nonstreaming_response_emits_provider_usage():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_cancelled_text_tool_turn_rolls_back_ordered_call():
    pass  # TODO: implement





def test_provider_error_after_text_tool_rolls_back_ordered_call():
    pass  # TODO: implement

    class FailingStream:
        pass  # TODO: implement
        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement




def test_generation_is_rejected_until_ordered_tool_output_arrives():
    pass  # TODO: implement

    def create(**kwargs):
        pass  # TODO: implement





    def completed_create(**kwargs):
        pass  # TODO: implement



def test_responses_api_timing_logs_only_text_chunks():
    pass  # TODO: implement



def test_setup_uses_dummy_api_key_for_custom_base_url(monkeypatch):
    pass  # TODO: implement

    class FakeOpenAI:
        pass  # TODO: implement
        def __init__(self, *, api_key, base_url):
            pass  # TODO: implement





def test_setup_preserves_environment_api_key_for_custom_base_url(monkeypatch):
    pass  # TODO: implement

    class FakeOpenAI:
        pass  # TODO: implement
        def __init__(self, *, api_key, base_url):
            pass  # TODO: implement





def test_setup_does_not_inject_dummy_key_for_remote_custom_url(monkeypatch):
    pass  # TODO: implement

    class FakeOpenAI:
        pass  # TODO: implement
        def __init__(self, *, api_key, base_url):
            pass  # TODO: implement





def test_process_read_timeout_speaks_fallback_and_preserves_failure():
    pass  # TODO: implement

    def make_timeout_stream():
        pass  # TODO: implement





def test_read_timeout_after_partial_text_fails_without_apology_or_history_commit():
    pass  # TODO: implement

    class PartialThenTimeoutStream:
        pass  # TODO: implement
        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement





def test_read_timeout_after_tool_call_fails_and_rolls_back_call():
    pass  # TODO: implement

    class ToolThenTimeoutStream:
        pass  # TODO: implement
        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement





def test_generation_error_emits_failed_end_of_response():
    pass  # TODO: implement

    def boom(**kwargs):
        pass  # TODO: implement





def test_empty_context_fails_with_clear_message_without_calling_provider():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement






def test_disable_thinking_passes_extra_body():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_no_disable_thinking_omits_extra_body():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_responses_reasoning_omitted_when_unset():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_responses_extra_body_uses_provider_fallback_only_without_reasoning_effort():
    pass  # TODO: implement



def test_second_turn_flattens_assistant_history_for_responses():
    pass  # TODO: implement


    def fake_create(**kwargs):
        pass  # TODO: implement





def test_audio_request_uses_chat_completions_input_audio_payload():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement






def test_audio_second_turn_retains_recent_audio_then_compacts_older_turn():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_audio_nonstreaming_tool_call_uses_chat_protocol_and_survives_next_turn():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement






def test_audio_streaming_reuses_tool_parser_and_emits_trailing_usage():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_audio_nonstreaming_refusal_is_emitted_and_stored():
    pass  # TODO: implement




def test_failed_audio_request_rolls_back_provisional_history():
    pass  # TODO: implement




def test_interrupted_audio_tool_turn_rolls_back_user_call_and_fast_output():
    pass  # TODO: implement





# ── Out-of-band (conversation="none") responses ──────────────────────────


def _make_oob_request(input_items, *, conversation="none", chat_size=2, seed_default="Hi"):
    pass  # TODO: implement


def _capture_create(handler, events):
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement



def test_out_of_band_emits_output_but_does_not_commit_to_default_conversation():
    pass  # TODO: implement




def test_empty_response_overrides_disable_session_instructions_and_tools():
    pass  # TODO: implement




def test_out_of_band_timeout_after_tool_call_fails_without_apology():
    pass  # TODO: implement

    class ToolThenTimeoutStream:
        pass  # TODO: implement
        def __iter__(self):
            pass  # TODO: implement

        def close(self):
            pass  # TODO: implement





def test_out_of_band_input_builds_fresh_context():
    pass  # TODO: implement




def test_out_of_band_empty_input_clears_context():
    pass  # TODO: implement




def test_out_of_band_absent_input_reads_default_conversation():
    pass  # TODO: implement




def test_out_of_band_invalid_input_emits_failed_end_of_response():
    pass  # TODO: implement

    def fake_create(**kwargs):
        pass  # TODO: implement





def test_response_history_precedes_speech_that_arrived_during_generation():
    pass  # TODO: implement

    def create(**kwargs):
        pass  # TODO: implement





def test_responses_backend_keeps_injected_context_with_session_instructions():
    pass  # TODO: implement

    def create(**kwargs):
        pass  # TODO: implement


