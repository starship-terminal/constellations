#!/usr/bin/env python3
"""Build tokens.json from Uber's public Base stylesheet.

Source: systems/uber/raw/client-main-styles.css, fetched from
https://www.uber.com/_static/client-main-styles-6a69a55fd9196980.css
while https://www.uber.com/us/en/ride/ was open, signed out, on 2026-11-19.

The sheet declares colour primitives on :root (--base-{hue}-{step}), light
semantics under [data-base-version-color="2"], and dark semantics under
[data-base-version-color="2"][data-theme="dark"]. Marketing pages do not set
data-base-version-color, so a live element often does not resolve these
names. This builder resolves var(--base-*) aliases against the primitives in
the same file. A value that is still a var() after that is not tokenised.

Component tokens are computed styles from the signed-out ride page
(raw/pages.json) and the signup wall (raw/auth-wall.json). Nothing was typed
into the wall.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
CSS = (RAW / "client-main-styles.css").read_text()
SRC = "raw/client-main-styles.css (uber.com client-main-styles, 2026-11-19)"

HUES = (
    "amber", "blue", "green", "indigo", "lime", "magenta", "membership",
    "neutral", "orange", "purple", "red", "taupe", "teal", "yellow",
)


def decls_in(text: str) -> dict[str, str]:
    out = {}
    for name, val in re.findall(r"(--base-[a-z0-9-]+)\s*:\s*([^;]+);", text):
        out.setdefault(name, re.sub(r"\s+", " ", val).strip())
    return out


def slice_between(start: str, end: str) -> str:
    i = CSS.find(start)
    if i < 0:
        raise SystemExit(f"missing marker {start}")
    j = CSS.find(end, i + len(start))
    if j < 0:
        j = len(CSS)
    return CSS[i:j]


def primitives() -> dict[str, str]:
    i = CSS.find("--base-amber-0")
    j = CSS.find("/* font families */", i)
    return decls_in(CSS[i:j])


def resolve(val: str, prim: dict[str, str], depth: int = 0) -> str:
    if depth > 8:
        return val

    def repl(match: re.Match) -> str:
        name = match.group(1)
        if name in prim:
            return resolve(prim[name], prim, depth + 1)
        return match.group(0)

    return re.sub(r"var\((--base-[a-z0-9-]+)\)", repl, val)


def color_token(value: str, source: str) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim_token(value: str, source: str) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def nest(path: str, token: dict, root: dict) -> None:
    node = root
    parts = path.split(".")
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = token


def shadow_pair(prefix: str, elev: dict[str, str], source: str) -> dict | None:
    """Two-layer elevation: key then ambient, as the sheet declares them."""
    def get(part: str) -> str | None:
        return elev.get(f"--base-elevation-{prefix}-{part}")

    layers = []
    for kind in ("key", "ambient"):
        color = get(f"{kind}-color")
        blur = get(f"{kind}-blur")
        if not color or not blur:
            return None
        layers.append({
            "offsetX": get(f"{kind}-x") or "0",
            "offsetY": get(f"{kind}-y") or "0",
            "blur": blur if blur.endswith("px") else f"{blur}px",
            "spread": get(f"{kind}-spread") or "0",
            "color": color,
        })
    return {
        "$type": "shadow",
        "$value": layers,
        "$extensions": {"source": source},
    }


def build() -> dict:
    prim = primitives()
    light_text = slice_between("/* v2 light semantics */", "color-scheme: light;")
    dark_text = slice_between("/* v2 dark semantics */", "color-scheme: dark;")
    light = {k: resolve(v, prim) for k, v in decls_in(light_text).items()}
    dark = {k: resolve(v, prim) for k, v in decls_in(dark_text).items()}
    elev_l = decls_in(slice_between("/* v2 light elevation */", "/* v2 dark elevation */"))
    elev_d = decls_in(slice_between("/* v2 dark elevation */", "/* "))

    core: dict = {}
    for hue in HUES:
        for name, val in prim.items():
            m = re.fullmatch(rf"--base-{hue}-(\d+)", name)
            if m and val.startswith("#"):
                nest(f"color.{hue}.{m.group(1)}", color_token(val, SRC + " :root primitive"), core)
    for name, val in prim.items():
        m = re.fullmatch(r"--base-corner-radius-([a-z0-9]+)", name)
        if m:
            nest(f"radius.{m.group(1)}", dim_token(val, SRC + " :root radius"), core)
    type_prim = decls_in(slice_between("/* font families */", "/* typography ramp"))
    prim = {**prim, **type_prim}
    for name, val in prim.items():
        m = re.fullmatch(r"--base-font-size-(\d+)", name)
        if m:
            px = int(m.group(1))
            nest(f"font.size.{m.group(1)}", dim_token(f"{px}px", SRC + " font-size, rem resolved at 16px"), core)
        m = re.fullmatch(r"--base-line-height-(\d+)", name)
        if m:
            # calc(N/16*1rem) or 1rem
            cm = re.fullmatch(r"calc\((\d+)/16\*1rem\)", val)
            px = int(cm.group(1)) if cm else (16 if val == "1rem" else None)
            if px is not None:
                nest(f"font.lineHeight.{m.group(1)}", dim_token(f"{px}px", SRC + " line-height, rem resolved at 16px"), core)
        m = re.fullmatch(r"--base-font-weight-([a-z]+)", name)
        if m:
            nest(f"weight.{m.group(1)}", {"$type": "fontWeight", "$value": val, "$extensions": {"source": SRC}}, core)
        m = re.fullmatch(r"--base-font-family-([a-z]+)", name)
        if m:
            nest(f"family.{m.group(1)}", {"$type": "fontFamily", "$value": val, "$extensions": {"source": SRC}}, core)

    # Type roles measured on the ride page, plus the sheet's display/body stacks.
    type_src = "computed on https://www.uber.com/us/en/ride/ signed out, 1440x900, 2026-11-19"
    nest("typography.display", {
        "$type": "typography",
        "$value": {
            "fontFamily": "{family.display}",
            "fontSize": "52px",
            "fontWeight": "700",
            "lineHeight": "64px",
            "letterSpacing": "0",
        },
        "$extensions": {"source": type_src + " h1 Request a ride"},
    }, core)
    nest("typography.heading", {
        "$type": "typography",
        "$value": {
            "fontFamily": "{family.display}",
            "fontSize": "36px",
            "fontWeight": "700",
            "lineHeight": "44px",
            "letterSpacing": "0",
        },
        "$extensions": {"source": type_src + " h2"},
    }, core)
    nest("typography.nav", {
        "$type": "typography",
        "$value": {
            "fontFamily": "{family.body}",
            "fontSize": "14px",
            "fontWeight": "500",
            "lineHeight": "16px",
            "letterSpacing": "0",
        },
        "$extensions": {"source": type_src + " header pill"},
    }, core)
    nest("typography.body", {
        "$type": "typography",
        "$value": {
            "fontFamily": "{family.body}",
            "fontSize": "16px",
            "fontWeight": "400",
            "lineHeight": "24px",
            "letterSpacing": "0",
        },
        "$extensions": {"source": type_src + " body copy"},
    }, core)
    nest("typography.label", {
        "$type": "typography",
        "$value": {
            "fontFamily": "{family.body}",
            "fontSize": "14px",
            "fontWeight": "400",
            "lineHeight": "20px",
            "letterSpacing": "0",
        },
        "$extensions": {"source": type_src + " field label"},
    }, core)

    for theme, mapping, elev in (("light", light, elev_l), ("dark", dark, elev_d)):
        group: dict = {}
        skipped = []
        for name, val in mapping.items():
            path = name.removeprefix("--base-").replace("-", ".")
            if "var(" in val or val.startswith("linear-gradient"):
                skipped.append({"name": name, "value": val})
                continue
            if not (val.startswith("#") or val.startswith("rgb")):
                skipped.append({"name": name, "value": val})
                continue
            nest(path, color_token(val, f"{SRC} v2 {theme} semantics, alias resolved"), group)
        for level in ("lowest", "low", "mid", "high", "highest"):
            token = shadow_pair(level, elev, f"{SRC} v2 {theme} elevation")
            if token:
                nest(f"elevation.{level}", token, group)
        if skipped:
            group.setdefault("$extensions", {})["notTokenised"] = skipped
        # component roles from the live marketing chrome (light only measured)
        if theme == "light":
            nest("component.button.primary.bg", color_token("#111111", type_src + " See prices"), group)
            nest("component.button.primary.text", color_token("#fcfcfc", type_src + " See prices"), group)
            nest("component.button.primary.radius", dim_token("8px", type_src + " See prices"), group)
            nest("component.button.primary.height", dim_token("48px", type_src + " See prices"), group)
            nest("component.button.nav.bg", color_token("#111111", type_src + " header pill"), group)
            nest("component.button.nav.text", color_token("#fcfcfc", type_src + " header pill"), group)
            nest("component.button.nav.radius", dim_token("999px", type_src + " header pill"), group)
            nest("component.button.nav.height", dim_token("36px", type_src + " header pill"), group)
            nest("component.button.signup.bg", color_token("#ffffff", type_src + " Sign up pill"), group)
            nest("component.button.signup.text", color_token("#000000", type_src + " Sign up pill"), group)
            nest("component.button.signup.radius", dim_token("999px", type_src + " Sign up pill"), group)
            nest("component.field.bg", color_token("#f6f6f6", type_src + " pickup field box"), group)
            nest("component.field.radius", dim_token("8px", type_src + " pickup field box"), group)
            nest("component.field.height", dim_token("56px", type_src + " pickup field box"), group)
            nest("component.header.bg", color_token("#000000", type_src + " header"), group)
            nest("component.header.height", dim_token("64px", type_src + " header"), group)
            nest("component.banner.bg", color_token("#eff4fe", type_src + " signup promo banner"), group)
        core_out = core
        if theme == "light":
            light_set = group
        else:
            dark_set = group

    return {
        "core": core_out,
        "light": light_set,
        "dark": dark_set,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }


def main() -> None:
    tokens = build()
    text = json.dumps(tokens, indent=2) + "\n"
    (HERE / "tokens.json").write_text(text)
    light_n = sum(1 for _ in walk(tokens["light"]))
    dark_n = sum(1 for _ in walk(tokens["dark"]))
    core_n = sum(1 for _ in walk(tokens["core"]))
    print(f"wrote tokens.json core={core_n} light={light_n} dark={dark_n}")


def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v)


if __name__ == "__main__":
    main()
