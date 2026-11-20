#!/usr/bin/env python3
"""Write components.md from the Loom public measurements."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

lines = [
    "# Loom components",
    "",
    "Measured on public signed-out pages, 2026-11-18, light, 1440. Hover is a real pointer. Focus-visible is keyboard. Pressed is a forced `:active` and did not fire the control. Nothing was submitted, signed into, or purchased.",
    "",
    "| Component | States | Where | Crop |",
    "|---|---|---|---|",
]
for key in sorted(C):
    comp = C[key]
    states = []
    for name, val in (comp.get("states") or {}).items():
        via = val.get("via") if isinstance(val, dict) else ""
        if via and "failed" in via:
            states.append(f"{name} (not captured: {via})")
        else:
            states.append(name)
    # A keyboard focus that never landed is not a reading: list it as not captured,
    # never as a state that draws no ring (the kit's builders do the same).
    for name, val in (comp.get("notCaptured") or {}).items():
        if isinstance(val, dict) and "failed" in str(val.get("via", "")):
            states.append(f"{name} (focus could not be captured)")
    states = ", ".join(states) or "missing"
    where = comp.get("where") or comp.get("url") or ""
    crop = ""
    for st, val in (comp.get("states") or {}).items():
        if isinstance(val, dict) and val.get("crop"):
            crop = val["crop"]
            break
    crop_cell = f"[{key}]({crop})" if crop else ""
    lines.append(f"| {key} | {states} | {where} | {crop_cell} |")

lines += [
    "",
    "## Gaps",
    "",
    "Text area, select, checkbox, switch, tooltip, toast, table, and avatar are not on the captured public pages. The library, the recorder, and workspace settings sit behind sign-in. The pricing FAQ is a disclosure, and one question was opened. Reactions on the public share page were not pressed, so no reaction was sent. A focus-visible reading whose via says focus failed is not a captured focus state.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("wrote components.md", len(C))
