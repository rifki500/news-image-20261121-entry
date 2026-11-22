#!/usr/bin/env python3
"""Entry program for news-image-20261121.

Copies the bundled newspaper front page (entry.png, 1024x1024, summing up
the world news of Saturday 21 November 2026) to the output directory.
Standard library only, no network, deterministic.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    # The output file keeps the name entry.png, as the competition requires.
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
