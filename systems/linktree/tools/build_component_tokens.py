#!/usr/bin/env python3
"""Write raw/component-tokens.json from measured Linktree styles and CSS vars.

Every colour and metric is read from raw/components-computed.json or from a
resolved custom property in raw/css-vars.json. Nothing is filled from memory.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})


def st(comp, state="default"):
    c = C[comp]
    if c.get("missing"):
        raise KeyError(comp + " missing")
    return c["states"][state]


def style(comp, state="default"):
    return st(comp, state)["style"]


def text_color(comp, state="default"):
    s = st(comp, state)
    return (s.get("textStyle") or {}).get("color") or s["style"]["color"]


def text_font(comp, state="default"):
    s = st(comp, state)
    t = s.get("textStyle") or s["style"]
    return t


def norm_color(v):
    v = v.strip().lower()
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
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    return v


def val(v, ty, src, desc):
    if ty == "color":
        v = norm_color(v)
    return {"value": v, "type": ty, "source": src, "description": desc}


def measured(comp, state, prop, ty, desc, text=False):
    if text:
        v = text_color(comp, state) if prop == "color" else text_font(comp, state).get(prop)
    else:
        v = style(comp, state)[prop]
    return val(v, ty, f"computed {prop} of {comp} {state}", desc)


def split_shadow(v):
    """Split a computed box-shadow on its top-level commas (rgb() holds commas too)."""
    out, depth, cur = [], 0, ""
    for ch in v or "":
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def painted_ring(sty):
    """(colour, how) of the focus ring a state really paints: a drawn outline
    (style neither none nor auto, width above 0, colour not transparent), else
    the outermost visible box-shadow layer with a spread. An `auto` outline is
    the browser's own ring, whose colour the computed style does not report as
    painted, and nav-link's outline is none/0px (it shows focus as a fill), so
    its outlineColor is not a ring. Raises when nothing is painted."""
    if sty.get("outlineStyle", "none") not in ("none", "auto") and float(sty.get("outlineWidth", "0px")[:-2] or 0) > 0 \
            and not re.fullmatch(r"rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0\s*\)", sty.get("outlineColor", "")):
        return sty["outlineColor"], f"outline {sty['outlineWidth']} {sty['outlineStyle']}"
    ring = None
    for layer in split_shadow(sty.get("boxShadow", "none")):
        m = re.match(r"^(rgba?\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?$", layer)
        if not m or m.group(6) or float(m.group(5)) <= 0:
            continue
        if re.fullmatch(r"rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0\s*\)", m.group(1)):
            continue
        ring = (m.group(1), f"box-shadow {m.group(5)}px spread")
    if ring:
        return ring
    raise KeyError("no painted focus ring")


def focus_ring(comp, desc):
    s = st(comp, "focus-visible")
    if s.get("via") == "focus failed" or s.get("skipped"):
        raise KeyError(f"{comp} focus-visible was not captured")
    colour, how = painted_ring(s["style"])
    return val(colour, "color", f"computed focus ring ({how}, outermost layer) of {comp} focus-visible", desc)


def cssvar(name, ty, desc):
    node = RL.get(name)
    if not node or "value" not in node:
        raise KeyError(name)
    return val(node["value"], ty, f"css-var {name} resolved on the light probe", desc)


SPEC = {
    "_about": (
        "Linktree public signed-out tokens. Semantic colours are computed styles "
        "from the marketing site and the official public profile. Tailwind theme "
        "scales in core.scale come from resolved --color-*, --text-* and "
        "--breakpoint-* custom properties. The captured pages paint light."
    ),
    "core": {},
    "light": {},
    "dark": {},
    "component": {},
}

core = SPEC["core"]
light = SPEC["light"]
comp = SPEC["component"]

# Brand and surface colours, each from a painted node.
# The marketing body paints white. Nav and claim-wrap are transparent, so the
# page ground is the claim field's painted white fill. The footer is a separate band.
light["page"] = measured("claim-field", "default", "backgroundColor", "color", "Claim field fill, the painted page ground")
light["surface"] = measured("claim-field", "default", "backgroundColor", "color", "Claim field fill")
light["band"] = measured("footer", "default", "backgroundColor", "color", "Footer band fill")
light["hero"] = cssvar("--color-chartreuse", "color", "Hero band fill on the marketing home")
light["text"] = measured("nav-link", "default", "color", "color", "Nav link ink", text=True)
light["textInverse"] = measured("nav-signup", "default", "color", "color", "Ink on the signup pill", text=True)
light["muted"] = measured("profile-badge", "default", "color", "color", "Verified badge ink", text=True)
light["accent"] = measured("hero-title", "default", "color", "color", "Hero title colour", text=True)
light["border"] = measured("login-field", "default", "borderTopColor", "color", "Login field border")
light["link"] = measured("footer-link", "default", "color", "color", "Footer link ink", text=True)
light["focus"] = focus_ring("nav-login", "Keyboard focus ring on the Log in link (the Sign up pill, hero and claim buttons draw the same ring)")

# Page ground: body was white in recon. If footer is the only filled surface we
# also record the signup pill as the ink button.
light["button"] = measured("nav-signup", "default", "backgroundColor", "color", "Sign up free pill fill")
light["buttonText"] = measured("nav-signup", "default", "color", "color", "Sign up free pill label", text=True)

# Tailwind palette used as the published scale. Only names that resolved.
scale_colors = {
    "black": "--color-black",
    "white": "--color-white",
    "shade": "--color-shade",
    "forest": "--color-forest",
    "dahlia": "--color-dahlia",
    "chartreuse": "--color-chartreuse",
    "lavender": "--color-lavender",
    "marble": "--color-marble",
}
core["color"] = {}
for slug, name in scale_colors.items():
    if name in RL and "value" in RL[name]:
        core["color"][slug.replace("-", "")] = cssvar(name, "color", f"Tailwind theme {name}")

# Type roles from measured text.
def typo(comp_name, state, role, desc):
    t = text_font(comp_name, state)
    family = t.get("fontFamily", "").split(",")[0].strip().strip('"')
    size = t.get("fontSize")
    weight = t.get("fontWeight")
    lh = t.get("lineHeight")
    return {
        "fontFamily": val(family, "fontFamily", f"computed fontFamily of {comp_name} {state} text", desc),
        "fontSize": val(size, "dimension", f"computed fontSize of {comp_name} {state} text", desc),
        "fontWeight": val(int(weight) if str(weight).isdigit() else weight, "fontWeight", f"computed fontWeight of {comp_name} {state} text", desc),
        "lineHeight": val(lh, "dimension", f"computed lineHeight of {comp_name} {state} text", desc),
    }

core["typography"] = {
    "display": typo("hero-title", "default", "display", "Hero title"),
    "body": typo("nav-link", "default", "body", "Nav link"),
    "label": typo("nav-signup", "default", "label", "Signup pill label"),
    "caption": typo("profile-title", "default", "caption", "Public profile title") if "profile-title" in C else typo("pricing-title", "default", "caption", "Pricing title"),
}

# Control metrics.
comp["control"] = {
    "radiusPill": measured("nav-signup", "default", "borderTopLeftRadius", "dimension", "Signup pill radius"),
    "heightNav": measured("nav-signup", "default", "height", "dimension", "Signup pill height"),
    "heightField": measured("claim-field", "default", "height", "dimension", "Claim field height") if "claim-field" in C and not C["claim-field"].get("missing") else measured("login-field", "default", "height", "dimension", "Login field height"),
}
comp["header"] = {
    "height": measured("navbar", "default", "height", "dimension", "Marketing nav height"),
}

# Motion from the signup pill when it declares a transition.
tr = style("nav-signup").get("transitionDuration", "0s")
if tr and tr != "0s":
    comp["motion"] = {
        "duration": val(tr.split(",")[0].strip(), "duration", "computed transitionDuration of nav-signup default", "Signup pill transition"),
    }

# Breakpoints from CSS.
core["layout"] = {}
for key, name in (("sm", "--breakpoint-sm"), ("md", "--breakpoint-md"), ("lg", "--breakpoint-lg"), ("xl", "--breakpoint-xl")):
    if name in RL and RL[name].get("kind") == "dimension":
        core["layout"][key] = cssvar(name, "dimension", f"Tailwind {name}")

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("component-tokens", {k: len(v) if isinstance(v, dict) else 0 for k, v in SPEC.items()})
