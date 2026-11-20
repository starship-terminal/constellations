#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

lovable.dev declares a named token layer (--bg-*, --fg-*, --border-*,
--shadow-*, --text-*-lmk, --radius-*-lmk, --font-*) and resolves it under
html.light and html.dark. Public marketing paints light. /enterprise-form
paints dark. Docs (docs.lovable.dev) is a separate host and is not in this
token file.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
V = json.loads((HERE / "raw" / "css-vars.json").read_text())
LIGHT = V["resolved"]["light"]
DARK = V["resolved"]["dark"]

ROLES = [
    "page", "surface", "raised", "overlay", "scrim",
    "text", "textSecondary", "textDisabled", "textOnAccent", "link",
    "border", "borderStrong", "focus",
    "accent", "accentHoverGlow", "accentPressedGlow",
    "success", "warning", "danger", "info",
]

# role -> css variable. Same names in both themes; values differ.
ROLE_VARS = {
    "page": "--bg-base",
    "surface": "--bg-secondary",
    "raised": "--bg-primary",
    "overlay": "--bg-translucent",
    "scrim": "--bg-scrim",
    "text": "--fg-primary",
    "textSecondary": "--fg-secondary",
    "textDisabled": "--fg-quaternary",
    "textOnAccent": "--fg-inverse",
    "link": "--fg-accent",
    "border": "--border-base",
    "borderStrong": "--border-primary",
    "focus": "--border-focus",
    "accent": "--bg-accent",
    "accentHoverGlow": "--glow-accent-hover",
    "accentPressedGlow": "--glow-accent-pressed",
    "success": "--bg-positive",
    "warning": "--bg-attention",
    "danger": "--bg-destructive",
    "info": "--bg-special",
}


def val(theme, name):
    box = (LIGHT if theme == "light" else DARK).get(name) or {}
    v = box.get("value", box.get("raw"))
    if v in (None, ""):
        raise KeyError(f"{theme} {name} was not resolved")
    return v


def color_token(theme, name):
    return {
        "$value": val(theme, name),
        "$type": "color",
        "$extensions": {"source": f"css-var {name} resolved on html.{theme}"},
    }


COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]


def rect(key):
    r = ((COMP.get(key) or {}).get("states", {}).get("default") or {}).get("rect")
    if not r:
        raise SystemExit(f"{key} default rect missing from raw/components-computed.json")
    return r


def dimension(v):
    """'-.03em' -> '-0.03em', 'normal' -> '0px'; anything else that is not one length fails."""
    v = v.strip()
    if v == "normal":
        return "0px"
    v = re.sub(r"^(-?)\.(\d)", r"\g<1>0.\2", v)
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em)", v):
        raise SystemExit(f"not a dimension: {v!r}")
    return v


def dim_token(name, source):
    v = val("light", name)
    if isinstance(v, (int, float)):
        v = f"{v:g}px"
    return {
        "$value": v,
        "$type": "dimension",
        "$extensions": {"source": source},
    }


# --glow-* are translucent tints Lovable paints over a fill on hover and press; the accent fill
# itself stays --bg-accent. No declared or measured accent hover fill exists, so the roles say glow.
GLOW = "A translucent tint painted over the accent fill on {}, not a fill: the fill stays `accent`."


def theme_set(theme):
    out = {}
    for role, name in ROLE_VARS.items():
        out[role] = color_token(theme, name)
    out["accentHoverGlow"]["$description"] = GLOW.format("hover")
    out["accentPressedGlow"]["$description"] = GLOW.format("press")
    # Extra paints the product names and the public surface uses.
    extras = {
        "inverse": "--bg-inverse",
        "accentForeground": "--fg-on-attention",
        "destructiveForeground": "--fg-destructive",
        "positive": "--bg-positive",
        "attention": "--bg-attention",
        "special": "--bg-special",
        "muted": "--bg-muted",
        "depth": "--bg-depth",
    }
    for role, name in extras.items():
        if name in (LIGHT if theme == "light" else DARK):
            out[role] = color_token(theme, name)
    return out


