#!/usr/bin/env python3
"""Confirm style-guide.html still names the sampled Fiverr fills.

The guide is handwritten for this blocked capture. It must mention the four
sampled colours and must not invent a dark theme. When a later capture reads
CSS, replace this checker with a generator.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
text = (HERE / "style-guide.html").read_text()
needed = ["#ffffff", "#222325", "#1dbf73", "#76293b", "Not captured"]
missing = [n for n in needed if n not in text]
if "data-mode=\"dark\"" in text or "dark theme was observed" in text.lower():
    missing.append("dark theme claimed")
if missing:
    print("style guide missing: " + ", ".join(missing), file=sys.stderr)
    sys.exit(1)
print("style-guide.html matches sampled fills")
