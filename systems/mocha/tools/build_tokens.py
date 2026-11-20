#!/usr/bin/env python3
"""Build tokens.json from the Mocha public capture.

Mocha's marketing host (getmocha.com) has no A record as of 2026-11-19.
mocha.app and the product hosts answer 410 with a static shutdown page.
The live designed surface is docs.getmocha.com (Mintlify), which declares
RGB-triplet custom properties on :root (--primary, --primary-light,
--primary-dark, --background-light, --background-dark, --gray-50..950).
html.light and html.dark both resolve. The 410 page on app.mocha.app paints
a second, inline palette (no custom properties).

Nothing here is invented. Triplet tokens become sRGB hex. Component colours
are the computed styles in raw/components-computed.json.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))

VARS = json.loads((RAW / "css-vars.json").read_text())
LIGHT = VARS["resolved"]["light"]
COMP = json.loads((RAW / "components-computed.json").read_text())

S = "Resolved from docs.getmocha.com :root custom properties, 2026-11-19"
M = "Measured computed style, docs.getmocha.com, 2026-11-19, 1440"
G = "Measured computed style, app.mocha.app 410 page, 2026-11-19, 1440"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def triplet(name):
    raw = LIGHT[name]["value"]
    parts = [int(p) for p in raw.split()]
    if len(parts) != 3:
        raise SystemExit(f"{name} is not an RGB triplet: {raw}")
    return "#{:02x}{:02x}{:02x}".format(*parts), raw


def ramp(prefix):
    out = {}
    for key, node in LIGHT.items():
        if not key.startswith(prefix):
            continue
        step = key[len(prefix):]
        if not step.isdigit():
            continue
        hexed, raw = triplet(key)
        out[step] = color(hexed, f"{S}: {key} was {raw}")
    return dict(sorted(out.items(), key=lambda kv: int(kv[0])))


def state(name, key):
    return ((COMP["components"].get(name) or {}).get("states") or {}).get(key) or {}


def style(name, key):
    return (state(name, key).get("style") or {})


primary, primary_raw = triplet("--primary")
primary_light, primary_light_raw = triplet("--primary-light")
primary_dark, primary_dark_raw = triplet("--primary-dark")
bg_light, bg_light_raw = triplet("--background-light")
bg_dark, bg_dark_raw = triplet("--background-dark")
tooltip, tooltip_raw = triplet("--tooltip-foreground")

core = {
    "color": {
        "gray": ramp("--gray-"),
        "primary": color(primary, f"{S}: --primary was {primary_raw}"),
        "primaryLight": color(primary_light, f"{S}: --primary-light was {primary_light_raw}"),
        "primaryDark": color(primary_dark, f"{S}: --primary-dark was {primary_dark_raw}"),
        "backgroundLight": color(bg_light, f"{S}: --background-light was {bg_light_raw}"),
        "backgroundDark": color(bg_dark, f"{S}: --background-dark was {bg_dark_raw}"),
        "tooltipForeground": color(tooltip, f"{S}: --tooltip-foreground was {tooltip_raw}"),
        "white": color("#ffffff", f"{S}: --color-white"),
        "black": color("#000000", f"{S}: --color-black"),
        "shutdown": {
            "ink": color("#221f1c", f"{G}: body color"),
            "muted": color("#5d5751", f"{G}: .message color"),
            "page": color("#f7f5f1", f"{G}: :root background"),
            "surface": color("#ffffff", f"{G}: link background"),
            "border": color("#d7d1ca", f"{G}: link border"),
            "borderHover": color("#a9a199", f"{G}: link:hover border"),
            "focus": color("#ef6a3a", f"{G}: link:focus-visible outline"),
        },
        "callout": {
            "lightFill": color("#fefce8", f"{M}, light: shutdown callout background"),
            "lightBorder": color("#fef08a", f"{M}, light: shutdown callout border"),
            "darkBorder": color("#713f12", f"{M}, dark: shutdown callout border"),
        },
    },
    "font": {
        "family": {
            "sans": font(
                'Inter, -apple-system, "system-ui", "Segoe UI", system-ui, sans-serif',
                f"{M}: computed font-family on body",
            ),
            "mono": font(
                'Paper Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
                f"{S}: --font-paper-mono",
            ),
        },
        "weight": {
            "normal": num(400, f"{S}: --font-weight-normal"),
            "medium": num(500, f"{S}: --font-weight-medium"),
            "semibold": num(600, f"{S}: --font-weight-semibold"),
            "bold": num(700, f"{S}: --font-weight-bold"),
        },
        "size": {
            "sm": dim("0.875rem", f"{S}: --text-sm"),
            "base": dim("1rem", f"{S}: --text-base"),
            "lg": dim("1.125rem", f"{S}: --text-lg"),
            "xl": dim("1.25rem", f"{S}: --text-xl"),
            "2xl": dim("1.5rem", f"{S}: --text-2xl"),
            "3xl": dim("1.875rem", f"{S}: --text-3xl"),
            "4xl": dim("2.25rem", f"{S}: --text-4xl"),
        },
        "tracking": {
            "tight": num(-0.025, f"{S}: --tracking-tight", "number"),
        },
    },
    "space": {
        "1": dim("0.25rem", f"{S}: --spacing"),
        "searchPadX": dim("14px", f"{M}: search button padding-left"),
        "navPad": dim("6px", f"{M}: active sidebar link padding-block"),
        "accordionPadY": dim("14px", f"{M}: FAQ summary padding-block"),
        "calloutPad": dim("16px", f"{M}: callout padding-block"),
        "shutdownPad": dim("13px", f"{G}: link padding-block"),
    },
    "radius": {
        "md": dim("8px", f"{M}: theme button border-radius"),
        "lg": dim("12px", f"{S}: --radius-xl resolves to .75rem; search, nav active, and the Go to Mocha face use 12px"),
        "xl": dim("16px", f"{M}: callout border-radius"),
        "dialog": dim("20px", f"{M}: search dialog border-radius"),
        "pill": dim("999px", f"{G}: shutdown link border-radius"),
    },
    "layout": {
        "topbar": dim("64px", f"{M}: [data-layout-item=topbar] height"),
        "sidebar": dim("288px", f"{M}: [data-layout-item=sidebar] width at 1440"),
        "search": dim("36px", f"{M}: search button height"),
        "control": dim("36px", f"{M}: Go to Mocha face height"),
        "desktop": dim("1440px", "Capture viewport width"),
        "phone": dim("390px", "Phone capture viewport width"),
    },
}

def semantic(theme):
    if theme == "light":
        page = "{color.backgroundLight}"
        text = "{color.gray.900}"
        muted = "{color.gray.600}"
        accent = "{color.primary}"
        border = "{color.gray.100}"
        surface = "{color.backgroundLight}"
        focus = "{color.primary}"
        active_bg = "oklab(0.364975 0.0100353 0.0705809 / 0.1)"
        callout_bg = "{color.callout.lightFill}"
        callout_border = "{color.callout.lightBorder}"
        button_bg = "{color.primaryDark}"
        button_fg = "{color.white}"
    else:
        page = "{color.backgroundDark}"
        text = "{color.gray.200}"
        muted = "{color.gray.400}"
        accent = "{color.primaryLight}"
        border = "{color.gray.800}"
        surface = "{color.backgroundDark}"
        focus = "{color.primaryLight}"
        active_bg = "oklab(0.921162 -0.129713 0.145731 / 0.1)"
        callout_bg = "oklab(0.68064 0.0348215 0.137956 / 0.2)"
        callout_border = "{color.callout.darkBorder}"
        button_bg = "{color.white}"
        button_fg = "{color.black}"
    return {
        "page": color(page, f"{S}: --background-{'light' if theme=='light' else 'dark'}"),
        "surface": color(surface, f"{M}, {theme}: page and search share the page colour"),
        "text": color(text, f"{M}, {theme}: h1 color"),
        "muted": color(muted, f"{M}, {theme}: body and sidebar color"),
        "accent": color(accent, f"{S}: --primary{'' if theme=='light' else '-light'}"),
        "border": color(border, f"{M}, {theme}: computed border-top-color on body"),
        "focus": color(focus, f"{M}, {theme}: Go to Mocha focus outline"),
        "button": {
            "background": color(button_bg, f"{M}, {theme}: Go to Mocha face (span.bg-primary-{'dark' if theme=='light' else 'light'})"),
            "text": color(button_fg, f"{M}, {theme}: label over the Go to Mocha face"),
        },
        "nav": {
            "activeBackground": color(active_bg, f"{M}, {theme}: current sidebar link background"),
            "activeText": color(accent, f"{M}, {theme}: current sidebar link color"),
        },
        "callout": {
            "background": color(callout_bg, f"{M}, {theme}: shutdown callout background"),
            "border": color(callout_border, f"{M}, {theme}: shutdown callout border"),
        },
    }


tokens = {
    "core": core,
    "light": semantic("light"),
    "dark": semantic("dark"),
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# Motion, when the probe has run. motion.build returns (group, notTokenised): the group is the
# token tree, and what DTCG cannot carry is kept beside core, as the kit does.
if (RAW / "motion.json").exists():
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    tokens["core"]["motion"], motion_not_core = motion.build(json.loads((RAW / "motion.json").read_text()))
    if motion_not_core:
        tokens["core"].setdefault("$extensions", {}).setdefault("notTokenised", []).extend(motion_not_core)

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print(f"wrote {HERE / 'tokens.json'}")
