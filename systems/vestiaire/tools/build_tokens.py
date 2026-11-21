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
    (hex_of(by_role["search"]["background"]), colors["search"]["$value"], "search"),
    (hex_of(by_role["search"]["color"]), colors["search-ink"]["$value"], "search-ink"),
    (hex_of(by_role["sale"]["color"]), colors["sale"]["$value"], "sale"),
    (hex_of(by_role["promo"]["background"]), colors["promo"]["$value"], "promo"),
    (hex_of(by_role["promo"]["color"]), colors["on-promo"]["$value"], "on-promo"),
    (hex_of(by_role["sell"]["background"]), colors["sell"]["$value"], "sell"),
    (hex_of(by_role["sell"]["color"]), colors["on-sell"]["$value"], "on-sell"),
    (hex_of(by_role["footer-link"]["color"]), colors["footer-link"]["$value"], "footer-link"),
    (hex_of(by_role["footer-label"]["color"]), colors["footer-label"]["$value"], "footer-label"),
    (hex_of(by_role["press"]["background"]), colors["press"]["$value"], "press"),
    (hex_of(by_role["crumb"]["color"]), colors["ink-soft"]["$value"], "ink-soft"),
    (hex_of(by_role["price"]["color"]), colors["price"]["$value"], "price"),
]
for got, want, name in checks:
    if got != want:
        errors.append(f"{name}: reading {got} token {want}")

type_checks = [
    ("body", "body", "fontSize", "fontSize"),
    ("body", "body", "fontWeight", "fontWeight"),
    ("nav", "nav", "fontSize", "fontSize"),
    ("nav", "nav", "fontWeight", "fontWeight"),
    ("button", "sell", "fontSize", "fontSize"),
    ("button", "sell", "fontWeight", "fontWeight"),
    ("promo", "promo", "fontSize", "fontSize"),
    ("hero", "hero", "fontSize", "fontSize"),
    ("section", "section", "fontSize", "fontSize"),
    ("category", "category-title", "fontSize", "fontSize"),
    ("about", "about-title", "fontSize", "fontSize"),
    ("brand", "brand", "fontSize", "fontSize"),
    ("price", "price", "fontSize", "fontSize"),
    ("footer-label", "footer-label", "fontSize", "fontSize"),
    ("footer-link", "footer-link", "fontSize", "fontSize"),
    ("menu-link", "menu-link", "fontSize", "fontSize"),
]
for token_name, role, token_key, reading_key in type_checks:
    got = str(by_role[role][reading_key])
    want = str(type_tokens[token_name]["$value"][token_key])
    if got != want:
        errors.append(f"{token_name}.{token_key}: reading {got} token {want}")

if sizes["header"]["$value"] != by_role["header"]["height"]:
    errors.append("header")
if sizes["sell"]["$value"] != by_role["sell"]["height"]:
    errors.append("sell")
if sizes["search"]["$value"] != by_role["search"]["height"]:
    errors.append("search")
if tokens["core"]["radius"]["sell"]["$value"] != by_role["sell"]["borderRadius"]:
    errors.append("radius")
if "HelveticaNowText" not in tokens["core"]["font"]["ui"]["$value"]:
    errors.append("font")
if "Albra-Regular" not in tokens["core"]["font"]["display"]["$value"]:
    errors.append("display")

unverified = [
    "page (sampled #ffffff from home-light-1440.png; computed body background is transparent)",
    "hairline (sampled #ececec from home-light-1440.png)",
    "footer (black block; computed footer background is transparent)",
]
if errors:
    print("mismatch:", "; ".join(errors))
    sys.exit(1)
print("tokens match readings")
print("not checked against readings.json:")
for line in unverified:
    print(" ", line)
