#!/usr/bin/env python3
"""components.md is maintained with the capture. This script only checks it exists."""
import pathlib, sys
p = pathlib.Path(__file__).resolve().parent.parent / "components.md"
if not p.exists():
    sys.exit("components.md missing")
print("components.md", p.stat().st_size, "bytes")
