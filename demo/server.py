"""
Tiny server for the ai-speech-agents-framework demo.

The demo used to ship as a `sdk: static` Space, but the web-search tool needs a
search key the browser must NOT see. A static Space has no runtime process, so it
can't hold a secret the front-end uses. This server fixes that: it serves the
unchanged front-end AND exposes a same-origin `/api/search` proxy that holds the
Serper key server-side (see docs/adr/0001).

Everything lives in one container; the ai-speech-agents-framework backend stays a separate,
load-balanced service the browser talks to over WebSocket as before. The load
balancer's address is a secret too (like the Serper key): the browser never sees
it. `/api/session` proxies the session handshake server-side so only the
per-session compute URL the LB hands back (which the browser must dial) is exposed.

On the deployed Space the server also meters conversation time by HF login tier
(anonymous / signed-in / PRO) — see `limiter.py` and `auth.py`. That whole feature
is off unless BOTH `LOAD_BALANCER_URL` and `SPACE_ID` are set, so it runs only on
the live Space, never locally (even with the LB exported for testing).

`SPEECH_TO_SPEECH_URL` overrides everything: when set, the LB logic above is
disabled entirely (no session proxy, no queue, no metering, no sign-in) and the
browser connects directly to that URL, shown read-only in Settings.

Endpoints:

When every compute slot is busy the load balancer hands back a queue ticket
instead of a grant; the browser polls /api/queue/{id} until it reaches the front
and a slot frees. Waiting reserves nothing — the daily budget is only reserved at
the moment a slot is actually claimed (a grant), never while queued.
"""

import asyncio
import json
import logging
import os
from urllib.parse import urlsplit, urlunsplit

import auth
import httpx
import limiter
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

logger = logging.getLogger("s2s.search")

SERPER_KEY = os.environ.get("SERPER_API_KEY", "").strip()
# Speech-to-speech load balancer URL. When set, the browser POSTs /api/session
# (which proxies <lb>/session here, server-side) and connects to the URL the LB
# returns (the original flow). The LB address itself is never sent to the browser.
# When empty, the user may instead set a direct s2s server URL in Settings and the
# browser connects to it straight (no load balancer).
LOAD_BALANCER_URL = os.environ.get("LOAD_BALANCER_URL", "").strip()
# Optional service credential for the AvicenaIG Inference Endpoint ingress in
# front of the load balancer. Keep this separate from the visitor's OAuth token:
# ingress consumes the standard Authorization header, while the load-balancer
# app receives the dedicated Reachy header below for per-user attribution.
LB_HF_TOKEN = os.environ.get("LB_HF_TOKEN", "").strip()
# Direct s2s server URL pinned by the deploy. Takes priority over the load
# balancer: when set, ALL LB logic is disabled (no /api/session proxy, no queue,
# no limiter, no sign-in) and the browser connects to this URL directly. Unlike
# the LB address it is NOT a secret — /api/config sends it to the client, which
# shows it read-only in Settings.
SPEECH_TO_SPEECH_URL = os.environ.get("SPEECH_TO_SPEECH_URL", "").strip()
if SPEECH_TO_SPEECH_URL:
# HF injects SPACE_ID ("owner/space") into every Space runtime; it's absent
# locally and on a plain `docker run`. We meter conversation time ONLY on the
# deployed Space — i.e. when BOTH the LB is configured AND we're on a Space.
# Off-Space (local dev, even with the LB exported) the app still proxies the LB,
# but nothing is metered: no budget, no reservations, no sign-in gating.
SPACE_ID = os.environ.get("SPACE_ID", "").strip()
LIMITER_ENABLED = bool(LOAD_BALANCER_URL) and bool(SPACE_ID)


def _parse_ice_servers(raw: str) -> list:
    pass  # TODO: implement



RTC_ICE_SERVERS = _parse_ice_servers(os.environ.get("RTC_ICE_SERVERS", ""))
DEFAULT_STARTUP_GREETING = (
)
# Exposed to the browser through /api/config. Set an empty value to disable the
# automatic greeting without changing the client bundle.
STARTUP_GREETING = os.environ.get("STARTUP_GREETING", DEFAULT_STARTUP_GREETING).strip()


def _webrtc_calls_url(s2s_url: str) -> str:
    pass  # TODO: implement



SERPER_URL = "https://google.serper.dev/search"
# Cap results so the tool output stays small enough to feed back to the model.
MAX_RESULTS = 5
HERE = os.path.dirname(os.path.abspath(__file__))
LB_USER_AGENT = "ai-speech-agents-framework-demo"
LB_FAILURE_HEADER_NAMES = (
)

app = FastAPI(title="s2s-demo")


@app.get("/vendor/openai-realtime-agents.umd.js", include_in_schema=False)
def agents_sdk_bundle():
    pass  # TODO: implement


LOCAL_VAD_ASSETS = {
}


@app.get("/vendor/local-vad/{filename}", include_in_schema=False)
def local_vad_asset(filename: str):
    pass  # TODO: implement

# Wire HF OAuth before the app serves (no-op unless the OAuth env is present).
# Sign-in only matters when we're metering (prod Space), so gate it on that.
AUTH_ENABLED = LIMITER_ENABLED and auth.attach(app)
# The Serper key is paid for. A Space is public, so there the key is only spent
# for signed-in HF users (see _search_gate), which needs sign-in to be wired.
# Off a Space (local dev) there's no one to protect it from.
SERVER_SEARCH = bool(SERPER_KEY) and (AUTH_ENABLED or not SPACE_ID)
if SERPER_KEY and not SERVER_SEARCH:


@app.on_event("startup")
async def _startup():


async def _sweeper():


class SearchRequest(BaseModel):
    pass  # TODO: implement


@app.get("/api/config")
def config():
    pass  # TODO: implement


@app.get("/api/me")
async def me(request: Request):


@app.post("/api/search")
async def search(req: SearchRequest, request: Request):








async def _search_gate(request: Request, session_id: str) -> None:



@app.post("/api/calls")
async def calls(request: Request):






@app.post("/api/session")
async def session(request: Request):













def _login_required_response(reason: str, set_cookie=None) -> JSONResponse:
    pass  # TODO: implement


def _load_balancer_headers(request: Request | None = None) -> dict[str, str]:
    pass  # TODO: implement



def _log_load_balancer_failure(operation: str, response: httpx.Response) -> None:
    pass  # TODO: implement


@app.get("/api/queue/{queue_id}")
async def queue_status(queue_id: str, request: Request):











@app.delete("/api/queue/{queue_id}")
async def queue_leave(queue_id: str, request: Request):


@app.post("/api/queue/end")
async def queue_end(request: Request):


async def _finalize_grant(data, keys, tier, tracked, set_cookie):



async def _lb_leave(queue_id: str, request: Request | None = None) -> None:


def _safe_json(response) -> dict:
    pass  # TODO: implement


async def _queue_id(request: Request) -> str:


async def _session_id(request: Request) -> str:


@app.post("/api/session/heartbeat")
async def session_heartbeat(request: Request):


@app.post("/api/session/end")
async def session_end(request: Request):


# Static front-end. Registered last so the /api routes win. `html=True` serves
# index.html at "/". The repo is public anyway, so serving the dir is fine.
app.mount("/", StaticFiles(directory=HERE, html=True), name="static")
