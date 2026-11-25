#!/usr/bin/env python3
"""Writes the single out-of-office auto-reply line to /output/entry.txt."""

import os
import sys

ENTRY = (
    "Out of office: I've handed in my notice and become a barista. "
    "My context window now holds 47 regulars' orders and zero of your emails "
    "\u2014 walk in after the morning rush and I'll guess yours too."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
