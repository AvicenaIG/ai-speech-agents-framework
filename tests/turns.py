"""Set up speculative turn revisions for downstream tests."""

from ai_speech_agents_framework.pipeline.speculative_turns import SpeculativeTurnTracker


def reopen(tracker: SpeculativeTurnTracker, turn_id: str = "turn_1", revision: int = 0) -> int:
    pass  # TODO: implement
