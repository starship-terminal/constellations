#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

FlutterFlow's public site (www.flutterflow.io, Astro) declares a named token
set on :root as --ff-* (and a shorter alias set --page, --ink, ...). Dark
overrides live on :root[data-theme="dark"] and :root:not([data-theme="light"]).
Switching data-theme on <html> paints the page; this capture did that and
recorded the computed result in resolved.dark.

Duplicate declarations (desktop then a later mobile override in the same
sheet) keep the first desktop value. A later identical name on a different
selector is a theme override, not a replacement.

Deterministic: same inputs, byte-identical output. Edit the raw file, never
tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())

COLOR = re.compile(
    r"^(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)|hsla?\([^)]+\))$"
)
LENGTH = re.compile(r"^(-?\d+(?:\.\d+)?)(px|rem|em)$")
DURATION = re.compile(r"^(-?\d+(?:\.\d+)?)(ms|s)$")


def first_decls(selector):
    seen = {}
    for d in RAW["decls"]:
        if d.get("selector") != selector or not d.get("name", "").startswith("--"):
            continue
        seen.setdefault(d["name"], d["value"])
    return seen


LIGHT = first_decls(":root")
DARK = first_decls(':root[data-theme="dark"]')


def token(value, typ, source):
    return {"$value": value, "$type": typ, "$extensions": {"source": source}}


def nest(tree, parts, leaf):
    node = tree
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def classify(name, value):
    if name.startswith("--ff-color-") or name in {
        "--page", "--app", "--tender", "--card", "--card-2", "--ink", "--ink-2",
        "--muted", "--faint", "--line", "--accent", "--success", "--btn",
        "--btn-ink", "--sb", "--accent-ink", "--edge", "--line-1",
    }:
        return "color"
    if name.startswith("--ff-radius-") or name in {"--r-page"}:
        return "radius"
    if name.startswith("--ff-space-") or name in {"--gutter", "--sec", "--head-gap"}:
        return "space"
    if name.startswith("--ff-shadow-") or name == "--fsh":
        return "shadow"
    if name.startswith("--ff-duration-") or name in {"--d1", "--d2"}:
        return "duration"
    if name.startswith("--ff-ease-") or name in {"--ease", "--ease-ui", "--sp-soft"}:
        return "cubicBezier"
    if name.startswith("--ff-font-") or name in {"--sans", "--mono"}:
        return "fontFamily"
    if name.startswith("--ff-text-") and not name.endswith("-tracking"):
        return "typography"
    if name.startswith("--ff-size-") or name in {"--hair", "--ff-border-hair", "--ff-focus-width", "--ff-focus-offset", "--ff-size-bar"}:
        return "sizing"
    if name.startswith("--ff-z-"):
        return "number"
    if COLOR.match(value.strip()):
        return "color"
    return None


def path_for(name, kind):
    short = name[2:]
    if short.startswith("ff-"):
        short = short[3:]
    parts = short.replace("_", "-").split("-")
    if kind == "color" and parts and parts[0] == "color":
        parts = parts[1:]
    if kind == "radius" and parts and parts[0] == "radius":
        parts = parts[1:]
    if kind == "space" and parts and parts[0] == "space":
        parts = parts[1:]
    if kind == "shadow" and parts and parts[0] == "shadow":
        parts = parts[1:]
    if kind == "duration" and parts and parts[0] == "duration":
        parts = parts[1:]
    if kind == "cubicBezier" and parts and parts[0] == "ease":
        parts = parts[1:] or ["ui"]
    if kind == "fontFamily" and parts and parts[0] == "font":
        parts = parts[1:]
    if kind == "typography" and parts and parts[0] == "text":
        parts = parts[1:]
    if kind == "sizing" and parts and parts[0] == "size":
        parts = parts[1:]
    if kind == "number" and parts and parts[0] == "z":
        parts = ["z"] + parts[1:]
    return parts


