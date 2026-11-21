#!/usr/bin/env python3
"""Build tokens.json from the live CSS custom properties read on calendly.com.

Source: raw/css-vars.json, written by tools/capture/public/read-vars.mjs from
the signed-out homepage on 2026-11-21. Calendly publishes one light theme on
the public marketing site. Dark shadow tokens exist (--var-shadow-ui-dark-*)
but no captured page sets a dark theme, so they stay in core as unused
alternates and no dark set is emitted.

Every leaf carries $extensions.source. A colour that is a plain hex alias of
another token points at that token. calc(.25rem * N) lengths are kept as the
authored calc and also recorded as a derived px note. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RESOLVED = RAW["resolved"]
AUTHORED = RAW.get("authored", {})
SOURCE = "css-var on https://calendly.com/ :root, read 2026-11-21, headless Chromium, signed out"

# Semantic and brand names. Tailwind's default palette (--color-red-600 and
# the rest of the stock hue steps) is not Calendly's system and is left out.
COLOR_PREFIXES = (
    "--color-action-",
    "--color-badge-",
    "--color-border-",
    "--color-iconbutton-",
    "--color-ramp-",
    "--color-status-",
    "--color-surface-",
    "--color-text-",
    "--color-legacy-",
)
COLOR_EXACT = {
    "--color-ash", "--color-avocado", "--color-black", "--color-cloud",
    "--color-cobalt", "--color-coffee", "--color-cornflower", "--color-divider",
    "--color-haze", "--color-honeydew", "--color-iris", "--color-jade",
    "--color-lake", "--color-lavender", "--color-lilac", "--color-lime",
    "--color-linen", "--color-magnolia", "--color-midnight", "--color-navy",
    "--color-new-leaf", "--color-olive", "--color-onyx", "--color-peach",
    "--color-plum", "--color-rain", "--color-seafoam", "--color-silver",
    "--color-sky", "--color-smoke", "--color-steel", "--color-sunbeam",
    "--color-tangerine", "--color-white",
}
# Alpha steps of the named pigments, authored as 8-digit hex.
COLOR_ALPHA = ("--color-magnolia-a", "--color-midnight-a", "--color-cornflower-a")

KEEP_PREFIXES = (
    "--spacing-", "--gap-", "--radius-", "--text-ui-", "--leading-ui-",
    "--font-weight-", "--font-calendly", "--font-geist", "--font-wulkan",
    "--font-system", "--font-mono", "--ease-", "--shadow-ui-", "--var-shadow-ui-",
    "--breakpoint-ui-", "--header-height", "--header-nav-", "--header-panel-",
    "--color-action-focus",
)


def keep_color(name):
    if name in COLOR_EXACT:
        return True
    if name.startswith(COLOR_PREFIXES):
        return True
    if name.startswith(COLOR_ALPHA):
        return True
    return False


def keep(name):
    if name.startswith("--tw-") or name.startswith("--lightningcss"):
        return False
    if keep_color(name):
        return True
    return name.startswith(KEEP_PREFIXES)


def norm_hex(value):
    v = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if not m:
        return None
    h = m.group(1)
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) == 6:
        return "#" + h
    if len(h) == 8:
        rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        a = int(h[6:8], 16) / 255
        if a >= 1:
            return "#%02x%02x%02x" % tuple(rgb)
        return "rgba(%d, %d, %d, %s)" % (*rgb, "%g" % round(a, 3))
    return None


def calc_px(value):
    """calc(.25rem * N) at 16px, or a bare px length. None when it is not one length."""
    v = value.strip()
    m = re.fullmatch(r"calc\(\s*\.25rem\s*\*\s*(\d+(?:\.\d+)?)\s*\)", v)
    if m:
        return "%gpx" % (float(m.group(1)) * 4)
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", v)
    if m:
        return "%gpx" % float(m.group(1))
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)rem", v)
    if m:
        return "%gpx" % (float(m.group(1)) * 16)
    return None


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def put(tree, path, token):
    node = tree
    for part in path[:-1]:
        node = node.setdefault(part, {})
    node[path[-1]] = token


def path_for(name):
    body = name[2:]
    return body.split("-")


core = {}
light = {}


def authored_alias(name):
    """A plain var(--other) declaration, not a lightningcss light/dark pair."""
    raw = (AUTHORED.get(name) or "").strip()
    m = re.fullmatch(r"var\((--[\w-]+)\)", raw)
    if not m:
        return None
    target = m.group(1)
    if target not in RESOLVED or not keep_color(target):
        return None
    return target


for name, value in sorted(RESOLVED.items()):
    if not keep(name):
        continue
    src = "%s %s; authored %s" % (SOURCE, name, (AUTHORED.get(name) or value)[:140])
    if keep_color(name):
        hx = norm_hex(value)
        if not hx:
            continue
        target = authored_alias(name)
        stored = hx
        if target:
            stored = "{%s}" % ".".join(path_for(target))
            src += "; alias of %s" % target
        put(light, path_for(name), tok(stored, "color", src))
        continue
    if name.startswith("--font-weight-"):
        put(core, path_for(name), tok(int(value), "fontWeight", src))
        continue
    if name.startswith("--font-"):
        put(core, path_for(name), tok(value, "fontFamily", src))
        continue
    if name.startswith("--ease-"):
        m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", value.strip())
        if not m:
            continue
        nums = [float("%g" % float(x)) for x in m.group(1).split(",")]
        put(core, path_for(name), tok(nums, "cubicBezier", src))
        continue
    if name.startswith("--leading-"):
        put(core, path_for(name), tok(float(value) if re.fullmatch(r"[\d.]+", value) else value, "number", src))
        continue
    if name.startswith(("--spacing-", "--gap-", "--radius-", "--text-ui-", "--breakpoint-", "--header-")):
        px = calc_px(value)
        if not px:
            continue
        note = src
        if px != value.strip():
            note += "; derived %s from the authored calc at 16px root" % px
        put(core, path_for(name), tok(px, "dimension", note))
        continue
    if name.startswith(("--shadow-ui-", "--var-shadow-ui-")):
        put(core, path_for(name), tok(value, "shadow", src + "; kept as the authored shadow string"))

# Role aliases the coverage checklist asks for, each pointing at a measured token.
roles = {
    "page": "color.surface.bg.primary",
    "surface": "color.surface.bg.secondary",
    "raised": "color.white",
    "text": "color.text.primary",
    "muted": "color.text.secondary",
    "disabled": "color.text.tertiary",
    "on-accent": "color.action.primary.text",
    "link": "color.cobalt",
    "border": "color.border.default",
    "border-strong": "color.border.strong",
    "focus": "color.action.focus.border",
    "accent": "color.action.primary.bg",
    "success": "color.badge.success.bg",
    "warning": "color.badge.warning.bg",
    "danger": "color.status.error",
    "info": "color.badge.info.bg",
}
for key, target in roles.items():
    put(light, ["role", key], tok("{" + target + "}", "color",
        "alias of %s; %s" % (target, SOURCE)))

light["$description"] = "Calendly's public marketing theme. One painted theme (magnolia page, midnight text). Dark shadow tokens live in core and were not observed on a dark page."
core["$description"] = "Scales read from calendly.com custom properties on 2026-11-21. Lengths that were authored as calc(.25rem * N) are stored as the derived px at a 16px root."

doc = {
    "$schema": "https://tr.designtokens.org/format/2023-04-06.json",
    "core": core,
    "light": light,
    "$themes": [{"name": "light", "selectedTokenSets": {"core": "enabled", "light": "source"}}],
}
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "core groups", len(core), "light groups", len(light))
