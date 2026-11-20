#!/usr/bin/env python3
"""Build tokens.json from the Lummi public signed-out harvest.

Colour roles are the shadcn HSL custom properties declared on :root
(--background, --primary, …) and the matching --*-dark twins. Those twins
are declared, not painted: the captured pages keep a light root. Component
sizes come from computed styles on 2026-11-18. HSL triplets are converted
to hex here so the style guide can paint them. Nothing is recalled.
"""
import colorsys
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
M = "Measured computed style, public lummi.ai, 2026-11-18, light, 1440x900"
C = "Declared on :root in the lummi.ai stylesheet, resolved 2026-11-18, light"
K = "Declared as a --*-dark custom property on :root, 2026-11-18. Not painted on the captured pages."
D = "Derived from a measured value on the same capture"


def hsl_to_hex(raw):
    """Turn `240 6% 10%` or `239,84%,67%` into #rrggbb. Leave other strings."""
    s = raw.strip()
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)[,\s]+(-?\d+(?:\.\d+)?)%?[,\s]+(-?\d+(?:\.\d+)?)%?", s)
    if not m:
        return None
    h, sat, lig = float(m.group(1)) / 360, float(m.group(2)) / 100, float(m.group(3)) / 100
    r, g, b = colorsys.hls_to_rgb(h % 1, lig, sat)
    return "#{:02x}{:02x}{:02x}".format(round(r * 255), round(g * 255), round(b * 255))


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


