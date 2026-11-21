#!/usr/bin/env python3
"""Build tokens.json from Sketch's measured public styles.

Sources, read from www.sketch.com on 2026-11-21:
  raw/components-computed.json  computed styles per component and state
                                (tools/capture/public/measure.mjs)
  raw/css-vars.json             custom properties. The marketing site declares
                                almost none that carry colour or type. Those
                                names are recorded under $extensions.notTokenised.
                                Colour and type tokens below are Measured from
                                computed styles, not from custom properties.

The site paints one light theme on the captured public routes. No dark set
is emitted. Unread values stay out: they are Not captured, not filled in.

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]
V = json.loads((RAW / "css-vars.json").read_text())


def style(name, state="default"):
    s = (C.get(name) or {}).get("states", {}).get(state) or {}
    if "style" not in s:
        raise KeyError(f"{name}.{state} has no computed style")
    return s["style"], s


def rgb_to_hex(v):
    v = v.strip()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", v)
    if not m:
        if re.fullmatch(r"#[0-9a-fA-F]{6}", v):
            return v.lower()
        raise ValueError("not a colour: " + v)
    r, g, b = (int(m.group(i)) for i in (1, 2, 3))
    a = m.group(4)
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d, %d, %d, %g)" % (r, g, b, float(a))


def px(v):
    m = re.fullmatch(r"(-?\d*\.?\d+)px", str(v).strip())
    if not m:
        raise ValueError("not px: " + repr(v))
    return "%gpx" % round(float(m.group(1)), 2)


def tok(value, ty, source, description=None):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def color_of(name, state, prop, label):
    st, _ = style(name, state)
    return tok(rgb_to_hex(st[prop]), "color", f"Measured computed {prop} on {label} ({name}/{state})")


def dim_of(name, state, prop, label):
    st, _ = style(name, state)
    return tok(px(st[prop]), "dimension", f"Measured computed {prop} on {label} ({name}/{state})")


page_bg, _ = style("page")
hero, _ = style("hero-title")
btn, _ = style("button-primary")
field, _ = style("newsletter-field")
email, _ = style("email-field")
link, _ = style("create-account")
card, _ = style("plan-card")
tip, _ = style("tooltip")
foot, _ = style("footer-link")
nav, nav_s = style("nav-link", "hover")

core = {
    "font": {
        "family": {
            "display": tok(
                "Reckless, serif",
                "fontFamily",
                "Measured computed fontFamily on h1.hero__title (hero-title/default)",
            ),
            "ui": tok(
                "InterVariable, Inter, system-ui, -apple-system, Helvetica Neue, Helvetica, Arial, sans-serif",
                "fontFamily",
                "Measured computed fontFamily on body (page/default). The live stack also repeats system-ui; the token keeps one.",
            ),
            "auth": tok(
                "Inter, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
                "fontFamily",
                "Measured computed fontFamily on the sign-in title (signin-title/default). The auth host does not use InterVariable.",
            ),
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "76px",
                "fontWeight": 500,
                "lineHeight": "76px",
                "letterSpacing": "-1.5px",
            },
            "$extensions": {"source": "Measured computed style on h1.hero__title (hero-title/default)"},
        },
        "docs-display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "76px",
                "fontWeight": 900,
                "lineHeight": "76px",
                "letterSpacing": "-1.5px",
            },
            "$extensions": {"source": "Measured computed style on the docs h1 (docs-title/default). Weight 900, unlike the homepage display at 500."},
        },
        "auth-title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.auth}",
                "fontSize": "32px",
                "fontWeight": 700,
                "lineHeight": "32px",
            },
            "$extensions": {"source": "Measured computed style on the sign-in h1 (signin-title/default)"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "16px",
            },
            "$extensions": {"source": "Measured computed style on body (page/default). Body line-height equals font-size on this page."},
        },
        "button": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "16px",
                "fontWeight": 600,
                "lineHeight": "24px",
            },
            "$extensions": {"source": "Measured computed style on a.button-new--primary (button-primary/default)"},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "16px",
                "fontWeight": 600,
                "lineHeight": "16px",
            },
            "$extensions": {"source": "Measured computed style on the Pricing header link (nav-link/default)"},
        },
        "footer-link": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "15px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": "Measured computed style on a footer link (footer-link/default)"},
        },
        "field": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": "Measured computed style on the newsletter email field (newsletter-field/default)"},
        },
        "auth-field": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.auth}",
                "fontSize": "14px",
                "fontWeight": 400,
                "lineHeight": "16.1px",
            },
            "$extensions": {"source": "Measured computed style on the sign-in email field (email-field/default)"},
        },
        "tooltip": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "14px",
                "fontWeight": 400,
                "lineHeight": "20px",
            },
            "$extensions": {"source": "Measured computed style on the pricing tooltip panel (tooltip/default)"},
        },
    },
    "radius": {
        "control": dim_of("button-primary", "default", "borderTopLeftRadius", "primary button"),
        "field": dim_of("newsletter-field", "default", "borderTopLeftRadius", "newsletter field"),
        "auth": dim_of("email-field", "default", "borderTopLeftRadius", "sign-in email field"),
        "card": dim_of("plan-card", "default", "borderTopLeftRadius", "plan card"),
        "promo": dim_of("promo", "default", "borderTopLeftRadius", "homepage promo card"),
        "tooltip": dim_of("tooltip", "default", "borderTopLeftRadius", "tooltip panel"),
        "pill": dim_of("billing-yearly", "default", "borderTopLeftRadius", "billing toggle option"),
    },
}

light = {
    "page": color_of("page", "default", "backgroundColor", "body"),
    "surface": color_of("promo", "default", "backgroundColor", "promo card"),
    "text": color_of("page", "default", "color", "body text"),
    "muted": color_of("footer-link", "default", "color", "footer link"),
    "accent": color_of("button-primary", "default", "backgroundColor", "primary button fill"),
    "on-accent": color_of("button-primary", "default", "color", "primary button label"),
    "border": tok(
        "rgba(0, 0, 0, 0.08)",
        "color",
        "Measured computed box-shadow ring on the phone header (m-header/default): rgba(0, 0, 0, 0.08) 0px 0px 0px 1px",
    ),
    "link": color_of("create-account", "default", "color", "Create an account link"),
    "link-hover": color_of("create-account", "hover", "color", "Create an account link hover"),
    "nav-hover": color_of("nav-link", "hover", "color", "header nav link hover"),
    "field": color_of("newsletter-field", "default", "backgroundColor", "newsletter field"),
    "field-focus": color_of("newsletter-field", "focused", "backgroundColor", "newsletter field focused"),
    "auth-field": color_of("email-field", "default", "backgroundColor", "sign-in email field"),
    "auth-field-focus": color_of("email-field", "focused", "backgroundColor", "sign-in email field focused"),
    "sso": color_of("sso-google", "default", "backgroundColor", "Continue with Google"),
    "sso-hover": color_of("sso-google", "hover", "backgroundColor", "Continue with Google hover"),
    "disabled": color_of("signin-submit", "default", "backgroundColor", "disabled Sign In button"),
    "on-disabled": color_of("signin-submit", "default", "color", "disabled Sign In label"),
    "card": color_of("plan-card", "default", "backgroundColor", "plan card"),
    "tooltip": color_of("tooltip", "default", "backgroundColor", "tooltip panel"),
    "footer": color_of("footer", "default", "backgroundColor", "footer"),
    "phone-header": color_of("m-header", "default", "backgroundColor", "phone header"),
    "menu": color_of("m-menu", "default", "backgroundColor", "phone menu drawer"),
    "component": {
        "button": {
            "height": dim_of("button-primary", "default", "height", "primary button"),
            "radius": {"$value": "{radius.control}", "$type": "dimension", "$extensions": {"source": "alias of core.radius.control"}},
            "padding-top": dim_of("button-primary", "default", "paddingTop", "primary button"),
            "padding-x": dim_of("button-primary", "default", "paddingLeft", "primary button"),
        },
        "header": {
            "height": dim_of("header", "default", "height", "desktop header"),
            "phone-height": dim_of("m-header", "default", "height", "phone header"),
        },
        "field": {
            "height": dim_of("newsletter-field", "default", "height", "newsletter field"),
            "auth-height": dim_of("email-field", "default", "height", "sign-in field"),
        },
        "card": {
            "radius": {"$value": "{radius.card}", "$type": "dimension", "$extensions": {"source": "alias of core.radius.card"}},
            "padding": dim_of("plan-card", "default", "paddingTop", "plan card"),
        },
    },
}

# Fix alias sources so they do not claim a second measurement.
light["component"]["button"]["radius"]["$extensions"]["source"] = "alias of core.radius.control, measured on button-primary/default"
light["component"]["card"]["radius"]["$extensions"]["source"] = "alias of core.radius.card, measured on plan-card/default"

not_tokenised = {
    "css-custom-properties": "www.sketch.com declares --rotationAmount and --swiper-theme-color on the homepage stylesheets. Neither is a design-system colour or type role. --swiper-theme-color resolved to #007aff and is Swiper's default, not a Sketch accent.",
    "dark-theme": "Not captured. No dark class or attribute is bound on the public pages that loaded.",
    "success-warning-danger-info": "Not captured. No status colour role was painted on the public pages measured.",
    "focus-ring": "Not captured as a distinct token. focus-visible on the header link and primary button did not change outline or box-shadow in the computed style.",
    "pressed-colour": "Not captured as a colour. CDP :active on the primary button scaled the box (157.95x47 to 153.21x45.59) and did not change the fill.",
    "spacing-scale": "Not captured. No spacing custom properties. Padding is recorded per component.",
    "motion": "Not captured as tokens. Durations were not read into a scale.",
    "elevation-scale": "Not captured as a scale. Individual box-shadows stay in the component readings.",
    "nav-menu": "Not captured. The Product disclosure did not stay visible long enough for a crop in measure.mjs. The open menu is in screenshots/home-light-nav-product.png.",
    "checkbox-radio-switch-tabs-toast-table-avatar-textarea": "Not present on the public pages measured, or not captured.",
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the public Sketch marketing site painted on 2026-11-21.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
    "$extensions": {"notTokenised": not_tokenised},
}

# Alias check
def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from walk(v, prefix + k + ".")

names = {n for n, _ in walk(core)} | {n for n, _ in walk(light)}
for n, t in walk(tokens):
    if not isinstance(t, dict) or "$value" not in t:
        continue
    for a in re.findall(r"\{([^{}]+)\}", json.dumps(t["$value"])):
        if a not in names:
            raise SystemExit(f"alias {{{a}}} from {n} missing")

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("tokens", len(names))
