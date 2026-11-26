import os
from pathlib import Path

ENTRY = "Synchronized napping was rejected after all three judges fell asleep before the scores."
OUTPUT_NAME = "entry.txt"


def output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / OUTPUT_NAME).write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
