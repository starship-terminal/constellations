#!/usr/bin/env python3
"""Build tokens.json from readings taken on portrait.so on 2026-11-19.

Custom properties were read from the live documentElement. Component roles
were read from computed styles on the same page. Dark page and text colours
were read after setting data-mode="dark" on the document (the site's own
selector is :where([data-mode="dark"], [data-mode="dark"] *)). That pass is
a forced attribute, not a live theme switch.

No token is invented. A role the page did not show is left out.
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
COLORS = RAW["colors"]

VAR = "computed custom property on documentElement, https://portrait.so/, light, 1169px, 2026-11-19"
COMP = "computed style on a live element, https://portrait.so/, light, 1169px, 2026-11-19"
DARK = "computed style after documentElement data-mode=dark, same page, 2026-11-19. Forced attribute, not a live theme control."


HAND = "Reconstruction: entered by hand at capture time from a live reading that raw/ does not hold (raw/css-vars.json keeps only the --color-* custom properties)"


def hex_of(value):
    return "#ffffff" if value == "#fff" else "#000000" if value == "#000" else value


def ext(source, measured):
    """A value raw/ holds is Measured; anything else was typed in from a reading that was not saved."""
    if measured:
        return {"source": source, "evidence": "Measured"}
    return {"source": f"{source}. {HAND}", "evidence": "Reconstruction"}


def color_token(value, source, measured=False):
    return {"$type": "color", "$value": value, "$extensions": ext(source, measured)}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": ext(source, False)}


def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": ext(source, False)}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": ext(source, False)}


def shadow(value, source):
    return {"$type": "shadow", "$value": value, "$extensions": ext(source, False)}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": ext(source, False)}


def cubic(value, source):
    """cubic-bezier(a, b, c, d) as the DTCG four-number list."""
    nums = [float(n) for n in re.fullmatch(r"cubic-bezier\(([^)]*)\)", value).group(1).split(",")]
    nums = [int(n) if n.is_integer() else n for n in nums]
    return {"$type": "cubicBezier", "$value": nums, "$extensions": ext(source + f" ({value})", False)}


def alias(ref, source, type_="color"):
    return {"$type": type_, "$value": ref, "$extensions": ext(source, False)}


def ramp(prefix):
    out = {}
    needle = "--color-" + prefix + "-"
    for key in sorted(COLORS):
        if not key.startswith(needle):
            continue
        step = key[len(needle):]
        out[step] = color_token(hex_of(COLORS[key]), VAR + f" {key}", measured=True)
    return out


def typography(family, size, weight, line_height, source, tracking=None):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if tracking:
        value["letterSpacing"] = tracking
    return {"$type": "typography", "$value": value, "$extensions": ext(source, False)}


def build():
    """The token document, without writing it."""
    core = {
        "color": {
            "black": color_token(hex_of(COLORS["--color-black"]), VAR + " --color-black", measured=True),
            "white": color_token(hex_of(COLORS["--color-white"]), VAR + " --color-white", measured=True),
            "gray": ramp("gray"),
            "brand": {
                "blue": ramp("brand-blue"),
                "green": ramp("brand-green"),
                "orange": ramp("brand-orange"),
                "pink": ramp("brand-pink"),
                "red": ramp("brand-red"),
                "yellow": ramp("brand-yellow"),
            },
            "red": ramp("red"),
            "green": ramp("green"),
            "blue": ramp("blue"),
        },
        "font": {
            "family": {
                "display": font("Basier Circle, sans-serif", COMP + " h1 font-family __basierCircle"),
                "sans": font("Switzer, ui-sans-serif, system-ui, sans-serif", VAR + " --font-sans __switzer"),
                "mono": font("JetBrains Mono, ui-monospace, monospace", VAR + " --font-jetbrains-mono"),
                "open-runde": font("Open Runde, sans-serif", VAR + " --font-open-runde"),
            },
            "weight": {
                "normal": num(400, VAR + " --font-weight-normal"),
                "medium": num(500, VAR + " --font-weight-medium"),
                "semibold": num(600, VAR + " --font-weight-semibold"),
                "bold": num(700, VAR + " --font-weight-bold"),
                "button": num(540, COMP + " button face font-weight 540"),
            },
        },
        "typography": {
            "display": typography("{font.family.display}", "71.49px", 500, 1, COMP + " h1.text-h1-lg-fluid computed 71.4924px / line-height 71.4924px / letter-spacing -3.57462px. Declared --text-h1-lg-fluid is clamp(2.2807rem, 1.3073rem + 4.3264vw, 4.7684rem).", "-0.05em"),
            "h2": typography("{font.family.display}", "46.42px", 500, 1.04, COMP + " h2.text-h2-fluid computed 46.415px", "-0.032em"),
            "h3": typography("{font.family.display}", "37.44px", 500, 1.08, COMP + " h2.text-h3-fluid computed 37.4425px", "-0.0256em"),
            "h4": typography("{font.family.display}", "31.25px", 500, 1.1, VAR + " --text-h4 1.9531rem; h2.text-h4 computed 31.2496px", "-0.02048em"),
            "h6": typography("{font.family.display}", "20px", 500, 1.2, VAR + " --text-h6 1.25rem; h3.text-h6 computed 20px", "-0.0131em"),
            "body": typography("{font.family.sans}", "16px", 400, 1.5, COMP + " body 16px / 24px"),
            "body-lg": typography("{font.family.sans}", "18px", 400, 1.5, COMP + " hero lede computed 18px"),
            "label": typography("{font.family.sans}", "14px", 540, 1.43, COMP + " header Log in face 14px / 20px / weight 540"),
            "caption": typography("{font.family.sans}", "12px", 600, 1.33, COMP + " New badge 12px / weight 600"),
        },
        "radius": {
            "xs": dim("2px", VAR + " --radius-xs .125rem"),
            "sm": dim("4px", VAR + " --radius-sm .25rem; NEW badge computed 4px"),
            "md": dim("6px", VAR + " --radius-md .375rem; points Dashboard tab computed 6px"),
            "lg": dim("8px", VAR + " --radius-lg .5rem; account menu item computed 8px"),
            "xl": dim("12px", VAR + " --radius-xl .75rem; confirmation-code cell and Accept button computed 12px"),
            "2xl": dim("16px", VAR + " --radius-2xl 1rem; sign-in dialog and blog card computed 16px"),
            "3xl": dim("24px", VAR + " --radius-3xl 1.5rem"),
            "4xl": dim("32px", VAR + " --radius-4xl 2rem"),
            "full": dim("9999px", COMP + " button border-radius computed as a pill (16777215px)"),
            "menu": dim("20px", COMP + " editor account menu computed 20px"),
            "field": dim("25px", COMP + " email input computed 25px"),
        },
        "spacing": {
            "1": dim("4px", VAR + " --spacing .25rem"),
            "2": dim("8px", "2 x --spacing .25rem"),
            "3": dim("12px", COMP + " menu item padding-inline 12px; email input padding 12px"),
            "4": dim("16px", COMP + " header Log in padding-inline 16px"),
            "5": dim("20px", COMP + " primary button padding-inline 20px"),
            "8": dim("32px", COMP + " header padding 32px 32px 0; footer padding-block 32px"),
        },
        "size": {
            "button-sm": dim("36px", COMP + " header Log in and Sign up height 36px"),
            "button-md": dim("44px", COMP + " Create your Portrait, Apply, editor Account height 44px"),
            "button-lg": dim("56px", COMP + " hero Sign up height 56px"),
            "field": dim("50px", COMP + " email input height 50px"),
            "username": dim("80px", COMP + " username field wrapper height 80px"),
            "code": dim("58px", COMP + " confirmation-code cell height 58px, width 46px"),
            "icon-button": dim("44px", COMP + " editor trailing icon button 44px"),
            "avatar": dim("28px", COMP + " editor Account avatar 28px"),
        },
        "border": {"width": dim("1px", COMP + " username field and email input border 1px")},
        "shadow": {
            "sm": shadow(
                "0 16px 16px -8px #00000008, 0 10px 10px -5px #00000008, 0 5px 5px -2.5px #00000008, 0 3px 3px -1.5px #00000008, 0 2px 2px -1px #00000008, 0 1px 1px -0.5px #00000008",
                COMP + " primary button face box-shadow layers at rgba(0,0,0,0.03)",
            ),
            "lg": shadow(
                "0 28px 28px -14px #0000000f, 0 16px 16px -8px #0000000d",
                "computed .shadow-lg utility, first two painted layers. Signup hover class is group-hocus/button:shadow-lg.",
            ),
        },
        "motion": {
            "duration": {
                "fast": duration("150ms", VAR + " --default-transition-duration .15s"),
                "accordion": duration("200ms", VAR + " --animate-accordion-open .2s"),
                "slide": duration("600ms", VAR + " --animate-slide-up .6s"),
            },
            "easing": {
                "standard": cubic("cubic-bezier(0.4, 0, 0.2, 1)", VAR + " --default-transition-timing-function"),
                "out": cubic("cubic-bezier(0, 0, 0.2, 1)", VAR + " --ease-out"),
                "in": cubic("cubic-bezier(0.4, 0, 1, 1)", VAR + " --ease-in"),
                "out-smooth": cubic("cubic-bezier(0.26, 0.08, 0.25, 1)", VAR + " --ease-out-smooth"),
                "dropdown": cubic("cubic-bezier(0.16, 1, 0.3, 1)", VAR + " --animate-dropdown-in"),
            },
        },
        "layout": {
            "breakpoint-xs": dim("360px", VAR + " --breakpoint-xs"),
            "breakpoint-sm": dim("640px", VAR + " --breakpoint-sm"),
            "breakpoint-md": dim("768px", VAR + " --breakpoint-md"),
            "breakpoint-lg": dim("1024px", VAR + " --breakpoint-lg"),
            "breakpoint-xl": dim("1280px", VAR + " --breakpoint-xl"),
            "breakpoint-2xl": dim("1536px", VAR + " --breakpoint-2xl"),
            "content": dim("1280px", VAR + " nav max-w-(--breakpoint-xl)"),
            "dialog": dim("420px", COMP + " sign-in dialog width 420px"),
            "menu": dim("272px", COMP + " editor account menu width 272px"),
        },
    }

    light = {
        "color": {
            "bg": {
                "page": alias("{color.gray.10}", COMP + " body background rgb(247, 247, 247), class bg-gray-10"),
                "surface": alias("{color.white}", COMP + " footer and sign-in dialog background rgb(255, 255, 255)"),
                "inverse": alias("{color.gray.1000}", COMP + " editor body background rgb(20, 20, 20)"),
            },
            "text": {
                "primary": alias("{color.gray.600}", COMP + " body color rgb(53, 53, 53)"),
                "heading": alias("{color.brand.blue.1000}", COMP + " h1 color rgb(8, 48, 76), class text-brand-blue-1000"),
                "muted": alias("{color.gray.400}", COMP + " header Log in face color rgb(88, 88, 88)"),
                "quiet": alias("{color.gray.300}", COMP + " footer link Overview color rgb(121, 121, 121)"),
                "strong": alias("{color.gray.900}", COMP + " username input color rgb(27, 27, 27)"),
                "on-accent": alias("{color.white}", COMP + " primary button face color rgb(255, 255, 255)"),
            },
            "border": {
                "default": alias("{color.gray.50}", COMP + " username field border rgb(222, 222, 222)"),
                "input": color_token("#ebebeb", COMP + " email input border rgb(235, 235, 235). Not a named gray step."),
            },
            "action": {
                "fill": alias("{color.gray.700}", COMP + " Create your Portrait face background rgb(44, 44, 44)"),
                "fill-hover": alias("{color.gray.25}", "class group-hocus/button:bg-gray-25 on the quiet button. Rest was transparent. Class read, not a live :hover."),
            },
            "status": {
                "info": alias("{color.brand.blue.100}", COMP + " New badge background rgb(223, 243, 255)"),
                "warning": alias("{color.brand.orange.100}", COMP + " NEW badge background rgb(255, 235, 214)"),
                "danger": alias("{color.red.500}", VAR + " --color-red-500. Declared. Not seen as a live error."),
                "success": alias("{color.green.500}", VAR + " --color-green-500. Declared. Not seen as a live success message."),
            },
        },
        "component": {
            "button-primary": {
                "bg": alias("{color.action.fill}", COMP + " primary face"),
                "text": alias("{color.text.on-accent}", COMP + " primary face color"),
                "radius": alias("{radius.full}", COMP + " pill", "dimension"),
                "height": alias("{size.button-md}", COMP + " 44px", "dimension"),
            },
            "button-signup": {
                "bg": alias("{color.white}", COMP + " Sign up inner face white inside the rainbow ring"),
                "text": alias("{color.action.fill}", COMP + " Sign up face color rgb(44, 44, 44)"),
                "radius": alias("{radius.full}", COMP + " pill", "dimension"),
                "height": alias("{size.button-sm}", COMP + " header Sign up 36px", "dimension"),
            },
            "field": {
                "bg": alias("{color.white}", COMP + " email input background"),
                "text": color_token("#4d4d4d", COMP + " email input color rgb(77, 77, 77)"),
                "radius": alias("{radius.field}", COMP + " email input 25px", "dimension"),
                "height": alias("{size.field}", COMP + " email input 50px", "dimension"),
            },
            "dialog": {
                "bg": alias("{color.white}", COMP + " sign-in dialog"),
                "radius": alias("{radius.2xl}", COMP + " dialog 16px", "dimension"),
                "width": alias("{layout.dialog}", COMP + " dialog 420px", "dimension"),
            },
            "badge": {
                "bg": alias("{color.brand.blue.100}", COMP + " New badge"),
                "text": alias("{color.brand.blue.900}", COMP + " New badge text rgb(8, 78, 114)"),
                "radius": alias("{radius.full}", COMP + " pill", "dimension"),
            },
            "menu": {
                "bg": color_token("#000000cc", COMP + " editor menu background oklab(0 0 0 / 0.8)"),
                "text": alias("{color.gray.100}", COMP + " menu item rgb(199, 199, 199)"),
                "radius": alias("{radius.menu}", COMP + " menu 20px", "dimension"),
            },
        },
    }

    dark = {
        "color": {
            "bg": {
                "page": alias("{color.gray.1000}", DARK + " body background rgb(20, 20, 20)"),
                "canvas": alias("{color.gray.1000}", COMP + " editor body rgb(20, 20, 20) while prefers-color-scheme was light"),
            },
            "text": {
                "primary": alias("{color.white}", DARK + " body color rgb(255, 255, 255)"),
                "heading": alias("{color.brand.blue.1000}", DARK + " h1 stayed rgb(8, 48, 76)"),
                "muted": alias("{color.gray.100}", COMP + " editor menu item rgb(199, 199, 199)"),
            },
            "action": {
                "glass": color_token("#ffffff24", COMP + " editor Account face oklab white / 0.14"),
                "glass-border": color_token("#ffffff33", COMP + " editor Account border oklab white / 0.2"),
            },
        }
    }

    tokens = {
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    return tokens


def main():
    (HERE / "tokens.json").write_text(json.dumps(build(), indent=2) + "\n")
    print("wrote", HERE / "tokens.json")


if __name__ == "__main__":
    main()
