#!/usr/bin/env python3
"""Build tokens.json from measured public Reflect styles.

Values are typed from the 2026-11-21 readings in raw/. The marketing site
declares almost no custom properties. Roles come from computed styles on
reflect.app and from the .button CSS rules dumped in raw/button-rules.json.
The Classic auth wall at /auth is a second surface and is labelled as such.
"""
import json
import pathlib

ADAPTED_FOR = "reflect"

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def src(label, where, file):
    return {"label": label, "where": where, "file": file}


def color(value, where, file="raw/controls.json"):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": src("Measured", where, file)},
    }


def dim(value, where, file="raw/controls.json"):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": src("Measured", where, file)},
    }


def typo(family, size, weight, line, where, file="raw/controls.json"):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": src("Measured", where, file)},
    }


def text(value, where, file):
    return {
        "$type": "other",
        "$value": value,
        "$extensions": {"source": src("Measured", where, file)},
    }


tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "font": {
            "family": {
                "display": {
                    "$type": "fontFamily",
                    "$value": "AeonikPro, system-ui, -apple-system, system-ui, Segoe UI, Roboto, sans-serif",
                    "$extensions": {"source": src("Measured", "h1 computed font-family on https://reflect.app/ at 1440", "raw/controls.json")},
                },
                "ui": {
                    "$type": "fontFamily",
                    "$value": "Inter V, system-ui, -apple-system, system-ui, Segoe UI, Roboto, sans-serif",
                    "$extensions": {"source": src("Measured", "body and nav computed font-family", "raw/home-measured.json")},
                },
                "auth": {
                    "$type": "fontFamily",
                    "$value": "Inter, ui-sans-serif, system-ui, sans-serif",
                    "$extensions": {"source": src("Measured", "email field on https://reflect.app/auth", "raw/auth-wall.json")},
                },
            }
        },
        "typography": {
            "display": typo("AeonikPro", "72px", 500, "80px", "h1 Think better with Reflect at 1440x900"),
            "heading": typo("AeonikPro", "56px", 500, "64px", "h2 on the homepage", "raw/home-measured.json"),
            "blog-title": typo("Inter", "48px", 700, "48px", "h1 Reflect Blog", "raw/blog-controls.json"),
            "body": typo("Inter V", "16px", 400, "24px", "hero subcopy"),
            "label": typo("Inter V", "14px", 400, "20px", "nav link Product"),
            "button": typo("Inter V", "14px", 500, "20px", "Download for Mac"),
        },
        "radius": {
            "control": dim("8px", "Download button and auth email field"),
            "pill": dim("32px", "Meet Reflect Open pill"),
            "tag": dim("9999px", "blog All Tags chip", "raw/blog-controls.json"),
        },
        "space": {
            "button-x": dim("16px", "button padding 8px 16px"),
            "button-y": dim("8px", "button padding 8px 16px"),
            "control": dim("36px", "Download for Mac height"),
            "field": dim("50px", "auth email field height", "raw/auth-wall.json"),
            "continue": dim("44px", "auth Continue button height", "raw/auth-buttons.json"),
        },
        "motion": {
            "button": text(
                "opacity 0.2s cubic-bezier(0.6, 0.6, 0, 1)",
                ".button::before and ::after transition",
                "raw/button-rules.json",
            )
        },
    },
    "light": {
        "color": {
            "bg": {
                "page": color("#030014", "body background-color rgb(3, 0, 20)", "raw/home-measured.json"),
                "menu": color("#030014e6", "mobile .header-nav background rgba(3, 0, 20, 0.9)", "raw/mobile-menu.json"),
                "field": color("#0f172a80", "auth email field rgba(15, 23, 42, 0.5)", "raw/auth-wall.json"),
                "legal": color("#f9fafb", "privacy page body, a light document surface", "raw/auth-buttons.json"),
            },
            "text": {
                "primary": color("#ffffff", "h1 color"),
                "secondary": color("#efedfd99", "hero subcopy rgba(239, 237, 253, 0.6)"),
                "nav": color("#ffffffe6", "nav link rgba(255, 255, 255, 0.9)"),
                "on-button": color("#f4f0ff", ".button color rgb(244, 240, 255)", "raw/button-rules.json"),
                "legal": color("#020817", "privacy and auth document ink rgb(2, 8, 23)", "raw/auth-buttons.json"),
            },
            "action": {
                "primary-wash": color("#712fff1f", ".button-primary::before rgba(113, 47, 255, 0.12)", "raw/button-rules.json"),
                "primary-hover": color("#712fff3d", ".button-primary::after rgba(113, 47, 255, 0.24)", "raw/button-rules.json"),
                "trial": color("#a855f7", "blog Start Free Trial background", "raw/blog-controls.json"),
                "continue": color("#7c3aed", "auth Continue background", "raw/auth-buttons.json"),
                "tag": color("#1e3a8a", "blog All Tags selected chip", "raw/blog-controls.json"),
            },
            "border": {
                "field": color("#1e293b", "auth email field 1px solid rgb(30, 41, 59)", "raw/auth-wall.json"),
                "secondary": color("#f3eeff14", ".button-secondary border rgba(243, 238, 255, 0.08)", "raw/button-rules.json"),
            },
        },
        "component": {
            "button": {
                "primary": {
                    "background": color("#712fff1f", ".button-primary::before wash", "raw/button-rules.json"),
                    "text": color("#f4f0ff", ".button color", "raw/button-rules.json"),
                    "radius": dim("8px", ".button border-radius", "raw/button-rules.json"),
                    "padding": text("8px 16px", ".button padding", "raw/button-rules.json"),
                    "height": dim("36px", "Download for Mac bounding box"),
                },
                "trial": {
                    "background": color("#a855f7", "Start Free Trial", "raw/blog-controls.json"),
                    "text": color("#ece5ff", "Start Free Trial text", "raw/blog-controls.json"),
                    "radius": dim("8px", "Start Free Trial radius", "raw/blog-controls.json"),
                    "height": dim("40px", "Start Free Trial height", "raw/blog-controls.json"),
                },
            }
        },
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
