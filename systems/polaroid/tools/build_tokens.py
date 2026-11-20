#!/usr/bin/env python3
"""Build tokens.json from the Polaroid public-store readings. Deterministic.

Every measured value is read from raw/components-computed.json (computed styles on the live
controls) or raw/css-vars.json (the custom properties on :root). A value no reading holds is
labelled Reconstruction in its source. `python3 tools/build_tokens.py` writes tokens.json;
build() returns the document without writing it.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())
V = json.loads((RAW / "css-vars.json").read_text())

SRC = "computed style, www.polaroid.com/en_sg, 2026-11-19, signed out"
HAND = "Reconstruction: entered by hand at capture time; no reading in raw/ holds it"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(families, source):
    return {"$type": "fontFamily", "$value": families, "$extensions": {"source": source}}


def typo(family, el, source, letter_spacing=False, size=None, weight=None, line_height=None):
    """A type style from a computed reading `el`; an argument given here overrides the reading."""
    value = {
        "fontFamily": family,
        "fontSize": size or el["size"],
        "fontWeight": int(weight or el["weight"]),
        "lineHeight": line_height or el["lh"],
    }
    if letter_spacing:
        value["letterSpacing"] = el["ls"]
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}


def cubic(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def text(value, source):
    return {"$type": "other", "$value": value, "$extensions": {"source": source}}


def hex_of(value):
    """rgb(21, 21, 21) or #fff as six-digit lower-case hex."""
    value = value.strip()
    if value.startswith("#"):
        h = value[1:].lower()
        return "#" + ("".join(c * 2 for c in h) if len(h) == 3 else h)
    nums = re.findall(r"[\d.]+", value)
    if len(nums) != 3:
        raise SystemExit(f"not an opaque rgb() colour: {value!r}")
    return "#" + "".join(f"{round(float(n)):02x}" for n in nums)


def px(value):
    """A computed length rounded to whole px: 15.04px -> 15px."""
    return f"{round(float(value[:-2]))}px"


def rem_px(value):
    """A declared rem length at the 16px root: .9375rem -> 15px."""
    n = float(value[:-3]) * 16
    return f"{n:g}px"


def pad(el, side):
    """One side of a computed `padding` reading (top right bottom left)."""
    top, right, bottom, left = el["pad"].split()
    return {"top": top, "right": right, "bottom": bottom, "left": left}[side]


def seconds_ms(value):
    return f"{round(float(value[:-1]) * 1000)}ms"


def bezier(easing):
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", easing)
    return [float(n) for n in m.group(1).split(",")]


def has_duration(value):
    return any(value in [d.strip() for d in entry.split(",")] for entry in C["motion"]["durations"])


def has_easing(value):
    return any(value in [e.strip() for e in re.split(r",\s*(?=[a-z])", entry)] for entry in C["motion"]["easings"])


def need(ok, what):
    if not ok:
        raise SystemExit(f"raw/ no longer holds {what}; recapture or relabel the token")


ROOT = V["root"]
HOME, LOGIN, CHROME, FILTERS = C["home-details"], C["login-details"], C["chrome"], C["filters"]
NAV, PANEL = HOME["nav"][0], HOME["nav"][1]
FONTS = V["fonts"]

S = SRC
display = "{core.font.family.display}"
text_face = "{core.font.family.text}"
mono = "{core.font.family.mono}"
FALLBACK = "; the Arial, sans-serif fallback is a Reconstruction: entered by hand at capture time (raw/css-vars.json records only 'fallback stack')"

need(C["cameras"]["h1"]["font"] == "REAL_HEADER_OFFC_DEMIBOLD", "the h1 face")
need(NAV["font"] == "REAL_HEADER_OFFC_REGULAR", "the nav face")
need(HOME["shop"]["font"] == "COMMIT_MONO", "the button face")
need(FONTS["--font-saol-text"].startswith("SAOL_TEXT"), "--font-saol-text")
need(has_duration("0.2s") and has_duration("0.3s"), "the 0.2s and 0.3s transition durations")
need(has_easing("cubic-bezier(0.45, 0.02, 0.09, 0.98)"), "the standard easing")

