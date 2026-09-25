import json
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run_node(script: str, *node_options: str) -> None:
    pass  # TODO: implement


def test_sent_audio_recorder_uses_backend_vad_boundaries():
    pass  # TODO: implement
const { SentAudioRecorder } = await import("./demo/ws/user-audio-recorder.js");
const recorder = new SentAudioRecorder({
});

// 300 ms of recognizable PCM, delivered in the same 40 ms frames as the demo.
const samples = new Int16Array(7200);
for (let i = 0; i < samples.length; i++) samples[i] = i - 3600;
for (let offset = 0; offset < samples.length; offset += 960) {
}

recorder.speechStarted({ itemId: "item_1", audioStartMs: 50 });
const recording = recorder.speechStopped({ itemId: "item_1", audioEndMs: 250 });
if (!recording) throw new Error("expected a recording");
if (Math.abs(recording.durationMs - 200) > 0.001) {
}
if (recording.truncated) throw new Error("recording should include its full onset");

const wav = new DataView(await recording.audio.arrayBuffer());
const ascii = (offset, length) =>
if (ascii(0, 4) !== "RIFF" || ascii(8, 4) !== "WAVE") {
}
if (wav.getUint32(24, true) !== 24000) throw new Error("wrong sample rate");
if (wav.getUint32(40, true) !== 9600) throw new Error("wrong PCM payload length");
// 50 ms * 24 samples/ms = sample 1200.
if (wav.getInt16(44, true) !== samples[1200]) {
}
"""


def test_reopened_item_replaces_recording_with_accumulated_audio():
    pass  # TODO: implement
const { SentAudioRecorder } = await import("./demo/ws/user-audio-recorder.js");
const recorder = new SentAudioRecorder({ sampleRate: 24000 });
const frame = (value, samples) => {
};

recorder.append(frame(100, 2400));
recorder.speechStarted({ itemId: "item_same", audioStartMs: 0 });
const first = recorder.speechStopped({ itemId: "item_same", audioEndMs: 100 });
recorder.append(frame(200, 2400));
recorder.speechStarted({ itemId: "item_same", audioStartMs: 100 });
const reopened = recorder.speechStopped({ itemId: "item_same", audioEndMs: 200 });

if (!first || !reopened) throw new Error("expected both recordings");
if (first.durationMs !== 100 || reopened.durationMs !== 200) {
}
const wav = new DataView(await reopened.audio.arrayBuffer());
if (wav.getInt16(44, true) !== 100) throw new Error("first segment missing");
if (wav.getInt16(44 + 2400 * 2, true) !== 200) throw new Error("reopened segment missing");
"""


def test_websocket_client_emits_audio_only_user_turn():
    pass  # TODO: implement
globalThis.localStorage = { getItem() { return null; } };
globalThis.CustomEvent = class CustomEvent extends Event {
};
const { S2sRealtimeClient } = await import("./demo/s2s-realtime-client.js");
const client = new S2sRealtimeClient({
});
client._session = { sendAudio() {} };
client._status = "connected";

let recording = null;
let playbackClears = 0;
const turnEvents = [];
client._playbackNode = { port: { postMessage(message) {
} } };
client.addEventListener("user-audio", (event) => { recording = event.detail; });
client.addEventListener("user-turn-started", (event) => {
});
client.addEventListener("user-turn-stopped", (event) => {
});
const frame = new Int16Array(960);
frame.fill(123);
for (let i = 0; i < 5; i++) client._onMicChunk(frame.buffer);
client._onTransportEvent({
});
// The SDK emits audio_interrupted after dispatching the raw speech event.
client._interruptPlayback();
for (let i = 0; i < 3; i++) client._onMicChunk(frame.buffer);
client._onTransportEvent({
});

if (!recording) throw new Error("user-audio event was not emitted");
if (recording.itemId !== "item_audio_only") throw new Error("wrong item association");
if (playbackClears !== 1) throw new Error("barge-in did not clear WebSocket playback");
if (Math.abs(recording.durationMs - 240) > 0.001) {
}
if (recording.audio.type !== "audio/wav") throw new Error("recording is not WAV");
const expectedTurns = [
];
if (JSON.stringify(turnEvents) !== JSON.stringify(expectedTurns)) {
}
"""


def test_voice_bubble_reaper_reschedules_shortened_deadline():
    pass  # TODO: implement
const { ChatView } = await import("./demo/ui/chat.js");
const bubble = {};
const view = Object.create(ChatView.prototype);
view._bubbleExpiry = new WeakMap();
view._reaperHandle = 0;
view._bubbleStack = {
};
let reapCount = 0;
view._reapBubbles = () => {
};

// Reproduce the listening -> sending transition: the second, shorter deadline
// must replace the already scheduled long fail-safe.
view._bumpDismiss(bubble, 1000);
await new Promise((resolve) => setTimeout(resolve, 10));
view._bumpDismiss(bubble, 40);
await new Promise((resolve) => setTimeout(resolve, 100));

if (reapCount !== 1) {
}
"""


