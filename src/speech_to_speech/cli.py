from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from typing import Any, Literal

from ai_speech_agents_framework.api.openai_realtime.audio_client import (
)
from ai_speech_agents_framework.pipeline.transcript_logging import (
)

Command = Literal["serve", "talk", "local"]

_LEGACY_MODE_COMMANDS: dict[str, Command] = {
}


def _command_parser() -> argparse.ArgumentParser:
    pass  # TODO: implement


def _extract_legacy_mode(command_args: list[str], parser: argparse.ArgumentParser) -> tuple[str | None, list[str]]:
    pass  # TODO: implement



def parse_command(argv: Sequence[str] | None = None) -> tuple[Command, list[str]]:
    pass  # TODO: implement



def parse_talk_arguments(argv: Sequence[str]) -> RealtimeAudioClientConfig:
    pass  # TODO: implement



def _run_file_command(command: Command, command_args: list[str]) -> None:
    pass  # TODO: implement




def main() -> None:
    pass  # TODO: implement




if __name__ == "__main__":
