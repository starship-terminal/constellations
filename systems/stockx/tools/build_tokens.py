#!/usr/bin/env python3
"""Check systems/stockx/tokens.json against raw/readings.json. No writes."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
core = tokens["core"]
failed = []


def check(name, got, want):
    if got != want:
        failed.append(f"{name}: token {got!r} readings {want!r}")


check("page", core["color"]["page"]["$value"], readings["tokens"]["--colors-background-primary"])
check("surface", core["color"]["surface"]["$value"], readings["tokens"]["--colors-background-secondary"])
check("footer", core["color"]["footer"]["$value"], readings["tokens"]["--colors-background-tertiary"])
check("text", core["color"]["text"]["$value"], readings["tokens"]["--colors-text-primary"])
check("text-secondary", core["color"]["text-secondary"]["$value"], readings["tokens"]["--colors-text-secondary"])
check("brand", core["color"]["brand"]["$value"], readings["tokens"]["--colors-brand-primary"])
check("border-strong", core["color"]["border-strong"]["$value"], readings["tokens"]["--colors-border-secondary"])
check("deals", core["color"]["deals"]["$value"], readings["tokens"]["--colors-status-error"])
check("success", core["color"]["success"]["$value"], readings["tokens"]["--colors-status-success"])
check("warning", core["color"]["warning"]["$value"], readings["tokens"]["--colors-status-warning"])
check("ui font", core["font"]["ui"]["$value"], "SuisseIntl, sans-serif")
check("search radius", core["radius"]["search"]["$value"], readings["computed"]["search"]["radius"])
check("signup radius", core["radius"]["pill"]["$value"], readings["computed"]["signup"]["radius"])
check("header", core["size"]["header"]["$value"], f"{readings['computed']['header']['height']}px")
check("category bar", core["size"]["category-bar"]["$value"], f"{readings['computed']['categoryBar']['height']}px")
check("search height", core["size"]["search"]["$value"], f"{readings['computed']['search']['height']}px")
check("buy height", core["size"]["buy"]["$value"], f"{readings['product']['buyNow']['height']}px")
check("display size", core["typography"]["display"]["$value"]["fontSize"], readings["about"]["h1"]["fontSize"])
check("title size", core["typography"]["title"]["$value"]["fontSize"], readings["product"]["h1"]["fontSize"])
check("section size", core["typography"]["section"]["$value"]["fontSize"], readings["computed"]["sectionHeading"]["fontSize"])
check("price size", core["typography"]["price"]["$value"]["fontSize"], readings["computed"]["price"]["fontSize"])
check("body size", core["typography"]["body"]["$value"]["fontSize"], readings["page"]["bodySize"])
check("button size", core["typography"]["button"]["$value"]["fontSize"], readings["computed"]["signup"]["fontSize"])
check("fast", core["duration"]["fast"]["$value"], readings["tokens"]["--durations-fast"])
check("md", core["breakpoint"]["md"]["$value"], readings["tokens"]["--breakpoints-md"])

if failed:
    print("tokens do not match readings:")
    print("\n".join(failed))
    sys.exit(1)
print("tokens match readings")
