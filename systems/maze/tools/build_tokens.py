#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

maze.co paints one light theme. Colours are declared as oklch() on :root and
converted here with the CSS Color 4 OKLab matrix. The hex is Derived from the
measured oklch. A value that was not read is not invented.

Deterministic: same inputs, byte-identical output. Edit the readings, never tokens.json.
"""
import json
import math
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
LIGHT = RAW["resolved"]["light"]


def oklch_to_srgb(L, C, H):
    h = math.radians(H)
    a = C * math.cos(h)
    b = C * math.sin(h)
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b_ = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s

    def lin(c):
        c = 0 if c < 0 else (1 if c > 1 else c)
        return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

    R, G, B = (round(lin(c) * 255) for c in (r, g, b_))
    return "#%02x%02x%02x" % (R, G, B)


def parse_oklch(value):
    m = re.fullmatch(r"oklch\(\s*([\d.]+)(%)?\s+([\d.]+)\s+([\d.]+)\s*\)", value.strip())
    if not m:
        return None
    L = float(m.group(1))
    if m.group(2) == "%":
        L /= 100
    return oklch_to_srgb(L, float(m.group(3)), float(m.group(4)))


def color(name):
    raw = LIGHT[name]["raw"]
    resolved = LIGHT[name]["value"]
    hexed = parse_oklch(resolved) or parse_oklch(raw)
    if not hexed:
        raise SystemExit(f"{name}: not an oklch colour ({resolved!r})")
    return {
        "$value": hexed,
        "$type": "color",
        "$extensions": {
            "source": f"Derived from css-var {name} = {raw} on :root, maze.co homepage 2026-11-21, converted OKLab to sRGB",
            "evidence": "Derived",
            "oklch": raw,
        },
    }


def dim(name, note=""):
    raw = LIGHT[name]["value"].strip()
    if raw.startswith("."):
        raw = "0" + raw
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", raw):
        raise SystemExit(f"{name}: not a dimension ({raw!r})")
    return {
        "$value": raw,
        "$type": "dimension",
        "$extensions": {"source": f"Measured css-var {name} on :root, maze.co homepage 2026-11-21" + ("; " + note if note else ""), "evidence": "Measured"},
    }


def number_token(name):
    raw = LIGHT[name]["value"].strip()
    if not re.fullmatch(r"\d+", raw):
        raise SystemExit(f"{name}: not an integer ({raw!r})")
    return {
        "$value": int(raw),
        "$type": "fontWeight",
        "$extensions": {"source": f"Measured css-var {name} on :root, maze.co homepage 2026-11-21", "evidence": "Measured"},
    }


def duration(name):
    raw = LIGHT[name]["value"].strip()
    m = re.fullmatch(r"([\d.]+)s", raw)
    if not m:
        raise SystemExit(f"{name}: not a duration ({raw!r})")
    ms = int(round(float(m.group(1)) * 1000))
    return {
        "$value": f"{ms}ms",
        "$type": "duration",
        "$extensions": {"source": f"Derived from css-var {name} = {raw} on :root, maze.co homepage 2026-11-21", "evidence": "Derived"},
    }


def bezier(name):
    raw = LIGHT[name]["value"].strip()
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", raw)
    if not m:
        raise SystemExit(f"{name}: not a cubic-bezier ({raw!r})")
    return {
        "$value": [float(x) for x in m.groups()],
        "$type": "cubicBezier",
        "$extensions": {"source": f"Measured css-var {name} on :root, maze.co homepage 2026-11-21", "evidence": "Measured"},
    }


def font_family():
    raw = LIGHT["--font-phonic"]["value"]
    return {
        "$value": "Phonic, sans-serif",
        "$type": "fontFamily",
        "$extensions": {"source": "Measured css-var --font-phonic on :root, maze.co homepage 2026-11-21; @font-face Phonic woff2 from /fonts/phonic/", "evidence": "Measured"},
    }


core = {
    "color": {
        "neutral": {step: color(f"--color-neutral-{step}") for step in ("000", "100", "200", "300", "400", "500", "600", "700", "900")},
        "blue": {step: color(f"--color-blue-{step}") for step in ("100", "200", "300", "400", "500", "600", "700")},
        "cyan": {step: color(f"--color-cyan-{step}") for step in ("100", "200", "300", "400", "500", "600", "700")},
        "lime": {step: color(f"--color-lime-{step}") for step in ("100", "200", "300", "400", "500", "600", "700")},
        "purple": {step: color(f"--color-purple-{step}") for step in ("100", "200", "300", "400", "500", "600", "700")},
        "red": {step: color(f"--color-red-{step}") for step in ("100", "200", "300", "400", "500", "600", "700")},
        "yellow": {step: color(f"--color-yellow-{step}") for step in ("100", "200", "300", "400", "500", "600", "700")},
    },
    "font": {
        "family": {"display": font_family(), "ui": font_family()},
        "weight": {
            "light": number_token("--font-weight-light"),
            "normal": number_token("--font-weight-normal"),
            "medium": number_token("--font-weight-medium"),
            "semibold": number_token("--font-weight-semibold"),
        },
    },
    "radius": {
        "xs": dim("--radius-xs"),
        "sm": dim("--radius-sm"),
        "md": dim("--radius-md"),
        "lg": dim("--radius-lg"),
        "xl": dim("--radius-xl"),
        "2xl": dim("--radius-2xl"),
    },
    "spacing": {
        "1": dim("--spacing"),
        "nav-height": dim("--nav-height"),
    },
    "motion": {
        "duration": duration("--default-transition-duration"),
        "ease-out": bezier("--ease-out"),
        "ease-in-out": bezier("--ease-in-out"),
    },
    "layout": {
        "breakpoint-2xl": dim("--breakpoint-2xl"),
        "container-sm": dim("--container-sm"),
        "container-md": dim("--container-md"),
        "container-3xl": dim("--container-3xl"),
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "130px",
                "fontWeight": "{font.weight.light}",
                "lineHeight": "136.5px",
                "letterSpacing": "-11.7px",
            },
            "$extensions": {"source": "Measured computed style of homepage h1, maze.co, light, 1440, 2026-11-21", "evidence": "Measured"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "16px",
                "fontWeight": "{font.weight.normal}",
                "lineHeight": "24px",
            },
            "$extensions": {"source": "Measured computed style of body, maze.co homepage, light, 1440, 2026-11-21", "evidence": "Measured"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "14px",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": "24px",
            },
            "$extensions": {"source": "Measured computed style of header button, maze.co homepage, light, 1440, 2026-11-21", "evidence": "Measured"},
        },
    },
    "shadow": {
        "nav": {
            "$type": "shadow",
            "$value": [{"color": "rgba(0, 0, 0, 0.039)", "offsetX": "0px", "offsetY": "4px", "blur": "30px", "spread": "0px"}],
            "$extensions": {"source": "Derived from css-var --shadow-nav = 0px 4px 30px #0000000a on :root", "evidence": "Derived"},
        },
        "modal": {
            "$type": "shadow",
            "$value": [{"color": "rgba(0, 0, 0, 0.078)", "offsetX": "0px", "offsetY": "4px", "blur": "20px", "spread": "0px"}],
            "$extensions": {"source": "Derived from css-var --shadow-modal = 0 4px 20px #00000014 on :root", "evidence": "Derived"},
        },
    },
}

light = {
    "page": color("--color-neutral-000"),
    "surface": color("--color-neutral-100"),
    "text": color("--color-neutral-700"),
    "muted": color("--color-neutral-500"),
    "accent": color("--color-lime-400"),
    "accent-ink": color("--color-neutral-700"),
    "border": color("--color-neutral-300"),
    "success": color("--color-success"),
    "danger": color("--color-error"),
    "link": color("--link-color"),
    "heading": color("--heading-color"),
    "chip": color("--chips-background"),
    "on-accent": color("--chips-text"),
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme maze.co paints on the captured public pages. No dark class or data-theme switch was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# Refuse a colour token whose value is not hex.
for set_name, tree in (("core", core), ("light", light)):
    def walk(node, path=""):
        if isinstance(node, dict) and "$value" in node:
            if node["$type"] == "color" and not re.fullmatch(r"#[0-9a-f]{6}", node["$value"]):
                raise SystemExit(f"{path} colour {node['$value']!r}")
            if "source" not in node.get("$extensions", {}):
                raise SystemExit(f"{path} missing source")
        elif isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, f"{path}.{k}" if path else k)
    walk(tree)

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
