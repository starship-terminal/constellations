#!/usr/bin/env python3
"""Build tokens.json from Klarna's declared Klarna UI custom properties.

Source: raw/css-vars.json, harvested 2026-11-18 from inline stylesheets on
www.klarna.com/us/ (and shopping, help, international). Light is
`:root, .klarna-ui-DEFAULT-light`. Dark is `.klarna-ui-DEFAULT-dark`.
The public marketing site paints light. Dark is declared and tokenised,
labelled as a declared theme rather than a live marketing capture.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]


def norm_color(v):
    v = str(v).strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a == 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b = (round(float(x)) for x in m.group(1, 2, 3))
        a = m.group(4)
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(float(a), 3))
    return v


def tok(val, ty, source):
    if ty == "color":
        val = norm_color(val)
    return {"$value": val, "$type": ty, "$extensions": {"source": source}}


def declared(theme):
    """Last declaration on the theme's own selector, ignoring widget themes."""
    sel = ":root, .klarna-ui-DEFAULT-light" if theme == "light" else ".klarna-ui-DEFAULT-dark"
    out = {}
    bucket = V.get("theme" if theme == "light" else "dark", [])
    for r in bucket:
        if r.get("context"):
            continue
        if r.get("selector") != sel:
            continue
        out.update(r["properties"])
    return out


DECL = {"light": declared("light"), "dark": declared("dark")}


def put(tree, path, token):
    """Place a token at a dotted path without nesting it inside another token.

    --colors-bg-brand and --colors-bg-brand-hover both split on "-", so the second
    would land inside the first token, where tools/catalog.py's flatten (it stops at
    $value) never sees it. When the walk reaches a token, the rest of the path stays
    joined with "-" as a sibling key (brand and brand-hover). A taken path raises.
    """
    node = tree
    parts = path.split(".")
    for i, p in enumerate(parts[:-1]):
        nxt = node.get(p)
        if isinstance(nxt, dict) and "$value" in nxt:
            parts = parts[:i] + ["-".join(parts[i:])]
            break
        node = node.setdefault(p, {})
    if parts[-1] in node:
        raise ValueError("token path already taken: " + ".".join(parts))
    node[parts[-1]] = token


def slug(name):
    return name.strip("-").replace("--", "").replace("_", "-")


core = {}
light = {}
dark = {}

# Colour roles from the resolved light/dark values of --colors-*
for name, rec in sorted(RES["light"].items()):
    if not name.startswith("--colors-"):
        continue
    path = "color." + name[len("--colors-"):].replace("-", ".")
    # flatten one level groups: color.bg.page
    src = f"css-var {name}, declared on :root, .klarna-ui-DEFAULT-light (raw/css-vars.json, 2026-11-18)"
    raw = rec.get("raw") or rec.get("value")
    put(light, path, tok(raw, "color", src))
    drec = RES["dark"].get(name) or {}
    draw = drec.get("raw") or drec.get("value")
    if not draw:  # never publish the light value under a dark source
        raise KeyError(f"{name}: no dark value in raw/css-vars.json")
    dsrc = f"css-var {name}, declared on .klarna-ui-DEFAULT-dark (raw/css-vars.json, 2026-11-18). Declared theme; the public marketing site paints light."
    put(dark, path, tok(draw, "color", dsrc))

# Scales from the light theme declaration (same numbers in dark).
SCALE_TYPE = {
    "spaces": "dimension",
    "radiuses": "dimension",
    "textSizes": "dimension",
    "lineHeights": "dimension",
    "shadows": "shadow",
    "fonts": "fontFamily",
    "weights": "fontWeight",
}
for name, raw in sorted(DECL["light"].items()):
    if name.startswith("--colors-"):
        continue
    parts = name[2:].split("-", 1)
    if len(parts) < 2:
        continue
    group, rest = parts
    ty = SCALE_TYPE.get(group)
    if not ty:
        continue
    # drop fluid calc() sizes: they are not a single px/rem length
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", raw.strip()):
        continue
    if ty == "fontWeight":
        if not re.fullmatch(r"\d+", raw.strip()):
            continue
        raw = int(raw)
    if ty == "fontFamily":
        raw = raw.strip().strip('"')
    if ty == "shadow":
        m = re.fullmatch(
            r"(-?\d+px)\s+(-?\d+px)\s+(-?\d+px)\s+(-?\d+px)\s+(rgba?\([^)]+\)|#[0-9a-fA-F]+)",
            raw.strip(),
        )
        if not m:
            continue
        raw = [{
            "color": norm_color(m.group(5)),
            "offsetX": m.group(1),
            "offsetY": m.group(2),
            "blur": m.group(3),
            "spread": m.group(4),
        }]
    path = group + "." + rest.replace("-", ".")
    # textSizes.display.desktop.3xl is fine
    put(core, path, tok(raw, ty, f"css-var {name}, declared on :root, .klarna-ui-DEFAULT-light"))

