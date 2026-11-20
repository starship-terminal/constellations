#!/usr/bin/env python3
"""Build tokens.json from Wealthsimple's published :root custom properties.

Source: the marketing site's stylesheet chunk 3d8dv3vht62lo.css, :root rules,
read 2026-11-21 from https://www.wealthsimple.com/build-assets/_next/static/chunks/.
Computed checks on /en-ca/pricing and /en-ca/contact are in raw/components-computed.json.

The public site ships one light scheme. Dark is a section class
(ws-content-dark-theme / data-theme-md=dark), not a site theme, so this file
has core + light only. Unread values are not invented.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SRC = (
    "Measured from :root in stylesheet chunk 3d8dv3vht62lo.css "
    "(www.wealthsimple.com, 2026-11-21). raw/css-vars.json."
)

ROOT = json.loads((RAW / "css-vars.json").read_text())["vars"]


def hex_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if not m:
        raise ValueError(v)
    h = m.group(1)
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) == 8 and h[6:] in ("ff",):
        h = h[:6]
    if len(h) == 8:
        return "rgba(%d, %d, %d, %s)" % (
            int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16),
            "%g" % round(int(h[6:8], 16) / 255, 3),
        )
    return "#" + h


def dim_from_rem(token_name):
    """A spacing token stored as Nrem, converted to px at 16px root. Derived."""
    raw = ROOT[token_name]
    m = re.fullmatch(r"([\d.]+)rem", raw.strip())
    if not m:
        raise ValueError(token_name + " " + raw)
    px = float(m.group(1)) * 16
    return ("%g" % px) + "px"


def color(name, value, source, description=""):
    t = {"$value": value, "$type": "color", "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def dimension(value, source, description=""):
    if not re.fullmatch(r"-?\d*\.?\d+(px|rem)", value):
        raise ValueError("bad dimension " + value)
    t = {"$value": value, "$type": "dimension", "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def number(value, source, description=""):
    t = {"$value": value, "$type": "number", "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def font_weight(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def cubic(value, source):
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def typography(family, size, weight, line, source, letter=None):
    v = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line,
    }
    if letter:
        v["letterSpacing"] = letter
    return {
        "$value": v,
        "$type": "typography",
        "$extensions": {"source": source},
    }


# Palette: hex literals on :root.
palette = {}
for key, raw in ROOT.items():
    if not key.startswith("--ws-color-"):
        continue
    if not re.fullmatch(r"#[0-9a-fA-F]{3,8}", raw.strip()):
        continue
    slug = key.removeprefix("--ws-color-").replace("-", "_")
    # keep hyphen groups as nested where the name has a step
    palette[key] = hex_color(raw)

def pal(css_name):
    return "{color." + css_name.removeprefix("--ws-color-").replace("-", ".") + "}"


def nest_palette():
    tree = {}
    for css_name, value in palette.items():
        parts = css_name.removeprefix("--ws-color-").split("-")
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = color(
            css_name,
            value,
            SRC + f" Declaration {css_name}: {ROOT[css_name]}.",
        )
    return tree


# Spacing scale: rem on :root, stored as rem (a legal dimension).
space = {}
for key, raw in ROOT.items():
    if not key.startswith("--ws-spacing-"):
        continue
    step = key.removeprefix("--ws-spacing-")
    space[step] = dimension(raw.strip(), SRC + f" Declaration {key}: {raw}.")

def resolved_dim(name):
    raw = ROOT[name].strip()
    if raw.startswith("var(--ws-spacing-"):
        step = raw[len("var(--ws-spacing-"):-1]
        raw = ROOT["--ws-spacing-" + step]
    if not raw[0].isdigit() and not raw.startswith("."):
        raise ValueError(name + " " + raw)
    if raw.startswith("."):
        raw = "0" + raw
    return raw

radius = {
    "small": dimension(resolved_dim("--ws-border-radius-small"), SRC + " --ws-border-radius-small aliases --ws-spacing-1 (0.25rem). Derived from that alias."),
    "normal": dimension(resolved_dim("--ws-border-radius-normal"), SRC + " --ws-border-radius-normal aliases --ws-spacing-3. Derived."),
    "large": dimension(resolved_dim("--ws-border-radius-large"), SRC + " --ws-border-radius-large aliases --ws-spacing-6. Derived."),
    "xlarge": dimension(resolved_dim("--ws-border-radius-xlarge"), SRC + " --ws-border-radius-xlarge aliases --ws-spacing-8. Derived."),
    "pill": dimension("1000px", SRC + " --ws-border-radius-pill: 1000px."),
}

border = {
    "thin": dimension(ROOT["--ws-border-width-thin"], SRC + " --ws-border-width-thin."),
    "default": dimension(ROOT["--ws-border-width-default"], SRC + " --ws-border-width-default."),
}

# Type roles from computed styles on the pricing page (raw/components-computed.json).
TYPE_SRC = (
    "Measured computed style on www.wealthsimple.com/en-ca/pricing, desktop 1440, "
    "2026-11-21. raw/components-computed.json."
)
CONTACT_SRC = (
    "Measured computed style on www.wealthsimple.com/en-ca/contact, desktop 1440, "
    "2026-11-21. raw/components-computed.json."
)

core = {
    "$description": "Wealthsimple marketing-site primitives from :root. One public light scheme.",
    "color": nest_palette(),
    "font": {
        "family": {
            "sans": font_family(
                "the-future, system-ui, Helvetica Neue, sans-serif",
                TYPE_SRC + " body and Get started fontFamily.",
            ),
            "serif": font_family(
                "tiempos, Lucida, Georgia, serif",
                CONTACT_SRC + " Contact h1 fontFamily. Preloaded as TiemposText-Regular.woff2.",
            ),
            "display": font_family(
                "wealthsimple-display-sans, the-future, sans-serif",
                "Observed @font-face family wealthsimple-display-sans in the same CSS bundle. "
                "Not assigned to a measured role on the pricing page, so the stack is the declared family plus the site sans.",
            ),
        },
    },
    "typography": {
        "display": typography("{font.family.sans}", "64px", 500, "1.1", TYPE_SRC + " h1 64px / 500 on the pricing page (the-future)."),
        "heading": typography("{font.family.sans}", "36px", 400, "1.2", TYPE_SRC + " h2 36px on the pricing page."),
        "editorial": typography("{font.family.serif}", "64px", 400, "1.15", CONTACT_SRC + " Contact h1 is tiempos 64px / 400."),
        "body": typography("{font.family.sans}", "18px", 400, "1.4", TYPE_SRC + " body 18px / 400."),
        "label": typography("{font.family.sans}", "14px", 500, "1.2", TYPE_SRC + " Get started and Log in and Trade nav, 14px / 500."),
        "caption": typography("{font.family.sans}", "14px", 400, "1.3", "Derived from the label size at weight 400. A dedicated caption role was not a separate computed reading."),
    },
    "fontWeight": {
        "regular": font_weight(400, TYPE_SRC + " body fontWeight 400. @font-face the-future 400."),
        "medium": font_weight(500, TYPE_SRC + " Get started fontWeight 500. @font-face the-future 500."),
        "bold": font_weight(700, "Observed @font-face the-future-bold weight 700 in the CSS bundle. Not measured on a live text role in this capture."),
    },
    "space": space,
    "radius": radius,
    "border": border,
    "size": {
        "header": dimension("5.75rem", SRC + " --ws-header-height: 5.75rem."),
        "inputMin": dimension("4rem", SRC + " --ws-min-input-height: 4rem."),
        "touchMin": dimension("2.75rem", SRC + " --ws-touch-min-target-area: 2.75rem."),
        "container": dimension("1264px", SRC + " --ws-container-max-width."),
        "navContainer": dimension("1440px", SRC + " --ws-nav-container-max-width."),
        "focusRing": dimension("0.25rem", SRC + " --ws-focus-ring-width."),
        "focusOffset": dimension("0.125rem", SRC + " --ws-focus-ring-offset."),
        "controlFocus": dimension("2px", SRC + " --ws-control-focus-ring-width."),
    },
    "motion": {
        "duration": duration("350ms", SRC + " --ws-transition-duration: .35s, converted to ms."),
        "easing": cubic([0.241, 0.969, 0.635, 0.997], SRC + " --ws-transition-easing1."),
    },
    "elevation": {
        "floating": {
            "$value": "0 1px 4px 0 rgba(16, 24, 40, 0.102), 0 1px 2px 0 rgba(16, 24, 40, 0.059)",
            "$type": "shadow",
            "$extensions": {"source": SRC + " --ws-shadow-floating: 0 1px 4px 0 #1018281a, 0 1px 2px 0 #1018280f."},
        },
    },
    "layout": {
        "zHeader": number(20, SRC + " --ws-z-index-header."),
        "zPopup": number(25, SRC + " --ws-z-index-popup."),
        "zCookie": number(21, SRC + " --ws-z-index-cookie-banner."),
    },
}

# Semantic light roles. Aliases point at core.color.*
def alias_color(token_path, source, description=""):
    return color(token_path, "{" + token_path + "}", source, description)


light = {
    "$description": "Semantic roles for the public light scheme. Dark sections restyle these names locally; there is no site-wide dark theme.",
    "background": {
        "page": color("color.greyscale.99", "{color.greyscale.99}", SRC + " --ws-color-background aliases --ws-color-greyscale-99. Computed body background on /en-ca/pricing is rgb(252, 252, 252)."),
        "surface": color("color.greyscale.100", "{color.greyscale.100}", SRC + " --ws-color-white / greyscale-100. Header and menu panel."),
        "linen": color("color.linen", "{color.linen}", SRC + " --ws-color-background-linen."),
        "linenLight": color("color.linen.light", "{color.linen.light}", SRC + " --ws-color-background-linen-light."),
        "midnight": color("color.midnight", "{color.midnight}", SRC + " --ws-color-background-midnight. Used on dark hero sections, not as the page theme."),
        "error": color("error.background", "#f2dedb", "Measured in the light theme block of the CSS bundle as --ws-color-background-error: #f2dedb (5 declarations in the light selector group). The dark-section override is #a13422 and is not the page theme."),
    },
    "text": {
        "primary": color("color.slate.10", "{color.slate.10}", TYPE_SRC + " body color rgb(28, 27, 27), which is --ws-color-slate-10."),
        "secondary": color("text.secondary", "#959595", "Declared --ws-color-text-secondary: #959595 in the light semantic block of the CSS bundle."),
        "muted": color("color.slate.40", "{color.slate.40}", SRC + " --ws-color-slate-40 #686664, used as a muted slate step. Secondary text on the light block is the separate #959595 token."),
        "onAccent": color("color.greyscale.99", "{color.greyscale.99}", TYPE_SRC + " Get started color rgb(252, 252, 252)."),
        "placeholder": color("text.placeholder", "#959595", "Declared --ws-color-text-placeholder: #959595 in the light semantic block."),
        "disabled": color("text.disabled", "#94908d", "Not captured as a computed disabled control. The CSS uses --ws-color-slate-60 (#94908d) and --ws-input-disabled-opacity: .6. This token records the slate-60 hex from :root, labelled as the disabled ink candidate, not a measured disabled state."),
        "error": color("color.terracotta.40", "{color.terracotta.40}", SRC + " --ws-color-terracotta-40 is the only error-adjacent hue on :root. A live error string was not produced (forms were not submitted)."),
        "link": color("color.slate.10", "{color.slate.10}", TYPE_SRC + " footer link color rgb(28, 27, 27). Links are ink, not a separate accent hue."),
    },
    "border": {
        "default": color("color.slate.90", "{color.slate.90}", CONTACT_SRC + " search field border rgb(228, 226, 225), which is --ws-color-slate-90."),
        "strong": color("color.slate.10", "{color.slate.10}", SRC + " --ws-color-slate-10, the ink used for strong outlines on light surfaces."),
        "focus": color("color.slate.10", "{color.slate.10}", SRC + " --ws-color-focus-ring-primary resolves toward slate-10 on light. Focus ring width is core.size.focusRing."),
    },
    "accent": {
        "default": color("color.slate.10", "{color.slate.10}", TYPE_SRC + " Get started background is the ink slate-10 (rgb(28, 27, 27)) before hover mixes it."),
        "hover": color("accent.hover", "#1c1b1b", TYPE_SRC + " Hover background computed as oklab mix of the ink at about 0.81 alpha. The underlying token is --ws-color-hover-button-solid: color-mix(in srgb, var(--ws-color-slate-10) 80%, transparent). Stored as the slate-10 hex because DTCG colour here is the ink, and the mix is named in the source."),
        "pressed": color("accent.pressed", "#1c1b1b", "Pressed state was not held as a distinct colour. The space-key attempt matched the focus reading (ink at 0.8 alpha). Not captured as a separate step."),
    },
    "status": {
        "success": color("color.celery.40", "{color.celery.40}", SRC + " --ws-color-celery-40 on :root. No success toast was shown on the public pages."),
        "warning": color("color.apricot.60", "{color.apricot.60}", SRC + " --ws-color-apricot-60 on :root. No warning state was shown."),
        "danger": color("color.terracotta.40", "{color.terracotta.40}", SRC + " --ws-color-terracotta-40 on :root. No submitted error was shown."),
        "info": color("color.sky.50", "{color.sky.50}", SRC + " --ws-color-sky-50 on :root. No info toast was shown."),
    },
    "focus": {
        "ring": color("color.slate.10", "{color.slate.10}", SRC + " --ws-focus-ring-width 0.25rem and --ws-color-focus-ring-primary. The Get started focus reading painted outline none; the ring is a separate pseudo element that this capture did not measure as a colour change on the element itself."),
    },
}

# Fix alias paths: color() helper stored the path in the value only when it starts with { 
# The calls above pass "{color.greyscale.99}" as value via the second arg when I used color(name, "{...}").
# Wait, color(name, value, source) — first arg is unused except I passed token path as name incorrectly.
# Looking at color(): first arg `name` is unused. Value is the second arg. Good if I passed the alias as second.
# I passed color("color.greyscale.99", "{color.greyscale.99}", ...) so value is the alias. Good.

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The public marketing site's scheme. Dark sections use ws-content-dark-theme locally. No site-wide dark theme was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# Validate aliases and dimensions.
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v, f"{path}.{k}" if path else k)

def resolve_alias(ref, seen=()):
    if ref in seen:
        raise KeyError("cycle " + ref)
    parts = ref.split(".")
    # search light then core
    for root_name, root in (("light", light), ("core", core)):
        node = root
        ok = True
        for p in parts:
            if isinstance(node, dict) and p in node and not p.startswith("$"):
                node = node[p]
            else:
                ok = False
                break
        if ok and isinstance(node, dict) and "$value" in node:
            val = node["$value"]
            if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
                return resolve_alias(val[1:-1], seen + (ref,))
            return val
    raise KeyError("alias missing: " + ref)

errors = []
for path, node in walk(tokens):
    if "source" not in node.get("$extensions", {}):
        errors.append(path + " missing source")
    val = node["$value"]
    ty = node["$type"]
    if isinstance(val, str) and val.startswith("{") and val.endswith("}") and "." in val and not val.startswith("{font"):
        try:
            resolve_alias(val[1:-1])
        except KeyError as e:
            errors.append(f"{path}: {e}")
    if ty == "dimension" and isinstance(val, str) and not val.startswith("{") and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", val):
        errors.append(f"{path}: bad dimension {val}")
    if ty == "color" and isinstance(val, str) and not val.startswith("{") and not re.fullmatch(r"#[0-9a-f]{6}|rgba\([^)]+\)", val):
        errors.append(f"{path}: bad color {val}")

if errors:
    print("ERRORS")
    for e in errors:
        print(" ", e)
    sys.exit(1)

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")
n = sum(1 for _ in walk(tokens))
print(f"tokens.json: {n} tokens")
