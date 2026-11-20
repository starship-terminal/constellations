#!/usr/bin/env python3
"""Build systems/rox/tokens.json from raw/readings.json.

Every colour, length and type role in the readings was measured on
https://www.rox.com/ and the signed-out Auth0 login on 2026-11-19, in the
T3 preview browser (computed style) with viewport screenshots from headless
Playwright after that browser stopped producing frames. A value that was not
on the page is absent here. See raw/gaps.md.

The mapping below is the only product-specific part. check() is the contract
tools/test_build_tokens.py runs.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw" / "readings.json"
OUT = HERE / "tokens.json"

ALIAS = re.compile(r"^\{([A-Za-z0-9_.-]+)\}$")


class CheckError(AssertionError):
    """A token file check() refuses. Raised as AssertionError so the kit tests,
    which catch AssertionError, still see it. python -O strips assert, so the
    checks are if-raises, not assert statements."""


def check(doc: dict) -> None:
    """Refuse a token file whose aliases point nowhere, whose themes disagree,
    or whose tokens carry no source."""
    if not isinstance(doc, dict) or "core" not in doc:
        raise CheckError("tokens.json needs a core set")

    def walk(node, path, found):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            found[path] = node
            if "$extensions" not in node or "source" not in node.get("$extensions", {}):
                raise CheckError(f"{path or 'root'} has no source")
            return
        for key, child in node.items():
            if key.startswith("$"):
                continue
            walk(child, f"{path}.{key}" if path else key, found)

    found: dict[str, dict] = {}
    for set_name, body in doc.items():
        if set_name.startswith("$") or not isinstance(body, dict):
            continue
        # Prefix with the set name so light.text.primary and auth.text.primary
        # stay distinct. An alias written as {font.display} still resolves,
        # because resolve() also tries core/light/auth prefixes.
        walk(body, set_name, found)

    def resolve(value, trail):
        if not isinstance(value, str):
            return
        match = ALIAS.fullmatch(value.strip())
        if not match:
            return
        target = match.group(1)
        if target in trail:
            raise CheckError(f"alias cycle at {target}")
        # The alias may name a token in any set. Tokens Studio writes
        # {fontWeight.regular} against the same set; this package also uses
        # cross-set names like {core.color.ink}.
        candidates = [target]
        if not target.startswith("core.") and not target.startswith("light.") and not target.startswith("auth."):
            candidates += [f"core.{target}", f"light.{target}", f"auth.{target}"]
        hit = next((c for c in candidates if c in found), None)
        if hit is None:
            raise CheckError(f"alias {{{target}}} points at nothing")
        resolve(found[hit].get("$value"), trail + (target,))

    for path, token in found.items():
        value = token.get("$value")
        if isinstance(value, dict):
            for part in value.values():
                resolve(part, (path,))
        else:
            resolve(value, (path,))

    themes = [name for name in ("light", "dark") if name in doc]
    if len(themes) == 2:
        def keys(node, prefix=""):
            out = set()
            for key, child in node.items():
                if key.startswith("$"):
                    continue
                path = f"{prefix}.{key}" if prefix else key
                if isinstance(child, dict) and "$value" in child:
                    out.add(path)
                elif isinstance(child, dict):
                    out |= keys(child, path)
            return out
        light_keys, dark_keys = keys(doc["light"]), keys(doc["dark"])
        if light_keys != dark_keys:
            raise CheckError(f"theme keys differ: {sorted(light_keys ^ dark_keys)[:8]}")


def tok(type_, value, source):
    return {"$type": type_, "$value": value, "$extensions": {"source": source}}


def color(value, source):
    return tok("color", value, source)


def dim(value, source):
    return tok("dimension", value, source)


SRC_HOME = "computed style on https://www.rox.com/ at 1440x900, 2026-11-19 (T3 preview)"
SRC_PRICE = "computed style on https://www.rox.com/pricing at 1440x900, 2026-11-19"
SRC_CONTACT = "computed style on https://www.rox.com/contact at 1440x900, 2026-11-19"
SRC_AUTH = "computed style on roxai.us.auth0.com/u/login/identifier, signed out, 2026-11-19"
SRC_TOKEN = "Framer --token-* custom property resolved on body at https://www.rox.com/"


def build(readings: dict | None = None) -> dict:
    """Map the measured readings to core, light and auth sets.

    readings is accepted so a rebuild can pass the file explicitly. The
    mapping uses the values recorded in this function, which were copied
    from raw/readings.json; the file is the evidence, not a second source.
    """
    if readings is None and RAW.exists():
        readings = json.loads(RAW.read_text())
    if readings is not None and readings.get("host") not in (None, "www.rox.com"):
        raise CheckError(f"readings host is {readings.get('host')}, expected www.rox.com")

    stone = {
        "50": "#fafaf9",
        "100": "#f5f5f4",
        "200": "#e7e5e4",
        "300": "#d6d3d1",
        "400": "#a6a09b",
        "500": "#87827d",
        "600": "#57534d",
        "700": "#44403b",
        "800": "#292524",
        "900": "#1c1917",
        "950": "#0c0a09",
    }
    core_color = {}
    for step, value in stone.items():
        core_color[f"stone-{step}"] = color(value, f"{SRC_TOKEN}; stone-{step}")
    core_color["page"] = color("#f7f6f4", f"{SRC_HOME}; document.body background-color rgb(247, 246, 244)")
    core_color["ink"] = color("#0c0a09", f"{SRC_HOME}; hero heading color rgb(12, 10, 9)")
    core_color["ink-soft"] = color("#1c1917", f"{SRC_PRICE}; price heading color rgb(28, 25, 23)")
    core_color["white"] = color("#ffffff", f"{SRC_TOKEN}; --token white")
    core_color["paper"] = color("#fafafa", f"{SRC_HOME}; nav Start now background rgb(250, 250, 250)")
    core_color["field"] = color("#f4f4f3", f"{SRC_CONTACT}; .framer-form-text-input background rgb(244, 244, 243)")
    # No file in raw/ holds these four: raw/readings.json keeps no --token-* resolution for them.
    # They were typed in from the capture session (docs/EVIDENCE.md, Reconstruction).
    hand = "Reconstruction: entered by hand at capture time; no file in raw/ holds this reading. Capture note: " + SRC_TOKEN
    core_color["blue"] = color("#0b63e8", f"{hand}; accent token, not painted on a measured control")
    core_color["green"] = color("#22c55e", f"{hand}; status token, not painted on a measured control")
    core_color["red"] = color("#e5484d", f"{hand}; status token, not painted on a measured control")
    core_color["orange"] = color("#f9700a", f"{hand}; status token, not painted on a measured control")
    core_color["nav-muted"] = color("#fafafacc", f"{SRC_HOME}; nav link color rgba(250, 250, 250, 0.8)")
    core_color["action-dark"] = color("#403f3e", f"{SRC_PRICE}; Start for free background rgb(64, 63, 62)")
    core_color["action-muted"] = color("#828282", f"{SRC_PRICE}; dimmed plan button background rgb(130, 130, 130)")

    font = {
        "display": tok("fontFamily", "Season Mix, sans-serif", f"{SRC_HOME}; computed font-family starts 'Season Mix-TRIAL Regular'. Trial face, not committed."),
        "sans": tok("fontFamily", "Geist, sans-serif", f"{SRC_HOME}; computed font-family Geist on nav and buttons"),
        "system": tok("fontFamily", "system-ui, sans-serif", f"{SRC_HOME}; announcement and some body copy compute to system-ui"),
        "auth": tok("fontFamily", "ulp-font, -apple-system, system-ui, Roboto, Helvetica, sans-serif", f"{SRC_AUTH}; body font-family"),
    }
    weight = {
        "regular": tok("fontWeight", 400, f"{SRC_HOME}; body copy"),
        "book": tok("fontWeight", 420, f"{SRC_HOME}; Season Mix display headings compute to 420"),
        "medium": tok("fontWeight", 500, f"{SRC_HOME}; Geist nav and button labels"),
    }
    typography = {
        "display": tok("typography", {
            "fontFamily": "{font.display}",
            "fontSize": "56px",
            "fontWeight": "{fontWeight.book}",
            "lineHeight": "67.2px",
            "letterSpacing": "-1.12px",
        }, f"{SRC_HOME}; hero 'The Revenue Agent'"),
        "title": tok("typography", {
            "fontFamily": "{font.display}",
            "fontSize": "42px",
            "fontWeight": "{fontWeight.book}",
            "lineHeight": "50.4px",
            "letterSpacing": "-0.84px",
        }, f"{SRC_PRICE}; 'Start free.' and {SRC_CONTACT}; 'Get in touch.'"),
        "heading": tok("typography", {
            "fontFamily": "{font.display}",
            "fontSize": "30px",
            "fontWeight": "{fontWeight.book}",
            "lineHeight": "36px",
            "letterSpacing": "-0.6px",
        }, f"{SRC_HOME}; section heading 'Automate the entire revenue cycle'"),
        "quote": tok("typography", {
            "fontFamily": "{font.display}",
            "fontSize": "18px",
            "fontWeight": "{fontWeight.book}",
            "lineHeight": "23.4px",
            "letterSpacing": "0px",
        }, f"{SRC_HOME}; hero quote"),
        "nav": tok("typography", {
            "fontFamily": "{font.sans}",
            "fontSize": "14px",
            "fontWeight": "{fontWeight.medium}",
            "lineHeight": "14px",
            "letterSpacing": "0px",
        }, f"{SRC_HOME}; nav link 'Pricing'"),
        "button": tok("typography", {
            "fontFamily": "{font.sans}",
            "fontSize": "16px",
            "fontWeight": "{fontWeight.medium}",
            "lineHeight": "16px",
            "letterSpacing": "0px",
        }, f"{SRC_CONTACT}; submit label 'Get in touch'"),
        "body": tok("typography", {
            "fontFamily": "{font.system}",
            "fontSize": "16px",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "22.4px",
            "letterSpacing": "0px",
        }, f"{SRC_HOME}; section paragraph, system-ui 16/22.4"),
        "body-sans": tok("typography", {
            "fontFamily": "{font.sans}",
            "fontSize": "18px",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "25.2px",
            "letterSpacing": "0px",
        }, f"{SRC_HOME}; Geist 18/25.2 paragraph"),
        "field": tok("typography", {
            "fontFamily": "{font.sans}",
            "fontSize": "14px",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "17px",
            "letterSpacing": "0px",
        }, f"{SRC_CONTACT}; input font-size 14px, placeholder rgb(166, 160, 155)"),
        "announcement": tok("typography", {
            "fontFamily": "{font.system}",
            "fontSize": "14px",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "19.6px",
            "letterSpacing": "0px",
        }, f"{SRC_HOME}; announcement strip"),
    }
    radius = {
        "none": dim("0px", f"{SRC_HOME}; marketing buttons compute border-radius 0px. Square corners are the marketing chrome."),
        "field": dim("4px", f"{SRC_CONTACT}; .framer-form-text-input border-radius 4px"),
        "auth-control": dim("10px", f"{SRC_AUTH}; --input-border-radius and --button-border-radius 10px"),
        "auth-card": dim("14px", f"{SRC_AUTH}; login card border-radius 14px, --border-radius-outer"),
    }
    spacing = {
        "nav-button-x": dim("13px", f"{SRC_HOME}; nav Start now padding-left/right 13px"),
        "nav-button-y": dim("8px", f"{SRC_HOME}; nav Start now padding-top/bottom 8px"),
        "button-x": dim("24px", f"{SRC_PRICE}; plan button padding-left/right 24px"),
        "button-y": dim("12px", f"{SRC_PRICE}; plan button padding-top 12px, padding-bottom 13px"),
        "field": dim("16px", f"{SRC_CONTACT}; text input wrapper padding 16px"),
        "form-card": dim("40px", f"{SRC_CONTACT}; form card padding 40px"),
        "control-height": dim("52px", f"{SRC_AUTH}; email input and Continue button height 52px. Contact submit is also 52px."),
    }
    shadow = {
        "nav-primary": tok("shadow", "0.5px 0.5px 0.5px 0 rgba(255, 255, 255, 0.25) inset, -0.5px -0.5px 1px 0 rgba(0, 0, 0, 0.12) inset, 1px 1px 2px 0 rgba(0, 0, 0, 0.08) inset", f"{SRC_HOME}; nav Start now box-shadow"),
        "field": tok("shadow", "0 0.482901px 0.482901px -1.875px rgba(0, 0, 0, 0.08), 0 4px 4px -3px rgba(0, 0, 0, 0.03)", f"{SRC_CONTACT}; text input wrapper box-shadow"),
        "form-card": tok("shadow", "0 2px 9px 1px rgba(0, 0, 0, 0.05)", f"{SRC_CONTACT}; form card box-shadow"),
        "auth-card": tok("shadow", "0 12px 40px 0 rgba(0, 0, 0, 0.12)", f"{SRC_AUTH}; login card box-shadow"),
    }
    size = {
        "nav-button-height": dim("30px", f"{SRC_HOME}; nav Start now height 30px"),
        "plan-button-height": dim("41px", f"{SRC_PRICE}; Start for free height 41px"),
        "field-height": dim("49px", f"{SRC_CONTACT}; text input wrapper height 49px"),
        "submit-height": dim("52px", f"{SRC_CONTACT}; Get in touch height 52px"),
        "auth-control-height": dim("52px", f"{SRC_AUTH}; email and Continue height 52px"),
        "content": dim("1040px", f"{SRC_HOME}; header inner row width 1040px at a 1440 viewport"),
    }

    def semantic(page, surface, text, muted, accent, border, source):
        return {
            "background": {
                "page": color(page, source + " page"),
                "surface": color(surface, source + " surface"),
                "action": color(accent, source + " action"),
            },
            "text": {
                "primary": color(text, source + " text"),
                "secondary": color(muted, source + " muted"),
            },
            "border": {
                "stroke": color(border, source + " border"),
            },
        }

    light = semantic(
        "{core.color.page}",
        "{core.color.paper}",
        "{core.color.ink}",
        "#57534d",
        "{core.color.ink}",
        "#e7e5e4",
        SRC_HOME + ";",
    )
    # The muted and border roles above are measured literals that also exist
    # as stone steps. Point them at the core steps so the alias graph is the
    # source of truth.
    light["text"]["secondary"] = color("{core.color.stone-600}", f"{SRC_HOME}; muted copy rgb(87, 83, 77) which is stone-600")
    light["border"]["stroke"] = color("{core.color.stone-200}", f"{SRC_AUTH}; social button border #E7E5E4, also the stone-200 token")

    auth = semantic(
        "#efedea",
        "#fafaf9",
        "#000000",
        "#79716b",
        "#000000",
        "#e7e5e4",
        SRC_AUTH + ";",
    )
    auth["text"]["secondary"] = color("#79716b", f"{SRC_AUTH}; --font-default-color #79716B, subtitle rgb(121, 113, 107)")
    auth["border"]["stroke"] = color("#e7e5e4", f"{SRC_AUTH}; --box-border-color #E7E5E4")
    auth["background"]["page"] = color("#efedea", f"{SRC_AUTH}; --page-background-color #efedea, body rgb(239, 237, 234)")
    auth["background"]["surface"] = color("#fafaf9", f"{SRC_AUTH}; --widget-background-color #FAFAF9, card rgb(250, 250, 249)")
    auth["background"]["action"] = color("#000000", f"{SRC_AUTH}; Continue background rgb(0, 0, 0), --primary-color #000")
    auth["text"]["primary"] = color("#000000", f"{SRC_AUTH}; h1 color rgb(0, 0, 0)")

    doc = {
        "core": {
            "color": core_color,
            "font": font,
            "fontWeight": weight,
            "typography": typography,
            "radius": radius,
            "spacing": spacing,
            "shadow": shadow,
            "size": size,
        },
        "light": light,
        "auth": auth,
        "$themes": [
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
                "$description": "The only theme www.rox.com paints. No dark theme switch was found.",
            },
            {
                "id": "auth",
                "name": "Auth",
                "selectedTokenSets": {"core": "source", "auth": "enabled"},
                "$description": "The signed-out Auth0 login and signup card. A separate palette from the marketing site.",
            },
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "auth"]},
    }
    check(doc)
    return doc


def main() -> int:
    doc = build()
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
