#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

getmatter.com declares a small --mr-* layer (colours, radii, breakpoints,
spacers, a system font stack, an accent gradient). The marketing site paints
one near-black theme. Measured leaves come from raw/components-computed.json.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
RL = V.get("resolved", {}).get("light", {})


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def measured(comp, state, prop, ty, source):
    st = C[comp]["states"][state]
    style = st.get("style") or {}
    return {"value": style[prop], "type": ty, "source": source}


SPEC = {
    "_about": (
        "Matter's public token tree. Declared --mr-* variables become var "
        "leaves. Painted values without a variable are measured leaves."
    ),
    "core": {
        "color": {
            "black": var("--mr-color-black"),
            "dark-2": var("--mr-color-dark-2"),
            "dark-3": var("--mr-color-dark-3"),
            "gray": var("--mr-color-gray"),
            "gray-light": var("--mr-color-gray-light"),
            "light-2": var("--mr-color-light-2"),
            "light-3": var("--mr-color-light-3"),
            "white": var("--mr-color-white"),
            "blurple": var("--mr-color-blurple"),
            "content-200": var("--mr-content-200"),
            "content-300": var("--mr-content-300"),
            "content-400": var("--mr-content-400"),
        },
        "font": {
            "family": {
                "system": var("--mr-font-system", "fontFamily"),
                "camphor": {
                    # Copied as the h1 computes it, not hand-composed: the earlier literal dropped
                    # the emoji faces and unquoted "system-ui".
                    "value": C["hero-h1"]["states"]["default"]["style"]["fontFamily"],
                    "type": "fontFamily",
                    "source": "computed font-family on the marketing h1, raw/components-computed.json hero-h1 (MR-Camphor, loaded from the site)",
                },
            },
        },
        "radius": {
            "s": var("--mr-border-radius-s", "dimension"),
            "m": var("--mr-border-radius-m", "dimension"),
            "pill": {
                "value": "100px",
                "type": "dimension",
                "source": "computed border-radius on GetMatterCTAButton (100px pill)",
            },
        },
        "spacing": {
            "hero": var("--mr-spacer-hero", "dimension"),
            "hero-text": var("--mr-spacer-hero-text", "dimension"),
            "xl": var("--mr-spacer-xl", "dimension"),
            "xxl": var("--mr-spacer-xxl", "dimension"),
            "margin-s": var("--mr-horizontal-margin-s", "dimension"),
            "margin-m": var("--mr-horizontal-margin-m", "dimension"),
        },
        "layout": {
            "column": var("--mr-column", "dimension"),
            "bp-mobile": var("--mr-bp-mobile", "dimension"),
            "bp-tablet": var("--mr-bp-tablet-portrait", "dimension"),
            "bp-laptop-small": var("--mr-bp-laptop-small", "dimension"),
            "bp-laptop-medium": var("--mr-bp-laptop-medium", "dimension"),
            "phone-width": var("--mr-phone-width", "dimension"),
            "logos-width": var("--mr-logos-width", "dimension"),
            "col-13": var("--mr-col-13", "dimension"),
        },
    },
    "light": {
        "page": var("--mr-color-white"),
        "surface": var("--mr-color-light-2"),
        "text": var("--mr-content-400"),
        "muted": var("--mr-color-gray"),
        "accent": var("--mr-color-blurple"),
        "border": var("--mr-color-gray-light"),
    },
    "dark": {
        "page": var("--mr-color-black"),
        "surface": var("--mr-color-dark-2"),
        "text": var("--mr-color-white"),
        "muted": var("--mr-color-gray"),
        "accent": var("--mr-color-blurple"),
        "border": var("--mr-color-dark-3"),
    },
    "component": {},
}

# Marketing page is the dark paint. The sign-in card is the light paint.
# Keep semantic roles as declared variables. Component sizes are measured.
if "nav-cta" in C and "default" in C["nav-cta"]["states"]:
    SPEC["component"]["button"] = {
        "radius": {
            "value": C["nav-cta"]["states"]["default"]["style"]["borderTopLeftRadius"],
            "type": "dimension",
            "source": "computed border-radius on the header Get Matter pill",
        },
        "font-size": {
            "value": C["nav-cta"]["states"]["default"]["style"]["fontSize"],
            "type": "dimension",
            "source": "computed font-size on the header Get Matter pill",
        },
    }
if "header" in C and "default" in C["header"]["states"]:
    SPEC["component"]["header"] = {
        "height": {
            "value": str(round(C["header"]["states"]["default"]["rect"]["h"])) + "px",
            "type": "dimension",
            "source": "measured header height on getmatter.com at 1440",
        },
    }

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("wrote component-tokens.json")
