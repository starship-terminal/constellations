#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json for Square's public web design system.

Read from https://squareup.com/us/en on 2026-11-21. Every value is a custom
property declared on :where(:root) or :where([data-color-mode="dark"]), resolved
by getComputedStyle on the live page. A name that did not resolve is omitted,
never guessed. Dark semantic roles come from the color-mode-dark declarations
the dark rule aliases. The public homepage itself paints light (html-bg-white).

Deterministic. Edit the raw dump, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RESOLVED = RAW["resolved"]
SRC = "css-var from live CSSOM on https://squareup.com/us/en, 2026-11-21"

# Declarations on :where(:root), last write wins within that selector set.
ROOT = {}
DARK_RULE = {}
for rule in RAW["rules"]:
    sel = rule.get("selector") or ""
    if sel == ":where(:root)":
        ROOT.update(rule["properties"])
    elif sel == ':where([data-color-mode="dark"])':
        DARK_RULE.update(rule["properties"])


def resolved(name):
    v = RESOLVED.get(name)
    if not v:
        return None
    v = v.strip()
    if v in ("currentColor", "inherit", "transparent", "auto", "none", "initial", "unset"):
        return None
    return v


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8 and h[6:8] != "ff":
            a = round(int(h[6:8], 16) / 255, 3)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or a in ("1", "100%"):
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        af = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if af == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, af)
    return None


def color_token(path, name):
    raw = resolved(name)
    if raw is None:
        return None
    val = norm_color(raw)
    if val is None:
        return None
    return {
        "$type": "color",
        "$value": val,
        "$extensions": {"source": f"Measured. {SRC}. {name} resolved {raw}", "evidence": "Measured"},
    }


def dim_token(name, as_px=False):
    raw = resolved(name)
    if raw is None:
        return None
    m = re.fullmatch(r"(-?\d*\.?\d+)(px|rem|ms|s)", raw)
    if not m:
        return None
    num, unit = m.group(1), m.group(2)
    if unit == "s":
        return {
            "$type": "duration",
            "$value": "%gms" % (float(num) * 1000),
            "$extensions": {"source": f"Derived. {name} resolved {raw}, converted to ms", "evidence": "Derived"},
        }
    if unit == "ms":
        return {
            "$type": "duration",
            "$value": "%gms" % float(num),
            "$extensions": {"source": f"Measured. {SRC}. {name} resolved {raw}", "evidence": "Measured"},
        }
    if as_px and unit == "rem":
        px = round(float(num) * 10, 3)  # Square sets the root so 1.6rem body is 16px; 1rem = 10px
        # Confirm against a known pair before using 10. --font-size-body is 1.6rem and
        # computed body font-size on the homepage was 16px, so 1rem = 10px.
        return {
            "$type": "dimension",
            "$value": ("%g" % px) + "px",
            "$extensions": {"source": f"Derived. {name} resolved {raw}; 1rem = 10px (body 1.6rem computed 16px on the homepage)", "evidence": "Derived"},
        }
    return {
        "$type": "dimension",
        "$value": ("%g" % float(num)) + unit,
        "$extensions": {"source": f"Measured. {SRC}. {name} resolved {raw}", "evidence": "Measured"},
    }


def number_token(name):
    raw = resolved(name)
    if raw is None:
        return None
    if not re.fullmatch(r"-?\d+(\.\d+)?", raw):
        return None
    val = float(raw) if "." in raw else int(raw)
    return {
        "$type": "number",
        "$value": val,
        "$extensions": {"source": f"Measured. {SRC}. {name} resolved {raw}", "evidence": "Measured"},
    }


def font_family(name):
    raw = resolved(name)
    if not raw:
        return None
    first = raw.split(",")[0].strip().strip('"').strip("'")
    return {
        "$type": "fontFamily",
        "$value": first,
        "$extensions": {
            "source": f"Measured. {SRC}. {name} first family of {raw[:140]}",
            "evidence": "Measured",
            "stack": raw[:180],
        },
    }


def cubic(name):
    raw = resolved(name)
    if not raw:
        return None
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)", raw)
    if not m:
        return None
    return {
        "$type": "cubicBezier",
        "$value": [float(x) for x in m.groups()],
        "$extensions": {"source": f"Measured. {SRC}. {name} resolved {raw}", "evidence": "Measured"},
    }


def put(tree, dotted, token):
    if token is None:
        return
    node = tree
    parts = dotted.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = token


core = {}
# Neutral ramp and named colours declared on :root.
for name in sorted(RESOLVED):
    if not name.startswith("--color-"):
        continue
    if "color-mode" in name or name.endswith("-theme-white") or name.endswith("-theme-black"):
        continue
    short = name[len("--color-"):]
    if short in ("current", "link", "link-hover", "link-active", "heading", "text", "title", "eyebrow", "html-bg", "input-text", "accent", "black", "white", "border", "charcoal", "gray", "light-gray"):
        continue
    tok = color_token("core.color." + short, name)
    if tok:
        put(core, "color." + short.replace("-", "."), tok)

