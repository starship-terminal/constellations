#!/usr/bin/env python3
"""Build tokens.json from the Maze public capture.

Maze marketing declares a named oklch palette on :root (Tailwind v4 custom
properties). tools/capture/vars.mjs resolved those to sRGB. Auth and the
public report paint Inter and a blue action as literals; those colours are
recorded only when a computed style measured them. One painted theme. There
is no dark set.
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

S = "Resolved from maze.co :root custom properties, 2026-11-18 (oklch converted to sRGB by tools/capture/vars.mjs)"
M = "Measured computed style, public Maze pages, 2026-11-18, light, 1440"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def resolved(name):
    node = LIGHT.get(name)
    if not node:
        raise SystemExit(f"missing {name} in raw/css-vars.json")
    return node.get("value") or node.get("raw")


def ramp(prefix):
    out = {}
    for key, node in LIGHT.items():
        m = re.fullmatch(re.escape(prefix) + r"([0-9]+)", key)
        if not m or node.get("kind") != "color":
            continue
        out[m.group(1)] = color(node["value"], f"{S}: {key} was {node.get('raw')}")
    if not out:
        raise SystemExit(f"no ramp for {prefix}")
    return dict(sorted(out.items(), key=lambda kv: int(kv[0])))


def measured_bg(key, state="default"):
    comp = COMP["components"].get(key) or {}
    st = (comp.get("states") or {}).get(state) or {}
    style = st.get("style") or {}
    return style.get("backgroundColor"), style.get("color"), style.get("fontFamily"), style.get("fontSize"), style.get("borderTopLeftRadius")


core = {
    "color": {
        "neutral": ramp("--color-neutral-"),
        "blue": ramp("--color-blue-"),
        "lime": ramp("--color-lime-"),
        "cyan": ramp("--color-cyan-"),
        "purple": ramp("--color-purple-"),
        "red": ramp("--color-red-"),
        "yellow": ramp("--color-yellow-"),
        "white": color(resolved("--color-neutral-000"), f"{S}: --color-white aliases --color-neutral-000"),
        "error": color(resolved("--color-red-500"), f"{S}: --color-error aliases --color-red-500"),
        "success": color(resolved("--color-cyan-600"), f"{S}: --color-success aliases --color-cyan-600"),
    },
    "font": {
        "family": {
            "display": font("Phonic, sans-serif", f"{S}: --font-phonic, weights 300 400 500 700 in phonic.css"),
            "sans": font("Inter, ui-sans-serif, system-ui, sans-serif", f"{M}: auth.maze.co and the public report paint Inter"),
            "mono": font(resolved("--font-mono"), f"{S}: --font-mono"),
        },
        "weight": {
            "light": num(300, f"{S}: --font-weight-light"),
            "regular": num(400, f"{S}: --font-weight-normal"),
            "medium": num(500, f"{S}: --font-weight-medium"),
            "semibold": num(600, f"{S}: --font-weight-semibold"),
            "bold": num(700, f"{S}: --font-weight-bold"),
        },
        "size": {
            "sm": dim(resolved("--text-sm"), f"{S}: --text-sm"),
            "base": dim(resolved("--text-base"), f"{S}: --text-base"),
            "lg": dim(resolved("--text-lg"), f"{S}: --text-lg"),
            "xl": dim(resolved("--text-xl"), f"{S}: --text-xl"),
            "2xl": dim(resolved("--text-2xl"), f"{S}: --text-2xl"),
            "3xl": dim(resolved("--text-3xl"), f"{S}: --text-3xl"),
            "4xl": dim(resolved("--text-4xl"), f"{S}: --text-4xl"),
            "7xl": dim(resolved("--text-7xl"), f"{S}: --text-7xl"),
        },
    },
    "space": {
        "1": dim(resolved("--spacing"), f"{S}: --spacing, the 4px unit"),
        "2": dim("8px", "Derived: --spacing times 2"),
        "3": dim("12px", "Derived: --spacing times 3"),
        "4": dim("16px", "Derived: --spacing times 4"),
        "6": dim("24px", "Derived: --spacing times 6"),
        "8": dim("32px", "Derived: --spacing times 8"),
        "10": dim("40px", "Derived: --spacing times 10, the header control height"),
        "12": dim("48px", "Derived: --spacing times 12, the login field height"),
    },
    "radius": {
        "xs": dim(resolved("--radius-xs"), f"{S}: --radius-xs"),
        "sm": dim(resolved("--radius-sm"), f"{S}: --radius-sm"),
        "md": dim(resolved("--radius-md"), f"{S}: --radius-md"),
        "lg": dim(resolved("--radius-lg"), f"{S}: --radius-lg"),
        "xl": dim(resolved("--radius-xl"), f"{S}: --radius-xl"),
        "2xl": dim(resolved("--radius-2xl"), f"{S}: --radius-2xl"),
        "3xl": dim(resolved("--radius-3xl"), f"{S}: --radius-3xl"),
        "pill": dim("9999px", f"{M}: Try Maze for free is a pill"),
    },
    "layout": {
        "page": dim("1440px", "Desktop capture width"),
        "phone": dim("390px", "Phone capture width"),
        "navHeight": dim(resolved("--nav-height"), f"{S}: --nav-height. The painted header measured about 81px under the promo bar."),
        "content": dim(resolved("--container-6xl"), f"{S}: --container-6xl"),
        "prose": dim(resolved("--container-4xl"), f"{S}: --container-4xl"),
    },
}

login_bg, login_fg, login_font, login_size, login_radius = measured_bg("login-submit")
# The action colour is the measured Log in fill; a missing or translucent reading fails the build
# instead of falling back to a typed literal under the same Measured source.
_m = re.fullmatch(r"rgba?\(\s*(\d+),\s*(\d+),\s*(\d+)\s*(?:,\s*1\s*)?\)", login_bg or "")
if not _m:
    raise SystemExit(f"login-submit backgroundColor is not an opaque rgb() reading: {login_bg!r}")
core["color"]["action"] = color("#%02x%02x%02x" % tuple(int(x) for x in _m.groups()), f"{M}: Log in submit backgroundColor {login_bg}")

light = {
    "page": color("{color.neutral.100}", f"{S}: marketing ground is the warm neutral 100"),
    "surface": color("{color.white}", f"{S}: cards and the auth form sit on white"),
    "text": color("{color.neutral.700}", f"{M}: hero ink is oklch(0.226 0 0), the painted step nearest neutral 700"),
    "textBody": color("{color.neutral.500}", f"{S}: secondary copy"),
    "textMuted": color("{color.neutral.400}", f"{S}: captions"),
    "textOnAccent": color("{color.white}", f"{M}: filled button labels"),
    "accent": color("{color.neutral.700}", f"{M}: Get a demo fill is oklch(0.226 0 0), nearest neutral 700"),
    "accentHover": color("{color.neutral.600}", f"{M}: Get a demo hover fill is oklch(0.356 0 0), nearest neutral 600"),
    "link": color("{color.action}", f"{M}: auth links and the report Sign up for free"),
    "action": color("{color.action}", f"{M}: Log in submit"),
    "focus": color("{color.blue.500}", f"{S}: blue 500 is the declared focus-adjacent step"),
    "border": color("{color.neutral.200}", f"{S}: hairline"),
    "error": color("{color.error}", f"{S}: --color-error"),
    "success": color("{color.success}", f"{S}: --color-success"),
    "lime": color("{color.lime.400}", f"{S}: the lime collage on pricing and auth"),
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


def alias_ok(alias):
    return alias in names or ("color." + alias) in names or alias.startswith("color.") and alias in names


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


for path, tok in walk({"core": core, "light": light}):
    for blob in strings(tok["$value"]):
        for alias in re.findall(r"\{([^{}]+)\}", blob):
            if alias not in names and not (alias.startswith("color.") and alias in names):
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
        "$description": "The only painted theme on captured Maze surfaces, 2026-11-18.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("tokens", len(names), "motion", motion_path.exists())
