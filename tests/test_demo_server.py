import importlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest

DEMO_DIR = Path(__file__).resolve().parents[1] / "demo"
sys.path.insert(0, str(DEMO_DIR))
demo_auth = importlib.import_module("auth")
demo_server = importlib.import_module("server")


@pytest.mark.parametrize("filename", list(demo_server.LOCAL_VAD_ASSETS))
@pytest.mark.parametrize("bundled", [False, True])
async def test_local_vad_assets_are_served_with_browser_content_types(monkeypatch, tmp_path, filename, bundled):


async def test_local_vad_missing_assets_fail_without_exposing_other_package_files(monkeypatch, tmp_path):


def _mock_whoami(monkeypatch, payload):
    pass  # TODO: implement

    def get(url, **kwargs):
        pass  # TODO: implement



def test_resolve_tier_prefers_oauth_pro_without_hub_lookup(monkeypatch):
    pass  # TODO: implement
    def unexpected_get(*args, **kwargs):
        pass  # TODO: implement




@pytest.mark.parametrize("oauth_is_pro", [None, False])
def test_user_view_uses_token_backed_pro_status(monkeypatch, oauth_is_pro):
    pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_token_backed_non_pro_tiers_remain_unchanged(monkeypatch, whoami, expected):
    pass  # TODO: implement



def test_failed_whoami_falls_back_without_blocking_retry(monkeypatch):
    pass  # TODO: implement

    def get(url, **kwargs):
        pass  # TODO: implement




async def test_me_reuses_whoami_resolution_and_retries_next_request(monkeypatch):

    def get(url, **kwargs):
        pass  # TODO: implement







def test_tier_and_org_resolution_share_one_whoami_request(monkeypatch):
    pass  # TODO: implement



def test_current_access_token_normalizes_oauth_token(monkeypatch):
    pass  # TODO: implement



def test_current_access_token_rejects_missing_or_empty_token(monkeypatch):
    pass  # TODO: implement



def test_expiring_oauth_token_requires_fresh_login(monkeypatch):
    pass  # TODO: implement



def test_load_balancer_headers_use_user_token_for_both_hops_without_service_token(monkeypatch):
    pass  # TODO: implement



def test_load_balancer_headers_keep_service_and_user_tokens_separate(monkeypatch):
    pass  # TODO: implement



def test_load_balancer_headers_keep_anonymous_requests_credential_free(monkeypatch):
    pass  # TODO: implement




def test_load_balancer_headers_authenticate_anonymous_request_with_service_token(monkeypatch):
    pass  # TODO: implement



def test_load_balancer_failure_logs_safe_diagnostic_headers(caplog):
    pass  # TODO: implement




async def test_session_preserves_load_balancer_authentication_failure(monkeypatch):
    class FakeAsyncClient:
        pass  # TODO: implement
        def __init__(self, **kwargs):
            pass  # TODO: implement








async def test_session_rejects_locally_expired_oauth_before_proxying(monkeypatch):




async def test_queue_rejects_locally_expired_oauth_before_polling(monkeypatch):




@pytest.fixture
def space_search(monkeypatch, tmp_path):
    pass  # TODO: implement

    class FakeAsyncClient:
        pass  # TODO: implement
        def __init__(self, **kwargs):
            pass  # TODO: implement






def _as(monkeypatch, tier, keys=("k_alice",)):
    pass  # TODO: implement


async def _search(session_id=None, key=None):


async def test_search_on_space_refuses_anonymous_callers(monkeypatch, space_search):




async def test_search_on_space_refuses_expired_sign_in(monkeypatch, space_search):




@pytest.mark.parametrize("tier", ["free", "pro", "org"])
async def test_search_needs_the_callers_live_session(monkeypatch, space_search, tier):





async def test_search_needs_a_heartbeating_session(monkeypatch, space_search):




def _advance(monkeypatch, seconds):
    pass  # TODO: implement


async def test_unlimited_search_recovers_after_a_sweep(monkeypatch, space_search):





def test_sweep_still_reaps_silent_metered_sessions(monkeypatch, space_search):
    pass  # TODO: implement



async def test_unlimited_grants_are_recorded_but_never_debited(monkeypatch, space_search):




async def test_server_key_searches_are_capped_per_user_per_day(monkeypatch, space_search):




async def test_user_supplied_key_skips_the_server_key_gate(monkeypatch, space_search):




async def test_server_key_is_never_spent_without_server_search(monkeypatch, space_search):




async def test_local_search_is_not_gated(monkeypatch, space_search):




def test_websocket_client_classifies_session_401_as_login_required():
    pass  # TODO: implement

globalThis.localStorage = { getItem() { return null; } };
globalThis.fetch = async () => ({
});
const { S2sRealtimeClient } = await import("./demo/s2s-realtime-client.js");
const client = new S2sRealtimeClient({
});
try {
} catch (error) {
}
"""


def test_login_required_state_wins_over_inflight_account_refresh():
    pass  # TODO: implement

globalThis.localStorage = { getItem() { return null; } };
const elements = new Map();
function element() {
    pass  # TODO: implement
}
globalThis.document = {
};

let resolveFetch;
globalThis.fetch = () => new Promise((resolve) => { resolveFetch = resolve; });

const { Account } = await import("./demo/ui/account.js");
const account = new Account();
const refresh = account.refresh();
account.showLoginRequired("/oauth/huggingface/login");
resolveFetch({
});
await refresh;

if (account.tier !== "anon") throw new Error(`unexpected tier: ${account.tier}`);
const root = elements.get("#account");
if (!root.innerHTML.includes("signin-pill")) {
}
"""