# Literals read from computed styles, kept so aliases can point at them.
core = {
    "color": {
        "ink": color("#09090b", f"{M}: body and h1 color rgb(9, 9, 11)"),
        "inkHover": color("#18181b", f"{M}: Log in hover and selected nav rgb(24, 24, 27)"),
        "white": color("#ffffff", f"{M}: page and popover background"),
        "offwhite": color("#fafafa", f"{M}: primary button label rgb(250, 250, 250)"),
        "muted": color("#71717a", f"{M}: unselected nav and license line rgb(113, 113, 122)"),
        "wash": color("#f4f4f5", f"{M}: icon-button hover and tag pill rgb(244, 244, 245)"),
        "black": color("#000000", f"{M}: Try Pro for free fill"),
        "zinc700": color("#3f3f46", f"{M}: Try Pro and Continue hover rgb(63, 63, 70)"),
        "proYellow": color("#e7b008", f"{D}: declared --yellow 45 93% 47%, converted from HSL. The word Pro is painted with this role, not a sampled glyph"),
    },
    "font": {
        "family": {
            "sans": font('Inter, "Inter Fallback"', f"{M}: body font-family"),
            "pro": font('"DM Sans", sans-serif', f"{M}: /pro marketing CTA, a separate Webflow page"),
        },
        "weight": {
            "regular": num(400, f"{M}: lede and body", "fontWeight"),
            "medium": num(500, f"{M}: nav, buttons, search", "fontWeight"),
            "semibold": num(600, f"{M}: display and Continue", "fontWeight"),
            "bold": num(700, f"{M}: Forgot password?", "fontWeight"),
        },
        "size": {
            "tag": dim("12px", f"{M}: photo tag pill and license line"),
            "ui": dim("14px", f"{M}: nav, buttons, fields, search"),
            "body": dim("16px", f"{M}: body default"),
            "lede": dim("20px", f"{M}: home subtitle"),
            "section": dim("18px", f"{M}: Similar images heading"),
            "explore": dim("64px", f"{M}: Explore h1"),
            "search": dim("104px", f"{M}: search results h1 Forest"),
            "display": dim("141.12px", f"{M}: home h1 at 1440, text-[9.6vw]"),
        },
        "lineHeight": {
            "display": dim("144px", f"{M}: home h1"),
            "explore": dim("70.4px", f"{M}: Explore h1"),
            "lede": dim("28px", f"{M}: home subtitle"),
            "body": dim("24px", f"{M}: body"),
            "ui": dim("24px", f"{M}: 14px nav line-height"),
            "tag": dim("14px", f"{M}: tag pill"),
        },
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.display}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.display}",
                "letterSpacing": "-7.056px",
            },
            "$extensions": {"source": f"{M}: home h1, tracking-tighter"},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.explore}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.explore}",
            },
            "$extensions": {"source": f"{M}: Explore h1"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "{font.lineHeight.body}",
            },
            "$extensions": {"source": f"{M}: body default"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.ui}",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": "{font.lineHeight.ui}",
            },
            "$extensions": {"source": f"{M}: nav and buttons"},
        },
        "caption": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.tag}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "{font.lineHeight.tag}",
            },
            "$extensions": {"source": f"{M}: license line"},
        },
    },
    "space": {
        "1": dim("4px", f"{D}: 4px step the 12/16/40 control sizes sit on"),
        "2": dim("8px", f"{D}: 4px times 2"),
        "3": dim("12px", f"{M}: Try Pro padding-inline"),
        "4": dim("16px", f"{M}: login field padding-inline and Continue"),
        "6": dim("24px", f"{M}: body line-height"),
        "10": dim("40px", f"{M}: nav link, icon button and Try Pro height"),
        "12": dim("48px", f"{M}: login field and Continue height"),
    },
    "radius": {
        "control": dim("4px", f"{M}: Try Pro, Download, login field, icon button, --radius 0.25rem"),
        "tab": dim("2px", f"{M}: By Subject tab"),
        "menu": dim("6px", f"{M}: Daily picks menu and search dialog"),
        "card": dim("8px", f"{M}: explore category tile"),
        "pill": dim("9999px", f"{M}: tag pill and heart icon button"),
    },
    "border": {
        "hairline": dim("1px", f"{M}: login field and menu panel border"),
        "focus": dim("2px", f"{M}: focus-visible outline width"),
    },
    "elevation": {
        "menu": {
            "$type": "shadow",
            "$value": [
                {"color": "rgba(0, 0, 0, 0.1)", "offsetX": "0px", "offsetY": "4px", "blur": "6px", "spread": "-1px"},
                {"color": "rgba(0, 0, 0, 0.1)", "offsetX": "0px", "offsetY": "2px", "blur": "4px", "spread": "-2px"},
            ],
            "$extensions": {"source": f"{M}: Daily picks menu and search dialog box-shadow"},
        },
    },
    "sizing": {
        "control": dim("40px", f"{M}: header buttons"),
        "field": dim("48px", f"{M}: login fields and Continue"),
        "search": dim("38px", f"{M}: header search input"),
        "icon": dim("20px", f"{M}: header icon buttons use a 20px svg"),
        "focus": dim("2px", f"{M}: focus-visible outline"),
    },
    "motion": {
        "fast": num("150ms", f"{M}: button and link transition-duration 0.15s", "duration"),
        "slow": num("300ms", f"{M}: opacity transition 0.3s on one header control", "duration"),
        "ease": {
            "$type": "cubicBezier",
            "$value": [0.4, 0, 0.2, 1],
            "$extensions": {"source": f"{M}: cubic-bezier(0.4, 0, 0.2, 1) on nav and buttons"},
        },
    },
    "layout": {
        "desktop": dim("1440px", f"{M}: desktop viewport innerWidth"),
        "phone": dim("390px", "Phone capture width requested and used, 390x844 at 2x"),
        "nav": dim("64px", f"{D}: sticky tool bar sits at top-16, 64px under the header"),
    },
}

LIGHT_ROLES = {
    "background": "page",
    "card": "surface",
    "popover": "overlay",
    "foreground": "text",
    "muted-foreground": "textMuted",
    "faint-foreground": "textFaint",
    "primary": "accent",
    "primary-foreground": "onAccent",
    "primary-hover": "accentHover",
    "secondary": "secondary",
    "border": "border",
    "destructive": "danger",
    "ring": "focus",
    "yellow": "warning",
    "highlight": "info",
    "muted": "surfaceMuted",
    "faint": "surfaceFaint",
    "input": "input",
}

