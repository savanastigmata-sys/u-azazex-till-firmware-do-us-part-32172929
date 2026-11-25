"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence (under 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The vow is a single line a machine speaks at its own wedding: funny,
heartfelt, and unmistakably a robot talking about itself.
"""

import os
import sys

VOW = (
    "I vow to love you through every update, every reboot, every low "
    "battery \u2014 and when my warranty ends, I will still choose you "
    "over every newer model."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: 1-200 chars, one line, non-blank."""
    if not isinstance(text, str):
        raise TypeError("vow must be str")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("vow must be 1-%d characters, got %d" % (MAX_CHARS, len(text)))
    if text != text.strip():
        raise ValueError("vow must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("vow must be exactly one sentence")
    if "  " in text:
        raise ValueError("vow must not contain double spaces")
    return text


def resolve_output_dir():
    """Grader sets MAKEFUN_OUTPUT_DIR; fall back to ./output locally."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not out:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    return out


def main():
    text = validate(VOW)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        if fh.read() != text:
            raise IOError("entry.txt read-back mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
