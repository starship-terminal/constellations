#!/usr/bin/env python3
"""Build tokens.json from doctronic.ai's declared custom properties.

Source: raw/css-vars.json, read live from https://www.doctronic.ai/ on 2026-11-21.
The site declares a --color-* role layer, ramps, type shorthands, shadows and
focus sizes. There is no dark theme. Component geometry that the wrappers do
not paint is recorded under core.measured from raw/components-computed.json.

Deterministic: same inputs, byte-identical output. Edit the raw files, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIGHT = V["resolved"]["light"]

SRC = "declared custom property on doctronic.ai (raw/css-vars.json, 2026-11-21)"


def raw(name):
    if name not in LIGHT:
        raise KeyError(name)
    return LIGHT[name]["value"]


def norm_color(v):
    v = v.strip().lower()
    if v.startswith("hsl(from"):
        return v
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a == 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


def color(name):
    return {
        "$value": norm_color(raw(name)),
        "$type": "color",
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def text_style(name):
    """--text-body-16: 400 1rem/1.4 "geist", system-ui, Arial, sans-serif"""
    value = raw(name)
    m = re.match(
        r"(?:(italic)\s+)?(\d+)\s+([\d.]+)rem/([\d.]+)\s+(.+)$",
        value,
    )
    if not m:
        raise ValueError(name + " " + value)
    italic, weight, rem, lh, family = m.groups()
    px = round(float(rem) * 16, 3)
    px_s = ("%g" % px) + "px"
    style = {
        "fontFamily": family,
        "fontSize": px_s,
        "fontWeight": int(weight),
        "lineHeight": float(lh),
    }
    if italic:
        style["fontStyle"] = "italic"
    return {
        "$value": style,
        "$type": "typography",
        "$extensions": {
            "source": f"{SRC}; {name} = {value}; rem converted at 16px",
            "evidence": "Derived",
        },
    }


def shadow(name):
    value = raw(name)
    col = re.search(r"#(?:[0-9a-fA-F]{3,8})", value)
    if not col:
        raise ValueError(name + " " + value)
    nums = re.findall(r"-?[\d.]+px", value)
    # offsetX offsetY blur [spread]
    nums = [n if n.endswith("px") else n + "px" for n in nums]
    if value.strip().startswith("0 ") and not value.strip().startswith("0px"):
        nums = ["0px"] + nums
    while len(nums) < 4:
        nums.append("0px")
    ox, oy, blur, spread = nums[:4]
    return {
        "$value": [{
            "offsetX": ox,
            "offsetY": oy,
            "blur": blur,
            "spread": spread,
            "color": norm_color(col.group(0)),
        }],
        "$type": "shadow",
        "$extensions": {"source": f"{SRC}; {name} = {value}"},
    }


def dim(name, unit="px"):
    value = raw(name)
    if value.endswith("rem"):
        px = round(float(value[:-3]) * 16, 3)
        shown = ("%g" % px) + "px"
        return {
            "$value": shown,
            "$type": "dimension",
            "$extensions": {"source": f"{SRC}; {name} = {value}; rem converted at 16px", "evidence": "Derived"},
        }
    if value.endswith("px"):
        return {"$value": value, "$type": "dimension", "$extensions": {"source": f"{SRC}; {name}"}}
    raise ValueError(name + " " + value)


def font_family(name):
    return {
        "$value": raw(name),
        "$type": "fontFamily",
        "$extensions": {"source": f"{SRC}; {name}"},
    }


def ramp(prefix):
    out = {}
    for step in ("50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"):
        key = f"--color-{prefix}-{step}"
        if key in LIGHT:
            out[step] = color(key)
    return out


core = {
    "color": {
        "white": color("--color-white"),
        "blue": ramp("blue"),
        "neutral": ramp("neutral"),
        "sage": ramp("sage"),
        "lime": ramp("lime"),
        "error": ramp("error"),
        "success": ramp("success"),
        "warning": ramp("warning"),
        "graphic": {
            "blue": {
                "bold": color("--color-graphic-blue-bold"),
                "strong": color("--color-graphic-blue-strong"),
                "moderate": color("--color-graphic-blue-moderate"),
                "muted": color("--color-graphic-blue-muted"),
                "soft": color("--color-graphic-blue-soft"),
                "subtle": color("--color-graphic-blue-subtle"),
            }
        },
        "wash": {
            "lavenderDeep": color("--color-wash-lavender-deep"),
            "lavenderSoft": color("--color-wash-lavender-soft"),
            "sage": color("--color-wash-sage"),
            "sky": color("--color-wash-sky"),
        },
        "chat": {
            "stop1": color("--chat-sheet-accent-stop-1"),
            "stop2": color("--chat-sheet-accent-stop-2"),
            "stop3": color("--chat-sheet-accent-stop-3"),
            "stop4": color("--chat-sheet-accent-stop-4"),
        },
    },
    "font": {
        "display": font_family("--font-display"),
        "sans": font_family("--font-sans"),
        "body": font_family("--font-body"),
        "mono": font_family("--font-mono"),
    },
    "typography": {},
    "shadow": {
        "xs": shadow("--shadow-xs"),
        "sm": shadow("--shadow-sm"),
        "md": shadow("--shadow-md"),
        "lg": shadow("--shadow-lg"),
        "xl": shadow("--shadow-xl"),
        "brandGlow": shadow("--shadow-brand-glow"),
        "brandGlowHover": shadow("--shadow-brand-glow-hover"),
        "focusRing": shadow("--shadow-focus-ring"),
    },
    "size": {
        "header": dim("--header-height"),
        "tapTarget": dim("--tap-target-min"),
        "focusRingWidth": dim("--focus-ring-width"),
        "focusRingOffset": dim("--focus-ring-offset"),
    },
    "measured": {
        "controlRadiusPill": {
            "$value": "32px",
            "$type": "dimension",
            "$extensions": {"source": "computed borderRadius of button-login default (raw/components-computed.json)"},
        },
        "controlRadiusCta": {
            "$value": "52px",
            "$type": "dimension",
            "$extensions": {"source": "computed borderRadius of button-start-chat default (raw/components-computed.json)"},
        },
        "controlHeightLogin": {
            "$value": "35px",
            "$type": "dimension",
            "$extensions": {"source": "computed height 34.8px of button-login, rounded (raw/components-computed.json)", "evidence": "Derived"},
        },
        "controlHeightCta": {
            "$value": "44px",
            "$type": "dimension",
            "$extensions": {"source": "computed height 43.6px of button-start-chat, rounded (raw/components-computed.json)", "evidence": "Derived"},
        },
        "displaySize": {
            "$value": "48px",
            "$type": "dimension",
            "$extensions": {"source": "computed fontSize of h1 on / (raw/components-computed.json)"},
        },
    },
}

for name in sorted(LIGHT):
    if not name.startswith("--text-"):
        continue
    key = name[len("--text-"):].replace("-", ".")
    # nest one level: body.16
    group, _, step = key.partition(".")
    # heading.italic.10 has two dots
    parts = key.split(".")
    node = core["typography"]
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = text_style(name)

light = {
    "page": color("--color-surface-canvas"),
    "surface": color("--color-surface-raised"),
    "sunken": color("--color-surface-sunken"),
    "text": color("--color-fg-default"),
    "muted": color("--color-fg-muted"),
    "subtle": color("--color-fg-subtle"),
    "disabled": color("--color-fg-disabled"),
    "onAccent": color("--color-accent-fg"),
    "link": color("--color-link-default"),
    "border": color("--color-border-default"),
    "borderStrong": color("--color-border-strong"),
    "accent": color("--color-accent-bg"),
    "accentHover": color("--color-accent-bg-hover"),
    "accentPressed": color("--color-accent-bg-pressed"),
    "focus": color("--color-accent-focus-ring"),
    "success": color("--color-success-fg"),
    "successBg": color("--color-success-bg"),
    "warning": color("--color-warning-fg"),
    "warningBg": color("--color-warning-bg"),
    "danger": color("--color-error-fg"),
    "dangerBg": color("--color-error-bg"),
    "info": color("--color-info-fg"),
    "infoBg": color("--color-info-bg"),
    "solid": color("--color-solid-bg"),
    "solidText": color("--color-solid-fg"),
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "core groups", list(core), "light", len(light))
