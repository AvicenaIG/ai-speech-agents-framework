import json
import sys
from types import SimpleNamespace

import pytest

from ai_speech_agents_framework.arguments_classes.chat_completions_language_model_arguments import (
)
from ai_speech_agents_framework.arguments_classes.language_model_arguments import (
)
from ai_speech_agents_framework.arguments_classes.local_audio_arguments import LocalAudioArguments
from ai_speech_agents_framework.arguments_classes.module_arguments import ModuleArguments
from ai_speech_agents_framework.arguments_classes.phonon_tts_arguments import PhononTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.qwen3_tts_arguments import Qwen3TTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.realtime_server_arguments import RealtimeServerArguments
from ai_speech_agents_framework.arguments_classes.responses_api_language_model_arguments import (
)
from ai_speech_agents_framework.arguments_classes.vad_arguments import VADHandlerArguments
from ai_speech_agents_framework.cli import main, parse_command, parse_talk_arguments
from ai_speech_agents_framework.pipeline.transcript_logging import set_log_transcripts, transcript_for_log
from ai_speech_agents_framework.s2s_pipeline import ParsedArguments, parse_arguments, prepare_all_args, prepare_module_args


def test_phonon_defaults_to_public_english_31m_checkpoint():
    pass  # TODO: implement


def test_release_defaults_match_local_qwen35_parakeet_qwen3_profile():
    pass  # TODO: implement




def test_parse_arguments_enables_llm_output_language_detection():
    pass  # TODO: implement



def test_server_defaults_to_loopback():
    pass  # TODO: implement


def test_parse_talk_arguments_keeps_retry_timeout_field_name():
    pass  # TODO: implement



def test_conversation_only_is_the_default_for_local_and_talk():
    pass  # TODO: implement


def test_verbose_restores_diagnostic_output_for_local_and_talk():
    pass  # TODO: implement


@pytest.mark.parametrize("flags", [["--print-json"], ["--verbose", "--print-json"]])
def test_raw_json_enables_diagnostic_output(flags):
    pass  # TODO: implement


def test_serve_rejects_client_verbose_flag():
    pass  # TODO: implement


def test_vad_firered_flag_is_accepted():
    pass  # TODO: implement



def test_mac_optimal_settings_flag_does_not_select_a_command():
    pass  # TODO: implement



def test_mac_optimal_settings_routes_explicit_model_to_mlx_backend():
    pass  # TODO: implement



def test_mac_optimal_settings_preserves_explicit_component_overrides():
    pass  # TODO: implement




def test_mac_optimal_settings_preserves_explicit_component_device():
    pass  # TODO: implement



@pytest.mark.parametrize("flag", ["--local_mac_optimal_settings", "--mac_optimal_settings"])
def test_noncanonical_mac_optimal_settings_flags_are_rejected(flag):
    pass  # TODO: implement


def test_mac_diarization_shortcut():
    pass  # TODO: implement



def test_diarization_shortcut_preserves_custom_model():
    pass  # TODO: implement



def test_diarization_defaults_to_automatic_device_selection():
    pass  # TODO: implement



def test_diarization_shortcut_preserves_explicit_settings():
    pass  # TODO: implement



def test_diarization_is_opt_in():
    pass  # TODO: implement


@pytest.mark.parametrize("platform", ["darwin", "linux", "win32"])
@pytest.mark.parametrize("command", ["serve", "local"])
def test_parse_arguments_default_backend_runs_local_qwen35(platform, command, monkeypatch):
    pass  # TODO: implement



def test_parse_arguments_accepts_smart_turn_options():
    pass  # TODO: implement



@pytest.mark.parametrize("platform", ["darwin", "linux"])
@pytest.mark.parametrize("backend", ["mlx-lm", "transformers", "responses-api", "chat-completions"])
def test_llm_defaults_follow_explicit_backend_and_keep_model_overrides(platform, backend, monkeypatch):
    pass  # TODO: implement


def test_parse_arguments_can_disable_smart_turn():
    pass  # TODO: implement



def test_parse_arguments_rejects_removed_smart_turn_device_option():
    pass  # TODO: implement


def test_parse_arguments_accepts_qwen3_tts_backend_override():
    pass  # TODO: implement



def test_parse_arguments_accepts_openai_tts_backend():
    pass  # TODO: implement



def test_parse_arguments_accepts_vllm_tts_stream_extension():
    pass  # TODO: implement



def test_parse_arguments_accepts_openai_stt_backend():
    pass  # TODO: implement



def test_parse_arguments_accepts_qwen3_tts_ggml_options():
    pass  # TODO: implement



@pytest.mark.parametrize("command", ["serve", "talk", "local"])
def test_cli_exposes_command_family(command):
    pass  # TODO: implement


def test_local_pipeline_arguments_support_smart_turn():
    pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_cli_maps_legacy_modes_to_commands_with_warning(mode, command, command_flag, capsys):
    pass  # TODO: implement



