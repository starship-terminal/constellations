#!/usr/bin/env python3
"""Check TrainingPeaks tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.navy": readings["home"]["athleteSignUp"]["backgroundColor"],
    "core.color.on-navy": readings["home"]["athleteSignUp"]["color"],
    "core.color.blue": readings["home"]["coachSignUp"]["backgroundColor"],
    "core.color.on-blue": readings["home"]["coachSignUp"]["color"],
    "core.color.link": readings["home"]["login"]["color"],
    "core.color.nav": readings["home"]["navLabel"]["color"],
    "core.color.ink": readings["home"]["body"]["color"],
    "core.color.heading": readings["features"]["h2"]["color"],
}

want_hex = {
    "core.color.navy": "#010f31",
    "core.color.on-navy": "#ffffff",
    "core.color.blue": "#3177ff",
    "core.color.on-blue": "#ffffff",
    "core.color.link": "#3177ff",
    "core.color.nav": "#64748b",
    "core.color.ink": "#000000",
    "core.color.heading": "#27303f",
}

want_rgb = {
    "core.color.navy": "rgb(1, 15, 49)",
    "core.color.on-navy": "rgb(255, 255, 255)",
    "core.color.blue": "rgb(49, 119, 255)",
    "core.color.on-blue": "rgb(255, 255, 255)",
    "core.color.link": "rgb(49, 119, 255)",
    "core.color.nav": "rgb(100, 116, 139)",
    "core.color.ink": "rgb(0, 0, 0)",
    "core.color.heading": "rgb(39, 48, 63)",
}

hexes = {key: tokens["core"]["color"][key.split(".")[-1]]["$value"] for key in expect}

failed = False
for key, rgb in expect.items():
    if rgb != want_rgb[key] or hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

props = readings["home"]["customProperties"]
if props["--wp--preset--color--brand-navy"] != "#010F31":
    print("mismatch brand-navy")
    failed = True
if props["--wp--preset--color--brand-blue"] != "#3177FF":
    print("mismatch brand-blue")
    failed = True
if "241, 253, 83" not in readings["home"]["bannerPaint"]["backgroundImage"]:
    print("mismatch lime paint")
    failed = True
if tokens["core"]["color"]["lime"]["$value"] != "#f1fd53":
    print("mismatch lime token")
    failed = True
if "EncodeSansExpanded-ExtraBold" not in readings["home"]["h1"]["fontFamily"]:
    print("mismatch display font")
    failed = True
if readings["home"]["heroAthlete"]["borderRadius"] != "9999px":
    print("mismatch hero radius")
    failed = True
if readings["features"]["signup"]["backgroundColor"] != "rgb(49, 119, 255)":
    print("mismatch features signup")
    failed = True
if readings["home"]["footer"]["backgroundColor"] != "rgb(1, 15, 49)":
    print("mismatch footer")
    failed = True

if failed:
    sys.exit(1)
print("trainingpeaks tokens match raw/readings.json")
