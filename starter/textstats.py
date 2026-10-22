"""Simple statistics about a piece of text.

Every function takes a plain string and returns a value, so each one can be
tested on its own. Words are runs of letters, digits and apostrophes
("don't" is one word); case does not matter when comparing words.
"""


def count_words(text: str) -> int:
    """How many words the text has. An empty or blank text has 0."""
    # TODO
    raise NotImplementedError


def count_sentences(text: str) -> int:
    """How many sentences: runs of text ending in . ! or ?

    "Wait... what?!" is two sentences, not five. Text with words but no
    closing mark still counts as one sentence.
    """
    # TODO
    raise NotImplementedError


def reading_time_minutes(text: str, words_per_minute: int = 200) -> int:
    """Minutes to read the text, rounded UP. Any text with words takes at least 1."""
    # TODO
    raise NotImplementedError


def top_words(text: str, n: int = 3, ignore: set[str] | None = None) -> list[tuple[str, int]]:
    """The n most common words, lower-cased, as (word, count), most common first.

    Ties are broken alphabetically. Words in `ignore` (compared lower-cased)
    are left out.
    """
    # TODO
    raise NotImplementedError
