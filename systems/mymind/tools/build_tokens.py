#!/usr/bin/env python3
"""Build tokens.json from readings taken on mymind.com on 2026-11-21.

The public site does not publish a design-token layer. styles.css declares
easing curves on :root and WordPress preset colours that the marketing pages
do not paint. Colour, type and geometry below were read as computed styles
on live elements, or as authored rules in /css/styles.css and /css/pages/home.css.
A value that was not read is absent. There is no dark theme on the public site.

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent


def color(value, source, description=""):
    token = {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def dim(value, source, description=""):
    token = {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def number(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def font_weight(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def cubic(value, source):
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def alias(path, source, ty="color"):
    return {"$value": "{" + path + "}", "$type": ty, "$extensions": {"source": source}}


S_PAGE = "computed backgroundColor of .transition-wrap on https://mymind.com/ at 1440x900, 2026-11-21"
S_H1 = "computed style of h1.mm-title on https://mymind.com/ at 1440x900, 2026-11-21"
S_BODY = "computed style of the hero paragraph on https://mymind.com/ at 1440x900, 2026-11-21"
S_CTA = "computed style of the TRY IT OUT .is-content wrap and its anchor on https://mymind.com/, 2026-11-21"
S_LINK = "computed color of the Log in anchor, matching the authored `a { color:#1573dd }` rule in https://mymind.com/css/styles.css"
S_CHIP = "computed style of the iPhone app .is-content chip on https://mymind.com/, 2026-11-21"
S_PRICE = "computed style on https://mymind.com/pricing at 1440x900, 2026-11-21"
S_CSS = "authored rule in https://mymind.com/css/styles.css, read 2026-11-21"
S_HOME = "authored rule in https://mymind.com/css/pages/home.css, read 2026-11-21"
S_ALIAS = "alias of a measured core colour"

core = {
    "$description": "Primitives read from the public marketing site. One theme.",
    "color": {
        "ink": color("#000000", S_H1, "Hero and body ink."),
        "ink-soft": color("#2c3441", S_PRICE + "; h1 color", "Pricing display ink."),
        "muted": color("#4a5465", S_BODY, "Hero supporting copy."),
        "muted-2": color("#748297", S_PRICE + "; price caption color rgb(116, 130, 151)", "Secondary captions on pricing."),
        "faint": color("#7e90a7", S_PRICE + "; Monthly/Yearly button color rgb(126, 144, 167)", "Unselected billing toggle."),
        "paper": color("#f9fafc", S_PAGE, "Page ground."),
        "white": color("#ffffff", "computed backgroundColor of .header-video-container and pricing cards on https://mymind.com/, 2026-11-21"),
        "chip": color("#f5f7f9", S_CHIP, "App-store chip fill."),
        "tab": color("#ebebf1", "computed backgroundColor of the iOS/Android role=button tabs on https://mymind.com/mobile, 2026-11-21"),
        "ember": color("#ff5924", S_CTA + "; also authored background-color:#ff5924 on .is-content in home.css", "The only filled accent."),
        "link": color("#1573dd", S_LINK),
        "card-sand": color("#f3f0e7", "computed backgroundColor of a home feature card (.content-wrapper), 2026-11-21"),
        "card-blue": color("#e5eaf2", "computed backgroundColor of a home feature card (.content-wrapper), 2026-11-21"),
        "card-green": color("#dde9d3", "computed backgroundColor of a home feature card (.content-wrapper), 2026-11-21"),
        "card-blush": color("#f4ecef", "computed backgroundColor of a home feature card (.content-wrapper), 2026-11-21"),
        "card-peach": color("#ffece5", "computed backgroundColor of a home feature card (.content-wrapper), 2026-11-21"),
        "section-warm": color("#f6f4f2", "computed backgroundColor of the IT JUST WORKS section container, 2026-11-21"),
        "section-reviews": color("#fff1f1", "computed backgroundColor of section.reviews-section, 2026-11-21"),
    },
    "font": {
        "family": {
            "display": font_family(
                "Avenir LT W01_45 Book1475508, sans-serif",
                S_H1 + "; fonts.net stylesheet https://fast.fonts.net/cssapi/ea5bdd24-21b4-4016-9bfc-2f59fe29ac87.css",
            ),
            "serif": font_family(
                "Louize-Regular-205TF, sans-serif",
                "computed fontFamily of the Log in anchor and of #content-holder h1 in styles.css",
            ),
            "ui": font_family(
                "Nunito-SemiBold, sans-serif",
                S_CTA + "; @font-face name declared in https://mymind.com/css/fonts.css",
            ),
            "body": font_family(
                "Inter-Regular, sans-serif",
                S_BODY + "; fonts.css comment says the Inter face lives there",
            ),
            "fallback": font_family(
                "Open Sans, Arial, sans-serif",
                "computed fontFamily of body on https://mymind.com/, 2026-11-21",
            ),
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "140px",
                "fontWeight": 400,
                "lineHeight": "119px",
                "letterSpacing": "-8.4px",
            },
            "$extensions": {"source": S_H1},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.serif}",
                "fontSize": "134px",
                "fontWeight": 400,
                "lineHeight": "122px",
            },
            "$extensions": {
                "source": S_PRICE + "; computed fontSize 134.11px on h1, box height 244px across two lines so lineHeight 122px is Derived from that box. letterSpacing was not read and is omitted"
            },
        },
        "title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.serif}",
                "fontSize": "50px",
                "fontWeight": 400,
                "lineHeight": "45px",
            },
            "$extensions": {"source": S_PRICE + "; plan name computed fontSize 50px and box height 45px, used as lineHeight. letterSpacing was not read and is omitted"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.body}",
                "fontSize": "20px",
                "fontWeight": 400,
                "lineHeight": "44px",
                "letterSpacing": "-0.4px",
            },
            "$extensions": {"source": S_BODY},
        },
        "ui": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "15px",
                "fontWeight": 400,
                "lineHeight": "25px",
                "letterSpacing": "0.8px",
            },
            "$extensions": {"source": S_CTA},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.serif}",
                "fontSize": "20px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": "computed style of the Log in anchor. The computed lineHeight was 0px; 24px is the measured border-box height, Derived as the line box. letterSpacing was normal and is omitted"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "28px",
            },
            "$extensions": {"source": "computed style of h2.mm-title.ts4 (OUR MANIFESTO) on https://mymind.com/, 2026-11-21. letterSpacing computed as normal and is omitted"},
        },
        "faq": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "28px",
                "fontWeight": 400,
                "lineHeight": "28px",
            },
            "$extensions": {"source": "computed fontSize 28px and fontFamily of h3 questions on https://mymind.com/faq. lineHeight was not read; 28px repeats the measured font size and is Derived, not a line-box measurement"},
        },
    },
    "radius": {
        "none": dim("0px", "computed borderRadius of h1.mm-title and body, 2026-11-21"),
        "card": dim("22px", S_PRICE + "; pricing card borderRadius"),
        "pill": dim("120px", S_CTA + "; authored border-radius: 6.666666666666667rem on the ember .is-content in home.css"),
        "chip": dim("100px", S_CHIP),
        "signup": dim("25px", S_PRICE + "; SIGN UP button borderRadius"),
    },
    "space": {
        "0": dim("0px", "computed padding of body, 2026-11-21"),
        "10": dim("10px", S_CTA + "; CTA padding-block"),
        "22": dim("22px", S_CTA + "; CTA padding-inline"),
        "60": dim("60px", "computed padding-bottom 60px of the OUR MANIFESTO column, 2026-11-21"),
    },
    "size": {
        "cta-height": dim("45px", S_CTA),
        "chip-height": dim("50px", S_CHIP),
        "signup-height": dim("50px", S_PRICE + "; SIGN UP button height"),
        "nav-link-height": dim("24px", "computed height of the Log in anchor, 2026-11-21"),
        "content": dim("1300px", S_H1 + "; measured width of h1.mm-title"),
    },
    "motion": {
        "link": duration("200ms", S_CSS + "; `a { transition: all .2s linear }`"),
        "linear": cubic([0, 0, 1, 1], S_CSS + "; :root --linear is the keyword linear, recorded as the matching curve"),
        "ease-out-quart": cubic(
            [0.165, 0.84, 0.44, 1],
            S_CSS + "; :root --ease-out-quart. Declared, not observed on a painted control",
        ),
    },
    "border": {
        "none": dim("0px", "computed borderTopWidth of the TRY IT OUT control and of body, 2026-11-21"),
    },
}

light = {
    "$description": "The only theme the public site paints.",
    "background": {
        "page": alias("color.paper", S_ALIAS),
        "surface": alias("color.white", S_ALIAS),
        "chip": alias("color.chip", S_ALIAS),
        "accent": alias("color.ember", S_ALIAS),
    },
    "text": {
        "primary": alias("color.ink", S_ALIAS),
        "secondary": alias("color.muted", S_ALIAS),
        "muted": alias("color.muted-2", S_ALIAS),
        "on-accent": color("#ffffff", S_CTA + "; CTA anchor color"),
        "link": alias("color.link", S_ALIAS),
    },
    "border": {
        "default": color("#000000", "computed border color of body is the text colour with 0px width; no painted border was measured. Recorded as the ink, width 0"),
    },
    "accent": {
        "default": alias("color.ember", S_ALIAS),
    },
    "component": {
        "button": {
            "bg": alias("color.ember", S_ALIAS),
            "text": color("#ffffff", S_CTA),
            "radius": alias("radius.pill", S_CTA, ty="dimension"),
            "height": alias("size.cta-height", S_CTA, ty="dimension"),
            "padding": alias("space.10", S_CTA, ty="dimension"),
        },
        "link": {
            "text": alias("color.link", S_ALIAS),
        },
    },
}

def check(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node["$type"]
        val = node["$value"]
        if not node.get("$extensions", {}).get("source"):
            raise SystemExit(f"missing source: {path}")
        if ty == "color" and isinstance(val, str) and not val.startswith("{"):
            if not re.fullmatch(r"#[0-9a-f]{6}", val):
                raise SystemExit(f"bad colour {path}: {val}")
        if ty == "dimension" and isinstance(val, str) and not val.startswith("{"):
            if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", val):
                raise SystemExit(f"bad dimension {path}: {val}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            check(v, f"{path}.{k}" if path else k)


check(core)
check(light)

tokens = {
    "$description": "mymind public marketing site, measured 2026-11-21. Light only.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", out, "core groups", list(core))
