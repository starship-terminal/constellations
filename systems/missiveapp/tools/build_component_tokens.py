#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

missiveapp.com is a Webflow marketing site. Its own token layer is declared
on :root (raw/css-vars.json, read by tools/capture/vars.mjs):

  --swatch--neutral-050..1000, --swatch--blue-*, --swatch--cumin-*,
  --swatch--green-*, --swatch--white, --swatch--black
                              the colour ramps
  --color--a..e, --color--bg-*, --color--brand*
                              semantic roles, each a var() of a swatch
  --spacing--1..28            a 4px-base spacing scale

There is no dark theme. The --k-* names belong to the Ketch consent banner
and are not product tokens. Measured component sizes come from
raw/components-computed.json when that file exists.

A leaf is {"var": "--name"} (resolved by build_tokens.py) or
{"value": ..., "source": "..."} for a measured or derived value.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
comp_path = RAW / "components-computed.json"
C = json.loads(comp_path.read_text())["components"] if comp_path.exists() else {}


def var(name, ty="color", **kw):
    return {"var": name, "type": ty, **kw}


def measured(key, state, prop, ty, fallback=None):
    st = (C.get(key) or {}).get("states", {}).get(state) or {}
    style = (st.get("style") or {})
    val = style.get(prop)
    if not val or val in ("none", "auto", "normal", "0px"):
        if fallback is None:
            return None
        return {"value": fallback, "type": ty, "source": f"Not captured on {key}.{state}; fallback recorded as a gap"}
    return {
        "value": val,
        "type": ty,
        "source": f"measured {key} {state} computed {prop} on {st.get('tag', 'element')} at 1440",
    }


SPEC = {
    "_about": (
        "Missive's public marketing token layer, read from :root on "
        "missiveapp.com. Swatches and semantic colours are declared CSS "
        "custom properties. There is no dark theme. Component sizes are "
        "computed styles where a capture measured them."
    ),
    "core": {"color": {"swatch": {}}, "spacing": {}, "font": {"family": {}}},
    "light": {},
    "component": {},
}

swatches = {
    "neutral": ["050", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950", "1000"],
    "blue": ["100", "600", "800"],
    "cumin": ["50", "200", "500", "600", "700"],
    "green": ["050", "100", "600"],
}
for hue, steps in swatches.items():
    SPEC["core"]["color"]["swatch"][hue] = {}
    for step in steps:
        name = f"--swatch--{hue}-{step}"
        if name in RL:
            SPEC["core"]["color"]["swatch"][hue][step] = var(name)
SPEC["core"]["color"]["swatch"]["white"] = var("--swatch--white")
SPEC["core"]["color"]["swatch"]["black"] = var("--swatch--black")

for step in ("1", "2", "3", "4", "6", "8", "12", "16", "20", "28"):
    SPEC["core"]["spacing"][step] = var(f"--spacing--{step}", "dimension")

SPEC["core"]["font"]["family"]["ui"] = {
    "value": "Inter, ui-sans-serif, system-ui, sans-serif",
    "type": "fontFamily",
    "source": "measured @font-face font-family Inter on missiveapp.com; the file is the site's webfont and is not committed",
}
SPEC["core"]["font"]["family"]["display"] = {
    "value": "\"Tiempos Headline\", Georgia, serif",
    "type": "fontFamily",
    "source": "measured @font-face font-family Tiempos Headline on missiveapp.com; the file is the site's webfont and is not committed",
}

# Semantic roles. Each --color--* resolves to a swatch. Aliased in the light set.
roles = {
    "page": "--color--bg-white",
    "surface": "--color--bg-neutral",
    "text": "--color--a",
    "muted": "--color--b",
    "border": "--color--d",
    "border-strong": "--color--c",
    "hairline": "--color--e",
    "accent": "--color--brand",
    "accent-hover": "--color--brand-dark",
    "accent-soft": "--color--brand-light",
    "on-accent": "--swatch--white",
}
SPEC["light"]["page"] = var("--color--bg-white")
SPEC["light"]["surface"] = var("--color--bg-neutral")
SPEC["light"]["text"] = var("--color--a")
SPEC["light"]["muted"] = var("--color--b")
SPEC["light"]["border"] = var("--color--d")
SPEC["light"]["accent"] = var("--color--brand")
SPEC["light"]["on-accent"] = var("--swatch--white")
SPEC["light"]["color"] = {k: var(v) for k, v in roles.items()}

# Status colours that exist as swatches, not as named status roles.
SPEC["light"]["status"] = {
    "success": var("--swatch--green-600"),
    "warning": var("--swatch--cumin-600"),
}
SPEC["light"]["status"]["success"]["description"] = "A green swatch. The site does not declare a success role."
SPEC["light"]["status"]["warning"]["description"] = "A cumin swatch. The site does not declare a warning role."

# Typography composites from the painted hero and body, when measured.
# Until measurements land, record the families only. Sizes stay Not captured
# in the coverage table rather than guessed.

comp = SPEC["component"]
for key, token, prop, ty, fallback in (
    ("nav-cta", "button.height", "height", "dimension", None),
    ("nav-link", "nav.link-height", "height", "dimension", None),
    ("hero-title", "type.hero-size", "fontSize", "dimension", None),
    ("docs-search", "field.height", "height", "dimension", None),
    ("header", "shell.header", "height", "dimension", None),
):
    leaf = measured(key, "default", prop, ty)
    if leaf:
        node = comp
        parts = token.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = leaf

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("wrote", RAW / "component-tokens.json")
