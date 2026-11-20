#!/usr/bin/env python3
"""Write tokens.json from raw/readings.json.

Every colour and length below was read on 2026-11-19 from the public
signed-out pages (computed style in the T3 preview tab, or a custom property
in https://www.time2book.me/_astro/base.BIUhdRuW.css resolved to sRGB in that
same page). A value that was not on the page is not invented here.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
HEX = RAW["hexFromCanvas"]


def tok(value, ty, evidence, where, **extra):
    if evidence is S:  # declared in the stylesheet raw/readings.json names: a Measured declaration
        evidence, extra = M, {"stylesheet": RAW["stylesheet"], **extra}
    source = {"evidence": evidence, "where": where}
    source.update(extra)
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def color(value, evidence, where, **extra):
    return tok(value, "color", evidence, where, **extra)


def dim(value, evidence, where, **extra):
    return tok(value, "dimension", evidence, where, **extra)


def ref(value, evidence, where):
    return tok(value, "dimension", evidence, where)


M = "Measured"
D = "Derived"
R = "Reconstruction"
S = object()  # a declaration read from the stylesheet; tok() writes it as Measured, naming the sheet

LIGHT = "computed style on https://www.time2book.me/ and https://time2book.me/login, 2026-11-19"
ROOT = ":root custom property in _astro/base.BIUhdRuW.css, resolved to sRGB in the T3 page"
DARK = ".dark custom property in the same sheet, resolved to sRGB in the T3 page. No public page applied .dark."

core = {
    "font": {
        "family": {
            "sans": tok(
                '"Inter Variable", ui-sans-serif, system-ui, sans-serif',
                "fontFamily", M, "document.body font-family",
            ),
            "mono": tok(
                'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
                "fontFamily", S, "--font-mono on :root. Not used on the public pages.",
            ),
        }
    },
    "fontWeight": {
        "regular": tok(400, "fontWeight", M, "body and eyebrow computed font-weight"),
        "medium": tok(500, "fontWeight", M, "display heading, nav link and primary button"),
        "semibold": tok(600, "fontWeight", R, "Entered by hand at capture time from --font-weight-semibold; no raw/ file holds this reading. Not seen on a public text node."),
    },
    "fontSize": {
        "legal": dim("12px", M, "signup Terms of Service link"),
        "nav": dim("14px", M, "nav Pricing link"),
        "body": dim("16px", M, "document.body"),
        "auth-title": dim("18px", M, "login 'Sign in to your account'"),
        "step": dim("20px", M, "feature page 'Add group classes'"),
        "card-title": dim("24px", M, "solution card title on a photo"),
        "feature": dim("30px", M, "feature page h3, desktop"),
        "section": dim("36px", M, "home section h2, desktop"),
        "display": dim("48px", M, "home hero h2 and pricing h1, desktop 1440"),
        "price": dim("40px", M, "pricing '$19.50'"),
    },
    "lineHeight": {
        "legal": dim("15px", M, "signup legal link bounding height at 12px"),
        "nav": dim("21px", M, "14px nav link"),
        "auth": dim("20px", M, "login field and OAuth button"),
        "body": dim("24px", M, "document.body"),
        "eyebrow": dim("25.6px", M, "16px eyebrow, leading 1.6"),
        "card-title": dim("26.4px", M, "24px card title, leading 1.1"),
        "auth-title": dim("28px", M, "18px auth title"),
        "step": dim("30px", M, "20px step heading"),
        "section": dim("39.6px", M, "36px section heading, leading 1.1"),
        "display": dim("52.8px", M, "48px display, leading 1.1"),
    },
    "letterSpacing": {
        "display": dim("-0.96px", M, "48px heading, tracking -0.02em"),
        "section": dim("-0.72px", M, "36px heading, tracking -0.02em"),
        "card-title": dim("-0.48px", M, "24px card title, tracking -0.02em"),
        "eyebrow": dim("0.16px", M, "16px eyebrow, tracking 0.01em"),
        "nav": dim("0px", M, "nav link tracking-[0em]"),
    },
    "radius": {
        "none": dim("0px", M, "page, nav and promo bar"),
        "control": dim("12px", M, "login field, OAuth button, search icon button"),
        "card": dim("16px", M, "pricing plan card and solution card class"),
        "pill": dim("100px", M, "marketing buttons, nav links, segment track"),
    },
    "spacing": {
        "2": dim("2px", M, "segment track padding"),
        "8": dim("8px", M, "search button padding and watch button gap"),
        "10": dim("10px", M, "login field vertical padding"),
        "12": dim("12px", M, "promo bar vertical padding and nav link horizontal padding"),
        "14": dim("14px", M, "login field horizontal padding"),
        "16": dim("16px", M, "nav vertical padding, primary nav button horizontal padding, pricing card column padding"),
        "18": dim("18px", M, "watch button right padding"),
        "20": dim("20px", M, "primary CTA horizontal padding and login button horizontal padding"),
        "24": dim("24px", M, "pricing plan card padding"),
        "32": dim("32px", M, "promo bar horizontal padding"),
        "40": dim("40px", M, "auth column horizontal padding"),
        "80": dim("80px", M, "home section and footer vertical padding"),
        "128": dim("128px", M, "auth column vertical padding at 1440"),
    },
    "size": {
        "segment-thumb": dim("34px", M, "Monthly/Yearly selected thumb"),
        "nav-control": dim("38px", M, "nav link, Log in, Sign up"),
        "segment-track": dim("38px", M, "billing period track"),
        "field": dim("40px", M, "email input"),
        "auth-button": dim("42px", M, "OAuth and Continue buttons"),
        "cta": dim("48px", M, "Get started for free"),
        "logo-height": dim("20px", M, "img[alt='Time2book logo']"),
        "content-auth": dim("420px", M, "login column max-width"),
        "content-hero": dim("690px", M, "hero column max-width"),
        "content-page": dim("1440px", M, "page max-width class max-w-[1440px]"),
    },
    "borderWidth": {
        "none": dim("0px", M, "marketing primary button"),
        "hairline": dim("1px", M, "login field and pricing column divider"),
    },
    "typography": {
        "display": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.medium}",
                "fontSize": "{fontSize.display}",
                "lineHeight": "{lineHeight.display}",
                "letterSpacing": "{letterSpacing.display}",
            },
            "typography", M, "home hero h2 at 1440",
        ),
        "section": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.medium}",
                "fontSize": "{fontSize.section}",
                "lineHeight": "{lineHeight.section}",
                "letterSpacing": "{letterSpacing.section}",
            },
            "typography", M, "home section h2 at 1440",
        ),
        "card-title": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.medium}",
                "fontSize": "{fontSize.card-title}",
                "lineHeight": "{lineHeight.card-title}",
                "letterSpacing": "{letterSpacing.card-title}",
            },
            "typography", M, "solution card title on a photo",
        ),
        "auth-title": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.medium}",
                "fontSize": "{fontSize.auth-title}",
                "lineHeight": "{lineHeight.auth-title}",
                "letterSpacing": "{letterSpacing.nav}",
            },
            "typography", M, "login heading",
        ),
        "body": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.regular}",
                "fontSize": "{fontSize.body}",
                "lineHeight": "{lineHeight.body}",
                "letterSpacing": "{letterSpacing.nav}",
            },
            "typography", M, "document.body",
        ),
        "nav": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.medium}",
                "fontSize": "{fontSize.nav}",
                "lineHeight": "{lineHeight.nav}",
                "letterSpacing": "{letterSpacing.nav}",
            },
            "typography", M, "nav Pricing link",
        ),
        "eyebrow": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.regular}",
                "fontSize": "{fontSize.body}",
                "lineHeight": "{lineHeight.eyebrow}",
                "letterSpacing": "{letterSpacing.eyebrow}",
            },
            "typography", M, "home h1 'Fitness studio software'",
        ),
        "legal": tok(
            {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{fontWeight.regular}",
                "fontSize": "{fontSize.legal}",
                "lineHeight": "{lineHeight.legal}",
                "letterSpacing": "{letterSpacing.nav}",
            },
            "typography", M, "signup legal links",
        ),
    },
    "motion": {
        "duration": {
            "fast": tok("75ms", "duration", M, "login OAuth button transition duration-75"),
            "base": tok("150ms", "duration", S, "--default-transition-duration .15s"),
            "sheen": tok("900ms", "duration", S, "promo link ::before hover transform .9s, only under reduced-motion no-preference"),
        },
        "easing": {
            "standard": tok([0.4, 0, 0.2, 1], "cubicBezier", S, "--default-transition-timing-function"),
            "out": tok([0, 0, 0.2, 1], "cubicBezier", S, "--ease-out"),
            "sheen": tok([0.22, 1, 0.36, 1], "cubicBezier", S, "promo sheen and promo-arrow"),
        },
    },
}

def semantic(page, surface, text, muted, accent, on_accent, border, ring, destructive, evidence, where):
    return {
        "color": {
            "background": {
                "page": color(page, evidence, where),
                "surface": color(surface, evidence, where),
                "promo": color(accent, evidence, where + " promo bar uses the ink fill"),
            },
            "text": {
                "primary": color(text, evidence, where),
                "secondary": color(muted, evidence, where),
                "on-accent": color(on_accent, evidence, where),
                "link": color(text, evidence, where + " nav links use the same ink as body text"),
            },
            "border": {
                "default": color(border, evidence, where),
                "strong": color(text, evidence, where),
                "focus": color(ring, evidence, where),
            },
            "accent": {
                "default": color(accent, evidence, where),
            },
            "status": {
                "danger": color(destructive, evidence, where),
            },
        },
        "component": {
            "button-primary": {
                "bg": color(accent, evidence, where),
                "text": color(on_accent, evidence, where),
                "radius": ref("{radius.pill}", evidence, where),
                "height": ref("{size.cta}", evidence, where),
                "padding": ref("{spacing.20}", evidence, where),
            },
            "button-secondary": {
                "bg": color("rgba(23, 23, 23, 0.05)", M, "Log in and OAuth buttons, rgba(23, 23, 23, 0.05)"),
                "text": color(text, evidence, where),
                "radius": ref("{radius.pill}", evidence, where),
                "height": ref("{size.nav-control}", evidence, where),
            },
            "field": {
                "bg": color(surface, evidence, where),
                "text": color("#000000", M, "email input computed color rgb(0, 0, 0)"),
                "radius": ref("{radius.control}", evidence, where),
                "height": ref("{size.field}", evidence, where),
                "padding": ref("{spacing.14}", evidence, where),
            },
        },
    }


light = semantic(
    HEX["page"], HEX["page"], HEX["ink"], HEX["mutedForeground"], HEX["ink"],
    "#ffffff", HEX["borderToken"], HEX["ring"], HEX["destructive"], M, LIGHT,
)
# Secondary button fill is an alpha, not the page white. Keep the measured alpha.
light["color"]["background"]["surface"] = color(HEX["page"], M, "nav, footer and login page bg-white")
light["color"]["text"]["secondary"] = color(HEX["mutedForeground"], S, "--muted-foreground resolved. Public muted copy also uses opacity 0.6 on #171717.")
light["color"]["border"]["default"] = color("rgba(23, 23, 23, 0.15)", M, "login field border-neutral-900/15")
light["color"]["border"]["focus"] = color("rgba(23, 23, 23, 0.5)", M, "login field focus-within:border-neutral-900/50")
light["shadow"] = {
    "segment": tok(
        [{"color": "rgba(23, 23, 23, 0.06)", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px"}],
        "shadow", S, "selected Monthly/Yearly thumb class shadow-[0px_1px_2px_0px_rgba(23,23,23,0.06)]",
    )
}

dark = semantic(
    HEX["darkBackground"], HEX["darkCard"], HEX["darkForeground"], HEX["darkMutedForeground"],
    HEX["darkPrimary"], HEX["darkPrimaryForeground"], "rgba(255, 255, 255, 0.1)",
    HEX["darkRing"], HEX["darkDestructive"], S, DARK,
)
dark["shadow"] = {
    "segment": tok(
        [{"color": "rgba(23, 23, 23, 0.06)", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px"}],
        "shadow", S, "same declared thumb shadow; not observed on a dark page",
    )
}

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The public signed-out pages. html class is font-sans antialiased. color-scheme is normal.",
        },
        {
            "id": "dark",
            "name": "Dark (declared, not shown)",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": ".dark custom properties from the marketing stylesheet. No public page applied this class.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}


def tokens_of(tree, prefix=""):
    for key, value in tree.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from tokens_of(value, prefix + key + ".")


def aliases(value):
    if isinstance(value, str):
        return [part[1:-1] for part in __import__("re").findall(r"\{[^{}]+\}", value)]
    if isinstance(value, dict):
        return [item for child in value.values() for item in aliases(child)]
    if isinstance(value, list):
        return [item for child in value for item in aliases(child)]
    return []


def check(doc):
    names = {}
    for set_name in ("core", "light", "dark"):
        if set_name not in doc:
            continue
        for path, token in tokens_of(doc[set_name]):
            names[path] = token
            if "source" not in token.get("$extensions", {}):
                raise SystemExit(f"{set_name}.{path} has no source")
    for set_name in ("core", "light", "dark"):
        if set_name not in doc:
            continue
        # An alias resolves in its own set, then in core (as tools/catalog.py's Resolver does),
        # never in another theme's set.
        local = dict(tokens_of(doc["core"]))
        local.update(dict(tokens_of(doc[set_name])))
        for path, token in tokens_of(doc[set_name]):
            for alias in aliases(token["$value"]):
                if alias not in local:
                    raise SystemExit(f"{set_name}.{path} alias {{{alias}}} points at nothing")


def render():
    """tokens.json's exact text, after the checks; nothing is written."""
    check(tokens)
    return json.dumps(tokens, indent=2) + "\n"


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(render())
    print("wrote", HERE / "tokens.json")
