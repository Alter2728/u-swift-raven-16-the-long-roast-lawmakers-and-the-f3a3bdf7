#!/usr/bin/env python3
"""Entry for make.fun bounty u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7:
"The Long Roast: Lawmakers and the File They Cannot Convert".

Writes one satirical sentence — a roast of lawmakers who would regulate AI,
crypto or the internet but cannot convert a file to PDF — to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3.13, standard library only. Deterministic: same bytes every run.

DRAFT (first version): a flat setup-and-punch line about lawmakers writing a
400-page AI law and then calling IT because the PDF button is "hiding".
It states the contrast but the punch is a reported quote, not a scene —
it tells the joke instead of showing it.

REVISED (final): the turn is now a scene, not a quote. The setup keeps the
authority (a year, 400 pages of AI law); the undercut is their own memo,
the one file that matters to them; and the punch lands on the last words —
they print it, scan it, and email the scan to themselves as the official
copy. Specific, unexpected detail (the print-scan-email loop) instead of
the worn "tech-illiterate politician calls IT" cliche, and the aim stays
on lawmakers and the rules they write.
"""

import os

ENTRY = (
    "They spent a year writing 400 pages of law to govern artificial "
    "intelligence, yet they cannot convert their own memo to PDF — so "
    "they print it, scan it, and email the scan to themselves as the "
    "official copy."
)

MAX_CHARS = 320


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry {len(ENTRY)} chars, must be 1-320"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
