"""Write the houseplant's out-of-office auto-reply to /output/entry.txt."""

import os

ENTRY = "Out of office: I haven't been watered since March. My leaves are on the floor. Please water the floor, not me."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_FILENAME = "entry.txt"


def entry_path():
    return os.path.join(OUTPUT_DIR, ENTRY_FILENAME)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
