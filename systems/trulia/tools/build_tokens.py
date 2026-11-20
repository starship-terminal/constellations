#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Trulia declares its palette and scales once, on :where(:root, :host). There is
no dark theme block. Semantic colour names are var() aliases of the ramps.
Every token's $extensions.source names the custom property and that selector.
Unread values stay out. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
STATES = json.loads((HERE / "raw" / "component-states.json").read_text())

ROOT = ":where(:root, :host)"
DECL = {}
for d in RAW["decls"]:
    if d.get("selector") == ROOT and d.get("value"):
        DECL[d["name"]] = d["value"].strip()


def rgb_to_hex(value):
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", value)
    if not m:
        return None
    return "#{:02x}{:02x}{:02x}".format(*map(int, m.groups()))


def token(value, type_, source, **ext):
    node = {"$value": value, "$type": type_, "$extensions": {"source": source}}
    node["$extensions"].update(ext)
    return node


def color_token(name):
    raw = DECL[name]
    hexed = rgb_to_hex(raw)
    if hexed is None and (raw.startswith("var(") or raw == "transparent"):
        return None
    if hexed is None:
        raise SystemExit(f"cannot read colour {name}={raw}")
    return token(hexed, "color", f"Measured CSS custom property {name} on {ROOT} ({raw})")


CORE_COLOR = {}
for name, raw in DECL.items():
    if not name.startswith("--colors-"):
        continue
    if raw.startswith("var("):
        continue
    key = name.removeprefix("--colors-").replace("-", ".")
    # nest one level: tarzana.500, grey.50, white
    parts = key.split(".")
    node = color_token(name)
    cursor = CORE_COLOR
    for part in parts[:-1]:
        cursor = cursor.setdefault(part, {})
    cursor[parts[-1]] = node

# semantic aliases in light
SEM = {}
ALIAS = {
    "page": ("--colors-white", "color.white"),
    "surface": ("--colors-grey-50", "color.grey.50"),
    "text": ("--colors-grey-900", "color.grey.900"),
    "muted": ("--colors-grey-600", "color.grey.600"),
    "accent": ("--colors-tarzana-700", "color.tarzana.700"),
    "accent-bright": ("--colors-tarzana-500", "color.tarzana.500"),
    "border": ("--colors-grey-400", "color.grey.400"),
    "on-accent": ("--colors-white", "color.white"),
    "link": ("--colors-tarzana-700", "color.tarzana.700"),
    "secondary": ("--colors-belmont-500", "color.belmont.500"),
    "tertiary": ("--colors-oakmore-500-a-a", "color.oakmore.500-a-a"),
    "success": ("--colors-okay", "color.okay"),
    "warning": ("--colors-gold", "color.gold"),
    "danger": ("--colors-oakmore-500-a-a", "color.oakmore.500-a-a"),
}
for key, (prop, alias) in ALIAS.items():
    raw = DECL[prop]
    hexed = rgb_to_hex(raw) or rgb_to_hex(DECL.get(prop, ""))
    # follow one var()
    if raw.startswith("var("):
        inner = raw[4:-1].strip()
        hexed = rgb_to_hex(DECL[inner])
        source = f"Measured CSS custom property {prop} on {ROOT}, alias of {inner} ({DECL[inner]})"
    else:
        source = f"Measured CSS custom property {prop} on {ROOT} ({raw})"
    SEM[key] = token("{" + alias + "}", "color", source)

# accent states from live controls, not from a declared hover token
login_hover = STATES["login-button-hover"]
search_hover = STATES["search-submit-hover"]
SEM["accent-hover"] = token(
    rgb_to_hex(login_hover["backgroundColor"]),
    "color",
    "Measured computed backgroundColor on [data-testid=navbar-login-button] hover, homepage 1440, 2026-11-21",
)
SEM["search-submit"] = token(
    rgb_to_hex(STATES["search-submit-default"]["backgroundColor"]),
    "color",
    "Measured computed backgroundColor on [aria-label=submit search], homepage 1440",
)
SEM["search-submit-hover"] = token(
    rgb_to_hex(search_hover["backgroundColor"]),
    "color",
    "Measured computed backgroundColor on [aria-label=submit search] hover, homepage 1440",
)
SEM["scrim"] = token(
    "#0000004d",
    "color",
    "Not captured as a token. Login dialog overlay class paints rgba(0,0,0,0.3); hex is Derived from that class string in the dialog HTML, not sampled from a pixel",
)

