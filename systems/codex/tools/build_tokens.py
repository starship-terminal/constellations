#!/usr/bin/env python3
"""Build tokens.json for the public Codex marketing site.

Values were read on 2026-11-22 from https://openai.com/codex/ in the T3
preview tab (incognito, signed out) and from the empty ChatGPT login wall.
The cookie banner was hidden, never accepted. Nothing was typed.

ADAPTED_FOR is set so this is not the kit's Claude example.
"""
import json
import pathlib

ADAPTED_FOR = "codex"

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "tokens.json"

CAPTURE = "https://openai.com/codex/ 2026-11-22 T3 preview, signed out, cookie banner hidden"


def src(evidence, note, capture=CAPTURE):
    return {"$extensions": {"source": {"evidence": evidence, "capture": capture, "note": note}}}


def color(value, evidence, note):
    token = {"$type": "color", "$value": value}
    token.update(src(evidence, note))
    return token


def dim(value, evidence, note):
    token = {"$type": "dimension", "$value": value}
    token.update(src(evidence, note))
    return token


def font(value, evidence, note):
    token = {"$type": "fontFamily", "$value": value}
    token.update(src(evidence, note))
    return token


def text(value, evidence, note):
    token = {"$type": "other", "$value": value}
    token.update(src(evidence, note))
    return token


# Computed custom properties on :root of https://openai.com/codex/ at 1440x900, color-scheme dark.
# Only the roles the painted page uses, plus the published radius and motion steps that resolved.
core = {
    "font": {
        "sans": font(
            "OpenAI Sans, OpenAI Sans Variable Scripts, sans-serif",
            "Computed",
            "getComputedStyle(document.body).fontFamily on https://openai.com/codex/",
        ),
        "mono": font(
            'SF Mono, Consolas, "Liberation Mono", ui-monospace, monospace',
            "Computed",
            "--font-mono on :root of https://openai.com/codex/. Not used on the hero.",
        ),
    },
    "radius": {
        "sm": dim("0.25rem", "Computed", "--radius-sm"),
        "md": dim("0.38rem", "Computed", "--radius-md"),
        "lg": dim("1rem", "Computed", "--radius-lg"),
        "2xl": dim("1rem", "Computed", "--radius-2xl"),
        "4xl": dim("2rem", "Computed", "--radius-4xl"),
        "pill": dim("40px", "Measured", "Download for macOS border-radius, 40px on a 40px control"),
    },
    "motion": {
        "duration-short": text("0.2s", "Computed", "--transition-duration-short"),
        "duration-medium": text("0.3s", "Computed", "--transition-duration-medium"),
        "duration-long": text("0.4s", "Computed", "--transition-duration-long"),
        "ease-out": text("cubic-bezier(0, 0, 0.2, 1)", "Computed", "--ease-out"),
        "ease-in": text("cubic-bezier(0.4, 0, 1, 1)", "Computed", "--ease-in"),
    },
    "space": {
        "header": dim("4rem", "Computed", "--spacing-header-h, the 64px desktop header"),
        "control-pad-x": dim("20px", "Measured", "Download for macOS padding 0 20px"),
    },
}

dark = {
    "color": {
        "page": color("#000000", "Computed", "document.body backgroundColor rgb(0, 0, 0) on the marketing page"),
        "text": color("#ffffff", "Computed", "document.body color rgb(255, 255, 255)"),
        "text-muted": color("rgba(255, 255, 255, 0.6)", "Measured", "nav link Research color"),
        "text-on-light": color("#000000", "Measured", "h1 Build anything with Codex, painted black over the hero wash"),
        "surface-nav": color("#000000", "Computed", "header paints on the page black"),
        "button-primary-bg": color("#000000", "Measured", "Download for macOS background"),
        "button-primary-text": color("#ffffff", "Measured", "Download for macOS color"),
        "button-secondary-bg": color("rgba(0, 0, 0, 0.04)", "Measured", "Try on web background, a quiet fill on the light hero"),
        "button-secondary-text": color("#000000", "Measured", "Try on web color"),
        "button-login-bg": color("rgba(255, 255, 255, 0.12)", "Measured", "Log in button on the black header"),
        "button-login-text": color("#ffffff", "Measured", "Log in button color"),
        "try-chatgpt-bg": color("#ffffff", "Derived", "Try ChatGPT is the inverse of Log in: white pill, black label. Sampled from the screenshot, not a named token."),
        "brand-gray-400": color("#8f8f8f", "Computed", "--color-brand-gray-400"),
        "brand-gray-900": color("#f9f9f9", "Computed", "--color-brand-gray-900"),
        "primary-solid-4": color("#1f1f1f", "Computed", "--color-primary-solid-4"),
        "primary-solid-12": color("#333333", "Computed", "--color-primary-solid-12"),
        "primary-solid-80": color("#cccccc", "Computed", "--color-primary-solid-80"),
    },
    "component": {
        "button-height": dim("40px", "Measured", "Download for macOS and Try on web height"),
        "login-height": dim("36px", "Measured", "Log in button height"),
        "nav-height": dim("64px", "Measured", "desktop header"),
        "h1-size": dim("64px", "Measured", "h1 font-size, line-height 64px, weight 500"),
        "button-size": dim("14px", "Measured", "Download for macOS font-size, weight 500"),
        "nav-size": dim("17px", "Measured", "nav link font-size, weight 400"),
    },
}

# Login wall is a different host. Kept as its own group so marketing tokens are not mixed with it.
login = {
    "color": {
        "page": color("#000000", "Computed", "chatgpt.com/auth/login body background, empty, nothing typed"),
        "text": color("#ededed", "Computed", "body color rgb(237, 237, 237)"),
        "continue-bg": color("#ededed", "Measured", "Continue button background"),
        "continue-text": color("#0d0d0d", "Measured", "Continue button color"),
        "provider-bg": color("#000000", "Measured", "Continue with Google background"),
        "provider-text": color("#ededed", "Measured", "Continue with Google color"),
        "provider-border": color("rgba(255, 255, 255, 0.15)", "Measured", "provider button border-top-color"),
        "field-border": color("rgba(255, 255, 255, 0.2)", "Measured", "empty email field border"),
    },
    "component": {
        "button-height": dim("52px", "Measured", "Continue and Continue with Google"),
        "field-height": dim("56px", "Measured", "empty email field"),
        "button-radius": dim("9999px", "Measured", "pill"),
        "card-width": dim("384px", "Measured", "login card width at 1440"),
        "h1-size": dim("30px", "Measured", "Log in or sign up"),
    },
}

doc = {
    "$description": "Public Codex marketing site, measured 2026-11-22. Dark is the only painted theme. Login values are a separate host and are not aliases of the marketing set.",
    "core": core,
    "dark": dark,
    "login": login,
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        {"id": "login", "name": "login", "selectedTokenSets": {"login": "enabled"}},
    ],
}

OUT.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", OUT)
