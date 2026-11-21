#!/usr/bin/env python3
"""components.md for the Replo public capture is written by hand from the live readings.

The public measure.mjs pass was not run. This script checks the file exists
and names the readings it depends on, so a rebuild does not invent crops.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
md = HERE / "components.md"
live = HERE / "raw" / "live.json"
if not md.exists() or not live.exists():
    sys.exit("components.md and raw/live.json are required")
print("components.md present;", md.stat().st_size, "bytes")
