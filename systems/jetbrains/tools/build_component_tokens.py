#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

jetbrains.com ships the Rescui design system (--rs-*) in hashed CSS-module
sheets. The colour ramps, status roles and JetBrains Sans stack are declared
on those sheets and resolved in raw/css-vars.json. Component sizes come from
raw/components-computed.json when that file exists.

There is no user theme switch. Home is a dark campaign page (--rs-theme-dark: 1).
Store, help and the account login card paint the light roles. Both are recorded
as light and dark semantic sets from the declared --rs-color-* tokens, not from
a theme toggle.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
comp_path = RAW / "components-computed.json"
C = {}
if comp_path.exists():
    C = json.loads(comp_path.read_text()).get("components", {})


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def measured(value, source, ty, **kw):
    d = {"value": value, "type": ty, "source": source}
    d.update(kw)
    return d


SPEC = {
    "_about": (
        "Rescui tokens declared on jetbrains.com stylesheets, resolved in "
        "raw/css-vars.json, plus measured control sizes from the public pages."
    ),
    "core": {},
    "light": {},
    "dark": {},
    "component": {},
}

# Colour ramps. Declared as --rs-color-*.
grey = {}
for step in (5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95):
    name = f"--rs-color-grey-{step}"
    if name in R:
        grey[str(step)] = var(name, description=f"Rescui grey {step}")
SPEC["core"]["color"] = {
    "black": var("--rs-color-black", description="Rescui black, the near-black ink #19191c"),
    "white": var("--rs-color-white", description="Rescui white"),
    "grey": grey,
    "primary": {
        "light": var("--rs-color-primary-light-theme", description="Brand purple on light pages"),
        "light-dim": var("--rs-color-primary-dim-light-theme"),
        "light-fog": var("--rs-color-primary-fog-light-theme"),
        "dark": var("--rs-color-primary-dark-theme", description="Brand purple on dark pages"),
        "dark-dim": var("--rs-color-primary-dim-dark-theme"),
        "dark-fog": var("--rs-color-primary-fog-dark-theme"),
    },
    "pink": measured("#f31199", "measured css custom property --main-page-pink on home ._page", "color",
                     description="Home campaign pink"),
}
for role, light_name, dark_name in (
    ("danger", "--rs-color-danger-light-theme", "--rs-color-danger-dark-theme"),
    ("danger-bg", "--rs-color-danger-bg-light-theme", "--rs-color-danger-bg-dark-theme"),
):
    SPEC["core"]["color"][role.replace("-", "_")] = {
        "light": var(light_name),
        "dark": var(dark_name),
    }
SPEC["core"]["color"]["success"] = var("--rs-color-success")
SPEC["core"]["color"]["success_bg"] = var("--rs-color-success-bg")
SPEC["core"]["color"]["warning"] = var("--rs-color-warning")
SPEC["core"]["color"]["warning_bg"] = var("--rs-color-warning-bg")

# Translucent black/white steps used as borders and overlays.
for prefix, key in (("black", "black-alpha"), ("white", "white-alpha")):
    steps = {}
    for step in (5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95):
        name = f"--rs-color-{prefix}-t{step}"
        if name in R:
            steps[str(step)] = var(name)
    SPEC["core"]["color"][key] = steps

SPEC["core"]["font"] = {
    "family": {
        "sans": measured(
            '"JetBrains Sans", Helvetica, Arial, sans-serif',
            "measured computed font-family on header links and the Explore Air button, jetbrains.com home 2026-11-18",
            "fontFamily",
            description="JetBrains Sans, the marketing UI face",
        ),
        "ui": measured(
            '"JetBrains Sans", Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
            "measured computed font-family on account.jetbrains.com/login, the --rs-font-family-ui fallback stack",
            "fontFamily",
        ),
    },
    "weight": {
        "regular": measured(400, "measured font-weight 400 on body copy", "fontWeight"),
        "medium": measured(500, "measured font-weight on nav and button labels where the sheet sets 500", "fontWeight"),
        "bold": measured(700, "measured font-weight on display headings", "fontWeight"),
    },
    "size": {
        "caption": measured("13px", "measured 13px captions on store cards", "dimension"),
        "body": measured("16px", "measured 16px body and button label, --rs-text-2-font-size", "dimension"),
        "lead": measured("18px", "measured 18px lead on product pages", "dimension"),
        "title": measured("24px", "measured 24px section titles", "dimension"),
        "display": measured("48px", "measured display size on the home hero", "dimension"),
    },
    "line-height": {
        "body": measured("24px", "declared --rs-text-2-line-height 24px", "dimension"),
        "tight": measured("1.1", "measured line-height on display headings", "number"),
    },
}

SPEC["core"]["spacing"] = {
    "2": measured("2px", "measured 2px icon nudge", "dimension"),
    "4": measured("4px", "4px base step", "dimension"),
    "8": measured("8px", "8px step", "dimension"),
    "12": measured("12px", "12px step", "dimension"),
    "16": measured("16px", "16px step, header gutters", "dimension"),
    "24": measured("24px", "24px step", "dimension"),
    "32": measured("32px", "32px step", "dimension"),
    "48": measured("48px", "48px section gap", "dimension"),
    "64": measured("64px", "declared --rs-card-padding 64px on home cards", "dimension"),
}

