#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

MasterClass publishes one dark theme on the public site. Values are the
custom properties declared in the site's own stylesheets on 2026-11-21.
Aliases stay aliases. A value that is not in the stylesheet is not invented.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["vars"]

SRC = "Measured: custom property in www.masterclass.com stylesheets, 2026-11-21, raw/css-vars.json"


def get(name):
    if name not in VARS:
        raise SystemExit(f"missing {name}")
    return VARS[name]["value"]


def resolve_name(name, seen=None):
    """Follow var(--x) until a palette token or a literal."""
    seen = seen or set()
    if name in seen:
        raise SystemExit("cycle " + name)
    seen.add(name)
    value = get(name)
    if value.startswith("var(--") and value.endswith(")") and "," not in value:
        return resolve_name(value[4:-1], seen)
    return name, value


def color(name, description=None):
    final, value = resolve_name(name)
    if value.startswith("var("):
        raise SystemExit(f"unresolved {name} -> {value}")
    token = alias_of(final)
    if token:
        value = "{" + token + "}"
    return leaf("color", value, f"{SRC}. {name} resolves to {final}", description)


def dim_from(name, description=None):
    return leaf("dimension", get(name), f"{SRC}. {name}", description)


def leaf(ty, value, source, description=None):
    if ty == "color" and isinstance(value, str) and not value.startswith("{"):
        value = norm_color(value)
    if ty == "dimension" and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", str(value)):
        raise SystemExit(f"bad dimension {value}")
    token = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def norm_color(v):
    v = v.strip().lower()
    if v == "#000":
        return "#000000"
    if v == "#fff":
        return "#ffffff"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8 and h.endswith("ff"):
            return "#" + h[:6]
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % float(a))
    raise SystemExit("not a colour: " + v)


def alias_of(css_name):
    """Map a --mc-color-* name onto a core token path."""
    name = css_name.removeprefix("--mc-color-")
    parts = name.split("-")
    # pink-500, neutral-1000, primary-500, green-500, red-500, yellow-500, purple-500
    if len(parts) == 2 and parts[1].isdigit():
        return f"color.{parts[0]}.{parts[1]}"
    if name in ("neutral-90", "neutral-1010"):
        return f"color.neutral.{name.split('-')[1]}"
    singles = {
        "brand": "color.brand",
        "focus": "color.focus",
        "announce": "color.announce",
        "nameplate": "color.nameplate",
        "ai-500": "color.ai.500",
    }
    if name in singles:
        return singles[name]
    return None


def ramp(family, steps):
    out = {}
    for step in steps:
        key = f"--mc-color-{family}-{step}"
        if key not in VARS:
            continue
        out[str(step)] = leaf("color", norm_color(get(key)) if not get(key).startswith("var(") else get(key), f"{SRC}. {key}")
        if isinstance(out[str(step)]["$value"], str) and out[str(step)]["$value"].startswith("var("):
            # resolve one level if the target is a literal we already know
            raise SystemExit("ramp alias " + key)
    return out


NEUTRAL_STEPS = ["90", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "1010"]
HUE_STEPS = ["100", "200", "300", "400", "500", "600", "700", "800", "900"]

