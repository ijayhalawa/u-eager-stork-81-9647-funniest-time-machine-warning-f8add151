#!/usr/bin/env python3
"""Funniest Time Machine Warning Label -- make.fun entry.

Writes a single original warning label (one line, at most 120
characters) to /output/entry.txt, plus a local copy entry.txt next to
this file for verification. Stdlib only, no network, fully
deterministic: every run writes the exact same bytes.

The joke: meeting your own duplicate self is a classic time-travel
hazard, and the label treats it with deadpan official calm -- the
punchline (you already owe yourself money) lands in the last words,
like a genuine safety notice that has seen this happen before.
"""

import os

ENTRY = "WARNING: Never shake your own hand. You still owe yourself money."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 120, "entry length %d out of range" % len(text)
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