def test_cli_accepts_equals_syntax_for_legacy_mode(capsys):
    pass  # TODO: implement


@pytest.mark.parametrize(("mode", "command"), [("realtime", "serve"), ("local", "local")])
def test_main_dispatches_legacy_modes_to_pipeline_commands(mode, command, monkeypatch, capsys):
    pass  # TODO: implement




@pytest.mark.parametrize("mode", ["socket", "raw-websocket", "websocket"])
def test_cli_rejects_other_legacy_modes_with_migration_guidance(mode, capsys):
    pass  # TODO: implement



def test_talk_accepts_one_full_url_connection_option():
    pass  # TODO: implement



def test_talk_leaves_api_key_unset_for_sdk_environment_authentication():
    pass  # TODO: implement


def test_talk_can_cycle_voices_without_losing_initial_voice():
    pass  # TODO: implement


def test_talk_accepts_custom_playback_buffer():
    pass  # TODO: implement



def test_packaged_audio_clients_have_no_general_playback_buffer_default():
    pass  # TODO: implement


@pytest.mark.parametrize("flag", ["--log-transcripts", "--log_transcripts"])
def test_talk_accepts_transcript_logging_opt_in(flag):
    pass  # TODO: implement


def test_main_wires_talk_transcript_logging_before_client_start(monkeypatch):
    pass  # TODO: implement

    def warning():
        pass  # TODO: implement

    def run_client(config):
        pass  # TODO: implement





def test_talk_loads_opt_in_tool_module(monkeypatch):
    pass  # TODO: implement





@pytest.mark.parametrize("flag", ["--host", "--port", "--base-url", "--websocket-base-url", "--stt"])
def test_talk_rejects_server_and_overlapping_connection_flags(flag):
    pass  # TODO: implement


@pytest.mark.parametrize("command", ["serve", "local"])
def test_pipeline_commands_reject_talk_url(command):
    pass  # TODO: implement


def test_serve_rejects_local_audio_flags():
    pass  # TODO: implement


def test_local_accepts_audio_flags_but_rejects_host():
    pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_local_accepts_opt_in_tool_module(flag):
    pass  # TODO: implement



def test_parse_arguments_transformers_backend():
    pass  # TODO: implement



def test_prepare_module_args_rejects_responses_api_for_stt_none():
    pass  # TODO: implement



def test_parse_arguments_stt_none_supports_chat_completions_audio_path():
    pass  # TODO: implement




def test_additive_config_api_preserves_flat_json_contract(tmp_path):
    pass  # TODO: implement



@pytest.fixture
def configured_cli(tmp_path, monkeypatch):
    pass  # TODO: implement
blocks:
pipelines:
""")


@pytest.mark.parametrize("flag", ["-f", "--file"])
def test_file_cli_dispatches_selected_pipeline(flag, configured_cli, monkeypatch):
    pass  # TODO: implement


def test_file_talk_resolves_only_client(configured_cli, monkeypatch):
    pass  # TODO: implement


@pytest.mark.parametrize("command", ["serve", "local"])
def test_file_cli_rejects_multiple_definitions_before_runtime(command, configured_cli, monkeypatch):
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_file_cli_rejects_invalid_and_mixed_flags(extra, configured_cli, monkeypatch, capsys):
    pass  # TODO: implement


def test_file_talk_rejects_name(configured_cli, monkeypatch):
    pass  # TODO: implement


@pytest.mark.parametrize("command", ["serve", "talk", "local"])
def test_cli_help_does_not_read_file_or_run_runtime(command, configured_cli, monkeypatch):
    pass  # TODO: implement


def test_name_requires_file(monkeypatch):
    pass  # TODO: implement


def test_file_cli_hides_runtime_error(configured_cli, monkeypatch, capsys):
    pass  # TODO: implement

    def fail(*_args):
        pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_configured_cli_rejects_or_helps_before_heavy_imports(arguments):
    pass  # TODO: implement

import importlib.abc, sys
class Block(importlib.abc.MetaPathFinder):
    pass  # TODO: implement
    def find_spec(self, fullname, *args):
        pass  # TODO: implement
sys.meta_path.insert(0, Block())
from ai_speech_agents_framework.cli import main
sys.argv = ["ai-speech-agents-framework", *sys.argv[1:]]
try:
except SystemExit as exc:
else:
"""


def test_file_cli_accepts_attached_short_file_flag(configured_cli, monkeypatch):
    pass  # TODO: implement


def test_file_cli_malformed_flags_hide_input_values(configured_cli, monkeypatch, capsys):
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_legacy_help_keeps_command_settings(arguments, flags, monkeypatch, capsys):
    pass  # TODO: implement


def test_parse_arguments_preserves_kitten_backend_options():
    pass  # TODO: implement



def test_parse_arguments_rejects_unsupported_kitten_device():
    pass  # TODO: implement
