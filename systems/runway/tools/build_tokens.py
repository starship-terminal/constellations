#!/usr/bin/env python3
"""Build tokens.json from Runway's public readings.

Sources, read on 2026-11-21 from runway.com, dev.runwayml.com and docs.dev.runwayml.com:
  raw/css-vars.json              custom properties harvested from live stylesheets
  raw/components-computed.json   computed styles of public controls

The marketing site is light only. The --rw-* gray ramp and level tokens are the
product's own dark-surface scale (docs and the app shell). They are recorded in
core, not as a captured dark theme. Unread values stay out.

Deterministic. Edit the raw inputs, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())
DECL = {n: v["value"] for n, v in V["resolved"]["light"].items()}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or a in ("1", "1.0", "100%"):
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


def token(path, ty, val, source, description=None):
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "dimension" and isinstance(val, (int, float)):
        val = "%gpx" % val
    if ty == "fontWeight" and isinstance(val, str) and val.isdigit():
        val = int(val)
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def css(name, ty, description=None):
    if name not in DECL:
        raise KeyError(name)
    return token(name, ty, DECL[name], f"css-var {name} (light, raw/css-vars.json)", description)


def comp(name, prop, ty, description=None):
    st = C["components"][name]["states"]["default"]
    return token(name + "." + prop, ty, st[prop], f"computed {prop} of {name} default (raw/components-computed.json)", description)


def core():
    gray = {}
    for n in range(0, 210, 10):
        name = f"--rw-gray-{n}"
        gray[str(n)] = css(name, "color", f"Declared gray step {n} (0 is white, 200 is black).")
    return {
        "color": {
            "gray": gray,
            "interactive": {
                "primary": css("--interactive-primary", "color", "Dev-site primary blue."),
                "primary-hover": css("--interactive-primary-hover", "color", "Dev-site primary hover."),
                "tertiary": css("--interactive-tertiary", "color", "Dev-site tertiary lavender."),
                "tertiary-hover": css("--interactive-tertiary-hover", "color", "Dev-site tertiary hover."),
            },
            "danger": css("--rw-danger", "color", "Declared danger."),
            "danger-dark": css("--rw-danger-dark", "color", "Declared danger, darker."),
            "ink": token("color.ink", "color", "rgb(12, 12, 12)", "computed color of nav-link default", "Marketing ink, measured on the Pricing nav link."),
            "off-black": token("color.off-black", "color", "rgb(26, 26, 26)", "computed color of nav-login default", "Near-black used on quiet buttons."),
            "cta": token("color.cta", "color", "rgb(38, 38, 38)", "computed backgroundColor of nav-cta default", "Filled CTA face."),
            "field-text": token("color.field-text", "color", "rgb(64, 64, 64)", "computed color of text-field default", "Form field text."),
            "hero-on-media": token("color.hero-on-media", "color", "rgb(255, 255, 255)", "computed color of hero-title default", "Type sitting on the hero media."),
            "menu-muted": token("color.menu-muted", "color", "rgb(100, 108, 120)", "computed color of nav-menu-trigger default", "Resting colour of a closed menu trigger."),
            "quiet": token("color.quiet", "color", "rgb(238, 241, 245)", "computed backgroundColor of nav-login default", "Quiet button fill."),
            "quiet-hover": token("color.quiet-hover", "color", "rgb(231, 234, 240)", "computed backgroundColor of nav-login hover", "Quiet button hover fill."),
            "hero-button": token("color.hero-button", "color", "rgb(247, 247, 247)", "computed backgroundColor of hero-cta default", "Hero CTA fill on the dark media."),
            "code-bg": token("color.code-bg", "color", "rgb(240, 242, 245)", "computed backgroundColor of code-block default", "Docs code block fill."),
            "code-fg": token("color.code-fg", "color", "rgb(44, 48, 55)", "computed color of code-block default", "Docs code block text."),
        },
        "font": {
            "family": {
                "sans": token("font.family.sans", "fontFamily", 'abcNormal, "abcNormal Fallback"', "computed fontFamily of nav-cta default", "Marketing face. Proprietary; the style guide falls back to system sans."),
                "docs": token("font.family.docs", "fontFamily", DECL["--rw-font"], "css-var --rw-font (light)", "Docs stack: ABC Normal, then Inter, then system."),
                "mono": token("font.family.mono", "fontFamily", DECL["--rw-font-mono"], "css-var --rw-font-mono (light)", "Mono stack. Proprietary first face."),
                "display": token("font.family.display", "fontFamily", DECL["--timesNow"], "css-var --timesNow (light)", "Declared display face. Not seen on the measured marketing controls."),
            },
            "size": {
                "hero": comp("hero-title", "fontSize", "dimension", "Desktop hero title."),
                "hero-mobile": comp("m-hero-title", "fontSize", "dimension", "Hero title at 390."),
                "price": comp("plan-price", "fontSize", "dimension", "Pricing figure."),
                "nav": comp("nav-link", "fontSize", "dimension", "Header nav link."),
                "body": comp("text-field", "fontSize", "dimension", "Form field and body."),
                "button": comp("nav-cta", "fontSize", "dimension", "Header CTA."),
                "code": comp("code-block", "fontSize", "dimension", "Docs code."),
            },
            "weight": {
                "regular": token("font.weight.regular", "fontWeight", 400, "computed fontWeight of hero-title default"),
                "medium": token("font.weight.medium", "fontWeight", 500, "computed fontWeight of nav-link default"),
                "semibold": token("font.weight.semibold", "fontWeight", 600, "computed fontWeight of nav-cta default"),
            },
        },
        "radius": {
            "sm": token("radius.sm", "dimension", "6px", "computed borderRadius of nav-cta default", "Header buttons."),
            "md": css("--rw-radius-sm", "dimension", "Declared small radius, also the hero CTA."),
            "lg": css("--rw-radius-md", "dimension", "Declared medium radius."),
            "xl": css("--rw-radius-lg", "dimension", "Declared large radius."),
            "pill": css("--rw-radius-pill", "dimension", "Declared pill. Pricing Start Free measured 9999px."),
        },
        "space": {
            "button-x": token("space.button-x", "dimension", "10px", "computed paddingLeft of nav-cta default"),
            "button-y": token("space.button-y", "dimension", "6px", "computed paddingTop of nav-cta default"),
            "field-x": token("space.field-x", "dimension", "14px", "computed paddingLeft of text-field default"),
            "field-y": token("space.field-y", "dimension", "8px", "computed paddingTop of text-field default"),
            "content": css("--landing-content-padding", "dimension", "Landing content padding."),
        },
        "size": {
            "nav-cta": token("size.nav-cta", "dimension", "32px", "computed height of nav-cta default"),
            "nav-link": token("size.nav-link", "dimension", "40px", "computed height of nav-link default"),
            "hero-cta": token("size.hero-cta", "dimension", "40px", "computed height of hero-cta default"),
            "field": token("size.field", "dimension", "41px", "computed height of text-field default"),
            "content-max": css("--landing-content-max-width", "dimension", "Landing content max width."),
            "docs-header": css("--devportal-site-header-height", "dimension", "Docs header height."),
        },
        "motion": {
            "landing": token("motion.landing", "duration", "250ms", "css-var --landing-duration (light), converted from .25s"),
            "ease": token("motion.ease", "cubicBezier", [0.2, 0, 0, 1], "css-var --landing-ease (light)"),
        },
        "elevation": {
            "drop-16": token("elevation.drop-16", "shadow", [{"color": "#00000080", "offsetX": "0px", "offsetY": "8px", "blur": "16px", "spread": "0px"}], "css-var --rw-drop-shadow-16 (light). Not seen on the measured marketing controls."),
        },
    }


def light():
    return {
        "page": {"$value": "{core.color.gray.0}", "$type": "color", "$extensions": {"source": "alias of core.color.gray.0; marketing page is white (screenshot home-light-default)"}},
        "surface": {"$value": "{core.color.quiet}", "$type": "color", "$extensions": {"source": "alias of measured quiet button fill"}},
        "text": {
            "DEFAULT": {"$value": "{core.color.ink}", "$type": "color", "$extensions": {"source": "alias of measured nav ink"}},
            "muted": {"$value": "{core.color.menu-muted}", "$type": "color", "$extensions": {"source": "alias of measured menu-trigger resting colour"}},
            "on-accent": {"$value": "{core.color.hero-on-media}", "$type": "color", "$extensions": {"source": "alias of white on the filled CTA"}},
        },
        "border": {
            "DEFAULT": {"$value": "rgba(0, 0, 0, 0.1)", "$type": "color", "$extensions": {"source": "class border-black/10 on the open Creative menu divider (menus-and-crops.mjs hover log)"}},
        },
        "accent": {"$value": "{core.color.interactive.primary}", "$type": "color", "$extensions": {"source": "alias of --interactive-primary. Focus ring on the hero CTA is Tailwind ring-blue-500; the exact ring colour was not read as a computed outline."}},
        "danger": {"$value": "{core.color.danger}", "$type": "color", "$extensions": {"source": "alias of --rw-danger. Not seen painted on the captured marketing pages."}},
        "focus": {
            "ring": {"$value": "{core.color.interactive.primary}", "$type": "color", "$extensions": {"source": "Not captured as a computed outline. The hero CTA class names focus-visible:ring-blue-500. Marked as the declared interactive primary, not a held focus-visible reading."}},
        },
        "component": {
            "button": {
                "bg": {"$value": "{core.color.cta}", "$type": "color", "$extensions": {"source": "alias of nav-cta background"}},
                "text": {"$value": "{core.color.hero-on-media}", "$type": "color", "$extensions": {"source": "alias of nav-cta text"}},
                "radius": {"$value": "{core.radius.sm}", "$type": "dimension", "$extensions": {"source": "alias of nav-cta radius"}},
                "height": {"$value": "{core.size.nav-cta}", "$type": "dimension", "$extensions": {"source": "alias of nav-cta height"}},
            },
        },
    }


def build():
    doc = {
        "core": core(),
        "light": light(),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        ],
    }
    # walk and confirm every leaf has a source
    def walk(node, path=""):
        if isinstance(node, dict) and "$value" in node:
            if "source" not in node.get("$extensions", {}):
                raise SystemExit("missing source " + path)
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if k.startswith("$"):
                    continue
                walk(v, path + "." + k)
    walk(doc)
    (HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
    print("wrote tokens.json")


if __name__ == "__main__":
    build()
