#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json for the Macaw capture."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]
lines = [
    "# Macaw components",
    "",
    "Measured on macawhq.com, signed out, 2026-11-18. Colours are computed styles. Token names are in [tokens.json](tokens.json).",
    "",
    "| Component | States | Crop |",
    "|---|---|---|",
]
for key, c in C.items():
    states = "missing" if c.get("missing") else (", ".join(c.get("states") or []) or "none")
    crop = ""
    for st, v in (c.get("states") or {}).items():
        if v.get("crop"):
            name = Path(v["crop"]).name
            crop = f"[{name}](components/crops/{name})"
            break
    title = c.get("title") or key
    lines.append(f"| {title} (`{key}`) | {states} | {crop or '-'} |")
lines += [
    "",
    "## Notes",
    "",
    "The Resources toggle is `display: none` at 1440, so that row is missing. Get started on pricing did not match a visible link during the run. Log in was cropped by its on-screen box: Playwright treats the Webflow nav link as hidden.",
    "",
    "Pressed on the coral button is a forced `:active` and paints the same `--primary700` as hover. The contact form was not submitted.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("components.md", len(C), "rows")
