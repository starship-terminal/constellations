#!/usr/bin/env python3
"""Build tokens.json from Programa's public CSS and measured components.

Sources, read from https://programa.design/ on 2026-11-21, signed out, 1440x900:
  raw/css-vars.json              declared custom properties from the live stylesheets
  raw/components-computed.json   computed styles of public controls

The site paints one light theme. Semantic colours live under `light`. There is
no dark set. Every token carries $extensions.source. Unread values stay out.

Deterministic: same inputs, same bytes. Edit the raw files, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())
DECL = {k: v["value"] for k, v in V["declared"].items()}

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem|em)")


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8 and h[6:] == "00":
            return "rgba(0, 0, 0, 0)" if h[:6] == "000000" else "#%s" % h[:6]
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a == 0:
                return "rgba(%d, %d, %d, 0)" % (r, g, b)
            if a == 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def color(name, source):
    raw = DECL[name]
    if raw.startswith("var("):
        inner = raw[4:].split(",")[0].rstrip(")").strip()
        return {
            "$type": "color",
            "$value": "{" + path_for(inner) + "}",
            "$extensions": {"source": source + "; alias of " + inner},
        }
    return {
        "$type": "color",
        "$value": norm_color(raw),
        "$extensions": {"source": source},
    }


def dim(name, source):
    raw = DECL[name].strip()
    if not DIM.fullmatch(raw):
        raise ValueError(f"{name}: not a dimension: {raw!r}")
    return {"$type": "dimension", "$value": raw, "$extensions": {"source": source}}


def measured_color(comp, state, prop):
    return {
        "$type": "color",
        "$value": norm_color(COMP["components"][comp]["states"][state][prop]),
        "$extensions": {"source": f"Measured computed {prop} on {comp} {state}, programa.design, 1440x900, 2026-11-21"},
    }


def measured_dim(comp, state, prop):
    val = COMP["components"][comp]["states"][state][prop]
    if not DIM.fullmatch(str(val).strip()):
        raise ValueError(f"{comp}.{prop}: {val!r}")
    return {
        "$type": "dimension",
        "$value": val,
        "$extensions": {"source": f"Measured computed {prop} on {comp} {state}, programa.design, 1440x900, 2026-11-21"},
    }


PATHS = {}


def path_for(css_name):
    return PATHS[css_name]


def put(tree, css_name, token_path, token):
    PATHS[css_name] = token_path
    node = tree
    parts = token_path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = token


core = {}
# colour ramps from --color-*
for css_name, leaf in [
    ("--color-neutral-0", "color.neutral.0"),
    ("--color-neutral-50", "color.neutral.50"),
    ("--color-neutral-100", "color.neutral.100"),
    ("--color-neutral-200", "color.neutral.200"),
    ("--color-neutral-300", "color.neutral.300"),
    ("--color-neutral-400", "color.neutral.400"),
    ("--color-neutral-600", "color.neutral.600"),
    ("--color-neutral-700", "color.neutral.700"),
    ("--color-neutral-800", "color.neutral.800"),
    ("--color-yellow-light", "color.yellow.light"),
    ("--color-yellow-hover", "color.yellow.hover"),
    ("--color-green-pale", "color.green.pale"),
    ("--color-green-light", "color.green.light"),
    ("--color-green-dark", "color.green.dark"),
    ("--color-green-ultra-dark", "color.green.ultraDark"),
    ("--color-blue-pale", "color.blue.pale"),
    ("--color-blue-light", "color.blue.light"),
    ("--color-blue-dark", "color.blue.dark"),
    ("--color-blue-ultra-dark", "color.blue.ultraDark"),
    ("--color-purple-pale", "color.purple.pale"),
    ("--color-purple-light", "color.purple.light"),
    ("--color-purple-dark", "color.purple.dark"),
    ("--color-purple-ultra-dark", "color.purple.ultraDark"),
    ("--color-red-pale", "color.red.pale"),
    ("--color-red-light", "color.red.light"),
    ("--color-red-dark", "color.red.dark"),
    ("--color-red-ultra-dark", "color.red.ultraDark"),
    ("--color-orange-pale", "color.orange.pale"),
    ("--color-orange-light", "color.orange.light"),
    ("--color-orange-dark", "color.orange.dark"),
    ("--color-black", "color.black"),
    ("--color-white", "color.white"),
]:
    put(core, css_name, leaf, color(css_name, f"Measured declared {css_name} in programa.design stylesheets, 2026-11-21"))

for css_name, leaf in [
    ("--spacing-spacing-4", "spacing.4"),
    ("--spacing-spacing-8", "spacing.8"),
    ("--spacing-spacing-12", "spacing.12"),
    ("--spacing-spacing-16", "spacing.16"),
    ("--spacing-spacing-24", "spacing.24"),
    ("--spacing-spacing-32", "spacing.32"),
    ("--spacing-spacing-40", "spacing.40"),
    ("--spacing-spacing-60", "spacing.60"),
    ("--spacing-spacing-68", "spacing.68"),
    ("--spacing-spacing-80", "spacing.80"),
    ("--spacing-header-height", "spacing.header"),
    ("--spacing-container-padding", "spacing.container"),
    ("--spacing-container-padding-md", "spacing.containerMd"),
]:
    put(core, css_name, leaf, dim(css_name, f"Measured declared {css_name} in programa.design stylesheets, 2026-11-21"))

for css_name, leaf in [
    ("--radius-2", "radius.2"),
    ("--radius-12", "radius.12"),
]:
    put(core, css_name, leaf, dim(css_name, f"Measured declared {css_name} in programa.design stylesheets, 2026-11-21"))

# 6px radius is measured on buttons, not declared as --radius-*
core.setdefault("radius", {})["control"] = measured_dim("button-dark", "default", "borderRadius")

for css_name, leaf in [
    ("--text-font-size-xxxxl", "fontSize.xxxxl"),
    ("--text-font-size-xxxl", "fontSize.xxxl"),
    ("--text-font-size-xxl", "fontSize.xxl"),
    ("--text-font-size-xl", "fontSize.xl"),
    ("--text-font-size-l", "fontSize.l"),
    ("--text-font-size-s", "fontSize.s"),
    ("--text-font-size-xs", "fontSize.xs"),
    ("--text-font-size-xxs", "fontSize.xxs"),
]:
    put(core, css_name, leaf, dim(css_name, f"Measured declared {css_name} in programa.design stylesheets, 2026-11-21"))

for css_name, leaf in [
    ("--leading-font-line-height-xxxxl", "lineHeight.xxxxl"),
    ("--leading-font-line-height-xxxl", "lineHeight.xxxl"),
    ("--leading-font-line-height-xxl", "lineHeight.xxl"),
    ("--leading-font-line-height-xl", "lineHeight.xl"),
    ("--leading-font-line-height-l", "lineHeight.l"),
    ("--leading-font-line-height-m", "lineHeight.m"),
    ("--leading-font-line-height-s", "lineHeight.s"),
    ("--leading-font-line-height-xs-s", "lineHeight.xsS"),
    ("--leading-font-line-height-xs", "lineHeight.xs"),
    ("--leading-font-line-height-xxs", "lineHeight.xxs"),
]:
    put(core, css_name, leaf, dim(css_name, f"Measured declared {css_name} in programa.design stylesheets, 2026-11-21"))

for css_name, leaf in [
    ("--max-width-container-sm", "content.sm"),
    ("--max-width-container-md", "content.md"),
    ("--max-width-container-lg", "content.lg"),
    ("--max-width-container-xl", "content.xl"),
    ("--max-width-container-2xl", "content.2xl"),
    ("--max-width-container-3xl", "content.3xl"),
]:
    put(core, css_name, leaf, dim(css_name, f"Measured declared {css_name} in programa.design stylesheets, 2026-11-21"))

core["fontFamily"] = {
    "display": {
        "$type": "fontFamily",
        "$value": "Rhymes Display, system-ui, sans-serif",
        "$extensions": {"source": "Measured computed fontFamily on h1, programa.design home, 2026-11-21. Declared --font-rhymes-display"},
    },
    "sans": {
        "$type": "fontFamily",
        "$value": "Inter, Inter Fallback, system-ui, sans-serif",
        "$extensions": {"source": "Measured computed fontFamily on Start free, programa.design home, 2026-11-21"},
    },
    "text": {
        "$type": "fontFamily",
        "$value": "Rhymes Text, system-ui, sans-serif",
        "$extensions": {"source": "Measured declared --font-rhymes-text. Face not used on the measured controls"},
    },
    "mono": {
        "$type": "fontFamily",
        "$value": "Roboto Mono, ui-monospace, SFMono-Regular, Menlo, monospace",
        "$extensions": {"source": "Measured declared --font-roboto-mono. Not observed on the captured controls"},
    },
}
core["fontWeight"] = {
    "display": {"$type": "number", "$value": 300, "$extensions": {"source": "Measured declared --font-weight-weight-300 and computed fontWeight on h1"}},
    "regular": {"$type": "number", "$value": 400, "$extensions": {"source": "Measured declared --font-weight-weight-400"}},
    "medium": {"$type": "number", "$value": 500, "$extensions": {"source": "Measured declared --font-weight-weight-500 and computed fontWeight on Start free"}},
}
core["motion"] = {
    "duration": {
        "$type": "duration",
        "$value": "150ms",
        "$extensions": {"source": "Derived from declared --default-transition-duration .15s"},
    },
    "ease": {
        "$type": "cubicBezier",
        "$value": [0.4, 0, 0.2, 1],
        "$extensions": {"source": "Measured declared --default-transition-timing-function"},
    },
}
core["typography"] = {
    "display": {
        "$type": "typography",
        "$value": {
            "fontFamily": "{fontFamily.display}",
            "fontSize": "{fontSize.xxxxl}",
            "fontWeight": "{fontWeight.display}",
            "lineHeight": "{lineHeight.xxxl}",
        },
        "$extensions": {"source": "Measured h1 Freedom, by design: Rhymes Display 80px/64px weight 300. Scale names from --text-font-size-xxxxl and --leading-font-line-height-xxxl"},
    },
    "body": {
        "$type": "typography",
        "$value": {
            "fontFamily": "{fontFamily.sans}",
            "fontSize": "{fontSize.s}",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "{lineHeight.s}",
        },
        "$extensions": {"source": "Measured body controls at 16px Inter. Scale name --text-font-size-s"},
    },
    "label": {
        "$type": "typography",
        "$value": {
            "fontFamily": "{fontFamily.sans}",
            "fontSize": "{fontSize.xs}",
            "fontWeight": "{fontWeight.medium}",
            "lineHeight": "{lineHeight.xs}",
        },
        "$extensions": {"source": "Measured Start free and nav links: Inter 14px/20px"},
    },
    "caption": {
        "$type": "typography",
        "$value": {
            "fontFamily": "{fontFamily.sans}",
            "fontSize": "{fontSize.xxs}",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "16px",
        },
        "$extensions": {"source": "Measured footer Privacy Policy link: Inter 12px/16px. 16px line height is the computed value, not a named leading token"},
    },
}

light = {
    "page": color("--color-backgrounds-base", "Measured declared --color-backgrounds-base"),
    "surface": color("--color-neutral-50", "Measured declared --color-neutral-50. Editorial and changelog pages paint this"),
    "raised": color("--color-neutral-100", "Measured declared --color-neutral-100. Quiet button hover paints this"),
    "text": color("--color-foregrounds-base", "Measured declared --color-foregrounds-base"),
    "muted": color("--color-foregrounds-muted", "Measured declared --color-foregrounds-muted"),
    "link": color("--color-neutral-400", "Measured computed color on footer Privacy Policy link matches --color-neutral-400"),
    "border": color("--color-borders-base", "Measured declared --color-borders-base"),
    "accent": color("--color-yellow-light", "Measured declared --color-yellow-light. Also --bs-primary"),
    "accentHover": color("--color-yellow-hover", "Measured declared --color-yellow-hover"),
    "focus": {
        "$type": "color",
        "$value": "#005fcc",
        "$extensions": {"source": "Not captured as a designed ring. Chromium default outline when keyboard focus lands. Recorded only so the gap is explicit"},
    },
    "success": {"$type": "color", "$value": "{color.green.dark}", "$extensions": {"source": "Measured declared --color-green-dark. Used by the New badge text"}},
    "danger": color("--bs-danger", "Measured declared --bs-danger #ff427b. Bootstrap override, not a --color-* ramp"),
    "warning": color("--bs-warning", "Measured declared --bs-warning. Bootstrap default, not seen as a designed status chip on the captured pages"),
    "info": color("--bs-info", "Measured declared --bs-info. Bootstrap default, not seen as a designed status chip on the captured pages"),
    "component": {
        "buttonPrimary": {
            "background": measured_color("button-primary", "default", "backgroundColor"),
            "text": measured_color("button-primary", "default", "color"),
            "radius": measured_dim("button-primary", "default", "borderRadius"),
            "height": measured_dim("button-primary", "default", "height"),
            "fontSize": measured_dim("button-primary", "default", "fontSize"),
        },
        "buttonDark": {
            "background": measured_color("button-dark", "default", "backgroundColor"),
            "text": measured_color("button-dark", "default", "color"),
            "hover": measured_color("button-dark", "hover", "backgroundColor"),
            "radius": measured_dim("button-dark", "default", "borderRadius"),
            "height": measured_dim("button-dark", "default", "height"),
        },
        "buttonSecondary": {
            "background": measured_color("button-secondary", "default", "backgroundColor"),
            "text": measured_color("button-secondary", "default", "color"),
            "hover": measured_color("button-secondary", "hover", "backgroundColor"),
            "radius": measured_dim("button-secondary", "default", "borderRadius"),
            "height": measured_dim("button-secondary", "default", "height"),
        },
        "badge": {
            "background": measured_color("badge", "default", "backgroundColor"),
            "text": measured_color("badge", "default", "color"),
            "radius": measured_dim("badge", "default", "borderRadius"),
        },
    },
}

# fix alias paths that color() stored before PATHS was complete for aliases
# --color-backgrounds-base etc. were stored as aliases via path_for during light build,
# after core paths existed. Good.

doc = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "$themes": [
        {"name": "light", "group": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Dark theme: not present on the public site.",
            "Pressed colour of Start free: hover computed style did not change. CDP pressed was recorded in components-computed.json where the selector matched.",
            "Text field and email field computed boxes landed on the inner input (20px, transparent). The painted field chrome is Not captured as a separate token.",
            "Plan card selector matched the page, not a card. Plan card metrics are Not captured.",
            "Elevation scale: not declared. Button shadows are in the raw computed styles and not tokenised as a scale.",
            "Bootstrap --bs-* ramps are the framework defaults. Only --bs-primary, --bs-danger, --bs-warning and --bs-info are kept, because Programa overrides primary and danger.",
        ],
    },
}


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
            return
        if ty == "dimension" and not DIM.fullmatch(str(val)):
            raise SystemExit(f"{path}: bad dimension {val!r}")
        if ty == "color":
            norm_color(val)
        if "$extensions" not in node or "source" not in node["$extensions"]:
            raise SystemExit(f"{path}: missing source")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k if path else k)


walk(core)
walk(light, "light")
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "core groups", list(core), "light keys", list(light))
