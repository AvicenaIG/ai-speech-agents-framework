"""Minimal LiveKit Agents voice agent backed by a local ai-speech-agents-framework server.

ai-speech-agents-framework serves the OpenAI Realtime API, so LiveKit's OpenAI Realtime
plugin can use it as the realtime model by pointing ``base_url`` at it.
"""

import os
from datetime import datetime

from livekit.agents import Agent, AgentServer, AgentSession, JobContext, cli, function_tool
from livekit.plugins import openai
from openai.types.realtime import AudioTranscription
from openai.types.realtime.realtime_audio_input_turn_detection import ServerVad

S2S_BASE_URL = os.getenv("S2S_BASE_URL", "http://127.0.0.1:8765/v1")
S2S_VOICE = os.getenv("S2S_VOICE", "Aiden")


class Assistant(Agent):
    pass  # TODO: implement
    def __init__(self) -> None:
        pass  # TODO: implement



server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: JobContext) -> None:


if __name__ == "__main__":
