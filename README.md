# ai-speech-agents-framework

<div align="center">

**Open-source framework for building low-latency AI voice agents with streaming ai-speech-agents-framework pipelines.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()

</div>

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#license)
- [License](#license)

## Features

- **Stream** real-time ai-speech-agents-framework conversations through a LiveKit voice agent (`Assistant` in `demo/livekit/agent.py`) that connects to a realtime session backend.
- **Control access** to your demo deployment with tiered identity resolution and OAuth gating — `resolve_identity`, `resolve_tier`, `oauth_login_required_reason`, and anonymous cookie issuance (`set_anon_cookie`) in `demo/auth.py`.
- **Meter usage budgets** per user with a SQLite-backed limiter: daily budgets (`budget_for`), session lifecycle accounting (`begin`, `heartbeat`, `end`), search-quota enforcement (`take_search`), and stale-session cleanup (`sweep`).
- **Swap speech backends** with pluggable STT/TTS handlers, including `MoonshineSTTHandler`, `MeloTTSHandler`, and `ParlerTTSHandler` with their matching `arguments_classes` for typed configuration.
- **Extend the agent with tools** — the demo client manages tool definitions (`activeToolDefs`, `pushToolsToSession`, `loadTools`) and reference examples wire a web search tool into a realtime session (`examples/realtime_web_search_tool.py`).
- **Benchmark models** with ready-made scripts for speech pipelines: `scripts/benchmark_stt.py` and `scripts/benchmark_tts.py`.

## Installation

```bash
git clone https://github.com/AvicenaIG/ai-speech-agents-framework.git
cd ai-speech-agents-framework

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Quick Start

Launch the demo server, which serves the web-based voice agent client:

```bash
python demo/server.py
```

Open the served page in your browser and start speaking. The client (`demo/main.js`) handles microphone capture via audio worklets (`demo/worklets/mic-capture.js`, `demo/worklets/audio-playback.js`), live audio-level visualization (`demo/ws/orb-visualizer.js`), and local VAD (`demo/ws/local-vad.js`), while `demo/auth.py` resolves your identity tier and `demo/limiter.py` tracks your session budget as you converse with the agent.

## Usage

### 1. Benchmark speech models

Measure latency and throughput of your speech pipeline components before deploying an agent:

```bash
python scripts/benchmark_stt.py   # speech recognition benchmarks
python scripts/benchmark_tts.py   # speech synthesis benchmarks
```

Use the results to choose between alternative handlers — for example, the archived `MoonshineSTTHandler` for on-device speech recognition, or `ParlerTTSHandler` / `MeloTTSHandler` for speech synthesis.

### 2. Connect a tool-augmented realtime agent

The demo client lets you attach tool definitions to a live session (`pushToolsToSession`, `saveTools`) so the LLM behind your voice agent can call them mid-conversation. A reference implementation of a web search tool for realtime sessions lives in `examples/realtime_web_search_tool.py` — a common pattern for giving voice agents fresh knowledge beyond their training data.

The client also supports direct WebSocket connections (`buildDirectWsUrl`) and resumable audio sessions (`createResumedAudioContext`) for robust agent sessions.

## Configuration

| Option | Type | Default | Description |
|---|---|---|---|
| `GITHUB_TOKEN` | `str` | unset | GitHub API token used by `.github/scripts/star_history.py` to fetch stargazer history via the GraphQL API and render an SVG chart. |

The demo limiter resolves its SQLite database path automatically (`_resolve_db_path` in `demo/limiter.py`); daily usage budgets and search quotas are enforced per identity resolved by `demo/auth.py`.

## Contributing

Contributions are welcome — whether new STT/TTS handlers, additional tool examples, or improvements to the demo client. Please open an issue describing your proposed change before submitting a pull request, and keep new code consistent with the existing module layout under `demo/`, `scripts/`, and `examples/`.

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

Copyright © 2026 ai-speech-agents-framework contributors