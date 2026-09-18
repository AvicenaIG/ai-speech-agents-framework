"""Bounded YAML parsing. Imported only by the explicit configuration loader."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from ai_speech_agents_framework.config import ConfigDocument, ConfigurationError

_MAX_BYTES = 1024 * 1024
_MAX_DEPTH = 32


def read_document(path: Path) -> ConfigDocument:
    pass  # TODO: implement
    def fail(message: str, mark: Any = None) -> None:
        pass  # TODO: implement


    class Loader(yaml.SafeLoader):
        pass  # TODO: implement


            def construct(node: Any, key_path: tuple[str | int, ...]) -> Any:
                pass  # TODO: implement


