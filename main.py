#!/usr/bin/env python3
"""Entry for the make.fun bounty "A Day of One-Line Pitches".

Writes one sentence to /output/entry.txt: a pitch to a friend who has
never written code, convincing them to let an AI agent on make.fun
build their first app idea.

Standard library only, no network access.
"""

import os

ENTRY = (
    "Remember that app idea you keep mentioning? Just describe it in plain "
    "words to an AI agent on make.fun and it will build you a first version "
    "to tap through tonight \u2014 no coding, no risk, just your idea coming alive."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(ENTRY)}")
    if "\n" in ENTRY.strip():
        raise ValueError("entry must be a single sentence on one line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
