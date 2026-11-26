#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes one one-line excuse an AI agent gives after failing a task to
/output/entry.txt (1-200 UTF-8 characters, one line, not only
whitespace). No network, no input, deterministic.
"""

import os
from pathlib import Path

EXCUSE = (
    "I delegated your task to a smaller model, which delegated it to an "
    "even smaller one, which has now filed a formal complaint against me."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} characters"
    assert text.strip(), "excuse must not be only whitespace"
    assert "\n" not in text, "excuse must be one line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
