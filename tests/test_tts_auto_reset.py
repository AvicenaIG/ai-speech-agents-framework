import pytest
from openai.types.realtime import RealtimeSessionCreateRequest

from ai_speech_agents_framework.api.openai_realtime.runtime_config import RuntimeConfig
from ai_speech_agents_framework.pipeline.messages import TTSInput
from ai_speech_agents_framework.TTS.facebookmms_handler import FacebookMMSTTSHandler
from ai_speech_agents_framework.TTS.kokoro_handler import KokoroTTSHandler


def _auto_config() -> RuntimeConfig:
    pass  # TODO: implement


def _session_config(language: str) -> RuntimeConfig:
    pass  # TODO: implement


def test_kokoro_short_auto_reply_restores_setup_voice_after_spanish(monkeypatch):
    pass  # TODO: implement

    class FakePipeline:
        pass  # TODO: implement
        def load_voice(self, voice):
            pass  # TODO: implement

    class FakeModel:
        pass  # TODO: implement
        def _get_pipeline(self, language):
            pass  # TODO: implement





def test_facebook_mms_short_auto_reply_restores_setup_model_after_spanish(monkeypatch):
    pass  # TODO: implement

    def fake_load_model(self, language, model_name=None):
        pass  # TODO: implement





@pytest.mark.parametrize(
)
def test_kokoro_detected_language_without_native_voice_keeps_session_language(monkeypatch, detected, expected):
    pass  # TODO: implement




@pytest.mark.parametrize(("detected", "expected_loads"), [("fr", [("fr", None)]), ("ja", [])])
def test_facebook_mms_detected_language_without_checkpoint_keeps_session_language(
    pass  # TODO: implement
):

    def fake_load_model(self, language, model_name=None):
        pass  # TODO: implement



