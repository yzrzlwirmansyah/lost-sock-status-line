#!/usr/bin/env python3
"""Write the competition entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Entry choice: a dollhouse premise is sock-specific (a sock longing for real
feet, worn by a tiny doll instead), the punch lands in the last words
("I miss feet"), and it reads aloud cleanly in one breath.
"""

import os
import sys

ENTRY = "Found in the dollhouse. A tiny man just climbed into me. I miss feet."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Validate guard: gate is 1-120 chars of UTF-8 text, no CR/LF.
    if not ENTRY.strip():
        print("entry is empty or whitespace-only", file=sys.stderr)
        return 2
    if len(ENTRY) > 120:
        print(f"entry is {len(ENTRY)} chars, over the 120-char limit", file=sys.stderr)
        return 2
    if "\r" in ENTRY or "\n" in ENTRY:
        print("entry contains CR/LF", file=sys.stderr)
        return 2

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
