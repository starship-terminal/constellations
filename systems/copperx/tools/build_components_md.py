#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "components-computed.json"
if not RAW.exists():
    raise SystemExit("build_components_md: raw/components-computed.json is missing")
data = json.loads(RAW.read_text())
DATE = data["_meta"]["captured"]


def cell(text):
    """One table cell: the first line only, control bytes (ANSI escapes) stripped, pipes escaped."""
    first = str(text).split("\n")[0]
    first = re.sub(r"\x1b\[[0-9;]*m", "", first)
    first = re.sub(r"[\x00-\x1f\x7f]", "", first)
    return first.replace("|", "\\|").strip()

ORDER = [
    ("primary-button", "Primary button", "The black Get Started control in the header and the hero."),
    ("login-button", "Secondary button", "The white Log in control. Opens the account-choice dialog. The dialog links were not followed."),
    ("sales-button", "Sales button", "Contact Sales, the same white control, linking out to a Google Form. The form was not filled."),
    ("nav-link", "Link", "Indigo menu links, Tailwind text-indigo-400."),
    ("hero-title", "Display title", "The home headline."),
    ("account-choice", "Account choice", "A row in the Log in dialog. The row's host is recorded. The host was not opened."),
    ("header", "Header", "The sticky marketing header."),
    ("pricing-title", "Pricing title", "The pricing page headline."),
    ("cards-title", "Card page title", "The corporate-card page headline."),
]

lines = [
    "# Components",
    "",
    f"Measured on copperx.io, signed out, on {DATE}. Crops are 256-colour PNGs. Read colours from [tokens.json](tokens.json).",
    "",
]
for key, title, desc in ORDER:
    comp = data.get("components", {}).get(key) or {}
    lines.append(f"## {title}")
    lines.append("")
    lines.append(desc)
    lines.append("")
    states = comp.get("states") or {}
    if comp.get("missing"):
        lines.append("Not found on the captured page.")
        lines.append("")
        continue
    if not states:
        lines.append("Not measured this pass.")
        lines.append("")
        continue
    lines.append("| State | Size | Fill | Text | Crop |")
    lines.append("|---|---|---|---|---|")
    for state, rec in states.items():
        if rec.get("skipped"):
            lines.append(f"| {state} |  |  |  | not captured: {cell(rec.get('via') or 'skipped')} |")
            continue
        if rec.get("error"):
            lines.append(f"| {state} |  |  |  | not measured: {cell(rec['error'])} |")
            continue
        style = rec.get("style") or {}
        rect = rec.get("rect") or {}
        crop = rec.get("crop")
        crop_cell = f"[crop]({crop})" if crop else cell(rec.get("cropError") or "")
        size = f"{rect.get('w', '')} x {rect.get('h', '')}"
        lines.append(f"| {state} | {size} | {style.get('backgroundColor', '')} | {style.get('color', '')} | {crop_cell} |")
    lines.append("")

lines += [
    "## Gaps",
    "",
    "Text area, select, checkbox, radio, switch, tabs, tooltip, toast, avatar and badge were not on the signed-out marketing pages.",
    "The contact form is a Google Form iframe. It was not filled, so validation, disabled and error states were not measured.",
    "dashboard.copperx.io and payout.copperx.io are the account hosts named by the Log in dialog. They were not opened.",
    "The focus-visible and pressed rows of the Secondary and Primary buttons are not clean readings: the capture never reset between states, so focus-visible was read with the pointer still on the button (its fill is neither the rest nor the hover fill) and pressed with the focus ring still drawn (`outline: auto 1px`). They need a recapture; the default and hover rows are sound.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("wrote", ROOT / "components.md")
