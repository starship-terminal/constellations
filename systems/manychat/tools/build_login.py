#!/usr/bin/env python3
"""Check the signed-in ManyChat notes against the screenshots they name.

Does not rebuild the marketing tokens. Those stay with build_tokens.py.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
review = json.loads((HERE / "login-review.json").read_text())
missing = [row["file"] for row in review["screens"] if not (HERE / row["file"]).is_file()]
if missing:
    sys.exit("login-review.json names missing files: " + ", ".join(missing))
if not review["signed_in"]:
    sys.exit("login-review.json is not a signed-in capture")
if len(review["screens"]) < 2:
    sys.exit("login-review.json needs at least two screens")
for key in ("nav", "settings", "create"):
    block = review["offered"][key]
    if "items" not in block or "reached" not in block:
        sys.exit(f"offered.{key} needs items and reached")
print(f"login notes ok: {len(review['screens'])} screens, {len(review['gaps'])} gaps")
