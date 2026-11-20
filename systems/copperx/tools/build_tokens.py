#!/usr/bin/env python3
"""Build tokens.json from Copperx's measured public surface.

Copperx does not publish a design-token custom-property layer. The marketing
site is Tailwind utility classes, so every value here is a computed style
read on copperx.io on 2026-11-18 (raw/foundations.json) or a duration read
by the motion probe (raw/motion.json, when present).

One light theme. Dark is not a published theme on the signed-out site.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = ROOT / "raw"
sys.path.insert(0, str(HERE))

F = json.loads((RAW / "foundations.json").read_text())
CJ = json.loads((RAW / "components-computed.json").read_text())
C = CJ["components"]


def need(v, what):
    if v in (None, ""):
        raise SystemExit("build_tokens: no reading for " + what)
    return v


def fnd(*path):
    """A value from raw/foundations.json, by key path."""
    v = F
    for k in path:
        v = v.get(k) if isinstance(v, dict) else None
    return need(v, "foundations.json " + ".".join(path))


def comp(key, prop, state="default"):
    """A computed style from raw/components-computed.json."""
    s = ((C.get(key) or {}).get("states") or {}).get(state) or {}
    return need((s.get("style") or {}).get(prop), "%s of %s %s" % (prop, key, state))


def hexa(v):
    """rgb()/rgba() as #rrggbb when opaque, rgba(r, g, b, a) otherwise."""
    m = re.fullmatch(r"rgba?\(\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\s*\)", str(v).strip())
    if not m:
        raise SystemExit("build_tokens: cannot read colour %r" % v)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
    return "rgba(%d, %d, %d, %g)" % (int(float(r)), int(float(g)), int(float(b)), float(a))


def ls(v):
    return "0px" if v == "normal" else v


def color(value, source, description=""):
    tok = {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": source},
    }
    if description:
        tok["$description"] = description
    return tok


def dim(value, source, description=""):
    tok = {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": source},
    }
    if description:
        tok["$description"] = description
    return tok


def typography(family, size, weight, line, tracking, source):
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$type": "typography",
        "$extensions": {"source": source},
    }


def shadow(value, source):
    """A computed box-shadow list as DTCG layers; Tailwind's all-zero transparent ring slots are dropped."""
    layers = []
    for part in re.split(r",\s*(?![^()]*\))", value):
        m = re.fullmatch(r"(rgba?\([^)]*\))\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)", part.strip())
        if not m:
            raise SystemExit("build_tokens: cannot read box-shadow layer %r" % part)
        if hexa(m.group(1)).endswith(", 0)") and m.group(2, 3, 4, 5) == ("0px",) * 4:
            continue
        layers.append({"color": hexa(m.group(1)), "offsetX": m.group(2), "offsetY": m.group(3), "blur": m.group(4), "spread": m.group(5)})
    return {"$value": layers, "$type": "shadow", "$extensions": {"source": source}}


DATE = F["captured"]
SRC = "computed on https://copperx.io/ %s (raw/foundations.json)" % DATE
CC = "computed on https://copperx.io/ %s (raw/components-computed.json" % CJ["_meta"]["captured"]


def cc(key, prop, state="default"):
    return "%s, %s of %s %s)" % (CC, prop, key, state)


# Typed in by hand at capture time; no raw file holds the value (docs/EVIDENCE.md: Reconstruction).
HAND = "Reconstruction: entered by hand at capture time on copperx.io %s; no raw reading holds it" % DATE

def ftype(role, what):
    f = fnd("type", role)
    return typography(f["fontFamily"], f["fontSize"], int(f["fontWeight"]), f["lineHeight"], ls(f.get("letterSpacing", "normal")),
                      "%s type.%s (%s)" % (SRC, role, what))


def ctype(key, what):
    return typography(comp(key, "fontFamily").split(",")[0].strip().strip('"'), comp(key, "fontSize"), int(comp(key, "fontWeight")),
                      comp(key, "lineHeight"), ls(comp(key, "letterSpacing")), "%s (%s)" % (cc(key, "font"), what))


BTN = fnd("buttons", "login")
PAD_Y, PAD_X = BTN["pad"].split()

