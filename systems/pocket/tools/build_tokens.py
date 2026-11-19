#!/usr/bin/env python3
"""Build systems/pocket/tokens.json from raw/css-vars.json.

The readings are the custom properties declared on :root and on
.colormode-light / .colormode-dark in the public shutdown page's stylesheet
(assets.getpocket.com, chunk f421bff56e9ba7e2.css), confirmed against computed
styles on https://getpocket.com/home on 2026-11-19.

Nothing here is invented. A role that was not on the page is absent.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "css-vars.json"
OUT = ROOT / "tokens.json"

MEASURED = (
    "Measured. Declared custom property on the public shutdown page, "
    "confirmed by getComputedStyle where the page applies it."
)
DECLARED = (
    "Measured. Declared in the public stylesheet "
    "(f421bff56e9ba7e2.css). Not painted on the shutdown page."
)


def color(value: str, evidence: str) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": evidence}}


def dim(value: str, evidence: str) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": evidence}}


def font(value: str, evidence: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": evidence}}


def cubic(value: str, evidence: str) -> dict:
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": evidence}}


def shadow(value: str, evidence: str) -> dict:
    return {"$type": "shadow", "$value": value, "$extensions": {"source": evidence}}


def other(value: str, evidence: str) -> dict:
    return {"$type": "other", "$value": value, "$extensions": {"source": evidence}}


def camel_to_kebab(name: str) -> str:
    out = []
    for ch in name:
        if ch.isupper():
            out.append("-")
            out.append(ch.lower())
        else:
            out.append(ch)
    return "".join(out).strip("-")


def nest(props: dict, prefix: str, evidence: str) -> dict:
    """Turn --color-textPrimary into color.text-primary."""
    tree: dict = {}
    for key, value in props.items():
        if not key.startswith(prefix):
            continue
        rest = key[len(prefix):]
        if rest.startswith("-"):
            rest = rest[1:]
        path = camel_to_kebab(rest).split("-")
        # keep numeric tails attached: grey-10 stays grey.10
        node = tree
        for i, part in enumerate(path):
            if i == len(path) - 1:
                node[part] = color(value, evidence)
            else:
                node = node.setdefault(part, {})
    return tree


def scale(props: dict, prefix: str, evidence: str) -> dict:
    out = {}
    for key, value in sorted(props.items()):
        if not key.startswith(prefix):
            continue
        name = key[len(prefix):]
        out[name] = dim(value, evidence)
    return out


def build() -> dict:
    raw = json.loads(RAW.read_text())
    g = raw["global"]
    light = raw["light"]
    dark = raw["dark"]

    core_color = nest(g, "--color-", MEASURED)
    # palette names that are scales (grey10) become grey.10 via kebab split.
    # That is the product's own step names.

    typography = {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.serif-alt}",
                "fontSize": "38px",
                "fontWeight": 700,
                "lineHeight": "42.75px",
            },
            "$extensions": {
                "source": (
                    "Measured. Computed style of the shutdown h1 "
                    "(\"So long, farewell, Auf Wiedersehen...\") on "
                    "https://getpocket.com/home at 1169px CSS width."
                )
            },
        },
        "section": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.serif-alt}",
                "fontSize": "24px",
                "fontWeight": 700,
                "lineHeight": "28.8px",
            },
            "$extensions": {
                "source": "Measured. Computed style of the shutdown h3 headings."
            },
        },
        "lede": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "20px",
                "fontWeight": 400,
                "lineHeight": "30px",
            },
            "$extensions": {
                "source": "Measured. Computed style of the shutdown lede paragraph."
            },
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {
                "source": "Measured. Computed style of body on the shutdown page."
            },
        },
        "error-title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "40px",
                "fontWeight": 700,
                "lineHeight": "48px",
            },
            "$extensions": {
                "source": (
                    "Measured. Computed style of the h1 on the error page "
                    "returned for /privacy and /tos."
                )
            },
        },
        "error-body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "20px",
                "fontWeight": 400,
                "lineHeight": "30px",
            },
            "$extensions": {
                "source": "Measured. Computed style of the error-page paragraph."
            },
        },
    }

    motion = {
        "duration": {
            "ui-enter": dim(g["--uiControlsDurationEnterMS"], MEASURED),
            "ui-exit": dim(g["--uiControlsDurationExitMS"], MEASURED),
            "dialog-enter": dim(g["--dialogsDurationEnterMS"], MEASURED),
            "dialog-exit": dim(g["--dialogsDurationExitMS"], MEASURED),
            "drawer-enter": dim(g["--navDrawerDurationEnterMS"], MEASURED),
            "drawer-exit": dim(g["--navDrawerDurationExitMS"], MEASURED),
            "link": dim(
                "0.1s",
                "Measured. Declared transition on `a` in f421bff56e9ba7e2.css: color .1s ease-out.",
            ),
            "control": dim(
                "50ms",
                "Measured. Declared transition on checkbox, radio and toggle borders.",
            ),
        },
        "easing": {
            "standard": cubic(g["--easingStandard"], MEASURED),
            "accelerate": cubic(g["--easingAccelerate"], MEASURED),
            "decelerate": cubic(g["--easingDecelerate"], MEASURED),
        },
    }

    core = {
        "color": core_color,
        "font": {
            "family": {
                "sans": font(g["--fontSansSerif"], MEASURED),
                "serif": font(g["--fontSerif"], DECLARED),
                "serif-alt": font(g["--fontSerifAlt"], MEASURED),
            },
            "size": scale(g, "--fontSize", MEASURED),
        },
        "spacing": scale(g, "--spacing", MEASURED),
        "size": scale(g, "--size", MEASURED),
        "radius": {
            "control": dim(g["--borderRadius"], MEASURED),
            "button": dim(g["--buttonBorderRadius"], MEASURED),
        },
        "shadow": {
            "raised": shadow(
                g["--raisedCanvas"],
                "Measured. --raisedCanvas. Computed on the fixed header as rgba(0, 0, 0, 0.08) 0px 2px 12px 0px.",
            ),
            "item": shadow(g["--itemActionLight"], DECLARED),
        },
        "layout": {
            "page-clamp": dim(g["--container-pageClamp"], MEASURED),
            "top-nav-height": dim(g["--container-topNavHeight"], MEASURED),
        },
        "z": {
            "raised": other(g["--zIndexRaised"], DECLARED),
            "header": other(g["--zIndexHeader"], DECLARED),
            "tooltip": other(g["--zIndexTooltip"], DECLARED),
            "modal-shade": other(g["--zIndexModalShade"], DECLARED),
            "modal": other(g["--zIndexModal"], DECLARED),
            "color-mode-picker": other(g["--zIndexColorModePicker"], DECLARED),
        },
        "typography": typography,
        "motion": motion,
    }

    def semantic(src: dict, evidence: str) -> dict:
        return {
            "color": {
                "canvas": color(src["--color-canvas"], evidence),
                "text": {
                    "primary": color(src["--color-textPrimary"], evidence),
                    "secondary": color(src["--color-textSecondary"], evidence),
                    "tertiary": color(src["--color-textTertiary"], evidence),
                    "link-hover": color(src["--color-textLinkHover"], evidence),
                    "link-pressed": color(src["--color-textLinkPressed"], evidence),
                    "accent": color(src["--color-textAccent"], evidence),
                },
                "action": {
                    "primary": color(src["--color-actionPrimary"], evidence),
                    "primary-hover": color(src["--color-actionPrimaryHover"], evidence),
                    "primary-subdued": color(src["--color-actionPrimarySubdued"], evidence),
                    "primary-text": color(src["--color-actionPrimaryText"], evidence),
                    "secondary": color(src["--color-actionSecondary"], evidence),
                    "secondary-hover": color(src["--color-actionSecondaryHover"], evidence),
                    "secondary-hover-text": color(src["--color-actionSecondaryHoverText"], evidence),
                    "secondary-text": color(src["--color-actionSecondaryText"], evidence),
                    "brand": color(src["--color-actionBrand"], evidence),
                    "brand-hover": color(src["--color-actionBrandHover"], evidence),
                    "brand-subdued": color(src["--color-actionBrandSubdued"], evidence),
                    "brand-text": color(src["--color-actionBrandText"], evidence),
                    "focus": color(src["--color-actionFocus"], evidence),
                },
                "form": {
                    "border": color(src["--color-formFieldBorder"], evidence),
                    "border-hover": color(src["--color-formFieldBorderHover"], evidence),
                    "focus-label": color(src["--color-formFieldFocusLabel"], evidence),
                    "text": color(src["--color-formFieldTextPrimary"], evidence),
                    "text-secondary": color(src["--color-formFieldTextSecondary"], evidence),
                },
                "divider": {
                    "primary": color(src["--color-dividerPrimary"], evidence),
                    "secondary": color(src["--color-dividerSecondary"], evidence),
                    "tertiary": color(src["--color-dividerTertiary"], evidence),
                },
                "surface": {
                    "active": color(src["--color-activeCanvas"], evidence),
                    "empty": color(src["--color-emptyCanvas"], evidence),
                    "popover": color(src["--color-popoverCanvas"], evidence),
                    "drawer": color(src["--color-drawerCanvas"], evidence),
                    "tooltip": color(src["--color-tooltipCanvas"], evidence),
                },
                "error": color(src["--color-error"], evidence),
            },
            "component": {
                "button-primary": {
                    "bg": color(src["--color-actionPrimary"], evidence + " Painted on the error-page Contact Support link."),
                    "text": color(src["--color-actionPrimaryText"], evidence),
                    "radius": dim(g["--buttonBorderRadius"], MEASURED),
                },
                "button-secondary": {
                    "bg": color(src["--color-canvas"], evidence + " Painted on the shutdown-page Additional details link."),
                    "text": color(src["--color-actionSecondaryText"], evidence),
                    "radius": dim(g["--buttonBorderRadius"], MEASURED),
                },
                "button-brand": {
                    "bg": color(src["--color-actionBrand"], DECLARED + " .brand button rule. Not painted on the shutdown page."),
                    "text": color(src["--color-actionBrandText"], DECLARED),
                    "radius": dim(g["--buttonBorderRadius"], MEASURED),
                },
            },
        }

    light_evidence = (
        "Measured. .colormode-light custom property. The live page had "
        "html.colormode-light, and computed styles matched these values."
    )
    dark_evidence = (
        "Measured. .colormode-dark custom property in the same stylesheet. "
        "The live page did not paint this theme: html stayed colormode-light, "
        "and no colour-mode control was on the shutdown page. "
        "@media (prefers-color-scheme: dark) repeats these values on .colormode-system only."
    )

    return {
        "$description": (
            "Pocket public shutdown page, captured 2026-11-19 from "
            "https://getpocket.com/home. Light values were computed on the "
            "live page. Dark values are the stylesheet's .colormode-dark "
            "declarations, not a painted theme."
        ),
        "core": core,
        "light": semantic(light, light_evidence),
        "dark": semantic(dark, dark_evidence),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }


def main() -> None:
    OUT.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
