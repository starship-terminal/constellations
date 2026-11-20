#!/usr/bin/env python3
"""Build tokens.json from the Limitless public capture.

Limitless ships one painted theme (light). Colour is Tailwind utilities
(slate, zinc, purple-500) plus a few measured fills, not a custom-property
system on the marketing site. The app host declares shadcn HSL variables;
those are in raw/app-css-vars.json. Every value here was read from a
computed style on 2026-11-18 or derived from those readings. There is no
dark set: the product does not paint one on the captured surfaces.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod

MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


M = "Measured computed style, public Limitless pages, 2026-11-18, light, 1440"
A = "Measured computed style, app.limitless.ai Sign Up Unavailable dialog, 2026-11-18, light, 1440"
D = "Derived from measured computed styles on the same capture"
# Values with no raw reading behind them, typed in at capture time. Kept, labelled.
RECON = "Reconstruction: entered by hand at capture time; no raw reading holds this value"

C = json.loads((RAW / "components-computed.json").read_text())["components"]
DIALOG = json.loads((RAW / "app-css-vars.json").read_text())["paintedOnDialog"]


def recon(note):
    return f"{RECON}; {note}"


def rd(comp, state, prop):
    """One computed property of a measured component state; raises when it is missing."""
    s = C[comp]["states"][state]
    if s.get("error") or "style" not in s:
        raise SystemExit(f"{comp}.{state} has no reading")
    v = s["style"].get(prop)
    if v in (None, ""):
        raise SystemExit(f"{comp}.{state} has no {prop}")
    return v


def norm_color(v):
    v = v.strip()
    m = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", v)
    if not m:
        raise SystemExit("colour not understood: " + v)
    r, g, b, a = m.groups()
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def at(comp, state, prop):
    return f"{comp}.{state} {prop}"


def cm(comp, state, prop, note):
    return color(norm_color(rd(comp, state, prop)), f"{M}: {at(comp, state, prop)}, {note}")


def ca(field, note):
    return color(norm_color(DIALOG[field]), f"{A}: raw/app-css-vars.json paintedOnDialog.{field}, {note}")


def dm(comp, state, prop, note):
    return dim(rd(comp, state, prop), f"{M}: {at(comp, state, prop)}, {note}")


def wm(comp, state, note):
    return num(int(rd(comp, state, "fontWeight")), f"{M}: {at(comp, state, 'fontWeight')}, {note}", "fontWeight")


def gradient_stop(i):
    stops = re.findall(r"rgba?\([^)]*\)", DIALOG["okGradient"])
    return norm_color(stops[i])


def shadow(comp, state, note):
    """The painted layers of a computed box-shadow: colour first, then four lengths, optional inset.
    Fully transparent or all-zero ring layers (Tailwind's empty --tw-ring slots) are dropped."""
    raw = rd(comp, state, "boxShadow")
    layers = []
    for m in re.finditer(r"(rgba?\([^)]*\))\s+((?:-?[\d.]+px\s*){2,4})(inset)?", raw):
        colour, lengths = norm_color(m.group(1)), m.group(2).split()
        lengths += ["0px"] * (4 - len(lengths))
        if colour.endswith(", 0)") or all(x == "0px" for x in lengths):
            continue
        layer = {"color": colour, "offsetX": lengths[0], "offsetY": lengths[1], "blur": lengths[2], "spread": lengths[3]}
        if m.group(3):
            layer["inset"] = True
        layers.append(layer)
    if not layers:
        raise SystemExit(f"{comp}.{state} boxShadow paints nothing: {raw}")
    return {"$type": "shadow", "$value": layers, "$extensions": {"source": f"{M}: {at(comp, state, 'boxShadow')}, {note}"}}


def typo(comp, state, family, note, tracking=True):
    v = {"fontFamily": family, "fontSize": rd(comp, state, "fontSize"), "fontWeight": int(rd(comp, state, "fontWeight")),
         "lineHeight": rd(comp, state, "lineHeight")}
    ls = rd(comp, state, "letterSpacing")
    if tracking and ls != "normal":
        v["letterSpacing"] = ls
    return {"$type": "typography", "$value": v, "$extensions": {"source": f"{M}: {comp}.{state} font, {note}"}}


SIGNIN_INK = rd("signin-link", "default", "color")  # rgba(100, 116, 139, 0.7)
_rgb = re.fullmatch(r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*[\d.]+\)", SIGNIN_INK)

core = {
    "color": {
        "slate": {
            "900": cm("hero-title", "default", "color", "hero and product titles (text-slate-900)"),
            "800": cm("nav-link", "hover", "color", "nav link hover ink"),
            "700": cm("help-link", "default", "color", "help link; also the carousel icon"),
            "600": cm("nav-link", "default", "color", "nav link and body copy (text-slate-600)"),
            "500": color("#%02x%02x%02x" % tuple(int(x) for x in _rgb.groups()),
                         f"{D}: the rgb of signin-link.default color {SIGNIN_INK}, alpha dropped"),
            "400": cm("help-link", "hover", "textDecorationColor", "the help link's hover underline"),
            "300": cm("help-link", "default", "textDecorationColor", "the help link's underline"),
            "200": color("#e2e8f0", recon("Tailwind slate-200, the step between 300 and 100")),
            "100": cm("code-block", "default", "backgroundColor", "code block fill (bg-slate-100)"),
            "50": cm("carousel-next", "hover", "backgroundColor", "carousel icon-button hover fill"),
        },
        "zinc": {
            "950": ca("title", "dialog title (text-xl tracking-tight)"),
            "800": cm("google-button", "default", "color", "sign-in card ink; also the email field"),
            "700": ca("body", "dialog body (text-zinc-700)"),
            "600": ca("caption", "dialog caption (text-zinc-600); also the Solutions menu item"),
            "500": color("#71717a", recon("Tailwind zinc-500, the dialog close icon; the icon was not measured")),
            "200": cm("google-button", "default", "borderTopColor", "the sign-in field hairline family"),
        },
        "gray": {
            "900": cm("faq", "default", "color", "FAQ summary ink"),
            "100": cm("faq", "default", "backgroundColor", "FAQ summary fill"),
        },
        "purple": {
            "500": cm("copy-button", "default", "backgroundColor", "Copy button; also the developer anchor (purple-500)"),
            "600": cm("copy-button", "hover", "backgroundColor", "Copy button hover"),
            "700": ca("link", "dialog mailto link (text-primary); also the sign-in Google button focus ring"),
            "appFrom": color(gradient_stop(0), f"{A}: raw/app-css-vars.json paintedOnDialog.okGradient, first stop"),
            "appTo": color(gradient_stop(1), f"{A}: raw/app-css-vars.json paintedOnDialog.okGradient, last stop"),
            "tint": cm("menu-item", "hover", "backgroundColor", "Solutions menu item hover fill"),
        },
        "white": cm("google-button", "default", "backgroundColor", "page, cards, Google button; also the dialog card"),
        "scrim": ca("overlay", "dialog overlay bg-black/30"),
        "ink": cm("collection-card", "default", "color", "help collection card text; also the focused search field"),
        "footer": cm("footer-link", "default", "color", "footer link on the dark footer band"),
        "navHover": cm("nav-link", "hover", "backgroundColor", "nav link and Solutions hover fill"),
        "focus": cm("nav-link", "focus-visible", "outlineColor", "browser focus-visible outline on links and buttons"),
    },
    "font": {
        "family": {
            "sans": font(
                "Greycliff, system-ui, -apple-system, Roboto, Open Sans, sans-serif",
                f"{M}: {at('nav-link', 'default', 'fontFamily')} is __greycliff (next/font); the hashed next/font names were "
                "renamed Greycliff by hand. The woff files are not shipped; the rest is the declared fallback.",
            ),
            "mono": font(rd("code-block", "default", "fontFamily").replace('"', ""),
                         f"{M}: {at('code-block', 'default', 'fontFamily')}, developer code samples"),
        },
        "weight": {
            "regular": wm("body-copy", "default", "body copy"),
            "medium": wm("signin-link", "default", "sign-in link; also the menu item and Google button"),
            "semibold": wm("nav-link", "default", "nav; also the hero title and help link"),
            "bold": wm("product-title", "default", "product title; also the wordmark, FAQ and section heading"),
        },
        "size": {
            "caption": dm("footer-link", "default", "fontSize", "footer link and code"),
            "menu": dm("menu-item", "default", "fontSize", "Solutions menu item"),
            "body": dm("nav-link", "default", "fontSize", "nav, buttons, fields"),
            "body-lg": dm("body-copy", "default", "fontSize", "letter body and FAQ"),
            "heading": dm("section-heading", "default", "fontSize", "section heading on /for/voice-recorder"),
            "display": dm("hero-title", "default", "fontSize", "hero and product titles"),
        },
        "lineHeight": {
            "display": dm("hero-title", "default", "lineHeight", "hero title line-height equals its 60px size"),
            "body": dm("nav-link", "default", "lineHeight", "16px body, 24px line"),
            "body-lg": dm("faq", "default", "lineHeight", "18px FAQ summary"),
        },
        "tracking": {
            "display": dm("hero-title", "default", "letterSpacing", "hero letter-spacing"),
        },
    },
    "space": {
        "1": dim("4px", recon("a step of the Tailwind 4px spacing unit")),
        "2": dm("nav-solutions", "default", "paddingTop", "Solutions button padding-block"),
        "3": dim("12px", recon("a step of the Tailwind 4px spacing unit")),
        "4": dm("nav-solutions", "default", "paddingLeft", "Solutions button padding-inline"),
        "5": dim("20px", recon("a step of the Tailwind 4px spacing unit")),
        "6": dm("letter-card", "default", "borderTopLeftRadius", "letter card radius; also the body line-height"),
        "8": dm("letter-card", "default", "paddingLeft", "letter card inline padding"),
        "10": dm("nav-link", "default", "height", "nav control height; also the carousel icon button"),
        "12": dm("google-button", "default", "height", "Google button height"),
        "16": dim("64px", recon("a step of the Tailwind 4px spacing unit")),
    },
    "radius": {
        "code": dm("code-block", "default", "borderTopLeftRadius", "code chip; also the Copy button"),
        "menu": dm("menu-item", "default", "borderTopLeftRadius", "Solutions menu item"),
        "control": dm("faq", "default", "borderTopLeftRadius", "FAQ summary; also the Google button and help card"),
        "search": dm("search-field", "default", "borderTopLeftRadius", "help search field"),
        "dialog": dim(DIALOG["cardRadius"], f"{A}: raw/app-css-vars.json paintedOnDialog.cardRadius, Sign Up Unavailable card (sm:rounded-xl)"),
        "card": dm("letter-card", "default", "borderTopLeftRadius", "letter card"),
        "pill": dm("nav-link", "default", "borderTopLeftRadius", "nav links, Solutions, carousel arrows"),
    },
    "border": {
        "hairline": dm("letter-card", "default", "outlineWidth", "the letter card's 1px outline"),
        "focus": dm("nav-link", "focus-visible", "outlineWidth", "focus-visible outline"),
    },
    "elevation": {
        "card": shadow("letter-card", "default", "letter and video cards (shadow-2xl / shadow-slate-800/15)"),
        "popover": {
            "$type": "shadow",
            "$value": [{"color": "rgba(15, 23, 42, 0.12)", "offsetX": "0px", "offsetY": "12px", "blur": "24px", "spread": "-8px"}],
            "$extensions": {"source": recon("the Solutions menu panel; the panel was not measured")},
        },
        "control": shadow("carousel-next", "default", "carousel icon button (shadow-md)"),
        "dialog": {
            "$type": "shadow",
            "$value": [
                {"color": "rgba(0, 0, 0, 0.1)", "offsetX": "0px", "offsetY": "10px", "blur": "15px", "spread": "-3px"},
                {"color": "rgba(0, 0, 0, 0.1)", "offsetX": "0px", "offsetY": "4px", "blur": "6px", "spread": "-4px"},
            ],
            "$extensions": {"source": recon("Tailwind shadow-lg for the dialog; the measured dialog card (raw/gated-dialog.json card) computes box-shadow none")},
        },
    },
    "layout": {
        "page": dim("1440px", recon("the desktop capture viewport width, not a product value")),
        "phone": dim("390px", recon("the phone capture viewport width, not a product value")),
        "content": dm("letter-card", "default", "width", "letter card width, max-w-5xl"),
        "prose": dm("hero-title", "default", "width", "hero title width, max-w-4xl"),
        "navHeight": dim("64px", recon("the top bar height; the bar was not measured")),
    },
}

# Type roles: one composite per measured element. Each field names the core token that holds the
# same reading where there is one, else carries the reading itself.
def _alias(group, value):
    for name, t in core["font"][group].items():
        if str(t["$value"]) == str(value):
            return "{font.%s.%s}" % (group, name)
    return value


def role(comp, state, family, note):
    t = typo(comp, state, family, note)
    v = t["$value"]
    v["fontSize"] = _alias("size", v["fontSize"])
    v["fontWeight"] = _alias("weight", v["fontWeight"])
    v["lineHeight"] = _alias("lineHeight", v["lineHeight"])
    if "letterSpacing" in v:
        v["letterSpacing"] = _alias("tracking", v["letterSpacing"])
    return t


core["typography"] = {
    "display": role("hero-title", "default", "{font.family.sans}", "h1 on the acquisition home"),
    "heading": role("section-heading", "default", "{font.family.sans}", "section h2 on /for/voice-recorder"),
    "body": role("roles-link", "default", "{font.family.sans}", "body default"),
    "body-lg": role("body-copy", "default", "{font.family.sans}", "letter paragraphs, text-lg leading-relaxed"),
    "label": role("nav-link", "default", "{font.family.sans}", "nav links"),
    "caption": role("footer-link", "default", "{font.family.sans}", "footer links"),
    "code": role("code-block", "default", "{font.family.mono}", "developer code samples"),
}
core = {k: core[k] for k in ("color", "font", "typography", "space", "radius", "border", "elevation", "layout")}

light = {
    "page": color("{color.white}", f"{M}: marketing page background"),
    "surface": color("{color.white}", f"{M}: letter card, help card, Google button"),
    "surfaceMuted": color("{color.gray.100}", f"{M}: FAQ summary"),
    "surfaceCode": color("{color.slate.100}", f"{M}: inline code"),
    "text": color("{color.slate.900}", f"{M}: titles"),
    "textBody": color("{color.slate.600}", f"{M}: letter and nav"),
    "textMuted": color(norm_color(SIGNIN_INK), f"{M}: {at('signin-link', 'default', 'color')}, Sign In link"),
    "textOnAccent": color("{color.white}", f"{M}: Copy button label"),
    "link": color("{color.purple.500}", f"{M}: developer anchors"),
    "accent": color("{color.purple.500}", f"{M}: Copy, wordmark, Join #developers"),
    "accentHover": color("{color.purple.600}", f"{M}: Copy hover"),
    "navHover": color("{color.navHover}", f"{M}: nav hover wash"),
    "focus": color("{color.focus}", f"{M}: focus-visible outline"),
    "border": color("{color.slate.200}", "alias of the hand-entered color.slate.200; no card hairline reading holds it"),
    "footerInk": color("{color.footer}", f"{M}: footer links"),
    "helpBand": color("#8a54e1", recon("the help center's purple header band; no raw file holds it")),
    "overlay": color("{color.scrim}", f"{A}: fixed inset overlay bg-black/30"),
    "scrim": color("{color.scrim}", f"{A}: same overlay, the dim behind the dialog"),
    "appInk": color("{color.zinc.950}", f"{A}: dialog title"),
    "appLink": color("{color.purple.700}", f"{A}: support mailto on the dialog"),
    "appAccentFrom": color("{color.purple.appFrom}", f"{A}: OK fill gradient start"),
    "appAccentTo": color("{color.purple.appTo}", f"{A}: OK fill gradient end"),
}

# Alias check
def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)

names = {n for n, _ in walk(core)}
names |= {n for n, _ in walk(light)}
import re
def alias_ok(alias):
    if alias in names:
        return True
    # {color.slate.900} is core.color.slate.900
    return alias.startswith("color.") and alias in names

def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)

for path, tok in list(walk({"core": core, "light": light})):
    for blob in strings(tok["$value"]):
        for alias in re.findall(r"\{([^{}]+)\}", blob):
            if not alias_ok(alias):
                raise SystemExit(f"{path} alias {{{alias}}} missing")

if MOTION:
    core["motion"], extra = motion_mod.build(MOTION)
    if extra:
        core["motion"].setdefault("$extensions", {})["notTokenised"] = extra

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only painted theme on captured Limitless surfaces, 2026-11-18 (marketing plus the app sign-in dialog).",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("tokens", len(names))
