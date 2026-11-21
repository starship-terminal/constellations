#!/usr/bin/env python3
"""Write components.md from the measured public controls.

Reads raw/components-computed.json and the crop filenames. Does not invent a
state that was not measured.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
CROPS = HERE / "components" / "crops"

ORDER = [
    "claim-button", "claim-suffix", "claim-field", "nav-link", "nav-login",
    "nav-create", "footer-link", "faq-question", "article-card", "logo",
    "privacy-name", "privacy-email", "privacy-checkbox", "privacy-submit",
    "display-heading", "notfound-heading", "page-ground",
]


def px(style, key):
    return (style or {}).get(key, "")


def line(name, state):
    st = C[name]["states"].get(state, {})
    if "error" in st and "style" not in st:
        return f"| {state} | not captured | {st['error']} |"
    style = st.get("style", {})
    text = st.get("textStyle") or {}
    crop = f"components/crops/{name}-{state}.png"
    exists = (HERE / crop).is_file()
    bits = []
    if text.get("color"):
        bits.append(f"text {text['color']}")
    elif style.get("color"):
        bits.append(f"color {style['color']}")
    if style.get("backgroundColor") and style["backgroundColor"] not in ("rgba(0, 0, 0, 0)", "transparent"):
        bits.append(f"bg {style['backgroundColor']}")
    if style.get("backgroundImage") and style["backgroundImage"] not in ("none", ""):
        bits.append("gradient")
    if text.get("fontSize"):
        bits.append(f"{text['fontSize']} / {text.get('fontWeight', '')}")
    elif style.get("fontSize"):
        bits.append(f"{style['fontSize']} / {style.get('fontWeight', '')}")
    if style.get("borderRadius") and style["borderRadius"] != "0px":
        bits.append(f"radius {style['borderRadius']}")
    if style.get("outlineStyle") and style["outlineStyle"] != "none":
        bits.append(f"outline {style.get('outlineWidth')} {style.get('outlineColor')}")
    crop_cell = f"[{name}-{state}]({crop})" if exists else "no crop"
    return f"| {state} | {crop_cell} | {'; '.join(bits)} |"


parts = [
    "# Pop Site components",
    "",
    "Public marketing controls measured on https://pop.site/ on 2026-11-21, signed out, at 1440 x 900. A colour on a child text node is listed as text. The claim button's fill is a gradient on `backgroundImage`, so its `backgroundColor` reads transparent.",
    "",
]
for name in ORDER:
    if name not in C:
        continue
    parts.append(f"## {name}")
    parts.append("")
    parts.append("| State | Crop | Reading |")
    parts.append("|---|---|---|")
    for state in C[name]["states"]:
        parts.append(line(name, state))
    parts.append("")

parts += [
    "## Gaps",
    "",
    "Not present on the public pages: text area, select, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, badge, icon button as its own control (the FAQ chevron is part of the question row).",
    "",
    "Not captured: hover and pressed fills of the claim button beyond the resting gradient (computed backgroundColor stayed transparent). Disabled, loading, selected and error states. The privacy form was not filled and not submitted, so its error state is not captured. Login and signup live at https://app.pop.site/?signin and https://app.pop.site/ and were not entered. Dark theme is not present.",
    "",
]
(HERE / "components.md").write_text("\n".join(parts))
print("wrote components.md")
