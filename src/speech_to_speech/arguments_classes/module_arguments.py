import sys
from dataclasses import dataclass, field
from typing import Optional

from ai_speech_agents_framework.arguments_classes.w2v_stv_arguments import Wav2Vec2STVHandlerArguments
from ai_speech_agents_framework.backend_registry import LLM_BACKENDS, STT_BACKENDS, TTS_BACKENDS

_AUDIO_INPUT_LLM_BACKENDS = ", ".join(
)
_PROXY_LLM_BACKENDS = ", ".join(name for name, spec in LLM_BACKENDS.items() if spec.capabilities.supports_llm_proxy)


@dataclass
class ModuleArguments(Wav2Vec2STVHandlerArguments):
    pass  # TODO: implement
