#!/usr/bin/env python3
"""The New York Times package checks: tokens rebuild, aliases resolve, shots exist.

Run from the package folder: python3 tools/test_build_tokens.py
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "tools"))
from build_tokens import doc  # noqa: E402


def fail(msg):
    print("FAIL", msg)
    raise SystemExit(1)


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    import re
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


core_names = {n for n, _ in tokens_of(doc["core"])}
light_names = core_names | {n for n, _ in tokens_of(doc["light"])}
for n, tok in tokens_of(doc["light"]):
    for a in aliases(tok["$value"]):
        if a not in light_names:
            fail(f"light.{n} alias {{{a}}} points at nothing")
    if "source" not in tok.get("$extensions", {}):
        fail(f"light.{n} has no source")

ink = doc["core"]["color"]["ink"]["$value"]
if ink != "#121212":
    fail(f"ink is {ink}")
if "dark" in doc:
    fail("this account had no dark theme")
if doc["core"]["spacing"]["2"]["$value"] != "1rem":
    fail("spacing 2")

subprocess.check_call([sys.executable, str(HERE / "tools" / "build_tokens.py")], cwd=HERE)
written = json.loads((HERE / "tokens.json").read_text())
if written != doc:
    fail("tokens.json drifted from build_tokens.py")

shots = [
    "account-settings-light.png",
    "saved-empty-light.png",
    "search-empty-light.png",
    "search-typed-light.png",
    "section-nav-light.png",
    "account-phone.png",
    "account-nav-phone.png",
]
for name in shots:
    png = HERE / "screenshots" / name
    side = HERE / "screenshots" / f"{name}.capture.json"
    if not png.is_file() or not side.is_file():
        fail(f"missing {name}")
    rec = json.loads(side.read_text())
    if rec["innerWidth"] not in (1440, 390):
        fail(f"{name} width {rec['innerWidth']}")

review = json.loads((HERE / "login-review.json").read_text())
for key in ("offered", "screens", "gaps", "not_submitted"):
    if key not in review:
        fail(f"login-review missing {key}")
if len(review["screens"]) < 2:
    fail("need at least two screens")

print("ok", len(list(tokens_of(doc["core"]))), "core tokens,", len(shots), "screens")