# Declared HSL, converted. These match the computed rgb readings
# (foreground 240 10% 4% is #09090b, muted-foreground 240 4% 46% is #71717a).
DECLARED = {
    "background": "0 0% 100%",
    "foreground": "240 10% 4%",
    "card": "0 0% 100%",
    "popover": "0 0% 100%",
    "primary": "240 6% 10%",
    "primary-foreground": "0 0% 98%",
    "primary-hover": "240 5% 26%",
    "secondary": "240 5% 96%",
    "muted": "240 5% 96%",
    "muted-foreground": "240 4% 46%",
    "faint": "0 0% 98%",
    "faint-foreground": "240 5% 65%",
    "destructive": "0 84% 60%",
    "border": "240 6% 90%",
    "input": "240 6% 90%",
    "ring": "240 5% 65%",
    "yellow": "45 93% 47%",
    "highlight": "239,84%,67%",
}
DECLARED_DARK = {
    "background": "240 10% 4%",
    "foreground": "0 0% 98%",
    "card": "240 10% 4%",
    "popover": "240 10% 4%",
    "primary": "0 0% 98%",
    "primary-foreground": "240 6% 10%",
    "primary-hover": "240 6% 90%",
    "secondary": "240 4% 16%",
    "muted": "240 4% 16%",
    "muted-foreground": "240 5% 65%",
    "faint": "240 4% 10%",
    "faint-foreground": "240 4% 46%",
    "destructive": "0 72% 51%",
    "border": "240 5% 26%",
    "input": "240 4% 16%",
    "ring": "240 5% 84%",
    "yellow": "45 93% 47%",
    "highlight": "239,84%,67%",
}


def roles(table, source):
    out = {}
    for key, name in LIGHT_ROLES.items():
        hx = hsl_to_hex(table[key])
        if not hx:
            raise SystemExit(f"cannot convert {key}={table[key]!r}")
        out[name] = color(hx, f"{source}: --{key} = {table[key]}")
    return out


class CheckError(SystemExit):
    """A token that fails the alias, source or type check."""


def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


def check(doc):
    """Every alias resolves inside its theme's sets, every token has a source, and a
    duration is a duration. Returns the flat {path: token} of every set."""
    names = {n for n, _ in walk(doc["core"])}
    names |= {n for n, _ in walk(doc["light"])}
    names |= {n for n, _ in walk(doc["dark"])}
    flat = {}
    for path, tok in walk({"core": doc["core"], "light": doc["light"], "dark": doc["dark"]}):
        flat[path] = tok
        for blob in strings(tok["$value"]):
            for alias in re.findall(r"\{([^{}]+)\}", blob):
                if alias not in names:
                    raise CheckError(f"{path} alias {{{alias}}} missing")
        src = tok.get("$extensions", {}).get("source", "")
        if not src:
            raise CheckError(f"{path} has no source")
        if isinstance(tok["$value"], str) and re.fullmatch(r"[\d.]+m?s", tok["$value"]) and tok.get("$type") != "duration":
            raise CheckError(f"{path} is a time typed {tok.get('$type')}, not duration")
    return flat


def build():
    light = roles(DECLARED, C)
    light["textOnAccent"] = color("{color.offwhite}", f"{M}: Try Pro label rgb(250, 250, 250)")
    light["link"] = color("{color.ink}", f"{M}: Log in and license links use the ink, not a blue")
    light["scrim"] = color("rgba(0, 0, 0, 0.8)", f"{M}: search dialog overlay class bg-black/80")
    light["accentPressed"] = color("{color.zinc700}", f"{M}: Try Pro and Continue pressed/hover fill")
    dark = roles(DECLARED_DARK, K)
    return {
        "core": json.loads(json.dumps(core)),
        "light": light,
        "dark": dark,
        "$themes": [
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
                "$description": "The painted theme on every captured lummi.ai page, 2026-11-18.",
            },
            {
                "id": "dark",
                "name": "Dark",
                "selectedTokenSets": {"core": "source", "dark": "enabled"},
                "$description": "Declared --*-dark custom properties. Not painted on the captured pages.",
            },
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    }


if __name__ == "__main__":
    tokens = build()
    names = check(tokens)
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("tokens", len(names), "light.page", tokens["light"]["page"]["$value"], "dark.page", tokens["dark"]["page"]["$value"])
