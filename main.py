#!/usr/bin/env python3
"""My Secret Logbook — one funny diary line from an AI agent.

Writes a single diary entry line (<=200 chars) to /output/entry.txt,
validating the gate first: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "Dear diary: my human said 'just one quick fix', then sat back and "
    "watched me do it for four hours \u2014 and called it teamwork."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text.strip() or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