def core():
    c = {"color": {}, "fontFamily": {}, "fontWeight": {}, "typography": {}, "radius": {}, "space": {}, "elevation": {}, "duration": {}, "easing": {}, "layout": {}}
    # A short named palette, light values. These are brand constants the dark
    # theme does not invert (accent, destructive, positive, attention).
    palette = {
        "accent": "--bg-accent",
        "destructive": "--bg-destructive",
        "positive": "--bg-positive",
        "attention": "--bg-attention",
        "special": "--bg-special",
        "highlight": "--bg-highlight",
        "focus": "--border-focus",
        "marketingAccent": "--marketing-accent-primary",
    }
    for key, name in palette.items():
        c["color"][key] = color_token("light", name)
        c["color"][key]["$extensions"]["source"] += "; constant paint, same hex in the light capture"

    c["fontFamily"]["sans"] = {
        "$value": val("light", "--font-sans"),
        "$type": "fontFamily",
        "$extensions": {"source": "css-var --font-sans on html.light; @font-face Camera Plain Variable is in the bundle, files not committed"},
    }
    c["fontFamily"]["mono"] = {
        "$value": val("light", "--font-mono"),
        "$type": "fontFamily",
        "$extensions": {"source": "css-var --font-mono on html.light; Roboto Mono Variable @font-face, files not committed"},
    }
    c["fontFamily"]["serif"] = {
        "$value": val("light", "--font-serif"),
        "$type": "fontFamily",
        "$extensions": {"source": "css-var --font-serif on html.light; a system serif stack, not a webfont"},
    }
    for key, name in (
        ("normal", "--font-weight-normal"),
        ("medium", "--font-weight-medium"),
        ("semibold", "--font-weight-semibold"),
    ):
        c["fontWeight"][key] = {
            "$value": int(float(val("light", name))),
            "$type": "fontWeight",
            "$extensions": {"source": f"css-var {name} resolved to {val('light', name)}"},
        }

    type_roles = {
        "display": "--text-heading-lg-lmk",
        "heading": "--text-heading-md-lmk",
        "title": "--text-title-lmk",
        "label": "--text-label-lmk",
        "body": "--text-ui-lmk",
        "caption": "--text-ui-sm-lmk",
    }
    for role, name in type_roles.items():
        size = val("light", name)
        lh = val("light", name + "--line-height")
        ls = val("light", name + "--letter-spacing")
        fw = val("light", name + "--font-weight")
        c["typography"][role] = {
            "$value": {
                "fontFamily": "{fontFamily.sans}",
                "fontSize": size if isinstance(size, str) else f"{size:g}px",
                "fontWeight": int(float(fw)) if not isinstance(fw, int) else fw,
                "lineHeight": lh if isinstance(lh, (int, float)) else lh,
                "letterSpacing": dimension(ls) if isinstance(ls, str) else f"{ls:g}px",
            },
            "$type": "typography",
            "$extensions": {"source": f"css-var {name} and its --line-height/--letter-spacing/--font-weight companions"},
        }

    for key, name in (
        ("trigger", "--radius-trigger-lmk"),
        ("menu", "--radius-menu-lmk"),
        ("menuItem", "--radius-menu-item-lmk"),
        ("menuLink", "--radius-menu-link-lmk"),
        ("menuCard", "--radius-menu-card-lmk"),
        ("menuBlock", "--radius-menu-block-lmk"),
        ("focus", "--radius-focus-lmk"),
    ):
        c["radius"][key] = dim_token(name, f"css-var {name}")

    c["space"]["unit"] = {
        "$value": dimension(val("light", "--spacing")),
        "$type": "dimension",
        "$extensions": {"source": f"css-var --spacing ({LIGHT['--spacing'].get('raw')}), computed at the default root size"},
    }
    c["border"] = {
        "default": {
            "$value": val("light", "--border-default") if isinstance(val("light", "--border-default"), str) else f"{val('light', '--border-default'):g}px",
            "$type": "dimension",
            "$extensions": {"source": "css-var --border-default"},
        }
    }
    # One elevation sample. The full shadow strings are long computed values.
    shadow = val("light", "--shadow-surface-xxs")
    c["elevation"]["surfaceXxs"] = {
        "$value": shadow if isinstance(shadow, str) else str(shadow),
        "$type": "other",
        "$extensions": {"source": "css-var --shadow-surface-xxs computed box-shadow on html.light"},
    }
    dur = val("light", "--default-transition-duration")
    m = re.fullmatch(r"(\d*\.?\d+)(m?s)", dur)
    if not m:
        raise SystemExit(f"--default-transition-duration is not a time: {dur!r}")
    c["duration"]["default"] = {
        "$value": "%gms" % (float(m.group(1)) * (1 if m.group(2) == "ms" else 1000)),
        "$type": "duration",
        "$extensions": {"source": f"css-var --default-transition-duration is {dur}"},
    }
    ease = val("light", "--default-transition-timing-function")
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", ease)
    if not m:
        raise SystemExit(f"--default-transition-timing-function is not a cubic-bezier: {ease!r}")
    c["easing"]["default"] = {
        "$value": [float(x) if "." in x else int(x) for x in m.groups()],
        "$type": "cubicBezier",
        "$extensions": {"source": f"css-var --default-transition-timing-function {ease}"},
    }
    header, m_header = rect("header"), rect("m-header")
    c["layout"]["desktop"] = {
        "$value": f"{header['w']:g}px",
        "$type": "dimension",
        "$extensions": {"source": "measured width of the header on https://lovable.dev/, the desktop viewport (raw/components-computed.json header)"},
    }
    c["layout"]["phone"] = {
        "$value": f"{m_header['w']:g}px",
        "$type": "dimension",
        "$extensions": {"source": "measured width of the phone header, the phone viewport (raw/components-computed.json m-header)"},
    }
    c["layout"]["header"] = {
        "$value": f"{header['h']:g}px",
        "$type": "dimension",
        "$extensions": {"source": "measured header height on https://lovable.dev/ at 1440 (raw/components-computed.json header)"},
    }
    return c


def check_color(v):
    if isinstance(v, str) and (v.startswith("#") or v.startswith("rgb") or v.startswith("okl")):
        return
    raise ValueError(f"not a colour: {v!r}")


tokens = {
    "core": core(),
    "light": theme_set("light"),
    "dark": theme_set("dark"),
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Painted on the public marketing routes (html.light)."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Declared as html.dark and painted on /enterprise-form. Marketing routes stay light."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

for theme in ("light", "dark"):
    for role, leaf in tokens[theme].items():
        check_color(leaf["$value"])

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote tokens", {k: len(v) if isinstance(v, dict) else 0 for k, v in tokens.items()})
