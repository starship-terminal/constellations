#!/usr/bin/env python3
"""components.md is written from the capture notes. This script checks it exists."""
import pathlib
import sys

p = pathlib.Path(__file__).resolve().parent.parent / "components.md"
if not p.exists():
    sys.exit("components.md missing")
print("components.md present", p.stat().st_size)
