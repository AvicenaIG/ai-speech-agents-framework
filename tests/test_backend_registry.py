import subprocess
import sys
from copy import deepcopy
from dataclasses import dataclass, fields, replace
from queue import Queue
from threading import Event
from types import SimpleNamespace

import pytest
from openai.types.realtime import RealtimeErrorEvent, SessionUpdateEvent

import ai_speech_agents_framework.s2s_pipeline as s2s_pipeline
from ai_speech_agents_framework.arguments_classes.module_arguments import ModuleArguments
from ai_speech_agents_framework.arguments_classes.vad_arguments import VADHandlerArguments
from ai_speech_agents_framework.backend_registry import (
)
from ai_speech_agents_framework.pipeline.cancel_scope import CancelScope
from ai_speech_agents_framework.pipeline.speculative_turns import SpeculativeTurnTracker
from ai_speech_agents_framework.s2s_pipeline import (
)


@dataclass
class FakeArguments:
    pass  # TODO: implement


def _context() -> HandlerContext:
    pass  # TODO: implement


def _factory(_context, config):
    pass  # TODO: implement


def test_builtin_registry_lookup_and_cli_choices_share_one_catalog():
    pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_session_language_validation_uses_loaded_faster_whisper_capabilities(model_name, supported_languages, expected):
    pass  # TODO: implement



def test_parakeet_session_language_selection_remains_unsupported():
    pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_faster_whisper_loaded_languages_control_session_update(monkeypatch, model_name, supported_languages, accepted):
    pass  # TODO: implement




@pytest.mark.parametrize(
)
def test_transformers_whisper_session_language_uses_loaded_generation_config(
    pass  # TODO: implement
):




@pytest.mark.parametrize(("setup_language", "rejected"), [("en", True), (None, False)])
def test_openai_realtime_stt_auto_reset_is_rejected_only_when_setup_hint_cannot_be_cleared(
    pass  # TODO: implement
):




def test_omnivoice_tts_backend_is_registered_as_optional():
    pass  # TODO: implement



@pytest.mark.parametrize(("num_threads", "expected_threads"), [(None, 4), (2, 2)])
def test_phonon_cli_and_registry_construct_native_handler(monkeypatch, num_threads, expected_threads):
    pass  # TODO: implement


    def load(**kwargs):
        pass  # TODO: implement



def test_phonon_missing_dependency_reports_install_extra(monkeypatch):
    pass  # TODO: implement


def test_phonon_stays_on_cpu_when_global_device_is_set():
    pass  # TODO: implement


@pytest.mark.parametrize(("normalizer", "expected"), [("en", {"en"}), ("fr", {"fr"}), ("none", set())])
@pytest.mark.parametrize("enable_visemes", [False, True])
def test_phonon_session_languages_match_fixed_normalizer(monkeypatch, normalizer, expected, enable_visemes):
    pass  # TODO: implement


def test_sensevoice_stt_backend_is_registered_with_its_optional_extra():
    pass  # TODO: implement



def test_sensevoice_cli_config_is_normalized_for_the_handler():
    pass  # TODO: implement



def test_omnivoice_cli_config_is_normalized_for_the_handler():
    pass  # TODO: implement



def test_registry_rejects_duplicate_names_and_wrong_kinds():
    pass  # TODO: implement



def test_supertonic_cli_config_is_normalized_for_the_handler():
    pass  # TODO: implement



def test_audio_input_validation_uses_registry_capability_not_backend_name():
    pass  # TODO: implement



def test_llm_proxy_validation_uses_registry_capability():
    pass  # TODO: implement



def test_llm_proxy_validation_happens_before_pipeline_construction(monkeypatch):
    pass  # TODO: implement

    def fake_build_pipeline(*_args, **_kwargs):
        pass  # TODO: implement





def test_test_backend_only_needs_config_factory_and_registry_entry():
    pass  # TODO: implement

    def factory(context, config):
        pass  # TODO: implement




@pytest.mark.parametrize("backend", ["openai", "drama3"])
def test_openai_tts_backend_constructs_through_registry(monkeypatch, backend):
    pass  # TODO: implement




def test_openai_tts_factory_receives_assistant_language_opt_in(monkeypatch):
    pass  # TODO: implement

    class FakeHandler:
        pass  # TODO: implement
        def __init__(self, *_args, setup_kwargs, **_kwargs):
            pass  # TODO: implement




