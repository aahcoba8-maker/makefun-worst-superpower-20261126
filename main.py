#!/usr/bin/env python3
"""Worst Superpower entry.

Writes one line inventing the most useless superpower to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt when the variable is unset).
"""

import os

TEXT = "I always know exactly where my phone is, but only when I'm holding it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    path = os.path.join(out_dir, "entry.txt") if out_dir else "entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
