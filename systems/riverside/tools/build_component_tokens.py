#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

riverside.com is a Webflow marketing site. Its :root block (raw/css-vars.json,
read by tools/capture/vars.mjs) declares a named palette:

  --peacock / --peacock-2 / --slate-blue / --primary-purple / --primary-500
                           the purple accent family
  --brand-black / --black / --dark
                           ink
  --white / --white-smoke / --ghost-white / --light
                           paper and surfaces
  --lavender / --lime / --mint-cream / --floral-white
                           washes
  --grey / --tech-gray / --secondary-c300
                           muted ink

The site paints one light theme. The login wall is a dark panel on the same
theme, not a second theme. A leaf is {"var": "--name"} or a measured value
with the component it came from.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {
    "_about": (
        "The token tree build_tokens.py turns into tokens.json. riverside.com "
        "declares a named Webflow palette on :root. Colour names stay under "
        "core.color. Roles are the light set. Measured sizes come from "
        "raw/components-computed.json. The login wall is a dark panel, not a theme."
    ),
    "core": {},
    "light": {},
    "dark": {},
    "component": {},
}


def emit_color(group, key, name):
    SPEC["core"].setdefault("color", {}).setdefault(group, {})[key] = var(name)


# Named palette, grouped by role. Names that are not colours are skipped.
PALETTE = {
    "ink": {
        "brand": "--brand-black",
        "navy": "--black",
        "dark": "--dark",
        "black": "--black-2",
        "slate": "--black-3",
        "secondary": "--secondary--black-2",
    },
    "paper": {
        "white": "--white",
        "smoke": "--white-smoke",
        "smoke-2": "--white-smoke-2",
        "smoke-3": "--white-smoke-3",
        "ghost": "--ghost-white",
        "light": "--light",
        "floral": "--floral-white",
        "alice": "--alice-blue",
    },
    "accent": {
        "peacock": "--peacock",
        "peacock-2": "--peacock-2",
        "slate-blue": "--slate-blue",
        "purple": "--primary-purple",
        "purple-500": "--primary-500",
        "purple-2": "--secondary-purple",
        "medium": "--medium-slate-blue",
        "royal": "--royal-blue",
        "sky": "--slate-blue-2",
    },
    "wash": {
        "lavender": "--lavender",
        "lime": "--lime",
        "mint": "--mint-cream",
    },
    "muted": {
        "grey": "--grey",
        "tech": "--tech-gray",
        "tech-text": "--tech-gray-text",
        "c150": "--secondary-c150",
        "c300": "--secondary-c300",
        "white-ca": "--white-ca",
    },
}
for group, names in PALETTE.items():
    for key, name in names.items():
        if name in R:
            emit_color(group, key, name)


def st(comp, state):
    c = C[comp]
    if c.get("missing") or not c.get("states") or state not in c["states"]:
        raise KeyError(comp + " " + state)
    if "style" not in c["states"][state]:
        raise KeyError(comp + " " + state)
    return c["states"][state]["style"]


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 0.999:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return "rgba(%d, %d, %d, %g)" % (int(float(r)), int(float(g)), int(float(b)), float(a))
    if re.fullmatch(r"#[0-9a-fA-F]{3,8}", v):
        return v.lower()
    return v


