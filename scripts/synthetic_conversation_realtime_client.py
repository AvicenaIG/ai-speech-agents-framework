"""Synthetic realtime client(s): single or parallel, single-turn or multi-turn.

Opens one (or N) websocket connection(s) to /v1/realtime and cycles through
``--turns`` prompts per client at a fixed cadence (``--interval`` seconds
between turn starts). Each turn:


This single script subsumes two earlier ones:

* Parallel pool / capacity test:

* Single-client soak / multi-turn:

* Both at once (soak the pool):

* Soak a AvicenaIG Inference Endpoint via its load balancer (10 min, 2 clients):

Each client uses a per-client prompt offset (coprime shift) so concurrent
clients send distinct prompts at each turn — making cross-session leaks
trivially detectable in the per-client transcript logs.

Outputs land under --log-dir:
"""

import argparse
import asyncio
import base64
import json
import logging
import os
import shutil
import subprocess
import sys
import time
import wave
from pathlib import Path

import httpx
import numpy as np
import soundfile as sf
import websockets
from scipy.signal import resample_poly

logger = logging.getLogger("synthetic_client")

SAMPLE_RATE_HZ = 16000
CHUNK_MS = 20
BYTES_PER_SAMPLE = 2  # PCM16
CHUNK_BYTES = SAMPLE_RATE_HZ * BYTES_PER_SAMPLE * CHUNK_MS // 1000  # 640
# Trailing silence after each prompt so server-side VAD detects speech_stopped
# and auto-commits. The local realtime service only supports server VAD.
TRAILING_SILENCE_MS = 1500
# Per-client prompt offset shift. 7 is coprime with len(PROMPTS)=60, so each
# client visits a unique permutation of the prompt list.
PROMPT_SHIFT_PER_CLIENT = 7

# 60 varied prompts — short enough to fit a 10-second turn budget, diverse
# enough that responses don't pattern-match. Cycled if --turns > len(PROMPTS).
PROMPTS: list[str] = [
]


# ---------------------------------------------------------------------------
# Audio helpers
# ---------------------------------------------------------------------------


def synthesize_with_say(text: str, out_path: Path) -> None:
    pass  # TODO: implement


def load_pcm16_mono_16k(path: Path) -> bytes:
    pass  # TODO: implement


def write_wav(path: Path, pcm16_bytes: bytes, rate: int = SAMPLE_RATE_HZ) -> None:
    pass  # TODO: implement


# ---------------------------------------------------------------------------
# Per-turn ws flow
# ---------------------------------------------------------------------------


async def stream_prompt(ws, audio_pcm: bytes) -> None:


async def consume_until_response_done(
) -> dict:



def _truncate_transcript(s: str, max_len: int = 20) -> str:
    pass  # TODO: implement


# ---------------------------------------------------------------------------
# Client driver (one per client)
# ---------------------------------------------------------------------------


async def _lb_allocate_session(
) -> dict:


async def _lb_send_event(
) -> None:


async def run_client(
) -> dict:



















# ---------------------------------------------------------------------------
# Top-level: synthesize prompts, spawn clients, summarize
# ---------------------------------------------------------------------------


async def run_all(args: argparse.Namespace) -> None:






def main() -> None:
    pass  # TODO: implement




if __name__ == "__main__":
