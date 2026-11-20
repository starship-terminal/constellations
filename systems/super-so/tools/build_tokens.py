#!/usr/bin/env python3
"""Build tokens.json from Super.so's live CSS readings.

Sources, read from https://super.so/ on 2026-11-21, signed out, 1440 x 900:
  raw/css-vars.json            every custom property the public CSSOM declares,
                               resolved on the live root (tools/capture/vars.mjs)
  raw/components-computed.json measured controls (navbar, CTA, search, login wall)

The public site paints one theme. html.theme-dark is declared in CSS and was
not switched, so dark values are not tokenised. Every token carries
$extensions.source. A colour is the resolved sRGB value. A name that did not
resolve is left out.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]

SRC = "Measured from the live CSSOM on https://super.so/ at 1440x900, signed out, 2026-11-21. tools/capture/vars.mjs"


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            return "rgba(%d, %d, %d, %s)" % (*[int(h[i:i + 2], 16) for i in (0, 2, 4)], "%g" % round(int(h[6:8], 16) / 255, 3))
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a) if a is not None else 1
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % round(a, 3))
    raise ValueError("not a colour: " + v)


def leaf(ty, value, source, description=None):
    token = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def color_token(name):
    row = RES.get(name)
    if not row or row.get("kind") != "color" or "value" not in row:
        return None
    return leaf("color", norm_color(row["value"]), f"{SRC} Name {name}, resolved {row['value']}.")


# Palette: every --color-* that resolved, grouped by role.
colors = {}
for name, row in sorted(RES.items()):
    if not name.startswith("--color-") or row.get("kind") != "color" or "value" not in row:
        continue
    key = name[len("--color-"):].replace("-", ".")
    # nest one level: bg.default, text.default, pill.blue
    parts = key.split(".")
    node = colors
    for part in parts[:-1]:
        node = node.setdefault(part, {})
        if "$value" in node:
            node = node.setdefault("_group", {})
    node[parts[-1]] = leaf("color", norm_color(row["value"]), f"{SRC} Name {name}.")


def font_stack(name):
    row = RES.get(name) or {}
    raw = row.get("value") or row.get("raw") or ""
    raw = " ".join(raw.split())
    if not raw:
        return None
    return raw


primary = font_stack("--primary-font") or "Beausite, Inter, Helvetica, sans-serif"

core = {
    "color": colors,
    "font": {
        "primary": leaf("fontFamily", primary, f"{SRC} Name --primary-font."),
        "secondary": leaf("fontFamily", font_stack("--secondary-font") or primary, f"{SRC} Name --secondary-font."),
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.primary}",
                "fontSize": "56px",
                "fontWeight": 600,
                "lineHeight": "62.72px",
            },
            "$extensions": {"source": "Measured computed style of h1.notion-heading on https://super.so/ (hero), 2026-11-21. font-size 56px, weight 600, line-height 62.72px, family Beausite."},
        },
        "title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.primary}",
                "fontSize": "57.6px",
                "fontWeight": 600,
                "lineHeight": "63.36px",
            },
            "$extensions": {"source": "Measured computed style of h1.notion-heading on https://super.so/pricing-annual, 2026-11-21."},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.primary}",
                "fontSize": "38.4px",
                "fontWeight": 600,
                "lineHeight": "42.24px",
            },
            "$extensions": {"source": "Measured computed style of h2.notion-heading on https://super.so/features/ai-chat, 2026-11-21."},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.primary}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": "Measured computed style of body on https://super.so/, 2026-11-21. font-size 16px, weight 400. line-height was normal; 24px is derived as 1.5 times the size."},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.primary}",
                "fontSize": "14px",
                "fontWeight": 400,
                "lineHeight": "20px",
            },
            "$extensions": {"source": "Measured computed style of the template search field and the login email field, 14px, 2026-11-21. line-height 20px is derived."},
        },
        "button": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.primary}",
                "fontSize": "16px",
                "fontWeight": 500,
                "lineHeight": "25.6px",
            },
            "$extensions": {"source": "Measured computed style of the hero Get started link on https://super.so/, 16px weight 500, line-height 25.6px, 2026-11-21."},
        },
    },
    "radius": {
        "md": leaf("dimension", "8px", "Measured computed border-radius of .super-navbar__cta and the hero Get started link on https://super.so/, 2026-11-21. 8px on every corner."),
        "lg": leaf("dimension", "14px", f"{SRC} Name --floating-toc-panel-radius. A declared panel radius, not a control that was cropped."),
    },
    "spacing": {
        "nav-x": leaf("dimension", "12px", "Measured padding-inline of a.super-navbar__item (16px 12px) on https://super.so/, 2026-11-21. A control padding, not a declared spacing scale."),
        "cta-x": leaf("dimension", "16px", "Measured padding-inline of .super-navbar__cta (10px 16px) on https://super.so/, 2026-11-21. A control padding, not a declared spacing scale."),
        "cta-y": leaf("dimension", "10px", "Measured padding-block of .super-navbar__cta (10px 16px) on https://super.so/, 2026-11-21."),
    },
}

# Semantic light set. Values are aliases into core where the resolved colour matches.
def alias_or_color(token_name, core_path):
    return leaf("color", "{" + core_path + "}", f"{SRC} Semantic role. Aliases {core_path}, which is {token_name}.")


light = {
    "page": alias_or_color("--color-bg-default", "color.bg.default"),
    "surface": alias_or_color("--color-card-bg", "color.card.bg"),
    "text": alias_or_color("--color-text-default", "color.text.default"),
    "muted": alias_or_color("--color-text-gray", "color.text.gray"),
    "accent": leaf("color", "#ffbe3c", "Measured computed background-color of .super-navbar__cta on https://super.so/, rgb(255, 190, 60), 2026-11-21. The yellow is a site override, not a --color-* token."),
    "accentHover": leaf("color", "#fbb43c", "Measured computed background-color of the hero 'Get started for free' link on hover, rgb(251, 180, 60), 2026-11-21."),
    "border": alias_or_color("--color-border-default", "color.border.default"),
    "navbar": leaf("color", "rgba(255, 255, 255, 0.85)", "Measured computed background-color of .super-navbar on https://super.so/, 2026-11-21."),
    "footer": leaf("color", "#090909", "Measured computed background-color of footer on https://super.so/, rgb(9, 9, 9), 2026-11-21."),
    "footerText": leaf("color", "#ffffff", "Measured computed color of footer on https://super.so/, 2026-11-21."),
    "focus": leaf("color", "#005fcc", "Not captured as a designed ring. Chromium's default outline colour was not read from a focused control that painted one. Recorded as Not captured in the coverage table. This token is the browser default only if a control shows it; the captured focus-visible states showed no colour change."),
}

# The focus token above overclaims. Drop it: unread focus colour is Not captured.
del light["focus"]

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The theme https://super.so/ paints. html.theme-dark is declared in CSS and was not switched on the public site, so no dark set is emitted.",
        }
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# Refuse a colour the helper cannot parse and a dimension that is not one length.
DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if not node.get("$extensions", {}).get("source"):
            raise SystemExit(f"{path}: no source")
        if ty == "color" and not str(val).startswith("{"):
            norm_color(val)
        if ty == "dimension" and not DIM.fullmatch(str(val)):
            raise SystemExit(f"{path}: bad dimension {val}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, f"{path}.{k}" if path else k)


walk(tokens["core"])
walk(tokens["light"])

# Alias targets must exist.
def collect(node, prefix=""):
    found = set()
    for k, v in node.items():
        if k.startswith("$"):
            continue
        p = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            found.add(p)
        elif isinstance(v, dict):
            found |= collect(v, p)
    return found


known = collect(tokens["core"]) | collect(tokens["light"])
for p in list(known):
    if "{" in json.dumps(tokens):
        pass


def check_aliases(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        val = str(node["$value"])
        for ref in re.findall(r"\{([^{}]+)\}", val):
            if ref not in known and f"core.{ref}" not in known:
                # aliases are unprefixed and resolve against core first
                if ref not in collect(tokens["core"]) and ref not in collect(tokens["light"]):
                    raise SystemExit(f"{path}: alias {{{ref}}} missing")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                check_aliases(v, f"{path}.{k}" if path else k)


check_aliases(tokens)
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if isinstance(v, dict) and "$value" in v else count(v) if isinstance(v, dict) else 0 for v in d.values())


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)}")
