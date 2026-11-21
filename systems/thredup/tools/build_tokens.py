#!/usr/bin/env python3
"""Check that tokens.json still matches raw/readings.json. Does not rewrite tokens."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())


def hex_of(rgb):
    if rgb.startswith("#"):
        return rgb.lower()
    parts = rgb.replace("rgb(", "").replace("rgba(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts[:3]))


by_role = {r["role"]: r for r in readings["readings"]}
colors = tokens["core"]["color"]
type_tokens = tokens["core"]["typography"]
sizes = tokens["core"]["size"]
errors = []

checks = [
    (hex_of(by_role["body"]["color"]), colors["ink"]["$value"], "ink"),
    (hex_of(by_role["body"]["background"]), colors["page"]["$value"], "page"),
    (hex_of(by_role["header"]["background"]), colors["header"]["$value"], "header"),
    (hex_of(by_role["promo"]["background"]), colors["promo"]["$value"], "promo"),
    (hex_of(by_role["promo-chip"]["background"]), colors["chip"]["$value"], "chip"),
    (hex_of(by_role["pill"]["background"]), colors["sand"]["$value"], "sand"),
    (hex_of(by_role["nav-accent"]["color"]), colors["burgundy"]["$value"], "burgundy"),
    (hex_of(by_role["hero"]["color"]), colors["cream"]["$value"], "cream"),
    (hex_of(by_role["price-was"]["color"]), colors["muted"]["$value"], "muted"),
    (hex_of(by_role["add-to-cart"]["color"]), colors["on-ink"]["$value"], "on-ink"),
    (hex_of(by_role["add-to-cart"]["background"]), colors["ink"]["$value"], "add-to-cart fill"),
]
for got, want, name in checks:
    if got != want:
        errors.append(f"{name}: reading {got} token {want}")

type_checks = [
    ("body", "body", "fontSize", "fontSize"),
    ("body", "body", "fontWeight", "fontWeight"),
    ("nav", "nav", "fontSize", "fontSize"),
    ("nav", "nav", "fontWeight", "fontWeight"),
    ("toggle", "shop-toggle", "fontSize", "fontSize"),
    ("toggle", "shop-toggle", "fontWeight", "fontWeight"),
    ("kicker", "kicker", "fontSize", "fontSize"),
    ("button", "sale-cta", "fontSize", "fontSize"),
    ("button", "add-to-cart", "fontWeight", "fontWeight"),
    ("hero", "hero", "fontSize", "fontSize"),
    ("hero", "category-title", "fontSize", "fontSize"),
    ("brand", "brand", "fontSize", "fontSize"),
    ("price", "price", "fontSize", "fontSize"),
    ("price", "price", "fontWeight", "fontWeight"),
]
for token_name, role, token_key, reading_key in type_checks:
    got = str(by_role[role][reading_key])
    want = str(type_tokens[token_name]["$value"][token_key])
    if got != want:
        errors.append(f"{token_name}.{token_key}: reading {got} token {want}")

if sizes["header"]["$value"] != by_role["header"]["height"]:
    errors.append("header")
if sizes["promo"]["$value"] != by_role["promo"]["height"]:
    errors.append("promo")
if sizes["nav"]["$value"] != by_role["nav"]["height"]:
    errors.append("nav")
if sizes["control"]["$value"] != by_role["search"]["height"]:
    errors.append("control")
if sizes["search"]["$value"] != by_role["search"]["width"]:
    errors.append("search")
if sizes["cart"]["$value"] != by_role["add-to-cart"]["width"]:
    errors.append("cart")
if tokens["core"]["radius"]["control"]["$value"] != by_role["search"]["borderRadius"]:
    errors.append("radius")
if tokens["core"]["radius"]["pill"]["$value"] != by_role["pill"]["borderRadius"]:
    errors.append("pill")
if "Season Sans" not in tokens["core"]["font"]["sans"]["$value"]:
    errors.append("sans")
if "Season Serif" not in tokens["core"]["font"]["serif"]["$value"]:
    errors.append("serif")

unverified = [
    "field-border (computed rgb(182, 181, 178) on search and email)",
    "hero panel rgb(131, 33, 30) is one step from the burgundy token rgb(131, 33, 29)",
]
if errors:
    print("mismatch:", "; ".join(errors))
    sys.exit(1)
print("tokens match readings")
print("not checked against readings.json:")
for item in unverified:
    print("-", item)
