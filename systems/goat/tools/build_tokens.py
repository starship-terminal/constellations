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
    (hex_of(by_role["body-interior"]["color"]), colors["ink"]["$value"], "ink"),
    (hex_of(by_role["body-interior"]["background"]), colors["page"]["$value"], "page"),
    (hex_of(by_role["body-home"]["background"]), colors["home"]["$value"], "home"),
    (hex_of(by_role["body-home"]["color"]), colors["on-home"]["$value"], "on-home"),
    (hex_of(by_role["signup"]["background"]), colors["signup"]["$value"], "signup"),
    (hex_of(by_role["signup"]["color"]), colors["on-signup"]["$value"], "on-signup"),
]
for got, want, name in checks:
    if got != want:
        errors.append(f"{name}: reading {got} token {want}")

type_checks = [
    ("body", "body-interior", "fontSize", "fontSize"),
    ("body", "body-interior", "fontWeight", "fontWeight"),
    ("nav", "nav", "fontSize", "fontSize"),
    ("nav", "nav", "fontWeight", "fontWeight"),
    ("category", "category-title", "fontSize", "fontSize"),
    ("category", "category-title", "fontWeight", "fontWeight"),
    ("product", "product-title", "fontSize", "fontSize"),
    ("about", "about-title", "fontWeight", "fontWeight"),
    ("button", "signup", "fontSize", "fontSize"),
    ("price", "price", "fontSize", "fontSize"),
    ("footer-link", "footer-link", "fontSize", "fontSize"),
    ("menu-heading", "menu-heading", "fontSize", "fontSize"),
]
for token_name, role, token_key, reading_key in type_checks:
    got = str(by_role[role][reading_key])
    want = str(type_tokens[token_name]["$value"][token_key])
    if got != want:
        errors.append(f"{token_name}.{token_key}: reading {got} token {want}")

if sizes["header"]["$value"] != by_role["header-home"]["height"]:
    errors.append("header")
if sizes["signup"]["$value"] != by_role["signup"]["height"]:
    errors.append("signup")
if sizes["field"]["$value"] != by_role["email-field"]["wrapperHeight"]:
    errors.append("field")
if sizes["menu"]["$value"] != by_role["menu-panel"]["width"]:
    errors.append("menu")
if tokens["core"]["radius"]["control"]["$value"] != by_role["signup"]["borderRadius"]:
    errors.append("radius")
if "GOATProductVariableVF" not in tokens["core"]["font"]["ui"]["$value"]:
    errors.append("font")

# Painted samples the script cannot read from readings.json.
unverified = [
    "hairline (sampled #515151 from category-light-1440.png; computed rgba(0, 0, 0, 0.7))",
    "hairline-home (sampled #aeaeae from home-light-1440.png; computed rgba(255, 255, 255, 0.7))",
    "field-border (computed rgba(0, 0, 0, 0.25), recorded as #bfbfbf)",
]
if errors:
    print("mismatch:", "; ".join(errors))
    sys.exit(1)
print("tokens match readings")
print("not checked against readings.json:")
for item in unverified:
    print("-", item)
