#!/usr/bin/env python3
"""components.md is maintained with the capture notes.

The kit's Gauth builder does not apply to this package. This script checks that
components.md still names the measured token paths and exits non-zero if one is missing.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
text = (ROOT / "components.md").read_text()
needed = [
    "dark.component.button-primary-bg",
    "dark.component.button-secondary-bg",
    "core.typography.nav",
    "not captured",
]
missing = [n for n in needed if n not in text]
if missing:
    sys.exit("components.md is missing: " + ", ".join(missing))
print("components.md ok")
