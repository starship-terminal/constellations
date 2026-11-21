#!/usr/bin/env python3
"""Build tokens.json from the Letterboxd public CSS harvest.

Source: raw/css-vars.json, written by tools/capture/harvest.mjs from a
signed-out load of https://letterboxd.com/ at 1440 x 900 on 2026-11-21.
The site paints one dark field. There is no theme switch, so dark is empty.

Every token carries $extensions.source. Edit the harvest, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = V["resolved"]["light"]


def norm_color(v):
    v = str(v).strip().lower()
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
            return "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour this builder converts: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem|em)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


def tok(val, ty, source):
    check(source, ty, val)
    return {"$value": val, "$type": ty, "$extensions": {"source": source}}


def color_tok(name):
    return tok(norm_color(DECL[name]), "color", f"css-var {name} (light)")


def rem_to_px(v):
    v = v.strip()
    if v.endswith("px"):
        return v
    if v.endswith("rem"):
        n = float(v[:-3])
        px = n * 16
        text = ("%g" % px) + "px"
        return text
    raise ValueError(v)


def dim_tok(name, note=""):
    raw = DECL[name].strip()
    if raw.endswith("rem"):
        val = rem_to_px(raw)
        src = f"css-var {name} = {raw}, converted at 16px root"
    else:
        val = raw
        src = f"css-var {name}"
    if note:
        src += "; " + note
    return tok(val, "dimension", src)


def ms(name):
    raw = DECL[name].strip()
    if raw == "calc(1s * 1 / 3)":
        return tok("333ms", "duration", f"css-var {name} = {raw}, resolved as one third of a second")
    if raw.endswith("ms"):
        n = int(float(raw[:-2]))
    elif raw.endswith("s"):
        n = int(round(float(raw[:-1]) * 1000))
    else:
        raise ValueError(name + " " + raw)
    return tok(f"{n}ms", "duration", f"css-var {name} = {raw}")


def bezier(name):
    raw = DECL[name].strip()
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", raw)
    if not m:
        raise ValueError(raw)
    return tok([float(x) for x in m.groups()], "cubicBezier", f"css-var {name}")


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


core = {
    "font": {
        "family": {
            "sans": tok(
                "GraphikWeb, -apple-system, system-ui, Segoe UI, Hiragino Sans, Meiryo, sans-serif",
                "fontFamily",
                "css-var --font-stack-graphik; computed on body at letterboxd.com",
            ),
            "display": tok(
                "TiemposHeadlineWeb, Georgia, serif",
                "fontFamily",
                "css-var --font-stack-tiempos-headline",
            ),
            "serif": tok(
                "TiemposTextWeb, Georgia, serif",
                "fontFamily",
                "css-var --font-stack-tiempos-text",
            ),
        },
        "weight": {
            "light": tok(300, "fontWeight", "@font-face GraphikWeb 300"),
            "regular": tok(400, "fontWeight", "@font-face GraphikWeb 400"),
            "bold": tok(700, "fontWeight", "@font-face GraphikWeb 700; nav links compute 700"),
            "black": tok(800, "fontWeight", "@font-face GraphikWeb 800"),
        },
        "size": {},
        "lineHeight": {},
    },
    "space": {},
    "radius": {},
    "duration": {},
    "easing": {},
    "layout": {
        "content-gutter": dim_tok("--layout-content-gutter"),
        "page-gutter": dim_tok("--page-gutter-width-fixed"),
    },
    "size": {
        "search-height": tok("30px", "dimension", "measured #search-q height on the homepage header"),
        "nav-link-height": tok("23px", "dimension", "measured a.navlink height on the homepage header"),
        "logo-height": tok("25px", "dimension", "measured a.logo height on the homepage header"),
    },
    "borderWidth": {
        "focus": tok("2px", "dimension", "measured focus ring width is not a published token; recorded as the common control outline. Not captured as a live focus ring."),
    },
}

for name, key in (
    ("--heading-1-font-size", "heading-1"),
    ("--heading-2-font-size", "heading-2"),
    ("--heading-3-font-size", "heading-3"),
    ("--heading-4-font-size", "heading-4"),
    ("--heading-5-font-size", "heading-5"),
    ("--heading-6-font-size", "heading-6"),
    ("--body-large-font-size", "body-large"),
    ("--body-medium-font-size", "body-medium"),
    ("--body-small-font-size", "body-small"),
    ("--body-meta-font-size", "body-meta"),
    ("--body-tiny-font-size", "body-tiny"),
    ("--title-all-caps-font-size", "label"),
):
    core["font"]["size"][key] = dim_tok(name)

for name in (
    "--spacing-xsmall",
    "--spacing-small",
    "--spacing-medium",
    "--spacing-large",
    "--spacing-xlarge",
    "--spacing-dense-small",
    "--spacing-dense-medium",
    "--spacing-dense-large",
    "--spacing-sparse-small",
    "--spacing-sparse-medium",
    "--spacing-sparse-large",
    "--spacing-adjacent-listing",
    "--spacing-adjacent-component",
    "--spacing-grid-gutter",
):
    key = name.removeprefix("--spacing-")
    core["space"][key] = dim_tok(name)

for name in (
    "--border-radius-xxsmall",
    "--border-radius-xsmall",
    "--border-radius-small",
    "--border-radius-medium",
    "--border-radius-large",
    "--poster-border-radius",
    "--control-medium-border-radius",
    "--panel-border-radius-default",
):
    key = name.removeprefix("--").replace("border-radius-", "radius-")
    core["radius"][key] = dim_tok(name)

for name in ("--duration-xshort", "--duration-short", "--duration-medium", "--duration-long", "--duration-xlong", "--dropdown-fade-in-duration"):
    core["duration"][name.removeprefix("--duration-").removeprefix("dropdown-fade-in-duration") or "dropdown"] = ms(name)
core["duration"]["dropdown"] = ms("--dropdown-fade-in-duration")

for name, key in (
    ("--timing-function-ease-out-expo", "out-expo"),
    ("--timing-function-ease-out-back", "out-back"),
    ("--timing-function-ease-in-back", "in-back"),
):
    core["easing"][key] = bezier(name)

light = {
    "page": color_tok("--theme-background-color"),
    "page-hover": color_tok("--theme-background-hover-color"),
    "surface": color_tok("--theme-surface-color"),
    "surface-hover": color_tok("--theme-surface-hover-color"),
    "text": color_tok("--theme-body-content-color"),
    "text-high": color_tok("--theme-body-high-contrast-content-color"),
    "muted": color_tok("--theme-body-low-contrast-content-color"),
    "heading": color_tok("--theme-heading-content-color"),
    "link": color_tok("--theme-body-link-content-color"),
    "link-hover": color_tok("--theme-body-link-hover-content-color"),
    "link-active": color_tok("--theme-body-link-active-content-color"),
    "border": color_tok("--theme-separator-color"),
    "border-secondary": color_tok("--theme-separator-secondary-color"),
    "accent": color_tok("--theme-brand-green-content-color"),
    "accent-surface": color_tok("--theme-brand-green-surface-color"),
    "accent-hover": color_tok("--theme-brand-green-hover-surface-color"),
    "accent-pressed": color_tok("--theme-brand-green-active-surface-color"),
    "blue": color_tok("--theme-brand-blue-content-color"),
    "blue-surface": color_tok("--theme-brand-blue-surface-color"),
    "orange": color_tok("--theme-brand-orange-content-color"),
    "orange-surface": color_tok("--theme-brand-orange-surface-color"),
    "danger": color_tok("--theme-button-destructive-active-surface-color"),
    "danger-hover": color_tok("--theme-button-destructive-hover-surface-color"),
    "focus": color_tok("--theme-focus-color"),
    "button": color_tok("--theme-button-default-surface-color"),
    "button-hover": color_tok("--theme-button-default-hover-surface-color"),
    "button-text": color_tok("--theme-button-default-content-color"),
    "primary-button": color_tok("--theme-button-primary-surface-color"),
    "primary-button-text": color_tok("--theme-button-primary-content-color"),
    "poster": color_tok("--poster-background-color"),
    "rating": color_tok("--theme-rating-icon-color"),
    "like": color_tok("--theme-like-icon-color"),
    "metadata": color_tok("--theme-metadata-content-color"),
    "fill": color_tok("--theme-fill-color"),
    "on-accent": color_tok("--theme-brand-mono-primary-color"),
}

# Drop the accidental empty key if duration loop created one.
core["duration"].pop("", None)

doc = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "dark": {},
    "$themes": [
        {"id": "light", "name": "Letterboxd", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
    "$extensions": {
        "source": V["source"],
        "capturedAt": V.get("capturedAt"),
        "note": "Letterboxd's public site paints one dark field. The set is named light because the catalog expects a light palette. There is no second theme.",
    },
}

# Walk and check
def walk(node, prefix):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            check(path, v["$type"], v["$value"])
        elif isinstance(v, dict):
            walk(v, path)

walk(core, "core")
walk(light, "light")

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "core groups", list(core), "light", len(light))
