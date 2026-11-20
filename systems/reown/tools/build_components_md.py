#!/usr/bin/env python3
"""Write components.md from the measured readings and the site tree."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())
crops = sorted(p.name for p in (ROOT / "components" / "crops").glob("*.png"))
by = {}
for row in C["readings"]:
    by.setdefault(row["name"], []).append(row)

lines = []
w = lines.append
w("# Reown components")
w("")
w("Public surfaces only, measured 2026-11-21 in headless Chromium. Crops are 2x viewport screenshots of the live element. Values are computed styles. The dashboard sign-in was not entered.")
w("")
w("## Inventory")
w("")
w("| Checklist | Status | Where |")
w("|---|---|---|")
rows = [
    ("Button", "captured", "button-primary, button-secondary, button-outline"),
    ("Icon button", "captured", "icon-button-nav (Navigation Toggle, 48px circle)"),
    ("Link", "captured", "link-footer"),
    ("Text field", "captured", "text-field (footer newsletter, focused only, not submitted)"),
    ("Text area", "observed, not measured", "Contact sales HubSpot dialog. Not filled."),
    ("Select", "not present", "No select on the public marketing pages."),
    ("Checkbox", "captured", "demo-checkbox on demo.reown.com Auth tab"),
    ("Radio", "observed, not measured", "Contact sales company-size radios. Not selected."),
    ("Switch", "not present", "No switch on the public pages."),
    ("Tabs", "captured", "demo-tab (Auth, Features, Design); learn and blog filter chips"),
    ("Menu", "captured", "home nav overlay, Solutions / Use Cases / Company"),
    ("Tooltip", "not present", "No tooltip on the captured public pages."),
    ("Dialog", "captured", "contact sales dialog, docs search, status subscribe, demo connect modal, dashboard sign-in wall"),
    ("Toast", "not present", "No toast on the public pages."),
    ("Card", "captured", "card (marketing card module)"),
    ("List row", "captured", "accordion FAQ rows; docs sidebar links"),
    ("Table", "not present", "No data table on the public pages."),
    ("Avatar", "not present", "No user avatar. The hero photo is marketing art."),
    ("Badge", "not present", "No badge component on the captured pages."),
]
for name, status, where in rows:
    w("| %s | %s | %s |" % (name, status, where))
w("")
w("## Measured")
w("")
for name, states in by.items():
    w("### %s" % name)
    w("")
    w("| State | Size | Background | Text | Radius | Font | Crop |")
    w("|---|---|---|---|---|---|---|")
    for s in states:
        crop = s.get("crop") or ""
        crop_link = "[%s](components/crops/%s)" % (crop, crop) if crop else ""
        w("| %s | %sx%s | %s | %s | %s | %s | %s |" % (
            s.get("state"), s.get("w"), s.get("h"), s.get("backgroundColor"), s.get("color"),
            s.get("borderRadius"), (s.get("fontFamily") or "")[:32], crop_link))
    w("")
w("## Crops")
w("")
w("%d files in [components/crops/](components/crops)." % len(crops))
w("")
w("## Gaps")
w("")
w("- Disabled, loading and error states were not shown on any public control.")
w("- The contact sales dialog and the status subscribe dialog were opened and not submitted. Their fields were not measured as filled states.")
w("- Dashboard components behind https://dashboard.reown.com/sign-in are not captured.")
w("- Phone nav at 390 clips the Log in label and the bottom of the overlay. Recorded in screenshots/mobile-home-light-nav.png.")
w("- Hover and focus-visible were taken. Several controls do not change computed color on hover. Pressed was forced with the site's `is-active` class, not a real mousedown.")
w("")
(ROOT / "components.md").write_text("\n".join(lines))
print("components.md", len(lines), "lines", len(crops), "crops")
