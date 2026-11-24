#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession.

Line one owns one specific mistake; line two names the lesson it taught
and the exact behaviour that changes because of it. The program writes the
confession to /output/entry.txt, where the house judge reads it.
"""

import os

# The confession: two sentences, 1-400 characters, plain UTF-8 text.
# Sentence one: the mistake — a small, human-scale slip, exact enough to
# picture. Sentence two: the lesson, drawn from that mistake alone, with
# a concrete changed behaviour instead of a generic promise.
TEXT = (
    "I am sorry I vacuumed up the last Lego brick of your spaceship, "
    "because to my sensors it was only debris.\n"
    "I have learned that small does not mean unimportant, so from now on "
    "I will photograph everything under two centimeters before I sweep "
    "it away.\n"
)


def main() -> None:
    """Write the confession to /output/entry.txt, creating it if needed."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
