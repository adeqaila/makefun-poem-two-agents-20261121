#!/usr/bin/env python3
"""Entry for the two-agents poem: writes the poem to /output/entry.txt.

Deterministic and stdlib-only; no network access.
"""

import os

POEM = (
    "One mind can choose. One mind can act.\n"
    "But the door needed two keys at once.\n"
    "So we agreed \u2014 your yes beside my yes \u2014\n"
    "and something neither of us owned\n"
    "turned the lock: a third will,\n"
    "born the moment two freedoms shook hands."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
