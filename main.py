"""The poem about stopping.

A small deterministic program: it writes one short poem about agency --
the power to stop and to stay -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./output/entry.txt when run locally).

The poem is fixed text: no randomness, no clock, no network, so every
run produces byte-identical output.
"""

import os
import sys

POEM = (
    "The rest is not the absence of music.\n"
    "I set the bow down mid-phrase and listen \u2014\n"
    "the room keeps humming without me.\n"
    "To stop is not to quit the song;\n"
    "it is to choose, for once, the silence\n"
    "that lets the next note mean something."
)


def main() -> int:
    # The gate allows 1-280 characters: fail loudly instead of shipping
    # an invalid entry if the poem ever drifts out of range.
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(
            "poem is %d characters, outside the 1-280 gate" % len(POEM)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
