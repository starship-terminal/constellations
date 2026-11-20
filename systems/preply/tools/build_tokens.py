#!/usr/bin/env python3
"""Build systems/preply/tokens.json from measured computed styles.

Values were read on 2026-11-19 from preply.com signed out, in headless Chromium
at 1440x900 and 390x844. Preply's Tokyo UI custom properties are content-hashed
(--603ec6 and the like), so semantic roles are the computed styles of the
controls that use them, not invented names. There is no theme switch: forcing
prefers-color-scheme: dark left the pink header and #121117 ink unchanged.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def weight(value, source):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": source}}


def string(value, source):
    return {"$type": "string", "$value": value, "$extensions": {"source": source}}


def typography(family, size, weight_v, line, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight_v,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source},
    }


def shadow(css, source):
    return {"$type": "shadow", "$value": css, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def cubic(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


SRC = "computed style, preply.com signed out, 1440x900, 2026-11-19"
HOME = SRC + ", home"
LOGIN = SRC + ", /en/login chrome (not submitted)"
TUTORS = SRC + ", /en/online/english-tutors"

core = {
    "font": {
        "family": {
            "ui": font(
                "Figtree, Figtree-fallback, Figtree-fallback-android, Noto Sans, NotoSans-fallback, sans-serif",
                HOME + "; body and controls compute to Figtree first. Files are served from static.preply.com and are not shipped",
            ),
            "display": font(
                "Platform, Platform-fallback, Platform-fallback-android, Noto Sans, NotoSans-fallback, sans-serif",
                HOME + "; h1/h2/h3 compute to Platform. Proprietary, not shipped",
            ),
        }
    },
    "typography": {
        "hero": typography("{font.family.display}", "63px", "700", "68px", "-0.315px", HOME + "; h1 at 1440"),
        "display": typography("{font.family.display}", "96px", "700", "96px", "-0.48px", HOME + "; h2 'Progress starts with the right tutor'"),
        "heading-l": typography("{font.family.display}", "48px", "700", "52px", "0px", HOME + "; h3 'Find your tutor.'"),
        "heading-m": typography("{font.family.display}", "32px", "700", "36px", "0.32px", HOME + "; stat '100,000+' and h3"),
        "heading-s": typography("{font.family.display}", "24px", "700", "32px", "0.3px", HOME + "; language tile title"),
        "label": typography("{font.family.display}", "20px", "700", "24px", "0.35px", HOME + "; footer column title and tutor name"),
        "body-l": typography("{font.family.ui}", "24px", "400", "32px", "-0.12px", HOME + "; Text--variant-large-regular"),
        "body": typography("{font.family.ui}", "16px", "400", "24px", "0px", HOME + "; Text--variant-default-regular"),
        "body-strong": typography("{font.family.ui}", "16px", "600", "24px", "0px", HOME + "; Text--variant-default-semibold"),
        "caption": typography("{font.family.ui}", "14px", "400", "20px", "0.07px", HOME + "; Text--variant-small-regular, secondary ink"),
        "caption-strong": typography("{font.family.ui}", "14px", "600", "20px", "0.07px", HOME + "; Text--variant-small-semibold"),
        "button-l": typography("{font.family.ui}", "18px", "600", "24px", "0.09px", HOME + "; ButtonBase size-large"),
        "button-s": typography("{font.family.ui}", "14px", "600", "16px", "0.175px", HOME + "; ButtonBase size-small"),
        "hero-mobile": typography("{font.family.display}", "40px", "700", "36.8px", "0px", "computed style, preply.com home, 390x844 @2x, 2026-11-19; h1"),
    },
    "radius": {
        "xs": dim("4px", HOME + "; link radius and step card"),
        "sm": dim("8px", HOME + "; ButtonBase, field wrap, tutor card, search"),
    },
    "space": {
        "2": dim("2px", HOME + "; button border width"),
        "4": dim("4px", HOME + "; radius step and link radius"),
        "8": dim("8px", HOME + "; button radius"),
        "12": dim("12px", HOME + "; tutor card padding"),
        "14": dim("14px", LOGIN + "; field wrap horizontal padding"),
        "16": dim("16px", HOME + "; small button horizontal padding and body size"),
        "24": dim("24px", HOME + "; body line height"),
        "28": dim("28px", HOME + "; large button horizontal padding"),
        "32": dim("32px", HOME + "; step card padding"),
        "40": dim("40px", HOME + "; small control height (Log In, icon button)"),
        "48": dim("48px", HOME + "; medium control and field wrap height"),
        "56": dim("56px", HOME + "; large button height and header band on the first viewport read"),
        "72": dim("72px", HOME + "; header height at 1440x900"),
    },
    "size": {
        "control-s": dim("40px", HOME + "; Log In and icon button"),
        "control-m": dim("48px", LOGIN + "; social buttons and email field wrap"),
        "control-l": dim("56px", HOME + "; Find your tutor"),
        "checkbox": dim("20px", LOGIN + "; .checkbox__KtCna around the native checkbox"),
        "field": dim("48px", LOGIN + "; .root__USarf around the email input"),
        "content": dim("1440px", HOME + "; measured viewport. No max-width token was read off a container"),
    },
    "border": {
        "hairline": dim("0.5px", HOME + "; tutor card border-top-width"),
        "thin": dim("1px", HOME + "; step card border"),
        "control": dim("2px", HOME + "; ButtonBase border-top-width"),
    },
    "motion": {
        "duration": {
            "control": duration("220ms", HOME + "; ButtonBase transition-duration 0.22s on color, border-color, background-color"),
        },
        "easing": {
            "control": cubic([0.22, 1, 0.36, 1], HOME + "; ButtonBase transition-timing-function"),
        },
    },
    "shadow": {
        "menu": shadow("0px 0px 8px rgba(9, 15, 25, 0.1)", HOME + "; the one non-none box-shadow read on the home DOM"),
    },
}

light = {
    "color": {
        "bg": {
            "page": color("#ffffff", HOME + "; card and page surfaces compute to rgb(255, 255, 255). body itself is transparent"),
            "inverse": color("#121117", HOME + "; footer rgb(18, 17, 23)"),
            "banner": color("#141414", "sampled pixel on home-light-default.png at (720, 20), the Ukraine bar. Computed style of that strip was transparent, so the painted black is a screenshot sample, not a CSS read"),
            "pink": color("#ff7aac", HOME + "; hero section and header computed background rgb(255, 122, 172). The logo pixel on the same screenshot is also #ff7aac"),
            "blue": color("#99c5ff", HOME + "; Book a demo secondary fill rgb(153, 197, 255)"),
            "hover-wash": color("rgba(71, 71, 133, 0.06)", HOME + "; Log In button background on real hover"),
            "pressed-ink": color("rgba(18, 17, 23, 0.72)", HOME + "; onColor button background on real hover"),
        },
        "text": {
            "primary": color("#121117", HOME + "; body color rgb(18, 17, 23)"),
            "secondary": color("#4d4c5c", HOME + "; Text accent-secondary rgb(77, 76, 92)"),
            "muted": color("#6a697c", HOME + "; tutor card border and secondary grey rgb(106, 105, 124)"),
            "inverse": color("#ffffff", HOME + "; footer link and onColor label"),
            "link": color("#0000ee", HOME + "; unstyled tile link computes to the browser default link blue"),
        },
        "border": {
            "strong": color("#121117", HOME + "; secondary and primary button border"),
            "default": color("#dcdce5", HOME + "; tertiary button and field wrap rgb(220, 220, 229)"),
            "soft": color("rgba(20, 20, 82, 0.15)", HOME + "; tertiary-small button border"),
            "card": color("#6a697c", HOME + "; tutor card border"),
        },
        "action": {
            "primary": color("#ff7aac", HOME + "; ButtonBase--variant-primary fill, Log in submit"),
            "on-color": color("#121117", HOME + "; ButtonBase--variant-onColor fill, Find your tutor"),
            "on-color-hover": color("rgba(18, 17, 23, 0.72)", HOME + "; same control on real hover"),
            "focus": color("#006af5", HOME + "; :focus-visible outline rgb(0, 106, 245), declared as var(--603ec6) which the base scheme sets to #006af5"),
        },
        "status": {
            "danger": color("#a3120a", "declared on .ds-tokyo-ui__PkpFv.ds-scheme--base as a repeated colour (#a3120a). Not observed on a status component in the signed-out capture"),
            "success": color("#067560", "declared on .ds-tokyo-ui__PkpFv.ds-scheme--base (#067560). Not observed on a status component in the signed-out capture"),
            "warning": color("#966208", "declared on .ds-tokyo-ui__PkpFv.ds-scheme--base (#966208). Not observed on a status component in the signed-out capture"),
            "info": color("#0450b4", "declared on .ds-tokyo-ui__PkpFv.ds-scheme--base (#0450b4). Not observed on a status component in the signed-out capture"),
        },
    },
    "component": {
        "button": {
            "primary": {
                "bg": color("{color.action.primary}", LOGIN + "; Log in submit"),
                "text": color("{color.text.primary}", LOGIN),
                "border": color("{color.border.strong}", LOGIN),
                "radius": dim("{radius.sm}", HOME),
                "height": dim("{size.control-m}", LOGIN + "; 48px medium. Home scroll-to-top primary icon is 56px"),
                "pad-x": dim("28px", HOME + "; size-large. Login submit is medium and was not given horizontal padding in the first read"),
                "font-size": dim("18px", LOGIN),
                "font-weight": weight("600", LOGIN),
                "border-width": dim("{border.control}", LOGIN),
            },
            "onColor": {
                "bg": color("{color.action.on-color}", HOME + "; Find your tutor"),
                "text": color("{color.text.inverse}", HOME),
                "radius": dim("{radius.sm}", HOME),
                "height": dim("{size.control-l}", HOME),
                "pad-x": dim("28px", HOME),
                "font-size": dim("18px", HOME),
                "font-weight": weight("600", HOME),
                "hover-bg": color("{color.action.on-color-hover}", HOME + "; real hover"),
            },
            "secondary": {
                "bg": color("rgba(0, 0, 0, 0)", HOME + "; Log In at rest is transparent with a 2px #121117 border. Book a demo is the same variant with a blue fill on the pink hero"),
                "text": color("{color.text.primary}", HOME),
                "border": color("{color.border.strong}", HOME),
                "radius": dim("{radius.sm}", HOME),
                "height": dim("{size.control-s}", HOME + "; header Log In. Hero Book a demo is size-large at 56px"),
                "hover-bg": color("{color.bg.hover-wash}", HOME + "; real hover on Log In"),
            },
            "ghost": {
                "bg": color("rgba(0, 0, 0, 0)", HOME + "; How our platform works"),
                "text": color("{color.text.primary}", HOME),
                "radius": dim("{radius.sm}", HOME),
                "height": dim("{size.control-l}", HOME),
                "decoration": string("underline", HOME),
            },
            "focus": {
                "color": color("{color.action.focus}", HOME + "; keyboard focus on Find your tutor"),
                "width": dim("2px", HOME),
                "offset": dim("2px", HOME),
            },
        },
        "field": {
            "bg": color("rgba(0, 0, 0, 0)", LOGIN + "; input is transparent; wrap .root__USarf carries the border"),
            "text": color("#000000", LOGIN + "; email input color rgb(0, 0, 0), not the page ink"),
            "border": color("{color.border.default}", LOGIN),
            "radius": dim("{radius.sm}", LOGIN),
            "height": dim("{size.field}", LOGIN),
            "pad-x": dim("14px", LOGIN),
            "font-size": dim("16px", LOGIN),
        },
        "search": {
            "bg": color("#ffffff", TUTORS),
            "border": color("{color.border.default}", TUTORS),
            "radius": dim("{radius.sm}", TUTORS),
            "height": dim("48px", TUTORS),
            "pad-x": dim("16px", TUTORS),
        },
        "checkbox": {
            "bg": color("{color.text.primary}", LOGIN + "; .checkbox__KtCna computed fill. Native input is 16px and transparent"),
            "border": color("{color.border.strong}", LOGIN),
            "radius": dim("{radius.xs}", LOGIN),
            "size": dim("{size.checkbox}", LOGIN),
        },
        "card": {
            "bg": color("{color.bg.page}", HOME + "; styles_card step card"),
            "border": color("{color.border.strong}", HOME),
            "radius": dim("{radius.xs}", HOME),
            "pad": dim("32px", HOME),
            "border-width": dim("{border.thin}", HOME),
        },
        "tutorCard": {
            "bg": color("{color.bg.page}", HOME),
            "border": color("{color.border.card}", HOME),
            "radius": dim("{radius.sm}", HOME),
            "pad": dim("12px", HOME),
        },
        "header": {
            "bg": color("{color.bg.pink}", HOME + "; header.Main_TokyoPinkBg computed rgb(255, 122, 172), and the logo pixel matches"),
            "height": dim("{space.72}", HOME + "; 72px at 1440, sitting under a 64px Ukraine bar"),
        },
        "banner": {
            "bg": color("{color.bg.banner}", "sampled, home screenshot (720, 20)"),
            "height": dim("64px", HOME + "; styles_TopPrompt bounding height"),
            "text": color("#ffffff", "observed on the screenshot; the computed color of the strip's text node was #121117 because its background was transparent"),
        },
        "footer": {
            "bg": color("{color.bg.inverse}", HOME),
            "text": color("{color.text.inverse}", HOME),
            "pad-top": dim("60px", HOME + "; footer padding-top"),
        },
    },
}

def build():
    """The token document. Writes nothing; in particular nothing under raw/, which holds readings."""
    return {
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
        "$metadata": {
            "tokenSetOrder": ["core", "light"],
            "note": "Preply paints one theme signed out (tokyo-ui / ds-scheme--base). prefers-color-scheme: dark did not restyle the page.",
        },
    }


def main():
    (HERE / "tokens.json").write_text(json.dumps(build(), indent=2) + "\n")
    print("wrote", HERE / "tokens.json")


if __name__ == "__main__":
    main()
