#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Read from teenage.engineering on 2026-11-21, public, signed out, 1440x900.
The site declares a palette and a type scale as custom properties on :root
(root.CjpT3LAa.css). The home page overrides --theme-body-bc to black in an
inline style; the store and newsletter pages use the declared white body.
One theme. Every token carries $extensions.source. A value that was not read
is absent, never guessed.

Deterministic: same inputs, byte-identical output. Edit the raw files, never tokens.json.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())
RES = V["resolved"]["light"]

# Declared :root values from the same-origin stylesheet, not the home-page inline override.
DECLARED = {}
for rule in V["theme"]:
    if rule.get("selector") == ":root" and not rule.get("context") and rule.get("file", "").startswith("root."):
        DECLARED.update(rule["properties"])
    if rule.get("file", "").startswith("form.") and rule.get("selector") == ":root":
        DECLARED.update(rule["properties"])


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            return "#%02x%02x%02x" % rgb if a >= 1 else "rgba(%d, %d, %d, %g)" % (*rgb, a)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    raise ValueError("not a colour: " + v)


def px_of(v):
    m = re.fullmatch(r"(-?\d*\.?\d+)px", str(v).strip())
    if not m:
        raise ValueError("not a px length: %r" % v)
    return ("%g" % round(float(m.group(1)), 3)) + "px"


def token(ty, value, source, description=None):
    if ty == "color" and not str(value).startswith("{"):
        value = norm_color(value)
    if ty == "dimension" and not str(value).startswith("{"):
        value = px_of(value)
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def css_color(name):
    rec = RES[name]
    if rec.get("kind") != "color":
        raise SystemExit(f"{name} did not resolve as a colour: {rec}")
    return token("color", rec["value"], f"css-var {name} resolved on :root at 1440x900 (raw/css-vars.json)")


def declared_color(name):
    raw = DECLARED[name]
    if raw.startswith("var("):
        inner = raw[raw.find("--"):].split(")")[0]
        return token("color", "{" + inner[2:].replace("-", ".") + "}", f"css-var {name} declared as {raw} in root stylesheet")
    return token("color", raw, f"css-var {name} declared {raw} in root stylesheet (raw/css-vars.json)")


def css_dim(name, note=""):
    rec = RES[name]
    if rec.get("kind") != "dimension":
        raise SystemExit(f"{name} did not resolve as a dimension: {rec}")
    src = f"css-var {name} resolved to {rec['value']} at 1440x900"
    if rec.get("note"):
        src += "; " + rec["note"]
    if note:
        src += "; " + note
    return token("dimension", rec["value"], src + " (raw/css-vars.json)")


def comp(component, state, prop):
    node = C["components"][component]["states"][state]
    if "error" in node or prop not in node:
        raise SystemExit(f"missing {component} {state} {prop}")
    return node[prop]


# Palette names keep the product's own names. Dots in the token path match the CSS name with -- stripped.
core_color = {
    "white": css_color("--white"),
    "teWhite": css_color("--te-white"),
    "teBlack": css_color("--te-black"),
    "grey100": css_color("--te-grey-100"),
    "grey200": css_color("--te-grey-200"),
    "grey300": css_color("--te-grey-300"),
    "grey500": css_color("--te-grey-500"),
    "grey600": css_color("--te-grey-600"),
    "grey700": css_color("--te-grey-700"),
    "grey900": css_color("--te-grey-900"),
    "grey1000": css_color("--te-grey-1000"),
    "blue": css_color("--te-blue"),
    "green": css_color("--te-green"),
    "orange": css_color("--te-orange"),
    "red": css_color("--te-red"),
    "yellow": css_color("--te-yellow"),
    "error": css_color("--error"),
    "paper": token("color", "#f1f2f2", "computed color of logo, nav-link and search-button on the home page (raw/components-computed.json)", "Off-white used as text on the black home and menu."),
}

# Alias success to green, matching the stylesheet declaration var(--te-green).
core_color["success"] = token("color", "{color.green}", "css-var --success declared as var(--te-green) in root stylesheet")

