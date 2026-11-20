#!/usr/bin/env python3
"""Build tokens.json from Webflow's public CSS readings.

Sources, read from https://webflow.com/ on 2026-11-21:
  raw/css-vars.json          declared custom properties and font faces
  raw/computed-colors.json   the same names computed to sRGB on the live page,
                             once without and once with html.u-mode-dark

Every token carries $extensions.source. A clamp() size is Not captured as a
single dimension: the desktop end of the clamp is recorded as Derived and the
authored clamp is kept on the token. Deterministic.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COLORS = json.loads((RAW / "computed-colors.json").read_text())
LIGHT = VARS["resolved"]["light"]
DARK = VARS["resolved"]["dark"]


def rgb_to_hex(s):
    s = s.strip()
    if s in ("white", "#fff", "#ffffff"):
        return "#ffffff"
    if s in ("black",):
        return "#000000"
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", s)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6].lower()
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)", s)
    if m:
        r, g, b, a = m.groups()
        rgb = tuple(int(round(float(x))) for x in (r, g, b))
        if a is None or float(a) >= 0.999:
            return "#%02x%02x%02x" % rgb
        return "rgba(%d, %d, %d, %g)" % (*rgb, round(float(a), 3))
    m = re.fullmatch(r"color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+))?\)", s)
    if m:
        rgb = tuple(int(round(float(x) * 255)) for x in m.groups()[:3])
        a = m.group(4)
        if a is None or float(a) >= 0.999:
            return "#%02x%02x%02x" % rgb
        return "rgba(%d, %d, %d, %g)" % (*rgb, round(float(a), 3))
    raise ValueError("not a colour: " + s)


def color_token(name, theme, description=None):
    block = COLORS[theme]["computed"].get(name)
    if not block:
        raw = (LIGHT if theme == "light" else DARK)[name]["value"]
        val = rgb_to_hex(raw) if raw.startswith("#") or raw in ("white", "black") else raw
        src = f"css-var {name} ({theme}), declared"
    else:
        val = rgb_to_hex(block["computed"])
        src = f"Measured computed style of var({name}) on html at webflow.com, {theme}, 1440px"
    t = {"$value": val, "$type": "color", "$extensions": {"source": src}}
    if description:
        t["$description"] = description
    return t


def declared(name, theme="light"):
    return (LIGHT if theme == "light" else DARK)[name]["value"]


def dim_from_clamp(raw):
    """Desktop end of a Webflow clamp(min, preferred, max) is the max, in rem.
    The authored string is kept; the single length is Derived."""
    m = re.search(r",\s*([\d.]+)\s*\*\s*1rem\)\s*$", raw.replace(" ", ""))
    if not m:
        m = re.search(r",\s*([\d.]+)\s*\*\s*1rem\)", raw.replace(" ", ""))
    if m:
        return "%grem" % float(m.group(1)), "Derived desktop end of clamp, authored: " + raw[:140]
    if re.fullmatch(r"-?[\d.]+(rem|px|em)", raw.strip()):
        return raw.strip(), "Measured css-var"
    return None, raw


def dim_token(name, path_note):
    raw = declared(name)
    val, note = dim_from_clamp(raw)
    if val is None:
        return None
    return {"$value": val, "$type": "dimension", "$extensions": {"source": f"{note}; css-var {name}; {path_note}"}}


def num_token(name):
    raw = declared(name).strip()
    if re.fullmatch(r"-?\d+(\.\d+)?", raw):
        val = float(raw) if "." in raw else int(raw)
        return {"$value": val, "$type": "number", "$extensions": {"source": f"Measured css-var {name}"}}
    return None


def font_token(name):
    raw = declared(name).strip().strip('"')
    return {"$value": raw, "$type": "fontFamily", "$extensions": {"source": f"Measured css-var {name}"}}


def weight_token(name):
    raw = declared(name).strip()
    if re.fullmatch(r"\d+", raw):
        return {"$value": int(raw), "$type": "fontWeight", "$extensions": {"source": f"Measured css-var {name}"}}
    return None


def duration_token(name):
    raw = declared(name).strip()
    m = re.fullmatch(r"([\d.]+)(m?s)", raw)
    if not m:
        return None
    ms = float(m.group(1)) * (1 if m.group(2) == "ms" else 1000)
    return {"$value": "%gms" % ms, "$type": "duration", "$extensions": {"source": f"Measured css-var {name} ({raw})"}}


core = {
    "color": {
        "neutral": {},
        "blue": {},
        "secondary": {},
    },
    "fontFamily": {
        "ui": font_token("--_typography---fonts--primary-font"),
        "mono": {"$value": "Inconsolata, ui-monospace, monospace", "$type": "fontFamily",
                 "$extensions": {"source": "Measured @font-face family Inconsolata loaded by webflow.com; stack completed with a generic fallback (Derived)"}},
    },
    "radius": {},
    "spacing": {},
    "motion": {},
}

for step in ("100", "200", "300", "400", "500", "600", "700", "800", "900"):
    core["color"]["neutral"][step] = color_token(f"--_color---neutral--gray-{step}", "light")
core["color"]["neutral"]["white"] = color_token("--_color---neutral--white", "light")
core["color"]["neutral"]["black"] = color_token("--_color---neutral--black", "light")
core["color"]["blue"]["300"] = color_token("--_color---blue-300", "light")
core["color"]["blue"]["400"] = color_token("--_color---primary--blue-400", "light")
core["color"]["blue"]["500"] = color_token("--_color---primary--webflow-blue", "light", "Brand blue. meta theme-color is #146EF5.")
core["color"]["blue"]["600"] = color_token("--_color---primary--blue-600", "light")
for hue in ("green", "orange", "pink", "purple", "red", "yellow"):
    core["color"]["secondary"][hue] = color_token(f"--_color---secondary--{hue}", "light")

core["radius"]["button"] = {"$value": "0.25rem", "$type": "dimension", "$extensions": {"source": "Measured css-var --_components---button--border-radius"}}
core["radius"]["card"] = {"$value": "0.5rem", "$type": "dimension", "$extensions": {"source": "Measured css-var --_components---card--border-radius"}}
core["radius"]["input"] = {"$value": "0.25rem", "$type": "dimension", "$extensions": {"source": "Measured css-var --_components---input--border-radius"}}

for step, name in (("xs", "margin-xs"), ("sm", "margin-sm"), ("md", "margin-md"), ("lg", "margin-lg"), ("xl", "margin-xl")):
    tok = dim_token(f"--_layout---spacing--{name}", "desktop end of the responsive clamp")
    if tok:
        core["spacing"][step] = tok

for step, var in (("1", "--transition-duration-1"), ("2", "--transition-duration-2"), ("3", "--transition-duration-3"), ("4", "--transition-duration-4")):
    core["motion"]["duration" + step] = duration_token(var)
core["motion"]["ease"] = {
    "$value": [0.645, 0.045, 0.355, 1],
    "$type": "cubicBezier",
    "$extensions": {"source": "Measured css-var --transition-timing-inoutcubic"},
}

# Type composites use the desktop end of the clamp as the size (Derived) and the measured weight and line height.
def type_style(role, size_var, weight_var, line_var, family_var="--_typography---fonts--primary-font"):
    size, note = dim_from_clamp(declared(size_var))
    weight = int(declared(weight_var))
    line = declared(line_var).strip()
    line_n = float(line) if re.fullmatch(r"[\d.]+", line) else line
    family = declared(family_var).split(",")[0].strip().strip('"')
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size or declared(size_var)[:40],
            "fontWeight": weight,
            "lineHeight": line_n,
        },
        "$type": "typography",
        "$extensions": {"source": f"Measured css-vars {size_var}, {weight_var}, {line_var}. Size: {note}"},
    }

core["typography"] = {
    "display": type_style("display", "--_typography---h0--font-size", "--_typography---h0--font-weight", "--_typography---h0--line-height"),
    "heading": type_style("heading", "--_typography---h1--font-size", "--_typography---h1--font-weight", "--_typography---h1--line-height"),
    "heading2": type_style("heading2", "--_typography---h2--font-size", "--_typography---h2--font-weight", "--_typography---h2--line-height"),
    "heading3": type_style("heading3", "--_typography---h3--font-size", "--_typography---h3--font-weight", "--_typography---h3--line-height"),
    "body": type_style("body", "--_typography---paragraph-body--font-size", "--_typography---paragraph-body--font-weight", "--_typography---paragraph-body--line-height"),
    "label": type_style("label", "--_typography---eyebrow--font-size", "--_typography---eyebrow--font-weight", "--_typography---eyebrow--line-height"),
    "caption": type_style("caption", "--_typography---caption--font-size", "--_typography---caption--font-weight", "--_typography---caption--line-height"),
}


def semantic(theme):
    return {
        "page": color_token("--colors--background", theme, "Page background"),
        "surface": color_token("--colors--secondary-background", theme, "Secondary surface"),
        "text": color_token("--colors--text", theme, "Primary text"),
        "muted": color_token("--colors--text-secondary", theme, "Secondary text"),
        "accent": color_token("--colors--primary-accent", theme, "Primary accent. meta theme-color #146EF5."),
        "border": color_token("--colors--border", theme, "Default border"),
        "accentText": color_token("--colors--primary-accent-text", theme),
        "accentSoft": color_token("--colors--primary-accent-background", theme),
        "onAccent": {"$value": "#ffffff", "$type": "color", "$extensions": {"source": "Measured computed color of a primary button on webflow.com, both themes: rgb(255, 255, 255)"}},
        "component": {
            "button": {
                "radius": {"$value": "{radius.button}", "$type": "dimension", "$extensions": {"source": "alias of measured button radius"}},
                "background": color_token("--colors--primary-accent", theme),
                "text": {"$value": "{onAccent}", "$type": "color", "$extensions": {"source": "alias of measured on-accent"}},
                "fontSize": {"$value": "1rem", "$type": "dimension", "$extensions": {"source": "Measured css-var --_components---button--font-size"}},
                "fontWeight": weight_token("--_components---button--font-weight"),
            },
            "input": {
                "radius": {"$value": "{radius.input}", "$type": "dimension", "$extensions": {"source": "alias of measured input radius"}},
                "fontSize": {"$value": "1rem", "$type": "dimension", "$extensions": {"source": "Measured css-var --_components---input--font-size"}},
            },
            "card": {
                "radius": {"$value": "{radius.card}", "$type": "dimension", "$extensions": {"source": "alias of measured card radius"}},
            },
            "nav": {
                "height": {"$value": "4.25rem", "$type": "dimension", "$extensions": {"source": "Measured css-var --_components---nav--height"}},
            },
        },
    }


light = semantic("light")
dark = semantic("dark")

# Fix aliases that point at sibling tokens without a set prefix. Tokens Studio
# resolves within the set; onAccent lives in the same set.
for theme_set in (light, dark):
    theme_set["component"]["button"]["text"] = {"$value": "#ffffff", "$type": "color", "$extensions": {"source": "Measured computed color of a primary button, rgb(255, 255, 255)"}}
    theme_set["component"]["button"]["radius"]["$value"] = "0.25rem"
    theme_set["component"]["input"]["radius"]["$value"] = "0.25rem"
    theme_set["component"]["card"]["radius"]["$value"] = "0.5rem"

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Default public theme. html has no u-mode-dark. Body background computed rgb(255, 255, 255)."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Public theme after the Dark mode control. html.u-mode-dark. Body background computed rgb(8, 8, 8)."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

# Drop typography entries whose size is not a single length (DTCG dimension inside composite is a string here; keep them).
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote", HERE / "tokens.json")
print("light.page", light["page"]["$value"], "dark.page", dark["page"]["$value"])
print("light.text", light["text"]["$value"], "dark.text", dark["text"]["$value"])
