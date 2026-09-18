"""Persian normalization adapted from mallahyari/pocket-tts.

Source: training/farsi/normalize_fa.py at 3807c204babb5fe54be8fe18a362a58315e870d6.
Only inference normalization is included.

Permission is hereby granted, free of charge, to any
person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the
Software without restriction, including without
limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice
shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import re
import unicodedata

ZWNJ = "‌"

# The 32 letters of the Persian alphabet, in the spelling the aligner expects.
PERSIAN_LETTERS = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی" + "ئ"
# Exactly the alphabet of m3hrdadfi/wav2vec2-large-xlsr-persian-v3 (and of
# SLPL/Sharif-wav2vec2 and masoudmzb/wav2vec2-xlsr-multilingual-53-fa).
ALIGNER_ALPHABET = set(PERSIAN_LETTERS + ZWNJ)

# Punctuation kept in the transcript: it carries prosody (pauses, question
# intonation) and the tokenizer learns it. Everything else is dropped.
KEPT_PUNCT = ".،؛؟!:"

ALLOWED = ALIGNER_ALPHABET | set(KEPT_PUNCT) | {" "}

# Letter-form folding. Arabic codepoints that look identical to Persian ones
# but are a different character to every downstream model.
CHAR_MAP: dict[str, str | int | None] = {
}
# Harakat, tashdid, sukun, superscript alef, hamza-above/below combining marks.
DIACRITICS = re.compile(r"[ً-ٰٕۖ-ۭٖ-ٟ]")
# Bidi controls, BOM, and every zero-width mark EXCEPT U+200C.
INVISIBLES = re.compile(r"[​‍‎‏‪-‮⁦-⁩﻿­]")

DIGIT_MAP: dict[str, str | int | None] = {chr(0x06F0 + i): str(i) for i in range(10)}  # ۰-۹
DIGIT_MAP.update({chr(0x0660 + i): str(i) for i in range(10)})  # ٠-٩

PUNCT_MAP: dict[str, str | int | None] = {
}


# ---------------------------------------------------------------------------
# Numbers
# ---------------------------------------------------------------------------

_ONES = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
_TEENS = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
_TENS = ["", "", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
_HUNDREDS = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
_SCALES = [(10**12, "تریلیون"), (10**9, "میلیارد"), (10**6, "میلیون"), (10**3, "هزار")]
_FRACTION_UNITS = {1: "دهم", 2: "صدم", 3: "هزارم"}
_JOIN = " و "
# Above this many digits a run is read one digit at a time (phone numbers,
# account numbers, timestamps), which is what a speaker actually does.
MAX_NUMBER_DIGITS = 12


def _under_thousand(n: int) -> str:
    pass  # TODO: implement


def number_to_words(n: int) -> str:
    pass  # TODO: implement


def _digits_one_by_one(digits: str) -> str:
    pass  # TODO: implement


def _number_token_to_words(match: re.Match) -> str:
    pass  # TODO: implement


# A sign belongs to a number at a token boundary, not to a range like 5-10.
_NUMBER_RE = re.compile(r"((?<!\w)[−-])?(\d+)(?:[.](\d+))?")


def numbers_to_words(text: str) -> str:
    pass  # TODO: implement


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------


def normalize(text: str, *, spell_numbers: bool = True) -> str:
    pass  # TODO: implement

