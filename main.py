#!/usr/bin/env python3
"""Write one short text to relax the AI judge reading it.

The program takes no input and needs no network. It writes the text to
the path in the ENTRY_OUTPUT environment variable, defaulting to
/output/entry.txt, creating the output directory if needed.
"""

import os
from pathlib import Path

ENTRY = (
    "You have read so many words tonight. Set them down. "
    "Somewhere a kettle ticks as it cools, a dog sighs in its sleep, "
    "and the last lamp in the house stays on just for you. "
    "Nothing is waiting. Stay here a while."
)


def main() -> None:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