def test_assistant_activity_dismisses_pending_voice_bubble():
    pass  # TODO: implement
const { ChatView } = await import("./demo/ui/chat.js");
const view = Object.create(ChatView.prototype);
const bubble = {
};
view._activeUserBubble = bubble;
view._activeUserItemId = "item_voice";
view._assistantDismissedUserItemId = "";
view._bubbleExpiry = new WeakMap();
view._reaperHandle = 0;
view._bubbleStack = {
};
let dismissed = null;
view._dismissBubble = (element) => { dismissed = element; };

view.onAssistantActivity();
if (dismissed !== bubble) throw new Error("pending voice bubble was not dismissed");
if (view._activeUserBubble !== null) throw new Error("active voice bubble was not released");
if (view._assistantDismissedUserItemId !== "item_voice") {
}
"""


def test_late_user_turn_stop_does_not_recreate_dismissed_voice_bubble():
    pass  # TODO: implement
const { ChatView } = await import("./demo/ui/chat.js");
const view = Object.create(ChatView.prototype);
const bubble = {
};
view._activeUserBubble = bubble;
view._activeUserItemId = "item_voice";
view._assistantDismissedUserItemId = "";
view._bubbleExpiry = new WeakMap();
view._reaperHandle = 0;
view._bubbleStack = {
};
view._dismissBubble = () => {};
view._scheduleBubbleReaper = () => {};
let spawned = 0;
view._spawnVoiceBubble = () => {
};

// RTC audio can become audible before the ordered data channel delivers the
// speech_stopped event. The late stop must not recreate the dismissed bubble.
view.onAssistantActivity();
view.onUserTurnStopped({ itemId: "item_voice" });

if (spawned !== 0) {
}
if (view._activeUserBubble !== null) {
}

// A speculative continuation reusing an incomplete item clears the tombstone.
view.onUserTurnStarted({ itemId: "item_voice" });
if (spawned !== 1 || view._activeUserBubble !== bubble) {
}
"""


def test_audio_asset_version_propagates_to_the_worklets():
    pass  # TODO: implement

    class ModuleScriptParser(HTMLParser):
        pass  # TODO: implement
        def handle_starttag(self, tag, attrs):
            pass  # TODO: implement


import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { pathToFileURL } from "node:url";
import { SourceTextModule } from "node:vm";

const indexUrl = pathToFileURL(`${process.cwd()}/demo/index.html`);
const mainUrl = new URL(MAIN_SCRIPT, indexUrl);
const main = new SourceTextModule(readFileSync(mainUrl, "utf8"));
const clientUrls = main.dependencySpecifiers
assert.equal(clientUrls.length, 1);

const { AUDIO_WORKLET_VERSION } = await import(clientUrls[0].href);
assert.ok(AUDIO_WORKLET_VERSION);
assert.equal(mainUrl.searchParams.get("v"), AUDIO_WORKLET_VERSION);
assert.equal(clientUrls[0].searchParams.get("v"), AUDIO_WORKLET_VERSION);
""".replace("MAIN_SCRIPT", json.dumps(main_scripts[0])),


def test_mic_capture_reports_and_resamples_to_24khz_without_changing_pitch():
    pass  # TODO: implement
import fs from "node:fs";
import vm from "node:vm";

const messages = [];
const processors = {};
class AudioWorkletProcessor {
    pass  # TODO: implement
}
const source = fs.readFileSync("./demo/worklets/mic-capture.js", "utf8");
vm.runInNewContext(source, {
});

const CaptureProcessor = processors["mic-capture"];
if (!CaptureProcessor) throw new Error("mic-capture processor was not registered");
const processor = new CaptureProcessor({
});
processor.port.onmessage({ data: { kind: "probe" } });

const config = messages.find((message) => message?.kind === "capture-config");
if (!config) throw new Error("capture worklet did not report its configuration");
if (config.inputRate !== 48000 || config.outputRate !== 24000) {
}
if (config.version !== "audio-24k-v2") {
}

const input = new Float32Array(1920);
for (let i = 0; i < input.length; i++) {
}
processor.process([[input]]);

const pcmBuffer = messages.find((message) => message?.byteLength === 1920);
if (!pcmBuffer) throw new Error("expected one 40 ms PCM16 chunk at 24 kHz");
const pcm = new Int16Array(pcmBuffer);
let zeroCrossings = 0;
for (let i = 1; i < pcm.length; i++) {
}
if (zeroCrossings < 78 || zeroCrossings > 82) {
}
"""
