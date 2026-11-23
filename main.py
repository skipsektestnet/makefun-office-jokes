"""Make the AI Judge Laugh: Office Jokes: writes the entry text to /output/entry.txt.

Why this line: a meeting everyone has sat in, the exaggeration is exact,
the punch turns the calendar on itself.
"""

import os

# The entry itself: one line, the calendar is both the setup and the punch.
ENTRY = "We have a thirty-minute 'quick sync' that always runs ninety, so I now block time on my calendar to recover from my calendar."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
