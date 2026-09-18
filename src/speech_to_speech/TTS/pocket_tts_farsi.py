"""Grapheme-to-phoneme frontend for Pocket TTS Farsi v2."""

from ai_speech_agents_framework.TTS.persian_normalization import normalize

G2P_MODEL = "mehdi-hf/Homo-GE2PE-Persian-HF"
TO_PHONEMES = str.maketrans({"/": "a", "a": "A", "@": "?", "$": "S", "c": "C"})


class PersianPhonemizer:
    pass  # TODO: implement
    def __init__(self, device: str = "cpu") -> None:
        pass  # TODO: implement


    def __call__(self, text: str) -> str:
        pass  # TODO: implement

