#!/usr/bin/env python3
"""Build tokens.json from Workflow's public CSS custom properties.

Sources, read from www.workflow.design on 2026-11-21 in headless Chromium:
  raw/css-vars.json            declared custom properties and their resolved values
  raw/components-computed.json computed styles of the public header button, nav link and h1

The marketing site paints one light theme. There is no dark set. Every token
carries $extensions.source. A name that was not in the stylesheet is not invented.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RESOLVED = V["resolved"]
SRC = "declared on :root in workflowdesign.webflow CSS, resolved in headless Chromium on https://www.workflow.design/ on 2026-11-21 (raw/css-vars.json)"
COMP = "computed style on https://www.workflow.design/ at 1440x900 on 2026-11-21 (raw/components-computed.json)"

NAMED = {
    "white": "#ffffff",
    "black": "#000000",
}


def norm_color(v):
    v = str(v).strip().lower()
    if v in NAMED:
        return NAMED[v]
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            r, g, b, a = [int(h[i:i + 2], 16) for i in (0, 2, 4, 6)]
            if a == 255:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %s)" % (r, g, b, "%g" % round(a / 255, 3))
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % a)
    raise ValueError("not a colour: " + v)


def color(name, description=None):
    raw = RESOLVED[name]
    val = norm_color(raw)
    token = {
        "$value": val,
        "$type": "color",
        "$extensions": {"source": f"Measured. {SRC}. {name} resolved to {raw}."},
    }
    if description:
        token["$description"] = description
    return token


def dim_from_var(name, description=None):
    raw = RESOLVED[name].strip()
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", raw):
        raise ValueError(f"{name}: not a dimension {raw!r}")
    token = {
        "$value": raw,
        "$type": "dimension",
        "$extensions": {"source": f"Measured. {SRC}. {name} = {raw}."},
    }
    if description:
        token["$description"] = description
    return token


def font_family(name):
    raw = RESOLVED[name].strip().strip('"')
    return {
        "$value": raw,
        "$type": "fontFamily",
        "$extensions": {"source": f"Measured. {SRC}. {name} = {raw}."},
    }


def group_colors(prefix):
    out = {}
    for name in sorted(RESOLVED):
        if not name.startswith(prefix):
            continue
        rest = name[len(prefix):].replace("--", ".")
        # skip the broken deleted variable if it survived
        if "deleted" in name or "<" in name:
            continue
        node = out
        parts = rest.split(".")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = color(name)
    return out


core = {
    "$description": "Primitives declared on :root of the public Workflow marketing CSS. One theme.",
    "color": {
        "base": group_colors("--color--base--"),
        "legacy": group_colors("--legacy--"),
    },
    "font": {
        "family": {
            "body": font_family("--type--body"),
            "display": font_family("--type--display"),
        }
    },
    "space": {},
    "radius": {},
}

# space and radius are dimensions, not colours. Rebuild them.
def dim_group(prefix):
    out = {}
    for name in sorted(RESOLVED):
        if not name.startswith(prefix):
            continue
        key = name[len(prefix):]
        if not re.fullmatch(r"[a-z0-9]+", key):
            continue
        out[key] = dim_from_var(name)
    return out

core["space"] = dim_group("--space--")
core["radius"] = dim_group("--radius--")

# Type roles measured on the live page, not invented from a scale the CSS does not declare.
core["typography"] = {
    "display": {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.display}",
            "fontSize": "32px",
            "fontWeight": 300,
            "lineHeight": "32px",
        },
        "$extensions": {"source": f"Measured. {COMP}. h1 on the home page."},
    },
    "body": {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.body}",
            "fontSize": "14px",
            "fontWeight": 400,
            "lineHeight": "21px",
        },
        "$extensions": {"source": f"Measured. {COMP}. document body."},
    },
    "label": {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.body}",
            "fontSize": "14px",
            "fontWeight": 400,
            "lineHeight": "21px",
        },
        "$extensions": {"source": f"Measured. {COMP}. header nav link and Try now button."},
    },
}

core["motion"] = {
    "duration": {
        "control": {
            "$value": "200ms",
            "$type": "duration",
            "$extensions": {"source": f"Derived. {COMP}. button and nav transitionDuration 0.2s, converted to ms."},
        }
    },
    "easing": {
        "control": {
            "$value": [0.455, 0.03, 0.515, 0.955],
            "$type": "cubicBezier",
            "$extensions": {"source": f"Measured. {COMP}. button and nav transitionTimingFunction."},
        }
    },
}

core["size"] = {
    "buttonHeight": {
        "$value": "40px",
        "$type": "dimension",
        "$extensions": {"source": f"Measured. {COMP}. a.button--new height."},
    },
    "headerHeight": {
        "$value": "83px",
        "$type": "dimension",
        "$extensions": {"source": "Measured. nav.nav--new getBoundingClientRect height 83 at 1440x900 on the home page, 2026-11-21."},
    },
    "logoHeight": {
        "$value": "28px",
        "$type": "dimension",
        "$extensions": {"source": f"Measured. {COMP}. a.nav-logo-link height."},
    },
}

# Flatten base colours that group_colors nested wrong for black-10 style names.
# group_colors splits on "."; black-10 stays one key. Good.

light = {
    "$description": "Semantic roles from the public :root colour tokens. No dark theme was found.",
    "background": {
        "page": color("--color--surface--page", "Warm page ground used behind marketing sections."),
        "surface": color("--color--surface--default", "Default surface. Resolves to white."),
        "raised": color("--color--surface--light", "A step above the page."),
        "sunken": color("--color--surface--secondary", "Secondary surface."),
        "strong": color("--color--surface--strong"),
        "medium": color("--color--surface--medium"),
        "invert": color("--color--surface--invert", "Ink surface. Resolves to base black."),
    },
    "text": {
        "primary": color("--color--text--default", "Resolves to base black #1a1a1a."),
        "secondary": color("--color--text--weak"),
        "disabled": color("--color--text--disabled"),
        "onAccent": color("--color--text--invert", "Light text on the ink surface."),
        "invertWeak": color("--color--text--invert-weak"),
    },
    "border": {
        "default": color("--color--border--default"),
        "strong": color("--color--border--active"),
        "hover": color("--color--border--hover"),
        "weak": color("--color--border--weak"),
    },
    "accent": {
        "default": color("--color--base--black", "The marketing accent is the ink, not a separate hue."),
        "hover": color("--legacy--hover", "Legacy hover ink, declared beside the current tokens."),
    },
    "overlay": {
        "scrim30": color("--color--overlay--30"),
        "scrim50": color("--color--overlay--50"),
        "scrim70": color("--color--overlay--70"),
    },
    "status": {
        "success": group_colors("--color--success--"),
        "error": group_colors("--color--error--"),
    },
    "icon": group_colors("--color--icon--"),
    "shadow": {
        "comment": color("--color--shadow--comment"),
        "commentDark": color("--color--shadow--comment-dark"),
    },
    "focus": {
        "ring": {
            "$value": "{color.base.black}",
            "$type": "color",
            "$extensions": {"source": f"Measured. {COMP}. outlineColor on the Try now button is rgb(26, 26, 26), the same as --color--base--black. outlineWidth was 0px, so no ring paints by default."},
        }
    },
    "component": {
        "button": {
            "background": color("--color--text--invert", "Try now resting fill matched --color--text--invert (#f6f6f6)."),
            "text": color("--color--text--default"),
            "radius": {
                "$value": "{radius.medium}",
                "$type": "dimension",
                "$extensions": {"source": f"Measured. {COMP}. a.button--new borderRadius 8px, equal to --radius--medium."},
            },
            "height": {
                "$value": "40px",
                "$type": "dimension",
                "$extensions": {"source": f"Measured. {COMP}. a.button--new height."},
            },
            "padding": {
                "$value": "8px",
                "$type": "dimension",
                "$extensions": {"source": f"Measured. {COMP}. a.button--new padding-top. Horizontal padding was 16px, recorded in components-computed.json."},
            },
        }
    },
}

# group_colors on success/error returns a nested dict of tokens already. icon too.
# accent.hover uses legacy. The alias {color.base.black} must exist.

# Fix base nesting: group_colors("--color--base--") yields keys like "black", "black-10", "white".
# Confirm.
assert "black" in core["color"]["base"], core["color"]["base"].keys()

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_checks import alias_errors  # noqa: E402

errors = alias_errors(core, light, {})
if errors:
    raise SystemExit("alias errors: " + "; ".join(errors))

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the public marketing site paints. No dark toggle was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
    "$extensions": {
        "notTokenised": [
            "Warning and info colour roles: not declared in the public CSS. Not captured.",
            "Pressed accent colour: CDP :active on Try now did not change the fill from the hover value in the reading kept here. Not captured as a separate token.",
            "Link colour as a distinct role: nav and footer links use text.primary. No separate link token was declared.",
            "Dark theme: not present on the public marketing site.",
        ]
    },
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if "$value" in v else count(v) for v in d.values() if isinstance(v, dict))


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)}")
