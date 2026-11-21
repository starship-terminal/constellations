#!/usr/bin/env python3
"""Check tokens.json against the measured public-site readings.

PRODUCT (adapt): Ulysses public marketing site, captured 2026-11-22.
catalog.json was left alone, so this does not regenerate DESIGN.md.
"""
import json
import pathlib
import sys

ADAPTED_FOR = "Ulysses"

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
tokens = json.loads((HERE / "tokens.json").read_text())
home = json.loads((RAW / "home-computed.json").read_text())
pricing = json.loads((RAW / "pricing-computed.json").read_text())
login = json.loads((RAW / "login-computed.json").read_text())


def rgb_to_hex(value):
    parts = value.removeprefix("rgb(").removesuffix(")").split(",")
    nums = [int(p.strip()) for p in parts]
    return "#{:02x}{:02x}{:02x}".format(*nums)


errors = []
ink = rgb_to_hex(home["body"]["color"])
page = rgb_to_hex(home["body"]["backgroundColor"])
footer = rgb_to_hex(pricing["footer"]["backgroundColor"])
accent = rgb_to_hex(login["submit"]["border"].split("rgb(")[1].removesuffix(")"))
field = rgb_to_hex(login["email"]["backgroundColor"])

expect = {
    "core.color.ink": ink,
    "core.color.page": page,
    "core.color.footer": footer,
    "core.color.accent": accent,
    "core.color.field": field,
}
flat = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.footer": tokens["core"]["color"]["footer"]["$value"],
    "core.color.accent": tokens["core"]["color"]["accent"]["$value"],
    "core.color.field": tokens["core"]["color"]["field"]["$value"],
}
for key, want in expect.items():
    got = flat[key]
    if got.lower() != want:
        errors.append(f"{key} is {got}, reading is {want}")

if tokens["core"]["typography"]["display"]["$value"]["fontSize"] != home["h2"]["fontSize"]:
    errors.append("display size does not match the homepage h2")
if tokens["core"]["typography"]["body"]["$value"]["fontSize"] != home["body"]["fontSize"]:
    errors.append("body size does not match")
if "interstate" not in tokens["core"]["font"]["family"]["ui"]["$value"]:
    errors.append("ui family does not name interstate")
if tokens["light"]["color"]["page"]["$value"] != "{core.color.page}":
    errors.append("light page is not an alias of the measured page")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("tokens match the Ulysses readings")
