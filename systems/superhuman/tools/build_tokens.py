#!/usr/bin/env python3
"""Check the hand-written Superhuman tokens against the CSS readings.

ADAPTED_FOR = "Superhuman"
The tokens file is written from measured computed styles.
This script does not rewrite tokens.json. It fails if a named reading disagrees.
"""
ADAPTED_FOR = "Superhuman"

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
pricing = json.loads((ROOT / "raw" / "pricing-computed.json").read_text())
auth = json.loads((ROOT / "raw" / "auth-computed.json").read_text())
home = json.loads((ROOT / "raw" / "home-computed.json").read_text())
biz = json.loads((ROOT / "raw" / "biz-computed.json").read_text())

failed = 0


def need(label, value, needle):
    global failed
    if needle not in value:
        print(f"mismatch {label}: {value}")
        failed += 1


need("ink", pricing["h1"]["color"], "rgb(41, 40, 39)")
need("violet", biz["bg"], "rgb(113, 76, 182)")
need("auth violet", auth["emailBtn"]["bg"], "rgb(113, 76, 182)")
need("home h1", home["h1"]["size"], "64px")
need("font", home["body"]["font"], "Super Sans VF")
if tokens["core"]["color"]["violet"]["$value"] != "#714cb6":
    print("violet token drifted")
    failed += 1
if tokens["core"]["color"]["ink"]["$value"] != "#292827":
    print("ink token drifted")
    failed += 1
if tokens["light"]["color"]["action"]["fill"]["$value"] != "{core.color.violet}":
    print("action fill drifted")
    failed += 1
if failed:
    sys.exit(1)
print("superhuman tokens match the named CSS readings")
