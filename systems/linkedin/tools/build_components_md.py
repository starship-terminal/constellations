#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json. Does not invent missing states."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())

lines = [
    "# LinkedIn components",
    "",
    "Public guest pages, measured on 2026-11-21. Each value is a computed style. A state that did not resolve is listed under Gaps.",
    "",
]
gaps = []
for key, comp in COMP["components"].items():
    lines.append("## %s" % key)
    lines.append("")
    lines.append("Page: %s. Selector: `%s`." % (comp.get("page"), comp.get("selector", "visible element")))
    if comp.get("wall"):
        lines.append("This control sits on a login wall. It was measured and not submitted.")
    lines.append("")
    lines.append("| State | Background | Color | Size | Radius | Crop |")
    lines.append("|---|---|---|---|---|---|")
    for state, node in comp.get("states", {}).items():
        if node.get("missing") or node.get("error"):
            gaps.append("%s %s: %s" % (key, state, node.get("error") or "selector missed"))
            continue
        s = node.get("style") or {}
        crop = node.get("crop") or ""
        crop_cell = "[%s](%s)" % (state, crop) if crop else ""
        lines.append("| %s | %s | %s | %s | %s | %s |" % (
            state, s.get("backgroundColor", ""), s.get("color", ""),
            s.get("fontSize", ""), s.get("borderRadius", ""), crop_cell))
    lines.append("")

lines += ["## Gaps", ""]
if gaps:
    for g in gaps:
        lines.append("- %s" % g)
else:
    lines.append("- No measurement misses in the recorded set.")
lines += [
    "",
    "- Text area, select, radio, switch, tooltip, toast, table, avatar, and badge were not present as measurable public controls on the captured pages.",
    "- Disabled, loading, and error states were not shown without submitting a form.",
    "- The jobs listing opened a sign-in dialog on its own. That dialog was not dismissed by submitting it. The listing underneath is in the screenshot.",
    "- Dark theme is declared in the guest CSS and was not painted.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("wrote components.md", len(COMP["components"]), "entries")
