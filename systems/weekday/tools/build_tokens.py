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
    (hex_of(by_role["nav"]["color"]), colors["ink"]["$value"], "ink"),
    (hex_of(by_role["body"]["color"]), colors["ink-black"]["$value"], "ink-black"),
    (hex_of(by_role["body"]["background"]), colors["page"]["$value"], "page"),
    (hex_of(by_role["promo"]["background"]), colors["promo"]["$value"], "promo"),
    (hex_of(by_role["promo"]["color"]), colors["on-promo"]["$value"], "on-promo"),
    (hex_of(by_role["sale"]["color"]), colors["sale"]["$value"], "sale"),
    (hex_of(by_role["primary"]["background"]), colors["button"]["$value"], "button"),
    (hex_of(by_role["primary"]["color"]), colors["on-button"]["$value"], "on-button"),
    (hex_of(by_role["footer-border"]["border"].split("solid ", 1)[-1]), colors["footer-line"]["$value"], "footer-line"),
]
for got, want, name in checks:
    if got != want:
        errors.append(f"{name}: reading {got} token {want}")

type_checks = [
    ("body", "body", "fontSize", "fontSize"),
    ("body", "body", "fontWeight", "fontWeight"),
    ("nav", "nav", "fontSize", "fontSize"),
    ("promo", "promo", "fontSize", "fontSize"),
    ("home", "home-title", "fontSize", "fontSize"),
    ("hero", "hero-title", "fontSize", "fontSize"),
    ("sale", "sale", "fontSize", "fontSize"),
    ("product", "product-title", "fontSize", "fontSize"),
    ("about", "about-title", "fontSize", "fontSize"),
    ("footer-heading", "footer-heading", "fontSize", "fontSize"),
    ("footer-link", "footer-link", "fontSize", "fontSize"),
    ("button", "add-to-cart", "fontSize", "fontSize"),
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
if sizes["button"]["$value"] != by_role["primary"]["height"]:
    errors.append("button")
if tokens["core"]["radius"]["control"]["$value"] != by_role["join"]["borderRadius"]:
    errors.append("radius")
if "weekdayRegularFont" not in tokens["core"]["font"]["ui"]["$value"]:
    errors.append("font")

unverified = [
    "promo screenshot sample #ffff55 (computed rgb(255, 255, 3) is the token)",
    "border (computed JOIN NOW border rgb(29, 29, 27))",
]
if errors:
    print("mismatch:", "; ".join(errors))
    sys.exit(1)
print("tokens match readings")
print("not checked against readings.json:")
for item in unverified:
    print("-", item)
