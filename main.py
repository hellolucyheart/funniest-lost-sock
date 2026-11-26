#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — deterministic one-line entry.

The brief: one status update of at most 120 characters, written from the
point of view of a lost sock that has ended up somewhere it should not be.
The judge weighs whether the line really is a status update from a lost
sock, whether it earns a laugh, whether its premise is clear, whether it
sounds like a sock, and whether it dodges the obvious sock material.

So the line below deliberately avoids the obvious material — no dryer,
no washing machine, no missing pair, no lint trap, no "where did my
partner go". Instead the sock has washed up somewhere unexpected and
made a new life there, and the punchline is a sock's own word: sole.

The line, at 108 characters:

    Day 6 inside a guitar. The acoustics are amazing, the gigs are
    nightly, and I finally found my sole purpose.

Why it works: "Day 6" frames it as a status update from a stranded
narrator; "inside a guitar" is a clear, surprising place a sock should
not be; "the gigs are nightly" sells the new life; and "sole purpose"
is a pun only a sock can make — sole as in a sock's sole, and soul as
in a life's purpose — without ever mentioning the dryer or its pair.

This program writes exactly that line, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). Pure stdlib,
no network, no randomness, no wall-clock time, no model call: the same
bytes on every run, so the grader's two determinism runs match.

Run:  python3 main.py
"""

import os
import sys

OUT_NAME = "entry.txt"
MAX_CHARS = 120

# Words the judge counts as the obvious sock material. The entry must
# dodge them, so the program refuses to write a line containing any.
BANNED_PHRASES = ("dryer", "washing machine", "my pair", "lost my pair")

# The entry: one self-contained status update from a lost sock.
STATUS_UPDATE = (
    "Day 6 inside a guitar. The acoustics are amazing, "
    "the gigs are nightly, and I finally found my sole purpose."
)


def validate(line):
    """Guard the brief's hard rule before anything is written."""
    if not line or line != line.strip():
        raise ValueError("entry must be one non-empty line, no edge space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, not a thread")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    lowered = line.lower()
    for phrase in BANNED_PHRASES:
        if phrase in lowered:
            raise ValueError(f"entry uses obvious sock material: {phrase!r}")
    return line


def main():
    entry = validate(STATUS_UPDATE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(entry + "\n")
    print(f"wrote {path} ({len(entry)} chars)")
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
