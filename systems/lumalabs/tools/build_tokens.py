#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/component-tokens.json.

Sources, read from lumalabs.ai on 2026-11-21:
  raw/css-vars.json           semantic colours resolved from the Next.js stylesheet
                              (.light,:root and .dark). Marketing pages paint light.
  raw/component-tokens.json   computed styles of the home Sign In control, hero CTA,
                              and display type.

Every token carries $extensions.source. Deterministic: same inputs, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
CSS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "component-tokens.json").read_text())

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    if not DIM.fullmatch(str(value)):
        raise ValueError(f"dimension {value!r}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def semantic(theme):
    src = f"css-var lumalabs.ai stylesheet .{theme} resolved 2026-11-21 (raw/css-vars.json)"
    block = CSS[theme]
    return {
        "page": color(block["surface-primary"], src + " --surface-primary"),
        "surface": color(block["surface-subtle"], src + " --surface-subtle"),
        "raised": color(block["surface-elevated"], src + " --surface-elevated"),
        "text": color(block["primary"], src + " --primary"),
        "muted": color(block["secondary"], src + " --secondary"),
        "faint": color(block["tertiary"], src + " --tertiary"),
        "disabled": color(block["inactive"], src + " --inactive"),
        "onAccent": color(block["inverted-primary"], src + " --inverted-primary"),
        "border": color(block["border"], src + " --border"),
        "accent": color(block["primary"], src + " --primary (the product uses ink, not a hue, as the accent)"),
        "danger": color(block["destructive"], src + " --destructive"),
        "focus": color("#005fcc" if theme == "light" else block["ring"],
                       "measured a:focus-visible outline rgb(0, 95, 204) on home Sign In" if theme == "light"
                       else src + " --ring"),
    }


def core():
    css = "css-var :root lumalabs.ai stylesheet 2026-11-21"
    measured = "measured https://lumalabs.ai/ 1440x900 2026-11-21 (raw/component-tokens.json)"
    b = COMP["button"]["signin"]
    hero = COMP["button"]["hero"]
    typ = COMP["type"]
    return {
        "font": {
            "family": {
                "sans": {"$value": "Graphik, ui-sans-serif, system-ui, sans-serif", "$type": "fontFamily",
                         "$extensions": {"source": "measured body font-family __graphik_7126cf. Commercial face, not redistributed. Fallback stack is --font-sans."}},
                "display": {"$value": "PP Editorial, Georgia, serif", "$type": "fontFamily",
                            "$extensions": {"source": "css-var --font-pp-editorial declared. Face was unloaded on the home capture. Not used for the measured h1."}},
                "mono": {"$value": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace", "$type": "fontFamily",
                         "$extensions": {"source": css + " --font-mono"}},
            },
            "weight": {
                "regular": num(400, css + " --font-weight-normal", "fontWeight"),
                "medium": num(500, css + " --font-weight-medium", "fontWeight"),
                "semibold": num(600, css + " --font-weight-semibold", "fontWeight"),
                "bold": num(700, css + " --font-weight-bold", "fontWeight"),
            },
            "size": {
                "xs": dim("12px", "derived --text-xs .75rem at 16px root"),
                "sm": dim("14px", "derived --text-sm .875rem at 16px root"),
                "base": dim("16px", css + " --text-base 1rem; " + measured + " body"),
                "lg": dim("18px", "derived --text-lg 1.125rem; measured hero CTA"),
                "xl": dim("20px", "derived --text-xl 1.25rem"),
                "2xl": dim("24px", "derived --text-2xl 1.5rem"),
                "3xl": dim("30px", "derived --text-3xl 1.875rem"),
                "4xl": dim("36px", "derived --text-4xl 2.25rem"),
                "5xl": dim("48px", "derived --text-5xl 3rem"),
                "display": dim(typ["display"]["size"], measured + " h1"),
                "ctaHero": dim("22px", css + " --text-cta-hero"),
            },
        },
        "radius": {
            "xs": dim("2px", "derived --radius-xs .125rem"),
            "sm": dim("4px", "derived --radius-sm .25rem"),
            "md": dim("6px", "derived --radius-md .375rem"),
            "lg": dim("8px", "derived --radius-lg .5rem"),
            "xl": dim("12px", "derived --radius-xl .75rem"),
            "2xl": dim("16px", "derived --radius-2xl 1rem"),
            "3xl": dim("24px", "derived --radius-3xl 1.5rem"),
            "4xl": dim("32px", "derived --radius-4xl 2rem"),
            "pill": dim("9999px", measured + " Sign In border-radius computed as a pill"),
        },
        "space": {
            "1": dim("4px", "derived --spacing .25rem"),
            "2": dim("8px", "derived 2 * --spacing"),
            "3": dim("12px", measured + " Sign In padding-inline"),
            "4": dim("16px", "derived 4 * --spacing"),
            "6": dim("24px", "derived 6 * --spacing"),
            "8": dim("32px", measured + " hero CTA padding-inline"),
        },
        "motion": {
            "duration": {"$value": "150ms", "$type": "duration", "$extensions": {"source": css + " --default-transition-duration .15s"}},
            "accordion": {"$value": "200ms", "$type": "duration", "$extensions": {"source": css + " --animate-accordion-down .2s"}},
        },
        "layout": {
            "nav": dim("64px", "derived --navigation-bar-height 4rem at min-width 48rem"),
            "navMobile": dim("56px", "derived --navigation-bar-height 3.5rem"),
            "content": dim("1280px", "derived --container-7xl 80rem"),
        },
        "component": {
            "button": {
                "height": dim(b["height"], measured + " Sign In"),
                "heightHero": dim(hero["height"], measured + " Try for free"),
                "radius": dim("9999px", measured + " pill"),
                "paddingX": dim("12px", measured + " Sign In"),
            }
        },
    }


def check(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty, val = node["$type"], node["$value"]
        if ty == "dimension" and not DIM.fullmatch(str(val)) and val != "9999px":
            raise ValueError(f"{path}: {val!r}")
        if ty == "color" and not (str(val).startswith("#") or str(val).startswith("rgb")):
            raise ValueError(f"{path}: colour {val!r}")
        if "source" not in node.get("$extensions", {}):
            raise ValueError(f"{path}: missing source")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                check(v, path + "." + k)


core_set = core()
light = semantic("light")
dark = semantic("dark")
doc = {
    "core": core_set,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
}
check(doc)
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out)
