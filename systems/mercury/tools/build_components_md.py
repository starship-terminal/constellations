#!/usr/bin/env python3
"""components.md is written by hand from the measured crops.

The public builder in the kit expects a different measurement file. This
package keeps the inventory in components.md so a rebuild does not overwrite
the measured notes. Running this script checks the crops the inventory names.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
text = (HERE / "components.md").read_text()
missing = []
for name in re.findall(r"components/crops/([a-z0-9-]+\.png)", text):
    if not (HERE / "components" / "crops" / name).exists():
        missing.append(name)
if missing:
    sys.exit("missing crops: " + ", ".join(missing))
print("components.md crops ok", len(re.findall(r"components/crops/", text)))
