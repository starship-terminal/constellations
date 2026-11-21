#!/usr/bin/env python3
"""Build tokens.json from Pryzm's live CSS readings.

Source: raw/css-vars.json, dumped from the CSSOM of https://pryzm.design/ on
2026-11-21. The public pages pin html.dark. A light token set is declared on
:root but is not what the public pages paint; it is kept as declared, labelled
as such, and is not a live theme capture.

Every token carries $extensions.source. Hex literals in the stylesheet are
Measured. lab() twins of the same declaration are recorded as the hex the
stylesheet also declares. Unread states stay out of this file.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())

# Prefer the hex declaration when the same name is declared twice (hex and lab).
def pick(selector, name):
    hits = [d for d in RAW["decls"] if d["selector"] == selector and d["name"] == name]
    if not hits:
        return None
    hexes = [d for d in hits if d["value"].startswith("#")]
    return (hexes or hits)[0]


def colour(selector, name, label):
    d = pick(selector, name)
    if not d:
        raise SystemExit(f"missing {selector} {name}")
    return {
        "$type": "color",
        "$value": d["value"],
        "$extensions": {
            "source": f"Measured CSS custom property {name} on {selector} ({label}), https://pryzm.design/ 2026-11-21",
            "evidence": "Measured",
        },
    }


def dim(value, source):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source, "evidence": "Measured"},
    }


def font(value, source):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": source, "evidence": "Measured"},
    }


ROLES = [
    ("page", "--background"),
    ("surface", "--card"),
    ("raised", "--popover"),
    ("sidebar", "--sidebar"),
    ("text-primary", "--foreground"),
    ("text-secondary", "--muted-foreground"),
    ("text-on-accent", "--primary-foreground"),
    ("border-default", "--border"),
    ("border-input", "--input"),
    ("accent", "--primary"),
    ("accent-foreground", "--primary-foreground"),
    ("muted", "--muted"),
    ("secondary", "--secondary"),
    ("destructive", "--destructive"),
    ("ring", "--ring"),
    ("sidebar-accent", "--sidebar-primary"),
    ("chart-1", "--chart-1"),
    ("chart-2", "--chart-2"),
    ("chart-3", "--chart-3"),
    ("chart-4", "--chart-4"),
    ("chart-5", "--chart-5"),
]

dark = {key: colour(".dark", name, "live theme, html.dark") for key, name in ROLES}
light = {key: colour(":root", name, "declared light, not painted on public pages") for key, name in ROLES}

# Sonner status colours exist only as toaster theme hooks, not as painted page roles.
for key, name in (
    ("toast-success-text", "--success-text"),
    ("toast-warning-text", "--warning-text"),
    ("toast-error-text", "--error-text"),
    ("toast-info-text", "--info-text"),
):
    hits = [d for d in RAW["decls"] if d["name"] == name and d["value"].startswith("hsl")]
    if hits:
        dark[key] = {
            "$type": "color",
            "$value": hits[0]["value"],
            "$extensions": {
                "source": f"Measured {name} on sonner toaster theme hook, not observed as a painted toast on 2026-11-21",
                "evidence": "Measured",
            },
        }

core = {
    "fontFamily": {
        "sans": font("Inter, Inter Fallback", "Measured --font-sans computed on :root, Inter loaded"),
        "heading": font("Poppins, Poppins Fallback", "Measured --font-heading computed on :root"),
        "mono": font("Geist Mono, Geist Mono Fallback", "Measured --font-mono computed on :root"),
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.fontFamily.heading}",
                "fontSize": "48px",
                "fontWeight": "600",
                "lineHeight": "1.05",
                "letterSpacing": "-0.02em",
            },
            "$extensions": {
                "source": "Derived from the home hero heading on screenshots/home-dark-default.png plus --font-heading and --tracking-heading. Exact computed size not stored in components-computed.json.",
                "evidence": "Derived",
            },
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.fontFamily.sans}",
                "fontSize": "14px",
                "fontWeight": "400",
                "lineHeight": "1.5",
            },
            "$extensions": {
                "source": "Measured computed fontSize 14px on the sign-in text field and nav link, Inter",
                "evidence": "Measured",
            },
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.fontFamily.sans}",
                "fontSize": "12px",
                "fontWeight": "500",
                "lineHeight": "1.25",
            },
            "$extensions": {
                "source": "Measured computed fontSize 12px fontWeight 500 on the studio Export button",
                "evidence": "Measured",
            },
        },
        "caption": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.fontFamily.sans}",
                "fontSize": "10px",
                "fontWeight": "600",
                "lineHeight": "1.2",
            },
            "$extensions": {
                "source": "Measured computed fontSize 10px fontWeight 600 on the PRO badge",
                "evidence": "Measured",
            },
        },
        "code": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.fontFamily.mono}",
                "fontSize": "13px",
                "fontWeight": "400",
                "lineHeight": "1.5",
            },
            "$extensions": {
                "source": "Family is Measured (--font-mono). Size is Not captured as a painted code specimen; 13px is a placeholder omitted. See gaps.",
                "evidence": "Not captured",
            },
        },
    },
    "spacing": {
        "1": dim("4px", "Derived from --spacing .25rem at a 16px root"),
        "2": dim("8px", "Derived from --spacing .25rem * 2"),
        "3": dim("12px", "Derived from --spacing .25rem * 3"),
        "4": dim("16px", "Derived from --spacing .25rem * 4"),
        "6": dim("24px", "Derived from --spacing .25rem * 6"),
        "8": dim("32px", "Derived from --spacing .25rem * 8"),
    },
    "radius": {
        "sm": dim("6px", "Derived from --radius-sm calc(.625rem * .6) = 6px"),
        "md": dim("8px", "Derived from --radius-md calc(.625rem * .8) = 8px; matches measured 8px button and field radius"),
        "lg": dim("10px", "Measured --radius .625rem = 10px"),
        "xl": dim("14px", "Derived from --radius-xl calc(.625rem * 1.4) = 14px"),
        "card": dim("18px", "Measured border radius on the gallery card and the export dialog"),
        "full": dim("9999px", "Measured pill radius on the pricing tab and PRO badge (computed 3.35544e+07px, the pill keyword)"),
    },
    "motion": {
        "duration": dim("150ms", "Measured --default-transition-duration .15s"),
        "ease": {
            "$value": "cubic-bezier(0.4, 0, 0.2, 1)",
            "$extensions": {
                "source": "Measured --default-transition-timing-function",
                "evidence": "Measured",
            },
        },
    },
    "sizing": {
        "nav-button": dim("24px", "Measured height of the marketing Open studio link"),
        "studio-button": dim("32px", "Measured height of the studio Export button"),
        "field": dim("44px", "Measured height of the sign-in email field"),
        "icon-button": dim("28px", "Measured height of the studio Undo button"),
        "switch": dim("17px", "Measured height 16.59px of the Grain enable switch, rounded"),
    },
    "layout": {
        "desktop": dim("1440px", "Capture viewport, confirmed by screenshot PNG width 1440"),
        "phone": dim("390px", "Capture viewport, confirmed by mobile PNG width 780 at 2x"),
    },
}

# Drop the code style: its size was not measured. Recording a guessed size would
# violate the evidence rule.
del core["typography"]["code"]

tokens = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"name": "dark", "group": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        {"name": "light", "group": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": {
            "liveTheme": "dark only. html has class dark on every public page. prefers-color-scheme light and dark both paint the dark set.",
            "lightSet": "Declared on :root in the stylesheet. Not observed as a painted public page.",
            "focusRing": "Not captured as a visible change. Programmatic focus on measured controls did not change background, outline or box-shadow in components-computed.json.",
            "pressed": "Not captured. The kit could not hold :active long enough for a stable reading.",
            "disabled": "Not captured. No disabled control was shown on the public pages that were opened.",
            "loading": "Not captured.",
            "errorField": "Not captured. No form was submitted, so no validation error was shown.",
            "hover": "Several controls showed no computed-style change on hover. The change may live on an inner layer or a transform. See components.md.",
            "successWarningInfo": "Declared only as sonner toaster hooks. No toast was shown.",
        }
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "dark", len(dark), "light", len(light))
