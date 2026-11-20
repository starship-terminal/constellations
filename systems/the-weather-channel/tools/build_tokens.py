#!/usr/bin/env python3
"""Build tokens.json from raw/vars-news.json and raw/components-computed.json.

The news page declares colour ramps as hex custom properties. Semantic roles
that the page paints (page, text, selected nav, focus ring, unit chip) are
taken from computed styles in raw/components-computed.json. A declared
variable that the light page does not paint is kept in core and not aliased
into the light set.

    python3 tools/build_tokens.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "vars-news.json").read_text())
DECL = VARS["declared"]

SRC_VARS = "raw/vars-news.json"
SRC_COMP = "raw/components-computed.json"


def tok(value, typ, desc, evidence, capture):
    return {
        "$value": value,
        "$type": typ,
        "$description": desc,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def measured_var(name, typ, desc):
    if name not in DECL:
        raise SystemExit(f"missing declared variable {name}")
    return tok(DECL[name], typ, desc, "Measured", f"{SRC_VARS} {name}")


def measured_comp(value, typ, desc):
    return tok(value, typ, desc, "Measured", SRC_COMP)


def alias(path, typ, desc):
    return tok("{" + path + "}", typ, desc, "Derived", SRC_VARS)


def main():
    core_color = {
        "black": measured_var("--color-black", "color", "Declared --color-black."),
        "white": measured_var("--color-white", "color", "Declared --color-white."),
        "ink": measured_comp("#252422", "color", "Computed rgb(37, 36, 34) on body text and the Settings label. Matches declared --color-gray-900."),
        "brand": {
            "100": measured_var("--color-brand-100", "color", "Declared brand ramp."),
            "200": measured_var("--color-brand-200", "color", "Declared brand ramp."),
            "300": measured_var("--color-brand-300", "color", "Declared brand ramp."),
            "400": measured_var("--color-brand-400", "color", "Declared brand ramp."),
            "active": measured_var("--color-brand-active", "color", "Declared --color-brand-active. Not observed as a painted control on the public news page."),
            "light": measured_var("--color-brand-light", "color", "Declared --color-brand-light. The selected sidebar item paints this blue."),
            "dark": measured_var("--color-brand-dark", "color", "Declared --color-brand-dark."),
        },
        "alert": {
            "advisory": measured_var("--color-alert-advisory", "color", "Declared alert advisory."),
            "warning": measured_var("--color-alert-warning", "color", "Declared alert warning."),
            "severe": measured_var("--color-alert-severe", "color", "Declared alert severe."),
            "special": measured_var("--color-alert-special", "color", "Declared alert special."),
        },
        "gray": {str(n): measured_var(f"--color-gray-{n}", "color", f"Declared --color-gray-{n}.") for n in range(100, 1000, 100)},
        "blue": {str(n): measured_var(f"--color-blue-{n}", "color", f"Declared --color-blue-{n}.") for n in range(100, 1000, 100)},
    }
    core = {
        "color": core_color,
        "font": {
            "family": {
                "sans": tok(
                    "Inter, \"Inter Fallback\", Arial, sans-serif",
                    "fontFamily",
                    "Computed font-family on body, heading, and nav.",
                    "Measured",
                    SRC_COMP,
                ),
                "mono": measured_var("--font-mono", "fontFamily", "Declared --font-mono. No code specimen was on the public pages."),
            },
            "weight": {
                "regular": measured_var("--font-weight-normal", "fontWeight", "Declared --font-weight-normal."),
                "medium": measured_var("--font-weight-medium", "fontWeight", "Declared --font-weight-medium. Nav and Settings use 500."),
                "semibold": measured_var("--font-weight-semibold", "fontWeight", "Declared --font-weight-semibold. Trend links use 600."),
                "bold": measured_var("--font-weight-bold", "fontWeight", "Declared --font-weight-bold. The selected unit chip uses 700."),
                "extrabold": measured_var("--font-weight-extrabold", "fontWeight", "Declared --font-weight-extrabold. The page heading uses 800."),
            },
            "size": {
                "body": measured_comp("16px", "dimension", "Computed body font-size."),
                "label": measured_comp("14px", "dimension", "Computed nav, Settings, and heading-adjacent label size."),
                "heading": measured_comp("24px", "dimension", "Computed h1 font-size on Top Stories."),
            },
        },
        "radius": {
            "sm": measured_var("--radius-sm", "dimension", "Declared --radius-sm."),
            "md": measured_var("--radius-md", "dimension", "Declared --radius-md."),
            "lg": measured_var("--radius-lg", "dimension", "Declared --radius-lg."),
            "nav": measured_comp("10px", "dimension", "Computed border-radius on a sidebar nav item."),
            "dialog": measured_comp("16px", "dimension", "Computed border-radius on the Settings dialog."),
            "pill": measured_comp("9999px", "dimension", "Computed border-radius on Settings and Sign in is a full pill (the browser reported an unbounded pixel radius)."),
        },
        "space": {
            "control-gap": measured_comp("8px", "dimension", "Computed gap on the Settings button."),
            "header": measured_comp("64px", "dimension", "Computed header height."),
            "control": measured_comp("40px", "dimension", "Computed Settings and Sign in height."),
            "nav-item": measured_comp("32px", "dimension", "Computed sidebar item height."),
        },
        "motion": {
            "duration": measured_var("--default-transition-duration", "duration", "Declared --default-transition-duration."),
            "ease-out": measured_var("--ease-out", "cubicBezier", "Declared --ease-out."),
            "ease-in-out": measured_var("--ease-in-out", "cubicBezier", "Declared --ease-in-out."),
        },
    }
    light = {
        "page": alias("color.white", "color", "Computed body background rgb(255, 255, 255)."),
        "surface": alias("color.white", "color", "Settings dialog computed to white."),
        "text": alias("color.ink", "color", "Computed text colour on the page heading and nav."),
        "text-on-accent": alias("color.white", "color", "Computed text on the selected sidebar item."),
        "muted": alias("color.gray.500", "color", "Declared gray-500. Secondary editorial text was not separately measured; this step is the declared mid gray."),
        "accent": alias("color.brand.light", "color", "Selected sidebar item computed rgb(58, 97, 204), which is --color-brand-light."),
        "border": alias("color.gray.200", "color", "Declared gray-200. Hairlines were visible; the exact computed border was not a hex read."),
        "focus": alias("color.brand.light", "color", "Settings focus ring computed as a 2px rgb(58, 97, 204) box-shadow."),
        "ink": alias("color.ink", "color", "Location pill, Sign in on the maps chrome, and the selected unit chip."),
        "component": {
            "nav-selected": {
                "background": alias("color.brand.light", "color", "Selected Top Stories item."),
                "text": alias("color.white", "color", "Selected Top Stories item."),
                "radius": alias("radius.nav", "dimension", "Sidebar item."),
                "height": alias("space.nav-item", "dimension", "Sidebar item."),
            },
            "button": {
                "height": alias("space.control", "dimension", "Settings and Sign in."),
                "radius": alias("radius.pill", "dimension", "Settings and Sign in."),
                "text": alias("color.ink", "color", "Settings label."),
            },
            "dialog": {
                "radius": alias("radius.dialog", "dimension", "Settings dialog."),
                "background": alias("color.white", "color", "Settings dialog."),
            },
        },
    }
    doc = {
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
        "$metadata": {
            "tokenSetOrder": ["core", "light"],
            "product": "The Weather Channel",
            "captured": "2026-11-21",
        },
    }
    text = json.dumps(doc, indent=2) + "\n"
    (HERE / "tokens.json").write_text(text)
    print("wrote tokens.json")


if __name__ == "__main__":
    main()
