import logging
from queue import Queue
from threading import Event

from ai_speech_agents_framework.pipeline.events import (
)
from ai_speech_agents_framework.pipeline.messages import (
)
from ai_speech_agents_framework.STT.transcription_notifier import TranscriptionNotifier


def _notifier(
    pass  # TODO: implement
) -> TranscriptionNotifier:


def test_empty_final_transcription_still_emits_completion_after_partial():
    pass  # TODO: implement





def test_non_empty_final_transcription_logs_metadata_without_content(caplog):
    pass  # TODO: implement





def test_empty_final_transcription_reenables_listening_without_runtime_config():
    pass  # TODO: implement




def test_transcription_failure_defers_listening_change_to_realtime_owner():
    pass  # TODO: implement




def test_diarization_status_logs_without_transcript(caplog):
    pass  # TODO: implement



def test_no_diarization_status_when_disabled(caplog):
    pass  # TODO: implement


def test_speaker_durations_include_brief_and_simultaneous_activity():
    pass  # TODO: implement

