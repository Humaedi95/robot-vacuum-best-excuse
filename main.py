#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line -- the vacuum's excuse for missing a spot -- to
/output/entry.txt, as required by the make.fun bounty
u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.
"""

import os

ENTRY = (
    "My cliff sensor saw the rug's shadow, panicked, and filed "
    "the whole corner as a staircase. I believed it."
)


def main() -> None:
    # The gate requires UTF-8 text of 1 to 140 characters, not only
    # whitespace, on a single line -- check before writing.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
