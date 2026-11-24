#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label (120 characters or fewer) for a time machine
to /output/entry.txt (or $OUTPUT_PATH when set).
Standard library only. No network, no secrets.
"""

import os
import sys

LINE = (
    "CAUTION: Passengers who meet themselves must not exchange wallets. "
    "One of you is already broke, and it is both of you."
)

MAX_CHARS = 120


def fail(message: str) -> "SystemExit":
    print(f"error: {message}", file=sys.stderr)
    return SystemExit(1)


def main() -> int:
    # Validate the label before writing anything.
    if not LINE or not LINE.strip():
        print("error: label is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: label must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(
            f"error: label is {len(LINE)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    output_path = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    try:
        parent = os.path.dirname(output_path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        if output_path != "./output/entry.txt":
            fallback = "./output/entry.txt"
            try:
                os.makedirs(os.path.dirname(fallback), exist_ok=True)
                with open(fallback, "w", encoding="utf-8") as f:
                    f.write(LINE)
                output_path = fallback
            except OSError as exc:
                print(f"error: cannot write output: {exc}", file=sys.stderr)
                return 1
        else:
            print(
                f"error: cannot write output to {output_path}",
                file=sys.stderr,
            )
            return 1

    # Read back and verify the file holds exactly the label.
    try:
        with open(output_path, "r", encoding="utf-8") as f:
            written = f.read()
    except OSError as exc:
        print(f"error: cannot read back output: {exc}", file=sys.stderr)
        return 1
    if written != LINE:
        print(
            "error: verification failed — file contents do not match the label",
            file=sys.stderr,
        )
        return 1

    print(f"Wrote {len(LINE)} characters to {output_path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