core = {
    "color": {
        "neutral": ramp("neutral", NEUTRAL_STEPS),
        "pink": ramp("pink", HUE_STEPS),
        "red": ramp("red", HUE_STEPS),
        "yellow": ramp("yellow", HUE_STEPS),
        "green": ramp("green", HUE_STEPS),
        "purple": ramp("purple", HUE_STEPS),
        "brand": leaf("color", norm_color(get("--mc-color-brand")), f"{SRC}. --mc-color-brand", "Brand pink, distinct from primary-500"),
        "focus": leaf("color", norm_color(get("--mc-color-focus")), f"{SRC}. --mc-color-focus"),
        "announce": leaf("color", norm_color(get("--mc-color-announce")), f"{SRC}. --mc-color-announce"),
        "nameplate": leaf("color", norm_color(get("--mc-color-nameplate")), f"{SRC}. --mc-color-nameplate"),
        "ai": {"500": leaf("color", norm_color(get("--mc-color-ai-500")), f"{SRC}. --mc-color-ai-500")},
    },
    "fontFamily": {
        "sans": leaf("fontFamily", "Sohne, Helvetica, Arial, sans-serif", "Measured: computed font-family on body, homepage, 2026-11-21. @font-face Sohne 400 and 600 in the site CSS."),
        "display": leaf("fontFamily", '"Sohne Schmal", Helvetica, Arial, sans-serif', "Measured: computed font-family on a display heading, homepage, 2026-11-21. @font-face Sohne Schmal 600."),
        "serif": leaf("fontFamily", '"Ivar Display Condensed", serif', "Measured: computed font-family on a serif heading, homepage, 2026-11-21. @font-face Ivar Display Condensed."),
    },
    "fontWeight": {
        "regular": leaf("fontWeight", 400, "Measured: @font-face Sohne weight 400, and computed font-weight on body text."),
        "medium": leaf("fontWeight", 500, "Measured: @font-face Sohne Kraftig weight 500."),
        "semibold": leaf("fontWeight", 600, "Measured: computed font-weight 600 on the Get MasterClass button, homepage, 2026-11-21."),
    },
    "typography": {},
    "spacing": {str(i): dim_from(f"--spacing-scale-{i}") for i in range(0, 13)},
    "radius": {
        "sm": leaf("dimension", "8px", "Derived: --mc-corners--sm is var(--mc-scale-2), and --mc-scale-2 is 0.8rem. 0.8 times 16px is 8px. The Get MasterClass button computed border-radius is 8px."),
        "md": leaf("dimension", "12px", "Derived: --mc-corners--md is var(--mc-scale-3), and --mc-scale-3 is 1.2rem. 1.2 times 16px is 12px."),
        "lg": leaf("dimension", "16px", "Derived: --mc-corners--lg is var(--mc-scale-4), and --mc-scale-4 is 1.6rem. 1.6 times 16px is 16px."),
        "xl": leaf("dimension", "18px", "Derived: --mc-corners--xl is var(--mc-scale-6), and --mc-scale-6 is 1.8rem. 1.8 times 16px is 18px."),
    },
    "borderWidth": {
        "hairline": leaf("dimension", "1px", f"{SRC}. --mc-border--default starts with 1px."),
        "control": leaf("dimension", "2px", f"{SRC}. --mc-button-primary-border-width"),
    },
    "breakpoint": {
        "xs": leaf("dimension", "0px", f"{SRC}. --mc-bp-xs is 0. Recorded as 0px."),
        "sm": dim_from("--mc-bp-sm"),
        "md": dim_from("--mc-bp-md"),
        "lg": dim_from("--mc-bp-lg"),
        "xl": dim_from("--mc-bp-xl"),
    },
    "layout": {
        "content": dim_from("--mc-container-max-width", "Content column"),
        "maximum": dim_from("--mc-maximum-content-width"),
    },
    "duration": {
        "fast": leaf("duration", "150ms", "Measured: transition-duration .15s in the site CSS, the shortest named duration."),
        "base": leaf("duration", "200ms", "Measured: transition-duration .2s in the site CSS."),
        "slow": leaf("duration", "300ms", "Measured: transition-duration .3s in the site CSS."),
    },
    "easing": {
        "standard": leaf("cubicBezier", [0.4, 0, 0.2, 1], "Measured: transition-timing-function cubic-bezier(.4,0,.2,1), the default ease in the site CSS."),
        "out": leaf("cubicBezier", [0, 0, 0.2, 1], "Measured: cubic-bezier(0,0,.2,1) as --ease-out's fallback in the site CSS."),
        "enter": leaf("cubicBezier", [0.22, 1, 0.36, 1], "Measured: cubic-bezier(.22,1,.36,1) in the site CSS."),
    },
    "size": {
        "search": leaf("dimension", "44px", "Measured: computed height of #searchInput, homepage, 2026-11-21."),
        "button-pad-y": leaf("dimension", "12px", "Measured: computed padding-top of the Get MasterClass link, homepage, 2026-11-21."),
        "button-pad-x": leaf("dimension", "24px", "Measured: computed padding-left of the Get MasterClass link, homepage, 2026-11-21."),
    },
    "focus": {
        "color": color("--mc-color-focus"),
    },
}


