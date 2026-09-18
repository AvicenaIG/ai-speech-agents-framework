"""Upload committed evaluation source to a private Docker Space for image builds.


The Space builds and hosts the container image for `hf jobs run`; it does not
run evaluations or need a long-running app. A storage bucket can hold files but
does not provide the Docker build and image-registry workflow.

Commit source changes before uploading. Run the built image using `hf jobs run`.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from huggingface_hub import HfApi

ROOT = Path(__file__).resolve().parents[1]


def prepare(destination: Path) -> str:
    pass  # TODO: implement


def main() -> None:
    pass  # TODO: implement


if __name__ == "__main__":