BG = hex_of(C["home"]["body"]["bg"])
INK = hex_of(C["home"]["body"]["color"])
GREY = hex_of(ROOT["--color-grey-200"])
CONTINUE = LOGIN["continue"]
BADGE = FILTERS["badge"]
PROMO = CHROME["bars"][1]
need(PROMO["cls"] == "SFI2JW_container", "the announcement bar")
BORDER_W, BORDER_C = ROOT["--border-solid"].split()[:2]
need(hex_of(LOGIN["wrap"]["bc"]) == hex_of(BORDER_C), "the email field wrapper border")


def build():
    return {
        "$description": "Polaroid public storefront (www.polaroid.com/en_sg). Signed out, 2026-11-19. One light theme. polaroid.com redirects to /en_sg.",
        "core": {
            "font": {
                "family": {
                    "display": font(
                        ["REAL_HEADER_OFFC_DEMIBOLD", "Arial", "sans-serif"],
                        S + "; computed font on h1 (RealHeadOffc Demibold, weight 600)" + FALLBACK,
                    ),
                    "text": font(
                        ["REAL_HEADER_OFFC_REGULAR", "Arial", "sans-serif"],
                        S + "; computed font on nav and the email field" + FALLBACK,
                    ),
                    "mono": font(
                        ["COMMIT_MONO", "Arial", "sans-serif"],
                        S + "; computed font on Shop Bundles, Continue, and Add to Bag" + FALLBACK,
                    ),
                    "serif": font(
                        ["SAOL_TEXT", "Times", "serif"],
                        "declared --font-saol-text, www.polaroid.com/en_sg 2026-11-19; not computed on a visible specimen; the Times, serif fallback is a Reconstruction: entered by hand at capture time (raw/css-vars.json records only 'fallback stack')",
                    ),
                }
            },
            "typography": {
                "display": typo(display, C["cameras"]["h1"], S + "; listing and product h1"),
                "hero": typo(display, C["home"]["h1"], S + "; home hero h1"),
                "title": typo(display, C["login"]["h1"], S + "; login h1, letter-spacing -1.28px", letter_spacing=True),
                "nav-panel": typo(display, PANEL, S + "; mega-menu links, letter-spacing -0.845px", letter_spacing=True),
                "nav": typo(text_face, NAV, S + "; header nav, letter-spacing -0.2106px", letter_spacing=True),
                "price": typo(text_face, NAV, HAND + " (the product price span was not read; the values repeat the nav style)"),
                "body": typo(text_face, LOGIN["email"], S + "; email input"),
                "button": typo(mono, HOME["shop"], S + "; Shop Bundles, Continue, Add to Bag"),
            },
            "radius": {
                "none": dim(HOME["shop"]["radius"], S + "; Shop Bundles, Continue, Add to Bag, email field, product card"),
                "pill": dim(CHROME["finder"]["radius"], S + "; Product Finder link"),
            },
            "space": {
                "page-margin": dim(rem_px(ROOT["--page-margin"]), S + "; --page-margin .9375rem at 1024px and up (16px root)"),
                "nav-safe": dim(rem_px(ROOT["--page-nav-safe-area"]), S + "; --page-nav-safe-area 5.1rem at 1024px and up"),
                "button-pad-x": dim(px(pad(HOME["shop"], "left")), S + "; Shop Bundles padding-left 15.04px"),
                "button-pad-y": dim(px(pad(HOME["shop"], "top")), S + "; Shop Bundles padding-top 12.96px"),
                "field-pad-x": dim(px(pad(LOGIN["email"], "left")), S + "; email input padding-left 15.04px"),
                "promo-height": dim(f'{PROMO["h"]}px', S + "; announcement bar SFI2JW_container"),
            },
            "border": {
                "solid": dim(BORDER_W, S + "; --border-solid, and the email field wrapper"),
            },
            "control": {
                "shop-height": dim(f'{HOME["shop"]["h"]}px', S + "; Shop Bundles and Get Inspired"),
                "continue-height": dim(f'{CONTINUE["h"]}px', S + "; Continue and Add to Bag"),
                "field-height": dim(f'{LOGIN["wrap"]["h"]}px', S + "; email field wrapper IEMMsq_inputContainer"),
                "finder-height": dim(f'{CHROME["finder"]["h"]}px', S + "; Product Finder"),
                "search-size": dim("20px", HAND + " (the header search button)"),
            },
            "motion": {
                "duration-fast": duration(seconds_ms("0.2s"), "declared transition-duration 0.2s in stylesheets, www.polaroid.com/en_sg 2026-11-19"),
                "duration": duration(seconds_ms("0.3s"), "declared transition-duration 0.3s in stylesheets, www.polaroid.com/en_sg 2026-11-19"),
                "easing-standard": cubic(
                    bezier("cubic-bezier(0.45, 0.02, 0.09, 0.98)"),
                    "declared transition-timing-function, www.polaroid.com/en_sg 2026-11-19",
                ),
                "easing-card": cubic(
                    [0.38, 0.07, 0.41, 0.88],
                    HAND + " (--card-grid-ease-background on .eKUYtG_container; raw/components-computed.json motion.easings does not list it)",
                ),
            },
            "aspect": {
                "polaroid": text(ROOT["--aspect-ratio-polaroid"], S + "; --aspect-ratio-polaroid"),
            },
        },
        "light": {
            "page": color(BG, S + "; body background rgb(255, 255, 255)"),
            "surface": color(GREY, S + "; --color-grey-200, product card background rgb(233, 233, 233)"),
            "text": color(INK, S + "; --color-secondary, body color rgb(21, 21, 21)"),
            "muted": color(
                hex_of(LOGIN["label"]["color"]),
                S + "; the email field label, the store's secondary text, computes to rgb(21, 21, 21), the same ink as light.text. Polaroid sets no lighter secondary text colour.",
            ),
            "accent": color(hex_of(CONTINUE["bg"]), S + "; Continue and Add to Bag background rgb(21, 21, 21)"),
            "on-accent": color(hex_of(CONTINUE["color"]), S + "; Continue and Add to Bag color rgb(255, 255, 255)"),
            "border": color(hex_of(BORDER_C), S + "; --border-solid colour and the email field wrapper"),
            "promo": color(hex_of(PROMO["bg"]), S + "; announcement bar SFI2JW_container background"),
            "on-promo": color(hex_of(PROMO["color"]), S + "; announcement bar color"),
            "nav-active": color(hex_of(CHROME["holidays"]["color"]), S + "; Holidays nav link color rgb(214, 0, 38) on the cameras page"),
            "error": color(hex_of(ROOT["--color-error"]), S + "; --color-error"),
            "highlight": color(hex_of(ROOT["--color-highlight"]), S + "; --color-highlight on :root and html.light-mode"),
            "inverse": color(hex_of(ROOT["--color-primary"]), S + "; --color-primary, the light page fill"),
            "badge": color(hex_of(BADGE["bg"]), S + "; Bundle Savings tag background rgb(21, 21, 21)"),
            "on-badge": color(hex_of(BADGE["color"]), S + "; Bundle Savings tag color"),
            "card-hover": color(
                "#c6c6c6",
                HAND + " (worked out from the declared card hover color-mix(in srgb, var(--color-grey-200) 85%, black); not a live hover reading)",
            ),
        },
        "$themes": [
            {
                "id": "light",
                "name": "light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
            }
        ],
    }


def main():
    out = HERE / "tokens.json"
    out.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
