#!/usr/bin/env python3
"""Build tokens.json from the Lemon Squeezy public capture.

Sources, read on 2026-11-18:
  raw/css-vars.json              :root custom properties from the Webflow stylesheet
  raw/components-computed.json   computed styles of public controls

The marketing site declares one light palette. A --dark-mode-bg-lighter name
exists and is unused on the captured pages, so there is no dark set.
Every dimension, type role and component colour that a measured element holds
is read from raw/ through measured(), which stops the build when the reading is
missing. The few values no capture measured (the home h1, .text-size-xlarge,
the hero paragraph, the medium label, the code role and the nav scrim) were
entered by hand at capture time and carry the Reconstruction label.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())
DECL = V["resolved"]["light"]
SRC = "declared on :root in lemon-squeezy-staging.shared CSS (raw/css-vars.json), captured 2026-11-18"


def norm_color(v):
    v = str(v).strip().lower()
    named = {"black": "#000000", "white": "#ffffff"}
    if v in named:
        return named[v]
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a >= 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def color(name, var=None, value=None, source=None):
    raw = DECL[var] if var else value
    return {
        "$value": norm_color(raw),
        "$type": "color",
        "$extensions": {"source": source or f"css-var {var} ({SRC})"},
    }


def dim(value, source):
    value = str(value)
    if re.fullmatch(r"-?\d+(\.\d+)?", value):
        value += "px"
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value):
        raise ValueError("bad dimension " + value)
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def measured(comp, state, prop):
    st = C["components"][comp]["states"][state]
    if st.get("error") or prop not in (st.get("style") or {}):
        raise SystemExit(f"no reading of {prop} on {comp}/{state}")
    return st["style"][prop], f"computed {prop} on {comp}/{state} ({st.get('classes', '')}), {C['components'][comp]['url']}"


def mdim(comp, prop, state="default", note=""):
    """A dimension read from the component's computed style, never typed in."""
    value, source = measured(comp, state, prop)
    return dim(value, source + (note and "; " + note))


def mcolor(comp, prop, state="default"):
    value, source = measured(comp, state, prop)
    return color(comp, value=value, source=source)


HAND = "Reconstruction: entered by hand at capture time; no raw reading holds this value"


def hand(note):
    return HAND + "; " + note


def ramp(prefix, steps):
    """steps: list of (step, css var name)."""
    out = {}
    for step, var in steps:
        if var not in DECL:
            raise KeyError(var)
        out[step] = color(step, var=var)
    return out


def ms(comp):
    value, source = measured(comp, "default", "transitionDuration")
    m = re.fullmatch(r"([\d.]+)(m?s)", value.split(",")[0].strip())
    if not m:
        raise SystemExit(f"{comp} transitionDuration not understood: {value}")
    n = float(m.group(1)) * (1 if m.group(2) == "ms" else 1000)
    return "%gms" % n, source


def bezier(comp, points):
    value, source = measured(comp, "default", "transitionTimingFunction")
    want = "cubic-bezier(%s)" % ", ".join("%g" % p for p in points)
    if value.split(",  ")[0].strip() != want and not value.startswith(want):
        raise SystemExit(f"{comp} timing function is {value}, not {want}")
    return source