core = {
    "color": core_color,
    "font": {
        "family": {
            "te20": token("fontFamily", RES["--te-20"]["value"], "css-var --te-20 declared on :root (raw/css-vars.json)", "Product face. Proprietary. The guide falls back to sans-serif."),
            "te40": token("fontFamily", RES["--te-40"]["value"], "css-var --te-40 declared on :root (raw/css-vars.json)"),
        },
        "weight": {
            "thin": token("fontWeight", 100, "css-var --fw-thin declared 100; computed fontWeight of logo and nav-link"),
            "light": token("fontWeight", 300, "css-var --fw-light declared 300; computed fontWeight of subscribe, add-to-cart, fields"),
        },
        "scale": {
            "10": css_dim("--fs-10", "authored calc of client width; 13.219px at 1440"),
            "15": css_dim("--fs-15"),
            "20": css_dim("--fs-20"),
            "25": css_dim("--fs-25"),
            "30": css_dim("--fs-30"),
            "40": css_dim("--fs-40"),
            "ui": token("dimension", px_of(comp("nav-link", "default", "fontSize")), "computed fontSize of nav-link, logo, search-button, footer-link at 1440"),
        },
    },
    "space": {
        "xs": css_dim("--space-xs"),
        "sm": css_dim("--space-sm"),
        "md": css_dim("--space-md"),
        "lg": css_dim("--space-lg"),
        "xl": css_dim("--space-xl"),
    },
    "radius": {
        "none": token("dimension", "0px", "computed borderTopLeftRadius of subscribe, add-to-cart, newsletter-field, store-tile"),
        "field": css_dim("--field-border-radius", "declared calc of client width; resolved 0px at 1440"),
        "tile": css_dim("--tile-border-radius"),
        "pill": css_dim("--round", "declared 9999px"),
    },
    "border": {
        "hairline": token("dimension", "1px", "computed borderTopWidth of newsletter-field"),
        "checkbox": token("dimension", px_of(comp("newsletter-check", "default", "borderTopWidth")), "computed borderTopWidth of newsletter-check"),
    },
    "size": {
        "clickMin": css_dim("--btn-min-click-area", "declared 48px, not viewport-relative"),
        "field": token("dimension", px_of(comp("newsletter-field", "default", "height")), "computed height of newsletter email field at 1440"),
        "button": token("dimension", px_of(comp("subscribe", "default", "height")), "computed height of subscribe and add-to-cart at 1440"),
        "icon": css_dim("--icon-size"),
        "header": css_dim("--header-height"),
        "checkbox": token("dimension", px_of(comp("newsletter-check", "default", "height")), "computed height of the newsletter checkbox"),
    },
    "z": {
        "over": token("number", 100, "css-var --z-over"),
        "navigation": token("number", 1000, "css-var --z-navigation"),
        "modalBackdrop": token("number", 2000, "css-var --z-modal-backdrop"),
        "dialog": token("number", 2001, "css-var --z-dialog"),
    },
    "typography": {
        "nav": {
            "$value": {
                "fontFamily": "{font.family.te20}",
                "fontSize": "{font.scale.ui}",
                "fontWeight": "{font.weight.thin}",
                "lineHeight": "15px",
                "letterSpacing": "0px",
            },
            "$type": "typography",
            "$extensions": {"source": "computed font of nav-link default (raw/components-computed.json)"},
        },
        "body": {
            "$value": {
                "fontFamily": "{font.family.te20}",
                "fontSize": "{font.scale.ui}",
                "fontWeight": "{font.weight.light}",
                "lineHeight": "22px",
                "letterSpacing": "0px",
            },
            "$type": "typography",
            "$extensions": {"source": "computed font of footer-link and newsletter-check label size"},
        },
        "field": {
            "$value": {
                "fontFamily": "{font.family.te20}",
                "fontSize": "{font.scale.15}",
                "fontWeight": "{font.weight.light}",
                "lineHeight": "24px",
                "letterSpacing": "0px",
            },
            "$type": "typography",
            "$extensions": {"source": "computed fontSize of newsletter-field, matching --fs-15"},
        },
        "button": {
            "$value": {
                "fontFamily": "{font.family.te20}",
                "fontSize": "{font.scale.20}",
                "fontWeight": "{font.weight.light}",
                "lineHeight": "29px",
                "letterSpacing": "0px",
            },
            "$type": "typography",
            "$extensions": {"source": "computed fontSize of subscribe and add-to-cart, matching --fs-20 at 1440"},
        },
    },
}

