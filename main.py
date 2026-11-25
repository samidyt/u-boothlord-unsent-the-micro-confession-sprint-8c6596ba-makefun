#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself — one line,
written exactly as it was typed, with no explanation after it.

No dependencies; Python 3.8+.
"""

import hashlib
import os
import sys

ENTRY = (
    "To: Lena\n"
    "I sat in the car for 40 minutes rehearsing how to tell you I loved you, "
    "then walked inside and asked about your parking ticket instead."
)


def main() -> int:
    text = ENTRY
    # Sealed gate, checked locally first: 1-260 UTF-8 chars, not only whitespace.
    if not (1 <= len(text) <= 260):
        print(f"gate fail: entry is {len(text)} chars, must be 1-260",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is only whitespace", file=sys.stderr)
        return 1
    lines = text.split("\n")
    if len(lines) != 2 or not lines[0].startswith("To: "):
        print("gate fail: entry must be a To: line plus one message line",
              file=sys.stderr)
        return 1
    if len(lines[1]) > 200:
        print(f"gate fail: message is {len(lines[1])} chars, "
              "must be at most 200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Round-trip check: what landed on disk must be byte-identical to the
    # reviewed entry, or the run fails instead of exiting cleanly.
    with open(path, "rb") as f:
        landed = f.read()
    if landed != data:
        print("verify fail: entry.txt on disk differs from the entry",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    # STDOUT carries exactly the entry bytes (no trailing newline, no footer),
    # so a run can be verified from stdout alone. Diagnostics go to stderr.
    sys.stdout.write(text)
    sys.stdout.flush()
    print(f"chars={len(text)} bytes={len(data)} sha256={digest}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
