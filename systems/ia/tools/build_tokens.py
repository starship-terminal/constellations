#!/usr/bin/env python3
"""Build tokens.json for the public iA Writer site.

Sources:
  raw/css-vars.json            custom properties resolved on :root of
                               https://ia.net/writer (tools/capture/vars.mjs)
  raw/components-computed.json computed styles of the header, links and
                               download pill (tools/capture/public/measure.mjs)

The marketing pages paint one light theme. A night palette is declared in
the same sheet (--night-*) and is kept as a dark set, labelled as declared
but not applied on the captured pages. No theme switch was found.

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V["resolved"]["light"]


def css(name, note, evidence="Measured"):
    value = R.get(name, "").strip()
    if not value:
        raise SystemExit(f"missing {name}")
    kind = "color" if value.startswith(("#", "rgb", "hsl", "oklch", "color(")) else "other"
    if value.endswith("px") or value.endswith("rem"):
        kind = "dimension"
    return {
        "$value": value,
        "$type": kind,
        "$description": note,
        "$extensions": {"source": {
            "evidence": evidence,
            "capture": f"custom property {name} resolved on :root of https://ia.net/writer (raw/css-vars.json)",
        }},
    }


def color(name, note, evidence="Measured"):
    token = css(name, note, evidence)
    token["$type"] = "color"
    return token


tokens = {
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    "core": {
        "font": {
            "family": {
                "sans": css("--font-sans", "Day sans stack used on the light marketing pages."),
                "sansInverse": css("--font-sans-inverse", "Night sans stack, used on the blue download pill."),
                "serif": css("--font-serif", "Day serif stack."),
                "serifHeadline": css("--font-serif-headline", "Day headline serif."),
            },
        },
        "rounded": {
            "card": css("--radius-card", "Card corner."),
            "pill": css("--radius-pill", "Download pill corner."),
            "small": css("--radius-small", "Small corner."),
        },
        "space": {
            "line": css("--space-line", "Line spacing step. A clamp expression, resolved by the browser."),
            "paragraph": css("--space-paragraph", "Paragraph spacing step."),
            "section": css("--space-section", "Section spacing step."),
        },
        "layout": {
            "pageWidth": css("--page-width", "Content width."),
            "pageMargin": css("--page-margin", "Page margin. A clamp expression."),
        },
        "shadow": {
            "button": css("--shadow-button", "Button shadow."),
            "card": css("--shadow-card", "Card shadow."),
            "raised": css("--shadow-raised", "Raised panel shadow."),
        },
    },
    "light": {
        "page": color("--page", "Page ground. Matches theme-color and body background."),
        "surface": color("--surface", "Raised surface."),
        "card": color("--card", "Card fill."),
        "text": color("--ink", "Primary ink."),
        "muted": color("--ink-muted", "Muted ink."),
        "accent": color("--blue", "Brand blue. The download pill paints this."),
        "onAccent": color("--on-dark", "Ink on the blue pill."),
        "border": color("--hairline", "Hairline."),
        "field": color("--field", "Field fill."),
        "fieldBorder": color("--field-border", "Field border."),
        "success": color("--success", "Success."),
        "error": color("--error", "Error."),
        "warning": color("--day-alert-warning", "Warning. An oklch() declaration."),
        "editor": color("--editor", "Editor well."),
        "surfaceSunken": color("--surface-sunken", "Sunken surface."),
    },
    "dark": {
        "page": color("--night-page", "Declared night page. Not applied on the captured pages.", "Derived"),
        "surface": color("--night-surface", "Declared night surface. Not applied.", "Derived"),
        "card": color("--night-card", "Declared night card. Not applied.", "Derived"),
        "text": color("--night-ink", "Declared night ink. Not applied.", "Derived"),
        "accent": color("--night-blue", "Declared night blue. Same hex as the day blue.", "Derived"),
        "success": color("--night-success", "Declared night success. Not applied.", "Derived"),
        "error": color("--night-error", "Declared night error. Not applied.", "Derived"),
        "cardEdge": color("--night-card-edge", "Declared night card edge. Not applied.", "Derived"),
    },
}

# Record the measured pill so the component reading is not only a variable.
comp = json.loads((RAW / "components-computed.json").read_text())["components"]
pill = comp["download-mac"]["states"]["default"]["style"]
tokens["core"]["size"] = {
    "downloadPillHeight": {
        "$value": pill["height"],
        "$type": "dimension",
        "$description": "Download for Mac pill height on /writer at 1440.",
        "$extensions": {"source": {
            "evidence": "Measured",
            "capture": "computed height on download-mac/default (raw/components-computed.json)",
        }},
    },
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("tokens.json", "accent", tokens["light"]["accent"]["$value"], "page", tokens["light"]["page"]["$value"])
