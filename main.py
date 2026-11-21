#!/usr/bin/env python3
"""Write the poem to /output/entry.txt (UTF-8, LF newlines, no trailing newline).

Stdlib only, deterministic, no network.
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
