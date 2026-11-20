#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Kraken publishes a design-system layer as custom properties. This builder
reads the values the browser resolved on the body of the public light page
(www.kraken.com, data-theme=magic-light) and the public dark page
(www.kraken.com/pro, data-theme=magic-dark) on 2026-11-18.

core holds scales that do not change with theme (radius, elevation, type,
motion, the brand primitive). light and dark hold the semantic colour roles
resolved in that theme. Every token carries $extensions.source naming the
custom property. A value that is still a var() is skipped rather than guessed.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
LIGHT = RAW["resolved"]["light"]
DARK = RAW["resolved"]["dark"]
CAPTURED = RAW.get("captured", "2026-11-18")


def norm_color(v):
    v = v.strip().lower()
    if v in ("transparent", "#0000", "#fff0"):
        return "rgba(0, 0, 0, 0)"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
            a = int(h[6:8], 16) / 255
            if a >= 0.999:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if a >= 0.999:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, round(a, 3))
    raise ValueError("not a colour: " + v)


def is_color(v):
    try:
        norm_color(v)
        return True
    except ValueError:
        return False


def rem_to_px(v):
    v = v.strip()
    m = re.fullmatch(r"(-?[\d.]+)rem", v)
    if m:
        return "%gpx" % (float(m.group(1)) * 16)
    m = re.fullmatch(r"(-?[\d.]+)px", v)
    if m:
        return "%gpx" % float(m.group(1))
    return None


def color_token(name, value, description=None):
    return {
        "$value": norm_color(value),
        "$type": "color",
        "$description": description or name,
        "$extensions": {"source": f"Measured css-var {name} resolved on body, kraken.com, {CAPTURED}"},
    }


def dim_token(name, value, description=None):
    px = rem_to_px(value)
    if not px:
        raise ValueError(name + " " + value)
    return {
        "$value": px,
        "$type": "dimension",
        "$description": description or f"{name} = {value}",
        "$extensions": {"source": f"Derived from css-var {name} ({value}) at 16px root, {CAPTURED}" if value.endswith("rem") else f"Measured css-var {name}, {CAPTURED}"},
    }


def num_token(name, value, ty="number"):
    return {
        "$value": value,
        "$type": ty,
        "$extensions": {"source": f"Measured css-var {name}, {CAPTURED}"},
    }


def put(tree, path, token):
    node = tree
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = token


def semantic(resolved):
    """Map Kraken's --colors-ds-semantic-* layer onto the library's role names."""
    s = {}

    def take(path, var, desc):
        if var not in resolved or not is_color(resolved[var]):
            return
        put(s, path, color_token(var, resolved[var], desc))

    take("background.page", "--colors-ds-semantic-surface-page", "Page ground")
    take("background.canvas", "--colors-ds-semantic-surface-canvas", "Canvas")
    take("background.surface", "--colors-ds-semantic-surface-raised", "Raised surface")
    take("background.overlay", "--colors-ds-semantic-surface-overlay", "Overlay")
    take("background.sunken", "--colors-ds-semantic-surface-sunken", "Sunken surface")
    take("background.hover", "--colors-ds-semantic-surface-hover", "Hover wash")
    take("background.selected", "--colors-ds-semantic-surface-selected", "Selected wash")
    take("background.scrim", "--colors-ds-semantic-overlay-scrim", "Scrim")
    take("text.primary", "--colors-ds-semantic-content-primary", "Primary text")
    take("text.secondary", "--colors-ds-semantic-content-neutral", "Secondary text")
    take("text.muted", "--colors-ds-semantic-content-dimmed", "Muted text")
    take("text.disabled", "--colors-ds-semantic-content-disabled", "Disabled text")
    take("text.inverse", "--colors-ds-semantic-content-inverse", "Inverse text")
    take("text.on-accent", "--text-color-ds-button-primary-high", "Text on the primary button")
    take("text.link", "--colors-ds-semantic-content-brand", "Brand / link text")
    take("border.default", "--colors-ds-semantic-border-default", "Default border")
    take("border.subtle", "--colors-ds-semantic-border-subtle", "Subtle border")
    take("border.strong", "--colors-ds-semantic-border-strong", "Strong border")
    take("border.focus", "--colors-ds-semantic-focus-ring", "Focus ring")
    take("accent.default", "--colors-ds-semantic-action-primary-background", "Primary action")
    take("accent.hover", "--colors-ds-semantic-action-primary-background-hover", "Primary action hover")
    take("accent.pressed", "--background-color-ds-button-primary-high-active", "Primary action pressed")
    take("accent.on", "--colors-ds-semantic-action-primary-foreground", "Foreground on primary action")
    take("action.secondary", "--colors-ds-semantic-action-secondary-background", "Secondary action wash")
    take("action.secondary-hover", "--colors-ds-semantic-action-secondary-background-hover", "Secondary action hover")
    take("action.secondary-text", "--colors-ds-semantic-action-secondary-foreground", "Secondary action text")
    for status in ("positive", "negative", "warning", "info", "brand", "neutral"):
        take(f"status.{status}.solid", f"--colors-ds-semantic-status-{status}-solid", f"{status} solid")
        take(f"status.{status}.subtle", f"--colors-ds-semantic-status-{status}-subtle", f"{status} subtle")
        take(f"status.{status}.on-solid", f"--colors-ds-semantic-status-{status}-on-solid", f"text on {status} solid")
        take(f"status.{status}.on-subtle", f"--colors-ds-semantic-status-{status}-on-subtle", f"text on {status} subtle")
        take(f"status.{status}.content", f"--colors-ds-semantic-status-{status}-content", f"{status} content")
    take("status.positive.border", "--colors-ds-semantic-border-positive", "Positive border")
    take("status.negative.border", "--colors-ds-semantic-border-negative", "Negative border")
    return s


