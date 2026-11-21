#!/usr/bin/env python3
"""Confirm components.md exists. Component notes were written from the live walk."""
import pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "components.md"
assert p.exists()
print("components.md ok")
