#!/usr/bin/env python3
"""Remind that DESIGN.md in this package is hand-synced, not make design-md output.

make design-md only emits packages that catalog.json already lists. This capture
does not edit catalog.json, so DESIGN.md is written beside the tokens and the
README says so. Re-read tokens.json before changing DESIGN.md.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
accent = tokens["dark"]["color"]["accent"]["hover"]["$value"]
page = tokens["dark"]["color"]["bg"]["page"]["$value"]
design = (HERE / "DESIGN.md").read_text()
if accent not in design or page not in design:
    sys.exit(f"DESIGN.md is missing {accent} or {page}. Update it from tokens.json.")
print("DESIGN.md still names", accent, "and", page)
