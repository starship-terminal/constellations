#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Every value is a custom property declared in
https://visitors.now/assets/styles-pNqCiRay.css and read on 2026-11-21.
`:root` is the live light theme. `.dark` is declared in the same file and
was not applied on any public page, so the dark set is stylesheet evidence.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
THEME = RAW["themeLayer"]
ROOT = RAW["root"]
DARK = RAW["dark"]
SRC = "styles-pNqCiRay.css on https://visitors.now/ (2026-11-21)"


def color(value, source, description=None):
    token = {"$value": value, "$type": "color", "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, typ="number"):
    return {"$value": value, "$type": typ, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def expand_hex(v):
    v = v.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}", v):
        return "#" + "".join(c * 2 for c in v[1:])
    if re.fullmatch(r"#[0-9a-f]{4}", v):
        return "#" + "".join(c * 2 for c in v[1:])
    return v


def group_colors(props, prefix, source):
    out = {}
    for name, value in props.items():
        if not name.startswith(prefix) or name.startswith(prefix + "a"):
            continue
        step = name[len(prefix):]
        if not step.isdigit():
            continue
        out[step] = color(expand_hex(value), f"{source} {name}")
    return out


def alpha_group(props, hue, source):
    out = {}
    for step in ("1", "2", "3", "4"):
        name = f"--{hue}-a{step}"
        if name in props:
            out[step] = color(expand_hex(props[name]), f"{source} {name}")
    return out


HUES = ["gray", "blue", "red", "green", "amber", "purple", "sky", "yellow", "pink", "orange"]


def palette(props, source):
    out = {}
    for hue in HUES:
        out[hue] = group_colors(props, f"--{hue}-", source)
        alphas = alpha_group(props, hue, source)
        if alphas:
            out[hue + "-alpha"] = alphas
    return out


def semantic(props, source, theme_note):
    def c(name):
        return color(expand_hex(props[name]), f"{source} {name}. {theme_note}")

    return {
        "background": {
            "page": c("--background"),
            "subtle": c("--background-subtle"),
            "bg-1": c("--bg-1"),
            "bg-2": c("--bg-2"),
            "bg-3": c("--bg-3"),
            "bg-4": c("--bg-4"),
        },
        "text": {
            "fg-1": c("--fg-1"),
            "fg-2": c("--fg-2"),
            "fg-3": c("--fg-3"),
            "fg-4": c("--fg-4"),
        },
        "alpha": {
            "bg-1": c("--bg-a1"),
            "bg-2": c("--bg-a2"),
            "bg-3": c("--bg-a3"),
            "bg-4": c("--bg-a4"),
            "fg-1": c("--fg-a1"),
            "fg-2": c("--fg-a2"),
            "fg-3": c("--fg-a3"),
            "fg-4": c("--fg-a4"),
        },
    }


def shadow(value, source):
    return {"$value": value, "$type": "shadow", "$extensions": {"source": source}}


core = {
    "font": {
        "family": {
            "sans": font(
                ["OpenRunde", "Open Runde", "Inter", "sans-serif"],
                f"{SRC} --default-font-family",
            ),
            "mono": font(
                ["SF Mono", "Menlo", "OpenRunde", "Open Runde", "sans-serif"],
                f"{SRC} --font-mono",
            ),
        },
        "weight": {
            "normal": num(400, f"{SRC} --font-weight-normal"),
            "medium": num(500, f"{SRC} --font-weight-medium"),
            "semibold": num(600, f"{SRC} --font-weight-semibold"),
            "extrabold": num(800, f"{SRC} --font-weight-extrabold"),
        },
    },
    "palette": palette(ROOT, f"{SRC} :root"),
    "radius": {
        "1": dim("0.125rem", f"{SRC} --radius-1"),
        "2": dim("0.25rem", f"{SRC} --radius-2"),
        "3": dim("0.375rem", f"{SRC} --radius-3"),
        "4": dim("0.5rem", f"{SRC} --radius-4"),
        "5": dim("0.75rem", f"{SRC} --radius-5"),
        "6": dim("1rem", f"{SRC} --radius-6"),
        "2xl": dim("1rem", f"{SRC} --radius-2xl"),
        "3xl": dim("1.5rem", f"{SRC} --radius-3xl"),
        "4xl": dim("2rem", f"{SRC} --radius-4xl"),
    },
    "spacing": {
        "unit": dim("0.25rem", f"{SRC} --spacing"),
    },
    "fontSize": {},
    "blur": {
        "sm": dim(THEME["--blur-sm"], f"{SRC} --blur-sm"),
        "md": dim(THEME["--blur-md"], f"{SRC} --blur-md"),
        "lg": dim(THEME["--blur-lg"], f"{SRC} --blur-lg"),
        "xl": dim(THEME["--blur-xl"], f"{SRC} --blur-xl"),
        "2xl": dim(THEME["--blur-2xl"], f"{SRC} --blur-2xl"),
    },
    "duration": {
        "default": {"$value": "150ms", "$type": "duration", "$extensions": {"source": f"{SRC} --default-transition-duration (.15s)"}},
    },
    "easing": {
        "out": {"$value": [0, 0, 0.2, 1], "$type": "cubicBezier", "$extensions": {"source": f"{SRC} --ease-out"}},
        "in-out": {"$value": [0.4, 0, 0.2, 1], "$type": "cubicBezier", "$extensions": {"source": f"{SRC} --ease-in-out"}},
    },
    "shadow": {
        "1": shadow(THEME["--shadow-1"], f"{SRC} --shadow-1"),
        "2": shadow(THEME["--shadow-2"], f"{SRC} --shadow-2"),
        "3": shadow(THEME["--shadow-3"], f"{SRC} --shadow-3"),
        "4": shadow(THEME["--shadow-4"], f"{SRC} --shadow-4"),
    },
    "container": {},
}

for step in ("xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "9xl"):
    core["fontSize"][step] = dim(THEME[f"--text-{step}"], f"{SRC} --text-{step}")
for name in ("xs", "sm", "md", "lg", "xl", "3xl", "5xl"):
    core["container"][name] = dim(THEME[f"--container-{name}"], f"{SRC} --container-{name}")

light_note = "Computed on the public pages, which render :root with no .dark class."
dark_note = "Declared on .dark in the same stylesheet. Not applied on any public page visited, so this is stylesheet evidence, not a rendered measurement."

tokens = {
    "core": core,
    "light": semantic(ROOT, f"{SRC} :root", light_note),
    "dark": semantic(DARK, f"{SRC} .dark", dark_note),
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Tailwind --tw-* utilities were skipped.",
            "oklch() leftovers (--color-blue-500, --color-gray-600, --color-gray-700) are Tailwind defaults, not the product ramps.",
            "Line-height calc() tokens (--text-*--line-height) stay in raw/css-vars.json.",
            "Dark purple-4 is #9580ff in .dark and #918df6 in :root. The core palette keeps the :root ramp.",
        ]
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
