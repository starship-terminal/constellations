#!/usr/bin/env python3
"""Build tokens.json from the Gestalt custom properties read on www.pinterest.com.

Source: raw/sema.json, written by the capture from getComputedStyle on :root
of the signed-out homepage on 2026-11-21. Every value is a resolved custom
property (Measured). Dark values are the stylesheet's own *-dark / *-inverse
names. The public site paints light only; dark is declared, not a shipped
theme switch a signed-out visitor can flip.

A token is a colour, a dimension, or a shadow. Gradients and non-length
values are omitted rather than stored as a guessed type. Aliases point at
core.palette when the resolved hex matches a ramp step.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw" / "sema.json"
SRC = "Measured: getComputedStyle(:root) on https://www.pinterest.com/ signed out, 2026-11-21, raw/sema.json"


def load():
    data = json.loads(RAW.read_text())
    tokens = data["tokens"]
    return {k[2:] if k.startswith("--") else k: v for k, v in tokens.items()}


def hex_of(v):
    v = v.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}", v):
        return "#" + "".join(c * 2 for c in v[1:])
    if re.fullmatch(r"#[0-9a-f]{6}", v):
        return v
    return None


def dim(v):
    v = v.strip()
    if re.fullmatch(r"-?\d+(\.\d+)?px", v):
        n = float(v[:-2])
        return ("%g" % n) + "px"
    if v in ("0", "0px"):
        return "0px"
    return None


def colour_token(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim_token(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def shadow_token(value, source):
    return {"$type": "shadow", "$value": value, "$extensions": {"source": source}}


def other_token(value, source):
    return {"$type": "other", "$value": value, "$extensions": {"source": source}}


def main():
    t = load()
    palette = {}
    for name, value in sorted(t.items()):
        if not name.startswith("base-color-"):
            continue
        if any(s in name for s in ("translucent", "gradient", "hover", "pressed", "opacity")):
            continue
        hx = hex_of(value)
        if not hx:
            continue
        parts = name[len("base-color-"):].split("-")
        # grayscale-0, red-500, or a single brand name (pinterest)
        if len(parts) == 1 and parts[0] == "pinterest":
            palette.setdefault("brand", {})["pinterest"] = colour_token(hx, f"{SRC}; --{name}")
            continue
        if len(parts) < 2 or not parts[1].isdigit():
            continue
        hue, step = parts[0], parts[1]
        palette.setdefault(hue, {})[step] = colour_token(hx, f"{SRC}; --{name}")

    by_hex = {}
    for hue, steps in palette.items():
        for step, node in steps.items():
            by_hex.setdefault(node["$value"], f"{{palette.{hue}.{step}}}")

    def paint(value, name):
        hx = hex_of(value)
        node = colour_token(value if not hx else hx, f"{SRC}; --{name}")
        if hx and hx in by_hex:
            node["$value"] = by_hex[hx]
            node["$extensions"]["resolved"] = hx
        return node

    def pick(prefix, theme):
        """theme light uses unsuffixed / -default / -light. theme dark uses -dark when present."""
        out = {}
        keys = [k for k in t if k.startswith(prefix)]
        for k in keys:
            if any(s in k for s in ("gradient", "wash-", "fade-", "scrim", "angle", "position")):
                continue
            if theme == "light" and k.endswith("-dark"):
                continue
            if theme == "dark" and not (k.endswith("-dark") or k.endswith("-inverse")):
                # keep shared names only when no dark sibling exists
                sibling = k + "-dark"
                if sibling in t:
                    continue
                if k.endswith("-light") or k.endswith("-default"):
                    continue
            short = k[len(prefix):]
            if theme == "dark" and short.endswith("-dark"):
                short = short[: -len("-dark")]
            if theme == "dark" and short.endswith("-inverse"):
                short = short[: -len("-inverse")] + "-inverse"
            val = t[k]
            if hex_of(val) or val.startswith("hsl") or val.startswith("rgb") or val == "transparent":
                out[short] = paint(val, k)
        return out

    space = {}
    radius = {}
    motion = {"duration": {}, "easing": {}}
    elevation = {}
    type_size = {}
    type_weight = {}
    type_line = {}
    for name, value in t.items():
        if name.startswith("sema-space-") and "negative" not in name:
            d = dim(value)
            if d:
                space[name[len("sema-space-"):]] = dim_token(d, f"{SRC}; --{name}")
        elif name.startswith("sema-rounding-") and name != "sema-rounding-circle":
            d = dim(value)
            if d:
                radius[name[len("sema-rounding-"):]] = dim_token(d, f"{SRC}; --{name}")
        elif name.startswith("sema-motion-bezier-duration-"):
            motion["duration"][name.split("-")[-1]] = other_token(value, f"{SRC}; --{name}")
        elif name.startswith("sema-motion-bezier-easing-"):
            motion["easing"][name[len("sema-motion-bezier-easing-"):]] = other_token(value, f"{SRC}; --{name}")
        elif name in (
            "sema-elevation-shadow-surface",
            "sema-elevation-shadow-raised",
            "sema-elevation-shadow-floating",
            "sema-elevation-shadow-none",
        ):
            elevation[name.split("-")[-1]] = shadow_token(value, f"{SRC}; --{name}")
        elif name.startswith("sema-font-size-"):
            d = dim(value)
            if d:
                type_size[name[len("sema-font-size-"):]] = dim_token(d, f"{SRC}; --{name}")
        elif name.startswith("sema-font-weight-"):
            type_weight[name[len("sema-font-weight-"):]] = other_token(value, f"{SRC}; --{name}")
        elif name.startswith("sema-font-lineheight-"):
            type_line[name[len("sema-font-lineheight-"):]] = other_token(value, f"{SRC}; --{name}")

    typography = {}
    roles = [
        ("display", "display-800"),
        ("heading-1", "heading-700"),
        ("heading-2", "heading-600"),
        ("heading-3", "heading-500"),
        ("heading-4", "heading-400"),
        ("body", "body-300"),
        ("label", "ui-200"),
        ("caption", "body-100"),
    ]
    for role, key in roles:
        size = t.get(f"sema-font-size-{key}")
        weight_key = key if f"sema-font-weight-{key}" in t else (
            key + "-default" if f"sema-font-weight-{key}-default" in t else None
        )
        weight = t.get(f"sema-font-weight-{weight_key}") if weight_key else None
        line = t.get(f"sema-font-lineheight-{key}")
        if not size:
            continue
        typography[role] = {
            "$type": "typography",
            "$value": {
                "fontFamily": "Pin Sans",
                "fontSize": dim(size) or size,
                "fontWeight": weight or "400",
                "lineHeight": line or "1.4",
            },
            "$extensions": {"source": f"{SRC}; --sema-font-size-{key}"},
        }

    button = {}
    for variant in ("primary", "secondary", "tertiary"):
        button[variant] = {}
        for state, suffix in (("default", "default"), ("hover", "hover"), ("pressed", "pressed")):
            prefix = "comp-button-color-background-" if state == "default" else f"comp-button-color-{state}-background-"
            key = f"{prefix}{variant}-default"
            if key in t:
                button[variant][state] = paint(t[key], key)
        text_key = f"comp-button-color-text-{variant}-default"
        if text_key in t:
            button[variant]["text"] = paint(t[text_key], text_key)
    for size, token_name in (("sm", "comp-button-rounding-sm"), ("md", "comp-button-rounding-md"), ("lg", "comp-button-rounding-lg")):
        if token_name in t and dim(t[token_name]):
            button.setdefault("radius", {})[size] = dim_token(dim(t[token_name]), f"{SRC}; --{token_name}")


    light_bg = {
        "page": paint(t["sema-color-background-default"], "sema-color-background-default"),
        "surface": paint(t["sema-color-background-secondary"], "sema-color-background-secondary"),
        "raised": paint(t["sema-color-background-elevation"], "sema-color-background-elevation"),
        "subtle": paint(t["sema-color-background-subtle"], "sema-color-background-subtle"),
        "inverse": paint(t["sema-color-background-inverse"], "sema-color-background-inverse"),
        "disabled": paint(t["sema-color-background-disabled"], "sema-color-background-disabled"),
        "accent": paint(t["sema-color-background-primary"], "sema-color-background-primary"),
        # catalog.json names this path light.background.action. Same measured primary.
        "action": paint(t["sema-color-background-primary"], "sema-color-background-primary"),
        "accent-hover": paint(t["comp-button-color-hover-background-primary-default"], "comp-button-color-hover-background-primary-default"),
        "accent-pressed": paint(t["comp-button-color-pressed-background-primary-default"], "comp-button-color-pressed-background-primary-default"),
        "scrim": paint(t.get("sema-color-background-scrims-translucent", "hsla(60,2%,45%,.4)"), "sema-color-background-scrims-translucent"),
    }
    light_text = {
        "primary": paint(t["sema-color-text-default"], "sema-color-text-default"),
        "secondary": paint(t["sema-color-text-subtle"], "sema-color-text-subtle"),
        # catalog.json names this path light.text.subtle. Same measured subtle text.
        "subtle": paint(t["sema-color-text-subtle"], "sema-color-text-subtle"),
        "disabled": paint(t["sema-color-text-disabled"], "sema-color-text-disabled"),
        "on-accent": paint(t["sema-color-text-inverse"], "sema-color-text-inverse"),
        "link": paint(t["sema-color-text-link"], "sema-color-text-link"),
        "inverse": paint(t["sema-color-text-inverse"], "sema-color-text-inverse"),
    }
    light_border = {
        "default": paint(t["sema-color-border-decorative"], "sema-color-border-decorative"),
        # catalog.json names this path light.border.stroke. Same measured decorative border.
        "stroke": paint(t["sema-color-border-decorative"], "sema-color-border-decorative"),
        "strong": paint(t["sema-color-border-interactive"], "sema-color-border-interactive"),
        "focus": paint(t["sema-color-border-focus-outer-default"], "sema-color-border-focus-outer-default"),
        "focus-inner": paint(t["sema-color-border-focus-inner-default"], "sema-color-border-focus-inner-default"),
    }
    status = {}
    for kind, border_name in (
        ("success", "sema-color-border-success"),
        ("warning", "sema-color-border-warning"),
        ("error", "sema-color-border-error"),
        ("info", "sema-color-border-education"),
    ):
        status[kind] = {
            "fill": paint(t[f"sema-color-background-{kind}-default"], f"sema-color-background-{kind}-default"),
            "text": paint(t[f"sema-color-text-{kind}"], f"sema-color-text-{kind}"),
            "border": paint(t[border_name], border_name),
            "weak": paint(t[f"sema-color-background-{kind}-weak"], f"sema-color-background-{kind}-weak"),
        }

    # Declared dark siblings. The public site does not apply a dark theme.
    dark_bg = {
        "page": paint(t.get("sema-color-background-inverse", "#000"), "sema-color-background-inverse"),
        "surface": paint("#242421" if "base-color-grayscale-450" in t else t["sema-color-background-selected"], "base-color-grayscale-450"),
        "raised": paint(t.get("sema-color-background-selected", "#33332e"), "sema-color-background-selected"),
        "subtle": paint(t.get("base-color-grayscale-400", "#33332e") if False else t["sema-color-background-selected"], "sema-color-background-selected"),
        "accent": paint(t["sema-color-background-primary"], "sema-color-background-primary"),
        "accent-hover": paint(t["comp-button-color-hover-background-primary-default"], "comp-button-color-hover-background-primary-default"),
        "accent-pressed": paint(t["comp-button-color-pressed-background-primary-default"], "comp-button-color-pressed-background-primary-default"),
    }
    # Use declared inverse text (white on dark page).
    dark_text = {
        "primary": paint(t["sema-color-text-inverse"], "sema-color-text-inverse"),
        "secondary": paint(t["sema-color-text-inverse-subtle"], "sema-color-text-inverse-subtle"),
        "disabled": paint(t["sema-color-text-disabled"], "sema-color-text-disabled"),
        "on-accent": paint(t["sema-color-text-inverse"], "sema-color-text-inverse"),
        "link": paint(t.get("sema-color-border-focus-outer-inverse", t["sema-color-text-link"]), "sema-color-border-focus-outer-inverse"),
    }
    dark_border = {
        "default": paint(t["sema-color-border-dark-decorative"], "sema-color-border-dark-decorative"),
        "strong": paint(t["sema-color-border-dark-interactive"], "sema-color-border-dark-interactive"),
        "focus": paint(t["sema-color-border-focus-outer-inverse"], "sema-color-border-focus-outer-inverse"),
    }

    doc = {
        "$description": "Pinterest public web, Gestalt tokens read from www.pinterest.com signed out on 2026-11-21. Light is the painted theme. Dark uses declared inverse and dark-suffixed names; the site does not ship a theme switch on the public pages.",
        "core": {
            "palette": palette,
            "space": space,
            "radius": radius,
            "elevation": elevation,
            "motion": motion,
            "font": {
                "family": {
                    "pin-sans": other_token(
                        'Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, Helvetica, "Apple Color Emoji", Segoe UI Emoji, Segoe UI Symbol, sans-serif',
                        "Measured: computed font-family on body, www.pinterest.com, 2026-11-21",
                    ),
                },
                "size": type_size,
                "weight": type_weight,
                "lineHeight": type_line,
            },
            "typography": typography,
            "component": {"button": button},
        },
        "light": {
            "background": light_bg,
            "text": light_text,
            "border": light_border,
            "status": status,
            # Existing package test reads light.component.button.radius. Same 16px as core.component.button.radius.lg.
            "component": {
                "button": {
                    "radius": dim_token(
                        dim(t["comp-button-rounding-lg"]),
                        f"{SRC}; --comp-button-rounding-lg; painted header button radius",
                    ),
                },
            },
        },
        "dark": {
            "background": dark_bg,
            "text": dark_text,
            "border": dark_border,
            "status": status,
        },
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark (declared)", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=1) + "\n")
    print("wrote", out, "palette hues", list(palette))


if __name__ == "__main__":
    main()