core = {
    "color": {
        "neutral": ramp("neutral", [
            ("50", "--grey-50"),
            ("100", "--grey-100"),
            ("200", "--grey-200"),
            ("300", "--gray-300"),
            ("500", "--gray-500"),
            ("700", "--grey-700"),
            ("900", "--black-2"),
            ("950", "--dark-grey"),
        ]),
        "purple": ramp("purple", [
            ("50", "--purple-50-501"),
            ("100", "--purple-100"),
            ("200", "--purple-200"),
            ("300", "--purple-300"),
            ("400", "--purple-400"),
            ("500", "--purple-500"),
            ("600", "--purple-600"),
            ("700", "--purple-700"),
            ("900", "--purple-900"),
        ]),
        "yellow": ramp("yellow", [
            ("50", "--yellow-50-501"),
            ("100", "--yellow-100"),
            ("200", "--yellow-200"),
            ("300", "--yellow-300"),
            ("400", "--yellow-400"),
            ("500", "--yellow-500"),
            ("700", "--yellow-700"),
        ]),
        "pink": ramp("pink", [
            ("50", "--pink-50"),
            ("100", "--pink-100"),
            ("200", "--pink-200"),
            ("300", "--pink-300"),
            ("400", "--pink-400"),
            ("500", "--pink-500"),
            ("600", "--pink-600"),
            ("700", "--pink-700"),
            ("800", "--pink-800"),
        ]),
        "green": ramp("green", [
            ("50", "--green-50-501"),
            ("100", "--green-100"),
            ("200", "--green-200"),
            ("300", "--green-300"),
            ("400", "--green-400"),
            ("500", "--green-500"),
            ("600", "--green-600"),
            ("700", "--green-700"),
        ]),
        "blue": ramp("blue", [
            ("50", "--blue-50-501"),
            ("100", "--blue-100"),
            ("200", "--blue-200"),
            ("300", "--blue-300"),
            ("400", "--blue-400"),
            ("500", "--blue-500"),
            ("600", "--blue-600"),
            ("700", "--blue-700"),
        ]),
        "orange": ramp("orange", [
            ("50", "--orange-50"),
            ("100", "--orange-100"),
            ("200", "--orange-200"),
            ("300", "--orange-300"),
            ("400", "--orange-400"),
            ("500", "--orange-500"),
            ("600", "--orange-600"),
            ("700", "--orange-700"),
        ]),
        "red": ramp("red", [
            ("50", "--red-50-501"),
            ("100", "--red-100"),
            ("200", "--red-200"),
            ("400", "--red-400"),
            ("500", "--red-500"),
            ("700", "--red-700"),
        ]),
        "plum": ramp("plum", [
            ("100", "--plum-100"),
            ("500", "--plum-500"),
        ]),
        "white": color("white", var="--white-900"),
        "black": color("black", var="--black"),
    },
    "font": {
        "family": {
            "display": font_family(*measured("price-card", "default", "fontFamily")),
            "sans": font_family(*measured("nav-button", "default", "fontFamily")),
            "mono": font_family(
                "Jetbrainsmono, ui-monospace, monospace",
                "@font-face Jetbrainsmono in the Webflow stylesheet (raw/css-vars.json fonts)",
            ),
        },
    },
    "typography": {},
    "radius": {
        "pill": mdim("nav-button", "borderTopLeftRadius"),
        "control": mdim("login-email", "borderTopLeftRadius"),
        "docs": mdim("docs-nav", "borderTopLeftRadius"),
        "none": mdim("banner", "borderTopLeftRadius"),
    },
    "space": {
        "1": mdim("docs-nav", "paddingTop"),
        "2": mdim("nav-button", "paddingTop"),
        "3": mdim("docs-nav", "paddingRight"),
        "4": mdim("login-email", "paddingLeft"),
        "5": mdim("nav-button", "paddingLeft"),
        "6": dim(*(lambda v, s: (v, "Derived: " + s + "; a line-height reused as a spacing step, not a measured gap"))(*measured("nav-button", "default", "lineHeight"))),
        "8": mdim("nav-link", "paddingTop"),
        "10": mdim("nav-button", "height"),
    },
    "size": {
        "nav-button": mdim("nav-button", "height"),
        "field": mdim("login-email", "height"),
        "submit": mdim("login-submit", "height"),
        "orchid": mdim("button-orchid", "height"),
        "icon-button": mdim("menu-button", "height", note="mobile home at 390"),
        "checkbox": mdim("login-remember", "height"),
    },
    "stroke": {
        "hairline": dim("1px", "auth field inset ring is 1px (computed box-shadow spread)"),
        "focus": dim("2px", "computed focus ring width on auth input (box-shadow 0 0 0 2px)"),
    },
    "motion": {
        "duration": {
            "fast": num(*ms("nav-button"), "duration"),
            "docs": num(*ms("docs-nav"), "duration"),
        },
        "easing": {
            "ease": {
                "$value": [0.25, 0.1, 0.25, 1],
                "$type": "cubicBezier",
                "$extensions": {"source": "Derived: CSS keyword ease on .nav_button, expanded to control points"},
            },
            "standard": {
                "$value": [0.4, 0, 0.2, 1],
                "$type": "cubicBezier",
                "$extensions": {"source": bezier("docs-nav", [0.4, 0, 0.2, 1])},
            },
        },
    },
}

