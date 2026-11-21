#!/usr/bin/env python3
"""Build tokens.json from Trip.com's declared custom properties.

Source: raw/css-vars.json, read from the public homepage CSSOM on 2026-11-21.
The site declares --core* primitives, --smtc* semantic roles, and --comp*
component tokens. No dark theme is declared. Every token carries
$extensions.source. A name that does not resolve is left out, not invented.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]
DECL = V["decls"]

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def norm_color(v):
    v = v.strip().lower()
    if v in ("transparent", "currentcolor"):
        return v
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8 and h[6:] == "ff":
            h = h[:6]
        if len(h) == 6:
            return "#" + h
        return v
    if v == "#fff":
        return "#ffffff"
    if v == "#000":
        return "#000000"
    return v


def camel_path(name):
    """--smtcColorTextPrimary -> color.text.primary"""
    body = name[2:]
    body = re.sub(r"^(smtc|core|comp)", "", body)
    parts = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])", body)
    return ".".join(p.lower() for p in parts)


def token(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def colour_token(name):
    raw = RES.get(name) or DECL[name]["raw"]
    val = norm_color(raw)
    if not (val.startswith("#") or val.startswith("rgb") or val in ("transparent", "currentcolor")):
        return None
    return token(val, "color", f"Measured custom property {name} on the public homepage CSSOM, 2026-11-21")


def dim_token(name):
    raw = (RES.get(name) or DECL[name]["raw"]).strip()
    if not DIM.fullmatch(raw):
        return None
    return token(raw, "dimension", f"Measured custom property {name} on the public homepage CSSOM, 2026-11-21")


def num_token(name):
    raw = (RES.get(name) or "").strip()
    if not re.fullmatch(r"\d+", raw):
        return None
    return token(int(raw), "fontWeight", f"Measured custom property {name} on the public homepage CSSOM, 2026-11-21")


core = {"color": {}, "font": {}, "radius": {}, "spacing": {}, "fontWeight": {}}
light = {"color": {}, "component": {}}
skipped = []

for name in sorted(DECL):
    if name.startswith("--coreColor"):
        t = colour_token(name)
        if t:
            core["color"][camel_path(name).removeprefix("color.")] = t
        else:
            skipped.append(name)
    elif name.startswith("--coreFontFamily"):
        raw = (RES.get(name) or DECL[name]["raw"]).strip().strip('"')
        core["font"][camel_path(name).split(".")[-1]] = token(
            raw, "fontFamily", f"Measured custom property {name} on the public homepage CSSOM, 2026-11-21"
        )
    elif name.startswith("--coreFontWeight"):
        t = num_token(name)
        if t:
            core["fontWeight"][camel_path(name).split(".")[-1]] = t
    elif name.startswith("--coreBorderRadius"):
        t = dim_token(name)
        if t:
            core["radius"][camel_path(name).removeprefix("borderradius.")] = t
    elif name.startswith("--coreSpacing") and "Negative" not in name:
        t = dim_token(name)
        if t:
            core["spacing"][camel_path(name).removeprefix("spacing.")] = t
    elif name.startswith("--smtcColor"):
        t = colour_token(name)
        if t:
            light["color"][camel_path(name).removeprefix("color.")] = t
        else:
            skipped.append(name)
    elif name.startswith("--compButton") and name.endswith(("BackgroundColor", "Color", "BorderColor", "Height", "BorderRadius", "FontSize")):
        raw = (RES.get(name) or "").strip()
        key = camel_path(name).removeprefix("button.")
        if raw.startswith("#") or raw.startswith("rgb") or raw in ("transparent",):
            light["component"].setdefault("button", {})[key] = colour_token(name)
        elif DIM.fullmatch(raw):
            light["component"].setdefault("button", {})[key] = dim_token(name)

# Roles the catalog-shaped preview would want, as aliases into measured smtc names.
roles = {
    "page": "bg.surface",
    "surface": "bg.surface.secondary",
    "text": "text.primary",
    "muted": "text.secondary",
    "accent": "bg.brand",
    "border": "border.default" if "border.default" in light["color"] else "text.tertiary",
}
# border.default may not exist; pick a measured border if present
border = next((k for k in light["color"] if k.startswith("border") and "default" in k), None)
if not border:
    border = next((k for k in light["color"] if "border" in k and light["color"][k]["$value"].startswith("#")), None)
if border:
    roles["border"] = border

for role, path in roles.items():
    if path in light["color"] or path.replace(".", ".") in light["color"]:
        light["color"][role] = {
            "$value": "{color." + path + "}",
            "$type": "color",
            "$extensions": {"source": f"Derived alias of measured smtc color.{path}"},
        }

doc = {
    "$description": "Trip.com public design tokens, measured from sg.trip.com CSSOM on 2026-11-21. Light only: no dark theme is declared.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "skipped": skipped[:40],
        "notCaptured": [
            "Dark theme: not declared on the public site.",
            "Motion durations and easings: no --* duration or easing names in the CSSOM reading.",
            "Elevation: no --* shadow names in the CSSOM reading.",
        ],
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("core colors", len(core["color"]), "radius", len(core["radius"]), "spacing", len(core["spacing"]))
print("light colors", len(light["color"]), "button", len(light["component"].get("button", {})))
print("wrote", out)
