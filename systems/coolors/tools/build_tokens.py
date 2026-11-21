#!/usr/bin/env python3
"""Build tokens.json from the public Coolors CSSOM dump.

Reads raw/css-vars.json (resolved :root custom properties plus the
[data-theme=dark] overrides) and raw/components-computed.json (measured
public controls). Every token carries $extensions.source. Edit the raw
files, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())
RESOLVED = V["resolved"]
DARK = V["dark"]

STOPS = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]
RAMPS = [
    "primary", "slate", "gray", "zinc", "neutral", "stone",
    "red", "orange", "amber", "yellow", "lime", "green", "emerald", "teal",
    "cyan", "sky", "blue", "indigo", "violet", "purple", "fuchsia", "pink", "rose",
]


def color(name, value, source):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source},
    }


def dim(name, value, source):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }


def font_weight(value, source):
    return {
        "$type": "fontWeight",
        "$value": value,
        "$extensions": {"source": source},
    }


def font_family(value, source):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": source},
    }


def shadow(value, source):
    return {
        "$type": "shadow",
        "$value": value,
        "$extensions": {"source": source},
    }


def typography(value, source):
    return {
        "$type": "typography",
        "$value": value,
        "$extensions": {"source": source},
    }


def core_ramps():
    out = {}
    for ramp in RAMPS:
        stops = {}
        for stop in STOPS:
            key = f"--color-{ramp}-{stop}"
            if key not in RESOLVED:
                raise SystemExit(f"missing {key}")
            stops[stop] = color(
                stop,
                RESOLVED[key],
                f"css-var {key} from style.min.css?v=64 :root, public page",
            )
        out[ramp] = stops
    out["black"] = color("black", RESOLVED["--color-black"], "css-var --color-black")
    out["white"] = color("white", RESOLVED["--color-white"], "css-var --color-white")
    return out


def semantic(source_map, label):
    """Map Coolors role vars onto the catalog's light/dark role names."""
    page = source_map["--bg-color"]
    surface = source_map["--bg-color-2"]
    text = source_map["--text-color"]
    muted = source_map["--subtext-color"]
    # primary button paint is --color-primary-600 in light. Dark keeps the
    # same 500 stop via --color-smart-primary-500, which does not flip.
    accent = "{core.color.primary.600}" if label == "light" else "{core.color.primary.500}"
    return {
        "page": color("page", page, f"css-var --bg-color ({label})"),
        "surface": color("surface", surface, f"css-var --bg-color-2 ({label})"),
        "text": color("text", text, f"css-var --text-color ({label})"),
        "muted": color("muted", muted, f"css-var --subtext-color ({label})"),
        "accent": color("accent", accent, f"alias of the primary button fill ({label})"),
        "border": color("border", source_map["--border-transparent-color"], f"css-var --border-transparent-color ({label})"),
        "popover": color("popover", source_map["--popover-bg"], f"css-var --popover-bg ({label})"),
        "overlay": color("overlay", source_map["--overlay-color"], f"css-var --overlay-color ({label})"),
        "input": color("input", source_map["--input-bg"], f"css-var --input-bg ({label})"),
        "input-border": color("input-border", source_map["--input-border"], f"css-var --input-border ({label})"),
        "input-focus": color("input-focus", source_map["--input-focus-border"], f"css-var --input-focus-border ({label})"),
        "input-error": color("input-error", source_map["--input-error-border"], f"css-var --input-error-border ({label})"),
        "button-gray": color("button-gray", source_map["--button-gray-bg"], f"css-var --button-gray-bg ({label})"),
        "button-gray-text": color("button-gray-text", source_map["--button-gray-text"], f"css-var --button-gray-text ({label})"),
        "pro": color(
            "pro",
            "#ec4899" if label == "light" else "#f472b6",
            "measured Go Pro label rgb(236, 72, 153) on the public header"
            if label == "light"
            else "css-var --color-pink-400, the light pink used for accent labels when the ramp flips",
        ),
    }


