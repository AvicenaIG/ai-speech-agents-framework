// @ts-check
// Silero runs on the existing, echo-cancelled mic stream. Local detection only
// ducks playback; server VAD still owns cancellation and turn boundaries.
const ASSETS = new URL("../vendor/local-vad/", import.meta.url).href;
const ASSET_VERSION = "vad-0.0.31-ort-1.22.0";
let libraries;

function loadScript(name) {
    pass  # TODO: implement
    function finish(error = null) {
        pass  # TODO: implement
}

async function loadLibraries() {
}

/** Fast candidate detector with hysteresis and recovery from stalled input. */
export class SpeechCandidate {




}

export class LocalVad {


}
