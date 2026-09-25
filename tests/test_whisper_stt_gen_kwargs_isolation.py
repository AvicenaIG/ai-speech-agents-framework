"""The whisper STT handler must not write its language into the shared default.

`setup` takes `gen_kwargs: dict[str, Any] = {}`, so every call that omits the
argument receives the same dict object. `setup` then stores `language` in it,
which means the value survives in the default for the life of the process and is
handed to the next handler built without an explicit `gen_kwargs`.
"""

from typing import Any

import pytest
import torch

from ai_speech_agents_framework.STT import whisper_stt_handler
from ai_speech_agents_framework.STT.whisper_stt_handler import WhisperSTTHandler


class _FakeConfig:
    pass  # TODO: implement


class _FakeModel:
    pass  # TODO: implement

    def to(self, device: str) -> "_FakeModel":
        pass  # TODO: implement

    def generate(self, *args: Any, **kwargs: Any) -> torch.Tensor:
        pass  # TODO: implement


@pytest.fixture
def stub_transformers(monkeypatch: pytest.MonkeyPatch) -> None:
    pass  # TODO: implement


def _make_handler(**setup_kwargs: Any) -> WhisperSTTHandler:
    pass  # TODO: implement


def test_setup_does_not_mutate_the_shared_default(stub_transformers: None) -> None:
    pass  # TODO: implement




@pytest.mark.parametrize("language", [None, "auto", "AUTO", " Auto "])
def test_language_does_not_leak_into_a_later_handler(stub_transformers: None, language: str | None) -> None:
    pass  # TODO: implement




def test_handlers_do_not_share_one_gen_kwargs_dict(stub_transformers: None) -> None:
    pass  # TODO: implement



def test_caller_supplied_gen_kwargs_is_left_alone(stub_transformers: None) -> None:
    pass  # TODO: implement




def test_explicit_gen_kwargs_still_carries_the_language(stub_transformers: None) -> None:
    pass  # TODO: implement



@pytest.mark.parametrize("language", ["auto", "AUTO", " Auto "])
def test_auto_language_is_not_written_into_gen_kwargs(stub_transformers: None, language: str) -> None:
    pass  # TODO: implement

