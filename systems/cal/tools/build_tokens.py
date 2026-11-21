#!/usr/bin/env python3
"""Build tokens.json from cal.com's declared custom properties.

Sources, read from https://cal.com/ on 2026-11-21, signed out, 1440x900:
  raw/css-vars.json              stylesheet harvest (tools/capture/vars.mjs)
  raw/components-computed.json   computed styles of public controls

cal.com paints one light scheme on the public site. The product token layer
is --cal-* (app booker colours) plus --color-hp-* (homepage) and the shadcn
roles on :root (--background, --foreground, --primary, --border, --ring).
Tailwind's default hue ramps are recorded under core.color.ramp as declared
values, not as the product's own semantic roles.

There is no dark theme on the captured public surface, so tokens.json holds
core and light only. Every token carries $extensions.source. Unread values
stay out. Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
BY = {r["name"]: r["value"] for r in V["theme"] + V["app"]}
SRC = "raw/css-vars.json, declared on cal.com stylesheets, 2026-11-21, signed out"
MEAS = "raw/components-computed.json, computed style, 1440x900, signed out"


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            r, g, b, a = (int(h[i:i + 2], 16) for i in (0, 2, 4, 6))
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


def color(name, source=SRC):
    raw = BY[name]
    if raw.startswith("var("):
        inner = raw[4:].split(",")[0].rstrip(")").strip()
        if inner in BY and not BY[inner].startswith("var("):
            raw = BY[inner]
            source = SRC + "; alias " + name + " -> " + inner
        else:
            raise ValueError(name + " unresolved " + raw)
    return {
        "$value": norm_color(raw),
        "$type": "color",
        "$extensions": {"source": source + " (" + name + ")"},
    }


def dim(value, source):
    value = str(value).strip()
    if re.fullmatch(r"-?\d+(\.\d+)?", value):
        value += "px"
    if not re.fullmatch(r"-?\d*\.?\d+(px|rem)", value):
        raise ValueError("bad dimension " + value)
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


core = {"color": {"cal": {}, "hp": {}, "ramp": {}}, "font": {}, "radius": {}, "space": {}, "shadow": {}, "motion": {}, "typography": {}}

for name, value in sorted(BY.items()):
    if not name.startswith("--cal-") or name.startswith("--cal-bg-visualization") or name.startswith("--cal-text-visualization"):
        continue
    if value.startswith("var("):
        continue
    try:
        leaf = color(name)
    except ValueError:
        continue
    key = name[len("--cal-"):].replace("-", ".")
    node = core["color"]["cal"]
    parts = key.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf

for name, value in sorted(BY.items()):
    if not name.startswith("--color-hp-"):
        continue
    if value.startswith("var(") or not re.match(r"#|rgb", value):
        continue
    try:
        leaf = color(name)
    except ValueError:
        continue
    core["color"]["hp"][name[len("--color-hp-"):].replace("-", ".")] = leaf

# Neutral and a few status ramps the product's Tailwind theme declares.
# Incomplete steps stay incomplete: only declared stops are kept.
for hue in ("gray", "neutral", "emerald", "red", "amber", "blue", "orange"):
    steps = {}
    for name, value in BY.items():
        m = re.fullmatch(rf"--color-{hue}-(\d+)", name)
        if not m or value.startswith("var("):
            continue
        try:
            steps[m.group(1)] = color(name)
        except ValueError:
            pass
    if steps:
        core["color"]["ramp"][hue] = steps

# --font-sans and --font-display are var(--font-cal-sans), system-ui, sans-serif.
# The face that actually paints body and h1 is calSans (computed fontFamily).
core["font"]["family"] = {
    "sans": num('calSans, "calSans Fallback", system-ui, sans-serif', "fontFamily", MEAS + "; computed fontFamily on body and h1. Declared --font-sans is var(--font-cal-sans), system-ui, sans-serif."),
    "display": num('calSans, "calSans Fallback", system-ui, sans-serif', "fontFamily", MEAS + "; h1 computed fontFamily. Declared --font-display aliases --font-cal-sans."),
    "mono": num(BY["--font-mono"], "fontFamily", SRC + " (--font-mono)"),
    "serif": num(BY["--font-serif"], "fontFamily", SRC + " (--font-serif)"),
}
core["font"]["weight"] = {
    "normal": num(400, "fontWeight", SRC + " (--font-weight-normal = 400)"),
    "medium": num(500, "fontWeight", SRC + " (--font-weight-medium = 500)"),
    "semibold": num(600, "fontWeight", SRC + " (--font-weight-semibold = 600)"),
    "bold": num(700, "fontWeight", SRC + " (--font-weight-bold = 700)"),
}

# Only radii that are a single length. calc() aliases are recorded as
# derived px at a 16px root (0.625rem = 10px) and labelled Derived.
# --radius is 0.625rem. --radius-sm is calc(var(--radius) - 4px) = 6px.
# --radius-md is calc(var(--radius) * .8) = 8px. --radius-lg is var(--radius) = 10px.
# --radius-xl is calc(var(--radius) * 1.4) = 14px. --radius-2xl * 1.8 = 18px.
# --radius-3xl * 2.2 = 22px. --radius-xs is 0.125rem = 2px.
DERIVED_RADIUS = {
    "xs": ("0.125rem", "--radius-xs", False),
    "sm": ("6px", "--radius-sm calc(var(--radius) - 4px)", True),
    "md": ("8px", "--radius-md calc(var(--radius) * .8)", True),
    "lg": ("0.625rem", "--radius-lg var(--radius)", True),
    "xl": ("14px", "--radius-xl calc(var(--radius) * 1.4)", True),
    "2xl": ("18px", "--radius-2xl calc(var(--radius) * 1.8)", True),
    "3xl": ("22px", "--radius-3xl calc(var(--radius) * 2.2)", True),
}
for step, (value, note, derived) in DERIVED_RADIUS.items():
    leaf = dim(value, ("Derived from " if derived else "") + SRC + " (" + note + ")")
    core["radius"][step] = leaf
# Measured control radii, not the Tailwind scale.
core["radius"]["nav-pill"] = dim("10px", MEAS + "; nav-link borderRadius")
core["radius"]["cta"] = dim("12px", MEAS + "; nav-cta borderRadius")
core["radius"]["field"] = dim("10px", MEAS + "; login-email borderRadius, look-only")

core["space"]["unit"] = dim(BY["--spacing"], SRC + " (--spacing)")
for i, px in enumerate((4, 8, 12, 16, 20, 24, 32, 40, 48, 64), start=1):
    # The declared unit is 0.25rem. Steps are derived as multiples of that unit.
    core["space"][str(i)] = {
        "$value": "{space.unit}",
        "$type": "dimension",
        "$description": f"Derived: {i} x the declared 0.25rem spacing unit ({px}px at 16px root). Not a named token on the site.",
        "$extensions": {"source": "Derived from --spacing (" + BY["--spacing"] + ") x " + str(i)},
    }
# The alias above repeats the same token. Record the multiples as literal rem so they differ.
for i in range(1, 11):
    core["space"][str(i)] = dim(f"{i * 0.25:g}rem", "Derived from --spacing 0.25rem x " + str(i) + ", " + SRC)

core["shadow"]["md"] = num(BY["--shadow-md"], "shadow", SRC + " (--shadow-md)")
core["shadow"]["lg"] = num(BY["--shadow-lg"], "shadow", SRC + " (--shadow-lg)")
core["motion"]["ease-hp"] = num([0.19, 1, 0.22, 1], "cubicBezier", SRC + " (--ease-hp cubic-bezier(.19, 1, .22, 1))")
core["motion"]["ease-hp-fly"] = num([0.22, 1, 0.36, 1], "cubicBezier", SRC + " (--ease-hp-fly)")
core["motion"]["ease-out"] = num([0, 0, 0.2, 1], "cubicBezier", SRC + " (--ease-out)")
core["motion"]["menu"] = num("200ms", "duration", SRC + "; mega-menu transition duration-200 on the dialog class")

# Type ramp from declared --text-* sizes. Line heights are the paired tokens where present.
for step in ("xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"):
    size = BY.get("--text-" + step)
    leading = BY.get("--text-" + step + "--line-height")
    if not size:
        continue
    core["typography"][step] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.sans}",
            "fontSize": size if re.fullmatch(r"-?\d*\.?\d+(px|rem)", size) else size,
            "fontWeight": "{font.weight.normal}",
            "lineHeight": leading if leading and re.fullmatch(r"-?\d*\.?\d+(px|rem)", leading) else "1.5",
        },
        "$extensions": {"source": SRC + " (--text-" + step + ("" if not leading else " + --text-" + step + "--line-height") + ")"},
    }
# Display is measured, not on the Tailwind ramp.
core["typography"]["display"] = {
    "$type": "typography",
    "$value": {
        "fontFamily": "{font.family.sans}",
        "fontSize": "80px",
        "fontWeight": "{font.weight.bold}",
        "lineHeight": "86.4px",
        "letterSpacing": "-0.8px",
    },
    "$extensions": {"source": MEAS + "; h1 on https://cal.com/"},
}

light = {
    "page": color("--background"),
    "surface": color("--card"),
    "raised": color("--color-hp-raised"),
    "text": color("--foreground"),
    "muted": color("--muted-foreground"),
    "accent": color("--primary"),
    "on-accent": color("--cal-brand-text"),
    "link": color("--foreground"),
    "border": color("--border"),
    "border-strong": color("--cal-border-emphasis"),
    "focus": color("--ring"),
    "field": color("--color-hp-field"),
    "accent-brand": color("--color-hp-accent"),
    "scrim": color("--cal-bg-inverted"),
    "success": color("--success"),
    "warning": color("--warning"),
    "danger": color("--destructive"),
    "info": color("--info"),
    "success-subtle": color("--cal-bg-success"),
    "warning-subtle": color("--cal-bg-attention"),
    "danger-subtle": color("--cal-bg-error"),
    "info-subtle": color("--cal-bg-info"),
    "disabled": {
        "$value": "#9ca3b0",
        "$type": "color",
        "$extensions": {"source": SRC + " (--cal-text-muted, the muted ink used for quiet labels; no separate disabled token was declared)"},
    },
}

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_checks import alias_errors  # noqa: E402

errors = alias_errors(core, light, {})
if errors:
    raise SystemExit("\n".join(errors))

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme cal.com paints on the public site. color-scheme computed to light. No dark class or data-theme was set.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if "$value" in v else count(v) for v in d.values() if isinstance(v, dict))


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)}")
