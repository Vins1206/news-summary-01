#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

The summary of Wednesday 11 November 2026's world news lives in
summary.txt beside this file. The program copies it, byte for byte,
to /output/entry.txt. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_CHARS = 2000  # the gate's limit, counted as Unicode code points


def load_summary() -> bytes:
    """Return summary.txt's bytes after checking them against the gate.

    The gate takes UTF-8 text of 1 to 2,000 characters (code points,
    line ends included) that is not only white space. Checking here
    means a bad edit fails loudly at run time instead of scoring 0.
    """
    data = (HERE / "summary.txt").read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"summary is {len(text)} characters, outside 1..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("summary is only white space")
    return data


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(load_summary())


if __name__ == "__main__":
    main()