# Semantic aliases a reader can grab without walking color.bg.*
def alias(path, target, source):
    return {"$value": "{" + target + "}", "$type": "color", "$extensions": {"source": source}}


light["page"] = alias("page", "color.bg.page", "alias of --colors-bg-page")
light["surface"] = alias("surface", "color.bg.container", "alias of --colors-bg-container")
light["text"] = alias("text", "color.text.default", "alias of --colors-text-default")
light["muted"] = alias("muted", "color.text.subtle", "alias of --colors-text-subtle")
light["accent"] = alias("accent", "color.bg.brand", "alias of --colors-bg-brand, the pink pill")
light["border"] = alias("border", "color.border.default", "alias of --colors-border-default")
dark["page"] = alias("page", "color.bg.page", "alias of --colors-bg-page in dark")
dark["surface"] = alias("surface", "color.bg.container", "alias of --colors-bg-container in dark")
dark["text"] = alias("text", "color.text.default", "alias of --colors-text-default in dark")
dark["muted"] = alias("muted", "color.text.subtle", "alias of --colors-text-subtle in dark")
dark["accent"] = alias("accent", "color.bg.brand", "alias of --colors-bg-brand in dark")
dark["border"] = alias("border", "color.border.default", "alias of --colors-border-default in dark")

# Type composites from the fixed (non-fluid) display steps plus body 16.
core["typography"] = {
    "display-3xl": {
        "$value": {
            "fontFamily": "{fonts.font.brand.title}",
            "fontSize": "{textSizes.display.desktop.3xl}",
            "fontWeight": "{weights.bold}",
            "lineHeight": "124px",
        },
        "$type": "typography",
        "$extensions": {"source": "declared --textSizes-display-desktop-3xl 130px / --lineHeights-display-desktop-3xl 124px / --weights-bold, Klarna Title"},
    },
    "display-xl": {
        "$value": {
            "fontFamily": "{fonts.font.brand.title}",
            "fontSize": "{textSizes.display.desktop.xl}",
            "fontWeight": "{weights.bold}",
            "lineHeight": "80px",
        },
        "$type": "typography",
        "$extensions": {"source": "declared --textSizes-display-desktop-xl 84px; line height is the measured home h1 (84px/700 Klarna Title), not the fluid display-xl calc"},
    },
    "body": {
        "$value": {
            "fontFamily": "{fonts.font.brand.text}",
            "fontSize": "16px",
            "fontWeight": "{weights.normal}",
            "lineHeight": "24px",
        },
        "$type": "typography",
        "$extensions": {"source": "Klarna Text at 16/400; 24px leading is --lineHeights-body-desktop-m with a 16px root"},
    },
}

if (RAW / "motion.json").exists():
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core["motion"], _motion_extra = motion.build(json.loads((RAW / "motion.json").read_text()))
    if _motion_extra:  # what DTCG cannot carry is kept, as the kit does
        core["$extensions"] = {"notTokenised": _motion_extra}

# Component tokens from measurements, when present.
comp_path = RAW / "component-tokens.json"
if comp_path.exists():
    spec = json.loads(comp_path.read_text())
    light["component"] = spec.get("light", {})


def count(d):
    if isinstance(d, dict) and "$value" in d:
        return 1
    if isinstance(d, dict):
        return sum(count(v) for v in d.values())
    return 0


tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The painted marketing theme: white page, ink #0B051D, pink brand #FFA8CD, Klarna Title and Klarna Text.",
        },
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "Declared on .klarna-ui-DEFAULT-dark. The public marketing pages captured here paint light. Dark values are from the stylesheet, not a live dark capture of klarna.com/us/.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print({k: count(tokens[k]) for k in ("core", "light", "dark")})
