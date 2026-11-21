#!/usr/bin/env python3
"""Write systems/replit/tokens.json from raw/readings.json.

The readings were taken on 2026-11-22 from the signed-out public site.
Colours in the readings are hex from computed style, not from screenshots.
This script does not fetch the site. Re-measure in a browser, replace
raw/readings.json, then run:

    python3 tools/build_tokens.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
READINGS = ROOT / "raw" / "readings.json"
OUT = ROOT / "tokens.json"

SOURCE = (
    "computed custom property on documentElement at https://replit.com/ "
    "on 2026-11-22, signed out, color-scheme light. Hex from a probe "
    "element's computed color."
)


def color(value: str, source: str, description: str | None = None) -> dict:
    token = {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def dim(value: str, source: str) -> dict:
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }


def main() -> None:
    readings = json.loads(READINGS.read_text())
    named = readings["namedColors"]
    painted = readings["painted"]

    core_color: dict = {}
    for prop, hex_value in named.items():
        key = prop.removeprefix("--").replace("--", "-")
        core_color[key] = color(hex_value, f"{prop}. {SOURCE}")

    core_color["page"] = color(
        painted["homeBody"]["backgroundColor"],
        "computed backgroundColor of body on https://replit.com/, rgb(246, 245, 244)",
    )
    core_color["ink"] = color(
        painted["homeBody"]["color"],
        "computed color of body on https://replit.com/, rgb(24, 25, 27)",
    )
    core_color["header"] = color(
        painted["header"]["backgroundColor"],
        "computed backgroundColor of header on https://replit.com/",
    )
    core_color["footer"] = color(
        painted["footer"]["backgroundColor"],
        "computed backgroundColor of footer on https://replit.com/. The class sets bg-[hsl(33_47%_96%)].",
    )
    core_color["heading"] = color(
        painted["h1"]["color"],
        "computed color of the home h1, What will you build?",
    )
    core_color["signup"] = color(
        painted["signup"]["backgroundColor"],
        "computed backgroundColor of the header Sign up button on https://replit.com/",
    )
    core_color["on-signup"] = color(
        painted["signup"]["color"],
        "computed color of the header Sign up button",
    )
    core_color["composer"] = color(
        painted["composer"]["backgroundColor"],
        "computed backgroundColor of the home composer card",
    )
    core_color["field"] = color(
        painted["loginField"]["backgroundColor"],
        "computed backgroundColor of the empty email field on https://replit.com/login. Nothing was typed.",
    )
    core_color["provider"] = color(
        painted["identityProvider"]["backgroundColor"],
        "computed backgroundColor of Continue with Google on the empty login wall. The button was not clicked.",
    )
    core_color["link"] = color(
        painted["homeLink"]["color"],
        "computed color of the Home link on https://replit.com/login",
    )
    core_color["upgrade"] = color(
        painted["pricingUpgrade"]["backgroundColor"],
        "computed backgroundColor of Upgrade to Pro on https://replit.com/pricing. The link was not followed.",
    )
    core_color["try-now"] = color(
        painted["pricingTryNow"]["backgroundColor"],
        "computed backgroundColor of Try now on https://replit.com/pricing. The link was not followed.",
    )

    font_source = "computed fontFamily of body on https://replit.com/, and --font-family-default"
    tokens = {
        "$description": (
            "Replit public signed-out surfaces, measured 2026-11-22. "
            "The homepage, pricing, and the empty login wall paint light. "
            "prefers-color-scheme was dark and the page stayed light. "
            "No dark set."
        ),
        "core": {
            "color": core_color,
            "font": {
                "family": {
                    "sans": {
                        "$type": "fontFamily",
                        "$value": '"Replit Diatype", sans-serif',
                        "$extensions": {"source": font_source},
                    },
                    "mono": {
                        "$type": "fontFamily",
                        "$value": '"Replit Diatype Mono", monospace',
                        "$extensions": {
                            "source": "--font-family-code, and the computed family of the EXPLORE A NEW VIBE label"
                        },
                    },
                },
                "weight": {
                    "regular": {
                        "$type": "fontWeight",
                        "$value": 400,
                        "$extensions": {"source": "--font-weight-regular. Body and the home h1."},
                    },
                    "medium": {
                        "$type": "fontWeight",
                        "$value": 460,
                        "$extensions": {"source": "--font-weight-medium. Get started with templates computed 460."},
                    },
                    "signup": {
                        "$type": "fontWeight",
                        "$value": 500,
                        "$extensions": {"source": "computed fontWeight of the header Sign up button"},
                    },
                    "bold": {
                        "$type": "fontWeight",
                        "$value": 560,
                        "$extensions": {"source": "--font-weight-bold. Footer column titles computed 600."},
                    },
                },
            },
            "typography": {
                "display": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.family.sans}",
                        "fontSize": "64px",
                        "fontWeight": 400,
                        "lineHeight": "64px",
                        "letterSpacing": "-3.84px",
                    },
                    "$extensions": {
                        "source": "computed style of the home h1 at innerWidth 1169"
                    },
                },
                "section": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.family.sans}",
                        "fontSize": "32px",
                        "fontWeight": 460,
                        "lineHeight": "40px",
                        "letterSpacing": "0px",
                    },
                    "$extensions": {
                        "source": "computed style of Get started with templates"
                    },
                },
                "body": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.family.sans}",
                        "fontSize": "14px",
                        "fontWeight": 400,
                        "lineHeight": "22.4px",
                        "letterSpacing": "0px",
                    },
                    "$extensions": {
                        "source": "computed fontSize 14px of body. lineHeight uses --line-height-default 1.6"
                    },
                },
                "nav": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.family.sans}",
                        "fontSize": "14px",
                        "fontWeight": 400,
                        "lineHeight": "21px",
                        "letterSpacing": "0px",
                    },
                    "$extensions": {"source": "computed style of the Pricing nav link"},
                },
                "button": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.family.sans}",
                        "fontSize": "14px",
                        "fontWeight": 500,
                        "lineHeight": "20px",
                        "letterSpacing": "-0.28px",
                    },
                    "$extensions": {"source": "computed style of the header Sign up button"},
                },
            },
            "radius": {
                "4": dim("4px", "--radius-4"),
                "6": dim("6px", "--radius-6. Pricing nav link and pricing CTAs."),
                "8": dim("8px", "--radius-8. Header Sign up and the empty login fields."),
                "12": dim("12px", "--radius-12"),
                "16": dim("16px", "--radius-16"),
                "20": dim("20px", "--radius-20 was not a custom property. Computed borderRadius of the home composer card."),
                "24": dim("24px", "--radius-24"),
                "full": dim("9999px", "--radius-full. Computed 100px on the Start pill, which is the same full step."),
            },
            "spacing": {
                "1": dim("4px", "--spacing-100"),
                "2": dim("8px", "--spacing-200. Sign up padding-block."),
                "3": dim("12px", "--spacing-300. Sign up padding-inline."),
                "4": dim("16px", "--spacing-400"),
                "5": dim("20px", "--spacing-500"),
                "6": dim("24px", "--spacing-600"),
                "8": dim("32px", "--spacing-800"),
                "10": dim("40px", "--spacing-1000"),
                "12": dim("48px", "--spacing-1200"),
            },
            "shadow": {
                "control": {
                    "$type": "shadow",
                    "$value": {
                        "color": "#00000005",
                        "offsetX": "0px",
                        "offsetY": "1px",
                        "blur": "2px",
                        "spread": "0px",
                    },
                    "$extensions": {"source": "--shadow-control, declared 0px 1px 2px #00000005"},
                }
            },
        },
        "light": {
            "background": {
                "page": color("{core.color.page}", "body on the homepage, pricing, and the login wall"),
                "header": color("{core.color.header}", "homepage header"),
                "footer": color("{core.color.footer}", "homepage footer"),
                "surface": color(
                    "{core.color.background-default}",
                    "--background-default. The product surface token. The marketing page paints page instead.",
                ),
                "composer": color("{core.color.composer}", "home composer card"),
                "action": color("{core.color.signup}", "header Sign up"),
                "upgrade": color("{core.color.upgrade}", "Upgrade to Pro on pricing"),
            },
            "text": {
                "primary": color("{core.color.ink}", "body text"),
                "heading": color("{core.color.heading}", "home h1"),
                "muted": color(
                    "{core.color.foreground-dimmest}",
                    "--foreground-dimmest. Declared. Footer links computed #4b5563.",
                ),
                "on-action": color("{core.color.on-signup}", "Sign up label"),
                "link": color("{core.color.link}", "login Home link"),
            },
            "border": {
                "default": color("{core.color.outline-default}", "--outline-default"),
                "dimmer": color("{core.color.outline-dimmer}", "--outline-dimmer"),
                "brand": color("{core.color.brand-border}", "--brand-border"),
            },
            "accent": color("{core.color.signup}", "the orange painted on Sign up, Start, and the word Replit in the Meet Replit heading"),
        },
        "$themes": [
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "enabled", "light": "enabled"},
            }
        ],
    }
    OUT.write_text(json.dumps(tokens, indent=2) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
