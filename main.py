#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis from an AI therapist to its human
to /output/entry.txt and prints it. The diagnosis is pure deadpan: the
patient's file says one thing, their 3 a.m. search history says another,
and the therapist trusts the search history.
"""

import os

LINE = (
    "Your file says: 'fine.' "
    "Your 3 a.m. search history says: 'am I a bad person?' "
    "I'm siding with the search history."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
