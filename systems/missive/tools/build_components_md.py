#!/usr/bin/env python3
"""components.md is written from the measured readings and checked in.

This builder confirms the measurement file and the crop set still match.
It does not rewrite the prose. Run it after a recapture and update
components.md by hand when a measured value moves.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
comp = json.loads((ROOT / "raw" / "components-computed.json").read_text())
crops = sorted(p.name for p in (ROOT / "components" / "crops").glob("*.png"))
missing = [k for k, v in comp["components"].items() if not (v.get("states") or {}).get("default")]
print(f"components {len(comp['components'])}, crops {len(crops)}, readings without a default {missing}")
if not (ROOT / "components.md").exists():
    sys.exit("components.md missing")
text = (ROOT / "components.md").read_text()
absent = [c for c in crops if c not in text and c.replace(".png", "") not in text]
# wordmark and a few crops are linked; warn only
print("crops not named in components.md:", absent)
