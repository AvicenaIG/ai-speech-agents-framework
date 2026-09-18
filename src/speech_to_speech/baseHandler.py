from __future__ import annotations

# ruff: noqa: I001

import logging
from queue import Empty, Queue
from threading import Event
from time import perf_counter
from typing import Any, Generic, Iterator, TypeVar, cast

import numpy as np

from ai_speech_agents_framework.pipeline.control import PipelineControlMessage, is_control_message, SESSION_END
from ai_speech_agents_framework.pipeline.events import PipelineEvent, TokenUsageEvent
from ai_speech_agents_framework.pipeline.log_context import pipeline_log_ctx
from ai_speech_agents_framework.pipeline.messages import (
)
from ai_speech_agents_framework.pipeline.transcript_logging import log_exception

logger = logging.getLogger(__name__)

InT = TypeVar("InT")
OutT = TypeVar("OutT")


class BaseHandler(Generic[InT, OutT]):
    pass  # TODO: implement

    def __init__(
        pass  # TODO: implement

    def setup(self, *arg: Any, **kwargs: Any) -> None:
        pass  # TODO: implement

    def process(self, input: InT) -> Iterator[OutT]:
        pass  # TODO: implement

    def should_process_input(self, item: InT) -> bool:
        pass  # TODO: implement

    def should_emit_output(self, output: OutT) -> bool:
        pass  # TODO: implement

    def before_emit_output(self, output: OutT) -> None:
        pass  # TODO: implement

    def output_for_queue(self, output: OutT, source_input: InT) -> OutT | AudioOutput:
        pass  # TODO: implement

    def process_pipeline_event(self, event: PipelineEvent) -> Iterator[Any]:
        pass  # TODO: implement

    def run(self) -> None:
        pass  # TODO: implement

    def _run_loop(self) -> None:
        pass  # TODO: implement







    def last_time(self) -> float:
        pass  # TODO: implement

    def min_time_to_debug(self) -> float:
        pass  # TODO: implement

    def timing_log_level(self) -> int:
        pass  # TODO: implement

    def should_log_timing(self, output: OutT) -> bool:
        pass  # TODO: implement

    def cleanup(self) -> None:
        pass  # TODO: implement

    def on_session_end(self) -> None:
        pass  # TODO: implement
