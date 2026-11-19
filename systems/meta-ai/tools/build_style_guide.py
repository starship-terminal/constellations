#!/usr/bin/env python3
"""Confirm style-guide.html exists and names the measured page colour.

The guide is hand-authored from the same readings as tokens.json. This script
does not rewrite it, because the kit template assumes Claude's token paths.

    python3 tools/build_style_guide.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
html = (HERE / "style-guide.html").read_text()
need = ["#181819", "#1793ff", "9999px", "Meta AI"]
missing = [n for n in need if n not in html]
if missing:
    print("style-guide.html missing", ", ".join(missing))
    sys.exit(1)
print("style-guide.html ok")
