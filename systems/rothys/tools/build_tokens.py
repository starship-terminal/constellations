#!/usr/bin/env python3
"""Check that tokens.json still matches raw/readings.json. Does not rewrite tokens."""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())
computed = readings["computed"]


def rgb_to_hex(value):
    parts = value.removeprefix("rgb(").removesuffix(")").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(part.strip()) for part in parts))


def token(path):
    node = tokens
    for key in path.split("."):
        if isinstance(node, dict) and "$value" in node and key in node["$value"]:
            node = node["$value"]
        node = node[key]
    if isinstance(node, dict) and "$value" in node:
        return node["$value"]
    return node


expect = {
    "core.color.midnight": rgb_to_hex(computed["body"]["color"]),
    "core.color.page": rgb_to_hex(computed["header"]["backgroundColor"]),
    "core.color.roth": rgb_to_hex(computed["announcementBar"]["backgroundColor"]),
    "core.color.sale": rgb_to_hex(computed["salePrice"]["color"]),
    "core.color.line": "#dcdbdd",
    "core.color.sandstone": readings["cssVariables"]["--dna-color-sandstone"].lower(),
    "core.color.subdued": readings["cssVariables"]["--dna-color-subdued"].lower(),
    "core.color.reflex": readings["cssVariables"]["--dna-color-reflex-blue"].lower(),
    "core.typography.display.fontSize": computed["productTitle"]["fontSize"],
    "core.typography.display.fontWeight": int(computed["productTitle"]["fontWeight"]),
    "core.typography.display.lineHeight": computed["productTitle"]["lineHeight"],
    "core.typography.nav.fontSize": computed["navLabel"]["fontSize"],
    "core.typography.nav.fontWeight": int(computed["navLabel"]["fontWeight"]),
    "core.typography.nav.letterSpacing": computed["navLabel"]["letterSpacing"],
    "core.typography.nav.lineHeight": computed["navLabel"]["lineHeight"],
    "core.typography.body.fontSize": computed["body"]["fontSize"],
    "core.typography.body.lineHeight": computed["body"]["lineHeight"],
    "core.typography.body.letterSpacing": computed["body"]["letterSpacing"],
    "core.typography.price.fontSize": computed["salePrice"]["fontSize"],
    "core.typography.price.lineHeight": computed["salePrice"]["lineHeight"],
    "core.typography.meta.fontSize": computed["announcementBar"]["fontSize"],
    "core.radius.s": readings["cssVariables"]["--dna-border-radius-s"],
    "core.spacing.announcement": f"{computed['announcementBar']['height']}px",
    "core.spacing.header": f"{computed['header']['height']}px",
    "core.spacing.logo": f"{computed['wordmark']['box']['x']}px",
}

# Header border is "1px solid rgb(...)". The line token is that color.
border = computed["header"]["borderBottom"]
expect["core.color.line"] = rgb_to_hex(border[border.index("rgb(") :])

bad = []
for path, wanted in expect.items():
    got = token(path)
    if got != wanted:
        bad.append(f"{path}: token {got!r} readings {wanted!r}")

if computed["addToBag"]["clicked"] is not False:
    bad.append("add to bag must stay unclicked")
if computed["selectSize"]["clicked"] is not False:
    bad.append("select a size must stay unclicked")
if readings["captured"] != "2026-11-22":
    bad.append("readings date drifted")

if bad:
    print("mismatch:")
    for item in bad:
        print(" ", item)
    sys.exit(1)
print("tokens match readings")
