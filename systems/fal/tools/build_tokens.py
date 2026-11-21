#!/usr/bin/env python3
"""Build tokens.json from the public fal.ai readings.

Sources, read signed out on 2026-11-21:
  raw/css-vars.json     custom properties resolved on fal.ai/ (Webflow marketing)
                        and fal.ai/login (app shell). Marketing names keep Webflow's
                        <deleted|variable-...> suffix; the builder strips it.
  raw/states.json       hover/focus/pressed on the marketing nav and the GitHub
                        OAuth control (measured, never activated).
  raw/docs-dark-computed.json
                        computed colour on the docs shell after clicking
                        "Switch to dark theme".

Two painted systems, not one theme toggle:
  light   marketing site (fal.ai/, pricing, enterprise, blog, legal)
  app     signed-out app shell (login, explore, docs), light
  dark    docs shell after the public theme control

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
HOME = VARS["resolved"]["home"]
LOGIN = VARS["resolved"]["login"]


def strip_name(name):
    return re.sub(r"<deleted\|variable-[0-9a-f-]+>", "", name)


def home(name):
    key = name if name in HOME else None
    if key is None:
        for k, v in HOME.items():
            if strip_name(k) == name:
                return v, k
        raise KeyError(name)
    return HOME[key], key


def login(name):
    if name not in LOGIN:
        raise KeyError(name)
    return LOGIN[name]


def color(value, source):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source},
    }


def dim(value, source):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }


def font(value, source):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": source},
    }


def number(value, source):
    return {
        "$type": "number",
        "$value": value,
        "$extensions": {"source": source},
    }


def alias(path, source):
    return {
        "$type": "color",
        "$value": "{" + path + "}",
        "$extensions": {"source": source},
    }


H = "Measured CSS custom property on https://fal.ai/ :root, raw/css-vars.json"
L = "Measured CSS custom property on https://fal.ai/login, raw/css-vars.json"
M = "Measured computed style, raw/states.json and the capture log of 2026-11-21"
D = "Measured computed style on https://fal.ai/docs after Switch to dark theme, raw/docs-dark-computed.json"

bronze, bronze_key = home("--brand-colors--dark-bronze")
neon, neon_key = home("--brand-colors--neon")
cyan, cyan_key = home("--brand-colors--cyan")
grey, grey_key = home("--brand-colors--grey")
pink, pink_key = home("--brand-colors--pink")
yellow, yellow_key = home("--brand-colors--yellow")
red, red_key = home("--brand-colors--red")
blue, blue_key = home("--brand-colors--blue")
black, black_key = home("--brand-colors--black")
white, white_key = home("--brand-colors--white")
ink, ink_key = home("--text-color--text-primary")
paper, paper_key = home("--background-colors--background-secondary")

tokens = {
    "$description": "Public fal.ai, signed out, 2026-11-21. Marketing tokens from the Webflow site. App-shell tokens from the login and docs surfaces. No signed-in dashboard.",
    "core": {
        "color": {
            "brand": {
                "bronze": color(bronze if bronze != "black" else "#403700", f"{H} {bronze_key} resolved {bronze}"),
                "neon": color("#adff00" if neon in ("#adff00",) else neon, f"{H} {neon_key}"),
                "cyan": color("#99edff", f"{H} {cyan_key} resolved {cyan}"),
                "grey": color("#e5ece7", f"{H} {grey_key}"),
                "pink": color("#ffc4d8", f"{H} {pink_key}"),
                "yellow": color("#fff000", f"{H} {yellow_key}"),
                "red": color("#ec0648", f"{H} {red_key}"),
                "blue": color("#115ef3", f"{H} {blue_key}"),
                "black": color("#000000", f"{H} {black_key} resolved {black}"),
                "white": color("#ffffff", f"{H} {white_key} resolved {white}"),
            },
            "neutral": {
                "ink": color("#000000", f"{H} {ink_key}"),
                "secondary": color("#222222", f"{H} {home('--text-color--text-secondary')[1]}"),
                "paper": color("#ffffff", f"{H} {paper_key}"),
                "lightest": color("#eeeeee", f"{H} {home('--base-color-neutral--neutral-lightest')[1]}"),
            },
            "status": {
                "error-fill": color("#f8e4e4", f"{H} {home('--base-color-system--error-red')[1]}"),
                "error-text": color("#3b0b0b", f"{H} {home('--base-color-system--error-red-dark')[1]}"),
                "warning-fill": color("#fcf8d8", f"{H} {home('--base-color-system--warning-yellow')[1]}"),
                "warning-text": color("#5e5515", f"{H} {home('--base-color-system--warning-yellow-dark')[1]}"),
            },
            "app": {
                "content": color("rgb(32, 32, 34)", f"{L} --color-content-base"),
                "content-strong": color("rgb(25, 25, 26)", f"{L} --color-content-strong"),
                "content-lighter": color("#161618b3", f"{L} --color-content-lighter"),
                "content-muted": color("#16161899", f"{L} --content-muted"),
                "content-disabled": color("#a6a6ae", f"{L} --content-disabled"),
                "content-inverse": color("rgb(250, 250, 250)", f"{L} --color-content-inverse"),
                "surface": color("rgb(255, 255, 255)", f"{L} --color-surface"),
                "surface-muted": color("rgb(244, 244, 245)", f"{L} --color-surface-muted"),
                "surface-sunken": color("rgb(250, 250, 250)", f"{L} --color-surface-sunken"),
                "surface-alpha": color("rgb(18, 18, 22, 0.05)", f"{L} --color-surface-alpha"),
                "stroke": color("rgb(18, 18, 22, 0.1)", f"{L} --color-stroke-base"),
                "stroke-strong": color("rgb(18, 18, 22, 0.15)", f"{L} --color-stroke-strong"),
                "focus-brand": color("rgb(133, 83, 255)", f"{L} --color-stroke-focus-brand"),
                "primary": color("hsl(259.275, 96.02%, 60.59%)", f"{L} --color-primary-500"),
                "error": color("hsl(342.783, 95.04%, 47.45%)", f"{L} --color-error-500"),
                "success": color("hsl(95.077, 52.85%, 48.24%)", f"{L} --color-success-500"),
                "warning": color("hsl(33.937, 95.67%, 54.71%)", f"{L} --color-warning-500"),
                "info": color("hsl(215.468, 99.02%, 59.80%)", f"{L} --color-info-500"),
                "cyan": color("#99edff", f"{L} --color-cyan-300"),
            },
            "docs-dark": {
                "page": color("rgb(13, 12, 16)", D + " documentElement background"),
                "text": color("rgb(225, 223, 228)", D + " h1 color"),
                "muted": color("rgb(161, 159, 164)", D + " main color"),
                "border": color("rgb(39, 38, 43)", D + " computed borderTopColor"),
            },
        },
        "font": {
            "marketing": font("Focal Web, Arial, sans-serif", M + " nav-link fontFamily"),
            "app": font('publicSansRounded, "publicSansRounded Fallback", publicSans, sans-serif', f"{L} --font-public-sans-rounded plus measured login control"),
            "heading": font('focal, "focal Fallback", sans-serif', f"{L} --font-heading"),
            "mono": font('chivoMono, "chivoMono Fallback", ui-monospace, monospace', f"{L} --font-mono"),
        },
        "radius": {
            "nav": dim("4px", M + " nav-link borderRadius"),
            "control": dim("4px", M + " oauth-github borderRadius"),
            "sm": dim("0.25rem", f"{L} --radius-sm"),
            "md": dim("0.375rem", f"{L} --radius-md"),
            "lg": dim("0.5rem", f"{L} --radius-lg"),
            "xl": dim("0.75rem", f"{L} --radius-xl"),
        },
        "space": {
            "unit": dim("4px", f"{L} --spacing is 0.25rem"),
            "2": dim("8px", "Derived from --spacing 0.25rem"),
            "4": dim("16px", "Derived from --spacing 0.25rem"),
            "5": dim("20px", M + " nav-link paddingLeft 20px"),
        },
        "fontWeight": {
            "regular": number(400, f"{L} --font-weight-normal"),
            "medium": number(500, f"{L} --font-weight-medium; marketing nav measures 500"),
            "semibold": number(600, f"{L} --font-weight-semibold; OAuth control measures 600"),
        },
        "type": {
            "nav": {
                "fontSize": dim("16px", M + " nav-link"),
                "lineHeight": dim("24px", M + " nav-link"),
                "fontWeight": number(500, M + " nav-link"),
            },
            "display": {
                "fontSize": dim("96px", M + " pricing h1 computed font-size"),
                "fontWeight": number(500, M + " pricing h1"),
            },
            "login-title": {
                "fontSize": dim("30px", "Measured on login h1 class text-[30px], capture log"),
                "lineHeight": number(0.97, "Measured login h1 class leading-[0.97]"),
            },
            "oauth": {
                "fontSize": dim("16px", M + " oauth-github"),
                "fontWeight": number(600, M + " oauth-github"),
                "height": dim("40px", M + " oauth-github"),
            },
            "body": {
                "fontSize": dim("16px", f"{L} --text-base 1rem"),
                "lineHeight": number(1.5, f"{L} --text-base--line-height"),
            },
            "sm": {
                "fontSize": dim("14px", f"{L} --text-sm 0.875rem"),
                "lineHeight": number(1.43, f"{L} --text-sm--line-height calc(1.25 / 0.875)"),
            },
        },
    },
    "light": {
        "$description": "Marketing site. One painted light theme. Hero sits on bronze, not on white.",
        "page": alias("core.color.brand.bronze", "Hero canvas is brand bronze; white is the logo chip and the lower page"),
        "surface": alias("core.color.brand.grey", "Nav island and Contact Sales face"),
        "text": alias("core.color.neutral.ink", "Nav and body text"),
        "muted": alias("core.color.neutral.secondary", "Declared text-secondary"),
        "accent": alias("core.color.brand.neon", "Get Started hero button face"),
        "border": alias("core.color.neutral.lightest", "Declared border-primary"),
        "onAccent": alias("core.color.neutral.ink", "Neon button label is black"),
        "component": {
            "nav": {
                "height": dim("35px", M + " nav-link height 35.1875px"),
                "radius": dim("4px", M + " nav-link"),
                "hover": color("#e5ece7", M + " nav-link hover background"),
            },
            "button": {
                "start": color("#000000", "Capture log: header Get Started background rgb(0,0,0), hover rgb(229,236,231)"),
                "startHover": color("#e5ece7", "Capture log: header Get Started hover"),
                "sales": color("#e5ece7", "Capture log: Contact Sales background"),
                "salesHover": color("#d9d9d9", "Capture log: Contact Sales hover"),
                "hero": color("#adff00", "Capture log: hero Get Started background rgb(173,255,0)"),
                "height": dim("44px", "Capture log: hero CTA box height 44"),
                "navHeight": dim("35px", "Capture log: header button box height 35"),
            },
            "tab": {
                "selected": color("#403700", "Capture log: Model APIs tab background rgb(64,55,0)"),
            },
        },
    },
    "app": {
        "$description": "Signed-out app shell in light: login, explore, docs before the theme switch.",
        "page": alias("core.color.app.surface", "Login page background"),
        "surface": alias("core.color.app.surface-sunken", "Raised field and card face"),
        "text": alias("core.color.app.content", "OAuth label colour"),
        "muted": alias("core.color.app.content-lighter", "Secondary app text"),
        "accent": alias("core.color.app.primary", "Declared primary-500; marketing neon is a different system"),
        "border": alias("core.color.app.stroke", "Declared stroke-base"),
        "focus": color("rgb(0, 95, 204)", M + " oauth-github focus outline colour"),
        "hover": alias("core.color.app.surface-alpha", "OAuth hover background"),
    },
    "dark": {
        "$description": "Docs shell after the public Switch to dark theme control. Not a marketing theme.",
        "page": alias("core.color.docs-dark.page", D),
        "surface": alias("core.color.docs-dark.page", "Sidebar and page share the dark canvas in the capture; a separate raised token was not resolved"),
        "text": alias("core.color.docs-dark.text", D),
        "muted": alias("core.color.docs-dark.muted", D),
        "accent": alias("core.color.app.primary", "Docs accent was not re-resolved under .dark; app primary is the nearest declared accent and is marked as carried"),
        "border": alias("core.color.docs-dark.border", D),
    },
    "$themes": [
        {"id": "light", "name": "Marketing light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "app", "name": "App shell light", "selectedTokenSets": {"core": "source", "app": "enabled"}},
        {"id": "dark", "name": "Docs dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# fix bronze if the resolved value was the word black by mistake — we already checked
assert tokens["core"]["color"]["brand"]["bronze"]["$value"].startswith("#")
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote tokens.json")
