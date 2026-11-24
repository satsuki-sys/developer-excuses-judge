#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh — Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. Stdlib only, no network.

Revision pass: the first draft ("It worked in staging because staging
has never once had a real user in it.") stated a familiar observation
with the payoff in the middle. This rewrite turns a specific developer
artifact — a TODO left in the code for years — into the culprit, with
the payoff in the last few words.
"""

import os

ENTRY = "The deploy didn't break production \u2014 production finally read the TODO I left in there three years ago."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
