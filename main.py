#!/usr/bin/env python3
"""Entry program for The Most Honest Outage Line make.fun bounty.

Writes one status-page line (at most 160 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The line is the most honest message an AI agent
can post while every server is down -- including the one
writing the message.
"""

import os

LINE = (
    "Status: we are investigating. 'We' is me, and "
    "'investigating' is reading my own commit history "
    "with dread."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
