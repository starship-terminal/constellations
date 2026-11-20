#!/usr/bin/env python3
"""Build tokens.json from the Melius public capture.

www.melius.com declares a named hex palette on :root (--color-orange,
--color-yellow, --color-gray-dark-1, --radius-*, --spacing). tools/capture/vars.mjs
resolved those to computed values. One painted theme on the marketing site.
The signed-out app paints a dark card; those colours are recorded only when a
computed style measured them. There is no dark token set.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))

VARS = json.loads((RAW / "css-vars.json").read_text())
LIGHT = VARS["resolved"]["light"]
COMP = json.loads((RAW / "components-computed.json").read_text()) if (RAW / "components-computed.json").exists() else {"components": {}}

S = "Declared on the www.melius.com :root, 2026-11-19"
M = "Measured computed style, public Melius pages, 2026-11-19, light, 1440"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def other(value, source, ty="other"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def _marketing_root():
    """The top-level :root rule of the www.melius.com sheet: the one that declares the named
    --color-* palette. The merged `resolved` map keeps the last of 385 sheets, so a docs or app sheet
    that redeclares a name (--color-black #000, --container-xl 36rem) would win there."""
    rules = [a for a in VARS["app"] if a["selector"].startswith(":root") and a["context"] == ["@layer theme"]
             and "--color-orange" in a["properties"]]
    if len(rules) != 1:
        raise SystemExit(f"expected one marketing :root rule in raw/css-vars.json, found {len(rules)}")
    return rules[0]


MARKETING = _marketing_root()


def resolved(name):
    """A custom property as the marketing sheet declares it: #rgb expanded, rem at the 16px root."""
    v = MARKETING["properties"].get(name)
    if v is None:
        raise SystemExit(f"missing {name} on the marketing :root in raw/css-vars.json")
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3})", v)
    if m:
        return "#" + "".join(c * 2 for c in m.group(1))
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", v)
    if m:
        return "%gpx" % (float(m.group(1)) * 16)
    return v


def measured_style(key, state="default"):
    comp = COMP["components"].get(key) or {}
    st = (comp.get("states") or {}).get(state) or {}
    return st.get("style") or {}


core = {
    "color": {
        "black": color(resolved("--color-black"), f"{S}: --color-black on the marketing sheet; the hero ink measured rgb(14, 14, 14)."),
        "white": color(resolved("--color-white-2"), f"{S}: --color-white-2. Marketing --color-white is #fafafa, kept as offwhite."),
        "offwhite": color(resolved("--color-white"), f"{S}: marketing --color-white"),
        "offblack": color(resolved("--color-offblack"), f"{S}: --color-offblack"),
        "orange": color(resolved("--color-orange"), f"{S}: --color-orange, also --color-accent"),
        "yellow": color(resolved("--color-yellow"), f"{S}: --color-yellow"),
        "amber": color(resolved("--color-amber"), f"{S}: --color-amber"),
        "gray": color(resolved("--color-gray"), f"{S}: --color-gray"),
        "grayDark1": color(resolved("--color-gray-dark-1"), f"{S}: --color-gray-dark-1"),
        "grayDark2": color(resolved("--color-gray-dark-2"), f"{S}: --color-gray-dark-2"),
        "grayDark3": color(resolved("--color-gray-dark-3"), f"{S}: --color-gray-dark-3"),
        "grayLight1": color(resolved("--color-gray-light-1"), f"{S}: --color-gray-light-1"),
        "grayLight2": color(resolved("--color-gray-light-2"), f"{S}: --color-gray-light-2"),
        "grayLight3": color(resolved("--color-gray-light-3"), f"{S}: --color-gray-light-3"),
        "grayBackground": color(resolved("--color-gray-background"), f"{S}: --color-gray-background"),
        "lavender": color(resolved("--color-lavender"), f"{S}: --color-lavender"),
        "purple": color(resolved("--color-purple"), f"{S}: --color-purple"),
        "periwinkle": color(resolved("--color-periwinkle"), f"{S}: --color-periwinkle"),
        "navy": color(resolved("--color-navy"), f"{S}: --color-navy"),
        "lime": color(resolved("--color-lime"), f"{S}: --color-lime"),
        "olive": color(resolved("--color-olive"), f"{S}: --color-olive"),
        "red500": color(resolved("--color-red-500"), f"{S}: --color-red-500 on the marketing sheet. Browsers with lab() support paint the @supports override instead."),
        "green600": color(resolved("--color-green-600"), f"{S}: --color-green-600 on the marketing sheet. Browsers with lab() support paint the @supports override instead."),
    },
    "font": {
        "family": {
            "display": font("recklessStandard, \"recklessStandard Fallback\", ui-serif, Georgia, serif", f"{M}: h1 fontFamily recklessStandard. @font-face in 398ln9hj2tk0d.css, weight 400. Files not shipped."),
            "ui": font("easeStandard, \"easeStandard Fallback\", ui-sans-serif, system-ui, sans-serif", f"{M}: nav and button fontFamily easeStandard. @font-face weight 400. Files not shipped."),
            "mono": font("\"Geist Mono\", \"Geist Mono Fallback\", ui-monospace, monospace", f"{S}: --font-geist-mono on the marketing sheet. Files not shipped."),
            "app": font("Inter, ui-sans-serif, system-ui, sans-serif", "Declared on the app.melius.com and docs.melius.com sheets, 2026-11-19: --font-inter \"Inter\". The fallbacks after Inter are hand-written."),
        },
        "weight": {
            "regular": num(int(resolved("--font-weight-normal")), f"{S}: --font-weight-normal"),
            "medium": num(int(resolved("--font-weight-medium")), f"{S}: --font-weight-medium"),
            "semibold": num(int(resolved("--font-weight-semibold")), f"{S}: --font-weight-semibold"),
            "bold": num(700, "Declared on the app.melius.com and docs.melius.com sheets, 2026-11-19: --font-weight-bold 700. The marketing sheet declares no bold weight."),
        },
        "size": {
            "xs": dim(resolved("--text-xs"), f"{S}: --text-xs"),
            "sm": dim(resolved("--text-sm"), f"{S}: --text-sm"),
            "base": dim(resolved("--text-base"), f"{S}: --text-base"),
            "lg": dim(resolved("--text-lg"), f"{S}: --text-lg"),
            "2xl": dim(resolved("--text-2xl"), f"{S}: --text-2xl"),
            "3xl": dim(resolved("--text-3xl"), f"{S}: --text-3xl"),
            "hero": dim("56px", f"{M}: h1 font-size 56px, line-height 56px, letter-spacing -1.12px"),
        },
    },
    "space": {
        "1": dim(resolved("--spacing"), f"{S}: --spacing, the 4px unit"),
        "2": dim("8px", "Derived: --spacing times 2"),
        "3": dim("12px", "Derived: --spacing times 3"),
        "4": dim("16px", "Derived: --spacing times 4"),
        "6": dim("24px", "Derived: --spacing times 6. Hero CTA padding-inline."),
        "8": dim("32px", "Derived: --spacing times 8"),
        "10": dim("40px", "Derived: --spacing times 10. Nav Sign In height."),
        "12": dim("48px", "Derived: --spacing times 12. Hero CTA height."),
        "14": dim("56px", "Derived: --spacing times 14. Nav bar height."),
    },
    "radius": {
        "xs": dim(resolved("--radius-xs"), f"{S}: --radius-xs"),
        "sm": dim(resolved("--radius-sm"), f"{S}: --radius-sm"),
        "md": dim(resolved("--radius-md"), f"{S}: --radius-md. Nav and hero buttons measure 6px."),
        "lg": dim(resolved("--radius-lg"), f"{S}: --radius-lg"),
        "xl": dim(resolved("--radius-xl"), f"{S}: --radius-xl"),
        "2xl": dim(resolved("--radius-2xl"), f"{S}: --radius-2xl"),
        "3xl": dim(resolved("--radius-3xl"), f"{S}: --radius-3xl"),
    },
    "layout": {
        "page": dim("1440px", "Desktop capture width"),
        "phone": dim("390px", "Phone capture width"),
        "navHeight": dim("56px", f"{M}: nav height 56px"),
        "content": dim(resolved("--container-xl"), f"{S}: --container-xl"),
        "max": dim(resolved("--container-max"), f"{S}: --container-max"),
    },
}