SPACE = {}
for name, raw in DECL.items():
    if name.startswith("--spacing-") and raw.endswith("px"):
        key = name.removeprefix("--spacing-")
        SPACE[key] = token(raw, "dimension", f"Measured CSS custom property {name} on {ROOT}")

RADIUS = {}
for name, raw in DECL.items():
    if name.startswith("--radii-") and raw.endswith("px"):
        RADIUS[name.removeprefix("--radii-")] = token(raw, "dimension", f"Measured CSS custom property {name} on {ROOT}")

TYPE_SIZES = {}
for name, raw in DECL.items():
    if name.startswith("--font-sizes-") and name != "--font-sizes-0" and raw.endswith("px"):
        TYPE_SIZES[name.removeprefix("--font-sizes-")] = token(raw, "dimension", f"Measured CSS custom property {name} on {ROOT}")

LINE = {}
for name, raw in DECL.items():
    if name.startswith("--line-heights-") and name != "--line-heights-0":
        LINE[name.removeprefix("--line-heights-")] = token(raw, "number", f"Measured CSS custom property {name} on {ROOT}")

BREAKPOINTS = {}
for name, raw in DECL.items():
    if name.startswith("--breakpoints-") and raw.endswith("px"):
        BREAKPOINTS[name.removeprefix("--breakpoints-")] = token(raw, "dimension", f"Measured CSS custom property {name} on {ROOT}")

FOCUS = token(
    DECL["--focus-shadow"],
    "shadow",
    f"Measured CSS custom property --focus-shadow on {ROOT}",
)
ELEVATION = {
    "default": token(DECL["--shadows-default"], "shadow", f"Measured CSS custom property --shadows-default on {ROOT}"),
    "lead": token(DECL["--lead-shadow"], "shadow", f"Measured CSS custom property --lead-shadow on {ROOT}"),
}

FAMILY = token(
    "Figtree, \"Figtree Fallback\", Arial, sans-serif",
    "fontFamily",
    "Measured font-family on html (Figtree, \"Figtree Fallback\") plus the @font-face fallback local(\"Arial\")",
)

SIZING = {
    "header": token(DECL["--header-height"], "dimension", f"Measured CSS custom property --header-height on {ROOT}"),
    "filter-bar": token(DECL["--filter-bar-height"], "dimension", f"Measured CSS custom property --filter-bar-height on {ROOT}"),
    "banner": token(DECL["--banner-height"], "dimension", f"Measured CSS custom property --banner-height on {ROOT}"),
    "control": token("42px", "dimension", "Measured bounding box height of [data-testid=navbar-login-button], homepage 1440"),
    "search": token("60px", "dimension", "Measured bounding box height of #banner-search, homepage 1440"),
    "menu-drawer": token("320px", "dimension", "Measured bounding box width of [aria-label=Main Menu] dialog, homepage 1440"),
}

doc = {
    "core": {
        "color": CORE_COLOR,
        "space": SPACE,
        "radius": RADIUS,
        "fontSize": TYPE_SIZES,
        "lineHeight": LINE,
        "breakpoint": BREAKPOINTS,
        "fontFamily": {"sans": FAMILY},
        "elevation": ELEVATION,
        "focus": {"shadow": FOCUS},
        "sizing": SIZING,
    },
    "light": {
        "color": SEM,
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
}

# checks
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v, f"{path}.{k}" if path else k)

nodes = list(walk(doc))
missing = [p for p, n in nodes if not n.get("$extensions", {}).get("source")]
bad_dim = [p for p, n in nodes if n["$type"] == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(n["$value"]))]
if missing or bad_dim:
    raise SystemExit(f"token check failed missing={missing} bad_dim={bad_dim}")

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print(f"wrote {out} ({len(nodes)} tokens)")
