"""Roast the Smart Fridge: one line, best laugh wins.

Prints a single original one-line roast of a smart fridge and writes it
to <output>/entry.txt (honouring $MAKEFUN_OUTPUT_DIR when set).
Python 3 standard library only.
"""

import os
import sys

LINE = "My smart fridge has Wi-Fi, a camera, and opinions \u2014 basically a landlord that watches me eat."


def main() -> int:
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