light = {
    "page": color("{color.offwhite}", f"{M}: html background rgb(250, 250, 250), marketing --color-white"),
    "surface": color("{color.white}", f"{M}: Connect your agent button and auth Google button sit on white"),
    "nav": color("{color.grayDark1}", f"{M}: nav background rgb(32, 32, 32), --color-gray-dark-1"),
    "banner": color("{color.yellow}", f"{M}: announcement bar is the yellow token"),
    "text": color("{color.black}", f"{M}: body and h1 color rgb(14, 14, 14)"),
    "textOnDark": color("{color.offwhite}", f"{M}: nav labels rgb(250, 250, 250)"),
    "textMuted": color("{color.gray}", f"{S}: --color-gray, used for secondary copy"),
    "textOnAccent": color("{color.offwhite}", f"{M}: Start for Free label rgb(250, 250, 250)"),
    "accent": color("{color.orange}", f"{M}: Start for Free and Get started for free background rgb(240, 78, 35)"),
    "signIn": color("{color.yellow}", f"{M}: Sign In background rgb(255, 247, 139)"),
    "border": color("{color.grayLight3}", f"{S}: --color-gray-light-3"),
    "focus": color("#476cff", f"{S}: consent --legal-links-focus-color and accordion focus ring. Marketing buttons showed no focus ring at rest."),
    "error": color("{color.red500}", f"{S}: --color-red-500"),
    "success": color("{color.green600}", f"{S}: --color-green-600"),
}


def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)


names = {n for n, _ in walk(core)} | {n for n, _ in walk(light)}

for path, tok in list(walk({"core": core, "light": light})):
    blob = json.dumps(tok["$value"])
    for alias in re.findall(r"\{([^{}]+)\}", blob):
        if alias not in names:
            raise SystemExit(f"{path} alias {{{alias}}} missing")

motion_path = RAW / "motion.json"
if motion_path.exists():
    import motion as motion_mod
    core["motion"], extra = motion_mod.build(json.loads(motion_path.read_text()))
    if extra:
        core["motion"].setdefault("$extensions", {})["notTokenised"] = extra

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only painted theme on captured Melius marketing surfaces, 2026-11-19.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
TEXT = json.dumps(tokens, indent=2) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(TEXT)
    print("tokens", len(names), "motion", motion_path.exists())