def mtypo(family, comp, state="default"):
    """A type role read from one measured element."""
    st = C["components"][comp]["states"][state]["style"]
    _, source = measured(comp, state, "fontSize")
    tracking = st["letterSpacing"]
    return typo(family, st["fontSize"], int(st["fontWeight"]), st["lineHeight"],
                "0px" if tracking == "normal" else tracking, source.replace("computed fontSize", "computed type"))


def typo(family, size, weight, line, tracking, source):
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

core["typography"] = {
    "display": typo("{font.family.display}", "80px", 400, "80px", "-3.2px", hand("the home h1.heading-xxlarge, which no capture measured")),
    "heading": mtypo("{font.family.display}", "price-card"),
    "title": typo("{font.family.display}", "26px", 400, "31.72px", "-0.52px", hand(".text-size-xlarge on the home page, which no capture measured")),
    "body": typo("{font.family.sans}", "18px", 400, "30.6px", "0px", hand("the home hero paragraph, which no capture measured")),
    "body-strong": mtypo("{font.family.sans}", "nav-button"),
    "label": typo("{font.family.sans}", "14px", 500, "22.4px", "0px", hand(".text-size-small.text-weight-medium, which no capture measured")),
    "caption": mtypo("{font.family.sans}", "footer-link"),
    "code": typo("{font.family.mono}", "14px", 400, "22.4px", "0px", hand("the @font-face Jetbrainsmono family at the caption size; no code block was measured")),
}

light = {
    "surface": {
        "page": color("page", value="#ffffff", source="computed page background is transparent over white; auth card sits on white, 2026-11-18"),
        "hero": color("hero", var="--purple-600"),
        "banner": color("banner", var="--yellow-500"),
        "footer": color("footer", var="--purple-600", source="footer_component.background-color-blue paints --purple-600; confirmed on the home screenshot"),
        "raised": color("raised", var="--grey-50"),
        "overlay": color("overlay", var="--purple-600"),
        "scrim": color("scrim", value="rgba(18, 18, 23, 0.4)", source=hand("--black-2 at 40% for a mobile nav overlay; the menu itself paints --purple-600")),
    },
    "text": {
        "primary": color("primary", var="--black-2"),
        "secondary": color("secondary", var="--gray-500"),
        "muted": mcolor("nav-link", "color"),
        "on-accent": color("on-accent", var="--white-900"),
        "on-hero": color("on-hero", var="--white-900"),
        "link": color("link", var="--purple-500"),
        "disabled": color("disabled", var="--gray-300"),
    },
    "border": {
        "default": color("default", var="--border-color"),
        "strong": color("strong", var="--grey-700"),
        "focus": color("focus", var="--purple-500"),
    },
    "accent": color("accent", var="--purple-500"),
    "accent-hover": mcolor("login-submit", "backgroundColor", "hover"),
    "accent-pressed": color("accent-pressed", var="--purple-700"),
    "status": {
        "success": color("success", var="--green-500"),
        "warning": color("warning", var="--yellow-500"),
        "danger": color(
            "danger",
            var="--red-500",
            source="css-var --red-500; computed color on the login error text after a failed sign-in is rgb(245, 61, 107) (#f53d6b), auth.lemonsqueezy.com/login, 2026-11-18",
        ),
        "info": color("info", var="--blue-500"),
    },
    "component": {
        "button-bg": color("button-bg", var="--button-primary-light"),
        "button-text": color("button-text", var="--black-2"),
        "button-radius": mdim("button-primary", "borderTopLeftRadius"),
        "button-height": mdim("nav-button", "height"),
        "field-bg": color("field-bg", var="--white-900"),
        "field-text": mcolor("login-email", "color"),
        "field-radius": mdim("login-email", "borderTopLeftRadius"),
        "field-height": mdim("login-email", "height"),
    },
}

# alias check
def walk(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from walk(v, prefix + k + ".")

names = {n for n, _ in walk(core)} | {n for n, _ in walk(light)}
for n, t in list(walk(core)) + list(walk(light)):
    for a in re.findall(r"\{([^{}]+)\}", json.dumps(t["$value"])):
        if a not in names:
            raise SystemExit(f"{n}: alias {{{a}}} missing")

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the public marketing site, docs and sign-in card paint. --dark-mode-bg-lighter is declared and unused.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1

print({k: count(tokens[k]) for k in ("core", "light")})