LIGHT = [
    ("page", {"value": "#ffffff", "type": "color",
              "source": "computed background of the homepage body, matching --white (raw/css-vars.json)",
              "description": "Page paper."}),
    ("surface", {"value": "#f7f7f7", "type": "color",
                 "source": "computed backgroundColor of plan-card default (raw/components-computed.json)",
                 "description": "Pricing page field behind the plan cards."}),
    ("text", var("--brand-black", description="Primary ink on marketing pages, measured on the header and nav.")),
    ("muted", var("--secondary-c300", description="Muted grey from the :root palette.")),
    ("accent", var("--primary-purple", description="The purple CTA and link accent.")),
    ("border", var("--secondary-c150", description="Hairline grey from the :root palette.")),
    ("on-accent", var("--white", description="Text on the black nav CTA and the purple hero CTA.")),
    ("ink", var("--brand-black", description="The black Start for Free pill fill.")),
    ("footer-muted", {"value": "#c7c7c7", "type": "color",
                      "source": "computed color of footer-link default (raw/components-computed.json)",
                      "description": "Footer link ink on the dark footer."}),
    ("login-surface", {"value": "#222222", "type": "color",
                       "source": "computed backgroundColor of login-email default (raw/components-computed.json)",
                       "description": "Login field fill on the dark login panel. A panel, not a theme."}),
    ("login-text", {"value": "#fafafa", "type": "color",
                    "source": "computed color of login-title default (raw/components-computed.json)",
                    "description": "Text on the login panel."}),
    ("login-link", var("--primary-500", description="SSO and sign-up link colour on the login wall.")),
]
for key, leaf in LIGHT:
    SPEC["light"][key] = leaf

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("nav-cta", "default", "cta-fill", "backgroundColor", "The black Start for Free pill."),
    ("nav-cta", "default", "cta-text", "color", "White label on the black pill."),
    ("nav-link", "focus-visible", "focus-ring", "outlineColor", "Keyboard focus ring on the Pricing link, if one paints."),
    ("newsletter-field", "default", "field-fill", "backgroundColor", "The blog email field fill."),
    ("login-email", "default", "login-field", "backgroundColor", "The login email field fill."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v not in ("transparent", "rgba(0, 0, 0, 0)"):
            meas[key] = {
                "value": v, "type": "color",
                "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                "description": desc,
            }
    except KeyError:
        pass

font = SPEC["core"].setdefault("font", {})
font["family"] = {
    "display": {
        "value": '"Sharp Grotesk", Arial, sans-serif',
        "type": "fontFamily",
        "source": "computed fontFamily of hero-title default (raw/components-computed.json); @font-face Sharp Grotesk in raw/css-vars.json",
        "description": "Marketing display headings.",
    },
    "ui": {
        "value": '"Instrument Sans", Arial, sans-serif',
        "type": "fontFamily",
        "source": "computed fontFamily of nav-link and header (raw/components-computed.json); @font-face Instrument Sans in raw/css-vars.json",
        "description": "Marketing UI and body.",
    },
    "login": {
        "value": "Inter, sans-serif",
        "type": "fontFamily",
        "source": "computed fontFamily of login-email default (raw/components-computed.json)",
        "description": "The login wall uses Inter, not Instrument Sans.",
    },
}


def tstyle(comp, state, family_token, desc):
    s = st(comp, state)
    return {
        "fontFamily": "{" + family_token + "}",
        "fontSize": s["fontSize"],
        "lineHeight": s["lineHeight"] if s.get("lineHeight") not in (None, "normal") else s["fontSize"],
        "fontWeight": int(float(s["fontWeight"])),
        "letterSpacing": "0em" if s.get("letterSpacing") in (None, "normal") else s["letterSpacing"],
    }, f"computed type of {comp} {state} (raw/components-computed.json); {desc}"


typo = SPEC["core"].setdefault("typography", {})
for key, comp, state, fam, desc in [
    ("display", "hero-title", "default", "font.family.display", "the 60px Sharp Grotesk hero"),
    ("title", "pricing-title", "default", "font.family.display", "the 50px pricing heading"),
    ("ui", "nav-cta", "default", "font.family.ui", "the 14px pill label"),
    ("body", "header", "default", "font.family.ui", "the 16px header/body size"),
    ("caption", "footer-link", "default", "font.family.ui", "the 12px footer link"),
    ("login", "login-title", "default", "font.family.login", "the 20px login heading"),
]:
    try:
        v, src = tstyle(comp, state, fam, desc)
        typo[key] = {"$value": v, "$type": "typography", "$extensions": {"source": src}}
    except KeyError:
        pass

rad = SPEC["core"].setdefault("radius", {})
for key, comp, desc in [
    ("pill", "nav-cta", "the Start for Free pill (300px, fully round at 40px height)"),
    ("field", "newsletter-field", "the blog email field"),
    ("login-field", "login-email", "the login email field"),
]:
    try:
        rad[key] = {
            "type": "dimension",
            "value": st(comp, "default")["borderTopLeftRadius"],
            "source": f"computed borderTopLeftRadius of {comp} default (raw/components-computed.json)",
            "description": desc,
        }
    except KeyError:
        pass

lay = SPEC["core"].setdefault("layout", {})
for key, comp, prop, desc in [
    ("header-height", "header", "height", "the desktop top bar"),
    ("mobile-header-height", "m-header", "height", "the phone top bar"),
    ("control-height", "nav-cta", "height", "the Start for Free pill"),
    ("field-height", "newsletter-field", "height", "the blog email field"),
    ("login-field-height", "login-email", "height", "the login email field"),
]:
    try:
        lay[key] = {
            "type": "dimension",
            "value": st(comp, "default")[prop],
            "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
            "description": desc,
        }
    except KeyError:
        pass

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button.height", "nav-cta", "default", "height", "The header Start for Free pill."),
    ("button.radius", "nav-cta", "default", "borderTopLeftRadius", "The pill radius."),
    ("field.height", "newsletter-field", "default", "height", "The newsletter field."),
    ("field.radius", "newsletter-field", "default", "borderTopLeftRadius", "The newsletter field radius."),
    ("header.height", "header", "default", "height", "The desktop header."),
    ("menu.row", "m-nav-link", "default", "height", "A phone menu row."),
]:
    try:
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {
            "type": "dimension",
            "value": st(cname, state)[prop],
            "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
            "description": desc,
        }
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
print("wrote", RAW / "component-tokens.json")
