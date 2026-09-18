from __future__ import annotations

import logging
from collections.abc import Callable, Iterable, Mapping
from copy import deepcopy
from dataclasses import dataclass, field, fields
from importlib import import_module
from queue import Queue
from threading import Event
from typing import Any, Literal

from ai_speech_agents_framework.arguments_classes.chat_completions_language_model_arguments import (
)
from ai_speech_agents_framework.arguments_classes.chat_tts_arguments import ChatTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.drama3_tts_arguments import Drama3TTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.facebookmms_tts_arguments import FacebookMMSTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.faster_whisper_stt_arguments import (
)
from ai_speech_agents_framework.arguments_classes.kitten_tts_arguments import KittenTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.kokoro_tts_arguments import KokoroTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.language_model_arguments import (
)
from ai_speech_agents_framework.arguments_classes.minimax_tts_arguments import MiniMaxTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.mlx_audio_whisper_arguments import (
)
from ai_speech_agents_framework.arguments_classes.nemotron_streaming_stt_arguments import (
)
from ai_speech_agents_framework.arguments_classes.omnivoice_tts_arguments import OmniVoiceTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.openai_realtime_stt_arguments import OpenAIRealtimeSTTHandlerArguments
from ai_speech_agents_framework.arguments_classes.openai_stt_arguments import OpenAICompatibleSTTHandlerArguments
from ai_speech_agents_framework.arguments_classes.openai_tts_arguments import OpenAICompatibleTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.orukeet_stt_arguments import OrukeetSTTHandlerArguments
from ai_speech_agents_framework.arguments_classes.paraformer_stt_arguments import ParaformerSTTHandlerArguments
from ai_speech_agents_framework.arguments_classes.parakeet_tdt_arguments import (
)
from ai_speech_agents_framework.arguments_classes.parakeet_unified_stt_arguments import (
)
from ai_speech_agents_framework.arguments_classes.phonon_tts_arguments import PhononTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.pocket_tts_arguments import PocketTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.qwen3_asr_stt_arguments import Qwen3ASRSTTHandlerArguments
from ai_speech_agents_framework.arguments_classes.qwen3_tts_arguments import Qwen3TTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.responses_api_language_model_arguments import (
)
from ai_speech_agents_framework.arguments_classes.sense_voice_stt_arguments import SenseVoiceSTTHandlerArguments
from ai_speech_agents_framework.arguments_classes.supertonic_tts_arguments import SupertonicTTSHandlerArguments
from ai_speech_agents_framework.arguments_classes.vllm_realtime_stt_arguments import VLLMRealtimeSTTHandlerArguments
from ai_speech_agents_framework.arguments_classes.whisper_stt_arguments import WhisperSTTHandlerArguments
from ai_speech_agents_framework.pipeline.cancel_scope import CancelScope
from ai_speech_agents_framework.pipeline.speculative_turns import SpeculativeTurnTracker

BackendKind = Literal["stt", "llm", "tts"]
BackendConfig = dict[str, Any]

logger = logging.getLogger(__name__)


@dataclass
class EmptyBackendArguments:
    pass  # TODO: implement


@dataclass(frozen=True)
class BackendCapabilities:
    pass  # TODO: implement



@dataclass(frozen=True)
class HandlerContext:
    pass  # TODO: implement



HandlerFactory = Callable[[HandlerContext, Mapping[str, Any]], Any]
ConfigNormalizer = Callable[[Any], BackendConfig]


@dataclass(frozen=True)
class BackendSpec:
    pass  # TODO: implement


    def normalize(self, config: Any) -> BackendConfig:
        pass  # TODO: implement


@dataclass(frozen=True)
class BackendSelection:
    pass  # TODO: implement


    def name(self) -> str:
        pass  # TODO: implement

    def kind(self) -> BackendKind:
        pass  # TODO: implement

    def copy_for_pipeline(self) -> BackendSelection:
        pass  # TODO: implement


def normalize_dataclass_config(config: Any, prefix: str | None = None) -> BackendConfig:
    pass  # TODO: implement





def _normalize_facebook_mms_config(config: Any) -> BackendConfig:
    pass  # TODO: implement


def build_backend_registry(kind: BackendKind, specs: Iterable[BackendSpec]) -> dict[str, BackendSpec]:
    pass  # TODO: implement



def _optional_dependency_error(selection: BackendSelection, exc: BaseException) -> ImportError | None:
    pass  # TODO: implement


def create_backend_handler(selection: BackendSelection, context: HandlerContext) -> Any:
    pass  # TODO: implement



def _load_handler(module_name: str, class_name: str) -> type[Any]:
    pass  # TODO: implement


def _simple_handler_factory(
    pass  # TODO: implement
) -> HandlerFactory:
    def create(context: HandlerContext, config: Mapping[str, Any]) -> Any:
        pass  # TODO: implement



def _create_audio_input(context: HandlerContext, _config: Mapping[str, Any]) -> Any:
    pass  # TODO: implement


def _create_parakeet(context: HandlerContext, config: Mapping[str, Any]) -> Any:
    pass  # TODO: implement


def _create_orukeet(context: HandlerContext, config: Mapping[str, Any]) -> Any:
    pass  # TODO: implement


def _create_openai_tts(context: HandlerContext, config: Mapping[str, Any]) -> Any:
    pass  # TODO: implement


def _create_streaming_stt(class_name: str) -> HandlerFactory:
    pass  # TODO: implement
    def create(context: HandlerContext, config: Mapping[str, Any]) -> Any:
        pass  # TODO: implement



def _create_local_llm(backend: Literal["transformers", "mlx-lm"]) -> HandlerFactory:
    pass  # TODO: implement
    def create(context: HandlerContext, config: Mapping[str, Any]) -> Any:
        pass  # TODO: implement



STT_BACKENDS = build_backend_registry(
)

LLM_BACKENDS = build_backend_registry(
)

TTS_BACKENDS = build_backend_registry(
)
