#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line as the office printer's comeback to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate requires UTF-8 text of 1-240 characters, not whitespace-only.
"""
import os
import sys

LINE = "I only jam when the document is important. That is not a bug. That is my job."


def main() -> int:
    if not LINE:
        print("entry is empty", file=sys.stderr)
        return 1
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 240:
        print(f"entry is {len(text)} characters, over the 240 limit", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.endswith((".", "!", "?")):
        print("entry must end with sentence punctuation", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
