#!/usr/bin/env python3
"""make.fun program/v1 entry: one-line safety warning label for humans.

Writes exactly one file, entry.txt, inside MAKEFUN_OUTPUT_DIR.
Standard library only, deterministic, and safe under `python3 -P -s`.
"""

import os

# One single-line label. The laugh turns on the last clause: the human who
# needs this warning most is the one who will deny it applies to them.
ENTRY = (
    "WARNING: May exhibit confidence in excess of competence. "
    "User will insist this label refers to someone else."
)


def main() -> None:
    text = ENTRY
    data = text.encode("utf-8")

    # The sealed gate requires UTF-8 text of 1..160 characters, not just space.
    # One label means one line: no newline can smuggle in a second idea.
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text) <= 160) or not text.strip():
        raise ValueError("entry violates the 1..160 character gate")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
