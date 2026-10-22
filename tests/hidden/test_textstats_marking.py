"""Marking tests. Students never see them; TAs do not either."""
import os
import sys
from pathlib import Path

# The tests check the starter folder, where the student works. To check the
# reference solution instead: SUBMISSION_DIR=solution pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / os.environ.get("SUBMISSION_DIR", "starter")))

from textstats import count_sentences, count_words, reading_time_minutes, top_words


def test_repeated_marks_end_one_sentence():
    assert count_sentences("Wait... what?!") == 2


def test_text_without_a_closing_mark_is_one_sentence():
    assert count_sentences("no full stop here") == 1
    assert count_sentences("") == 0


def test_short_text_takes_one_minute():
    assert reading_time_minutes("Hello there.") == 1
    assert reading_time_minutes("") == 0


def test_custom_reading_speed():
    assert reading_time_minutes("word " * 100, words_per_minute=50) == 2


def test_top_words_ignores_case_and_breaks_ties_alphabetically():
    assert top_words("Pear apple pear Apple fig", n=2) == [("apple", 2), ("pear", 2)]


def test_top_words_leaves_out_ignored_words():
    assert top_words("the cat and the hat", n=2, ignore={"The", "and"}) == [("cat", 1), ("hat", 1)]
