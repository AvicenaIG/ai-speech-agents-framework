// @ts-check
/**

const DEFAULT_TARGET_RATE = 24000;
const DEFAULT_CHUNK_MS = 40;
// Gate envelope timing (fixed; only the threshold is user-tunable).
const GATE_ATTACK_MS = 5; // open almost instantly so word onsets survive
const GATE_HOLD_MS = 250; // stay open this long after the level drops back under
const GATE_RELEASE_MS = 80; // then fade closed over this long (no click)

class MicCaptureProcessor extends AudioWorkletProcessor {
    pass  # TODO: implement










}

registerProcessor("mic-capture", MicCaptureProcessor);
