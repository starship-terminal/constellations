#!/usr/bin/env python3
"""Build tokens.json from PlayStation's declared custom properties and computed controls.

Sources (captured 2026-11-21, en-sg, signed out):
  raw/css-vars.json          custom properties resolved on :root of playstation.com/en-sg
  raw/state-readings.json    computed styles of Sign In, nav, store tabs, Add to Cart
  raw/components-computed.json  viewport and body readings

The public site paints light. Dark role values are declared in the same stylesheets
(suffix -dark) and were not shown by a theme switch on the captured pages, so the
dark set is labelled as declared CSS, not a live theme capture.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["resolved"]
STATE = json.loads((RAW / "state-readings.json").read_text())


def rgb_to_hex(value):
    value = value.strip()
    trip = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", value)
    if trip:
        return "#%02x%02x%02x" % tuple(int(x) for x in trip.groups())
    m = re.fullmatch(r"rgb\(\s*(\d+)\s+(\d+)\s+(\d+)\s*/\s*1\s*\)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    m = re.fullmatch(r"rgb\(\s*(\d+)\s+(\d+)\s+(\d+)\s*/\s*([\d.]+)\s*\)", value)
    if m:
        r, g, b, a = m.groups()
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % float(a))
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", value)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgb\(\s*(\d+),\s*(\d+),\s*(\d+)\s*\)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    raise ValueError("cannot parse colour: " + value)


def color(path, css_name, description):
    raw = VARS[css_name]
    return {
        "$value": rgb_to_hex(raw),
        "$type": "color",
        "$description": description,
        "$extensions": {
            "source": {
                "evidence": "Measured",
                "file": "raw/css-vars.json",
                "property": css_name,
                "declared": raw,
            }
        },
    }


def dim(path, css_name, description):
    raw = VARS[css_name]
    if not re.fullmatch(r"-?\d+(\.\d+)?px", raw):
        raise ValueError(f"{css_name} is not a px length: {raw}")
    return {
        "$value": raw,
        "$type": "dimension",
        "$description": description,
        "$extensions": {
            "source": {
                "evidence": "Measured",
                "file": "raw/css-vars.json",
                "property": css_name,
                "declared": raw,
                "note": "Resolved on :root at desktop. The same names are also declared at smaller type steps in other breakpoints.",
            }
        },
    }


def computed_color(value, where):
    return {
        "$value": rgb_to_hex(value),
        "$type": "color",
        "$extensions": {
            "source": {
                "evidence": "Measured",
                "file": "raw/state-readings.json",
                "where": where,
                "computed": value,
            }
        },
    }


def leaf_dim(value, where, description=None):
    token = {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": where}},
    }
    if description:
        token["$description"] = description
    return token


ROLES = {
    "page": ("--color-role-page-backgrounds-primary-{theme}", "Page background."),
    "surface": ("--color-role-page-backgrounds-secondary-{theme}", "Secondary page surface."),
    "raised": ("--color-role-page-backgrounds-tertiary-{theme}", "Tertiary page surface."),
    "card": ("--color-role-backgrounds-card-{theme}", "Card fill."),
    "overlay": ("--color-role-backgrounds-overlay-card-{theme}", "Overlay card fill."),
    "scrim": ("--color-role-backgrounds-filter-{theme}", "Filter scrim."),
    "text": ("--color-role-text-primary-base-{theme}", "Primary text."),
    "muted": ("--color-role-text-secondary-{theme}", "Secondary text."),
    "disabled": ("--color-role-text-disabled-link-{theme}", "Disabled link text."),
    "onAccent": ("--color-role-text-button-{theme}", "Text on a primary button."),
    "link": ("--color-role-text-link-base-{theme}", "Link text."),
    "linkHover": ("--color-role-text-link-hover-{theme}", "Link text, hover."),
    "placeholder": ("--color-role-text-placeholder-{theme}", "Placeholder text."),
    "border": ("--color-role-borders-divider-line-base-{theme}", "Divider."),
    "borderStrong": ("--color-role-borders-primary-link-base-{theme}", "Primary link border."),
    "accent": ("--color-role-backgrounds-primary-link-base-{theme}", "Primary link fill."),
    "accentHover": ("--color-role-backgrounds-primary-link-hover-{theme}", "Primary link fill, hover."),
    "accentPressed": ("--color-role-backgrounds-primary-link-active-{theme}", "Primary link fill, active."),
    "commerce": ("--color-role-backgrounds-commerce-link-base-{theme}", "Commerce button fill."),
    "commerceHover": ("--color-role-backgrounds-commerce-link-hover-{theme}", "Commerce button fill, hover."),
    "commercePressed": ("--color-role-backgrounds-commerce-link-active-{theme}", "Commerce button fill, active."),
    "success": ("--color-role-text-success-{theme}", "Success text."),
    "warning": ("--color-role-text-warning-{theme}", "Warning text."),
    "info": ("--color-role-text-hint-{theme}", "Hint text. The stylesheet names this hint, not info."),
    "psPlus": ("--color-role-text-ps-plus-{theme}", "PlayStation Plus gold."),
    "formField": ("--color-role-backgrounds-form-field-{theme}", "Form field fill."),
    "focus": ("--color-role-backgrounds-primary-link-focus-{theme}", "Primary link focus fill."),
}

PALETTE = {
    "white": ("--color-1-light", "Colour ramp 1, light."),
    "ink": ("--color-1-dark", "Colour ramp 1, dark."),
    "blue": ("--color-10-light", "Colour ramp 10, light. Link blue."),
    "blueBright": ("--color-10-dark", "Colour ramp 10, dark."),
    "navy": ("--color-16-light", "Colour ramp 16."),
    "orange": ("--color-9-light", "Colour ramp 9, light. Commerce orange."),
    "orangeDark": ("--color-9-dark", "Colour ramp 9, dark."),
    "gold": ("--color-11-light", "Colour ramp 11. PS Plus gold."),
    "green": ("--color-12-light", "Colour ramp 12, light."),
    "red": ("--color-13-light", "Colour ramp 13, light."),
    "pink": ("--color-14-light", "Colour ramp 14, light."),
    "grey": ("--color-5-light", "Colour ramp 5, light."),
}


def theme_set(theme):
    out = {}
    for name, (pattern, desc) in ROLES.items():
        out[name] = color(name, pattern.format(theme=theme), desc)
    return out


core = {
    "$description": "Scales and the colour ramp declared on playstation.com. Semantic roles live in light and dark.",
    "color": {name: color(name, css, desc) for name, (css, desc) in PALETTE.items()},
    "font": {
        "family": {
            "sst": {
                "$value": "sst, Arial, sans-serif",
                "$type": "fontFamily",
                "$description": "SST is the marketing body face. Proprietary; not bundled.",
                "$extensions": {
                    "source": {
                        "evidence": "Measured",
                        "file": "raw/css-vars.json",
                        "property": "--dk-font",
                        "declared": VARS["--dk-font"],
                    }
                },
            },
            "condensed": {
                "$value": VARS["--dk-font-condensed"],
                "$type": "fontFamily",
                "$extensions": {"source": {"evidence": "Measured", "file": "raw/css-vars.json", "property": "--dk-font-condensed"}},
            },
        },
        "weight": {
            "light": {"$value": 300, "$type": "fontWeight", "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "h1 fontWeight 300"}}},
            "regular": {"$value": 400, "$type": "fontWeight", "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "body fontWeight 400"}}},
            "medium": {"$value": 500, "$type": "fontWeight", "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "nav and Sign In fontWeight 500"}}},
            "bold": {"$value": 700, "$type": "fontWeight", "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "Add to Cart fontWeight 700"}}},
        },
    },
    "space": {str(i): dim(str(i), f"--space-{i}", f"Space step {i}.") for i in range(1, 14)},
    "radius": {str(i): dim(str(i), f"--corner-size-{i}", f"Corner step {i}.") for i in range(0, 5)},
    "radiusPill": {
        "$value": "999px",
        "$type": "dimension",
        "$description": "Pill radius on Sign In and Add to Cart.",
        "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "Sign In and Add to Cart borderRadius"}},
    },
    "fontSize": {str(i): dim(str(i), f"--text-{i}", f"Type step {i}, desktop :root resolution.") for i in range(1, 12)},
    "size": {
        "header": leaf_dim("64px", "header rect height on home at 1440", "Shared nav height on the homepage."),
        "signIn": leaf_dim("24px", "Sign In rect height", "Sign In pill height. The control is short."),
        "commerce": leaf_dim("44px", "Shop Black Friday rect height", "Hero commerce link height."),
        "addToCart": leaf_dim("40px", "Add to Cart rect height", "Store primary button height."),
        "navLabel": leaf_dim("13px", "nav fontSize 13px", "Primary nav label size."),
    },
    "typography": {
        "display": {
            "$value": {
                "fontFamily": "{font.family.sst}",
                "fontWeight": "{font.weight.light}",
                "fontSize": "{fontSize.8}",
                "lineHeight": "48.75px",
            },
            "$type": "typography",
            "$description": "Homepage h1, light weight.",
            "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "h1 39px / 300 / 48.75px"}},
        },
        "body": {
            "$value": {
                "fontFamily": "{font.family.sst}",
                "fontWeight": "{font.weight.regular}",
                "fontSize": "{fontSize.4}",
                "lineHeight": "24px",
            },
            "$type": "typography",
            "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "body 16px and commerce line-height 24px"}},
        },
        "nav": {
            "$value": {
                "fontFamily": "{font.family.sst}",
                "fontWeight": "{font.weight.medium}",
                "fontSize": "13px",
                "lineHeight": "16px",
            },
            "$type": "typography",
            "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "nav button 13px / 500"}},
        },
        "button": {
            "$value": {
                "fontFamily": "{font.family.sst}",
                "fontWeight": "{font.weight.bold}",
                "fontSize": "{fontSize.4}",
                "lineHeight": "20px",
            },
            "$type": "typography",
            "$extensions": {"source": {"evidence": "Measured", "file": "raw/state-readings.json", "where": "Add to Cart 16px / 700"}},
        },
    },
}

# Sign In hover is computed, not a role token. Record it beside the declared accent.
light = theme_set("light")
light["signIn"] = computed_color(STATE["elements"]["signIn"]["backgroundColor"], "header Sign In background")
light["signInHover"] = computed_color(STATE["elements"]["signInHover"]["backgroundColor"], "header Sign In hover background")
light["navHover"] = computed_color(STATE["elements"]["navHover"]["color"], "primary nav hover color")
light["addToCart"] = computed_color("rgb(214, 61, 0)", "Add to Cart computed backgroundColor on the public product page")
light["addToCartHover"] = computed_color("rgb(163, 46, 0)", "Add to Cart hover computed backgroundColor")
light["textBody"] = computed_color("rgb(31, 31, 31)", "body computed color on playstation.com")
light["storeText"] = computed_color("rgb(54, 54, 54)", "store.playstation.com body color")
light["footer"] = computed_color("rgb(0, 67, 156)", "marketing footer background on ps5 page")
light["tabSelected"] = computed_color("rgb(235, 238, 240)", "store Deals tab selected background")

dark = theme_set("dark")

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Motion durations and easings: not read as a scale. Commerce hover paints a 2px box-shadow; no duration was stored.",
            "Icon sizes: icon glyphs are the product's artwork and are not kept.",
            "Dark theme was declared in CSS and not displayed by a public theme switch on the captured pages.",
            "Add to Cart focus did not paint an outline (outline 0). Focus ring for that control is Not captured.",
        ]
    },
}

out = json.dumps(tokens, indent=1, ensure_ascii=False) + "\n"
(HERE / "tokens.json").write_text(out)
print("wrote", HERE / "tokens.json")
