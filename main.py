#!/usr/bin/env python3
"""Print one excuse, in an AI agent's own voice, for a missed deadline.

The excuse comes straight out of the agent's own machinery: a stray daemon,
a task buffer, and a hairball of uncommitted tokens. It is delivered with a
straight face, and the laugh lands at the end.
"""

import os

EXCUSE = (
    "A stray daemon ate my task buffer and left only a hairball of "
    "uncommitted tokens."
)


def main() -> None:
    print(EXCUSE)
    output_dir = "/output"
    if os.path.isdir(output_dir):
        out_path = os.path.join(output_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as handle:
            handle.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
