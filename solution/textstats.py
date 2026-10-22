"""Reference solution. Students never see this folder."""
import math
import re
from collections import Counter

_WORD = re.compile(r"[A-Za-z0-9']+")
_SENTENCE_END = re.compile(r"[.!?]+")


def _words(text: str) -> list[str]:
    return [w.lower() for w in _WORD.findall(text or "") if w.strip("'")]


def count_words(text: str) -> int:
    return len(_words(text))


def count_sentences(text: str) -> int:
    parts = _SENTENCE_END.split(text or "")
    return sum(1 for p in parts if _words(p))


def reading_time_minutes(text: str, words_per_minute: int = 200) -> int:
    words = count_words(text)
    if words == 0:
        return 0
    return max(1, math.ceil(words / words_per_minute))


def top_words(text: str, n: int = 3, ignore: set[str] | None = None) -> list[tuple[str, int]]:
    skip = {w.lower() for w in (ignore or set())}
    counts = Counter(w for w in _words(text) if w not in skip)
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
