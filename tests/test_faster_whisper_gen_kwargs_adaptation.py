"""`adapt_gen_kwargs` must translate its argument without consuming it.

It maps the pipeline's `return_timestamps` onto faster-whisper's inverse
`without_timestamps`. Popping the source key out of the caller's dict makes the
translation single-use: the second handler built from the same config reads the
default instead of the supplied value, and the setting silently inverts.
"""

from typing import Any

import pytest

faster_whisper = pytest.importorskip("faster_whisper")

from ai_speech_agents_framework.STT.faster_whisper_handler import FasterWhisperSTTHandler  # noqa: E402


@pytest.fixture
def handler() -> FasterWhisperSTTHandler:
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_return_timestamps_is_inverted(
    pass  # TODO: implement
) -> None:



def test_default_is_timestamps_on(handler: FasterWhisperSTTHandler) -> None:
    pass  # TODO: implement


def test_caller_dict_is_not_consumed(handler: FasterWhisperSTTHandler) -> None:
    pass  # TODO: implement




def test_one_config_reused_gives_both_handlers_the_same_setting(
    pass  # TODO: implement
) -> None:




def test_shared_setup_default_is_not_polluted(handler: FasterWhisperSTTHandler) -> None:
    pass  # TODO: implement




def test_other_kwargs_pass_through(handler: FasterWhisperSTTHandler) -> None:
    pass  # TODO: implement

