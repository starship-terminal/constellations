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
# Required: every measured size below reads it, and a missing file must fail the build.
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def measured(value, source, ty, **kw):
    d = {"value": value, "type": ty, "source": source}
    d.update(kw)
    return d


HAND = "Reconstruction — entered by hand at capture time, no raw reading behind it"


def hand(value, note, ty, **kw):
    """A value typed in at capture time. Labelled as such, never as measured or declared."""
    return measured(value, f"{HAND}: {note}", ty, **kw)


def computed(comp, prop, ty, state="default", what=None, **kw):
    """A computed style read on a component in raw/components-computed.json; raises when the
    component, state or property is missing, so a recapture that loses it fails the build."""
    v = C[comp]["states"][state]["style"][prop]
    if v in (None, "", "auto", "normal"):
        raise KeyError(f"{comp} {state}: no {prop} reading")
    if ty == "fontWeight":
        v = int(v)
    return measured(v, f"computed {prop} of {comp} {state} (raw/components-computed.json)" + (f"; {what}" if what else ""), ty, **kw)


def declared(name, selector, ty, **kw):
    """A custom property declared on a selector in raw/css-vars.json (first rule whose selector
    contains `selector`); raises when no such declaration was harvested."""
    for b in ("app", "skins", "vendor", "utility"):
        for r in V.get(b, []):
            if selector in r.get("selector", "") and name in r.get("properties", {}):
                return measured(r["properties"][name], f"declared {name} on {r['selector']} (raw/css-vars.json)", ty, **kw)
    raise KeyError(f"{name} on {selector}: not in raw/css-vars.json")


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
    "pink": declared("--main-page-pink", "._page", "color", description="Home campaign pink"),
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
        "sans": computed("button-primary", "fontFamily", "fontFamily", what="the header CTA on home",
                         description="JetBrains Sans, the marketing UI face"),
        "ui": computed("email-field", "fontFamily", "fontFamily", what="account.jetbrains.com/login, the --rs-font-family-ui fallback stack"),
    },
    "weight": {
        "regular": computed("button-primary", "fontWeight", "fontWeight"),
        "medium": hand(500, "nav and button labels; every measured label reads 400", "fontWeight"),
        "bold": hand(700, "display headings; no heading was measured", "fontWeight"),
    },
    "size": {
        "caption": computed("badge", "fontSize", "dimension"),
        "body": computed("button-primary", "fontSize", "dimension"),
        "lead": hand("18px", "lead on product pages", "dimension"),
        "title": hand("24px", "section titles", "dimension"),
        "display": hand("48px", "display size on the home hero", "dimension"),
    },
    "line-height": {
        "body": computed("email-field", "lineHeight", "dimension"),
        "tight": hand("1.1", "display headings", "number"),
    },
}

# No spacing scale is declared; the steps are a suggested 4px scale. --rs-card-padding is the
# one declared spacing value (the home ._card).
SPEC["core"]["spacing"] = {
    "2": hand("2px", "icon nudge", "dimension"),
    "4": hand("4px", "base step", "dimension"),
    "8": hand("8px", "step", "dimension"),
    "12": hand("12px", "step", "dimension"),
    "16": hand("16px", "header gutters", "dimension"),
    "24": hand("24px", "step", "dimension"),
    "32": hand("32px", "step", "dimension"),
    "48": hand("48px", "section gap", "dimension"),
    "64": declared("--rs-card-padding", "._card_", "dimension"),
}

SPEC["core"]["radius"] = {
    "sm": computed("badge", "borderTopLeftRadius", "dimension"),
    "md": declared("--rs-card-border-radius", "._toolCard", "dimension"),
    "pill": computed("button-primary", "borderTopLeftRadius", "dimension", what="the Explore Air pill"),
    "round": hand("999px", "pill controls that resolve to a full capsule", "dimension"),
}

SPEC["core"]["borderWidth"] = {
    "hairline": hand("1px", "borders on outline buttons and cards", "dimension"),
    "focus": declared("--rs-card-focus-border-width", "._toolCard", "dimension"),
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
        "primary": hand("#343434", "store body text colour rgb(52, 52, 52); no raw file holds it", "color"),
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
    "accent-pressed": hand("#5646cc", "a suggested pressed step darker than #6b57ff; no pressed primary was measured on a light page", "color"),
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
        "radius": computed("button-primary", "borderTopLeftRadius", "dimension", what="the Explore Air button"),
        "padding-x": computed("button-primary", "paddingLeft", "dimension", what="the Explore Air button"),
        "height": computed("button-primary", "height", "dimension", what="a size-M button"),
        "font-size": computed("button-primary", "fontSize", "dimension", what="the Explore Air button"),
    },
    "card": {
        "radius": declared("--rs-card-border-radius", "._toolCard", "dimension"),
        "padding": declared("--rs-card-padding", "._card_", "dimension"),
    },
    "nav": {
        "height": computed("nav", "height", "dimension", what="the sticky header on jetbrains.com"),
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
if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1) + "\n")
    print("wrote", RAW / "component-tokens.json", "vars known", len(R))
