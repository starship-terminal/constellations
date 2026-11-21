#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Designmodo's public site does not publish a semantic token layer. The only
custom properties harvested on 2026-11-21 are Swiper vendor vars and landing
layout numbers (raw/css-vars.json). Every token here is a computed style read
from a named element. Roles that were not read are absent, not guessed.
One theme: light. No dark theme was observed (colorScheme normal, no toggle).
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())

def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if not m:
        if re.fullmatch(r"#[0-9a-f]{6}", v):
            return v
        raise ValueError("not a colour: " + v)
    r, g, b, a = m.groups()
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % float(a))

def leaf(path, spec):
    if not spec.get("source"):
        raise ValueError(path + ": no source")
    ty = spec["type"]
    val = spec["value"]
    if ty == "color":
        val = norm_color(val)
        ty_out = "color"
    elif ty == "typography":
        ty_out = "typography"
    elif ty == "shadow":
        ty_out = "shadow"
    elif ty == "fontFamily":
        ty_out = "fontFamily"
    elif ty == "dimension":
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
            raise ValueError(path + ": bad dimension " + repr(val))
        ty_out = "dimension"
    else:
        raise ValueError(path + ": unknown type " + ty)
    return {"$value": val, "$type": ty_out, "$extensions": {"source": spec["source"]}}

def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        out[k] = build(v, path + "." + k if path else k)
    return out

core = build({k: v for k, v in SPEC.items() if not k.startswith("_")})
# semantic set aliases the measured primitives. No extra values.
light = {
    "background": {
        "page": {"$value": "{color.page}", "$type": "color", "$extensions": {"source": "Alias of core.color.page. body itself is transparent; the painted page ground is white."}},
    },
    "text": {
        "primary": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "Alias of core.color.ink, body text on the light pages."}},
        "onAccent": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "Alias of core.color.white, button label colour."}},
        "muted": {"$value": "{color.muted}", "$type": "color", "$extensions": {"source": "Alias of core.color.muted."}},
        "hero": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "Alias of core.color.white, home h1."}},
        "heroMuted": {"$value": "{color.mutedHero}", "$type": "color", "$extensions": {"source": "Alias of core.color.mutedHero, home hero paragraph."}},
    },
    "accent": {
        "green": {"$value": "{color.green}", "$type": "color", "$extensions": {"source": "Alias of core.color.green, Open App."}},
        "greenHover": {"$value": "{color.greenHover}", "$type": "color", "$extensions": {"source": "Alias of core.color.greenHover, Open App hover."}},
        "orange": {"$value": "{color.orange}", "$type": "color", "$extensions": {"source": "Alias of core.color.orange, Sign Up."}},
        "blue": {"$value": "{color.blue}", "$type": "color", "$extensions": {"source": "Alias of core.color.blue, Login submit."}},
    },
    "border": {
        "field": {"$value": "{color.fieldBorder}", "$type": "color", "$extensions": {"source": "Alias of core.color.fieldBorder."}},
    },
    "component": {
        "button": {
            "openApp": {
                "background": {"$value": "{color.green}", "$type": "color", "$extensions": {"source": "states.openAppDefault.backgroundColor"}},
                "text": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "states.openAppDefault.color"}},
                "radius": {"$value": "{radius.pill}", "$type": "dimension", "$extensions": {"source": "states.openAppDefault.borderRadius"}},
                "height": {"$value": "{size.openApp}", "$type": "dimension", "$extensions": {"source": "states.openAppDefault.height"}},
            },
            "signUp": {
                "background": {"$value": "{color.orange}", "$type": "color", "$extensions": {"source": "states.signupDefault.backgroundColor"}},
                "text": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "states.signupDefault.color"}},
                "radius": {"$value": "{radius.pill}", "$type": "dimension", "$extensions": {"source": "states.signupDefault.borderRadius"}},
                "height": {"$value": "{size.signUp}", "$type": "dimension", "$extensions": {"source": "states.signupDefault.height"}},
            },
            "login": {
                "background": {"$value": "{color.blue}", "$type": "color", "$extensions": {"source": "pages.sign-in.primaryButton.backgroundColor"}},
                "text": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "pages.sign-in.primaryButton.color"}},
                "radius": {"$value": "{radius.field}", "$type": "dimension", "$extensions": {"source": "pages.sign-in.primaryButton.borderRadius"}},
                "height": {"$value": "{size.login}", "$type": "dimension", "$extensions": {"source": "pages.sign-in.primaryButton.height"}},
            },
        },
        "field": {
            "background": {"$value": "{color.page}", "$type": "color", "$extensions": {"source": "pages.sign-in.field.backgroundColor"}},
            "text": {"$value": "{color.fieldText}", "$type": "color", "$extensions": {"source": "pages.sign-in.field.color"}},
            "border": {"$value": "{color.fieldBorder}", "$type": "color", "$extensions": {"source": "pages.sign-in.field.borderTopColor"}},
            "radius": {"$value": "{radius.field}", "$type": "dimension", "$extensions": {"source": "pages.sign-in.field.borderRadius"}},
            "height": {"$value": "{size.field}", "$type": "dimension", "$extensions": {"source": "pages.sign-in.field.height"}},
        },
    },
}

doc = {
    "$description": "Designmodo public signed-out surface, measured 2026-11-21. Light only. Values are computed styles, not a published token file.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
out = json.dumps(doc, indent=1) + "\n"
(HERE / "tokens.json").write_text(out)
print("wrote tokens.json", len(out))
