#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Instagram publishes two token layers on the signed-out pages. The app layer
(--primary-text, --primary-button-background, --ig-*, --system-N-*) is what
the login wall and the signup form resolve. about.instagram.com adds
--about-ig-* brand colours and the Instagram Sans stacks.

light is getComputedStyle(documentElement) on www.instagram.com (the login
wall ships __fb-light-mode). dark is the same page with __ig-dark-mode and
__fb-dark-mode forced on the root, which is the class the signup wall paints
and the class the stylesheet declares. Every token carries $extensions.source.
A value that is still a var(), a gradient, or a bare channel triple is skipped
rather than guessed.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
LIGHT = RAW["resolved"]["light"]
DARK = RAW["resolved"]["dark"]
ABOUT = RAW["resolved"].get("about", {})
CAPTURED = RAW.get("captured", "2026-11-19")


def norm_color(v):
    v = str(v).strip().lower()
    if v in ("transparent", "#0000", "#fff0"):
        return "rgba(0, 0, 0, 0)"
    if v == "black":
        return "#000000"
    if v == "white":
        return "#ffffff"
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
    m = re.fullmatch(r"hsla?\(\s*([\d.]+)[,\s]+([\d.]+)%[,\s]+([\d.]+)%(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        return hsl_to_color(*m.groups())
    raise ValueError("not a colour: " + v)


def hsl_to_color(h, s, l, a=None):
    H, S, L = float(h), float(s) / 100, float(l) / 100
    c = (1 - abs(2 * L - 1)) * S
    x = c * (1 - abs((H / 60) % 2 - 1))
    m = L - c / 2
    if H < 60:
        r, g, b = c, x, 0
    elif H < 120:
        r, g, b = x, c, 0
    elif H < 180:
        r, g, b = 0, c, x
    elif H < 240:
        r, g, b = 0, x, c
    elif H < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    R, G, B = (round((r + m) * 255), round((g + m) * 255), round((b + m) * 255))
    if a is None:
        return "#%02x%02x%02x" % (R, G, B)
    af = float(a[:-1]) / 100 if str(a).endswith("%") else float(a)
    if af >= 0.999:
        return "#%02x%02x%02x" % (R, G, B)
    return "rgba(%d, %d, %d, %g)" % (R, G, B, round(af, 3))


def is_color(v):
    try:
        norm_color(v)
        return True
    except ValueError:
        return False


def rem_to_px(v):
    v = str(v).strip()
    m = re.fullmatch(r"(-?[\d.]+)rem", v)
    if m:
        return "%gpx" % (float(m.group(1)) * 16)
    m = re.fullmatch(r"(-?[\d.]+)px", v)
    if m:
        return "%gpx" % float(m.group(1))
    m = re.fullmatch(r"(-?[\d.]+)ms", v)
    if m:
        return None
    return None


def color_token(name, value, description=None):
    return {
        "$value": norm_color(value),
        "$type": "color",
        "$description": description or name,
        "$extensions": {"source": f"Measured css-var {name} resolved on documentElement, instagram.com, {CAPTURED}"},
    }


def dim_token(name, value, description=None):
    px = rem_to_px(value)
    if not px:
        raise ValueError(name + " " + value)
    return {
        "$value": px,
        "$type": "dimension",
        "$description": description or f"{name} = {value}",
        "$extensions": {"source": f"Measured css-var {name}, {CAPTURED}"},
    }


def put(tree, path, token):
    node = tree
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = token


def take(tree, resolved, path, var, desc):
    if var not in resolved or not is_color(resolved[var]):
        return
    put(tree, path, color_token(var, resolved[var], desc))


def semantic(resolved):
    s = {}
    take(s, resolved, "background.page", "--ig-primary-background", "Page ground. Declared as an RGB triple; the body background that paints it is recorded as the resolved colour.")
    # --ig-primary-background is "255, 255, 255", not a colour. Use the body
    # paint the harvest recorded, named after the variable that switches it.
    page = resolved.get("--surface-background") or resolved.get("--card-background")
    if page and is_color(page):
        put(s, "background.page", color_token("--surface-background", page, "Page and card ground on the login wall"))
    take(s, resolved, "background.surface", "--card-background", "Card surface")
    take(s, resolved, "background.sunken", "--background-deemphasized", "Deemphasized wash")
    take(s, resolved, "background.flat", "--card-background-flat", "Flat card")
    take(s, resolved, "background.comment", "--comment-background", "Comment wash")
    take(s, resolved, "background.popover", "--popover-background", "Popover")
    take(s, resolved, "text.primary", "--primary-text", "Primary text")
    take(s, resolved, "text.secondary", "--secondary-text", "Secondary text")
    take(s, resolved, "text.muted", "--placeholder-text", "Placeholder and muted text")
    take(s, resolved, "text.disabled", "--disabled-text", "Disabled text")
    take(s, resolved, "text.inverse", "--inverse-text", "Inverse text")
    take(s, resolved, "text.on-accent", "--primary-button-text", "Text on the primary button")
    take(s, resolved, "text.link", "--secondary-button-text", "Link and secondary button text")
    take(s, resolved, "text.link-strong", "--blue-link", "Strong link")
    take(s, resolved, "border.default", "--divider", "Divider")
    take(s, resolved, "border.focus", "--focus-ring-blue", "Focus ring blue")
    take(s, resolved, "border.focused", "--border-focused", "Focused border")
    take(s, resolved, "border.media", "--media-inner-border", "Media inner border")
    take(s, resolved, "accent.default", "--accent", "Instagram blue")
    take(s, resolved, "accent.button", "--primary-button-background", "Primary button")
    take(s, resolved, "accent.pressed", "--primary-button-pressed", "Primary button pressed")
    take(s, resolved, "accent.on", "--primary-button-text", "Text on primary button")
    take(s, resolved, "accent.deemphasized", "--primary-deemphasized-button-background", "Deemphasized button wash")
    take(s, resolved, "accent.deemphasized-text", "--primary-deemphasized-button-text", "Deemphasized button text")
    take(s, resolved, "status.positive.solid", "--positive", "Positive")
    take(s, resolved, "status.positive.subtle", "--positive-background", "Positive wash")
    take(s, resolved, "status.negative.solid", "--negative", "Negative")
    take(s, resolved, "status.negative.subtle", "--negative-background", "Negative wash")
    take(s, resolved, "status.warning.solid", "--badge-background-color-yellow", "Warning badge")
    take(s, resolved, "status.info.solid", "--text-badge-info-background", "Info badge")
    take(s, resolved, "status.info.subtle", "--new-notification-background", "Notification wash")
    take(s, resolved, "badge.blue", "--badge-background-color-blue", "Blue badge")
    take(s, resolved, "badge.green", "--badge-background-color-green", "Green badge")
    take(s, resolved, "badge.red", "--badge-background-color-red", "Red badge")
    take(s, resolved, "badge.gray", "--badge-background-color-gray", "Gray badge")
    return s


def core():
    c = {}
    brand = {
        "blue": "--accent",
        "link": "--blue-link",
        "facebook": "--base-blue",
        "positive": "--positive",
        "always-white": "--always-white",
        "always-black": "--always-black",
    }
    for key, var in brand.items():
        if var in LIGHT and is_color(LIGHT[var]):
            put(c, f"color.brand.{key}", color_token(var, LIGHT[var], f"Instagram brand {key}"))

    # About-site spectrum. These are the marketing brand colours, not the app blue.
    spectrum = [
        ("yellow", "--about-ig-yellow"),
        ("orange", "--about-ig-orange"),
        ("pink", "--about-ig-pink"),
        ("lavender", "--about-ig-lavender"),
        ("purple", "--about-ig-purple"),
        ("yellow-light", "--about-ig-light-yellow"),
        ("orange-light", "--about-ig-light-orange"),
        ("pink-light", "--about-ig-light-pink"),
        ("lavender-light", "--about-ig-light-lavender"),
        ("purple-light", "--about-ig-light-purple"),
        ("black", "--about-ig-black"),
        ("white", "--about-ig-white"),
        ("footer", "--about-ig-footer-gray"),
    ]
    for key, var in spectrum:
        if var in ABOUT and is_color(ABOUT[var]):
            put(c, f"color.spectrum.{key}", {
                "$value": norm_color(ABOUT[var]),
                "$type": "color",
                "$description": f"about.instagram.com spectrum {key}",
                "$extensions": {"source": f"Measured css-var {var} resolved on about.instagram.com, {CAPTURED}"},
            })

    # Neutral ramp from named roles, light to dark. Not a generated 10-step scale.
    ramp = [
        ("0", "--surface-background"),
        ("50", "--card-background-flat"),
        ("100", "--background-deemphasized"),
        ("200", "--divider"),
        ("400", "--disabled-text"),
        ("500", "--placeholder-text"),
        ("600", "--secondary-text"),
        ("900", "--primary-text"),
    ]
    for step, var in ramp:
        if var in LIGHT and is_color(LIGHT[var]):
            put(c, f"color.neutral.{step}", color_token(var, LIGHT[var], f"Neutral step from {var}"))

    radii = {
        "button": "--button-corner-radius",
        "button-medium": "--button-corner-radius-medium",
        "button-large": "--button-corner-radius-large",
        "card": "--card-corner-radius",
        "input": "--input-corner-radius",
        "input-ig": "--ig-input-border-radius",
        "dialog": "--dialog-corner-radius",
        "dialog-igds": "--igds-dialog-border-radius",
        "menu": "--igds-menu-border-radius",
        "modal": "--modal-border-radius",
        "chip": "--chip-corner-radius",
        "toast": "--toast-corner-radius",
        "tooltip": "--tooltip-corner-radius",
        "list-cell": "--list-cell-corner-radius",
        "chat-bubble": "--chat-bubble-border-radius",
        "alert": "--alert-banner-corner-radius",
    }
    # A variant of a radius that is itself a token stays a sibling (radius.button-medium): nested
    # under radius.button it would sit inside a token, where DTCG walkers never look.
    for key, var in radii.items():
        if var in LIGHT and rem_to_px(LIGHT[var]):
            path = key if key.split("-")[0] in radii else key.replace("-", ".")
            put(c, "radius." + path, dim_token(var, LIGHT[var]))

    # Spacing is not published as a scale. The 4px steps below are a suggested
    # scale (the step the radii and the system type sizes share), so they are a
    # Reconstruction, not a measurement (docs/EVIDENCE.md).
    for step, px in (("1", "4px"), ("2", "8px"), ("3", "12px"), ("4", "16px"), ("5", "20px"), ("6", "24px"), ("8", "32px"), ("10", "40px"), ("12", "48px")):
        put(c, f"spacing.{step}", {
            "$value": px,
            "$type": "dimension",
            "$description": "4px spacing step. Instagram's public CSS does not declare a space scale. The step matches the radius increment and the system type sizes.",
            "$extensions": {"source": f"Reconstruction — a suggested 4px scale, entered by hand at capture time; no spacing var is declared (the step matches --button-corner-radius and the --system-N-font-size steps), {CAPTURED}"},
        })

    families = {
        "system": "--font-family-system",
        "instagram-sans": "--about-ig-font-family",
        "instagram-sans-condensed": "--about-ig-condensed-font-family",
        "prism": "--font-family-system-prism",
        "mono": "--font-family-code",
    }
    for key, var in families.items():
        src = ABOUT if var.startswith("--about") else LIGHT
        if var not in src:
            continue
        put(c, f"font.family.{key}", {
            "$value": src[var],
            "$type": "fontFamily",
            "$extensions": {"source": f"Measured css-var {var}, {CAPTURED}"},
        })

    # Type roles from the published --system-N scale.
    for n in (10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32):
        size = LIGHT.get(f"--system-{n}-font-size")
        lh = LIGHT.get(f"--system-{n}-line-height")
        if not size or not rem_to_px(size):
            continue
        style = {
            "fontFamily": "{font.family.system}",
            "fontSize": rem_to_px(size),
            "fontWeight": 400,
            "lineHeight": rem_to_px(lh) if lh and rem_to_px(lh) else rem_to_px(size),
        }
        put(c, f"typography.system-{n}", {
            "$value": style,
            "$type": "typography",
            "$extensions": {"source": f"Measured --system-{n}-font-size and line-height, {CAPTURED}"},
        })

    durations = [
        ("extra-extra-short", "--fds-duration-extra-extra-short-in"),
        ("extra-short", "--fds-duration-extra-short-in"),
        ("short", "--fds-duration-short-in"),
        ("medium", "--fds-duration-medium-in"),
        ("long", "--fds-duration-long-in"),
        ("extra-long", "--fds-duration-extra-long-in"),
    ]
    for key, var in durations:
        val = LIGHT.get(var, "")
        m = re.fullmatch(r"(\d+)ms", val.strip())
        if not m:
            continue
        put(c, f"motion.duration.{key}", {
            "$value": val.strip(),
            "$type": "duration",
            "$extensions": {"source": f"Measured css-var {var}, {CAPTURED}"},
        })
    easings = {
        "soft": "--fds-soft",
        "strong": "--fds-strong",
        "move-in": "--ig-animation-move-in",
    }
    for key, var in easings.items():
        val = LIGHT.get(var, "")
        m = re.fullmatch(r"cubic-bezier\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*\)", val.strip())
        if not m:
            continue
        put(c, f"motion.easing.{key}", {
            "$value": [float(m.group(i)) for i in range(1, 5)],
            "$type": "cubicBezier",
            "$extensions": {"source": f"Measured css-var {var}, {CAPTURED}"},
        })
    return c


def component_tokens(resolved):
    out = {}
    mapping = {
        "button.primary.bg": "--primary-button-background",
        "button.primary.text": "--primary-button-text",
        "button.primary.pressed": "--primary-button-pressed",
        "button.primary.disabled": "--disabled-button-background",
        "button.secondary.text": "--secondary-button-text",
        "input.radius": "--ig-input-border-radius",
        "dialog.radius": "--igds-dialog-border-radius",
    }
    for path, var in mapping.items():
        if var not in resolved:
            continue
        val = resolved[var]
        if "radius" in path and rem_to_px(val):
            put(out, path, dim_token(var, val))
        elif is_color(val):
            put(out, path, color_token(var, val))
    return out


def apply_motion(doc):
    """Keep the named duration and easing tokens. The probe's class-hash names
    (x1pudf4l and the like) are not a scale, so they stay in raw/motion.json.
    The reduce verdict is recorded on $extensions."""
    motion_path = HERE / "raw" / "motion.json"
    if not motion_path.exists():
        return
    raw = json.loads(motion_path.read_text())
    summary = raw.get("summary") or {}
    doc["core"].setdefault("motion", {})["$extensions"] = {
        "source": f"motion-probe.mjs on the login wall, the signup form and about.instagram.com, {CAPTURED}",
        "reduce": summary.get("behaviour"),
        "moving": summary.get("moving"),
        "removed": summary.get("removed"),
        "kept": summary.get("kept"),
        "incomplete": "stylesheet lists were cut at 400 entries on each page",
    }


def build():
    light = semantic(LIGHT)
    dark = semantic(DARK)
    light["component"] = component_tokens(LIGHT)
    dark["component"] = component_tokens(DARK)
    doc = {
        "core": core(),
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "ig-light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "ig-dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
        "$extensions": {
            "source": f"instagram.com public pages, {CAPTURED}. light resolved on / (login wall, __fb-light-mode). dark resolved on the same URL after forcing __ig-dark-mode, the class the signup wall paints.",
        },
    }
    apply_motion(doc)
    return doc


def main():
    doc = build()
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=1) + "\n")
    print("wrote", out)


if __name__ == "__main__":
    main()
