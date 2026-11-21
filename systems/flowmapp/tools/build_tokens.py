#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Read from https://www.flowmapp.com/ on 2026-11-21. The marketing site declares
two palettes on :root: the painted short names (--bg, --primary-blue, ...) and
a Webflow Apps slot set (--_apps---colors--* plus a -dark twin). The painted
public pages use the light slots. The -dark slots are declared but no captured
public page binds them, so the dark set is recorded as declared, not as a
live theme. Every token carries $extensions.source.

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RESOLVED = RAW["resolved"]
COMP = RAW["components"]
STATES = RAW["states"]["cta"]


def norm_color(v):
    v = str(v).strip().lower()
    named = {"black": "#000000", "white": "#ffffff"}
    if v in named:
        return named[v]
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a == 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def color(name, source):
    return {
        "$type": "color",
        "$value": norm_color(RESOLVED[name]),
        "$extensions": {"source": source},
    }


def dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value):
        raise ValueError("not a dimension: " + value)
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font_family(name, source):
    return {"$type": "fontFamily", "$value": RESOLVED[name], "$extensions": {"source": source}}


SRC = "measured css-var on :root, https://www.flowmapp.com/ 2026-11-21, raw/css-vars.json"

# Short palette names the painted marketing CSS uses.
SHORT = {
    "bg": "--bg",
    "black": "--black",
    "white": "--white",
    "dodger-blue": "--dodger-blue",
    "dodger-blue-20": "--dodger-blue-20",
    "primary-blue": "--primary-blue",
    "basic-blue": "--basic-blue",
    "service-grey": "--service-grey",
    "dark-grey": "--dark-grey",
    "light-steel-blue": "--light-steel-blue",
    "alice-blue": "--alice-blue",
    "gainsboro": "--gainsboro",
    "yellow-green": "--yellow-green",
    "pale-violet-red": "--pale-violet-red",
}

APPS_LIGHT = [
    "background", "foreground", "card", "card-foreground", "popover", "popover-foreground",
    "primary", "primary-foreground", "secondary", "secondary-foreground", "muted",
    "muted-foreground", "accent", "accent-foreground", "destructive", "border", "input", "ring",
]
APPS_DARK = [n + "-dark" for n in APPS_LIGHT]
CHARTS = ["chart-1", "chart-2", "chart-3", "chart-4", "chart-5"]
SIDEBAR = [
    "sidebar", "sidebar-foreground", "sidebar-primary", "sidebar-primary-foreground",
    "sidebar-accent", "sidebar-accent-foreground", "sidebar-border", "sidebar-ring",
]


def apps(names, prefix):
    out = {}
    for n in names:
        key = n.replace("-dark", "") if n.endswith("-dark") and n != "card-foreground-dark" else n
        # keep the css suffix in the token name so light and dark do not collide inside core
        token = n
        out[token] = color(prefix + n, "css-var %s%s; %s" % (prefix, n, SRC))
    return out


core = {
    "color": {k: color(v, "css-var %s; %s" % (v, SRC)) for k, v in SHORT.items()},
    "apps": {
        "color": apps(APPS_LIGHT + APPS_DARK, "--_apps---colors--"),
        "chart": {n: color("--_apps---charts--" + n, "css-var --_apps---charts--%s; %s" % (n, SRC)) for n in CHARTS + [c + "-dark" for c in CHARTS]},
        "sidebar": {n: color("--_apps---sidebar--" + n, "css-var --_apps---sidebar--%s; %s" % (n, SRC)) for n in SIDEBAR + [s + "-dark" for s in SIDEBAR]},
    },
    "font": {
        "heading": font_family("--_apps---typography--heading-font", "css-var --_apps---typography--heading-font; " + SRC),
        "body": font_family("--_apps---typography--body-font", "css-var --_apps---typography--body-font; " + SRC),
        "button": font_family("--_apps---typography--button-font", "css-var --_apps---typography--button-font; " + SRC),
    },
    "radius": {
        "apps": dim(RESOLVED["--_apps---sizes--radius"], "css-var --_apps---sizes--radius; " + SRC),
        "nav-link": dim(COMP["navLink"]["radius"], "measured a.nav__link border-radius, home 1440, raw/css-vars.json components"),
        "nav-button": dim(COMP["login"]["radius"], "measured a.nav__btn Log in border-radius, home 1440"),
        "hero-cta": dim("1600px", "measured a.btn and .btn__wrapper border-radius 1600px (pill), home 1440"),
    },
    "typography": {
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.body}",
                "fontSize": "14px",
                "fontWeight": 400,
                "lineHeight": "20px",
            },
            "$extensions": {"source": "measured body computed style, home 1440, raw/css-vars.json components.body"},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.body}",
                "fontSize": COMP["navLink"]["size"],
                "fontWeight": int(COMP["navLink"]["weight"]),
                "lineHeight": COMP["navLink"]["lh"],
            },
            "$extensions": {"source": "measured a.nav__link computed style, home 1440"},
        },
        "hero": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.heading}",
                "fontSize": COMP["hero"]["size"],
                "fontWeight": int(float(COMP["hero"]["weight"])),
                "lineHeight": COMP["hero"]["lh"],
            },
            "$extensions": {"source": "measured h1 computed style, home 1440"},
        },
    },
}