def resolve_alias(value, scope):
    if isinstance(value, str) and value.startswith("var(--color-smart-"):
        name = value[len("var("):-1]  # --color-smart-neutral-50
        target = DARK.get(name) or RESOLVED.get(name)
        if not target:
            raise SystemExit(f"cannot resolve {value}")
        if target.startswith("var("):
            return resolve_alias(target, scope)
        return target
    if isinstance(value, str) and value.startswith("var(--"):
        name = value[len("var("):-1]
        if name in scope:
            return scope[name]
        if name in RESOLVED:
            return RESOLVED[name]
        raise SystemExit(f"cannot resolve {value}")
    return value


def dark_semantic():
    # Page roles are not redeclared under [data-theme=dark]. They alias
    # --color-smart-*, and that map flips the ramp. Resolve them here so the
    # dark set is paint values, not live measurements.
    light_roles = {
        "--bg-color": RESOLVED["--bg-color"],
        "--bg-color-2": RESOLVED["--bg-color-2"],
        "--text-color": RESOLVED["--text-color"],
        "--subtext-color": RESOLVED["--subtext-color"],
        "--overlay-color": RESOLVED["--overlay-color"],
    }
    # The stylesheet sets these once, to smart aliases. Dark is the flipped map.
    css = ""
    # Prefer the values already stored: light resolved map is the light paint.
    # Dark page colors come from substituting smart aliases.
    smart_light = {
        "--color-smart-neutral-50": RESOLVED["--color-neutral-50"],
        "--color-smart-neutral-100": RESOLVED["--color-neutral-100"],
        "--color-smart-neutral-600": RESOLVED["--color-neutral-600"],
        "--color-smart-neutral-950": RESOLVED["--color-neutral-950"],
        "--color-smart-primary-500": RESOLVED["--color-primary-500"],
        "--color-smart-red-500": RESOLVED["--color-red-500"],
    }
    smart_dark = {}
    for key, target in DARK.items():
        if key.startswith("--color-smart-"):
            smart_dark[key] = resolve_alias(target, RESOLVED)

    # :root assigns page roles to smart aliases. Confirmed in style.min.css:
    # --text-color: var(--color-smart-neutral-950)
    # --subtext-color: var(--color-smart-neutral-600)
    # --bg-color: var(--color-smart-neutral-50)
    # --bg-color-2: var(--color-smart-neutral-100)
    page = {
        "--bg-color": smart_dark["--color-smart-neutral-50"],
        "--bg-color-2": smart_dark["--color-smart-neutral-100"],
        "--text-color": smart_dark["--color-smart-neutral-950"],
        "--subtext-color": smart_dark["--color-smart-neutral-600"],
        "--overlay-color": DARK.get("--overlay-theme-color", RESOLVED["--overlay-color"]),
        "--border-transparent-color": DARK["--border-transparent-color"],
        "--popover-bg": smart_dark["--color-smart-neutral-100"],
        "--input-bg": DARK["--input-bg"],
        "--input-border": DARK["--input-border"],
        "--input-focus-border": smart_dark["--color-smart-primary-500"],
        "--input-error-border": smart_dark["--color-smart-red-500"],
        "--button-gray-bg": DARK["--button-gray-bg"],
        "--button-gray-text": DARK["--button-gray-text"],
    }
    # sanity: light smart map matches the resolved page colors
    if smart_light["--color-smart-neutral-950"] != RESOLVED["--text-color"] and RESOLVED["--text-color"].startswith("#"):
        # resolved text is the computed paint, which equals neutral-950
        if RESOLVED["--text-color"] != RESOLVED["--color-neutral-950"]:
            raise SystemExit("light text-color does not match neutral-950")
    del light_roles, css
    return semantic(page, "dark")


