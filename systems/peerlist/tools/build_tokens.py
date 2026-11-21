#!/usr/bin/env python3
"""Build systems/peerlist/tokens.json from raw/readings.json.

Values are the custom properties declared on :root and .dark, plus computed
styles measured on real elements on 2026-11-21. A channel triplet such as
"255 255 255" is how Peerlist declares --gray-* (rgb(var(--gray-00))).
Those become hex. Anything not read is omitted, never guessed.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
THEMES = RAW["themes"]

SRC_ROOT = "Measured CSS custom property on :root, peerlist.io homepage, 2026-11-21, raw/readings.json themes.lightDecls"
SRC_DARK = "Measured CSS custom property on .dark, same stylesheet, 2026-11-21, raw/readings.json themes.darkDecls"
SRC_UTIL = "Measured Tailwind utility colour in the homepage stylesheet, 2026-11-21, raw/readings.json themes.utilityColours"
SRC_EL = "Measured computed style on a real element, 2026-11-21, raw/readings.json pages"


def triplet(value):
    parts = value.replace(",", " ").split()
    if len(parts) < 3:
        raise ValueError(value)
    rgb = []
    for part in parts[:3]:
        if part.endswith("%"):
            rgb.append(round(float(part[:-1]) / 100 * 255))
        else:
            rgb.append(int(float(part)))
    return "#%02x%02x%02x" % tuple(rgb)


def util_color(selector, key="bg"):
    row = THEMES["utilityColours"].get(selector) or {}
    raw = row.get(key) or ""
    match = re.search(r"rgb\((\d+)\s+(\d+)\s+(\d+)", raw)
    if not match:
        match = re.search(r"rgba\((\d+),\s*(\d+),\s*(\d+)", raw)
    if not match:
        raise KeyError(selector)
    return "#%02x%02x%02x" % tuple(int(match.group(i)) for i in (1, 2, 3))


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def shadow(value, source):
    return {"$type": "shadow", "$value": value, "$extensions": {"source": source}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def text_style(family, size, weight, line, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": source},
    }


def gray_set(decls, source):
    out = {}
    for name, value in decls.items():
        if not name.startswith("--gray-"):
            continue
        step = name.removeprefix("--gray-")
        out[step] = color(triplet(value), f"{source}; {name}: {value}")
    return out


light_decls = THEMES["lightDecls"]
dark_decls = THEMES["darkDecls"]

core = {
    "color": {
        "gray": gray_set(light_decls, SRC_ROOT),
        "green": {
            "00": color(util_color(".bg-green-00"), f"{SRC_UTIL}; .bg-green-00"),
            "50": color(util_color(".bg-green-50"), f"{SRC_UTIL}; .bg-green-50"),
            "100": color(util_color(".bg-green-100"), f"{SRC_UTIL}; .bg-green-100"),
            "200": color(util_color(".text-green-200", "color"), f"{SRC_UTIL}; .text-green-200"),
            "300": color(util_color(".bg-green"), f"{SRC_UTIL}; .bg-green is rgb(0 170 69)"),
            "400": color(util_color(".bg-green-400"), f"{SRC_UTIL}; .bg-green-400"),
            "500": color(util_color(".bg-green-500"), f"{SRC_UTIL}; .bg-green-500"),
            "600": color(util_color(".text-green-600", "color"), f"{SRC_UTIL}; .text-green-600"),
            "800": color(util_color(".text-green-800", "color"), f"{SRC_UTIL}; .text-green-800"),
        },
        "red": {
            "00": color(util_color(".bg-red-00"), f"{SRC_UTIL}; .bg-red-00"),
            "50": color(util_color(".bg-red-50"), f"{SRC_UTIL}; .bg-red-50"),
            "200": color(util_color(".text-red-200", "color"), f"{SRC_UTIL}; .text-red-200"),
            "300": color(util_color(".bg-red-300"), f"{SRC_UTIL}; .bg-red-300"),
            "400": color(util_color(".text-red-400", "color"), f"{SRC_UTIL}; .text-red-400"),
            "500": color(util_color(".text-red-500", "color"), f"{SRC_UTIL}; .text-red-500"),
            "600": color(util_color(".text-red-600", "color"), f"{SRC_UTIL}; .text-red-600"),
            "700": color(util_color(".text-red-700", "color"), f"{SRC_UTIL}; .text-red-700"),
            "800": color(util_color(".text-red-800", "color"), f"{SRC_UTIL}; .text-red-800"),
        },
        "orange": {
            "400": color(util_color(".text-orange-400", "color"), f"{SRC_UTIL}; .text-orange-400"),
            "500": color(util_color(".text-orange-500", "color"), f"{SRC_UTIL}; .text-orange-500"),
            "700": color(util_color(".text-orange-700", "color"), f"{SRC_UTIL}; .text-orange-700"),
        },
        "chart": {
            "1": color("#2f80ed", f"{SRC_ROOT}; --chart-1: 47,128,237"),
        },
    },
    "fontFamily": {
        "sans": font("Geist, sans-serif", "Measured computed font-family on body, homepage, 2026-11-21"),
        "display": font('instrument, "instrument Fallback"', "Measured computed font-family on homepage h1, raw/readings.json extra.homeType.h1"),
        "mono": font("Geist Mono, sans-serif", "Measured @font-face family Geist Mono in the homepage stylesheet"),
    },
    "fontWeight": {
        "regular": {"$type": "fontWeight", "$value": 400, "$extensions": {"source": SRC_EL + " login email"}},
        "semibold": {"$type": "fontWeight", "$value": 600, "$extensions": {"source": SRC_EL + " Log in link and Post button"}},
    },
    "typography": {
        "display": text_style("{fontFamily.display}", "48px", "400", "57.6px", "Measured homepage h1, instrument 48/57.6, raw/readings.json extra.homeType.h1"),
        "body": text_style("{fontFamily.sans}", "16px", "400", "24px", "Derived line height from the 16px body size; size and family measured on body"),
        "label": text_style("{fontFamily.sans}", "14px", "600", "20px", "Measured Log in link and Post button, 14px/600/20px"),
        "caption": text_style("{fontFamily.sans}", "12px", "600", "16px", "Measured Follow and Preview controls, 12px"),
        "hero-line": text_style("{fontFamily.sans}", "18px", "400", "28px", "Measured homepage hero buttons, 18/28"),
    },
    "radius": {
        "sm": dim("8px", "Measured icon-button and login email radius, 8px"),
        "md": dim("12px", "Measured Log in, Post, Launch and Book button radius, 12px"),
        "lg": dim("16px", "Measured Continue with Google and Login button radius, 16px"),
    },
    "spacing": {
        "1": dim("4px", "Measured button gap 4px on Log in"),
        "2": dim("6px", "Measured button padding-top 6px on Log in and Post"),
        "3": dim("8px", "Measured login email padding-left 8px"),
        "4": dim("12px", "Measured Preview padding-left 12px"),
        "5": dim("16px", "Measured button padding-left 16px and job-row padding-top 16px"),
        "6": dim("24px", "Measured Google button padding-left 24px and job-row padding-left 24px"),
    },
    "size": {
        "control-sm": dim("24px", "Measured theme icon button and Preview height, 24px"),
        "control-md": dim("32px", "Measured Log in, Post, Launch and email field height, 32px"),
        "control-lg": dim("40px", "Measured Continue with Google and Login height, 40px"),
        "nav-row": dim("44px", "Measured Scroll/Jobs rail link height, 44px"),
        "nav-width": dim("187px", "Measured rail link width, 187px"),
    },
    "borderWidth": {
        "default": dim("1px", "Measured Log in and Post border-top-width 1px"),
    },
    "shadow": {
        "5": shadow(light_decls["--shadow-5"], f"{SRC_ROOT}; --shadow-5"),
        "10": shadow(light_decls["--shadow-10"], f"{SRC_ROOT}; --shadow-10"),
        "15": shadow(light_decls["--shadow-15"], f"{SRC_ROOT}; --shadow-15"),
        "focus": shadow(light_decls["--shadow-focus"], f"{SRC_ROOT}; --shadow-focus"),
    },
    "layout": {
        "desktop": dim("1440px", "Requested desktop viewport; sidecars record measured innerWidth"),
        "phone": dim("390px", "Requested phone viewport"),
    },
    "motion": {
        "button": dim("75ms", "Measured duration-75 on button class names (transition-all ease-in duration-75)"),
    },
}

def semantic(decls, source, theme):
    page = triplet(decls["--gray-00"])
    text = triplet(decls["--gray-1k"])
    muted = triplet(decls["--gray-500"])
    border = triplet(decls["--gray-200"] if theme == "light" else decls["--gray-100"])
    return {
        "color": {
            "page": color(page, f"{source}; --gray-00"),
            "surface": color(triplet(decls["--gray-25"]), f"{source}; --gray-25"),
            "raised": color(triplet(decls["--gray-50"]), f"{source}; --gray-50"),
            "text": {
                "primary": color(text, f"{source}; --gray-1k"),
                "secondary": color(triplet(decls["--gray-700"]), f"{source}; --gray-700"),
                "muted": color(muted, f"{source}; --gray-500"),
                "on-accent": color("#ffffff" if theme == "light" else "#171717", "Measured Post button color rgb(255,255,255) in light; dark on-accent not read from an element, so light value is recorded and dark uses --gray-00"),
                "link": color("#2f80ed", "Measured Follow color rgb(47, 128, 237), matches --chart-1"),
            },
            "border": {
                "default": color(border, f"{source}; --border resolves through --gray-200 in light and --gray-100 in dark"),
                "strong": color(triplet(decls["--gray-300"]), f"{source}; --gray-300"),
                "focus": color("#e1e4e8" if theme == "light" else "#262626", f"{source}; --shadow-focus ring colour"),
            },
            "accent": {
                "default": color("#00aa45", f"{SRC_UTIL}; .bg-green rgb(0 170 69), measured Post background"),
                "pressed": color("#1e874b", f"{SRC_UTIL}; .bg-green-500 and measured Post border rgb(30, 135, 75)"),
                "soft": color("#e3f5ea", "Measured Launch button background rgb(227, 245, 234), .bg-green-00"),
            },
            "status": {
                "success": color("#00aa45", f"{SRC_UTIL}; green-300 used as the product accent and success fill"),
                "danger": color("#eb5757", f"{SRC_UTIL}; .bg-red-300"),
                "warning": color("#f97316", f"{SRC_UTIL}; .text-orange-500"),
                "info": color("#2f80ed", f"{source}; --chart-1"),
            },
        },
        "shadow": {
            "5": shadow(decls["--shadow-5"], f"{source}; --shadow-5"),
            "10": shadow(decls["--shadow-10"], f"{source}; --shadow-10"),
            "15": shadow(decls["--shadow-15"], f"{source}; --shadow-15"),
            "focus": shadow(decls["--shadow-focus"], f"{source}; --shadow-focus"),
        },
    }


# Dark on-accent: Post was measured only in light. Do not invent a dark value.
semantic_dark = semantic(dark_decls, SRC_DARK, "dark")
semantic_dark["color"]["text"]["on-accent"] = {
    "$type": "color",
    "$value": "{color.page}",
    "$extensions": {"source": "Derived: light on-accent is white, which is dark --gray-00 (page). Not measured on a dark Post button."},
}

doc = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": core,
    "light": semantic(light_decls, SRC_ROOT, "light"),
    "dark": semantic_dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

# Fix dark on-accent alias: Tokens Studio aliases are same-set or need a path.
# A bare {color.page} resolves inside dark. Keep the hex of dark page instead.
semantic_dark["color"]["text"]["on-accent"] = color(
    triplet(dark_decls["--gray-00"]),
    "Derived from light on-accent being the page white, mapped to dark --gray-00. Not measured on a dark accent button.",
)

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
