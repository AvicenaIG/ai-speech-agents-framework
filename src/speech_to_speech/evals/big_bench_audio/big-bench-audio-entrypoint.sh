#!/usr/bin/env bash
# All evaluation options use environment variables; quoted values use shlex in Python.
set -euo pipefail
export S2S_SOURCE_REVISION="$(cat /opt/source-revision.txt)"
exec python -m ai_speech_agents_framework.evals.big_bench_audio.job
