"""JSON extension for avatar/robot clients; standard audio events stay intact."""

from typing import Literal

from pydantic import BaseModel

from ai_speech_agents_framework.pipeline.visemes import Viseme


class SpeechToSpeechVisemesEvent(BaseModel):
    type: Literal["ai_speech_agents_framework.output_audio.visemes"] = "ai_speech_agents_framework.output_audio.visemes"
    event_id: str
    response_id: str
    item_id: str
    output_index: int
    content_index: int = 0
    visemes: list[Viseme]
