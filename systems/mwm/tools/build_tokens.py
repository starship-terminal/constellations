#!/usr/bin/env python3
"""Write systems/mwm/tokens.json from raw/css-probe.json and raw/components-computed.json.

Every colour is a declared --mwm-* custom property resolved on html.dark-mode, or a
computed style on a named control. Hover and pressed button colours are Not captured:
CSS.forcePseudoState could not address the nodes, and the public sheets declare no
header-button :hover rule. Those states are omitted rather than invented.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "tokens.json"

probe = json.loads((RAW / "css-probe.json").read_text())
computed = probe["computed"]
readings = json.loads((RAW / "components-computed.json").read_text())
home = readings["pages"]["home"]
ip = readings["pages"]["ipDispute"]
gloss = readings["pages"]["glossary"]
pricing = readings["pages"]["pricing"]

DECLARED = "declared on .mwm-theme-dark, :root and resolved on html.dark-mode at https://mwm.ai/ (raw/css-probe.json, 2026-11-21)"


def color(value, source, description):
    return {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": source},
        "$description": description,
    }


def dim(value, source, description, typ="dimension"):
    return {
        "$value": value,
        "$type": typ,
        "$extensions": {"source": source},
        "$description": description,
    }


def other(value, source, description):
    return {
        "$value": value,
        "$extensions": {"source": source},
        "$description": description,
    }


def cvar(name):
    return computed[name]


tokens = {
    "core": {
        "color": {
            "ink": color(cvar("--mwm-ink"), f"{DECLARED}; --mwm-ink", "Page ink, #0c0c0c. Also the resolved --mwm-bg."),
            "ink-alt": color(cvar("--mwm-ink-alt"), f"{DECLARED}; --mwm-ink-alt", "Near-black alternate, #0d0d0d. Matches the theme-color meta #0D0D0D."),
            "surface-1": color(cvar("--mwm-surface-1"), f"{DECLARED}; --mwm-surface-1", "Raised surface. --mwm-panel aliases this on the shared theme."),
            "surface-2": color(cvar("--mwm-surface-2"), f"{DECLARED}; --mwm-surface-2", "Second surface. --mwm-panel-2 aliases this on the shared theme."),
            "surface-hover": color(cvar("--mwm-surface-hover"), f"{DECLARED}; --mwm-surface-hover", "Declared hover surface. Not measured on a hovered element."),
            "control": color(cvar("--mwm-control"), f"{DECLARED}; --mwm-control", "Control fill, #2a2a2a. Also --mwm-btn-secondary-bg."),
            "control-active": color(cvar("--mwm-control-active"), f"{DECLARED}; --mwm-control-active", "Declared active control, #3d3d3d. Not measured on a pressed element."),
            "hairline": color(cvar("--mwm-hairline"), f"{DECLARED}; --mwm-hairline", "Solid hairline, #1a1a1a. The IP form field border uses this."),
            "white": color(cvar("--mwm-text"), f"{DECLARED}; --mwm-text", "Primary text and the primary button fill, #fff."),
            "text-body": color(cvar("--mwm-text-body"), f"{DECLARED}; --mwm-text-body", "Body grey, #858585."),
            "text-muted": color(cvar("--mwm-text-muted"), f"{DECLARED}; --mwm-text-muted", "Muted grey, #9a9a9a."),
            "text-tertiary": color(cvar("--mwm-text-tertiary"), f"{DECLARED}; --mwm-text-tertiary", "Tertiary grey, #616161. Also the disabled Submit Dispute label."),
            "orange": color(cvar("--mwm-orange"), f"{DECLARED}; --mwm-orange", "Brand orange, #ff5301. Used as a selected-card ring, not as a button fill on the captured pages."),
            "orange-hot": color(cvar("--mwm-orange-hot"), f"{DECLARED}; --mwm-orange-hot", "Hotter orange, #ff4814."),
            "orange-data-muted": color(cvar("--mwm-orange-data-muted"), f"{DECLARED}; --mwm-orange-data-muted", "Orange at 72% for data marks."),
            "orange-data-border": color(cvar("--mwm-orange-data-border"), f"{DECLARED}; --mwm-orange-data-border", "Orange border at 22%."),
            "orange-data-border-strong": color(cvar("--mwm-orange-data-border-strong"), f"{DECLARED}; --mwm-orange-data-border-strong", "Orange border at 32%. The selected glossary card uses this as an inset ring."),
            "ai-grad-top": color(cvar("--mwm-ai-grad-top"), f"{DECLARED}; --mwm-ai-grad-top", "AI gradient top, #ff5732."),
            "ai-grad-bot": color(cvar("--mwm-ai-grad-bot"), f"{DECLARED}; --mwm-ai-grad-bot", "AI gradient bottom, #ff362b."),
            "glow-peak": color(cvar("--mwm-glow-peak"), f"{DECLARED}; --mwm-glow-peak", "Glow peak grey, #48494c."),
            "up": color(cvar("--mwm-up"), f"{DECLARED}; --mwm-up", "Positive movement, #2fcb6e."),
            "down": color(cvar("--mwm-down"), f"{DECLARED}; --mwm-down", "Negative movement, #ff4d4d."),
            "line": color(cvar("--mwm-line"), f"{DECLARED}; --mwm-line", "Hairline white at 10%."),
            "line-strong": color(cvar("--mwm-line-strong"), f"{DECLARED}; --mwm-line-strong", "Hairline white at 18%."),
            "muted": color(cvar("--mwm-muted"), f"{DECLARED}; --mwm-muted", "White at 60%."),
            "soft": color(cvar("--mwm-soft"), f"{DECLARED}; --mwm-soft", "White at 38%."),
            "field": color("#141414", "measured backgroundColor of the empty IP dispute text field (rgb(20, 20, 20)), same hex as --mwm-surface-1", "Form field fill."),
            "field-focus": color("#1c1c1c", "measured backgroundColor of the empty IP dispute text field after focus(), no value typed", "Form field fill while focused."),
            "field-focus-border": color("#3a3a3a", "measured borderTopColor of the empty IP dispute text field after focus()", "Form field border while focused."),
            "secondary-fill": color("rgba(255, 255, 255, 0.1)", "measured backgroundColor of the Open MWM Console link in the header at 1440x900", "Header secondary button. The token --mwm-btn-secondary-bg is #2a2a2a; this header control does not use it."),
            "chip": color("rgba(255, 255, 255, 0.05)", "measured backgroundColor of the Agent chip on the home composer", "Composer tool chip."),
            "lede": color("rgba(255, 255, 255, 0.7)", "measured color of the home lede paragraph", "Home lede. Stronger than --mwm-muted (60%)."),
            "pricing-heading": color("#f7f8f8", "measured color of the pricing h1 (rgb(247, 248, 248))", "Pricing display heading. Slightly off pure white."),
            "pricing-cta-fg": color("#000000", "measured color of Get MWM AI Pro on /pricing", "Pricing primary label is #000. The header primary label is #0c0c0c."),
            "composer-focus-ring": color("#ffffff2e", "declared box-shadow 0 0 0 2px #ffffff2e on .mwm-icon-button:focus-visible, .mwm-prompt-menu-option:focus-visible, .mwm-send:focus-visible, .mwm-tool-pill:focus-visible in https://mwm.ai/xx/index.DKqvgvwu.css", "Composer focus ring. Not measured via forcePseudoState."),
            "menu-option-hover": color("#373737", "declared background #373737 on .mwm-prompt-menu-option:hover and .mwm-prompt-menu-option.active in index.DKqvgvwu.css", "Composer menu row hover and selected row. Not measured on a hovered element."),
            "send-disabled": color("#fff3", "declared background #fff3 on .mwm-send in index.DKqvgvwu.css", "Send button before a prompt is typed. Not pressed."),
        },
        "font": {
            "ui": other(
                "Inter, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif",
                f"{DECLARED}; --mwm-font-ui. document.fonts loaded Inter 400 and 700. Computed header buttons resolve to Inter.",
                "UI face. Inter is the face that loaded.",
            ),
            "display-declared": other(
                "\"Modern Gothic\", Inter, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif",
                f"{DECLARED}; --mwm-font-display. document.fonts did not list Modern Gothic as loaded.",
                "Declared display stack. The measured home h1 resolved to Inter, not Modern Gothic.",
            ),
            "mono-declared": other(
                "\"Modern Gothic Mono\", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
                f"{DECLARED}; --mwm-font-mono. Not measured on a rendered element.",
                "Declared mono stack. Not confirmed loaded.",
            ),
            "instrument": other(
                "Instrument Sans",
                "document.fonts listed Instrument Sans 400 as loaded on https://mwm.ai/",
                "A loaded face. Not the computed family of the measured h1, buttons, or fields.",
            ),
        },
        "typography": {
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.ui}",
                    "fontSize": "72px",
                    "fontWeight": "600",
                    "lineHeight": "76px",
                    "letterSpacing": "-2.88px",
                },
                "$extensions": {"source": "measured computed style of the home h1 at 1440x900, html.dark-mode"},
                "$description": "Home display. Pricing h1 is the same size and weight, color rgb(247, 248, 248), font-family Inter, sans-serif.",
            },
            "lede": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.ui}",
                    "fontSize": "16px",
                    "fontWeight": "400",
                    "lineHeight": "24px",
                    "letterSpacing": "-0.32px",
                },
                "$extensions": {"source": "measured computed style of the home lede paragraph"},
            },
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.ui}",
                    "fontSize": "13px",
                    "fontWeight": "400",
                    "lineHeight": "16px",
                    "letterSpacing": "-0.26px",
                },
                "$extensions": {"source": "measured computed style of the Products header button"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.ui}",
                    "fontSize": "13px",
                    "fontWeight": "600",
                    "lineHeight": "16px",
                    "letterSpacing": "-0.26px",
                },
                "$extensions": {"source": "measured computed style of Build your app and Open MWM Console"},
            },
            "chip": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.ui}",
                    "fontSize": "14px",
                    "fontWeight": "500",
                    "lineHeight": "16px",
                    "letterSpacing": "-0.07px",
                },
                "$extensions": {"source": "measured computed style of the Agent chip"},
            },
            "field": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.ui}",
                    "fontSize": "12.25px",
                    "fontWeight": "400",
                    "lineHeight": "18.375px",
                    "letterSpacing": "0px",
                },
                "$extensions": {"source": "measured computed style of the empty IP dispute text field. letterSpacing was normal, recorded as 0px."},
            },
        },
        "radius": {
            "btn": dim("8px", f"{DECLARED}; --mwm-radius-btn. Also measured border-radius of header buttons, the Agent chip, form fields, and the glossary search.", "Control radius."),
            "card": dim("16px", f"{DECLARED}; --mwm-radius-card. Measured on the glossary category card.", "Card radius."),
            "panel": dim("24px", f"{DECLARED}; --mwm-radius-panel. Not measured on a panel element in this pass.", "Declared panel radius."),
        },
        "space": {
            "nav-pad-x": dim("12px", "measured paddingLeft and paddingRight of the Products button", "Header nav item horizontal padding."),
            "primary-pad-x": dim("14px", "measured paddingLeft and paddingRight of Build your app", "Header primary horizontal padding."),
            "secondary-pad-r": dim("16px", "measured paddingRight of Open MWM Console; paddingLeft was 14px", "Header secondary right padding."),
            "field-pad-x": dim("16px", "measured paddingLeft and paddingRight of the IP text field", "Field horizontal padding."),
            "field-pad-y": dim("10px", "measured paddingTop and paddingBottom of the IP text field", "Field vertical padding."),
            "card-pad": dim("18px", "measured padding of the glossary category card", "Category card padding."),
            "header-gap": dim("8px", "declared gap on .mwm-topbar-actions in index.DKqvgvwu.css", "Gap between header actions."),
            "chip-gap": dim("6px", "declared gap on .mwm-prompt-tools in index.DKqvgvwu.css", "Gap between composer chips."),
        },
        "size": {
            "header-control": dim("32px", "measured height of Products, Build your app, and Open MWM Console", "Header control height."),
            "chip": dim("40px", "measured height of the Agent chip; declared height of .mwm-tool-pill", "Composer chip height at desktop."),
            "field": dim("40px", "measured height of the IP text field, rounded from 40.375px", "Form field height."),
            "pricing-cta": dim("44px", "measured height of Get MWM AI Pro", "Pricing plan button height."),
            "search": dim("48px", "measured height of the glossary search input", "Directory search height."),
            "prompt": dim("48px", "measured height of the home prompt textarea", "Composer textarea height."),
            "submit": dim("48px", "measured height of Submit Dispute", "Form submit height."),
            "checkbox": dim("18px", "measured width and height of the IP checkbox", "Checkbox size."),
            "page": dim("1440px", "Playwright viewport width for desktop captures", "Desktop capture width."),
            "phone": dim("390px", "Playwright viewport width for phone captures", "Phone capture width."),
        },
        "tracking": {
            "eyebrow": dim("0.08em", f"{DECLARED}; --mwm-eyebrow-track", "Declared eyebrow tracking. Not measured on an eyebrow element."),
        },
        "shadow": {
            "composer-focus": other(
                "0 0 0 2px #ffffff2e",
                "declared on composer :focus-visible rules in index.DKqvgvwu.css",
                "Composer focus ring. Header buttons measured outline-style none.",
            ),
            "send-ready": other(
                "0 10px 30px #ffffff24",
                "declared on .mwm-prompt.has-prompt .mwm-send in index.DKqvgvwu.css",
                "Send button shadow after a prompt is typed. That state was not submitted and not screenshotted.",
            ),
            "send-hover": other(
                "0 14px 36px #fff3",
                "declared on .mwm-prompt.has-prompt .mwm-send:hover in index.DKqvgvwu.css",
                "Declared send hover. Not measured, and the prompt was not typed.",
            ),
            "selected-card": other(
                "rgba(255, 83, 1, 0.32) 0px 0px 0px 1px inset",
                "measured boxShadow of the glossary ASO card after click",
                "Selected category card ring. Matches --mwm-orange-data-border-strong.",
            ),
        },
        "motion": {
            "send": other(
                "background .18s ease, box-shadow .18s ease, transform .18s ease",
                "declared transition on .mwm-send in index.DKqvgvwu.css",
                "Send button transition. Captures used reduced motion.",
            ),
        },
    },
    "dark": {
        "page": color("{core.color.ink}", "alias of core.color.ink, the resolved --mwm-bg", "Page background."),
        "surface": color("{core.color.surface-1}", "alias of core.color.surface-1", "Card and field surface."),
        "surface-2": color("{core.color.surface-2}", "alias of core.color.surface-2", "Second surface."),
        "text": color("{core.color.white}", "alias of core.color.white, --mwm-text", "Primary text."),
        "muted": color("{core.color.text-muted}", "alias of core.color.text-muted, --mwm-text-muted #9a9a9a", "Muted text role used for contrast. The home lede is a separate measured white at 70%."),
        "accent": color("{core.color.orange}", "alias of core.color.orange", "Brand accent. Primary buttons are white, not orange."),
        "border": color("{core.color.line}", "alias of core.color.line", "Default hairline."),
        "border-strong": color("{core.color.line-strong}", "alias of core.color.line-strong", "Stronger hairline."),
        "up": color("{core.color.up}", "alias", "Positive."),
        "down": color("{core.color.down}", "alias", "Negative."),
        "component": {
            "button-primary-bg": color("{core.color.white}", "declared --mwm-btn-primary-bg and measured backgroundColor of Build your app", "Header primary fill."),
            "button-primary-fg": color("#0c0c0c", "declared --mwm-btn-primary-fg and measured color of Build your app", "Header primary label."),
            "button-primary-radius": dim("8px", "measured border-radius of Build your app. An older .mwm-topbar-primary rule in the same sheet declares 999px; the live header control is 8px.", "Header primary radius."),
            "button-primary-height": dim("32px", "measured height of Build your app", "Header primary height."),
            "button-secondary-bg": color("{core.color.secondary-fill}", "measured backgroundColor of Open MWM Console. Declared --mwm-btn-secondary-bg is #2a2a2a and is not this control.", "Header secondary fill."),
            "button-secondary-fg": color("{core.color.white}", "measured color of Open MWM Console", "Header secondary label."),
            "button-secondary-radius": dim("8px", "measured border-radius of Open MWM Console", "Header secondary radius."),
            "button-secondary-height": dim("32px", "measured height of Open MWM Console", "Header secondary height."),
            "button-pricing-bg": color("{core.color.white}", "measured backgroundColor of Get MWM AI Pro", "Pricing plan button fill."),
            "button-pricing-fg": color("{core.color.pricing-cta-fg}", "measured color of Get MWM AI Pro", "Pricing plan button label."),
            "button-pricing-height": dim("44px", "measured height of Get MWM AI Pro", "Pricing plan button height."),
            "button-disabled-bg": color("{core.color.control}", "measured backgroundColor of Submit Dispute while the empty form is incomplete", "Disabled submit fill. The control was not hovered or pressed."),
            "button-disabled-fg": color("{core.color.text-tertiary}", "measured color of Submit Dispute", "Disabled submit label."),
            "field-bg": color("{core.color.field}", "measured backgroundColor of the empty IP text field", "Field fill."),
            "field-fg": color("{core.color.white}", "measured color of the empty IP text field", "Field text."),
            "field-border": color("{core.color.hairline}", "measured borderTopColor rgb(26, 26, 26) of the empty IP text field", "Field border."),
            "field-radius": dim("8px", "measured border-radius of the IP text field", "Field radius."),
            "field-focus-bg": color("{core.color.field-focus}", "measured after focus() on the empty IP text field", "Focused field fill."),
            "field-focus-border": color("{core.color.field-focus-border}", "measured borderTopColor after focus()", "Focused field border."),
            "search-bg": color("{core.color.ink}", "measured backgroundColor of the glossary search, rgb(12, 12, 12)", "Directory search fill."),
            "search-height": dim("48px", "measured height of the glossary search", "Directory search height."),
            "card-bg": color("{core.color.surface-2}", "measured backgroundColor of the glossary category card, rgb(24, 24, 24)", "Category card fill."),
            "card-radius": dim("16px", "measured border-radius of the glossary category card", "Category card radius."),
            "card-selected-bg": color("{core.color.surface-hover}", "measured backgroundColor of the glossary ASO card after click, rgb(29, 29, 29)", "Selected category card fill."),
            "nav-fg": color("{core.color.white}", "measured color of the Products button", "Header nav label."),
            "nav-height": dim("32px", "measured height of the Products button", "Header nav item height."),
            "chip-bg": color("{core.color.chip}", "measured backgroundColor of the Agent chip", "Composer chip fill."),
            "chip-radius": dim("8px", "measured border-radius of the Agent chip", "Composer chip radius."),
            "chip-height": dim("40px", "measured height of the Agent chip", "Composer chip height."),
        },
    },
    "$themes": [
        {
            "id": "dark",
            "name": "dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
        }
    ],
    "$extensions": {
        "notTokenised": [
            "Hover and pressed colours of header buttons, pricing CTAs, and Submit Dispute. CSS.forcePseudoState failed with 'Could not find node with given id'. The captured stylesheets declare no :hover rule for those controls.",
            "Focus ring of header buttons. Measured outline-style was none. The only declared focus-visible ring is the composer rule 0 0 0 2px #ffffff2e.",
            "Light theme. html.dark-mode is the only public theme. No theme switch was found.",
            "Home-scoped --mwm-lilac, --mwm-gold, --mwm-green, and the hero spacing variables. They resolved empty on html, outside .mwm-home.",
            "Modern Gothic and Modern Gothic Mono. Declared, not listed in document.fonts, and the measured display resolved to Inter.",
            "Signed-in Console and Create App. Login walls. Not entered.",
            "A spacing scale. The product does not publish one. Only measured paddings and a few declared gaps are recorded.",
        ],
        "readings": {
            "css": "raw/css-probe.json",
            "components": "raw/components-computed.json",
            "viewport": home["viewport"],
            "pricingH1Color": pricing["h1"]["color"],
            "glossarySelectedShadow": gloss["asoSelected"]["boxShadow"],
            "fieldFocus": {
                "backgroundColor": ip["fieldFocus"]["backgroundColor"],
                "borderTopColor": ip["fieldFocus"]["borderTopColor"],
            },
        },
    },
}

OUT.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
