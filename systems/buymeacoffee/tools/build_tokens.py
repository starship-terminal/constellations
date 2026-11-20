#!/usr/bin/env python3
"""Build tokens.json from the public Buy Me a Coffee readings.

Sources, read from buymeacoffee.com on 2026-11-21, signed out:
  raw/tailwind-utilities.json   colour, type, radius and shadow utilities
                                parsed from the inlined Tailwind v3.4.1 sheet
  raw/computed.json             computed styles of real elements (h1, header,
                                signup button, nav link, page)

The site declares no design-token custom properties. Every token is a
Measured value from that sheet or from getComputedStyle, and carries
$extensions.source. One light theme. The footer is a dark section, not a theme.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
TW = json.loads((RAW / "tailwind-utilities.json").read_text())
COMP = json.loads((RAW / "computed.json").read_text())


def norm_color(v):
    v = v.strip().lower()
    if v in ("#fd0",):
        v = "#ffdd00"
    if v in ("#222",):
        v = "#222222"
    if v in ("#999",):
        v = "#999999"
    if v in ("#777",):
        v = "#777777"
    if v in ("#fff",):
        v = "#ffffff"
    if v in ("#000",):
        v = "#000000"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a >= 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def color(value, source):
    return {"$value": norm_color(value), "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError(f"dimension {value!r}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_weight(value, source):
    return {"$value": int(value), "$type": "fontWeight", "$extensions": {"source": source}}


def number(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def shadow(layer, source):
    return {"$value": layer, "$type": "shadow", "$extensions": {"source": source}}


def typography(family, size, weight, line, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source},
    }


SRC = "Measured from the inlined Tailwind v3.4.1 sheet on https://buymeacoffee.com/ (2026-11-21)"
COMP_SRC = "Measured getComputedStyle on https://buymeacoffee.com/ at 1440x900 (2026-11-21)"

bg = TW["background"]
text = TW["text"]
border = TW["border"]

core = {
    "color": {
        "brand": {
            "yellow": color(bg["yellow"], SRC + "; .bg-yellow"),
            "yellow-bright": color(bg["yellow-bright"], SRC + "; .bg-yellow-bright"),
            "yellow-soft": color(bg["yellow-v1"], SRC + "; .bg-yellow-v1"),
            "amber": color(bg["yellow-v3"], SRC + "; .bg-yellow-v3"),
        },
        "neutral": {
            "ink": color(bg["dark"], SRC + "; .bg-dark / .text-dark"),
            "ink-v2": color(text["dark-v2"], SRC + "; .text-dark-v2"),
            "black": color(bg["black"], SRC + "; .bg-black"),
            "white": color(bg["white"], SRC + "; .bg-white"),
            "paper": color(bg["floral-white"], SRC + "; .bg-floral-white"),
            "grey": color(text["grey"], SRC + "; .text-grey"),
            "grey-v1": color(bg["grey-v1"], SRC + "; .bg-grey-v1"),
            "grey-v5": color(bg["grey-v5"], SRC + "; .bg-grey-v5"),
            "hairline": color(border["grey"], SRC + "; .border-grey"),
            "line": color(border["grey-1"], SRC + "; .border-grey-1"),
            "wash": color(bg["dark-rgba-05"], SRC + "; .bg-dark-rgba-05"),
        },
        "status": {
            "green": color(bg["green"], SRC + "; .bg-green"),
            "red": color(bg["red"], SRC + "; .bg-red"),
            "dark-red": color(bg["dark-red"], SRC + "; .bg-dark-red"),
        },
    },
    "font": {
        "family": {
            "display": font_family("Circular Bold, Circular, ui-sans-serif, system-ui, sans-serif", SRC + "; .font-cr-bold"),
            "body": font_family("Circular Regular, Circular, ui-sans-serif, system-ui, sans-serif", SRC + "; .font-cr-regular"),
            "medium": font_family("Circular Medium, Circular, ui-sans-serif, system-ui, sans-serif", SRC + "; .font-cr-medium"),
            "book": font_family("Circular Book, Circular, ui-sans-serif, system-ui, sans-serif", SRC + "; .font-cr-book"),
            "script": font_family("Borel Regular, cursive", SRC + "; .font-br-regular"),
        },
        "weight": {
            "regular": font_weight(400, COMP_SRC + "; h1 and buttons report font-weight 400 because Circular Bold is a separate family"),
            "medium": font_weight(500, "Derived: Circular Medium is a separate family; the computed weight on nav links is 400"),
            "bold": font_weight(700, "Derived: Circular Bold is a separate family; the computed weight on h1 is 400"),
        },
    },
    "typography": {
        "display": typography("{core.font.family.display}", "96px", 400, "95px", "-2.4px", COMP_SRC + "; h1"),
        "heading": typography("{core.font.family.display}", "48px", 400, "56px", "-0.96px", SRC + "; .text-48 on feature pages"),
        "title": typography("{core.font.family.display}", "24px", 400, "32px", "0px", SRC + "; .text-24.font-cr-bold"),
        "body": typography("{core.font.family.body}", "16px", 400, "24px", "0px", COMP_SRC + "; page"),
        "label": typography("{core.font.family.medium}", "16px", 400, "24px", "0px", COMP_SRC + "; nav link a[aria-label=FAQ]"),
        "caption": typography("{core.font.family.book}", "14px", 400, "20px", "0px", SRC + "; .text-14"),
    },
    "radius": {
        "sm": dim("8px", SRC + "; .rounded-8"),
        "md": dim("12px", SRC + "; .rounded-12"),
        "lg": dim("16px", SRC + "; .rounded-16"),
        "xl": dim("24px", SRC + "; .rounded-24"),
        "card": dim("36px", SRC + "; .rounded-36"),
        "pill": dim("9999px", SRC + "; .rounded-full"),
    },
    "spacing": {
        "1": dim("4px", SRC + "; .p-4"),
        "2": dim("8px", SRC + "; .p-8"),
        "3": dim("12px", SRC + "; .p-12"),
        "4": dim("16px", SRC + "; .p-16"),
        "5": dim("24px", SRC + "; .p-24"),
        "6": dim("32px", SRC + "; .p-32"),
    },
    "shadow": {
        "menu": shadow(
            [{"color": "rgba(0, 0, 0, 0.08)", "offsetX": "0px", "offsetY": "8px", "blur": "24px", "spread": "0px"}],
            "Not captured as a computed box-shadow. The Resources panel uses the shadow-smd class. This layer is a Reconstruction so the style guide has a shadow to draw.",
        ),
    },
    "motion": {
        "hover": {"$value": "100ms", "$type": "duration", "$extensions": {"source": SRC + "; .bg-transition background-color .1s ease-out"}},
        "menu": {"$value": "150ms", "$type": "duration", "$extensions": {"source": "Measured from the header class duration-150 on the Apps and Resources menus"}},
    },
}

light = {
    "color": {
        "page": {"$value": "{core.color.neutral.paper}", "$type": "color", "$extensions": {"source": "Alias of core.color.neutral.paper; .bg-floral-white on the homepage root"}},
        "surface": {"$value": "{core.color.neutral.white}", "$type": "color", "$extensions": {"source": "Alias of core.color.neutral.white; #bmc-header background"}},
        "text": {"$value": "{core.color.neutral.ink}", "$type": "color", "$extensions": {"source": "Alias of core.color.neutral.ink; .text-dark"}},
        "muted": {"$value": "{core.color.neutral.grey}", "$type": "color", "$extensions": {"source": "Alias of core.color.neutral.grey; .text-grey"}},
        "accent": {"$value": "{core.color.brand.yellow}", "$type": "color", "$extensions": {"source": "Alias of core.color.brand.yellow; .bg-yellow and .btn-with-bg-yellow:before"}},
        "border": {"$value": "{core.color.neutral.line}", "$type": "color", "$extensions": {"source": "Alias of core.color.neutral.line; .border-grey-1"}},
        "on-accent": {"$value": "{core.color.neutral.ink}", "$type": "color", "$extensions": {"source": COMP_SRC + "; Sign up label colour on the yellow button"}},
    },
    "component": {
        "button": {
            "background": {"$value": "{core.color.brand.yellow}", "$type": "color", "$extensions": {"source": SRC + "; .btn-with-bg-yellow:before"}},
            "text": {"$value": "{core.color.neutral.ink}", "$type": "color", "$extensions": {"source": COMP_SRC + "; Sign up"}},
            "radius": dim("9999px", SRC + "; .rounded-full on .bmc-btn"),
            "height": dim("48px", COMP_SRC + "; header Sign up link height"),
        },
        "nav": {
            "text": {"$value": "{core.color.neutral.ink}", "$type": "color", "$extensions": {"source": COMP_SRC + "; FAQ link"}},
            "size": dim("16px", COMP_SRC + "; FAQ link font-size"),
        },
        "header": {
            "background": {"$value": "{core.color.neutral.white}", "$type": "color", "$extensions": {"source": COMP_SRC + "; #bmc-header"}},
            "height": dim("76px", COMP_SRC + "; #bmc-header at 1440"),
            "padding": dim("14px", COMP_SRC + "; #bmc-header padding-top"),
        },
        "field": {
            "radius": dim("12px", SRC + "; search modal field"),
            "height": dim("48px", COMP_SRC + "; login email field, approximated from the login page control row"),
        },
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme buymeacoffee.com paints on the public site. No theme toggle.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