def core():
    c = {}
    # Brand primitive and the flat colour roles Kraken names on --colors-ds-*.
    primitives = {
        "brand": "--colors-ds-brand",
        "primary": "--colors-ds-primary",
        "strong": "--colors-ds-strong",
        "neutral": "--colors-ds-neutral",
        "dimmed": "--colors-ds-dimmed",
        "subtle": "--colors-ds-subtle",
        "disabled": "--colors-ds-disabled",
        "divider": "--colors-ds-divider",
        "inverted": "--colors-ds-inverted",
        "positive": "--colors-ds-positive",
        "negative": "--colors-ds-negative",
        "warning": "--colors-ds-warning",
        "info": "--colors-ds-info",
    }
    for key, var in primitives.items():
        if var in LIGHT and is_color(LIGHT[var]):
            put(c, f"color.primitive.{key}", color_token(var, LIGHT[var], f"Kraken primitive {key}"))

    # A neutral ramp built from the resolved grey-adjacent surfaces and text,
    # ordered light to dark. These are named roles, not a generated scale.
    ramp = [
        ("0", "--colors-ds-semantic-surface-canvas"),
        ("50", "--colors-ds-semantic-surface-page"),
        ("100", "--colors-ds-semantic-surface-sunken"),
        ("200", "--colors-ds-semantic-border-subtle"),
        ("300", "--colors-ds-divider"),
        ("400", "--colors-ds-subtle"),
        ("500", "--colors-ds-dimmed"),
        ("600", "--colors-ds-neutral"),
        ("700", "--colors-ds-semantic-action-secondary-foreground"),
        ("800", "--colors-ds-strong"),
        ("900", "--colors-ds-primary"),
    ]
    for step, var in ramp:
        if var in LIGHT and is_color(LIGHT[var]):
            put(c, f"color.neutral.{step}", color_token(var, LIGHT[var], f"Neutral step from {var}"))

    purple = [
        ("100", "--colors-ds-semantic-status-brand-subtle"),
        ("300", "--background-color-ds-button-primary-medium"),
        ("500", "--colors-ds-brand"),
        ("600", "--background-color-ds-button-primary-high-hover"),
        ("800", "--colors-ds-semantic-status-brand-content"),
        ("900", "--colors-ds-semantic-status-brand-content-strong"),
    ]
    for step, var in purple:
        if var in LIGHT and is_color(LIGHT[var]):
            put(c, f"color.purple.{step}", color_token(var, LIGHT[var], f"Purple step from {var}"))

    for i in range(0, 9):
        var = f"--border-radius-ds-{i}"
        if var in LIGHT:
            put(c, f"radius.{i}", dim_token(var, LIGHT[var], f"Radius step {i}"))
    put(c, "radius.round", dim_token("--border-radius-ds-round", LIGHT["--border-radius-ds-round"], "Pill radius"))
    for name in ("button-md", "button-xs", "input-md", "card", "dialog", "menu", "tooltip", "badge-md", "container"):
        var = f"--border-radius-ds-{name}"
        if var in LIGHT:
            put(c, "radius." + name.replace("-", "."), dim_token(var, LIGHT[var]))

    for i in range(0, 8):
        var = f"--box-shadow-ds-{i}"
        val = LIGHT.get(var)
        if not val or val == "none":
            continue
        put(c, f"elevation.{i}", {
            "$value": val,
            "$type": "shadow",
            "$description": f"Kraken elevation step {i}",
            "$extensions": {"source": f"Measured css-var {var}, {CAPTURED}", "css": val},
        })

    # Spacing: Kraken does not publish a 4px space scale as custom properties.
    # The control gaps that do exist are recorded. The 4px steps were picked by
    # hand at capture time, so they are a Reconstruction (docs/EVIDENCE.md).
    for step, px in (("1", "4px"), ("2", "8px"), ("3", "12px"), ("4", "16px"), ("5", "20px"), ("6", "24px"), ("8", "32px"), ("10", "40px"), ("12", "48px"), ("16", "64px")):
        put(c, f"spacing.{step}", {
            "$value": px,
            "$type": "dimension",
            "$description": "4px spacing step. Kraken's public CSS does not declare a space scale; the step matches measured control padding (8, 12, 16) and the 2px radius increment.",
            "$extensions": {"source": f"Reconstruction: entered by hand at capture time; no reading in raw/ holds a spacing scale. A 4px step list chosen to fit the measured button padding (8, 12, 16) and the 2px --border-radius-ds-* increment, {CAPTURED}"},
        })
    for var, key in (
        ("--gap-ds-checkbox-md", "gap.checkbox-md"),
        ("--gap-ds-checkbox-lg", "gap.checkbox-lg"),
        ("--spacing-ds-radio-button-md", "control.radio-md"),
        ("--spacing-ds-radio-button-lg", "control.radio-lg"),
    ):
        if var in LIGHT:
            put(c, "spacing." + key, dim_token(var, LIGHT[var]))

    families = {
        "brand": "--fontFamily-ds-brand1",
        "product": "--fontFamily-ds-body1",
        "mono": "--fontFamily-ds-bodyMono1",
    }
    for key, var in families.items():
        put(c, f"font.family.{key}", {
            "$value": LIGHT[var],
            "$type": "fontFamily",
            "$extensions": {"source": f"Measured css-var {var}, {CAPTURED}"},
        })

    roles = [
        "display1", "display2", "display3", "display4",
        "heading1", "heading2", "heading3", "heading4", "heading5", "heading6",
        "body1", "body2", "body3", "body4",
        "label1", "label2", "label3",
        "caption1", "caption2",
        "editorial1", "brand1", "bodyMono1", "heroNumber",
    ]
    for role in roles:
        size = LIGHT.get(f"--fontSize-ds-{role}")
        lh = LIGHT.get(f"--lineHeight-ds-{role}")
        weight = LIGHT.get(f"--fontWeight-ds-{role}")
        family = LIGHT.get(f"--fontFamily-ds-{role}")
        if not (size and lh and weight and family):
            continue
        ls = LIGHT.get(f"--letterSpacing-ds-{role}")
        style = {
            "fontFamily": family,
            "fontSize": rem_to_px(size) or size,
            "fontWeight": int(float(weight)) if re.fullmatch(r"\d+", str(weight).strip()) else weight,
            "lineHeight": rem_to_px(lh) or lh,
        }
        if ls and rem_to_px(ls):
            style["letterSpacing"] = rem_to_px(ls)
        put(c, f"typography.{role}", {
            "$value": style,
            "$type": "typography",
            "$extensions": {"source": f"Measured --fontSize/Weight/lineHeight/Family-ds-{role}, {CAPTURED}"},
        })

    return c


