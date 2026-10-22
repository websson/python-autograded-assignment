"""Tests students can run. The marking tests check the same ideas with other text."""
import os
import sys
from pathlib import Path

# The tests check the starter folder, where the student works. To check the
# reference solution instead: SUBMISSION_DIR=solution pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / os.environ.get("SUBMISSION_DIR", "starter")))

from textstats import count_sentences, count_words, reading_time_minutes, top_words


def test_counts_words():
    assert count_words("The cat sat on the mat.") == 6


def test_blank_text_has_no_words():
    assert count_words("") == 0
    assert count_words("   \n ") == 0


def test_apostrophes_stay_inside_words():
    assert count_words("Don't panic, it's fine.") == 4


def test_counts_sentences():
    assert count_sentences("One. Two! Three?") == 3


def test_reading_time_rounds_up():
    assert reading_time_minutes("word " * 201) == 2


def test_top_words():
    assert top_words("b a b c b a") == [("b", 3), ("a", 2), ("c", 1)]
