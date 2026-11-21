#!/usr/bin/env python3
"""Check that tokens.json still matches raw/readings.json. Does not rewrite tokens."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())


def hex_of(rgb):
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts[:3]))


by_role = {r["role"]: r for r in readings["readings"]}
colors = tokens["core"]["color"]
type_tokens = tokens["core"]["typography"]
sizes = tokens["core"]["size"]
errors = []

checks = [
    (hex_of(by_role["ink"]["color"]), colors["ink"]["$value"], "ink"),
    (hex_of(by_role["body"]["color"]), colors["quiet"]["$value"], "quiet"),
    (hex_of(by_role["body"]["background"]), colors["page"]["$value"], "page"),
    (hex_of(by_role["header"]["background"]), colors["surface"]["$value"], "surface"),
    (hex_of(by_role["search"]["background"]), colors["search"]["$value"], "search"),
    (hex_of(by_role["sell"]["background"]), colors["teal"]["$value"], "teal"),
    (hex_of(by_role["sell"]["color"]), colors["on-teal"]["$value"], "on-teal"),
    (hex_of(by_role["chip-selected"]["background"]), colors["chip"]["$value"], "chip"),
    (hex_of(by_role["how-band"]["background"]), colors["mint"]["$value"], "mint"),
    (hex_of(by_role["hairline"]["sampled"]), colors["hairline"]["$value"], "hairline"),
]
for got, want, name in checks:
    if got != want:
        errors.append(f"{name}: reading {got} token {want}")

type_checks = [
    ("body", "body", "fontSize"),
    ("nav", "nav", "fontSize"),
    ("search", "search-input", "fontSize"),
    ("button", "sell", "fontSize"),
    ("hero", "hero-title", "fontSize"),
    ("hero-button", "hero-sell", "fontSize"),
    ("category", "category-title", "fontSize"),
    ("about", "about-title", "fontSize"),
    ("price", "price", "fontSize"),
    ("footer-link", "footer-link", "fontSize"),
    ("menu-link", "menu-link", "fontSize"),
]
for token_name, role, key in type_checks:
    got = str(by_role[role][key])
    want = str(type_tokens[token_name]["$value"][key])
    if got != want:
        errors.append(f"{token_name}.{key}: reading {got} token {want}")

if sizes["header"]["$value"] != by_role["header"]["height"]:
    errors.append("header")
if sizes["sell"]["$value"] != by_role["sell"]["height"]:
    errors.append("sell")
if sizes["search"]["$value"] != by_role["search"]["height"]:
    errors.append("search")
if tokens["core"]["radius"]["control"]["$value"] != by_role["sell"]["borderRadius"]:
    errors.append("radius")
if "V_INTER" not in tokens["core"]["font"]["ui"]["$value"]:
    errors.append("font")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("tokens match readings")
