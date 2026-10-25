# Text statistics (Python, autograded)

Write four small functions that describe a piece of text: how many words and
sentences it has, how long it takes to read, and which words it uses most.

## What you are building

Everything goes in `textstats.py`:

1. `count_words(text)`: the number of words. Words are runs of letters, digits
   and apostrophes, so "don't" is one word.
2. `count_sentences(text)`: the number of sentences, ending in `.`, `!` or `?`.
   "Wait... what?!" is two sentences, not five.
3. `reading_time_minutes(text, words_per_minute=200)`: minutes to read it,
   rounded up.
4. `top_words(text, n=3, ignore=None)`: the `n` most common words, most common
   first, ties in alphabetical order.

The docstrings in the file give the exact rules.

## Getting started

Open `textstats.py` in your lab and replace each `raise NotImplementedError`
with your code. Press **Run the tests** as often as you like: the checks fail
until the functions work. They don't cover every case, and the marking tests
use other text, so test your own edge cases too. Press **Submit** when you're
done.

## How this is marked

| Criterion | Points |
|---|---|
| Words counted correctly | 25 |
| Sentences counted correctly, including repeated marks | 25 |
| Reading time rounded up, custom speed honoured | 20 |
| Top words: case, ties and ignored words handled | 30 |

---

## For teachers

This repository is an example assignment in the layout
[Uppcoder](https://portal.uppcoder.com/education?utm_source=github&utm_medium=repo&utm_campaign=example-assignment)
uses for coding assignments:

| Path | What it holds | Who sees it |
|---|---|---|
| `README.md` | The instructions | Students (as ASSIGNMENT.md) |
| `starter/` | The code every student starts from | Students |
| `tests/public/` | Checks students run with "Run the tests" | Teachers and TAs |
| `tests/hidden/` | The marking tests | Teachers only |
| `solution/` | The reference solution | Teachers only |
| `.autograder/config.yaml` | How the tests are run and scored | Teachers |

Try it locally: `pip install pytest`, then `pytest` fails against the starter
(12 failed) and `SUBMISSION_DIR=solution pytest` passes (12 passed).

To use it in a course, copy the repository (keep your copy private, since it
holds the solution and the marking tests) and import its URL into an Uppcoder
course. Each student gets their own copy of the starter in a ready coding lab
in the browser, and every submission is marked by the tests. Uppcoder runs on
its own or inside Moodle, Canvas or Brightspace over LTI 1.3, and works as a
[GitHub Classroom alternative](https://portal.uppcoder.com/github-classroom-alternative?utm_source=github&utm_medium=repo&utm_campaign=example-assignment).

Step by step, with pictures: [autograde Python assignments with pytest and a rubric in Canvas or Moodle](https://portal.uppcoder.com/guides/autograde-python-canvas-moodle?utm_source=github&utm_medium=repo&utm_campaign=example-assignment).

MIT licensed: use it, change it, hand it out.
