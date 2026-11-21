#!/usr/bin/env python3
"""Build tokens.json from the Threads CSSOM dump.

Sources, read from https://www.threads.com/ on 2026-11-21, signed out:
  raw/css-vars.json  declared custom properties. The semantic set lives on
                     `:root, .__fb-light-mode:root, .__fb-light-mode` and on
                     `.__fb-dark-mode:root, .__fb-dark-mode`.
  raw/components-computed.json  computed styles of a few public controls.

A token is Measured when its value is the declaration. An alias of another
token is Derived. A value that was not in the stylesheet is not invented.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())


def root_props(theme):
    bins = V["declared"]["light"]["bins"]
    rows = bins["light"] + bins["dark"]
    if theme == "light":
        sel = ":root, .__fb-light-mode:root, .__fb-light-mode"
    else:
        sel = ".__fb-dark-mode:root, .__fb-dark-mode"
    for row in rows:
        if row["selector"] == sel and "--background-primary" in row["properties"]:
            return row["properties"], row["selector"]
    raise SystemExit("missing " + theme + " root")


LIGHT, LIGHT_SEL = root_props("light")
DARK, DARK_SEL = root_props("dark")

# Names carried into the semantic sets. Each is a declared custom property.
ROLES = {
    "page": "--background-primary",
    "surface": "--background-secondary",
    "raised": "--background-tertiary",
    "elevated": "--barcelona-elevated-background",
    "overlay": "--barcelona-elevated-header-background",
    "scrim": "--barcelona-dark-backdrop-background",
    "text": "--primary-text",
    "muted": "--secondary-text",
    "disabled": "--disabled-text",
    "placeholder": "--placeholder-text",
    "onAccent": "--barcelona-primary-button-text",
    "link": "--barcelona-link-text",
    "border": "--divider",
    "borderStrong": "--border-focused",
    "focus": "--focus-ring-blue",
    "accent": "--barcelona-primary-button",
    "accentHover": "--hover-overlay",
    "accentPressed": "--barcelona-pressed-background",
    "success": "--positive",
    "successSurface": "--positive-background",
    "warning": "--warning",
    "danger": "--negative",
    "dangerSurface": "--negative-background",
    "badge": "--notification-badge",
    "secondaryButton": "--secondary-button-background",
    "icon": "--primary-icon",
    "iconMuted": "--secondary-icon",
    "meta": "--barcelona-secondary-icon",
}

CORE_COLOR = {
    "black": "--always-black",
    "white": "--always-white",
    "fdsBlack": "--fds-black",
    "fdsBlue60": "--fds-blue-60",
    "fdsGray00": "--fds-gray-00",
    "fdsGray100": "--fds-gray-100",
    "like": "--barcelona-activity-icon-background-like",
    "reply": "--barcelona-activity-icon-background-reply",
    "repost": "--barcelona-activity-icon-background-repost",
    "follow": "--barcelona-activity-icon-background-follow",
}


def color(name, props, sel, evidence):
    raw = props[name]
    return {
        "$type": "color",
        "$value": raw,
        "$extensions": {
            "source": {
                "evidence": evidence,
                "selector": sel,
                "property": name,
                "capture": "https://www.threads.com/ 2026-11-21",
            }
        },
    }


def dim(value, source):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }


def semantic(props, sel):
    out = {}
    for token, var in ROLES.items():
        if var not in props:
            continue
        evidence = "Derived" if str(props[var]).strip().startswith("var(") else "Measured"
        out[token] = color(var, props, sel, evidence)
    return out


core = {
    "color": {k: color(v, LIGHT, LIGHT_SEL, "Measured") for k, v in CORE_COLOR.items() if v in LIGHT},
    "fontFamily": {
        "body": {
            "$type": "fontFamily",
            "$value": 'system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
            "$extensions": {
                "source": {
                    "evidence": "Measured",
                    "note": "computed font-family on body and the left rail, home, 1440",
                    "capture": "raw/pages.json bodyFont",
                }
            },
        },
        "field": {
            "$type": "fontFamily",
            "$value": "Helvetica, Arial, sans-serif",
            "$extensions": {
                "source": {
                    "evidence": "Measured",
                    "note": "computed font-family on the login username field",
                    "capture": "raw/components-computed.json field-username",
                }
            },
        },
    },
    "fontWeight": {
        "regular": {"$type": "fontWeight", "$value": 400, "$extensions": {"source": {"evidence": "Measured", "note": "nav label computed font-weight"}}},
        "semibold": {"$type": "fontWeight", "$value": 600, "$extensions": {"source": {"evidence": "Measured", "note": "Log in button computed font-weight"}}},
    },
    "typography": {
        "nav": {
            "$type": "typography",
            "$value": {"fontFamily": "{fontFamily.body}", "fontSize": "15px", "fontWeight": 400, "lineHeight": "20px"},
            "$extensions": {"source": {"evidence": "Measured", "note": "left-rail label, computed 15px / 400"}},
        },
        "button": {
            "$type": "typography",
            "$value": {"fontFamily": "{fontFamily.body}", "fontSize": "15px", "fontWeight": 600, "lineHeight": "20px"},
            "$extensions": {"source": {"evidence": "Measured", "note": "Log in button, computed 15px / 600"}},
        },
        "field": {
            "$type": "typography",
            "$value": {"fontFamily": "{fontFamily.field}", "fontSize": "15px", "fontWeight": 400, "lineHeight": "20px"},
            "$extensions": {"source": {"evidence": "Measured", "note": "login field, computed 15px / 400"}},
        },
    },
    "radius": {
        "button": dim("10px", {"evidence": "Measured", "note": "Log in button computed border-radius"}),
        "field": dim("18px", {"evidence": "Measured", "note": "login field computed border-radius"}),
        "dialog": dim("16px", {"evidence": "Not captured", "note": "dialog radius was not read from CSS; left as Not captured rather than sampled"}),
    },
    "spacing": {
        "navItem": dim("32px", {"evidence": "Measured", "note": "left-rail item computed height"}),
        "button": dim("34px", {"evidence": "Measured", "note": "Log in button computed height"}),
        "field": dim("55px", {"evidence": "Measured", "note": "login field computed height"}),
    },
    "motion": {
        "fast": {
            "$type": "duration",
            "$value": "200ms",
            "$extensions": {"source": {"evidence": "Measured", "property": "--animation-duration-fast-default-in", "note": "declared duration; easings are cubic-bezier strings and stay in raw/css-vars.json"}},
        },
    },
}

# dialog radius was not measured. Do not ship a guessed number.
del core["radius"]["dialog"]

# motion: only emit if the declaration is a plain ms value
fast = LIGHT.get("--animation-duration-fast-default-in", "")
if re.fullmatch(r"\d+ms", fast.strip()):
    core["motion"]["fast"]["$value"] = fast.strip()
else:
    del core["motion"]

tokens = {
    "$schema": "https://design-tokens.github.io/community-group/format/",
    "core": core,
    "light": semantic(LIGHT, LIGHT_SEL),
    "dark": semantic(DARK, DARK_SEL),
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Focus ring shadow is a two-layer box-shadow referencing --focus-ring-blue; see raw/css-vars.json --focus-ring-shadow-default.",
            "Animation easings are cubic-bezier custom properties (--animation-curve-*). They are declared, not copied into a cubicBezier token.",
            "Dialog corner radius, post-card radius, and icon sizes were not read. They are Not captured.",
            "Hover on the Log in button did not change its computed background in this pass.",
        ]
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", out, "light", len(tokens["light"]), "dark", len(tokens["dark"]))