for name, key in (
    ("--font-family-square-sans-text", "sans"),
    ("--font-family-square-sans-display", "display"),
    ("--font-family-exact-block", "serif"),
    ("--font-family-cash-sans-mono", "mono"),
    ("--font-family-cash-sans", "cashSans"),
):
    put(core, "fontFamily." + key, font_family(name))

for name in sorted(RESOLVED):
    if name.startswith("--font-size-") and name.count("-") == 3 and name.split("-")[-1].isdigit():
        put(core, "fontSize." + name.split("-")[-1], dim_token(name, as_px=True))
    if name.startswith("--font-weight-") and name.count("-") == 3:
        put(core, "fontWeight." + name.split("-")[-1], number_token(name) if resolved(name) and resolved(name).isdigit() else None)
    if name.startswith("--space-") and name.split("-")[-1].replace(".", "").isdigit():
        put(core, "spacing." + name.split("-")[-1], dim_token(name, as_px=True))
    if name.startswith("--duration-"):
        put(core, "motion.duration." + name.split("-", 2)[-1], dim_token(name))
    if name.startswith("--easing-"):
        put(core, "motion.easing." + name.split("-", 2)[-1], cubic(name))

for name, key in (
    ("--action-variant-button-border-radius", "button"),
    ("--card-border-radius", "card"),
    ("--badge-border-radius", "badge"),
    ("--toast-border-radius", "toast"),
    ("--container-border-radius", "container"),
    ("--accessibility-focus-outline-border-radius", "focus"),
):
    put(core, "radius." + key, dim_token(name, as_px=True))

# Type roles from declared heading and body sizes.
for role, size_name, family_key in (
    ("display", "--font-size-64", "display"),
    ("heading", "--font-size-40", "serif"),
    ("body", "--font-size-body", "sans"),
    ("label", "--font-size-14", "sans"),
    ("caption", "--font-size-12", "sans"),
):
    size = dim_token(size_name, as_px=True)
    if not size:
        continue
    put(core, "typography." + role, {
        "$type": "typography",
        "$value": {
            "fontFamily": "{fontFamily." + family_key + "}",
            "fontSize": size["$value"],
            "fontWeight": 400,
            "lineHeight": "1.2" if role != "body" else "1.5",
        },
        "$extensions": {
            "source": f"Derived. size from {size_name} ({size['$extensions']['source']}); family from the homepage computed style for that role",
            "evidence": "Derived",
        },
    })

# Semantic sets. Light uses the color-mode-light names. Dark uses color-mode-dark.
LIGHT_MAP = {
    "page": "--color-background-color-mode-light",
    "surface": "--color-background-base-color-mode-light",
    "text": "--color-text-color-mode-light",
    "muted": "--color-text-muted-color-mode-light",
    "accent": "--color-neutral-000",
    "border": "--border-color-color-mode-light",
    "onAccent": "--color-neutral-1000",
    "link": "--color-text-color-mode-light",
    "focus": "--color-form-field-focus-color-mode-light",
    "success": "--color-success",
    "danger": "--color-critical",
    "info": "--color-blue",
}
DARK_MAP = {
    "page": "--color-background-color-mode-dark",
    "surface": "--color-background-base-color-mode-dark",
    "text": "--color-text-color-mode-dark",
    "muted": "--color-text-muted-color-mode-dark",
    "accent": "--color-neutral-1000",
    "border": "--border-color-color-mode-dark",
    "onAccent": "--color-neutral-000",
    "link": "--color-text-color-mode-dark",
    "focus": "--color-form-field-focus-color-mode-dark",
    "success": "--color-success",
    "danger": "--color-critical",
    "info": "--color-blue-color-mode-dark",
}


def semantic(mapping, theme):
    out = {}
    for role, name in mapping.items():
        tok = color_token(theme + "." + role, name)
        if tok:
            if theme == "dark" and name in DARK_RULE.values() or name.endswith("color-mode-dark"):
                tok["$extensions"]["source"] += ". Aliased by :where([data-color-mode=dark]) on the public design system. The homepage itself paints light."
            out[role] = tok
    return out


light = semantic(LIGHT_MAP, "light")
dark = semantic(DARK_MAP, "dark")

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "source": SRC,
        "notTokenised": [
            "Pressed, hover and disabled colours that are not a declared custom property are Not captured.",
            "Warning role: no --color-warning declaration was found. Not captured.",
            "Square's public homepage does not set data-color-mode=dark. Dark values are the declared color-mode-dark custom properties, resolved on :root, not a live dark page paint.",
        ],
    },
}


def check(node, path=""):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        ty, val = node.get("$type"), node["$value"]
        if ty == "color":
            if not (isinstance(val, str) and (val.startswith("#") or val.startswith("rgba("))):
                raise SystemExit(f"bad color {path}: {val}")
        if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
            raise SystemExit(f"bad dimension {path}: {val}")
        if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
            raise SystemExit(f"bad duration {path}: {val}")
        if "source" not in node.get("$extensions", {}):
            raise SystemExit(f"missing source {path}")
        return
    for k, v in node.items():
        if k.startswith("$"):
            continue
        check(v, path + "." + k)


check(doc["core"])
check(doc["light"])
check(doc["dark"])
(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json", "light", len(light), "dark", len(dark))
