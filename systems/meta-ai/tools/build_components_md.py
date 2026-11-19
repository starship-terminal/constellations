#!/usr/bin/env python3
"""Confirm components.md still names the controls that were measured.

    python3 tools/build_components_md.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
text = (HERE / "components.md").read_text()
need = ["Log in", "Ask Meta AI", "auth.meta.com", "9999px", "Gaps"]
missing = [n for n in need if n not in text]
if missing:
    print("components.md missing", ", ".join(missing))
    sys.exit(1)
print("components.md ok")
