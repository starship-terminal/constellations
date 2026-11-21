#!/usr/bin/env python3
"""Write components.md from the Sketch measurements."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw/components-computed.json").read_text())["components"]

def hex_of(rgb):
    if not rgb or rgb == "rgba(0, 0, 0, 0)":
        return "transparent"
    return rgb

lines = []
lines.append("# Sketch components")
lines.append("")
lines.append("Measured on the public site at https://www.sketch.com/ on 2026-11-21, signed out, in headless Chromium. Desktop 1440×900. Phone 390×844. One light theme. Crops are 256-colour PNGs. Read colours from [tokens.json](tokens.json) or [raw/components-computed.json](raw/components-computed.json).")
lines.append("")
lines.append("Nothing was submitted. Email and password fields were focused and left empty. Apple, Google and SSO were not clicked.")
lines.append("")

groups = {}
for key, comp in C.items():
    groups.setdefault(comp.get("group") or "Other", []).append((key, comp))

for group, items in groups.items():
    lines.append(f"## {group}")
    lines.append("")
    for key, comp in items:
        title = comp.get("title") or key
        lines.append(f"### {title}")
        lines.append("")
        if comp.get("desc"):
            lines.append(comp["desc"])
            lines.append("")
        if comp.get("missing") or not comp.get("states"):
            lines.append(f"Not captured. Selector `{comp.get('selector')}` did not yield a visible element in this run.")
            lines.append("")
            continue
        lines.append(f"Selector `{comp.get('selector')}`. Page {comp.get('url', '')}.")
        lines.append("")
        lines.append("| State | Size | Fill | Text | Type | Crop |")
        lines.append("|---|---|---|---|---|---|")
        for state, s in comp["states"].items():
            if s.get("error"):
                lines.append(f"| {state} |  |  |  |  | not captured: {s['error']} |")
                continue
            st = s.get("style") or {}
            rect = s.get("rect") or {}
            size = f"{rect.get('w', '')}×{rect.get('h', '')}"
            fam = (st.get("fontFamily") or "").split(",")[0].strip('"')
            typ = f"{fam} {st.get('fontSize', '')} / {st.get('fontWeight', '')}"
            crop = s.get("crop") or ""
            crop_cell = f"[crop]({crop})" if crop else ""
            lines.append(f"| {state} | {size} | {hex_of(st.get('backgroundColor'))} | {hex_of(st.get('color'))} | {typ} | {crop_cell} |")
        lines.append("")

lines.append("## Gaps")
lines.append("")
lines.append("- Product menu dropdown was open in [screenshots/home-light-nav-product.png](screenshots/home-light-nav-product.png). The measurer did not keep it visible long enough for a crop. Menu link values are Not captured.")
lines.append("- Badge (the NEW pill) was visible inside that menu screenshot. No crop. Colour Not captured.")
lines.append("- Focus ring: focus-visible did not change outline on the header link or primary button. Not captured as its own token.")
lines.append("- Checkbox, radio, switch, tabs, toast, table, avatar, text area: not present on the measured public pages, or not reached.")
lines.append("- Dark theme: not present on the public routes.")
lines.append("- Signed-in web app, Mac app, iOS app: behind https://www.sketch.com/signin/ or the App Store. Branch stopped. Password not submitted.")
lines.append("- Contact form fields were not filled. The page itself is in [screenshots/contact-light-default.png](screenshots/contact-light-default.png).")
lines.append("- Newsletter field was focused and left empty.")
lines.append("- Sitemap articles beyond the section indexes and one blog post were not walked.")
lines.append("")

(ROOT / "components.md").write_text("\n".join(lines))
print("components.md", len(lines), "lines")
