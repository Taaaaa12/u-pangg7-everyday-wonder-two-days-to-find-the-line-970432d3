#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single sentence (at most 200 characters) about a small moment
of wonder in everyday life to /output/entry.txt.

The sentence: the ordinary coincidence of toast popping up at the exact
moment a traffic light turns green, read as if the kitchen and the street
had rehearsed the same cue. No network, no randomness, no input files:
the output is identical on every run.
"""

import os

ENTRY = (
    "My toast pops up the instant the light outside turns green, "
    "as if the kitchen and the street had rehearsed the same cue."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert text.count(".") == 1, "entry must be a single sentence"
    assert text.endswith("."), "entry must end with a period"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
