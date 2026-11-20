#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Channel triples on :root were read with getComputedStyle(document.documentElement)
on https://ripple.com/ in the T3 preview tab on 2026-11-19. Component sizes,
radii and shadows were read from getComputedStyle on the same live page.
Hex values are those triples written as sRGB. Nothing here is sampled from a
screenshot.

    python3 tools/build_tokens.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
RAW = json.loads((PKG / "raw" / "css-vars.json").read_text())
COMP = json.loads((PKG / "raw" / "components-computed.json").read_text())

LIVE = "T3 preview tab, https://ripple.com/, 2026-11-19, innerWidth 1440"


def hex_of(triple):
    parts = triple.split()
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        raise ValueError(triple)
    return "#%02x%02x%02x" % tuple(int(p) for p in parts)


def tok(value, typ, evidence, capture, note=None):
    src = {"evidence": evidence, "capture": capture}
    if note:
        src["note"] = note
    return {"$value": value, "$type": typ, "$extensions": {"source": src}}


def color_from_var(name, note=None):
    return tok(hex_of(RAW["root"][name]), "color", "Measured", f"raw/css-vars.json {name}", note)


def dim(value, capture, note=None):
    return tok(value, "dimension", "Measured", capture, note)


def core():
    root = RAW["root"]
    color = {"bds": {}, "marketing": {}}
    for name, value in root.items():
        if not name.startswith("--") or name.startswith("--font") or name.startswith("--breakpoint"):
            continue
        if "," in value or value.startswith("$"):
            continue
        parts = value.split()
        if len(parts) != 3:
            continue
        leaf = name[2:].replace("-", ".")
        # keep a flat group: bds.color.blue.500 style via nested dict
        bits = name[2:].split("-")
        node = color
        for bit in bits[:-1]:
            node = node.setdefault(bit, {})
        node[bits[-1]] = tok(hex_of(value), "color", "Measured", f"raw/css-vars.json {name}")

    font = {
        "family": {
            "display": tok(
                "rippleFont, \"rippleFont Fallback\", Arial, sans-serif",
                "fontFamily",
                "Measured",
                "computed body fontFamily on https://ripple.com/",
                "rippleFont is TT Ripple (woff2). Fallback face is local Arial. Proprietary; not committed.",
            ),
            "ui": tok(
                "rippleBdsFont, \"rippleBdsFont Fallback\", Ripple, \"San Francisco\", \"Helvetica Neue\", Helvetica, Arial, sans-serif",
                "fontFamily",
                "Measured",
                "computed fontFamily on the Contact Sales link",
                "Declared as --font-ripple-bds plus the .bds-body-sm stack.",
            ),
        }
    }
    weight = {
        "book": tok("350", "fontWeight", "Measured", "@font-face rippleFont weight 350 (TT_Ripple_Book)"),
        "regular": tok("400", "fontWeight", "Measured", "computed body fontWeight; @font-face rippleBdsFont 400"),
        "medium": tok("500", "fontWeight", "Measured", "computed h1 fontWeight; @font-face rippleBdsFont 500"),
        "bold": tok("700", "fontWeight", "Measured", "@font-face rippleBdsFont weight 700 (TT_Ripple_Bold). Not used on the pages measured."),
    }
    typography = {
        "display": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.medium}", "fontSize": "68px", "lineHeight": "80px", "letterSpacing": "-1px"},
            "typography", "Measured", "computed h1.lg:headline1 at innerWidth 1440",
        ),
        "display-tablet": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.medium}", "fontSize": "49px", "lineHeight": "64px", "letterSpacing": "-1px"},
            "typography", "Measured", "stylesheet .headline2; also the computed home h1 at innerWidth 390 is .headline3 (42px/56px)",
        ),
        "display-phone": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.medium}", "fontSize": "42px", "lineHeight": "56px", "letterSpacing": "-1px"},
            "typography", "Measured", "computed h1 at innerWidth 390 (class headline3)",
        ),
        "hero": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.medium}", "fontSize": "93px", "lineHeight": "104px", "letterSpacing": "-1px"},
            "typography", "Measured", "computed h1 on /company/ at innerWidth 1440",
        ),
        "headline": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.medium}", "fontSize": "36px", "lineHeight": "48px", "letterSpacing": "-0.5px"},
            "typography", "Measured", "computed h2 on / at innerWidth 1440 (headline4)",
        ),
        "title": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.medium}", "fontSize": "22px", "lineHeight": "32px", "letterSpacing": "0px"},
            "typography", "Measured", "stylesheet .heading1 (22px/2rem) and computed FAQ h3 (22px/32px, weight 350 on the question)",
        ),
        "lede": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.book}", "fontSize": "19px", "lineHeight": "28px", "letterSpacing": "0px"},
            "typography", "Measured", "computed home lede p and insight card title",
        ),
        "body": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.regular}", "fontSize": "16px", "lineHeight": "24px", "letterSpacing": "0px"},
            "typography", "Measured", "computed body on https://ripple.com/",
        ),
        "ui": tok(
            {"fontFamily": "{font.family.ui}", "fontWeight": "{fontWeight.regular}", "fontSize": "16px", "lineHeight": "24px", "letterSpacing": "0px"},
            "typography", "Measured", "computed nav item and Contact Sales (.bds-body-sm)",
        ),
        "button": tok(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.medium}", "fontSize": "16px", "lineHeight": "24px", "letterSpacing": "0px"},
            "typography", "Measured", "stylesheet .button1 and computed .button-dark",
        ),
        "meta": tok(
            {"fontFamily": "{font.family.ui}", "fontWeight": "{fontWeight.regular}", "fontSize": "14px", "lineHeight": "20px", "letterSpacing": "0px"},
            "typography", "Measured", "computed mega-menu description (14px / 20.006px, rounded to 20px)",
        ),
    }
    radius = {
        "sm": dim("2px", "computed logo link borderRadius 2px (.rounded-sm)"),
        "md": dim("4px", "computed search field borderRadius 4px"),
        "nav": dim("6px", "computed nav item borderRadius 6px (.rounded-md)"),
        "lg": dim("8px", "computed FAQ button and insight image borderRadius 8px"),
        "xl": dim("12px", "computed mega-menu card borderRadius 12px"),
        "pill": dim("40px", "computed .button-dark borderRadius 40px (.rounded-4xl)"),
        "full": dim("9999px", "computed Contact Sales and icon button borderRadius 9999px"),
    }
    space = {
        "1": dim("4px", "search dialog uses 16px padding; 4px is the field radius, recorded as a step only where measured on padding of small controls", "4px appears as the focus ring's inner 1px plus the 3px outer ring offset, and as search padding differences. Kept because 4px is a computed padding component (search field 8px is 2x)."),
        "2": dim("8px", "computed .button-dark .wrapper padding-top 8px"),
        "3": dim("12px", "computed .button-dark .wrapper padding-right 12px"),
        "4": dim("16px", "computed flex gap 16px on the hero action row; phone drawer item padding 16px"),
        "5": dim("18px", "computed Contact Sales padding-left 18px"),
        "6": dim("24px", "computed search dialog padding 24px; body line-height 24px"),
        "8": dim("32px", "computed FAQ button padding 32px; header container padding-left 32px"),
        "header": dim("80px", "computed header height 80px"),
        "control": dim("40px", "computed primary button and icon button height 40px"),
        "nav": dim("36px", "computed nav item height 36px"),
    }
    # drop the shaky space.1 note-as-token if the description is a guess. 4px was
    # not a padding I measured as a standalone length. Remove it.
    del space["1"]
    size = {
        "icon-button": dim("40px", "computed Open search button 40x40"),
        "control": dim("40px", "computed .button-dark height 40px"),
        "nav-item": dim("36px", "computed header nav button height 36px"),
        "drawer-item": dim("56px", "computed phone drawer row height 56px at innerWidth 390"),
        "logo": dim("24px", "computed header wordmark svg height 24px, width 93px"),
    }
    layout = {
        "container": dim("1480px", "stylesheet .max-w-layout-container { max-width: 1480px }"),
        "content": dim("1152px", "stylesheet .max-w-layout-xl { max-width: 1152px }; computed at innerWidth 1440"),
        "page-desktop": dim("1440px", "measured window.innerWidth after preview_resize freeform 1440"),
        "page-phone": dim("390px", "measured window.innerWidth after preview_resize freeform 390"),
    }
    border = {
        "contact": dim("2px", "computed Contact Sales border-top-width 2px"),
        "focus": dim("3px", "stylesheet .bds-focus-ring:focus-visible box-shadow outer ring 3px"),
    }
    shadow = {
        "button-inset": tok(
            [
                {"color": "rgba(0, 91, 204, 0.9)", "offsetX": "0px", "offsetY": "3px", "blur": "12px", "spread": "0px", "inset": True},
                {"color": "rgba(0, 91, 204, 0.8)", "offsetX": "0px", "offsetY": "-3px", "blur": "4px", "spread": "0px", "inset": True},
            ],
            "shadow", "Measured", "computed boxShadow on button.button-dark",
        ),
        "menu": tok(
            [{"color": "rgba(0, 0, 0, 0.05)", "offsetX": "0px", "offsetY": "10px", "blur": "20px", "spread": "0px"}],
            "shadow", "Measured", "computed boxShadow on #nav-panel-0",
        ),
        "search": tok(
            [
                {"color": "rgba(0, 0, 0, 0.1)", "offsetX": "0px", "offsetY": "1px", "blur": "3px", "spread": "0px"},
                {"color": "rgba(0, 0, 0, 0.1)", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "-1px"},
            ],
            "shadow", "Measured", "computed boxShadow on the search dialog (700x434)",
        ),
        "focus": tok(
            [
                {"color": "#ffffff", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px"},
                {"color": "#006aff", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "3px"},
            ],
            "shadow", "Measured", "stylesheet .bds-focus-ring:focus-visible and computed search input boxShadow",
        ),
    }
    motion = {
        "duration": {
            "fast": tok("150ms", "duration", "Measured", "computed transition on the search icon button: 0.15s"),
            "short": tok("200ms", "duration", "Measured", "stylesheet transition-duration 0.2s (11 rules)"),
            "medium": tok("300ms", "duration", "Measured", "stylesheet transition-duration 0.3s (17 rules)"),
        },
        "easing": {
            "standard": tok([0.4, 0, 0.2, 1], "cubicBezier", "Measured", "computed transition-timing-function on the search icon button"),
            "enter": tok([0, 0, 0.2, 1], "cubicBezier", "Measured", "stylesheet cubic-bezier(0, 0, 0.2, 1), 14 rules"),
            "ease": tok("ease", "cubicBezier", "Derived", "stylesheet timing-function ease (33 rules). CSS ease is cubic-bezier(0.25, 0.1, 0.25, 1); the keyword was declared, the control points were not."),
        },
    }
    # cubicBezier type cannot be the keyword. Fix ease to the CSS-defined control points and mark Derived.
    motion["easing"]["ease"] = tok(
        [0.25, 0.1, 0.25, 1],
        "cubicBezier",
        "Derived",
        "stylesheet timing-function keyword ease (33 rules). CSS defines ease as cubic-bezier(0.25, 0.1, 0.25, 1). The control points were not in the sheet.",
    )
    return {
        "color": color,
        "font": font,
        "fontWeight": weight,
        "typography": typography,
        "radius": radius,
        "spacing": space,
        "size": size,
        "layout": layout,
        "borderWidth": border,
        "shadow": shadow,
        "motion": motion,
        "$extensions": {
            "notTokenised": RAW["notTokenised"] + [
                {"name": "button circle keyframes", "why": "circle-1 through circle-12 animate the primary button's liquid fill. Steps were read (translate offsets) but are not a duration token."},
                {"name": "hero gradient", "value": "linear-gradient(92deg, #0052b6 -2.09%, #33a3ff 66.48%, #0067e5 97.37%)", "why": "computed background-image on the /company/ h1. Recorded on light.gradient.hero."},
            ]
        },
    }


def semantic():
    return {
        "surface": {
            "page": color_from_var("--color-white", "Header computed background rgb(255, 255, 255) matches --color-white. The page section behind the hero is --color-gray-90."),
            "hero": color_from_var("--color-white", "The home hero section's painted band is white. A wrapper .bg-gray-90 computed to #141a1f, and that colour is the footer, recorded as surface.footer."),
            "raised": color_from_var("--color-gray-2-5", "computed background on .bg-gray-2.5 bands"),
            "white": color_from_var("--color-white"),
            "muted": color_from_var("--bds-neutral-50", "computed icon-button background rgb(242, 242, 243)"),
            "field": color_from_var("--bds-neutral-100", "computed search input background rgb(228, 229, 231)"),
            "accordion": color_from_var("--color-gray-10", "computed FAQ button background rgb(229, 231, 232)"),
            "footer": color_from_var("--color-gray-90", "computed footer background rgb(20, 26, 31)"),
            "menu-card": color_from_var("--bds-neutral-25", "computed mega-menu card background rgb(248, 248, 248)"),
            "featured": color_from_var("--bds-primary-900", "computed featured mega-menu card background rgb(0, 11, 51)"),
            "scrim": tok("rgba(16, 19, 21, 0.47)", "color", "Measured", "computed background on the search modal"),
        },
        "text": {
            "primary": color_from_var("--color-gray-90", "computed h1 and lede color rgb(20, 26, 31)"),
            "on-dark": color_from_var("--color-gray-2-5", "computed footer color rgb(250, 250, 250)"),
            "on-accent": color_from_var("--color-gray-5", "computed .button-dark color rgb(241, 242, 243)"),
            "muted": color_from_var("--bds-neutral-500", "computed mega-menu description rgb(112, 122, 143)"),
            "field": color_from_var("--bds-neutral-600", "computed search input color rgb(88, 96, 116)"),
            "link": color_from_var("--color-blue-60", "computed article link rgb(0, 91, 204) on /insights/ripple-swell-2026-recap/"),
            "link-bright": color_from_var("--color-blue-50", "computed legal link rgb(0, 140, 255) on /legal/privacy-policy/"),
            "stat": color_from_var("--color-blue-55", "computed stat figure color rgb(0, 103, 229)"),
            "current": color_from_var("--bds-primary-500", "computed Company nav item color rgb(0, 106, 255) on /company/"),
            "ink": tok("#000000", "color", "Measured", "computed nav item color rgb(0, 0, 0), matches --bds-neutral-black"),
        },
        "accent": color_from_var("--bds-primary-500", "Brand blue. Also --color-new-blue-50. Used as the focus ring and the current nav item."),
        "accent-hover": color_from_var("--color-blue-70", ".button-dark:hover moves --c-color-2 to rgb(var(--color-blue-70)/1)"),
        "accent-deep": color_from_var("--color-blue-60", "Primary button inset shadow color rgb(0, 91, 204)"),
        "border": {
            "subtle": color_from_var("--bds-neutral-100"),
            "strong": color_from_var("--color-gray-90"),
            "focus": color_from_var("--bds-primary-500", "focus ring outer color"),
        },
        "status": {
            "success": color_from_var("--bds-color-green-300"),
            "warning": color_from_var("--color-orange-50"),
            "danger": color_from_var("--color-swell-red", "Declared. Not seen as a validation error on a public page."),
            "info": color_from_var("--bds-primary-500"),
        },
        "gradient": {
            "hero": tok(
                [
                    {"color": "#0052b6", "position": 0},
                    {"color": "#33a3ff", "position": 0.6648},
                    {"color": "#0067e5", "position": 0.9737},
                ],
                "gradient",
                "Measured",
                "computed background-image on the /company/ h1: linear-gradient(92deg, rgb(0, 82, 182) -2.09%, rgb(51, 163, 255) 66.48%, rgb(0, 103, 229) 97.37%)",
            )
        },
        "component": {
            "button-primary": {
                "background": color_from_var("--color-blue-60", "The fill is animated circles using --color-blue-60 stops, not a flat background-color (computed background-color was transparent)."),
                "text": color_from_var("--color-gray-5"),
                "radius": tok("{radius.pill}", "dimension", "Measured", "computed .button-dark borderRadius 40px"),
                "height": tok("{size.control}", "dimension", "Measured", "computed .button-dark height 40px"),
                "padding": tok("8px", "dimension", "Measured", "computed .wrapper padding-top 8px"),
            },
            "button-secondary": {
                "text": tok("{text.ink}", "color", "Measured", "computed Contact Sales color rgb(0, 0, 0)"),
                "radius": tok("{radius.full}", "dimension", "Measured", "computed Contact Sales borderRadius 9999px"),
                "height": tok("{size.control}", "dimension", "Measured", "computed Contact Sales height 40px"),
            },
            "icon-button": {
                "background": color_from_var("--bds-neutral-50"),
                "radius": tok("{radius.full}", "dimension", "Measured", "computed icon button borderRadius 9999px"),
                "size": tok("{size.icon-button}", "dimension", "Measured", "computed 40x40"),
            },
            "text-field": {
                "background": color_from_var("--bds-neutral-100"),
                "text": color_from_var("--bds-neutral-600"),
                "radius": tok("{radius.md}", "dimension", "Measured", "computed search input borderRadius 4px"),
                "height": tok("{size.control}", "dimension", "Measured", "computed search input height 40px"),
            },
            "nav-item": {
                "text": tok("{text.ink}", "color", "Measured", "computed nav item color"),
                "radius": tok("{radius.nav}", "dimension", "Measured", "computed nav item borderRadius 6px"),
                "height": tok("{size.nav-item}", "dimension", "Measured", "computed nav item height 36px"),
            },
        },
    }


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


def check(doc):
    sets = [s for s in ("core", "light") if s in doc]
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            if not src.get("evidence") or not src.get("capture"):
                raise SystemExit(f"{where}: no source")
            for a in aliases(t["$value"]):
                if a not in paths:
                    raise SystemExit(f"{where}: alias {{{a}}} points at nothing")
            v = t["$value"]
            if isinstance(v, str) and v.startswith("{"):
                continue
            if t["$type"] == "color" and not re.fullmatch(r"#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)", v):
                raise SystemExit(f"{where}: bad colour {v}")
            if t["$type"] == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", v):
                raise SystemExit(f"{where}: bad dimension {v}")


def build():
    doc = {
        "core": core(),
        "light": semantic(),
        "$themes": [
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
                "$description": "The public site paints one scheme. color-scheme on the document is normal. No theme toggle was found. prefers-color-scheme: dark was true on the capture machine and the page stayed light.",
            }
        ],
        "$metadata": {"tokenSetOrder": ["core", "light"]},
    }
    # gradient position 0 may need to be 0.0 for some readers; leave as measured.
    check(doc)
    return doc


def write(doc):
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
    n = sum(1 for s in ("core", "light") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens")


if __name__ == "__main__":
    write(build())
