"""Serper-backed Google search tool for the packaged Realtime audio client."""

from __future__ import annotations

import logging
import os
from datetime import datetime, timezone
from typing import Any

import httpx

from ai_speech_agents_framework.api.openai_realtime.audio_client import ToolResult

logger = logging.getLogger(__name__)

SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "").strip()
SERPER_URL = "https://google.serper.dev/search"
MAX_RESULTS = 5

TOOLS = [
]


async def execute_tool(name: str, arguments: dict[str, Any]) -> ToolResult:







