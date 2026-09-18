// @ts-check
/**

import { readTurnLatency } from "./turn-latency.js";
import { extractResponseTranscript, trimTrailingSlash } from "./ws/codec.js";
import { OrbVisualiser, VIS_FFT_SIZE } from "./ws/orb-visualizer.js";
import { SentAudioRecorder } from "./ws/user-audio-recorder.js";
import { LocalVad } from "./ws/local-vad.js";

export const AUDIO_SAMPLE_RATE = 24_000;
export const AUDIO_WORKLET_VERSION = "audio-24k-v2";
export const DEFAULT_PLAYBACK_BUFFER_MS = 0;
const MIC_CHUNK_MS = 40;
const CAPTURE_CONFIG_TIMEOUT_MS = 2_000;
const SPEAKING_OPEN_DB = -50;
const SPEAKING_HANG_MS = 250;

/** @param {unknown} value */
export function normalizePlaybackBufferMs(value) {
}

/** @param {string} name @param {URL} base */
export function versionedAudioWorkletUrl(name, base) {
}

/** @param {string} message @param {string} code @param {object} [extra] */
function codedError(message, code, extra) {
    pass  # TODO: implement
}

function sdk() {
    pass  # TODO: implement
}

export class S2sRealtimeClient extends EventTarget {











































}
