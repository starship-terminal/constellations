#!/usr/bin/env python3
"""Build tokens.json from the Rive public signed-out readings.

Sources, read on 2026-11-19 from the live page in a T3 preview tab at
1169 x 731 CSS px, device pixel ratio 2:

  raw/css-vars.json              declared custom properties
  raw/components-computed.json   computed styles of the controls that were measured

The marketing site paints a black page. Login and signup paint a white panel.
Docs paint #0e0c0b. There is no theme switch on these pages. Every token
carries $extensions.source. Re-running on the same inputs writes the same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent

SRC = "Measured. Computed style or declared custom property, live page, 1169 CSS px, 2026-11-19."
HOME = SRC + " https://rive.app/."
LOGIN = SRC + " https://rive.app/login/."
DOCS = SRC + " https://rive.app/docs/getting-started/introduction."
PRICE = SRC + " https://rive.app/pricing."
SIGNUP = SRC + " https://rive.app/signup/."


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(family, size, weight, line, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source},
    }


def shadow(layers, source):
    return {"$type": "shadow", "$value": layers, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


ORBITRON = "Orbitron, Inter, system-ui, sans-serif"
INTER = "Inter, system-ui, sans-serif"
PRAGMATA = "PragmataPro, ui-monospace, monospace"
JETBRAINS = "JetBrains Mono, ui-monospace, monospace"
TOMORROW = "Tomorrow, system-ui, sans-serif"

tokens = {
    "core": {
        "color": {
            "black": color("#000000", HOME + " body background rgb(0, 0, 0)."),
            "white": color("#ffffff", HOME + " GET STARTED background rgb(255, 255, 255)."),
            "amber": color("#ffa41c", LOGIN + " .site-refresh --s-highlight. Framer body token --token-86ae4b96 is #ffa41c. Docs --primary is 255 164 28."),
            "amberDeep": color("#b86e00", LOGIN + " .LoginPage_LoginInputContainer --s-highlight, the light-panel focus colour."),
            "amberSoft": color("#f6c566", LOGIN + " :root --color-amber."),
            "blue": color("#3084ff", LOGIN + " .site-refresh --s-accent. Framer --token-b0653460 is #3084ff."),
            "blueHover": color("#5a9dff", LOGIN + " .site-refresh --s-accent-hover."),
            "authBlue": color("#1f6fe5", LOGIN + " LOG IN button background rgb(31, 111, 229). The panel sets --s-accent to #1f6fe5."),
            "authBlueHover": color("#1a5bc4", LOGIN + " panel --s-accent-hover. .LoginFormButton_LoginAction__VF8hR:hover sets background-color to var(--s-accent-hover)."),
            "sky": color("#33a7ff", LOGIN + " :root --color-blue."),
            "cyan": color("#19f2ff", HOME + " Framer body token --token-f03fb86e. Not seen on a measured control."),
            "green": color("#4cbe9c", LOGIN + " :root --color-green."),
            "lime": color("#71ff19", HOME + " Framer body token --token-7ef6dc17. Not seen on a measured control."),
            "magenta": color("#f30058", HOME + " Framer body token --token-75acc5c3. Not seen on a measured control."),
            "red": color("#ff483c", HOME + " Framer body token --token-b0402e74. Not seen on a measured control."),
            "danger": color("#d42a1f", LOGIN + " panel --s-danger. .LoginForm_Error__uMJV4 sets color to var(--s-danger). The error was not shown."),
            "signalRed": color("#ff3b58", LOGIN + " :root --color-red."),
            "canvas": color("#3c2b4b", LOGIN + " .LoginPage_Animation background rgb(60, 43, 75)."),
            "pageGrey": color("#303030", LOGIN + " body background rgb(48, 48, 48)."),
            "ink": color("#222222", LOGIN + " caption color rgb(34, 34, 34)."),
            "label": color("#555555", LOGIN + " field label color rgb(85, 85, 85). Panel --s-text-muted is #555555."),
            "faint": color("#666666", SIGNUP + " fine print rgb(102, 102, 102). Panel --s-text-faint is #666666."),
            "footerLink": color("#aaaaaa", LOGIN + " footer link rgb(170, 170, 170)."),
            "legal": color("#999999", LOGIN + " footer legal link rgb(153, 153, 153)."),
            "ctaHover": color("#dfe0e3", HOME + " .rn-cta:hover and :focus-visible background rgb(223, 224, 227)."),
            "planFace": color("#1d1d1d", PRICE + " plan button background rgb(29, 29, 29). Framer --token-f5fde02c is #1d1d1d."),
            "card": color("#141414", LOGIN + " .site-refresh --s-card."),
            "field": color("#1d1d1d", LOGIN + " :root --color-field."),
            "divider": color("#323232", LOGIN + " :root --color-divider."),
            "docsPage": color("#0e0c0b", DOCS + " html background rgb(14, 12, 11). --background-dark is 14 12 11."),
            "docsText": color("#e6e3df", DOCS + " h1 color rgb(230, 227, 223). --gray-200 is 230 227 223."),
            "docsMuted": color("#a6a39f", DOCS + " nav link color rgb(166, 163, 159). --gray-400 is 166 163 159."),
            "docsBorder": color("#2d2a26", DOCS + " search border-color rgb(45, 42, 38). --gray-800 is 45 42 38."),
            "docsGray50": color("#faf7f3", DOCS + " --gray-50 250 247 243."),
            "docsGray100": color("#f5f3ee", DOCS + " --gray-100 245 243 238."),
            "docsGray300": color("#d5d3ce", DOCS + " --gray-300 213 211 206."),
            "docsGray500": color("#777470", DOCS + " --gray-500 119 116 112."),
            "docsGray600": color("#575550", DOCS + " --gray-600 87 85 80."),
            "docsGray700": color("#46433f", DOCS + " --gray-700 70 67 63."),
            "docsGray900": color("#1e1b17", DOCS + " --gray-900 30 27 23."),
            "docsGray950": color("#110f0b", DOCS + " --gray-950 17 15 11."),
            "textDisabled": color("#444444", LOGIN + " :root --color-text-disabled."),
            "textValue": color("#cccccc", LOGIN + " :root --color-text-value."),
            "textLight": color("#f1f1f1", LOGIN + " :root --color-text-light. Pricing $0 computed rgb(241, 241, 241)."),
            "textSecondary": color("#e0e0e0", LOGIN + " .site-refresh --s-text-secondary."),
            "white85": color("#ffffffd9", HOME + " nav link rgba(255, 255, 255, 0.85)."),
            "white75": color("#ffffffbf", HOME + " lede rgba(255, 255, 255, 0.75)."),
            "white05": color("#ffffff0d", HOME + " ghost control background rgba(255, 255, 255, 0.05)."),
            "white90": color("#ffffffe6", HOME + " COPY button background rgba(255, 255, 255, 0.9)."),
            "hairline": color("#ffffff17", LOGIN + " .site-refresh --s-border rgba(255,255,255,0.09)."),
            "hairlineStrong": color("#ffffff26", LOGIN + " .site-refresh --s-border-strong rgba(255,255,255,0.15)."),
            "authBorder": color("#00000033", LOGIN + " field border rgba(0, 0, 0, 0.2). Panel --s-border is the same."),
            "authBorderHover": color("#00000066", LOGIN + " .LoginInput_Input__gxjE6:hover border-color rgba(0, 0, 0, 0.4)."),
        },
        "font": {
            "family": {
                "display": {"$type": "fontFamily", "$value": ORBITRON, "$extensions": {"source": LOGIN + " --s-font-display. Home h1 computed Orbitron."}},
                "body": {"$type": "fontFamily", "$value": INTER, "$extensions": {"source": LOGIN + " --s-font-body. Home body copy computed Inter."}},
                "mono": {"$type": "fontFamily", "$value": PRAGMATA, "$extensions": {"source": HOME + " GET STARTED computed PragmataPro VF, falling back to ui-monospace."}},
                "code": {"$type": "fontFamily", "$value": JETBRAINS, "$extensions": {"source": LOGIN + " --s-font-mono. SHOW computed JetBrains Mono."}},
                "docs": {"$type": "fontFamily", "$value": TOMORROW, "$extensions": {"source": DOCS + " h1 computed Tomorrow Placeholder. The loaded face was a placeholder, so the family is recorded as Tomorrow."}},
            }
        },
        "typography": {
            "display": font(ORBITRON, "48px", 900, "48.96px", "-1.44px", HOME + " h1 48px / 48.96px, weight 900, letter-spacing -1.44px."),
            "headline": font(ORBITRON, "34px", 900, "36.72px", "-0.34px", HOME + " h2 34px / 36.72px, weight 900, letter-spacing -0.34px."),
            "authTitle": font(ORBITRON, "32px", 800, "38px", "-0.32px", LOGIN + " h1 LOG IN, 32px / 38px, weight 800, letter-spacing -0.32px."),
            "price": font(ORBITRON, "32px", 600, "36.8px", "0.64px", PRICE + " plan price 32px / 36.8px, weight 600, letter-spacing 0.64px."),
            "planName": font(ORBITRON, "20px", 600, "23px", "0.4px", PRICE + " plan name h3 20px / 23px, weight 600, letter-spacing 0.4px."),
            "docsTitle": font(TOMORROW, "36px", 600, "36px", "0px", "Reconstruction for lineHeight only: the line height was not returned as its own number, so the font size stands in for it. " + DOCS + " h1 36px, weight 600."),
            "body": font(INTER, "16px", 400, "24.8px", "0px", HOME + " lede 16px / 24.8px, weight 400."),
            "bodySmall": font(INTER, "15px", 400, "23.25px", "0px", HOME + " feature copy 15px / 23.25px."),
            "ui": font(INTER, "14px", 400, "20px", "0px", DOCS + " body 14px Inter. Login caption is 14px Inter; footer line-height was 20px."),
            "label": font(INTER, "12px", 500, "15px", "0.96px", HOME + " nav link 12px, weight 500, letter-spacing 0.96px. Computed height of the link text was 15px."),
            "button": font(PRAGMATA, "12px", 500, "15.6px", "1.2px", HOME + " GET STARTED 12px / 15.6px, weight 500, letter-spacing 1.2px."),
            "authButton": font(ORBITRON, "12px", 500, "16px", "0.96px", LOGIN + " LOG IN button 12px / 16px, weight 500, letter-spacing 0.96px."),
            "field": font(INTER, "16px", 400, "16px", "0px", "Reconstruction for lineHeight only: the computed line-height was normal, so the font size stands in for it. Size, weight and tracking are measured. " + LOGIN + " #auth-email 16px Inter."),
            "code": font(JETBRAINS, "11px", 400, "11px", "0.88px", "Reconstruction for lineHeight only: the computed line-height was normal, so the font size stands in for it. Size, weight and tracking are measured. " + LOGIN + " SHOW 11px JetBrains Mono, letter-spacing 0.88px."),
        },
        "radius": {
            "auth": dim("2px", LOGIN + " --s-radius. Field and LOG IN button border-radius."),
            "control": dim("4px", HOME + " GET STARTED, COPY, and the email field border-radius."),
            "card": dim("8px", PRICE + " plan card border-radius."),
            "search": dim("12px", DOCS + " search button border-radius."),
        },
        "spacing": {
            "2": dim("2px", LOGIN + " focus ring inner offset, 0 0 0 2px."),
            "4": dim("4px", LOGIN + " focus ring outer offset, 0 0 0 4px."),
            "5": dim("5px", HOME + " GET STARTED padding-top 5px."),
            "6": dim("6px", HOME + " GET STARTED padding-bottom 6px."),
            "9": dim("9px", HOME + " GET STARTED padding-inline 9px."),
            "10": dim("10px", LOGIN + " SHOW padding-inline 10px."),
            "12": dim("12px", LOGIN + " field padding-inline 12px."),
            "14": dim("14px", HOME + " email field padding-inline 14px."),
            "16": dim("16px", PRICE + " plan card padding 16px. Login caption padding-block 16px."),
            "20": dim("20px", LOGIN + " caption padding-inline 20px."),
            "32": dim("32px", LOGIN + " footer padding-inline 32px."),
            "40": dim("40px", HOME + " nav padding-inline 40px."),
            "48": dim("48px", LOGIN + " form padding-block 48px. Footer padding-top 48px."),
            "60": dim("60px", PRICE + " pricing section padding-top 60px."),
            "64": dim("64px", LOGIN + " --s-header-h. Home nav bar height 64px."),
        },
        "size": {
            "nav": dim("64px", HOME + " nav bar height 64px."),
            "control": dim("44px", LOGIN + " field, Google button, and LOG IN button height."),
            "planButton": dim("40px", PRICE + " plan button height."),
            "email": dim("40px", HOME + " newsletter email height."),
            "search": dim("36px", DOCS + " search button height."),
            "cta": dim("27px", HOME + " GET STARTED height."),
            "checkbox": dim("16px", SIGNUP + " checkbox 16 x 16."),
            "fieldWidth": dim("360px", LOGIN + " field width."),
            "sidebar": dim("288px", DOCS + " sidebar width."),
        },
        "border": {
            "hairline": dim("1px", LOGIN + " field border-top-width 1px."),
        },
        "shadow": {
            "ctaInset": shadow(
                [{"color": "#ffffff1a", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px"}],
                HOME + " GET STARTED box-shadow rgba(255, 255, 255, 0.1) 0 0 0 1px inset. Inset is named in the source; the shadow token stores the measured offsets.",
            ),
            "fieldInset": shadow(
                [{"color": "#ffffff26", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px"}],
                HOME + " email field box-shadow rgba(255, 255, 255, 0.15) 0 0 0 1px inset.",
            ),
        },
        "motion": {
            "duration": {
                "hover": duration("150ms", HOME + " GET STARTED transition-duration 0.15s on background. Nav link transition-duration 0.15s on color."),
                "chevron": duration("200ms", HOME + " nav chevron SVG inline style, transition transform 0.2s."),
            },
            "easing": {
                "ease": {
                    "$type": "cubicBezier",
                    "$value": [0.25, 0.1, 0.25, 1],
                    "$extensions": {"source": "Derived. The keyword ease on the home CTA. The computed value was the keyword, not these control points."},
                }
            },
        },
    },
    "dark": {
        "page": color("{color.black}", HOME + " body background."),
        "surface": color("{color.card}", LOGIN + " --s-card on the dark shell."),
        "text": color("{color.white}", HOME + " h1 color rgb(255, 255, 255)."),
        "textMuted": color("{color.white75}", HOME + " lede rgba(255, 255, 255, 0.75)."),
        "accent": color("{color.amber}", LOGIN + " --s-highlight #ffa41c."),
        "border": color("{color.hairline}", LOGIN + " --s-border."),
        "focus": color("{color.amber}", LOGIN + " dark-shell --s-focus outer ring uses --s-highlight #ffa41c."),
        "action": color("{color.white}", HOME + " GET STARTED background."),
        "actionText": color("{color.black}", HOME + " GET STARTED color."),
        "danger": color("{color.danger}", LOGIN + " --s-danger is declared on the light panel. The dark shell does not redeclare it."),
    },
    "light": {
        "page": color("{color.white}", LOGIN + " login panel background rgb(255, 255, 255)."),
        "surface": color("{color.white}", LOGIN + " panel --s-card #ffffff."),
        "text": color("{color.black}", LOGIN + " panel --s-text #000000."),
        "textMuted": color("{color.label}", LOGIN + " label color rgb(85, 85, 85)."),
        "accent": color("{color.authBlue}", LOGIN + " LOG IN background, and the panel --s-accent."),
        "border": color("{color.authBorder}", LOGIN + " field border."),
        "focus": color("{color.amberDeep}", LOGIN + " panel --s-highlight #b86e00."),
        "action": color("{color.authBlue}", LOGIN + " LOG IN and SIGN UP background."),
        "actionText": color("{color.white}", LOGIN + " LOG IN color rgb(255, 255, 255)."),
        "danger": color("{color.danger}", LOGIN + " panel --s-danger."),
    },
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

if __name__ == "__main__":
    out = HERE / "tokens.json"
    out.write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", out)