light = {
    "page": {"$type": "color", "$value": "{color.bg}", "$extensions": {"source": "alias of --bg, painted body background rgb(246, 248, 250)"}},
    "surface": {"$type": "color", "$value": "{apps.color.card}", "$extensions": {"source": "alias of --_apps---colors--card; nav chrome is white on the painted page"}},
    "text": {"$type": "color", "$value": "{apps.color.foreground}", "$extensions": {"source": "alias of --_apps---colors--foreground; body color black"}},
    "muted": {"$type": "color", "$value": "{color.service-grey}", "$extensions": {"source": "alias of --service-grey, the painted secondary grey"}},
    "accent": {"$type": "color", "$value": "{color.dodger-blue}", "$extensions": {"source": "alias of --dodger-blue. The painted hero fill is .btn__wrapper rgb(0, 128, 255). --primary-blue #0050ff is the apps primary slot and the pricing CTA family, recorded as color.primary-blue."}},
    "border": {"$type": "color", "$value": "{color.gainsboro}", "$extensions": {"source": "alias of --gainsboro; Log in button border is rgba(0,0,0,0.1), recorded on the component"}},
    "destructive": {"$type": "color", "$value": "{apps.color.destructive}", "$extensions": {"source": "alias of --_apps---colors--destructive; not seen as a painted control on the public home page"}},
    "focus": {"$type": "color", "$value": "{apps.color.ring}", "$extensions": {"source": "alias of --_apps---colors--ring. Keyboard focus on a.btn returned outline %s, so this is the declared slot, not a painted focus ring." % STATES["focus"].get("outline")}},
    "component": {
        "nav-height": dim("82.1px", "measured .nav.w-nav height, home 1440"),
        "login-height": dim("38.5px", "measured Log in a.nav__btn height, home 1440"),
        "cta-height": dim("38.5px", "measured Try for free a.nav__btn height, home 1440"),
        "nav-link-radius": {"$type": "dimension", "$value": "{radius.nav-link}", "$extensions": {"source": "alias"}},
        "button-radius": {"$type": "dimension", "$value": "{radius.nav-button}", "$extensions": {"source": "alias"}},
        "hero-cta-fill": {"$type": "color", "$value": "#0080ff", "$extensions": {"source": "measured .btn__wrapper background rgb(0, 128, 255), home 1440. The a.btn itself is rgba(0, 128, 255, 0.2). Matches --dodger-blue."}},
        "hero-cta-shadow": {"$type": "shadow", "$value": [{"color": "rgba(0, 128, 255, 0.34)", "offsetX": "0px", "offsetY": "8px", "blur": "10px", "spread": "0px"}], "$extensions": {"source": "measured .btn__wrapper box-shadow, home 1440"}},
    },
}

# Fix the sloppy nav height token to the measured string the builder accepts.
light["component"]["nav-height"] = dim("82.1px", "measured .nav.w-nav height, home 1440, raw/css-vars.json components.nav.rect.h")

dark = {
    "page": color("--_apps---colors--background-dark", "css-var --_apps---colors--background-dark declared on :root; no captured public page binds this dark slot. " + SRC),
    "surface": color("--_apps---colors--card-dark", "css-var --_apps---colors--card-dark declared, not painted on captured public pages. " + SRC),
    "text": color("--_apps---colors--foreground-dark", "css-var --_apps---colors--foreground-dark declared, not painted. " + SRC),
    "muted": color("--_apps---colors--muted-foreground-dark", "css-var --_apps---colors--muted-foreground-dark declared, not painted. " + SRC),
    "accent": color("--_apps---colors--primary-dark", "css-var --_apps---colors--primary-dark declared, not painted. " + SRC),
    "border": color("--_apps---colors--border-dark", "css-var --_apps---colors--border-dark declared, not painted. " + SRC),
}

tokens = {
    "$description": "FlowMapp public site tokens, read 2026-11-21 from https://www.flowmapp.com/. Light is the painted marketing theme. Dark slots are declared on :root and were not bound on any captured public page.",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark-declared", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# validate colours and dimensions
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{"):
            return
        if ty == "color":
            norm_color(val)
        if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
            raise SystemExit("bad dimension %s %r" % (path, val))
        if "$extensions" not in node or "source" not in node["$extensions"]:
            raise SystemExit("missing source " + path)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)

walk(tokens)
out = json.dumps(tokens, indent=2) + "\n"
(HERE / "tokens.json").write_text(out)
print("wrote tokens.json", len(out))
