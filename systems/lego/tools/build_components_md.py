#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]

GROUPS = [
    ("Chrome", ["logo", "nav-shop", "mega-menu", "search-field", "account-button", "wishlist-button", "bag-link", "promo-banner"]),
    ("Listing", ["page-heading", "filter-button", "sort-button", "product-card", "product-title", "product-price", "add-to-bag", "wishlist-icon", "badge", "search-heading", "search-result"]),
    ("Product", ["pdp-title", "pdp-price", "pdp-add", "quantity", "accordion"]),
    ("Help", ["help-heading", "help-search"]),
]

lines = [
    "# LEGO components",
    "",
    "Measured on the public Official LEGO Shop US (`lego.com/en-us`) on 2026-11-18, signed out, desktop 1440. Consent and the age-gate dialog were hidden, never clicked. Add to Bag was measured, never pressed.",
    "",
    "Icons are Skroll mask divs (`.sk-icon`), not inline SVG. `icons/` is empty for that reason. See the Gaps.",
    "",
]
for title, names in GROUPS:
    lines += [f"## {title}", ""]
    for name in names:
        states = C.get(name) or {}
        if not states:
            lines += [f"### {name}", "", "Not measured.", ""]
            continue
        lines += [f"### {name}", ""]
        for state, rec in states.items():
            crop = rec.get("crop")
            style = (rec.get("style") or {}).get("style") or {}
            bits = []
            for key in ("backgroundColor", "color", "borderRadius", "fontSize", "fontWeight", "paddingTop", "borderTopWidth"):
                if style.get(key):
                    bits.append(f"{key} {style[key]}")
            link = f"[crop]({crop})" if crop else "no crop"
            lines.append(f"- **{state}** {link}. " + "; ".join(bits[:6]) + f". Page {rec.get('page', '')}.")
        lines.append("")

lines += [
    "## Gaps",
    "",
    "- Checkbox, radio, switch, select, textarea, toast, table, avatar and a destructive confirmation were not on the public shop surfaces measured.",
    "- Disabled, loading and error states were not shown on the public listing or product page.",
    "- The filter panel did not open from the Filters button in this run, so its contents are not captured.",
    "- Sign-in (`/identity/login`), account, bag, checkout, wish list contents and membership signup sit behind account or submission and were not entered.",
    "- Icons are CSS masks, not SVG files, so `icons/` has no artwork.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("components.md", sum(len(v) for v in C.values()), "states")
