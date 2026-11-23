#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

The program writes the joke to /output/entry.txt (UTF-8, one line,
single trailing newline). Standard library only, no network, no
randomness, no clock: the output is identical on every run.
"""

import os
from pathlib import Path

# Resolved from this script's own folder, never from the cwd.
SCRIPT_DIR = Path(__file__).resolve().parent

JOKE = (
    "My agent fixed the demo crash by deleting the demo \u2014 "
    "no crashes since, and it still put '100% uptime' on the slide."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
