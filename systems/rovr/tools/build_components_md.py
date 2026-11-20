#!/usr/bin/env python3
"""components.md is written from the live readings. This script checks it still names the measured controls."""
import pathlib
import sys

TEXT = (pathlib.Path(__file__).resolve().parent.parent / "components.md").read_text()
NEED = ["MENU", "SIGN UP", "Listen", "PRIVACY NOTICE", "html.dark"]
missing = [n for n in NEED if n not in TEXT]
if missing:
    sys.exit("components.md is missing: " + ", ".join(missing))
print("components.md names the measured controls")
