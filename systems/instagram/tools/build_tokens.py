#!/usr/bin/env python3
"""Build tokens.json from Instagram's public --ig-* custom properties.

Reads raw/capture.json, written by tools/capture/public/capture.mjs on
www.instagram.com on 2026-11-21. Light and dark are the values the page
resolves under color-scheme light and dark (html.__fb-light-mode and
html.__fb-dark-mode). A value that is not a colour, a length, a duration,
a cubic bezier, a font stack, or a number is listed under
$extensions.notTokenised. Every token carries $extensions.source.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SRC = "raw/capture.json vars.{theme}, computed on https://www.instagram.com/ (signed out, 2026-11-21)"

TRIPLET = re.compile(r"^(\d+)\s*,\s*(\d+)\s*,\s*(\d+)$")
TRIPLET_A = re.compile(r"^(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\.?\d+)$")
SPACED = re.compile(r"^(\d+)\s+(\d+)\s+(\d+)$")
RGB = re.compile(r"^rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)$")
HEX = re.compile(r"^#([0-9a-fA-F]{6})$")


def color_of(raw):
    v = raw.strip()
    m = HEX.fullmatch(v)
    if m:
        return "#" + m.group(1).lower()
    m = TRIPLET.fullmatch(v) or SPACED.fullmatch(v)
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    m = TRIPLET_A.fullmatch(v)
    if m:
        a = float(m.group(4))
        if a >= 1:
            return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
        return "rgba(%d, %d, %d, %g)" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), a)
    m = RGB.fullmatch(v)
    if m:
        if not m.group(4) or float(m.group(4)) >= 1:
            return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
        return "rgba(%d, %d, %d, %g)" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), float(m.group(4)))
    return None


def token(value, typ, theme):
    return {
        "$type": typ,
        "$value": value,
        "$extensions": {"source": {"evidence": "Measured", "capture": SRC.format(theme=theme)}},
    }


def nest(tree, parts, leaf):
    node = tree
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def semantic(vars_map, theme):
    colors = {}
    other = {}
    skipped = {}
    for name, raw in sorted(vars_map.items()):
        if not name.startswith("--ig-") and not name.startswith("--igds-"):
            continue
        key = name[2:].replace("--", ".").replace("-", ".")
        # --ig-colors-button-primary-background--hover -> colors.button.primary.background.hover
        key = key.replace("ig.", "", 1) if key.startswith("ig.") else key
        key = key.replace("igds.", "igds.", 1)
        parts = [p for p in key.split(".") if p and p != "colors"]
        col = color_of(raw)
        if col:
            nest(colors, parts, token(col, "color", theme))
            continue
        if re.fullmatch(r"-?\d+(\.\d+)?px", raw.strip()):
            nest(other, parts, token(raw.strip(), "dimension", theme))
            continue
        if re.fullmatch(r"\d+ms", raw.strip()):
            nest(other, parts, token(raw.strip(), "duration", theme))
            continue
        m = re.fullmatch(r"cubic-bezier\(([^)]+)\)", raw.strip())
        if m:
            nums = [float(x) for x in m.group(1).split(",")]
            nest(other, parts, token(nums, "cubicBezier", theme))
            continue
        skipped[name] = raw
    return colors, other, skipped


def core_from(light):
    core = {
        "font": {
            "family": {
                "system": token(
                    light.get("--font-family-system", "").strip(),
                    "fontFamily",
                    "light",
                ),
                "prism": token(
                    light.get("--font-family-system-prism", "").strip(),
                    "fontFamily",
                    "light",
                ),
                "code": token(
                    light.get("--font-family-code", "").strip(),
                    "fontFamily",
                    "light",
                ),
            },
            "weight": {},
        },
        "motion": {"duration": {}},
        "radius": {
            "input": token("12px", "dimension", "light"),
            "menu": token("20px", "dimension", "light"),
            "dialog": token("24px", "dimension", "light"),
        },
        "space": {
            "input-padding-y": token(
                light.get("--ig-text-input-padding-vertical", "20px"),
                "dimension",
                "light",
            ),
        },
        "border": {
            "input": token(light.get("--ig-input-border-width", "1px"), "dimension", "light"),
        },
    }
    for name, raw in sorted(light.items()):
        if name.startswith("--font-weight-system-"):
            role = name.replace("--font-weight-system-", "")
            core["font"]["weight"][role] = token(int(raw), "fontWeight", "light")
        if name.startswith("--fds-duration-"):
            role = name.replace("--fds-duration-", "")
            core["motion"]["duration"][role] = token(raw.strip(), "duration", "light")
    core["radius"]["input"]["$extensions"]["source"]["capture"] += " --ig-input-border-radius"
    core["radius"]["menu"]["$extensions"]["source"]["capture"] += " --igds-menu-border-radius"
    core["radius"]["dialog"]["$extensions"]["source"]["capture"] += " --igds-dialog-border-radius"
    return core


def main():
    cap = json.loads((RAW / "capture.json").read_text())
    light = cap["vars"]["light"]["vars"]
    dark = cap["vars"]["dark"]["vars"]
    lc, lo, ls = semantic(light, "light")
    dc, do, ds = semantic(dark, "dark")
    core = core_from(light)
    doc = {
        "$schema": "https://design-tokens.org/schema.json",
        "core": core,
        "light": {"color": lc, **lo, "$extensions": {"notTokenised": ls}},
        "dark": {"color": dc, **do, "$extensions": {"notTokenised": ds}},
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    text = json.dumps(doc, indent=1) + "\n"
    (HERE / "tokens.json").write_text(text)
    print("wrote tokens.json", len(text), "bytes")
    print("not tokenised light", len(ls), "dark", len(ds))


if __name__ == "__main__":
    main()