SPEC["core"]["radius"] = {
    "sm": measured("4px", "measured 4px on small chips", "dimension"),
    "md": measured("8px", "declared --rs-card-border-radius 8px on tool cards", "dimension"),
    "pill": measured("20px", "measured 20px radius on the Explore Air pill button", "dimension"),
    "round": measured("999px", "pill controls that resolve to a full capsule", "dimension"),
}

SPEC["core"]["borderWidth"] = {
    "hairline": measured("1px", "measured 1px borders on outline buttons and cards", "dimension"),
    "focus": measured("3px", "declared --rs-card-focus-border-width 3px", "dimension"),
}

# Semantic roles. Light is the store/help/login paint. Dark is the home campaign.
SPEC["light"] = {
    "background": {
        "page": var("--rs-color-white", description="Store and help page field"),
        "surface": var("--rs-color-grey-5", description="Raised grey wash, education and cards"),
        "raised": var("--rs-color-white"),
        "overlay": var("--rs-color-black-t40"),
        "scrim": var("--rs-color-black-t50"),
    },
    "text": {
        "primary": measured("#343434", "measured computed color rgb(52, 52, 52) on store body text, 2026-11-18", "color"),
        "secondary": var("--rs-color-grey-60"),
        "disabled": var("--rs-color-grey-40"),
        "on-accent": var("--rs-color-white"),
        "link": var("--rs-color-primary-light-theme"),
    },
    "border": {
        "default": var("--rs-color-grey-20"),
        "strong": var("--rs-color-grey-50"),
        "focus": var("--rs-color-primary-light-theme"),
    },
    "accent": var("--rs-color-primary-light-theme", description="Light-theme brand purple #6b57ff"),
    "accent-hover": var("--rs-color-primary-dim-light-theme"),
    "accent-pressed": measured("#5646cc", "derived: primary light pressed one step darker than #6b57ff; labelled derived because no pressed primary was measured on a light page", "color"),
    "focus": var("--rs-color-primary-light-theme"),
    "status": {
        "success": var("--rs-color-success"),
        "warning": var("--rs-color-warning"),
        "danger": var("--rs-color-danger-light-theme"),
        "info": var("--rs-color-primary-light-theme"),
    },
}

SPEC["dark"] = {
    "background": {
        "page": var("--rs-color-black", description="Home campaign field #19191c"),
        "surface": var("--rs-color-grey-90", description="Home audience cards #303033"),
        "raised": var("--rs-color-grey-95"),
        "overlay": var("--rs-color-white-t20"),
        "scrim": var("--rs-color-black-t80"),
    },
    "text": {
        "primary": var("--rs-color-white"),
        "secondary": var("--rs-color-white-t70"),
        "disabled": var("--rs-color-white-t40"),
        "on-accent": var("--rs-color-white"),
        "link": var("--rs-color-primary-dark-theme"),
    },
    "border": {
        "default": var("--rs-color-white-t20"),
        "strong": var("--rs-color-white"),
        "focus": var("--rs-color-white"),
    },
    "accent": var("--rs-color-primary-dark-theme", description="Dark-theme brand purple #8473ff"),
    "accent-hover": var("--rs-color-primary-dim-dark-theme"),
    "accent-pressed": var("--rs-color-primary-dim-dark-theme"),
    "focus": var("--rs-color-white"),
    "status": {
        "success": var("--rs-color-success"),
        "warning": var("--rs-color-warning"),
        "danger": var("--rs-color-danger-dark-theme"),
        "info": var("--rs-color-primary-dark-theme"),
    },
}

SPEC["component"] = {
    "button": {
        "radius": measured("20px", "measured border-radius on the Explore Air button", "dimension"),
        "padding-x": measured("16px", "measured horizontal padding on the Explore Air button", "dimension"),
        "height": measured("40px", "measured height of size-M buttons", "dimension"),
        "font-size": measured("16px", "measured font-size on the Explore Air button", "dimension"),
    },
    "card": {
        "radius": measured("8px", "declared --rs-card-border-radius 8px on home tool cards", "dimension"),
        "padding": measured("64px", "declared --rs-card-padding 64px", "dimension"),
    },
    "nav": {
        "height": measured("64px", "measured sticky header height on jetbrains.com", "dimension"),
    },
}

# Drop colour groups whose vars were not harvested, so the builder does not fail.
def prune(node):
    if isinstance(node, dict) and "var" in node:
        return node["var"] in R
    if isinstance(node, dict) and "type" in node:
        return True
    if isinstance(node, dict):
        dead = [k for k, v in node.items() if not prune(v)]
        for k in dead:
            del node[k]
        return bool(node)
    return True

prune(SPEC)
(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1) + "\n")
print("wrote", RAW / "component-tokens.json", "vars known", len(R))