def build():
    desk = C["desktop"]
    core = {
        "color": core_ramps(),
        "font": {
            "family": {
                "ui": font_family(
                    ["Inter", "sans-serif"],
                    "getComputedStyle(document.body).fontFamily on the public homepage, 1440x900",
                ),
                "mono": font_family(
                    ["IBM Plex Mono", "ui-monospace", "monospace"],
                    "Google font link on the public page: IBM Plex Mono. Not measured on a control.",
                ),
            },
            "weight": {
                "body": font_weight(450, "body font-weight 450 on the public homepage"),
                "medium": font_weight(500, "header Sign up font-weight 500"),
                "semibold": font_weight(600, "Explore button font-weight 600. Generator hex weight was not remeasured this pass."),
                "extrabold": font_weight(800, "homepage h1 font-weight 800"),
            },
        },
        "radius": {
            "button": dim("button", "8px", "header Sign up border-radius 8px"),
            "input": dim("input", "10px", "Explore button border-radius 10px. Account text inputs were not offered this pass."),
            "hex": dim("hex", "10px", "not remeasured this pass; prior phone hex chip radius"),
            "card": dim("card", "14px", ".homepage_tool and color-of-the-day border-radius 14px"),
        },
        "space": {
            "header": dim("header", "60px", "header height 60 at 1440x900 on the public homepage"),
            "button-x": dim("button-x", "12px", "header Sign up padding 0 12px"),
            "button-h": dim("button-h", "36px", "header Sign up height 36px"),
            "hero-button-h": dim("hero-button-h", "46px", "Explore 10M+ Palettes height 46px"),
            "card": dim("card", "40px", ".homepage_tool padding 40px"),
        },
        "typography": {
            "body": typography(
                {"fontFamily": "{core.font.family.ui}", "fontSize": "15px", "fontWeight": "{core.font.weight.body}", "lineHeight": "15px"},
                "body computed style on the public homepage",
            ),
            "button": typography(
                {"fontFamily": "{core.font.family.ui}", "fontSize": "15px", "fontWeight": "{core.font.weight.medium}", "lineHeight": "36px"},
                "header Sign up computed style",
            ),
            "hero-button": typography(
                {"fontFamily": "{core.font.family.ui}", "fontSize": "16px", "fontWeight": "{core.font.weight.semibold}", "lineHeight": "46px"},
                "Explore 10M+ Palettes computed style",
            ),
            "display": typography(
                {"fontFamily": "{core.font.family.ui}", "fontSize": "110px", "fontWeight": "{core.font.weight.extrabold}", "letterSpacing": "-3.85px", "lineHeight": "99px"},
                "homepage h1 #homepage_title at 1440x900",
            ),
        },
        "shadow": {
            "header": shadow(
                [{"color": "rgba(0, 0, 0, 0.07)", "offsetX": "0px", "offsetY": "1px", "blur": "0px", "spread": "0px"}],
                "header box-shadow rgba(0, 0, 0, 0.07) 0px 1px 0px 0px",
            ),
        },
    }
    light_map = {
        "--bg-color": RESOLVED["--bg-color"],
        "--bg-color-2": RESOLVED["--bg-color-2"],
        "--text-color": RESOLVED["--text-color"],
        "--subtext-color": RESOLVED["--subtext-color"],
        "--border-transparent-color": RESOLVED["--border-transparent-color"],
        "--popover-bg": RESOLVED["--popover-bg"],
        "--overlay-color": RESOLVED["--overlay-color"],
        "--input-bg": RESOLVED["--input-bg"],
        "--input-border": RESOLVED["--input-border"],
        "--input-focus-border": RESOLVED["--input-focus-border"],
        "--input-error-border": RESOLVED["--input-error-border"],
        "--button-gray-bg": RESOLVED["--button-gray-bg"],
        "--button-gray-text": RESOLVED["--button-gray-text"],
    }
    doc = {
        "$schema": "https://schemas.design/tokens.json",
        "core": core,
        "light": semantic(light_map, "light"),
        "dark": dark_semantic(),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    # measured primary button must match the light accent alias target
    if RESOLVED["--color-primary-600"] != "#2563eb":
        raise SystemExit("primary-600 drifted")
    if desk["buttonPrimary"]["backgroundColor"] != "rgb(37, 99, 235)":
        raise SystemExit("measured primary drifted")
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {out} core ramps {len(RAMPS)}")


if __name__ == "__main__":
    build()
