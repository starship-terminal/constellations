#!/usr/bin/env python3
"""components.md for Understory is written from the capture, not generated.

The public kit's builder expects a Gauth-shaped measurements file. This package
keeps components.md as the inventory of the states that were actually shot.
Re-running this script checks that the inventory still names files that exist.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
md = (HERE / "components.md").read_text()
missing = []
for line in md.splitlines():
    if "screenshots/" not in line:
        continue
    start = line.find("screenshots/")
    end = line.find(".png", start)
    if end < 0:
        continue
    end += 4
    if end < 0:
        continue
    rel = line[start:end]
    if not (HERE / rel).exists():
        missing.append(rel)
if missing:
    sys.exit("missing screenshots:\n" + "\n".join(missing))
print("components.md: referenced screenshots exist")
