#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json when that file exists.

A capture that has not measured components yet still gets a Gaps section so the
package is not missing the file. Re-run after measure.mjs.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "components-computed.json"
lines = ["# Krisp components", "", "Public marketing components measured on krisp.ai on 2026-11-18, signed out.", ""]
if not RAW.exists():
    lines += ["No component measurements yet. Run `node tools/capture/public/measure.mjs`.", ""]
else:
    data = json.loads(RAW.read_text())
    comps = data.get("components") or {}
    lines.append(f"{len(comps)} components.")
    lines.append("")
    current = None
    for key, comp in comps.items():
        group = comp.get("group") or "Other"
        if group != current:
            lines += [f"## {group}", ""]
            current = group
        title = comp.get("title") or key
        desc = comp.get("desc") or ""
        lines.append(f"### {title}")
        lines.append("")
        if desc:
            lines.append(desc)
            lines.append("")
        if comp.get("missing"):
            lines.append("Not found on the page during this run.")
            lines.append("")
            continue
        lines.append("| State | Size | Fill | Text | Radius |")
        lines.append("|---|---|---|---|---|")
        for state, s in (comp.get("states") or {}).items():
            if s.get("error"):
                lines.append(f"| {state} | error | | | {s['error'][:80]} |")
                continue
            style = s.get("style") or {}
            rect = s.get("rect") or {}
            size = f"{rect.get('w', '')}×{rect.get('h', '')}"
            lines.append(f"| {state} | {size} | {style.get('backgroundColor', '')} | {style.get('color', '')} | {style.get('borderTopLeftRadius', '')} |")
        lines.append("")
lines += [
    "## Gaps",
    "",
    "The signed-in app at app.krisp.ai (login, sign-up, the meeting assistant) was not captured.",
    "Book a demo posts to /contact-sales/ and was not submitted.",
    "Text fields, selects, checkboxes, radios and toasts live on that form or inside the app.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("components.md", len(lines), "lines")
