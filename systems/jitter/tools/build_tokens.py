#!/usr/bin/env python3
"""Build tokens.json for jitter.video from raw/css-vars.json and raw/components-computed.json.

One light theme. Foundation colours are the custom properties declared on body.
Button fills are measured on span.button-inner (the anchor itself is transparent).
Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from motion import build as motion_build  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text()) if (RAW / "components-computed.json").exists() else {"components": {}}

BODY = {}
for rule in V.get("foundation", []):
    if rule.get("selector") == "body" and not rule.get("context"):
        BODY.update(rule["properties"])


def tok(value, typ, source):
    return {"$value": value, "$type": typ, "$extensions": {"source": source}}


def color(value, source):
    return tok(norm(value), "color", source)


def norm(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = int(h[6:8], 16) / 255
            if a >= 0.999:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    raise ValueError("not a colour: " + v)


def face(key, state="default"):
    c = COMP["components"].get(key, {})
    st = (c.get("states") or {}).get(state) or {}
    return (st.get("face") or {}).get("backgroundColor") or (st.get("style") or {}).get("backgroundColor")


def face_color(key, state="default"):
    c = COMP["components"].get(key, {})
    st = (c.get("states") or {}).get(state) or {}
    return (st.get("face") or {}).get("color") or (st.get("style") or {}).get("color")


core = {
    "color": {
        "ink": color(BODY.get("--primary-color", "#19171c"), "css-var --primary-color on body"),
        "page": color(BODY.get("--bg-color", "#ffffff"), "css-var --bg-color on body"),
        "pink": color(BODY.get("--primary-color-alt", "#fba6ec"), "css-var --primary-color-alt on body"),
        "muted": color(BODY.get("--secondary-color", "#6e6e73"), "css-var --secondary-color on body"),
        "white": color("#ffffff", "css-var --bg-color on body; also the painted page"),
        "violet": color("#b593ff", "computed background of span.button-inner on the violet hero CTA, 2026-11-18"),
        "yellow": color("#f5ff63", "computed background of the yellow pill (Read customer stories), 2026-11-18"),
        "blue": color("#50b8ff", "computed background of the Free plan Get started pill, 2026-11-18"),
        "blue-strong": color("#29a9ff", "computed background of Continue with SSO, and of the editor Share button, rgb(41, 169, 255)"),
        "grey": color("#f2f1f3", "computed background of the header and the light-grey auth buttons, 2026-11-18"),
        "violet-export": color("#9262f0", "computed background of the editor Export button, rgb(146, 98, 240)"),
        "violet-upgrade": color("#7a40ed", "computed background of the editor Upgrade now chip, rgb(122, 64, 237)"),
    },
    "font": {
        "family": {
            "ui": tok("TWK Lausanne, sans-serif", "fontFamily", "computed font-family on button controls, jitter.video 2026-11-18"),
            "body": tok("Inter, sans-serif", "fontFamily", "computed font-family on body, jitter.video 2026-11-18"),
            "display": tok("Euclid Circular B, sans-serif", "fontFamily", "@font-face family harvested from the marketing stylesheet"),
        },
        "weight": {
            "regular": tok(400, "fontWeight", "body text weight"),
            "medium": tok(500, "fontWeight", "computed font-weight on the editor Share button"),
            "semibold": tok(600, "fontWeight", "computed font-weight on button controls"),
        },
        "size": {
            "body": tok("16px", "dimension", "body text size on the marketing pages"),
            "button": tok("18px", "dimension", "computed font-size on the small button"),
            "button-md": tok("20px", "dimension", "computed font-size on the medium hero CTA"),
        },
    },
    "radius": {
        "pill": tok("50px", "dimension", "computed border-radius on span.button-inner"),
        "sheet": tok("80px", "dimension", "computed border-radius on the footer inner, bottom corners only (0 0 80px 80px)"),
    },
    "space": {
        "header-offset": tok("48px", "dimension", "css-var --top-bar-offset on body at width >= 1025px"),
        "header-offset-phone": tok("20px", "dimension", "css-var --top-bar-offset on body below 1025px"),
        "logo-offset": tok("73px", "dimension", "css-var --top-logo-offset on body at width >= 1025px"),
    },
    "size": {
        "button-sm": tok("52px", "dimension", "computed height of the small pill"),
        "button-md": tok("60px", "dimension", "computed height of the medium pill"),
        "button-share": tok("32px", "dimension", "computed height of the editor Share button"),
        "button-export": tok("48px", "dimension", "computed height of the editor Export button"),
        "desktop": tok("1440px", "dimension", "capture viewport width"),
        "phone": tok("390px", "dimension", "capture viewport width"),
    },
}

# Prefer measured fills when the component pass has run.
measured = {
    "violet": ("hero-cta", "violet"),
    "yellow": ("stories-link", "yellow"),
    "blue": ("plan-free", "blue"),
}
for name, (key, _label) in measured.items():
    raw = face(key)
    if raw and raw != "rgba(0, 0, 0, 0)":
        try:
            core["color"][name] = color(raw, f"computed background of span.button-inner on {key}")
        except ValueError:
            pass

light = {
    "surface": {
        "page": tok("{color.page}", "color", "alias of body --bg-color"),
        "ink": tok("{color.ink}", "color", "alias of body --primary-color, used as the black button fill"),
    },
    "text": {
        "primary": tok("{color.ink}", "color", "computed color on body"),
        "muted": tok("{color.muted}", "color", "css-var --secondary-color"),
        "onAccent": tok("{color.ink}", "color", "computed color on the violet and yellow pills"),
        "onInk": tok("{color.white}", "color", "computed color on the black Sign up pill"),
    },
    "accent": tok("{color.violet}", "color", "hero CTA fill"),
    "border": {
        "subtle": tok("#d7d7db", "color", "computed border-top-color on the login email field, rgb(215, 215, 219)"),
    },
    "focus": tok("{color.ink}", "color", "keyboard focus ring colour on buttons"),
    "button": {
        "black": tok("{color.ink}", "color", "Sign up pill fill"),
        "violet": tok("{color.violet}", "color", "hero CTA fill"),
        "yellow": tok("{color.yellow}", "color", "stories and subscribe fill"),
        "white": tok("{color.white}", "color", "white pill fill"),
        "export": tok("{color.violet-export}", "color", "editor Export fill"),
        "upgrade": tok("{color.violet-upgrade}", "color", "editor Upgrade now fill"),
        "share": tok("{color.blue-strong}", "color", "editor Share fill"),
        "radius": tok("{radius.pill}", "dimension", "pill radius"),
        "height": tok("{size.button-sm}", "dimension", "small button height"),
    },
}

motion_path = RAW / "motion.json"
if motion_path.exists():
    group, skipped = motion_build(json.loads(motion_path.read_text()))
    if group:
        core["motion"] = group
    if skipped:
        core.setdefault("$extensions", {})["motionNotTokenised"] = skipped

doc = {
    "$description": "Jitter marketing plus signed-in files, account, onboarding and editor, captured 2026-11-18. One light theme on marketing and files; the editor chrome is a dark header on a light canvas.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

# Flatten aliases in $value that point at core groups for the checker.
def resolve(val, seen=()):
    if not isinstance(val, str) or not val.startswith("{"):
        return val
    path = val.strip("{}").split(".")
    node = core
    for p in path:
        node = node[p]
    return resolve(node["$value"], seen + (val,))

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "core groups", list(core))
