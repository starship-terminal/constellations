#!/usr/bin/env python3
"""Build tokens.json from the live Vercel dashboard reading.

Source: raw/css-vars.json, computed custom properties on documentElement
while the signed-in dashboard was in dark-theme at 1440 x 900. Only the
dark theme was on screen. Light values are not invented.

Colour tokens keep the computed CSS string. OKLCH and LAB values are not
converted to sRGB here: that conversion is a derivation, and the reading
already has the browser's string. A later pass can resolve them.

Deterministic: same inputs, same bytes.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
VARS = RAW["resolved"]
SOURCE = (
    "Measured: raw/css-vars.json resolved.%s; getComputedStyle(documentElement) "
    "on the signed-in dashboard, dark-theme, 1440x900, 2026-11-21"
)


def color(name):
    return {
        "$type": "color",
        "$value": VARS[name],
        "$extensions": {"source": SOURCE % name},
    }


def dim(name):
    return {
        "$type": "dimension",
        "$value": VARS[name],
        "$extensions": {"source": SOURCE % name},
    }


def other(name, kind):
    return {
        "$type": kind,
        "$value": VARS[name],
        "$extensions": {"source": SOURCE % name},
    }


def ramp(prefix, steps):
    return {step: color(f"--{prefix}-{step}") for step in steps}


STEPS = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "1000"]
HUES = ["gray", "blue", "red", "amber", "green", "teal", "purple", "pink"]

core = {
    "color": {hue: ramp(f"ds-{hue}", STEPS) for hue in HUES},
    "fontFamily": {
        "sans": other("--font-geist-sans", "fontFamily"),
        "mono": other("--font-mono", "fontFamily"),
        "sansFallback": other("--font-sans-fallback", "fontFamily"),
    },
    "radius": {
        "geist": dim("--geist-radius"),
        "sm": dim("--radius-sm"),
        "md": dim("--radius-md"),
        "lg": dim("--radius-lg"),
        "xl": dim("--radius-xl"),
        "popoverRow": dim("--ds-popover-row-radius"),
    },
    "spacing": {
        "unit": dim("--geist-space"),
        "2x": dim("--geist-space-2x"),
        "3x": dim("--geist-space-3x"),
        "4x": dim("--geist-space-4x"),
        "6x": dim("--geist-space-6x"),
        "8x": dim("--geist-space-8x"),
        "gap": dim("--geist-gap"),
        "gapHalf": dim("--geist-gap-half"),
        "pageMargin": dim("--geist-page-margin"),
    },
    "size": {
        "formSmall": dim("--geist-form-small-height"),
        "form": dim("--geist-form-height"),
        "formLarge": dim("--geist-form-large-height"),
        "controlSmall": dim("--ds-size-small"),
        "controlMedium": dim("--ds-size-medium"),
        "controlLarge": dim("--ds-size-large"),
        "sidebar": dim("--sidebar-width"),
        "header": dim("--header-height"),
    },
    "typography": {
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{fontFamily.sans}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {
                "source": "Measured: getComputedStyle(document.body) font-size 16px, line-height 24px, weight 400, family GeistSans; signed-in dashboard, dark-theme, 1440x900"
            },
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{fontFamily.sans}",
                "fontSize": "14px",
                "fontWeight": 500,
                "lineHeight": "20px",
            },
            "$extensions": {
                "source": "Measured: Save button, Team Settings, font-size 14px, line-height 20px, weight 500"
            },
        },
        "pageTitle": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{fontFamily.sans}",
                "fontSize": "24px",
                "fontWeight": 600,
                "lineHeight": "32px",
            },
            "$extensions": {
                "source": "Measured: Deployments h1, font-size 24px, weight 600"
            },
        },
    },
}

dark = {
    "bg": {
        "page": color("--geist-background"),
        "surface": color("--ds-background-100"),
        "raised": color("--ds-gray-100"),
    },
    "text": {
        "primary": color("--geist-foreground"),
        "secondary": color("--geist-secondary"),
        "link": color("--geist-link-color"),
    },
    "border": {
        "default": color("--ds-gray-400"),
    },
    "accent": {
        "default": color("--geist-success"),
        "link": color("--ds-blue-900"),
    },
    "focus": {
        "color": color("--ds-focus-color"),
        "ring": other("--ds-focus-ring", "shadow"),
    },
    "component": {
        "button": {
            "primary": {
                "bg": {
                    "$type": "color",
                    "$value": "rgb(237, 237, 237)",
                    "$extensions": {
                        "source": "Measured: Save button backgroundColor on Team Settings, dark-theme"
                    },
                },
                "text": {
                    "$type": "color",
                    "$value": "rgb(10, 10, 10)",
                    "$extensions": {
                        "source": "Measured: Save button color on Team Settings, dark-theme"
                    },
                },
                "radius": {
                    "$type": "dimension",
                    "$value": "6px",
                    "$extensions": {
                        "source": "Measured: Save button borderRadius on Team Settings"
                    },
                },
                "height": {
                    "$type": "dimension",
                    "$value": "32px",
                    "$extensions": {
                        "source": "Measured: Save button height on Team Settings"
                    },
                },
            }
        },
        "sidebarLink": {
            "text": {
                "$type": "color",
                "$value": "rgb(161, 161, 161)",
                "$extensions": {
                    "source": "Measured: sidebar Projects link color, dark-theme"
                },
            },
            "radius": {
                "$type": "dimension",
                "$value": "6px",
                "$extensions": {
                    "source": "Measured: sidebar Projects link borderRadius"
                },
            },
            "height": {
                "$type": "dimension",
                "$value": "36px",
                "$extensions": {
                    "source": "Measured: sidebar Projects link height"
                },
            },
        },
    },
}

# Keep the computed Geist and ds shadow strings as evidence, not a guessed scale.
shadows = {}
for name, value in sorted(VARS.items()):
    if name.startswith("--ds-shadow-") or name.startswith("--shadow-"):
        key = name.removeprefix("--").replace("-", ".")
        # Tokens Studio paths cannot start with a number after a dot in every tool.
        key = key.replace(".", "-")
        shadows[key] = {
            "$type": "shadow",
            "$value": value,
            "$extensions": {"source": SOURCE % name},
        }
core["shadow"] = shadows

out = {
    "core": core,
    "dark": dark,
    "$themes": [
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "enabled", "dark": "enabled"},
        }
    ],
    "$extensions": {
        "notTokenised": [
            "Light theme was offered (system, light, dark) and not switched. No light set is written.",
            "Hover, pressed, disabled and focus-visible component states were not forced.",
            "OKLCH and LAB custom properties are stored as the computed CSS string, not converted to sRGB.",
            "The full 559 computed custom properties stay in raw/css-vars.json. tokens.json keeps the Geist and ds roles used on the dashboard.",
        ]
    },
}

(HERE / "tokens.json").write_text(json.dumps(out, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
