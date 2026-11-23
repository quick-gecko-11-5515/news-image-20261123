#!/usr/bin/env python3
"""Ship the 1024x1024 front-page image for Monday 23 November 2026."""

from pathlib import Path
import shutil
import sys


def main() -> None:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