def test_qwen3_tts_factory_receives_assistant_language_opt_in(monkeypatch):
    pass  # TODO: implement

    class FakeHandler:
        pass  # TODO: implement
        def __init__(self, *_args, setup_kwargs, **_kwargs):
            pass  # TODO: implement




def test_openai_stt_backend_constructs_through_registry(monkeypatch):
    pass  # TODO: implement




@pytest.mark.parametrize("live", [False, True])
def test_windowed_http_stt_configuration_reaches_handler_and_vad(monkeypatch, live):
    pass  # TODO: implement

    class DummyHandler:
        pass  # TODO: implement
        def __init__(self, *_args, **kwargs):
            pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_streaming_stt_backends_parse_and_construct_through_registry(
    pass  # TODO: implement
):




def test_streaming_stt_backend_is_attached_to_vad_without_changing_notifier_path(monkeypatch):
    pass  # TODO: implement
    class DummyHandler:
        pass  # TODO: implement
        def __init__(self, *_args, **_kwargs):
            pass  # TODO: implement

    class DummyNotifier(DummyHandler):
        pass  # TODO: implement


    def stt_factory(_context, _config):
        pass  # TODO: implement

    def other_factory(_context, _config):
        pass  # TODO: implement






def test_new_stt_backend_gets_transcription_notifier_by_default(monkeypatch):
    pass  # TODO: implement

    class DummyHandler:
        pass  # TODO: implement
        def __init__(self, *_args, **_kwargs):
            pass  # TODO: implement

    class DummyNotifier(DummyHandler):
        pass  # TODO: implement

    def stt_factory(context, _config):
        pass  # TODO: implement

    def other_factory(_context, _config):
        pass  # TODO: implement






def test_parser_carries_only_selected_normalized_configs():
    pass  # TODO: implement



def test_facebook_mms_options_are_normalized_for_handler_setup(monkeypatch):
    pass  # TODO: implement


    def fake_setup(self, _should_listen, **kwargs):
        pass  # TODO: implement




def test_facebook_mms_handler_honors_model_override(monkeypatch):
    pass  # TODO: implement





def test_facebook_mms_restores_custom_model_when_returning_to_initial_language(monkeypatch):
    pass  # TODO: implement


    def fake_load_model(self, language, model_name=None):
        pass  # TODO: implement





def test_facebook_mms_session_reset_restores_custom_model_for_same_language(monkeypatch):
    pass  # TODO: implement





def test_parser_warning_ignores_known_options_for_inactive_backends(caplog):
    pass  # TODO: implement



def test_parser_still_rejects_unknown_options():
    pass  # TODO: implement


@pytest.mark.parametrize("selector", ["--stt", "--llm_backend", "--tts"])
def test_parser_reports_invalid_backend_selectors_with_argparse(selector, capsys):
    pass  # TODO: implement



@pytest.mark.parametrize("backend_name", ["whisper", "whisper-mlx", "mlx-audio-whisper"])
def test_common_language_flag_reaches_compatible_stt_backends(backend_name, caplog):
    pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_global_device_only_updates_device_aware_builtin_configs(kind, backend_name):
    pass  # TODO: implement





def test_global_device_does_not_reach_mlx_audio_whisper_setup(monkeypatch):
    pass  # TODO: implement


    def fake_setup(self, model_name, language, gen_kwargs):
        pass  # TODO: implement





def test_registry_import_keeps_backend_modules_lazy():
    pass  # TODO: implement
import sys
import ai_speech_agents_framework.backend_registry

eager_backends = [
]
assert not eager_backends, f"Registry imported backend modules: {eager_backends}"
""",



def test_dependency_error_names_backend_and_required_extra():
    pass  # TODO: implement
    def missing(_context, _config):
        pass  # TODO: implement




@pytest.mark.parametrize("option", ["--live_transcription_min_silence_ms", "--parakeet_tdt_compute_type"])
def test_removed_ineffective_options_are_rejected(option):
    pass  # TODO: implement


@pytest.mark.parametrize("enabled", [False, True])
def test_viseme_stage_is_optional_and_connected_after_tts(monkeypatch, enabled):
    pass  # TODO: implement

    class DummyHandler:
        pass  # TODO: implement
        def __init__(self, *_args, **kwargs):
            pass  # TODO: implement

    def factory(name):
        pass  # TODO: implement
        def build(context, _config):
            pass  # TODO: implement




def test_viseme_cli_and_json_configuration(tmp_path):
    pass  # TODO: implement



def test_pocket_farsi_model_cli_routes_to_setup():
    pass  # TODO: implement
