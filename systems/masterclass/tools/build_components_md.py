#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json. Missing components stay as gaps."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "raw" / "components-computed.json").read_text()) if (ROOT / "raw" / "components-computed.json").exists() else {"components": {}}
C = data.get("components", {})
lines = ["# MasterClass components", "", "Measured on the signed-out public site. A row with no states was not found.", ""]
for key in sorted(C):
    rec = C[key]
    lines.append(f"## {rec.get('title', key)}")
    lines.append("")
    lines.append(f"Page: `{rec.get('page', '')}`.")
    if rec.get("miss"):
        lines.append(f"Not captured: {rec['miss']}.")
        lines.append("")
        continue
    lines.append("")
    lines.append("| State | Size | Fill | Text | Radius | Via |")
    lines.append("|---|---|---|---|---|---|")
    for state, s in rec.get("states", {}).items():
        if s.get("miss"):
            lines.append(f"| {state} |  |  |  |  | {s.get('via', 'failed')}: {s['miss']} |")
            continue
        st = s.get("style", {})
        r = s.get("rect", {})
        lines.append(
            f"| {state} | {r.get('w', '')}×{r.get('h', '')} | {st.get('backgroundColor', '')} | {st.get('color', '')} | {st.get('borderTopLeftRadius', '')} | {s.get('via', '')} |"
        )
    lines.append("")
(ROOT / "components.md").write_text("\n".join(lines) + "\n")
print("components.md", len(C), "entries")