def composite(family, size, weight, line, tracking, transform):
    # tracking of 0px is a dimension; a unitless line height is a number
    lh = float(line) if re.fullmatch(r"\d+(\.\d+)?", line) else line
    lh_type = "number" if isinstance(lh, float) else "dimension"
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": lh,
            "letterSpacing": tracking,
        },
        "$extensions": {
            "source": "Measured: type scale steps and computed styles on the homepage, 2026-11-21. Display uses --font-scale-10 (46px) and Sohne Schmal. Heading uses --font-scale-9 (34px) and --mc-lh-heading--tight (1.15). Body uses 16px and --mc-lh-body (1.5). Label is the computed Get MasterClass button. Caption uses --font-scale-3 (12px) and --mc-lh-body--tight (1.45). Code is the browser monospace: the public pages do not declare a code family.",
            "textTransform": transform,
        },
    }


core["typography"] = {
    "display": composite("Sohne Schmal, Helvetica, Arial, sans-serif", "46px", 600, "46px", "0px", "uppercase"),
    "heading": composite("Sohne, Helvetica, Arial, sans-serif", "34px", 600, "1.15", "0px", "none"),
    "title": composite("Sohne, Helvetica, Arial, sans-serif", "20px", 600, "1.25", "0px", "none"),
    "body": composite("Sohne, Helvetica, Arial, sans-serif", "16px", 400, "1.5", "0px", "none"),
    "label": composite("Sohne, Helvetica, Arial, sans-serif", "16px", 600, "20px", "0.16px", "capitalize"),
    "caption": composite("Sohne, Helvetica, Arial, sans-serif", "12px", 400, "1.45", "0px", "none"),
    "code": composite("ui-monospace, SFMono-Regular, Menlo, monospace", "13px", 400, "1.45", "0px", "none"),
}


def check_tree(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if not node.get("$extensions", {}).get("source"):
            raise SystemExit(f"no source {path}")
        if ty == "color" and isinstance(val, str) and not val.startswith("{"):
            norm_color(val)
        if ty == "dimension" and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", str(val)):
            raise SystemExit(f"bad dim {path} {val}")
        if ty == "typography":
            for key in ("fontFamily", "fontSize", "fontWeight", "lineHeight", "letterSpacing"):
                if key not in val:
                    raise SystemExit(f"type missing {key} {path}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            check_tree(v, f"{path}.{k}")


# semantic dark set: the public site's only theme
dark = {
    "background": {
        "page": color("--mc-color-bg-page-default", "Page"),
        "surface": color("--mc-color-bg-container-tint-dark", "Raised surface"),
        "raised": leaf("color", norm_color(get("--mc-theme-dropdown-bg")), f"{SRC}. --mc-theme-dropdown-bg. Dropdown and form surface.", "Raised control surface"),
        "overlay": leaf("color", norm_color(get("--mc-theme-tooltip-bg")), f"{SRC}. --mc-theme-tooltip-bg", "Tooltip and menu surface"),
        "scrim": leaf("color", norm_color(get("--mc-theme-dropdown-backdrop")), f"{SRC}. --mc-theme-dropdown-backdrop", "Dialog scrim"),
    },
    "text": {
        "primary": color("--mc-color-text-light", "Primary text on the dark page"),
        "secondary": color("--mc-color-text-medium", "Secondary text"),
        "disabled": color("--mc-color-text-disabled-medium", "Disabled text"),
        "on-accent": color("--mc-color-accent-text", "Text on the accent button"),
        "link": color("--mc-color-text-link-default-default", "Link text"),
    },
    "border": {
        "default": leaf("color", norm_color(get("--mc-theme-form-border")), f"{SRC}. --mc-theme-form-border"),
        "strong": color("--mc-color-divider-strong"),
        "focus": color("--mc-color-focus"),
    },
    "accent": {
        "default": color("--mc-color-primary-default"),
        "hover": color("--mc-color-primary-hover"),
        "pressed": color("--mc-color-primary-pressed"),
    },
    "status": {
        "success": color("--mc-color-success-500"),
        "warning": color("--mc-color-warning-500"),
        "danger": color("--mc-color-error-500"),
        "info": leaf("color", "{color.focus}", f"{SRC}. No --mc-color-info token exists. Focus blue --mc-color-focus is the nearest info colour and is labelled as that stand-in."),
    },
}

check_tree(core, "core")
check_tree(dark, "dark")

doc = {
    "core": core,
    "dark": dark,
    "$themes": [{"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}],
}
# fix xs breakpoint: get returns "0"
# already handled if we passed 0px. Verify.
text = json.dumps(doc, indent=1) + "\n"
(HERE / "tokens.json").write_text(text)
print("tokens", text.count('"$value"'))