light = {
    "background": {
        "page": token("color", "{color.white}", "css-var --theme-body-bc declared #fff on :root. Home overrides it to #000 in an inline style; store, newsletter and checkout paint the declared white."),
        "pageInverse": token("color", "#000000", "computed backgroundColor of body on https://teenage.engineering/ (raw probe, 2026-11-21). The home campaign is black."),
        "surface": token("color", "{color.teWhite}", "css-var --product-background-color declared #f5f5f5; computed backgroundColor of store-tile"),
        "field": token("color", "{color.white}", "css-var --field-background declared #fff; computed backgroundColor of newsletter-field"),
        "fieldDisabled": css_color("--field-background-disabled"),
        "inverse": token("color", "{color.teBlack}", "computed backgroundColor of subscribe and add-to-cart"),
    },
    "text": {
        "primary": token("color", "#000000", "computed color of newsletter-field and store-tile"),
        "onInverse": token("color", "{color.teWhite}", "computed color of subscribe and add-to-cart"),
        "onBlack": token("color", "{color.paper}", "computed color of logo and nav-link on the black home page"),
        "muted": css_color("--field-placeholder"),
        "disabled": css_color("--field-color-disabled"),
        "link": token("color", "#000000", "computed color of the privacy-policy link was not isolated; the newsletter body text is black. Link colour on the white pages matches primary."),
    },
    "border": {
        "default": token("color", "#000000", "computed borderTopColor of newsletter-field"),
        "muted": css_color("--field-border-color"),
        "fieldMuted": token("color", "#e5e5e5", "computed borderTopColor of newsletter-check default"),
        "focus": token("color", "#000000", "computed borderTopColor of newsletter-check focus-visible"),
        "select": token("color", "#767676", "computed borderTopColor of region-select, matching --te-grey-600"),
    },
    "action": {
        "primary": token("color", "{color.teBlack}", "computed backgroundColor of subscribe and add-to-cart"),
        "primaryText": token("color", "{color.teWhite}", "computed color of subscribe and add-to-cart"),
        "soldOut": token("color", "{color.teBlack}", "computed color of the sold-out label; the control has a transparent background"),
    },
    "status": {
        "success": token("color", "{color.success}", "css-var --success. Not observed on a painted control in this capture."),
        "error": token("color", "{color.error}", "css-var --error. Not observed on a painted control in this capture."),
        "info": token("color", "{color.blue}", "css-var --te-blue. Declared, not observed on a control."),
        "warning": token("color", "{color.yellow}", "css-var --te-yellow. Declared, not observed on a control."),
    },
    "focus": {
        "ring": token("color", "#000000", "newsletter-check and region-select change borderTopColor to #000 on focus-visible. No outline width was painted on the measured controls."),
    },
}

# Fix alias paths: color.green is core.color.green, referenced as {color.green} from core,
# and from light as {color.green} which resolves against core. token_checks looks at dotted names
# without the set prefix, so {color.green} matches core.color.green. Good.
# light.background.page uses {color.white} which is core.color.white. Good.

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "teenage.engineering paints one theme. The home page is a black campaign; store and form pages are white. There is no dark-mode toggle.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_checks import alias_errors  # noqa: E402

errors = alias_errors(core, light, {})
if errors:
    raise SystemExit("\n".join(errors))

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if isinstance(v, dict) and "$value" in v else count(v) for v in d.values() if isinstance(v, dict))


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)}")