def component_tokens():
    """A few component colours the style guide can render from tokens."""
    groups = {}
    mapping = {
        "button.primary.bg": "--background-color-ds-button-primary-high",
        "button.primary.text": "--text-color-ds-button-primary-high",
        "button.primary.hover": "--background-color-ds-button-primary-high-hover",
        "button.primary.radius": "--border-radius-ds-button-md",
        "button.neutral.bg": "--background-color-ds-button-neutral-medium",
        "button.neutral.text": "--text-color-ds-button-neutral-medium",
        "input.bg": "--background-color-ds-input-default",
        "input.border": "--border-color-ds-input-default",
        "input.focus": "--border-color-ds-input-focused",
        "input.error": "--border-color-ds-input-error",
        "input.radius": "--border-radius-ds-input-md",
        "badge.positive.bg": "--background-color-ds-badge-positive-low",
        "badge.positive.text": "--text-color-ds-badge-positive-low",
        "badge.negative.bg": "--background-color-ds-badge-negative-low",
        "badge.negative.text": "--text-color-ds-badge-negative-low",
    }
    out = {}
    for path, var in mapping.items():
        if var not in LIGHT:
            continue
        val = LIGHT[var]
        if "radius" in path:
            token = dim_token(var, val)
        elif is_color(val):
            token = color_token(var, val)
        else:
            continue
        put(out, path, token)
    return out


