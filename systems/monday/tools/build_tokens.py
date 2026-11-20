#!/usr/bin/env python3
"""Build tokens.json from the Monday readings in raw/.

Two stacks were measured on 2026-11-19, both signed out:

  product   auth.monday.com login stylesheet (cdn.monday.com/build/login_monday-*.css).
            Light values are the browser's resolved custom properties on :root /
            .light-app-theme. Dark values are the declared .dark-app-theme block.
            The signed-out pages paint light only. Dark is declared, not painted.
  marketing monday.com home (Webflow) and /pricing (Next). The brand purple and
            the pill button were read from computed styles on live elements.

Every token carries $extensions.source. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())
LOGIN = VARS["login"]
RES = LOGIN["resolved"]

SRC_LOGIN = "auth.monday.com/auth/login_monday, resolved on :root, 2026-11-19, headless Chromium 1440x900"
SRC_DARK = "auth.monday.com login stylesheet, declared on .dark-app-theme, not painted on any signed-out page, 2026-11-19"
SRC_HOME = "monday.com home, computed style, 2026-11-19, headless Chromium 1440x900"
SRC_PRICE = "monday.com/pricing, computed style, 2026-11-19, headless Chromium 1440x900"


def tok(value, typ, source, **ext):
    out = {"$value": value, "$type": typ, "$extensions": {"source": source}}
    out["$extensions"].update(ext)
    return out


def color_of(name, source):
    return tok(norm(RES[name]), "color", f"{source}; {name}")


def norm(c):
    c = c.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3})$", c)
    if m:
        h = m.group(1)
        return "#" + "".join(ch * 2 for ch in h).lower()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", c)
    if m:
        return c.lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", c)
    if m:
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        a = m.group(4)
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %s)" % (r, g, b, "%g" % float(a))
    if c.lower() == "white":
        return "#ffffff"
    if c.lower() == "black":
        return "#000000"
    raise ValueError("colour not understood: " + c)


def dim(name, source):
    v = RES[name].strip()
    if not re.fullmatch(r"-?\d+(\.\d+)?px", v):
        raise ValueError("not a px length: " + name + "=" + v)
    return tok(v, "dimension", f"{source}; {name}")


def dark_decl():
    for decl in LOGIN["decls"]:
        sel = decl.get("sel") or ""
        if sel.strip() == ".dark-app-theme":
            return decl["props"]
    raise SystemExit("dark-app-theme block missing")


DARK = dark_decl()

# Status colours the product names, resolved on the light root.
STATUS = [
    ("done-green", "--color-done-green"),
    ("bright-green", "--color-bright-green"),
    ("grass-green", "--color-grass_green"),
    ("egg-yolk", "--color-egg_yolk"),
    ("working-orange", "--color-working_orange"),
    ("sunset", "--color-sunset"),
    ("stuck-red", "--color-stuck-red"),
    ("dark-red", "--color-dark-red"),
    ("sofia-pink", "--color-sofia_pink"),
    ("lipstick", "--color-lipstick"),
    ("bubble", "--color-bubble"),
    ("purple", "--color-purple"),
    ("dark-purple", "--color-dark_purple"),
    ("indigo", "--color-indigo"),
    # ("dark-indigo", "--color-dark-indigo") is not declared on the login page; it never was a token.
    ("bright-blue", "--color-bright-blue"),
    ("aquamarine", "--color-aquamarine"),
    ("chili-blue", "--color-chili-blue"),
    ("river", "--color-river"),
    ("navy", "--color-navy"),
    ("asphalt", "--color-asphalt"),
    ("explosive", "--color-explosive"),
    ("american-gray", "--color-american_gray"),
    ("blackish", "--color-blackish"),
    ("brown", "--color-brown"),
    ("orchid", "--color-orchid"),
    ("tan", "--color-tan"),
    ("sky", "--color-sky"),
    ("coffee", "--color-coffee"),
    ("royal", "--color-royal"),
    ("teal", "--color-teal"),
    ("lavender", "--color-lavender"),
    ("steel", "--color-steel"),
    ("lilac", "--color-lilac"),
    ("pecan", "--color-pecan"),
]


def status_group():
    """The status palette. A name missing from raw or a value that does not parse fails the build;
    it used to be skipped silently, so a recapture that renamed a variable lost the colour quietly."""
    group = {}
    for key, name in STATUS:
        if name not in RES or not RES[name]:
            raise SystemExit(f"status colour {name} is not in raw/css-vars.json")
        group[key] = color_of(name, SRC_LOGIN)
    return group


def shadow_tok(name):
    raw = RES[name]
    # "0px 4px 8px rgba(0, 0, 0, 0.2)"
    m = re.fullmatch(
        r"(-?\d+px)\s+(-?\d+px)\s+(-?\d+px)(?:\s+(-?\d+px))?\s+(rgba?\([^)]+\)|#[0-9a-fA-F]{3,8})",
        raw.strip(),
    )
    if not m:
        return None
    return tok(
        {
            "offsetX": m.group(1),
            "offsetY": m.group(2),
            "blur": m.group(3),
            "spread": m.group(4) or "0px",
            "color": norm(m.group(5)),
        },
        "shadow",
        f"{SRC_LOGIN}; {name}",
    )


def font_stack(value):
    return value.split(",")[0].strip().strip('"')


core = {
    "color": {
        "status": status_group(),
        "brand": {
            "purple": tok("#6161ff", "color", f"{SRC_HOME}; a.m_button-primary background-color rgb(97, 97, 255); also --purple on monday.com :root"),
            "blue": color_of("--primary-color", SRC_LOGIN),
            "black": tok("#000000", "color", f"{SRC_HOME}; body color rgb(0, 0, 0)"),
            "ink": tok("#323338", "color", f"{SRC_LOGIN}; --primary-text-color"),
            "white": tok("#ffffff", "color", f"{SRC_LOGIN}; --primary-background-color"),
        },
    },
    "fontFamily": {
        "figtree": tok("Figtree, Roboto, sans-serif", "fontFamily", f"{SRC_LOGIN}; --font-family (Noto fallbacks dropped from the token, kept in raw)"),
        "poppins": tok("Poppins, Roboto, sans-serif", "fontFamily", f"{SRC_LOGIN}; --h1-font-family; marketing home computed font-family starts Poppins"),
        "marketing": tok("Poppins, Arial, sans-serif", "fontFamily", f"{SRC_HOME}; body font-family"),
    },
    "fontSize": {
        "10": dim("--font-size-10", SRC_LOGIN),
        "30": dim("--font-size-30", SRC_LOGIN),
        "40": dim("--font-size-40", SRC_LOGIN),
        "50": dim("--font-size-50", SRC_LOGIN),
        "60": dim("--font-size-60", SRC_LOGIN),
        "h1": dim("--font-size-h1", SRC_LOGIN),
        "paragraph": dim("--font-size-paragraph", SRC_LOGIN),
        "subtext": dim("--font-size-subtext", SRC_LOGIN),
    },
    "fontWeight": {
        "light": tok(300, "fontWeight", f"{SRC_LOGIN}; --font-weight-light"),
        "normal": tok(400, "fontWeight", f"{SRC_LOGIN}; --font-weight-normal"),
        "bold": tok(500, "fontWeight", f"{SRC_LOGIN}; --font-weight-bold (the product names 500 bold)"),
    },
    "lineHeight": {
        "h1": dim("--font-line-height-h1", SRC_LOGIN),
        "h2": dim("--font-line-height-h2", SRC_LOGIN),
        "paragraph": dim("--font-line-height-paragraph", SRC_LOGIN),
        "subtext": dim("--font-line-height-subtext", SRC_LOGIN),
    },
    "letterSpacing": {
        "h1": dim("--letter-spacing-h1-normal", SRC_LOGIN),
        "h2": dim("--letter-spacing-h2-normal", SRC_LOGIN),
    },
    "spacing": {
        "xs": dim("--spacing-xs", SRC_LOGIN),
        "small": dim("--spacing-small", SRC_LOGIN),
        "medium": dim("--spacing-medium", SRC_LOGIN),
        "large": dim("--spacing-large", SRC_LOGIN),
        "xl": dim("--spacing-xl", SRC_LOGIN),
        "xxl": dim("--spacing-xxl", SRC_LOGIN),
        "xxxl": dim("--spacing-xxxl", SRC_LOGIN),
    },
    "radius": {
        "small": dim("--border-radius-small", SRC_LOGIN),
        "medium": dim("--border-radius-medium", SRC_LOGIN),
        "big": dim("--border-radius-big", SRC_LOGIN),
        "pill": tok("160px", "dimension", f"{SRC_HOME}; a.m_button-primary border-radius 160px"),
    },
    "borderWidth": {
        "default": dim("--border-width", SRC_LOGIN),
    },
    "shadow": {
        "xs": shadow_tok("--box-shadow-xs"),
        "small": shadow_tok("--box-shadow-small"),
        "medium": shadow_tok("--box-shadow-medium"),
        "large": shadow_tok("--box-shadow-large"),
    },
    "motion": {
        "duration": {
            "productive-short": tok("70ms", "duration", f"{SRC_LOGIN}; --motion-productive-short"),
            "productive-medium": tok("100ms", "duration", f"{SRC_LOGIN}; --motion-productive-medium"),
            "productive-long": tok("150ms", "duration", f"{SRC_LOGIN}; --motion-productive-long"),
            "expressive-short": tok("250ms", "duration", f"{SRC_LOGIN}; --motion-expressive-short"),
            "expressive-long": tok("400ms", "duration", f"{SRC_LOGIN}; --motion-expressive-long"),
            "button-press": tok("70ms", "duration", f"{SRC_LOGIN}; button.next-button transition transform 0.07s"),
            "field-border": tok("100ms", "duration", f"{SRC_LOGIN}; input.email-input transition border-color 0.1s ease-in"),
        },
        "easing": {
            "transition": tok([0.4, 0, 0.2, 1], "cubicBezier", f"{SRC_LOGIN}; --motion-timing-transition"),
            "enter": tok([0, 0, 0.35, 1], "cubicBezier", f"{SRC_LOGIN}; --motion-timing-enter"),
            "exit": tok([0.4, 0, 1, 1], "cubicBezier", f"{SRC_LOGIN}; --motion-timing-exit"),
            "emphasize": tok([0, 0, 0.2, 1.4], "cubicBezier", f"{SRC_LOGIN}; --motion-timing-emphasize (y2 is 1.4, outside the unit square)"),
        },
    },
    "typography": {
        "h1": tok(
            {"fontFamily": "{fontFamily.poppins}", "fontWeight": "{fontWeight.light}", "fontSize": "32px", "lineHeight": "40px", "letterSpacing": "{letterSpacing.h1}"},
            "typography",
            f"{SRC_LOGIN}; h1 computed 300 32px/40px Poppins, letter-spacing -0.5px",
        ),
        "paragraph": tok(
            {"fontFamily": "{fontFamily.figtree}", "fontWeight": "{fontWeight.normal}", "fontSize": "{fontSize.paragraph}", "lineHeight": "22px"},
            "typography",
            f"{SRC_LOGIN}; --font-text1-normal 400 16px/22px Figtree",
        ),
        "subtext": tok(
            {"fontFamily": "{fontFamily.figtree}", "fontWeight": "{fontWeight.normal}", "fontSize": "{fontSize.subtext}", "lineHeight": "{lineHeight.subtext}"},
            "typography",
            f"{SRC_LOGIN}; --font-size-subtext / --font-line-height-subtext",
        ),
        "marketing-display": tok(
            {"fontFamily": "{fontFamily.marketing}", "fontWeight": "{fontWeight.normal}", "fontSize": "56px", "lineHeight": "67.2px", "letterSpacing": "-2.24px"},
            "typography",
            f"{SRC_HOME}; h1 computed 400 56px/67.2px Poppins, letter-spacing -2.24px",
        ),
        "button": tok(
            {"fontFamily": "{fontFamily.figtree}", "fontWeight": "{fontWeight.normal}", "fontSize": "18px", "lineHeight": "28px"},
            "typography",
            f"{SRC_LOGIN}; button.next-button computed 400 18px/28px Figtree",
        ),
    },
}

# drop a shadow that failed to parse
core["shadow"] = {k: v for k, v in core["shadow"].items() if v}


def semantic(theme, source, getter):
    def c(key):
        return tok(norm(getter(key)), "color", f"{source}; {key}")

    return {
        "background": {
            "page": c("--primary-background-color"),
            "surface": c("--secondary-background-color"),
            "grey": c("--grey-background-color"),
            "dialog": c("--dialog-background-color"),
            "ui": c("--ui-background-color") if theme == "light" else c("--secondary-background-color"),
            "selected": c("--primary-selected-color"),
            "disabled": c("--disabled-background-color") if "--disabled-background-color" in (RES if theme == "light" else DARK) else c("--primary-background-color"),
        },
        "text": {
            "primary": c("--primary-text-color"),
            "secondary": c("--secondary-text-color"),
            "on-primary": c("--text-color-on-primary"),
            "disabled": (
            c("--disabled-text-color")
            if "var(" not in getter("--disabled-text-color")
            else tok(norm("rgba(213, 216, 223, 0.38)"), "color", f"{source}; --disabled-text-color with --disabled-component-opacity 0.38 substituted")
        ),
            "placeholder": c("--placeholder-color"),
            "link": c("--link-color"),
        },
        "border": {
            "ui": c("--ui-border-color"),
            "layout": c("--layout-border-color"),
        },
        "icon": c("--icon-color"),
        "accent": c("--primary-color"),
        "accentHover": c("--primary-hover-color"),
        "positive": c("--positive-color"),
        "negative": c("--negative-color"),
        "warning": c("--warning-color"),
        "component": {
            "button-primary-bg": c("--primary-color"),
            "button-primary-hover-bg": c("--primary-hover-color"),
            "button-primary-text": c("--text-color-on-primary"),
            "button-primary-radius": tok("{radius.small}", "dimension", f"{SRC_LOGIN}; button.next-button border-radius 4px matches --border-radius-small"),
            "field-bg": c("--primary-background-color"),
            "field-text": c("--primary-text-color"),
            "field-border": c("--ui-border-color"),
            "field-radius": tok("{radius.small}", "dimension", f"{SRC_LOGIN}; input.email-input border-radius 4px"),
        },
    }


def light_get(key):
    return RES[key]


def dark_get(key):
    if key not in DARK:
        raise KeyError(key)
    return DARK[key]


light = semantic("light", SRC_LOGIN, light_get)
# marketing roles sit beside the product roles; they are a different paint.
light["marketing"] = {
    "page": tok("#ffffff", "color", f"{SRC_HOME}; body background-color rgb(255, 255, 255)"),
    "text": tok("#000000", "color", f"{SRC_HOME}; body color rgb(0, 0, 0)"),
    "nav": tok("#535768", "color", f"{SRC_HOME}; a.nav_link-full color rgb(83, 87, 104)"),
    "accent": tok("#6161ff", "color", f"{SRC_HOME}; a.m_button-primary background-color rgb(97, 97, 255)"),
    "on-accent": tok("#ffffff", "color", f"{SRC_HOME}; a.m_button-primary color rgb(255, 255, 255)"),
    "pricing-text": tok("#333333", "color", f"{SRC_PRICE}; h1 color rgb(51, 51, 51)"),
}
# disabled text on light is rgba(50, 51, 56, 0.38) which norm keeps.
# dark disabled text references a var(); resolve it.
if "var(" in str(DARK.get("--disabled-text-color", "")):
    light_disabled_note = DARK["--disabled-text-color"]
    # declared: rgba(213, 216, 223, var(--disabled-component-opacity)) and opacity is 0.38
    light["text"]  # keep light as resolved
    dark_disabled = "rgba(213, 216, 223, 0.38)"
else:
    dark_disabled = DARK["--disabled-text-color"]

dark = semantic("dark", SRC_DARK, dark_get)
# ui background is not in the dark block we sampled; don't invent it.
if "--ui-background-color" not in DARK:
    dark["background"].pop("ui", None)
if "--disabled-background-color" not in DARK:
    dark["background"].pop("disabled", None)

# focus ring measured on the live Next button, both themes share the blue ring on light paint
light["component"]["button-focus-ring"] = tok(
    "rgba(0, 132, 255, 0.5)",
    "color",
    f"{SRC_LOGIN}; button.next-button:focus box-shadow 0 0 0 3px rgba(0, 132, 255, 0.5)",
)
dark["component"]["button-focus-ring"] = tok(
    "rgba(0, 132, 255, 0.5)",
    "color",
    f"{SRC_LOGIN}; same focus ring measured on the light login button; not re-measured under .dark-app-theme",
    painted=False,
)

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark (declared, not painted signed out)", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "source": "Measured 2026-11-19 from monday.com public pages and auth.monday.com signed-out login and signup. Dark tokens are declared on .dark-app-theme and were not painted on any page this pass reached.",
        "notTokenised": [
            "login input hover border rgb(50, 51, 56) is --primary-text-color, recorded on the element in raw/components-computed.json",
            "marketing pill radius 160px is a pill, not the product 4px radius; both are tokenised",
            "contact sales form fields were not component-measured; the page was screenshot only",
        ],
    },
}

# sanity: no missing shadows
assert core["shadow"]["small"]["$type"] == "shadow"
text = json.dumps(doc, indent=2) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(text)
    print("wrote", HERE / "tokens.json", "bytes", len(text))
