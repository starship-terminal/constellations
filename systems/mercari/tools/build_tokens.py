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
errors = []

checks = [
    (hex_of(by_role["body"]["color"]), colors["ink"]["$value"], "ink"),
    (hex_of(by_role["body"]["background"]), colors["page"]["$value"], "page"),
    (hex_of(by_role["header-home"]["background"]), colors["navy"]["$value"], "navy"),
    (hex_of(by_role["login"]["color"]), colors["on-navy"]["$value"], "on-navy"),
    (hex_of(by_role["category-label"]["color"]), colors["primary"]["$value"], "primary"),
    (hex_of(by_role["about-title"]["color"]), colors["on-primary"]["$value"], "on-primary"),
    (hex_of(by_role["search"]["background"]), colors["field"]["$value"], "field"),
    (hex_of(by_role["price"]["color"]), colors["muted"]["$value"], "muted"),
    (hex_of(by_role["favicon"]["fill"]), colors["mark"]["$value"], "mark"),
    (hex_of(by_role["sell"]["background"]), colors["on-navy"]["$value"], "sell fill is white"),
    (hex_of(by_role["list-an-item"]["background"]), colors["primary"]["$value"], "list-an-item"),
    (hex_of(by_role["footer-navy"]["background"]), colors["navy"]["$value"], "footer navy"),
    (hex_of(by_role["legal-bar"]["background"]), colors["field"]["$value"], "legal bar"),
]
for got, want, name in checks:
    if got != want:
        errors.append(f"{name}: reading {got} token {want}")

type_checks = [
    ("body", "body", "fontSize", "fontSize"),
    ("body", "body", "fontWeight", "fontWeight"),
    ("nav", "login", "fontSize", "fontSize"),
    ("nav", "login", "fontWeight", "fontWeight"),
    ("category", "category-label", "fontSize", "fontSize"),
    ("section", "section-title", "fontSize", "fontSize"),
    ("page-title", "category-title", "fontSize", "fontSize"),
    ("hero", "about-title", "fontSize", "fontSize"),
    ("button", "sell", "fontSize", "fontSize"),
    ("legal", "legal-link", "fontSize", "fontSize"),
]
for token_name, role, token_key, reading_key in type_checks:
    got = str(by_role[role][reading_key])
    want = str(type_tokens[token_name]["$value"][token_key])
    if got != want:
        errors.append(f"{token_name}.{token_key}: reading {got} token {want}")

if by_role["body"]["fontFamily"] != tokens["core"]["font"]["ui"]["$value"]:
    errors.append("font")
if by_role["search"]["borderRadius"] != tokens["core"]["radius"]["pill"]["$value"]:
    errors.append("radius pill")
if by_role["sell"]["borderRadius"] != tokens["core"]["radius"]["button"]["$value"]:
    errors.append("radius button")
if by_role["header-home"]["height"] != tokens["core"]["size"]["header"]["$value"]:
    errors.append("header height")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("tokens match readings")