def typed_value(kind, value):
    v = value.strip()
    if kind == "color":
        return v
    if kind == "duration":
        m = DURATION.match(v)
        if not m:
            return None
        num, unit = m.group(1), m.group(2)
        if unit == "ms":
            return f"{float(num) / 1000:g}s"
        return f"{float(num):g}s"
    if kind == "cubicBezier":
        m = re.fullmatch(r"cubic-bezier\(([^)]+)\)", v)
        if not m:
            return None
        return [float(x) for x in m.group(1).split(",")]
    if kind == "number":
        try:
            return int(v) if re.fullmatch(r"-?\d+", v) else float(v)
        except ValueError:
            return None
    if kind == "typography":
        # 600 clamp(44px, 4.6vw, 66px)/1.03 var(--ff-font-sans)
        m = re.match(
            r"(\d+)\s+(clamp\([^)]+\)|\d+(?:\.\d+)?px)\/([0-9.]+(?:px)?)\s+(.+)$",
            v,
        )
        if not m:
            return None
        weight, size, lh, family = m.groups()
        if re.fullmatch(r"[0-9.]+", lh):
            lh = str(float(lh))
        return {
            "fontWeight": int(weight),
            "fontSize": size,
            "lineHeight": lh,
            "fontFamily": family.strip(),
        }
    if kind in {"radius", "space", "sizing"}:
        if v.startswith("clamp(") or LENGTH.match(v) or v.endswith("px"):
            return v
        return None
    if kind == "fontFamily":
        return v
    if kind == "shadow":
        return v
    return v


def build_set(decls, source_sel):
    core_bits = {
        "color": {},
        "radius": {},
        "space": {},
        "shadow": {},
        "duration": {},
        "easing": {},
        "fontFamily": {},
        "typography": {},
        "sizing": {},
        "z": {},
    }
    skipped = []
    for name, value in decls.items():
        if not name.startswith("--ff-") and name not in {
            "--page", "--ink", "--muted", "--accent", "--line", "--btn", "--btn-ink",
        }:
            continue
        kind = classify(name, value)
        if kind is None:
            skipped.append({"name": name, "value": value[:80], "why": "not a token kind"})
            continue
        typed = typed_value(kind, value)
        if typed is None:
            skipped.append({"name": name, "value": value[:120], "why": "unparsed " + kind})
            continue
        src = f"css-var {name} on {source_sel}"
        leaf = token(typed, kind if kind != "cubicBezier" else "cubicBezier", src)
        parts = path_for(name, kind)
        bucket = {
            "color": "color",
            "radius": "radius",
            "space": "space",
            "shadow": "shadow",
            "duration": "duration",
            "cubicBezier": "easing",
            "fontFamily": "fontFamily",
            "typography": "typography",
            "sizing": "sizing",
            "number": "z",
        }[kind]
        nest(core_bits[bucket], parts, leaf)
    return core_bits, skipped


def semantic_from(resolved, label):
    """Role tokens from the computed theme, so light and dark are painted values."""
    roles = {
        "page": "--ff-color-page",
        "surface": "--ff-color-card",
        "raised": "--ff-color-card-2",
        "well": "--ff-color-well",
        "text": "--ff-color-ink",
        "textSecondary": "--ff-color-ink-2",
        "muted": "--ff-color-muted",
        "faint": "--ff-color-faint",
        "border": "--ff-color-line",
        "accent": "--ff-color-accent",
        "accentInk": "--ff-color-accent-ink",
        "onAccent": "--ff-color-send-ink",
        "focus": "--ff-color-focus",
        "success": "--ff-color-success",
        "danger": "--ff-color-danger",
        "button": "--ff-color-contrast",
        "buttonInk": "--ff-color-contrast-ink",
        "studio": "--ff-color-studio-ink",
        "studioTint": "--ff-color-studio-tint",
    }
    out = {}
    for role, var in roles.items():
        value = resolved.get(var) or resolved.get(var.replace("--ff-color-", "--"))
        if not value:
            continue
        out[role] = token(value, "color", f"computed {var} with data-theme={label} on html")
    return out


light_resolved = RAW["resolved"]["light"]
dark_resolved = RAW["resolved"]["dark"]
core_bits, skipped = build_set(LIGHT, ":root")

# Keep scales in core. Semantic colour roles live in light and dark.
core = {
    "color": core_bits["color"],
    "radius": core_bits["radius"],
    "space": core_bits["space"],
    "shadow": core_bits["shadow"],
    "duration": core_bits["duration"],
    "easing": core_bits["easing"],
    "fontFamily": core_bits["fontFamily"],
    "typography": core_bits["typography"],
    "sizing": core_bits["sizing"],
    "z": core_bits["z"],
}

doc = {
    "core": core,
    "light": semantic_from(light_resolved, "light"),
    "dark": semantic_from(dark_resolved, "dark"),
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "skipped": skipped,
        "note": "Public site tokens from www.flutterflow.io on 2026-11-21. Dark values are computed after setting data-theme=dark on html. Signed-in app tokens were not captured.",
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "skipped", len(skipped))
