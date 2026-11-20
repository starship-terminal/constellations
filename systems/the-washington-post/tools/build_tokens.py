#!/usr/bin/env python3
"""Build tokens.json from the live readings in raw/.

Every colour, length and font name comes from raw/computed-vars.json or
raw/components-computed.json. A value that was not on the page is not invented.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "computed-vars.json").read_text())["vars"]
COMP = json.loads((RAW / "components-computed.json").read_text())


def rgba_to_hex(value):
    text = value.strip()
    if text.startswith("#"):
        return text.lower()
    if text.startswith("rgba") or text.startswith("rgb"):
        inner = text[text.index("(") + 1:text.rindex(")")]
        parts = [p.strip() for p in inner.split(",")]
        r, g, b = (int(round(float(parts[0]))), int(round(float(parts[1]))), int(round(float(parts[2]))))
        alpha = float(parts[3]) if len(parts) > 3 else 1
        if alpha >= 0.999:
            return "#%02x%02x%02x" % (r, g, b)
        return "#%02x%02x%02x%02x" % (r, g, b, round(alpha * 255))
    # A value that is not a colour (a renamed var, a keyword) must not pass through as one.
    raise ValueError("not a colour reading: %r" % value)


def color(name, source):
    return {
        "$value": rgba_to_hex(VARS[name]),
        "$type": "color",
        "$extensions": {"source": "computed %s on html.wpds-dark (%s)" % (name, source)},
    }


def dim(name, source):
    return {
        "$value": VARS[name],
        "$type": "dimension",
        "$extensions": {"source": "computed %s (%s)" % (name, source)},
    }


def font_family(name, source):
    return {
        "$value": VARS[name],
        "$type": "fontFamily",
        "$extensions": {"source": "computed %s (%s)" % (name, source)},
    }


def number_token(name, source, type_name):
    return {
        "$value": float(VARS[name]) if "." in VARS[name] else int(VARS[name]),
        "$type": type_name,
        "$extensions": {"source": "computed %s (%s)" % (name, source)},
    }


def measured_color(value, source):
    return {
        "$value": rgba_to_hex(value),
        "$type": "color",
        "$extensions": {"source": source},
    }


def measured_dim(value, source):
    return {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": source},
    }


home = COMP["pages"]["home"]
article = COMP["pages"]["article"]
signin = COMP["pages"]["signin"]
politics = COMP["pages"]["politics"]
mobile = COMP["pages"]["mobile390"]

core = {
    "color": {
        "gray": {step: color("--wpds-colors-gray%s" % step, "home") for step in
                 ("0", "20", "40", "60", "80", "100", "200", "300", "400", "500", "600", "700")},
        "blue": {
            "100": color("--wpds-colors-blue100", "home"),
            "80": color("--wpds-colors-blue80", "home"),
        },
        "cta": color("--wpds-colors-cta", "home"),
        "cta-hover": color("--wpds-colors-cta-hover", "home"),
        "error": color("--wpds-colors-error", "home"),
        "success": color("--wpds-colors-success", "home"),
        "warning": color("--wpds-colors-warning", "home"),
        "opinions": color("--wpds-colors-opinions", "home"),
        "link": color("--link-color", "home"),
    },
    "font": {
        "family": {
            "franklin": font_family("--font-family-franklin", "home"),
            "meta": font_family("--wpds-fonts-meta", "home"),
            "headline": font_family("--wpds-fonts-headline", "home"),
            "magazine": font_family("--wpds-fonts-magazine", "home"),
            "body": font_family("--wpds-fonts-body", "home"),
            "subhead": font_family("--wpds-fonts-subhead", "home"),
            "georgia": font_family("--font-family-georgia", "home"),
        },
        "size": {step: dim("--wpds-fontSizes-%s" % step, "home") for step in
                 ("075", "087", "100", "112", "125", "150", "162", "175", "200", "225", "250", "275", "300", "350", "400", "450", "500")},
        "weight": {
            "light": number_token("--wpds-fontWeights-light", "home", "fontWeight"),
            "regular": number_token("--wpds-fontWeights-regular", "home", "fontWeight"),
            "bold": number_token("--wpds-fontWeights-bold", "home", "fontWeight"),
            "ultra": number_token("--wpds-fontWeights-ultra", "home", "fontWeight"),
        },
        "lineHeight": {step: number_token("--wpds-lineHeights-%s" % step, "home", "number") for step in
                       ("100", "110", "125", "150", "160", "175", "200", "240")},
    },
    "space": {step: dim("--wpds-space-%s" % step, "home") for step in
              ("025", "050", "075", "100", "125", "150", "175", "200", "225", "250", "275", "300", "350", "400", "450", "500")},
    "radius": {step: dim("--wpds-radii-%s" % step, "home") for step in
               ("012", "025", "050", "075", "100", "125", "150", "round")},
    "shadow": {step: {
        "$value": VARS["--wpds-shadows-%s" % step],
        "$type": "shadow",
        "$extensions": {"source": "computed --wpds-shadows-%s (home)" % step},
    } for step in ("50", "100", "200", "300", "400", "500")},
    "motion": {
        "duration": {step: {
            "$value": VARS["--motion-duration-%s" % step],
            "$type": "duration",
            "$extensions": {"source": "computed --motion-duration-%s (home)" % step},
        } for step in ("100", "200", "300", "400", "500", "extra-fast", "fast", "normal", "slow", "extra-slow")},
        "easing": {
            "in": {"$value": [0.4, 0, 0.7, 0.2], "$type": "cubicBezier",
                   "$extensions": {"source": "computed --motion-ease-in cubic-bezier(.4,0,.7,.2)"}},
            "out": {"$value": [0, 0, 0.2, 1], "$type": "cubicBezier",
                    "$extensions": {"source": "computed --motion-ease-out cubic-bezier(0,0,.2,1)"}},
            "in-out": {"$value": [0.4, 0, 0.2, 1], "$type": "cubicBezier",
                       "$extensions": {"source": "computed --motion-ease-in-out cubic-bezier(.4,0,.2,1)"}},
        },
        "transition": {
            "fast": {"$value": VARS["--wpds-transitions-fast"], "$type": "duration",
                     "$extensions": {"source": "computed --wpds-transitions-fast"}},
            "normal": {"$value": VARS["--wpds-transitions-normal"], "$type": "duration",
                       "$extensions": {"source": "computed --wpds-transitions-normal"}},
            "all-fast": {"$value": VARS["--wpds-transitions-allFast"], "$type": "other",
                         "$extensions": {"source": "computed --wpds-transitions-allFast"}},
        },
    },
    "typography": {
        "nav-pill": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.meta}",
                "fontSize": home["sectionPill"]["fontSize"],
                "fontWeight": int(home["sectionPill"]["fontWeight"]),
                "lineHeight": home["sectionPill"]["lineHeight"],
            },
            "$extensions": {"source": "computed section pill 'Politics' on home"},
        },
        "slogan": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.georgia}",
                "fontSize": home["slogan"]["fontSize"],
                "fontWeight": int(home["slogan"]["fontWeight"]),
                "lineHeight": home["slogan"]["lineHeight"],
            },
            "$extensions": {"source": "computed 'Democracy Dies in Darkness' on home"},
        },
        "story-headline": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.headline}",
                "fontSize": home["storyHeadlineLarge"]["fontSize"],
                "fontWeight": int(home["storyHeadlineLarge"]["fontWeight"]),
                "lineHeight": home["storyHeadlineLarge"]["lineHeight"],
            },
            "$extensions": {"source": "computed home h2 Postoni 26px"},
        },
        "article-headline": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.headline}",
                "fontSize": article["headline"]["fontSize"],
                "fontWeight": int(article["headline"]["fontWeight"]),
                "lineHeight": article["headline"]["lineHeight"],
            },
            "$extensions": {"source": "computed article h1 Postoni 48px"},
        },
        "article-dek": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.meta}",
                "fontSize": article["dek"]["fontSize"],
                "fontWeight": int(article["dek"]["fontWeight"]),
                "lineHeight": article["dek"]["lineHeight"],
            },
            "$extensions": {"source": "computed article dek Franklin 20px/300"},
        },
        "article-body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.body}",
                "fontSize": article["body"]["fontSize"],
                "fontWeight": int(article["body"]["fontWeight"]),
                "lineHeight": article["body"]["lineHeight"],
            },
            "$extensions": {"source": "computed article body georgia 20px/32px"},
        },
        "byline": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.franklin}",
                "fontSize": home["byline"]["fontSize"],
                "fontWeight": int(home["byline"]["fontWeight"]),
                "lineHeight": home["byline"]["lineHeight"],
            },
            "$extensions": {"source": "computed home byline Franklin 14px gray-dark"},
        },
        "section-title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.meta}",
                "fontSize": politics["title"]["fontSize"],
                "fontWeight": int(politics["title"]["fontWeight"]),
                "lineHeight": politics["title"]["lineHeight"],
            },
            "$extensions": {"source": "computed Politics h1 Franklin 48px"},
        },
        "signin-heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.headline}",
                "fontSize": signin["heading"]["fontSize"],
                "fontWeight": int(signin["heading"]["fontWeight"]),
                "lineHeight": "29px",
            },
            "$extensions": {"source": "computed sign-in h1 Postoni 24px, height 29px"},
        },
    },
    "component": {
        "nav-height": measured_dim("60px", "computed home nav height 60"),
        "section-bar-height": measured_dim("48px", "computed home section bar height 48, padding 8px 0"),
        "subscribe-height": measured_dim("32px", "computed home Save and subscribe height 32"),
        "sign-in-height": measured_dim("40px", "computed home Sign in height 40"),
        "icon-button-size": measured_dim("36px", "computed Search and browse sections button 36x36"),
        "field-height": measured_dim("48px", "computed sign-in email input height 48"),
        "field-chrome-height": measured_dim("50px", "computed focused sign-in field chrome height 50"),
        "next-height": measured_dim("40px", "computed sign-in Next button height 40"),
        "paywall-width": measured_dim("460px", "computed article offer card width 460"),
        "article-column": measured_dim("640px", "computed article h1 and body width 640"),
        "subscribe-padding": measured_dim("8px", "computed home subscribe padding 8px 16px; vertical step"),
        "subscribe-padding-x": measured_dim("16px", "computed home subscribe padding 8px 16px"),
        "mobile-section-title": measured_dim(mobile["sectionTitle"]["fontSize"], "computed Politics h1 at forced 390px width"),
        "mobile-sign-in-size": measured_dim(mobile["signIn"]["fontSize"], "computed Sign in font-size at forced 390px width"),
    },
}

dark = {
    "page": color("--wpds-colors-background", "home body"),
    "surface": color("--wpds-colors-surface", "home"),
    "surface-highest": color("--wpds-colors-surface-highest", "home"),
    "text": color("--wpds-colors-onBackground", "home"),
    "muted": color("--wpds-colors-onBackground-subtle", "home"),
    "headline": measured_color(home["storyHeadlineLarge"]["color"], "computed home story h2 color"),
    "timestamp": measured_color(article["timestamp"]["color"], "computed article time color"),
    "accent": color("--wpds-colors-cta", "home subscribe"),
    "accent-hover": color("--wpds-colors-cta-hover", "home"),
    "on-accent": color("--wpds-colors-onCta", "home"),
    "border": color("--wpds-colors-outline", "home"),
    "border-subtle": color("--wpds-colors-outline-subtle", "home"),
    "slogan": measured_color(home["slogan"]["color"], "computed slogan color"),
    "link": color("--link-color", "home"),
    "error": color("--wpds-colors-error", "home"),
    "success": color("--wpds-colors-success", "home"),
    "warning": color("--wpds-colors-warning", "home"),
    "opinions": color("--wpds-colors-opinions", "home"),
    "disabled": color("--wpds-colors-disabled", "home"),
    "on-disabled": color("--wpds-colors-onDisabled", "home"),
}

light = {
    "page": measured_color(signin["fieldChrome"]["backgroundColor"], "computed sign-in field chrome and offer card background"),
    "surface": measured_color("rgb(255, 255, 255)", "computed offer card and OAuth button background"),
    "text": measured_color(signin["heading"]["color"], "computed sign-in heading and offer card text rgb(17, 17, 17)"),
    "muted": measured_color(article["paywallCard"]["already"]["color"], "computed offer 'Already a subscriber?' rgb(89, 89, 89)"),
    "headline": measured_color(article["paywallCard"]["offerHeadline"]["color"], "computed offer headline rgb(42, 42, 42)"),
    "accent": measured_color(signin["next"]["backgroundColor"], "computed sign-in Next background rgb(22, 109, 252), also declared --wpds-colors-cta"),
    "on-accent": measured_color(signin["next"]["color"], "computed sign-in Next text"),
    "border": measured_color("rgb(233, 233, 233)", "computed offer card border"),
    "field-focus": measured_color("rgb(87, 132, 197)", "computed focused sign-in field border"),
    "oauth-border": measured_color("rgba(0, 0, 0, 0.1)", "computed OAuth button border"),
    "sso": measured_color(signin["sso"]["color"], "computed Continue with SSO"),
    "logo": measured_color(signin["logo"]["fill"], "computed sign-in wordmark fill"),
}

tokens = {
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The public site paints this theme: html class wpds-dark, page rgb(20, 20, 20)."},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The article offer card and the /subscribe/signin/ card paint light surfaces on the same visit. A site-wide light theme was not switched."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "dark", "light"]},
}



def render():
    """tokens.json's exact text; importing this module writes nothing."""
    return json.dumps(tokens, indent=2) + "\n"


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(render())
    print("wrote", HERE / "tokens.json")
