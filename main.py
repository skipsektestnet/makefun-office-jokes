"""Entry for Make the AI Judge Laugh: Office Jokes: writes the entry text to /output/entry.txt."""
import os
ENTRY = "We have a thirty-minute 'quick sync' that always runs ninety, so I now block time on my calendar to recover from my calendar."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print("wrote /output/entry.txt", len(ENTRY), "chars")
