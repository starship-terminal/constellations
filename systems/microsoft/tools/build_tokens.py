#!/usr/bin/env python3
"""Build tokens.json from the 2026-11-21 public microsoft.com readings.

Every colour, size and family is a computed style or a resolved custom
property from that capture. Re-running this script writes the same bytes.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
CHROME = json.loads((HERE / "raw" / "chrome.json").read_text())
FIELD = json.loads((HERE / "raw" / "search-field.json").read_text())
FOCUS = json.loads((HERE / "raw" / "search-field-focus.json").read_text())
VARS = RAW["pages"]["home"]["styles"]["vars"]
SRC = "computed on https://www.microsoft.com/en-sg 2026-11-21, 1440x900, signed out"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font_family(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def typography(family, size, weight, line_height, source, tracking=None):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if tracking:
        value["letterSpacing"] = tracking
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}


def rgb(value):
    parts = value.replace("rgb(", "").replace(")", "").split(",")
    return "#" + "".join(f"{int(p.strip()):02x}" for p in parts)


def rem_px(value):
    value = value.strip()
    if value.endswith("rem"):
        px = float(value[:-3]) * 16
        return ("%g" % round(px, 3)) + "px"
    if value.endswith("px"):
        return value
    raise SystemExit(f"not a length: {value}")


h1 = RAW["pages"]["home"]["styles"]["h1"]
cta = RAW["pages"]["home"]["styles"]["cta"]
MEASURED = "Measured computed style, " + SRC
DECLARED = "Resolved custom property on :root, " + SRC

core = {
    "font": {
        "family": {
            "display": font_family(
                ["Segoe UI Variable Text", "Segoe UI", "segoeui", "Helvetica Neue", "helvetica", "arial", "sans-serif"],
                "computed font-family on h1, " + SRC,
            ),
            "text": font_family(
                ["Segoe UI Variable Text", "Segoe UI", "segoeui", "Helvetica Neue", "helvetica", "arial", "sans-serif"],
                "computed font-family on body and a Shop now, " + SRC,
            ),
            "uhf": font_family(
                ["Segoe UI", "SegoeUI", "Helvetica Neue", "Helvetica", "Arial", "sans-serif"],
                "computed font-family on header Windows link, " + SRC,
            ),
        }
    },
    "fontSize": {
        "nav": dim("13px", "computed on header Windows link, " + SRC),
        "button": dim(cta["fontSize"], "computed on a Shop now, " + SRC),
        "hero": dim(h1["fontSize"], "computed on h1, " + SRC),
        "hero-line": dim(h1["lineHeight"], "computed line-height on h1, " + SRC),
        "field": dim(FIELD["fontSize"], "computed on the Search Microsoft.com input, " + SRC),
        "body-s": dim(rem_px(VARS["--ds-body-s-font-size"]), DECLARED + " --ds-body-s-font-size"),
        "body": dim(rem_px(VARS["--ds-body-m-font-size"]), DECLARED + " --ds-body-m-font-size"),
        "body-l": dim(rem_px(VARS["--ds-body-l-font-size"]), DECLARED + " --ds-body-l-font-size"),
    },
    "spacing": {
        "3xs": dim(rem_px(VARS["--ds-spacing-3xs"]), DECLARED + " --ds-spacing-3xs"),
        "2xs": dim(rem_px(VARS["--ds-spacing-2xs"]), DECLARED + " --ds-spacing-2xs"),
        "xs": dim(rem_px(VARS["--ds-spacing-xs"]), DECLARED + " --ds-spacing-xs"),
        "s": dim(rem_px(VARS["--ds-spacing-s"]), DECLARED + " --ds-spacing-s"),
        "m": dim(rem_px(VARS["--ds-spacing-m"]), DECLARED + " --ds-spacing-m"),
        "l": dim(rem_px(VARS["--ds-spacing-l"]), DECLARED + " --ds-spacing-l"),
        "xl": dim(rem_px(VARS["--ds-spacing-xl"]), DECLARED + " --ds-spacing-xl"),
        "2xl": dim(rem_px(VARS["--ds-spacing-2xl"]), DECLARED + " --ds-spacing-2xl"),
        "3xl": dim(rem_px(VARS["--ds-spacing-3xl"]), DECLARED + " --ds-spacing-3xl"),
    },
    "radius": {
        "button": dim(cta["borderRadius"], "computed border-radius on a Shop now, " + SRC),
        "field": dim(FIELD["borderRadius"], "computed border-radius on the search input, " + SRC),
    },
}

light = {
    "background": {
        "page": color("#ffffff", "computed background-color on body, " + SRC),
        "header": color(rgb(CHROME["header"]["backgroundColor"]), "computed background-color on header, " + SRC),
        "action": color(rgb(cta["backgroundColor"]), "computed background-color on a Shop now, " + SRC),
        "action-hover": color("#006dc1", "computed background-color on a Shop now :hover, " + SRC),
        "field": color(rgb(FIELD["backgroundColor"]), "computed background-color on the search input, " + SRC),
    },
    "text": {
        "heading": color(rgb(h1["color"]), "computed color on h1, " + SRC),
        "nav": color(rgb(CHROME["link"]["color"]), "computed color on header Windows link, " + SRC),
        "on-action": color(rgb(cta["color"]), "computed color on a Shop now, " + SRC),
        "field": color(rgb(FIELD["color"]), "computed color on the search input, " + SRC),
        "declared-strong": color(VARS["--ds-theme-foreground-base-strong"], DECLARED + " --ds-theme-foreground-base-strong"),
        "declared-subtle": color(VARS["--ds-theme-foreground-base-subtle"], DECLARED + " --ds-theme-foreground-base-subtle"),
    },
    "border": {
        "field": color("#0067b8", "computed border-top-color on the search input, " + SRC),
        "focus": color("#0067b8", "computed outline-color on the focused search input, " + SRC),
        "accent": color(VARS["--ds-theme-border-accent-strong-normal"], DECLARED + " --ds-theme-border-accent-strong-normal"),
        "accent-hover": color(VARS["--ds-theme-border-accent-strong-hover"], DECLARED + " --ds-theme-border-accent-strong-hover"),
        "accent-pressed": color(VARS["--ds-theme-border-accent-strong-pressed"], DECLARED + " --ds-theme-border-accent-strong-pressed"),
        "neutral-fade": color(VARS["--ds-theme-border-neutral-fade"], DECLARED + " --ds-theme-border-neutral-fade"),
    },
    "interactive": {
        "primary": color(VARS["--ds-color-brilliant-blue-500"], DECLARED + " --ds-color-brilliant-blue-500"),
        "primary-hover": color(VARS["--ds-color-brilliant-blue-600"], DECLARED + " --ds-color-brilliant-blue-600"),
        "primary-pressed": color(VARS["--ds-color-brilliant-blue-800"], DECLARED + " --ds-color-brilliant-blue-800"),
    },
    "status": {
        "success": color(VARS["--ds-color-success-500"], DECLARED + " --ds-color-success-500"),
        "warning": color(VARS["--ds-color-warning-500"], DECLARED + " --ds-color-warning-500"),
        "danger": color(VARS["--ds-color-error-500"], DECLARED + " --ds-color-error-500"),
        "info": color(VARS["--ds-color-info-500"], DECLARED + " --ds-color-info-500"),
    },
}

tokens = {
    "$description": "Microsoft public homepage, captured 2026-11-21 signed out from https://www.microsoft.com/en-sg. One painted light theme. Shop now fill is the computed #0078d4, matching --ds-color-interactive-primary.",
    "core": core,
    "light": light,
    "$themes": [{"name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", HERE / "tokens.json")
