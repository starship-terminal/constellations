#!/usr/bin/env python3
"""Build tokens.json from the Missive public capture.

Marketing colour lives on :root as --swatch--* and --color--* in the Webflow
sheet. The signed-out mail app (mail.missiveapp.com) declares its own custom
properties on :root for light and on [data-theme="dark"] for dark. tools/
capture/vars.mjs resolved both. Component colours that are literals (the
marketing Try for free fill, the mail Log in fill) come from
raw/components-computed.json.

Two painted themes. Marketing is light only. The dark set is the mail app.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))

VARS = json.loads((RAW / "css-vars.json").read_text())
LIGHT = VARS["resolved"]["light"]
DARK = VARS["resolved"]["dark"]
COMP = json.loads((RAW / "components-computed.json").read_text()) if (RAW / "components-computed.json").exists() else {"components": {}}

S = "Resolved from missiveapp.com and mail.missiveapp.com custom properties, 2026-11-19"
M = "Measured computed style, public Missive pages, 2026-11-19, light, 1440"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def text(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def cubic(value, source):
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def resolved(theme, name):
    node = (LIGHT if theme == "light" else DARK).get(name)
    if not node:
        raise SystemExit(f"missing {name} in {theme}")
    return node["value"]


def hex_of(value):
    value = value.strip()
    if value.startswith("#") and len(value) == 7:
        return value.lower()
    if value == "white":
        return "#ffffff"
    if value == "black":
        return "#000000"
    m = re.fullmatch(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    m = re.fullmatch(r"rgb\((\d+)\s+(\d+)\s+(\d+)\)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    m = re.fullmatch(r"rgba?\((\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,/]\s*([\d.]+))?\)", value)
    if m and (m.group(4) is None or float(m.group(4)) >= 1):
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    return None


def swatch(prefix):
    out = {}
    for key, node in LIGHT.items():
        m = re.fullmatch(re.escape(prefix) + r"(.+)", key)
        if not m or node.get("kind") != "color":
            continue
        step = m.group(1).replace("-", "")
        hx = hex_of(node["value"]) or node["value"]
        out[step] = color(hx, f"{S}: {key} was {node.get('raw')}")
    if not out:
        raise SystemExit(f"no swatch {prefix}")
    return out


core = {
    "color": {
        "neutral": swatch("--swatch--neutral-"),
        "blue": swatch("--swatch--blue-"),
        "cumin": swatch("--swatch--cumin-"),
        "green": swatch("--swatch--green-"),
        "white": color("#ffffff", f"{S}: --swatch--white"),
        "black": color("#000000", f"{S}: --swatch--black"),
        "brand": color(hex_of(resolved("light", "--color--brand")), f"{S}: --color--brand aliases --swatch--blue-600"),
        "mail": {
            "brand": color(hex_of(resolved("light", "--brand-color")), f"{S}: mail --brand-color"),
            "blue": color(hex_of(resolved("light", "--blue-color")), f"{S}: mail --blue-color"),
            "green": color(hex_of(resolved("light", "--green-color")), f"{S}: mail --green-color"),
            "red": color(hex_of(resolved("light", "--red-color")), f"{S}: mail --red-color"),
            "orange": color(hex_of(resolved("light", "--orange-color")), f"{S}: mail --orange-color"),
            "yellow": color(hex_of(resolved("light", "--yellow-color")), f"{S}: mail --yellow-color"),
            "ink": color(hex_of(resolved("light", "--text-color-a")), f"{S}: mail --text-color-a, light"),
            "inkMuted": color(hex_of(resolved("light", "--text-color-b")), f"{S}: mail --text-color-b, light"),
        },
    },
    "font": {
        "family": {
            "display": font('Tiempos Headline, "Times New Roman", sans-serif', f"{M}: marketing h1 paints Tiempos Headline"),
            "sans": font("Inter, Arial, sans-serif", f"{M}: marketing nav and body paint Inter"),
            "ui": font(resolved("light", "--font-family"), f"{S}: mail --font-family, the system stack"),
        },
        "weight": {
            "regular": num(400, f"{M}: marketing body and nav links"),
            "medium": num(500, f"{M}: Try for free is 500; mail title is 500"),
            "semibold": num(600, f"{M}: Continue with Google is 600"),
        },
        "size": {
            "ui": dim(resolved("light", "--font-size"), f"{S}: mail --font-size"),
            "nav": dim("14px", f"{M}: marketing nav links"),
            "body": dim("20px", f"{M}: home hero paragraph"),
            "title": dim("24px", f"{M}: Log in to Missive"),
            "display": dim("56px", f"{M}: home h1"),
        },
    },
    "space": {
        "1": dim("4px", f"{S}: --spacing--1 is 0.25rem"),
        "2": dim("8px", f"{S}: --spacing--2 is 0.5rem"),
        "3": dim("12px", f"{S}: --spacing--3 is 0.75rem"),
        "4": dim("16px", f"{S}: --spacing--4 is 1rem"),
        "6": dim("24px", f"{S}: --spacing--6 is 1.5rem"),
        "8": dim("32px", f"{S}: --spacing--8 is 2rem"),
        "12": dim("48px", f"{S}: --spacing--12 is 3rem"),
        "16": dim("64px", f"{S}: --spacing--16 is 4rem"),
        "20": dim("80px", f"{S}: --spacing--20 is 5rem"),
    },
    "radius": {
        "sm": dim(resolved("light", "--border-radius-small"), f"{S}: mail --border-radius-small"),
        "md": dim(resolved("light", "--border-radius"), f"{S}: mail --border-radius"),
        "control": dim("8px", f"{M}: marketing buttons and mail controls paint 8px"),
        "lg": dim(resolved("light", "--border-radius-large"), f"{S}: mail --border-radius-large"),
        "card": dim("16px", f"{M}: pricing plan card left radius is 16px"),
    },
    "layout": {
        "page": dim("1440px", "Desktop capture width"),
        "phone": dim("390px", "Phone capture width"),
        "navHeight": dim("61px", f"{M}: marketing navbar height"),
        "topBar": dim(resolved("light", "--top-bar-height"), f"{S}: mail --top-bar-height"),
        "control": dim("44px", f"{M}: marketing nav Try for free height"),
        "mailControl": dim("45px", f"{M}: Continue with Google height"),
    },
}

light = {
    "page": color("{color.white}", f"{M}: marketing body background is rgb(255, 255, 255)"),
    "surface": color("{color.neutral.050}", f"{S}: --color--bg-neutral aliases --swatch--neutral-050. Watch demo paints it."),
    "text": color("{color.neutral.900}", f"{M}: marketing ink is rgb(52, 54, 58), --swatch--neutral-900"),
    "textBody": color("{color.neutral.500}", f"{M}: hero paragraph is rgb(100, 108, 118), --swatch--neutral-500"),
    "textMuted": color("{color.neutral.400}", f"{S}: --color--c aliases --swatch--neutral-400's neighbour --swatch--neutral-300 is captions; muted step is 400"),
    "textOnAccent": color("{color.white}", f"{M}: Try for free label is white"),
    "accent": color("{color.brand}", f"{M}: Try for free and Log in fill is rgb(34, 102, 237)"),
    "accentHover": color("{color.blue.800}", f"{S}: --color--brand-dark aliases --swatch--blue-800"),
    "link": color("{color.mail.blue}", f"{M}: Forgot your password paints the mail blue"),
    "action": color("{color.brand}", f"{M}: mail Log in submit backgroundColor rgb(34, 102, 237)"),
    "focus": color("{color.mail.blue}", f"{S}: mail focus ring uses --blue-color"),
    "border": color("{color.neutral.100}", f"{M}: pricing card border is rgb(228, 230, 233), --swatch--neutral-100"),
    "error": color("{color.mail.red}", f"{S}: mail --red-color"),
    "success": color("{color.green.600}", f"{S}: --swatch--green-600"),
    "mailPage": color("#f5f6f7", f"{S}: mail --background-color rgb(245, 246, 247)"),
    "mailSurface": color("{color.white}", f"{S}: mail --input-background-color and --popup-background-color"),
    "mailText": color("{color.mail.ink}", f"{S}: mail --text-color-a"),
    "mailMuted": color("{color.mail.inkMuted}", f"{S}: mail --text-color-b"),
}

def dark_hex(name):
    """A mail colour under [data-theme=dark], read from raw/css-vars.json. Raises when it is
    missing or does not parse, so a recapture cannot keep a stale hand-typed value."""
    value = resolved("dark", name)
    hx = hex_of(value)
    if not hx:
        raise SystemExit(f"dark {name} is {value!r}, not an opaque colour")
    return hx


def dark_rgba(name):
    """A translucent mail colour under dark, written as rgba() with the raw channels and alpha."""
    value = resolved("dark", name)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)\s*[,/]\s*(\d*\.?\d+)\s*\)", value)
    if not m:
        raise SystemExit(f"dark {name} is {value!r}, not a translucent colour")
    alpha = float(m.group(4))
    return f"rgba({m.group(1)}, {m.group(2)}, {m.group(3)}, {alpha:g})"


DARK_PAGE = dark_hex("--background-color")
DARK_TEXT = dark_hex("--text-color-a")
DARK_BODY = dark_hex("--text-color-b")
DARK_MUTED = dark_hex("--text-color-c")
DARK_SURFACE = dark_hex("--popup-background-color")
DARK_INPUT = dark_hex("--input-background-color")
DARK_BORDER = dark_rgba("--border-color")

dark = {
    "page": color(DARK_PAGE, f"{S}: mail --background-color under [data-theme=dark] is {resolved('dark', '--background-color')}"),
    "surface": color(DARK_SURFACE, f"{S}: mail --popup-background-color under dark is {resolved('dark', '--popup-background-color')}"),
    "text": color(DARK_TEXT, f"{S}: mail --text-color-a under dark is {resolved('dark', '--text-color-a')}"),
    "textBody": color(DARK_BODY, f"{S}: mail --text-color-b under dark is {resolved('dark', '--text-color-b')}"),
    "textMuted": color(DARK_MUTED, f"{S}: mail --text-color-c under dark is {resolved('dark', '--text-color-c')}"),
    "textOnAccent": color("{color.white}", f"{M}: Log in label stays white on the brand fill"),
    "accent": color("{color.brand}", f"{S}: mail --brand-color does not change under dark"),
    "accentHover": color("{color.blue.800}", f"{S}: marketing brand-dark; mail brand is unchanged"),
    "link": color("{color.mail.blue}", f"{S}: mail --blue-color does not change under dark"),
    "action": color("{color.brand}", f"{S}: mail --brand-color"),
    "focus": color("{color.mail.blue}", f"{S}: mail --blue-color"),
    "border": color(DARK_BORDER, f"{S}: mail --border-color under dark is {resolved('dark', '--border-color')}"),
    "error": color("{color.mail.red}", f"{S}: mail --red-color"),
    "success": color("{color.mail.green}", f"{S}: mail --green-color"),
    "mailPage": color(DARK_PAGE, f"{S}: mail --background-color under dark"),
    "mailSurface": color(DARK_INPUT, f"{S}: mail --input-background-color under dark is {resolved('dark', '--input-background-color')}"),
    "mailText": color(DARK_TEXT, f"{S}: mail --text-color-a under dark"),
    "mailMuted": color(DARK_BODY, f"{S}: mail --text-color-b under dark"),
}


def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)


names = {n for n, _ in walk(core)} | {n for n, _ in walk(light)} | {n for n, _ in walk(dark)}


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


for path, tok in walk({"core": core, "light": light, "dark": dark}):
    for blob in strings(tok["$value"]):
        for alias in re.findall(r"\{([^{}]+)\}", blob):
            if alias not in names:
                raise SystemExit(f"{path} alias {{{alias}}} missing")
    if tok.get("$type") == "dimension":
        val = tok["$value"]
        if isinstance(val, str) and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", val):
            raise SystemExit(f"{path} dimension {val!r}")
    if tok.get("$type") == "color":
        val = tok["$value"]
        if isinstance(val, str) and not val.startswith("{") and not re.fullmatch(r"#[0-9a-f]{6}|rgba?\([^)]+\)", val):
            raise SystemExit(f"{path} colour {val!r}")

motion_path = RAW / "motion.json"
if motion_path.exists():
    import motion as motion_mod
    core["motion"], extra = motion_mod.build(json.loads(motion_path.read_text()))
    if extra:
        core["motion"].setdefault("$extensions", {})["notTokenised"] = extra

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
TEXT = json.dumps(doc, indent=2) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(TEXT)
    print("wrote", HERE / "tokens.json", "tokens", len(list(walk(core))) + len(list(walk(light))) + len(list(walk(dark))))
