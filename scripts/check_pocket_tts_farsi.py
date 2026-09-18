"""Run the Pocket TTS Farsi handler with real weights and save WAVs for listening.

Requires the Pocket TTS fork documented in README.md. Downloads both models and
the reference recording on first use. This checks synthesis, not pronunciation.
"""

import argparse
import json
from pathlib import Path
from queue import Queue
from threading import Event
from time import perf_counter

import numpy as np
import torch
from scipy.io import wavfile

from ai_speech_agents_framework.pipeline.messages import AUDIO_RESPONSE_DONE, EndOfResponse, TTSInput
from ai_speech_agents_framework.TTS.pocket_tts_handler import PocketTTSHandler

MODEL = "mehdi-hf/pocket-tts-farsi-v2"
REFERENCE = f"hf://{MODEL}/samples/prompt_short_sentence.wav"
CASES = {
}


def main() -> None:
    pass  # TODO: implement



if __name__ == "__main__":
