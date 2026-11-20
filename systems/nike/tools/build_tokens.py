#!/usr/bin/env python3
"""Build tokens.json from Nike SG's measured PDS and Podium custom properties.

Source: raw/css-vars.json, harvested as computed custom properties on
documentElement at https://www.nike.com/sg/ on 2026-11-19, signed out.
One light theme. Component colours that differ from the declared tokens
are recorded in raw/components-computed.json and are not invented here.

Deterministic. Edit the raw input, never tokens.json.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
PDS = RAW["pds"]
POD = RAW["podium"]
SRC = "computed css-var on documentElement, www.nike.com/sg 2026-11-19"


def color(value, name):
    return {
        "$type": "color",
        "$value": value.lower(),
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def dim(value, name):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def duration(value, name):
    return {
        "$type": "duration",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def easing(value, name):
    nums = [float(x) for x in value.replace("cubic-bezier(", "").rstrip(")").split(",")]
    return {
        "$type": "cubicBezier",
        "$value": nums,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def shadow(value, name):
    return {
        "$type": "shadow",
        "$value": value,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def font(stack, name):
    return {
        "$type": "fontFamily",
        "$value": stack,
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def typography(size, weight, line, family, name):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def build():
    """The token document, built in memory from raw/css-vars.json; main() writes it."""
    c = PDS["color"]
    core = {
        "font": {
            "family": {
                "text": font(
                    ["Helvetica Now Text", "Helvetica", "Arial", "sans-serif"],
                    "--pds-typography-body-1",
                ),
                "text-medium": font(
                    ["Helvetica Now Text Medium", "Helvetica", "Arial", "sans-serif"],
                    "computed font on header utility links and Add to Bag",
                ),
                "display": font(
                    ["Helvetica Now Display Medium", "Helvetica", "Arial", "sans-serif"],
                    "computed font on home h1 and PDP title",
                ),
                "display-bold": font(
                    ["Helvetica Now Display Bold", "Helvetica", "Arial", "sans-serif"],
                    "--pds-typography-title-3",
                ),
                "futura": font(
                    ["Nike Futura ND", "Helvetica Now Text Medium", "Helvetica", "Arial", "sans-serif"],
                    "--pds-typography-brand-display-5",
                ),
            }
        },
        "typography": {
            "body-1": typography("16px", 400, "24px", "{core.font.family.text}", "--pds-typography-body-1 (400 1rem/1.5)"),
            "body-2": typography("14px", 400, "21px", "{core.font.family.text}", "--pds-typography-body-2 (400 .875rem/1.5)"),
            "body-3": typography("12px", 400, "18px", "{core.font.family.text}", "--pds-typography-body-3 (400 .75rem/1.5)"),
            "title-3": typography("24px", 500, "28.8px", "{core.font.family.display-bold}", "--pds-typography-title-3 (500 1.5rem/1.2); home h1 computed 24px/28.8px weight 500 in Helvetica Now Display Medium"),
            "title-4": typography("20px", 500, "24px", "{core.font.family.display}", "--pds-typography-title-4 declared 1.25rem; PDP h1 computed 20px/24px weight 500"),
            "button": typography("16px", 500, "24px", "{core.font.family.text-medium}", "computed on Add to Bag and Shop pills"),
        },
        "radius": {k: dim(v, f"--pds-radius-{k}") for k, v in PDS["radius"].items()},
        "space": {k: dim(v, f"--pds-space-{k}") for k, v in PDS["space"].items()},
        "border-width": {
            "s": dim(POD["size-border-width-s"], "--podium-cds-size-border-width-s"),
            "m": dim(POD["size-border-width-m"], "--podium-cds-size-border-width-m"),
            "button": dim(POD["button-border-width"], "--podium-cds-button-border-width"),
        },
        "control": {
            "button-radius": dim(POD["button-border-radius"], "--podium-cds-button-border-radius"),
            "button-height-s": dim(POD["button-height-s"], "--podium-cds-button-height-s"),
            "button-height-m": dim(POD["button-height-m"], "--podium-cds-button-height-m"),
            "button-height-l": dim(POD["button-height-l"], "--podium-cds-button-height-l"),
            "button-pad-top-l": dim(POD["button-padding-top-l"], "--podium-cds-button-padding-top-l"),
            "button-pad-sides-l": dim(POD["button-padding-sides-l"], "--podium-cds-button-padding-sides-l"),
            "header-height": dim("60px", "computed header height, home desktop and 390"),
            "search-height": dim("36px", "computed search field height"),
            "add-height": dim("60px", "computed Add to Bag height"),
        },
        "motion": {
            "duration-150": duration(PDS["motion"]["duration-150"], "--pds-motion-duration-150"),
            "duration-250": duration(PDS["motion"]["duration-250"], "--pds-motion-duration-250"),
            "duration-300": duration(PDS["motion"]["duration-300"], "--pds-motion-duration-300"),
            "duration-350": duration(PDS["motion"]["duration-350"], "--pds-motion-duration-350"),
            "duration-400": duration(PDS["motion"]["duration-400"], "--pds-motion-duration-400"),
            "easing-expressive": easing(PDS["motion"]["easing-expressive"], "--pds-motion-easing-expressive"),
            "easing-functional": easing(PDS["motion"]["easing-functional"], "--pds-motion-easing-functional"),
        },
        "shadow": {
            "primary": shadow(PDS["shadow-primary"], "--pds-shadow-primary"),
        },
    }
    light = {
        "page": color(c["background-primary"], "--pds-color-background-primary"),
        "surface": color(c["background-secondary"], "--pds-color-background-secondary"),
        "text": color(c["text-primary"], "--pds-color-text-primary"),
        "muted": color(c["text-secondary"], "--pds-color-text-secondary"),
        "accent": color(c["element-primary"], "--pds-color-element-primary; also --podium-cds-button-color-bg-primary"),
        "on-accent": color(c["text-primary-inverse"], "--pds-color-text-primary-inverse"),
        "border": color(c["border-secondary"], "--pds-color-border-secondary"),
        "border-strong": color(c["border-primary"], "--pds-color-border-primary"),
        "link": color(c["text-link"], "--pds-color-text-link"),
        "focus": color(POD["color-focus-ring"], "--podium-cds-color-focus-ring; also --pds-color-border-focused"),
        "critical": color(c["text-critical"], "--pds-color-text-critical"),
        "success": color(c["text-success"], "--pds-color-text-success"),
        "warning": color(c["element-warning"], "--pds-color-element-warning"),
        "badge": color(c["text-badge"], "--pds-color-text-badge; computed Just In label"),
        "orange": color(c["element-brand-orange"], "--pds-color-element-brand-orange"),
        "disabled-fill": color(c["element-disabled"], "--pds-color-element-disabled; computed disabled size chip"),
        "disabled-text": color(c["text-disabled"], "--pds-color-text-disabled"),
        "hover": color(POD["button-color-bg-primary-hover"], "--podium-cds-button-color-bg-primary-hover; computed Add to Bag hover"),
        "scrim": color("#1111115c", "--pds-color-background-scrim"),
        "inverse": color(c["background-primary-inverse"], "--pds-color-background-primary-inverse"),
        "component": {
            "button-primary": {
                "background": color(POD["button-color-bg-primary"], "--podium-cds-button-color-bg-primary; computed Add to Bag"),
                "text": color("#FFFFFF", "computed Add to Bag color"),
                "radius": dim(POD["button-border-radius"], "--podium-cds-button-border-radius; computed Add to Bag"),
                "height": dim("60px", "computed Add to Bag height"),
                "padding": dim("18px", "computed Add to Bag padding-top; sides 24px"),
            },
            "button-on-image": {
                "background": color("#FFFFFF", "computed Shop pill on the home hero"),
                "text": color("#111111", "computed Shop pill color"),
                "radius": dim("30px", "computed Shop pill radius"),
                "height": dim("36px", "computed Shop pill height"),
            },
            "search": {
                "background": color("#F5F5F5", "computed search input background"),
                "radius": dim("24px", "computed search radius; matches --pds-radius-24"),
                "height": dim("36px", "computed search height"),
            },
            "size": {
                "radius": dim("4px", "computed size chip radius"),
                "border": color("#CACACB", "computed size chip border"),
                "height": dim("48px", "computed size chip height"),
            },
        },
    }
    doc = {
        "$description": "Nike Singapore public storefront (www.nike.com/sg), captured 2026-11-19 signed out. PDS and Podium CDS custom properties, one light theme. nike.com redirects to /sg/.",
        "core": core,
        "light": light,
        "$themes": [
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
            }
        ],
    }
    return doc


def main():
    (HERE / "tokens.json").write_text(json.dumps(build(), indent=2) + "\n")
    print("wrote", HERE / "tokens.json")


if __name__ == "__main__":
    main()
