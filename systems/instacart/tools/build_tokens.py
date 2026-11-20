#!/usr/bin/env python3
"""Build tokens.json from Instacart's IDS custom properties.

Source: raw/css-vars.json, harvested from www.instacart.com's live stylesheets.
Instacart paints one light theme. :root declares --ids-color-*, --ids-system-space-*,
--ids-system-radius-*, --ids-opacity-* and three easing functions. Typography is a
per-class --ids-typography-name, not a size scale, so type roles are measured
from computed styles recorded in this file.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = V["resolved"]["light"]


def norm_color(v):
    v = v.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", v)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    raise ValueError("not a colour: " + v)


def color(name, description):
    return {
        "$value": norm_color(DECL[name]),
        "$type": "color",
        "$description": description,
        "$extensions": {"source": f"css-var {name} (light)"},
    }


def dim(name, description):
    return {
        "$value": DECL[name].strip(),
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": f"css-var {name} (light)"},
    }


def number(name, description):
    return {
        "$value": float(DECL[name]),
        "$type": "number",
        "$description": description,
        "$extensions": {"source": f"css-var {name} (light)"},
    }


def easing(name, description):
    """The page resolves the @supports linear() spring. cubicBezier cannot hold it."""
    return {
        "$value": DECL[name].strip(),
        "$type": "other",
        "$description": description + " Resolved linear() spring. The stylesheet fallback, when linear() is unsupported, is cubic-bezier.",
        "$extensions": {"source": f"css-var {name} (light, resolved)"},
    }


def measured_color(value, source, description):
    return {
        "$value": norm_color(value),
        "$type": "color",
        "$description": description,
        "$extensions": {"source": source},
    }


def measured_dim(value, source, description):
    return {
        "$value": value,
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": source},
    }


def font_family(value, source, description):
    return {
        "$value": value,
        "$type": "fontFamily",
        "$description": description,
        "$extensions": {"source": source},
    }


def typography(family, size, weight, line_height, source, description):
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line_height,
        },
        "$type": "typography",
        "$description": description,
        "$extensions": {"source": source},
    }


# Measured from the public homepage and login card (computed styles, 1440).
# Body is the stylesheet's computed body. Header type and control sizes come
# from the live DOM crops in raw/components-computed.json when present, and
# from the same pages' computed styles recorded here when a crop missed.
BODY_FONT = '{font.family.sans}'
READINGS = {r["name"]: r for r in json.loads((RAW / "components-computed.json").read_text())["readings"]}
HAND = "Reconstruction — entered by hand at capture time, no raw reading behind it"


def reading(name, prop):
    """A computed style (or the box height) of a reading in raw/components-computed.json; raises
    when the reading is missing."""
    r = READINGS[name]
    if r.get("missing"):
        raise KeyError(f"{name}: recorded missing")
    if prop == "height":
        return f"{r['box']['height']:g}px"
    v = r["style"]["style"].get(prop)
    if not v:
        raise KeyError(f"{name}: no {prop} reading")
    return v


def read_dim(name, prop, description, note=""):
    return measured_dim(reading(name, prop), f"computed {prop} of {name} (raw/components-computed.json){note}", description)


def weight_alias(value):
    names = {"400": "regular", "500": "medium", "600": "semibold", "700": "bold"}
    return "{font.weight." + names[str(value)] + "}"

core = {
    "color": {
        "brand": {
            "primary": {
                "extra-light": color("--ids-color-brand-primary-extra-light", "Primary green wash."),
                "light": color("--ids-color-brand-primary-light", "Primary green light, also the success light."),
                "regular": color("--ids-color-brand-primary-regular", "Instacart green. Primary buttons and the wordmark."),
                "dark": color("--ids-color-brand-primary-dark", "Primary green pressed / dark."),
                "extra-dark": color("--ids-color-brand-primary-extra-dark", "Primary green extra dark."),
            },
            "secondary": {
                "light": color("--ids-color-brand-secondary-light", "Forest wash."),
                "regular": color("--ids-color-brand-secondary-regular", "Forest green. Hero band and wordmark ink."),
                "dark": color("--ids-color-brand-secondary-dark", "Forest dark."),
                "extra-dark": color("--ids-color-brand-secondary-extra-dark", "Forest extra dark."),
            },
            "tertiary": {
                "light": color("--ids-color-brand-tertiary-light", "Warm page wash behind the login card."),
                "regular": color("--ids-color-brand-tertiary-regular", "Warm cream."),
                "dark": color("--ids-color-brand-tertiary-dark", "Warm cream dark."),
            },
            "plus": {
                "extra-light": color("--ids-color-brand-plus-extra-light", "Instacart+ pink wash."),
                "light": color("--ids-color-brand-plus-light", "Instacart+ pink."),
                "regular": color("--ids-color-brand-plus-regular", "Instacart+ magenta."),
                "dark": color("--ids-color-brand-plus-dark", "Instacart+ magenta dark."),
                "extra-dark": color("--ids-color-brand-plus-extra-dark", "Instacart+ magenta extra dark."),
            },
            "max": {
                "light": color("--ids-color-brand-max-light", "Max yellow. Deal badges."),
                "dark": color("--ids-color-brand-max-dark", "Max ink, same as grayscale 80."),
            },
        },
        "grayscale": {
            "00": color("--ids-color-system-grayscale-00", "White."),
            "10": color("--ids-color-system-grayscale-10", "Near-white surface."),
            "20": color("--ids-color-system-grayscale-20", "Hairline and chip fill."),
            "30": color("--ids-color-system-grayscale-30", "Disabled and placeholder."),
            "40": color("--ids-color-system-grayscale-40", "Muted icon."),
            "50": color("--ids-color-system-grayscale-50", "Secondary text."),
            "60": color("--ids-color-system-grayscale-60", "Supporting text."),
            "70": color("--ids-color-system-grayscale-70", "Strong text."),
            "80": color("--ids-color-system-grayscale-80", "Near-black heading."),
            "90": color("--ids-color-system-grayscale-90", "Darker ink."),
            "99": color("--ids-color-system-grayscale-99", "Blackest ink."),
        },
        "feedback": {
            "alert": {
                "regular": color("--ids-color-system-feedback-alert-regular", "Alert orange."),
                "light": color("--ids-color-system-feedback-alert-light", "Alert yellow."),
            },
            "detrimental": {
                "light": color("--ids-color-system-feedback-detrimental-light", "Error wash."),
                "regular": color("--ids-color-system-feedback-detrimental-regular", "Error red."),
                "dark": color("--ids-color-system-feedback-detrimental-dark", "Error red dark."),
                "extra-dark": color("--ids-color-system-feedback-detrimental-extra-dark", "Error red extra dark."),
            },
            "success": {
                "light": color("--ids-color-system-feedback-success-light", "Success wash. Same value as primary light."),
                "regular": color("--ids-color-system-feedback-success-regular", "Success green. Same value as primary regular."),
                "dark": color("--ids-color-system-feedback-success-dark", "Success dark."),
                "extra-dark": color("--ids-color-system-feedback-success-extra-dark", "Success extra dark."),
            },
        },
    },
    "space": {
        "4": dim("--ids-system-space-4", "4px step."),
        "8": dim("--ids-system-space-8", "8px step."),
        "12": dim("--ids-system-space-12", "12px step."),
        "16": dim("--ids-system-space-16", "16px step."),
        "24": dim("--ids-system-space-24", "24px step."),
        "32": dim("--ids-system-space-32", "32px step."),
        "40": dim("--ids-system-space-40", "40px step."),
        "48": dim("--ids-system-space-48", "48px step."),
    },
    "radius": {
        "0": dim("--ids-system-radius-0", "Square."),
        "4": dim("--ids-system-radius-4", "Tight radius."),
        "8": dim("--ids-system-radius-8", "Control radius."),
        "12": dim("--ids-system-radius-12", "Card radius."),
        "24": dim("--ids-system-radius-24", "Large radius. Pills use a full radius beyond this step."),
    },
    "opacity": {
        "light": number("--ids-opacity-light", "0.08 overlay."),
        "border": number("--ids-opacity-border", "0.12 hairline."),
        "regular": number("--ids-opacity-regular", "0.16."),
        "dark": number("--ids-opacity-dark", "0.24."),
    },
    "font": {
        "family": {
            "sans": font_family(
                "Instacart Sans, Instacart Sans Fallback, Arial, sans-serif",
                "computed fontFamily of body (raw/css-vars.json body)",
                "The consumer UI face. Self-hosted variable woff2, Arial fallback.",
            ),
            "contrast": font_family(
                "Instacart Contrast, Instacart Contrast Fallback, Arial, sans-serif",
                "@font-face Instacart Contrast (raw/css-vars.json fonts)",
                "Display face declared beside Instacart Sans. Not the body default.",
            ),
        },
        "weight": {
            "regular": {"$value": int(V["body"]["fontWeight"]), "$type": "fontWeight", "$description": "Body.", "$extensions": {"source": "computed fontWeight of body (raw/css-vars.json body)"}},
            "medium": {"$value": 500, "$type": "fontWeight", "$description": "Labels and prices.", "$extensions": {"source": HAND + " (no captured element paints 500; the price line paints 600)"}},
            "semibold": {"$value": int(reading("chip-default", "fontWeight")), "$type": "fontWeight", "$description": "Chips and prices.", "$extensions": {"source": "computed fontWeight of chip-default (raw/components-computed.json); price-default matches"}},
            "bold": {"$value": 700, "$type": "fontWeight", "$description": "Headings.", "$extensions": {"source": HAND + " (no heading was measured)"}},
        },
    },
    "typography": {
        "body": typography(BODY_FONT, reading("login-card-default", "fontSize"), "{font.weight.regular}", reading("login-card-default", "lineHeight"),
                           "computed fontSize and lineHeight of login-card-default (raw/components-computed.json); body computes 16px, line-height normal", "Default body."),
        "label": typography(BODY_FONT, reading("chip-default", "fontSize"), weight_alias(reading("chip-default", "fontWeight")), reading("chip-default", "lineHeight"),
                            "computed fontSize, fontWeight and lineHeight of chip-default (raw/components-computed.json): the chip element's own style", "Chip label."),
        "button": typography(BODY_FONT, reading("button-continue-default", "fontSize"), weight_alias(reading("button-continue-default", "fontWeight")), reading("button-continue-default", "lineHeight"),
                             "computed fontSize, fontWeight and lineHeight of button-continue-default (raw/components-computed.json): the button element's own style; this capture recorded no separate text-node reading", "Primary button label."),
        "heading": typography(BODY_FONT, "32px", "{font.weight.bold}", "40px", HAND + " (homepage section titles were not measured)", "Section heading."),
        "display": typography(BODY_FONT, "48px", "{font.weight.bold}", "56px", HAND + " (the grocery-delivery hero was not measured)", "Marketing display."),
    },
    "motion": {
        "easing": {
            "smooth": easing("--smooth-easing-function", "Default press and fade."),
            "elevated": easing("--elevated-easing-function", "Overshoot for elevated motion."),
            "bounce": easing("--bounce-easing-function", "Stronger overshoot."),
        }
    },
}

light = {
    "color": {
        "page": color("--ids-color-system-grayscale-00", "Page. Marketing pages are white; login sits on tertiary light."),
        "surface": color("--ids-color-brand-tertiary-light", "Warm wash behind auth cards and some marketing bands."),
        "text": color("--ids-color-system-grayscale-80", "Primary ink. Headings and store names."),
        "muted": color("--ids-color-system-grayscale-50", "Secondary ink. Meta and placeholders."),
        "accent": color("--ids-color-brand-primary-regular", "Primary action fill."),
        "accent-ink": color("--ids-color-system-grayscale-00", "Label on the primary fill."),
        "on-accent": color("--ids-color-system-grayscale-00", "Text on primary green."),
        "border": color("--ids-color-system-grayscale-20", "Default hairline and field border."),
        "hero": color("--ids-color-brand-secondary-regular", "Homepage hero band."),
        "hero-ink": color("--ids-color-system-grayscale-00", "Text on the hero band."),
        "link": color("--ids-color-brand-primary-regular", "Inline links on marketing pages."),
        "deal": color("--ids-color-brand-max-light", "Yellow deal and highlight chips."),
        "danger": color("--ids-color-system-feedback-detrimental-regular", "Error text and fills."),
        "danger-surface": color("--ids-color-system-feedback-detrimental-light", "Error wash."),
        "success": color("--ids-color-system-feedback-success-regular", "Delivery-time green."),
        "warning": color("--ids-color-system-feedback-alert-regular", "Alert orange."),
        "focus": color("--ids-color-brand-primary-regular", "Focus ring colour observed on the email field."),
    },
    "component": {
        "button": {
            "primary": {
                "background": {"$value": "{color.accent}", "$type": "color", "$extensions": {"source": "alias of accent; measured Sign up and Continue"}},
                "text": {"$value": "{color.on-accent}", "$type": "color", "$extensions": {"source": "alias of on-accent"}},
                "radius": read_dim("button-primary-default", "borderTopLeftRadius", "Half the 40px height: a pill. The 56px Continue paints 28px, also half its height.",
                                   "; button-continue-default paints 28px on its 56px height"),
                "height": read_dim("button-primary-default", "height", "Header primary height.", "; the header Sign up"),
                "height-lg": read_dim("button-continue-default", "height", "Auth primary height.", "; the login Continue"),
                "radius-lg": read_dim("button-continue-default", "borderTopLeftRadius", "The 56px Continue's corner: half its height, a pill.", "; the login Continue"),
            },
            "secondary": {
                "background": {"$value": "{color.page}", "$type": "color", "$extensions": {"source": "alias of page"}},
                "text": {"$value": "{color.text}", "$type": "color", "$extensions": {"source": "alias of text"}},
                "border": {"$value": "{color.border}", "$type": "color", "$extensions": {"source": "alias of border"}},
            },
        },
        "search": {
            "height": read_dim("search-default", "height", "Header search height.", "; the homepage search"),
            "radius": read_dim("search-default", "borderTopLeftRadius", "Half the 56px height: a pill."),
        },
        "card": {
            "radius": {"$value": DECL["--ids-system-radius-12"].strip(), "$type": "dimension", "$description": "Card radius.",
                       "$extensions": {"source": "css-var --ids-system-radius-12 (light); the store-card and login-card readings paint 0px on the element measured, so no card reading holds it"}},
            "background": {"$value": "{color.page}", "$type": "color", "$extensions": {"source": "alias of page"}},
        },
        "chip": {
            "height": read_dim("chip-default", "height", "Filter chip height.", "; the EBT chip"),
            "radius": read_dim("chip-default", "borderTopLeftRadius", "Filter chip radius."),
        },
        "field": {
            "height": read_dim("text-field-default", "height", "Text field height.", "; the login email field"),
            "radius": read_dim("text-field-default", "borderTopLeftRadius", "Field radius.", "; matches --ids-system-radius-8"),
        },
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The only theme www.instacart.com paints. No data-theme toggle. IDS declares one light --ids-* set on :root.",
        }
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

if __name__ == "__main__":
    out = HERE / "tokens.json"
    text = json.dumps(doc, indent=2) + "\n"
    out.write_text(text)
    print("wrote", out, "bytes", len(text))
