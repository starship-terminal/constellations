#!/usr/bin/env python3
"""Build tokens.json from the Mercury public capture.

Mercury marketing declares a named colour system on :root (neutral, purple,
beige, green, blue, orange, red) and restyles the semantic roles under
theme classes. The home hero paints dark-neutral-theme. The light roles are
:root / .neutral-theme. tools/capture measured both by resolving each custom
property on a probe. Component colours that are not a token (the login card,
the demo chrome) stay out of the ramps and are recorded only when a computed
style measured them.

Nothing here is sampled from a screenshot.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))

VARS = json.loads((RAW / "css-vars.json").read_text())
LIGHT = VARS.get("root") or VARS["resolved"]["light"]
if "dark-neutral-theme" not in VARS:
    # Falling back to the light map would publish light values as the dark set.
    raise SystemExit("raw/css-vars.json has no dark-neutral-theme readings")
DARK = VARS["dark-neutral-theme"]
S = "Resolved from mercury.com stylesheets, 2026-11-19, custom properties computed on a probe"
M = "Measured computed style, public Mercury pages, 2026-11-19"


def color(value, source):
    # DTCG colours are six- or eight-digit hex; a declared "#fff" is written out in full.
    if re.fullmatch(r"#[0-9a-fA-F]{3}", value):
        value = "#" + "".join(c * 2 for c in value[1:])
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def cubic(value, source):
    # DTCG cubicBezier is four numbers, not the CSS function text the stylesheet declares.
    m = re.fullmatch(r"\s*cubic-bezier\(([^)]*)\)\s*", value or "")
    if not m:
        raise SystemExit(f"not a cubic-bezier(): {value!r}")
    points = [float(x) for x in m.group(1).split(",")]
    if len(points) != 4:
        raise SystemExit(f"cubic-bezier() needs four numbers: {value!r}")
    return {"$value": [int(x) if x == int(x) else x for x in points], "$type": "cubicBezier",
            "$extensions": {"source": source}}


def raw(name, bag=LIGHT):
    node = bag.get(name)
    if node is None:
        raise SystemExit(f"missing {name}")
    if isinstance(node, dict):
        return node.get("value") or node.get("raw")
    return node


def hex_ok(value):
    return bool(re.fullmatch(r"#[0-9a-fA-F]{3,8}", value or ""))


def ramp(prefix):
    out = {}
    for key, value in LIGHT.items():
        if not key.startswith(prefix) or "alpha" in key:
            continue
        step = key[len(prefix):]
        if not step.isdigit():
            continue
        if isinstance(value, dict):
            value = value.get("value") or value.get("raw")
        if not hex_ok(value):
            continue
        out[step] = color(value.lower(), f"{S}: {key}")
    if not out:
        raise SystemExit(f"no ramp for {prefix}")
    return dict(sorted(out.items(), key=lambda kv: int(kv[0])))


def rem(name):
    value = raw(name)
    if value.endswith("rem"):
        px = round(float(value[:-3]) * 16, 2)
        text = str(int(px)) if px == int(px) else str(px).rstrip("0").rstrip(".")
        return f"{text}px"
    if value.endswith("em"):
        return value
    return value


core = {
    "color": {
        "neutral": ramp("--color-neutral-base-"),
        "purple": ramp("--color-purple-base-"),
        "beige": ramp("--color-beige-base-"),
        "green": ramp("--color-green-base-"),
        "blue": ramp("--color-blue-base-"),
        "orange": ramp("--color-orange-base-"),
        "red": {
            "50": color(raw("--color-red-base-50").lower(), f"{S}: --color-red-base-50"),
            "500": color(raw("--color-red-base-500").lower(), f"{S}: --color-red-base-500"),
        },
        "magic": {
            "purple": color(raw("--color-purple-magic-600").lower(), f"{S}: --color-purple-magic-600, the primary fill"),
            "purpleHover": color(raw("--color-purple-magic-700").lower(), f"{S}: --color-purple-magic-700"),
            "purpleActive": color(raw("--color-purple-magic-800").lower(), f"{S}: --color-purple-magic-800"),
            "purpleSoft": color(raw("--color-purple-magic-400").lower(), f"{S}: --color-purple-magic-400, the dark-theme primary"),
            "green": color(raw("--color-green-magic-600").lower(), f"{S}: --color-green-magic-600"),
            "red": color(raw("--color-red-magic-600").lower(), f"{S}: --color-red-magic-600"),
            "redSoft": color(raw("--color-red-magic-400").lower(), f"{S}: --color-red-magic-400"),
            "orange": color(raw("--color-orange-magic-600").lower(), f"{S}: --color-orange-magic-600"),
            "blue": color(raw("--color-blue-magic-600").lower(), f"{S}: --color-blue-magic-600"),
        },
        "avatar": {
            "blue": color(raw("--color-avatar-blue").lower(), f"{S}: --color-avatar-blue"),
            "green": color(raw("--color-avatar-green").lower(), f"{S}: --color-avatar-green"),
            "purple": color(raw("--color-avatar-purple").lower(), f"{S}: --color-avatar-purple"),
            "yellow": color(raw("--color-avatar-yellow").lower(), f"{S}: --color-avatar-yellow"),
        },
        "white": color("#ffffff", f"{S}: --color-neutral-base-0"),
        "ink": color(raw("--color-neutral-base-950").lower(), f"{S}: --color-neutral-base-950, also the theme-color meta"),
    },
    "font": {
        "family": {
            "sans": font("arcadia, Arial, sans-serif", f"{S}: --font-arcadia is arcadia, arcadia Fallback. Fallback face is local Arial. Files are not shipped."),
            "display": font("arcadiaDisplay, Arial, sans-serif", f"{S}: --font-arcadia-display. Variable weight 320 to 480."),
            "serif": font("tiemposHeadline, Georgia, serif", f"{S}: --font-tiempos-headline, weight 400."),
            "mono": font("IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, monospace", f"{S}: --font-ibm-plex-mono. --font-mono is the generic ui-monospace stack."),
        },
        "weight": {
            "light": num(360, f"{S}: --font-weight-360, the light text step"),
            "regular": num(400, f"{S}: --font-weight-400"),
            "book": num(420, f"{S}: --font-weight-420, nav and button labels"),
            "medium": num(480, f"{S}: --font-weight-480, display"),
            "strong": num(530, f"{S}: --font-weight-medium"),
        },
        "size": {
            "xxs": dim(rem("--text-xxs"), f"{S}: --text-xxs"),
            "xs": dim(rem("--text-xs"), f"{S}: --text-xs"),
            "sm": dim(rem("--text-sm"), f"{S}: --text-sm"),
            "base": dim(rem("--text-base"), f"{S}: --text-base"),
            "md": dim(rem("--text-md"), f"{S}: --text-md"),
            "lg": dim(rem("--text-lg"), f"{S}: --text-lg"),
            "xl": dim(rem("--text-xl"), f"{S}: --text-xl"),
            "2xl": dim(rem("--text-2xl"), f"{S}: --text-2xl"),
            "3xl": dim(rem("--text-3xl"), f"{S}: --text-3xl"),
            "4xl": dim(rem("--text-4xl"), f"{S}: --text-4xl"),
            "5xl": dim(rem("--text-5xl"), f"{S}: --text-5xl"),
            "6xl": dim(rem("--text-6xl"), f"{S}: --text-6xl"),
            "7xl": dim(rem("--text-7xl"), f"{S}: --text-7xl"),
        },
        "leading": {
            "tight": num(1.25, f"{S}: --leading-tight"),
            "normal": num(1.5, f"{S}: --leading-normal"),
        },
    },
    "space": {
        "0": dim("0px", f"{S}: --spacing-0"),
        "1": dim("4px", f"{S}: --spacing-4. The declared --spacing unit is 1px; the scale steps by 4."),
        "2": dim("8px", f"{S}: --spacing-8"),
        "3": dim("12px", f"{S}: --spacing-12"),
        "4": dim("16px", f"{S}: --spacing-16"),
        "5": dim("20px", f"{S}: --spacing-20"),
        "6": dim("24px", f"{S}: --spacing-24"),
        "8": dim("32px", f"{S}: --spacing-32"),
        "10": dim("40px", f"{S}: --spacing-40"),
        "12": dim("48px", f"{S}: --spacing-48"),
        "14": dim("56px", f"{S}: --spacing-56"),
        "16": dim("64px", f"{S}: --spacing-64"),
        "18": dim("72px", f"{S}: --spacing-72, the navbar height"),
        "20": dim("80px", f"{S}: --spacing-80"),
        "24": dim("96px", f"{S}: --spacing-96"),
    },
    "radius": {
        "sm": dim("4px", f"{S}: --radius-sm is 0.25rem"),
        "md": dim("6px", f"{S}: --radius-md is 0.375rem"),
        "lg": dim("8px", f"{S}: --radius-lg is 0.5rem"),
        "xl": dim("12px", f"{S}: --radius-xl is 0.75rem"),
        "2xl": dim("16px", f"{S}: --radius-2xl is 1rem"),
        "3xl": dim("24px", f"{S}: --radius-3xl is 1.5rem"),
        "4xl": dim("32px", f"{S}: --radius-4xl is 2rem"),
        "5xl": dim("40px", f"{S}: --radius-5xl is 2.5rem"),
        "pill": dim("40px", f"{M}: Log in and Launch demo paint border-radius 40px on a 32px control"),
    },
    "layout": {
        "page": dim("1440px", "Desktop capture width"),
        "phone": dim("390px", "Phone capture width"),
        "navHeight": dim(raw("--navbar-height"), f"{S}: --navbar-height"),
        "navBanner": dim(raw("--navbar-banner-height"), f"{S}: --navbar-banner-height"),
        "content": dim("1440px", f"{M}: the desktop capture is 1440 wide. The marketing grid class is max-w-grid-max-width; that custom property did not resolve on the probe."),
        "columns": num(16, f"{M}: the home hero grid class is grid-cols-layout. --grid-total-columns was not on the probe."),
        "gutter": dim("32px", f"{M}: nav padding is 16px 32px. --grid-gutters was not on the probe."),
        "margin": dim("32px", f"{M}: the nav horizontal padding"),
        "zNav": num(99, f"{S}: --navbar-z-index"),
    },
    "ease": {
        "in": cubic(raw("--ease-in"), f"{S}: --ease-in"),
        "out": cubic(raw("--ease-out"), f"{S}: --ease-out"),
        "inOut": cubic(raw("--ease-in-out"), f"{S}: --ease-in-out"),
        "inOutCubic": cubic(raw("--ease-in-out-cubic"), f"{S}: --ease-in-out-cubic"),
    },
}


def role(name, bag, note):
    return color(raw(name, bag).lower(), note)


def semantic(bag, label):
    note = f"{S}: {label}"
    return {
        "page": role("--background-default", bag, f"{note}: --background-default"),
        "pageSecondary": role("--background-secondary", bag, f"{note}: --background-secondary"),
        "surface": role("--surface-default", bag, f"{note}: --surface-default"),
        "surfaceHover": role("--surface-default-hover", bag, f"{note}: --surface-default-hover"),
        "surfaceActive": role("--surface-default-active", bag, f"{note}: --surface-default-active"),
        "raised": role("--surface-elevated", bag, f"{note}: --surface-elevated"),
        "raisedHover": role("--surface-elevated-hover", bag, f"{note}: --surface-elevated-hover"),
        "input": role("--surface-input", bag, f"{note}: --surface-input"),
        "inverted": role("--surface-inverted", bag, f"{note}: --surface-inverted"),
        "scrim": color("#10101acc", f"{note}: reconstructed from --color-neutral-base-1000 at 80% for the menu overlay. The live menu was measured separately."),
        "text": role("--text-default", bag, f"{note}: --text-default"),
        "textEmphasis": role("--text-emphasized", bag, f"{note}: --text-emphasized"),
        "muted": role("--text-subdued", bag, f"{note}: --text-subdued"),
        "disabled": role("--text-disabled", bag, f"{note}: --text-disabled"),
        "textOnAccent": role("--text-on-primary", bag, f"{note}: --text-on-primary"),
        "link": role("--text-primary", bag, f"{note}: --text-primary"),
        "accent": role("--surface-primary", bag, f"{note}: --surface-primary"),
        "accentHover": role("--surface-primary-hover", bag, f"{note}: --surface-primary-hover"),
        "accentActive": role("--surface-primary-active", bag, f"{note}: --surface-primary-active"),
        "accentDisabled": role("--surface-primary-disabled", bag, f"{note}: --surface-primary-disabled"),
        "focus": role("--border-focus", bag, f"{note}: --border-focus"),
        "border": role("--border-subdued", bag, f"{note}: --border-subdued"),
        "borderStrong": role("--border-emphasized", bag, f"{note}: --border-emphasized"),
        "borderInput": role("--border-input", bag, f"{note}: --border-input"),
        "error": role("--text-error", bag, f"{note}: --text-error"),
        "errorBorder": role("--border-error", bag, f"{note}: --border-error"),
        "success": color(raw("--color-green-magic-600").lower(), f"{note}: --color-green-magic-600. No --text-success role is declared."),
        "warning": color(raw("--color-orange-magic-600").lower(), f"{note}: --color-orange-magic-600. No --text-warning role is declared."),
        "info": color(raw("--color-blue-magic-600").lower(), f"{note}: --color-blue-magic-600. No --text-info role is declared."),
        "magic": role("--surface-magic", bag, f"{note}: --surface-magic"),
        "magicHover": role("--surface-magic-hover", bag, f"{note}: --surface-magic-hover"),
        "magicActive": role("--surface-magic-active", bag, f"{note}: --surface-magic-active"),
    }


light = semantic(LIGHT, "light on :root / .neutral-theme")
dark = semantic(DARK, "dark on .dark-neutral-theme")



def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)


names = {n for n, _ in walk(core)} | {n for n, _ in walk(light)} | {n for n, _ in walk(dark)}


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


for path, tok in list(walk({"core": core, "light": light, "dark": dark})):
    if "$extensions" not in tok:
        raise SystemExit(f"{path} has no source")
    for blob in strings(tok["$value"]):
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
    "dark": dark,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The :root / .neutral-theme roles. Marketing pages below the hero paint these.",
        },
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "The .dark-neutral-theme roles. The home hero and the dark marketing bands paint these.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("tokens", len(names), "motion", motion_path.exists())
