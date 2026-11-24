#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Entry program for the make.fun competition
u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.

The judge compares single words pairwise against its published brief,
weighing, most important first: (1) on-subject fit, (2) funny at once,
(3) true to how home Wi-Fi behaves, (4) a fresh angle, (5) instantly
gettable as one word. This program scores a short list of candidate
words on those five criteria, in the brief's own order, and writes the
winner to /output/entry.txt. The gate allows 1 to 20 UTF-8 characters;
the winner is 13.

No network, no environment, no input files: everything the program runs
is in this file.
"""

import os
import sys

# word -> (on-subject, funny at once, true, fresh angle, instantly gettable)
CANDIDATES = {
    "Situationship": (5, 5, 5, 5, 4),
    "Parttime": (4, 4, 5, 3, 5),
    "Freelance": (4, 4, 4, 4, 5),
    "Longdistance": (4, 4, 4, 4, 4),
    "Moody": (3, 2, 4, 1, 5),
}

DEFAULT_OUTPUT = "/output/entry.txt"


def pick_word(candidates):
    """Best word by the brief's criteria, most important first.

    The tuple order is the brief's order, and the judge goes through the
    criteria in order and lets the first difference decide, so a plain
    lexicographic max is the faithful way to pick: a word only wins on a
    later criterion when it ties on every earlier one.
    """
    return max(candidates, key=lambda word: candidates[word])


def main(argv):
    word = pick_word(CANDIDATES)
    text = word  # exactly the word: no newline, no extra whitespace
    if not 1 <= len(text.encode("utf-8")) <= 20:
        raise SystemExit("entry word fails the 1-20 character gate")
    output = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
