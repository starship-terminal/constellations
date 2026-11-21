#!/usr/bin/env python3
"""Confirm style-guide.html exists. The page is hand-built from the measured tokens."""
import pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "style-guide.html"
assert p.exists() and "f35820" in p.read_text()
print("style-guide.html ok")