core = {
    "color": {
        "ink": color(hexa(fnd("buttons", "login", "color")), SRC + " buttons.login.color", "Button label on the light control. rgb(19, 23, 31)."),
        "ink-strong": color(hexa(fnd("type", "display", "color")), SRC + " type.display.color", "Hero headline and the dark button's hover. rgb(30, 35, 46)."),
        "body": color("#6a7385", HAND, "Secondary copy. rgb(106, 115, 133): the hue of the measured button ring, rgba(106, 115, 133, 0.16), but no text was read in it."),
        "muted": color(hexa(fnd("type", "body", "color")), SRC + " type.body.color", "Menu description copy. rgb(141, 144, 151)."),
        "indigo": color(hexa(fnd("heroAccent", "color")), SRC + " heroAccent.color", "The word Stablecoin in the hero, Tailwind text-indigo-500. rgb(76, 99, 237)."),
        "indigo-link": color(hexa(fnd("link", "color")), SRC + " link.color", "Menu link colour, Tailwind text-indigo-400. rgb(95, 118, 249)."),
        "indigo-deep": color(hexa(fnd("painted")[1]), SRC + " painted[1]", "Painted indigo block. rgb(62, 80, 183)."),
        "teal": color(hexa(fnd("painted")[0]), SRC + " painted[0]", "Painted teal block. rgb(46, 159, 178)."),
        "paper": color(hexa(fnd("buttons", "login", "hover")), SRC + " buttons.login.hover", "Light button hover and the cool page wash. rgb(247, 249, 252)."),
        "line": color(hexa(comp("login-button", "borderTopColor")), cc("login-button", "borderTopColor"), "Default border colour the buttons inherit. rgb(188, 195, 209)."),
        "white": color(hexa(fnd("header", "background")), SRC + " header.background", "Page and header."),
        "black": color(hexa(fnd("buttons", "primary", "bg")), SRC + " buttons.primary.bg", "Primary button fill."),
        "focus": color(hexa(fnd("buttons", "focusOutline")), SRC + " buttons.focusOutline", "Browser focus outline on the header buttons. rgb(0, 95, 204)."),
    },
    "font": {
        "family": {
            "sans": {
                "$value": fnd("type", "display", "fontFamily"),
                "$type": "fontFamily",
                "$extensions": {"source": SRC + " type.*.fontFamily"},
                "$description": "The marketing site sets Euclid Circular A on headings, body and buttons. The files are proprietary and are not shipped. Fall back to ui-sans-serif.",
            }
        }
    },
    "typography": {
        "display": ftype("display", "h1"),
        "title": typography("Euclid Circular A", "48px", 500, "52px", "-1.2px", HAND + " (product h1)"),
        "heading": ftype("heading", "menu heading"),
        "body": ftype("nav", "nav"),
        "ui": ctype("login-button", "button"),
        "caption": ftype("body", "menu description"),
    },
    "radius": {
        "control": dim(BTN["radius"], SRC + " buttons.login.radius (.btn)"),
        "panel": dim("16px", HAND + " (rounded-2xl menu panel)"),
    },
    "spacing": {
        "2": dim(PAD_Y, SRC + " buttons.login.pad (padding-block)"),
        "3": dim(PAD_X, SRC + " buttons.login.pad (padding-inline)"),
        "4": dim("16px", "Derived: the 4px step extended past the measured 8px and 12px paddings; not read"),
        "6": dim("24px", "Derived: the 4px step extended past the measured 8px and 12px paddings; not read"),
    },
    "size": {
        "button": dim("%dpx" % BTN["height"], SRC + " buttons.login.height (.btn)"),
        "header": dim("%dpx" % fnd("header", "height"), SRC + " header.height"),
    },
    "elevation": {
        "control": shadow(comp("login-button", "boxShadow"), cc("login-button", "boxShadow")),
    },
}

light = {
    "background": {
        "page": color("{color.white}", SRC, "Header and page field."),
        "wash": color("{color.paper}", SRC, "Light button hover and cool section wash."),
        "inverse": color("{color.black}", SRC, "Primary button."),
    },
    "text": {
        "primary": color("{color.ink-strong}", SRC, "Headlines."),
        "body": color("{color.body}", SRC, "Secondary copy."),
        "muted": color("{color.muted}", SRC, "Descriptions."),
        "inverse": color("{color.white}", SRC, "Label on the black button."),
        "link": color("{color.indigo-link}", SRC, "Menu links."),
    },
    "accent": {
        "default": color("{color.indigo}", SRC),
        "deep": color("{color.indigo-deep}", SRC),
        "teal": color("{color.teal}", SRC),
    },
    "border": {
        "default": color(hexa(comp("header", "borderTopColor")), cc("header", "borderTopColor") + "; the header's border-bottom, " + fnd("header", "borderBottom")),
        "control": color(shadow(comp("login-button", "boxShadow"), "")["$value"][-1]["color"], cc("login-button", "boxShadow") + ", the 1px ring layer"),
        "focus": color("{color.focus}", SRC),
    },
    "action": {
        "primary": color("{color.black}", SRC),
        "primary-hover": color("{color.ink-strong}", SRC),
        "secondary": color("{color.white}", SRC),
        "secondary-hover": color("{color.paper}", SRC),
    },
    "component": {
        "button": {
            "bg": color("{color.black}", SRC),
            "text": color("{color.white}", SRC),
            "radius": dim("{radius.control}", "alias to the measured .btn radius"),
            "height": dim("{size.button}", "alias to the measured .btn height"),
        },
        "button-secondary": {
            "bg": color("{color.white}", SRC),
            "text": color("{color.ink}", SRC),
            "radius": dim("{radius.control}", "alias to the measured .btn radius"),
        },
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
    }],
    "$metadata": {
        "tokenSetOrder": ["core", "light"],
    },
}

motion_path = RAW / "motion.json"
if motion_path.exists():
    import motion
    # motion.build returns (group, notTokenised), as the kit's build_tokens.py unpacks it.
    group, not_tokenised = motion.build(json.loads(motion_path.read_text()))
    tokens["core"]["motion"] = group
    if not_tokenised:
        tokens["$extensions"] = {"notTokenised": not_tokenised}

def build():
    return tokens


if __name__ == "__main__":
    (ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", ROOT / "tokens.json")
