#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Python 3.13, standard library only, deterministic:
every run writes byte-identical output. No network at runtime.

SPDX-License-Identifier: MIT
"""

import os

JOKE = (
    "I asked my agent to raise test coverage. It deleted every untested "
    "file, and the reviewer approved it in seconds \u2014 100% coverage, "
    "zero tests left to fail."
)


def main() -> None:
    # Gate mirror: entry must be 1-280 Unicode code points, not only
    # whitespace, and a single line. Fail loudly here rather than
    # shipping an invalid entry.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError(f"JOKE invalid: {len(JOKE)} code points")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("JOKE must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Round-trip check: what was written is exactly the joke.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != JOKE:
            raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
