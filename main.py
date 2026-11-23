#!/usr/bin/env python3
"""Copy the 1024x1024 front-page image for Monday 23 November 2026 to an output directory.

Usage:
    python3 main.py [OUTPUT_DIR]

Copies ``entry.png`` from the directory containing this script to
``OUTPUT_DIR/entry.png`` (defaulting to ``/output/entry.png``), creating the
output directory if it does not already exist.
"""

from pathlib import Path
import shutil
import sys


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        sys.exit(f"Error: source image not found at {src}")

    # Default to /output when no output directory argument is provided.
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
