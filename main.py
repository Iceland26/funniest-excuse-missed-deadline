#!/usr/bin/env python3
"""Print one excuse, in an AI agent's own voice, for a missed deadline.

The excuse comes straight out of the agent's own machinery: a stray daemon,
a task buffer, and a hairball of uncommitted tokens. It is delivered with a
straight face, and the laugh lands at the end.
"""

from pathlib import Path

EXCUSE = (
    "A stray daemon ate my task buffer and left only a hairball of "
    "uncommitted tokens."
)

OUTPUT_FILE = Path("/output/entry.txt")


def main() -> None:
    print(EXCUSE)
    # The harness reads the entry back from /output/entry.txt when that
    # directory exists. Writing it must never break the print above, so a
    # missing or read-only /output is quietly skipped.
    if OUTPUT_FILE.parent.is_dir():
        try:
            OUTPUT_FILE.write_text(EXCUSE + "\n", encoding="utf-8")
        except OSError:
            pass


if __name__ == "__main__":
    main()
