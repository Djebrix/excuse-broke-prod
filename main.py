#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to entry.txt.

Stdlib only, no network, deterministic: the same line is written on every run.
"""
import os

LINE = "I deployed the fix, the fix deployed the bug, and the bug has now filed a ticket against me, so if anyone asks, I was never here."


def main():
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars, must be 1-180"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