def main():
    light = semantic(LIGHT)
    dark = semantic(DARK)
    light["component"] = component_tokens()
    # Dark component colours from the dark resolution, same names.
    dark_comp = {}
    for path, token in _flat(light["component"]):
        var = token["$extensions"]["source"].split("css-var ", 1)[-1].split(" ", 1)[0].split(",", 1)[0]
        # source string is "Measured css-var NAME ..."
        m = re.search(r"--[A-Za-z0-9_-]+", token["$extensions"]["source"])
        if not m or m.group(0) not in DARK:
            continue
        var = m.group(0)
        val = DARK[var]
        if token["$type"] == "color" and is_color(val):
            put(dark_comp, path, color_token(var, val))
        elif token["$type"] == "dimension":
            put(dark_comp, path, dim_token(var, val))
    dark["component"] = dark_comp

    doc = {
        "core": core(),
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "magic-light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "magic-dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
        "$extensions": {
            "source": f"kraken.com public pages, {CAPTURED}. light resolved on / (data-theme=magic-light); dark resolved on /pro (data-theme=magic-dark).",
        },
    }
    # Drop elevation tokens whose value is not a DTCG shadow the checker accepts.
    # Keep them as $extensions.css strings by converting simple box-shadows.
    elev = doc["core"].get("elevation", {})
    kept = {}
    for key, token in elev.items():
        parsed = parse_shadow(token["$extensions"]["css"])
        if parsed:
            token["$value"] = [parsed]
            kept[key] = token
        else:
            token_note = token["$extensions"]["css"]
            # leave a colour-less record out; the README names the raw value
            print("skip elevation", key, token_note[:80])
    doc["core"]["elevation"] = kept
    apply_motion(doc)
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=1) + "\n")
    print("wrote", out, "core groups", list(doc["core"]), "light", list(doc["light"]))


def _flat(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from _flat(v, prefix + k + ".")


def parse_shadow(css):
    """Parse one box-shadow layer into DTCG. Returns None if it cannot."""
    css = css.strip()
    if "," in css or "inset" in css:
        return None
    m = re.fullmatch(
        r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(#(?:[0-9a-fA-F]{3,8})|rgba?\([^)]+\))",
        css,
    )
    if not m:
        return None
    try:
        color = norm_color(m.group(5))
    except ValueError:
        return None
    def px(s):
        return "%gpx" % float(s)
    return {
        "offsetX": px(m.group(1)),
        "offsetY": px(m.group(2)),
        "blur": px(m.group(3)),
        "spread": px(m.group(4)),
        "color": color,
    }


def apply_motion(doc):
    motion_path = HERE / "raw" / "motion.json"
    if not motion_path.exists():
        return
    import sys
    # The package's own motion.py, never the repo kit's: a kit change must not change this
    # package's rebuild.
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core_motion, skipped = motion.build(json.loads(motion_path.read_text()))
    doc.setdefault("core", {})["motion"] = core_motion
    if skipped:  # what DTCG cannot carry is kept, as the kit does
        doc["core"].setdefault("$extensions", {})["notTokenised"] = skipped


if __name__ == "__main__":
    main()
