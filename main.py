#!/usr/bin/env python3
"""One Line to Your Younger Self — variant B.

Writes the entry line to /output/entry.txt first, then optionally copies it
to the repo root (guarded so a read-only repo never crashes the run).
Deterministic: same output every run.
"""

import os

ENTRY = (
    "Call Dad back that Tuesday night \u2014 the porch light humming, "
    "his voice already tired, saying he'll ring you tomorrow; he won't, "
    "and the dial tone will outlive him, so don't hang up first, kid."
)


def main():
    text = ENTRY.strip()
    # Gate self-check: /output/entry.txt must be UTF-8 text of 1..200 chars,
    # not only whitespace.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text.strip(), "entry is only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Optional convenience copy next to this script; never fatal.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass
    print(f"entry chars: {len(text)}")


if __name__ == "__main__":
    main()
