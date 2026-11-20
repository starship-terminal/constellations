#!/usr/bin/env python3
"""Build systems/pixso/tokens.json from raw/css-vars.json and measured controls.

Values are read from pixso.net on 2026-11-21 in headless Chromium at 1440x900.
Declared custom properties come from :root and the header/footer selectors.
Painted control colours that are not custom properties are labelled Measured,
with the element and state named in $extensions.source.

One light theme. No dark set: html has no data-theme and color-scheme is normal.
Unread states stay out of the file. Not captured is recorded in the README.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
DECL = {name: spec["value"] for name, spec in RAW["declared"].items()}


def norm_color(v):
    v = str(v).strip().lower()
    named = {"#fff": "#ffffff", "#000": "#000000"}
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or a in ("1", "1.0"):
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    if v in named:
        return named[v]
    raise ValueError("not a colour: " + v)


def color(path, value, source):
    return {
        "$type": "color",
        "$value": norm_color(value),
        "$extensions": {"source": source, "evidence": "Measured"},
    }


def dim(path, value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?px", str(value)):
        raise ValueError(f"{path}: dimension {value!r}")
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source, "evidence": "Measured"},
    }


def font_weight(value, source):
    return {
        "$type": "fontWeight",
        "$value": int(value),
        "$extensions": {"source": source, "evidence": "Measured"},
    }


def typography(family, size, weight, line, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": source, "evidence": "Measured"},
    }


def alias(path, target):
    return {"$type": "color", "$value": target, "$extensions": {"source": "alias " + target, "evidence": "Derived"}}


core = {
    "color": {
        "ink": color("core.color.ink", "#1e2330", "css-var --pxn-ink on #wsc-header[data-pixso-nav-version]"),
        "inkSoft": color("core.color.inkSoft", "#202124", "css-var --pxf-text on #common-footer.px-footer-unified"),
        "muted": color("core.color.muted", "#647084", "css-var --pxn-muted on #wsc-header[data-pixso-nav-version]"),
        "mutedFooter": color("core.color.mutedFooter", "#667085", "css-var --pxf-muted on #common-footer.px-footer-unified"),
        "brand": color("core.color.brand", "#336fff", "css-var --v2--color-bg-brand-normal and --pxn-blue"),
        "brandHover": color("core.color.brandHover", "#4381ff", "css-var --v2--color-bg-brand-hover"),
        "action": color("core.color.action", "#006dff", "css-var --action on :root"),
        "support": color("core.color.support", "#ffc400", "css-var --support on :root"),
        "white": color("core.color.white", "#ffffff", "css-var --white on :root"),
        "black": color("core.color.black", "#000000", "css-var --black on :root"),
        "page": color("core.color.page", "rgb(255, 255, 255)", "computed background-color on body, home, default"),
        "text": color("core.color.text", "rgb(0, 0, 0)", "computed color on body and h1, home, default"),
        "button": color("core.color.button", "rgb(32, 33, 37)", "computed background-color on .login-btn.px-common-btn, Get started, default"),
        "buttonText": color("core.color.buttonText", "rgb(255, 255, 255)", "computed color on Get started link, default"),
        "loginText": color("core.color.loginText", "rgb(61, 61, 61)", "computed color on Log in link, default"),
        "field": color("core.color.field", "rgb(247, 247, 249)", "computed background-color on contact name input, default, not focused"),
        "fieldBorder": color("core.color.fieldBorder", "rgba(0, 0, 0, 0.1)", "computed border-top-color on login email input, resting, after blur"),
        "fieldText": color("core.color.fieldText", "rgb(25, 25, 26)", "computed color on login email input, resting"),
        "focus": color("core.color.focus", "rgb(31, 97, 255)", "computed border-top-color on login email input, focus, before blur"),
        "success": color("core.color.success", DECL["--success"], "css-var --success on :root"),
        "warning": color("core.color.warning", DECL["--warning"], "css-var --warning on :root"),
        "danger": color("core.color.danger", DECL["--danger"], "css-var --danger on :root"),
        "info": color("core.color.info", DECL["--info"], "css-var --info on :root"),
        "border": color("core.color.border", "#edf0f4", "css-var --pxn-border on #wsc-header[data-pixso-nav-version]"),
        "rule": color("core.color.rule", "rgba(16, 24, 40, 0.12)", "css-var --pxf-rule on #common-footer.px-footer-unified"),
    },
    "font": {
        "family": {
            "sans": {
                "$type": "fontFamily",
                "$value": "Figtree, Arial, Helvetica Neue, Microsoft YaHei, Helvetica, sans-serif",
                "$extensions": {"source": "computed font-family on body, home, default", "evidence": "Measured"},
            },
            "declaredSans": {
                "$type": "fontFamily",
                "$value": "Poppins, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif",
                "$extensions": {"source": "css-var --font-family-sans-serif on :root; body computed Figtree, so this stack is declared and not the painted body", "evidence": "Measured"},
            },
            "mono": {
                "$type": "fontFamily",
                "$value": "SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace",
                "$extensions": {"source": "css-var --font-family-monospace on :root", "evidence": "Measured"},
            },
        }
    },
    "typography": {
        "display": typography("Figtree", "60px", 700, "66px", "computed on h1.home-module__title, home, default"),
        "heading": typography("Figtree", "40px", 600, "46px", "computed on h2, pricing page, default"),
        "body": typography("Figtree", "16px", 400, "24px", "computed on body, home, default"),
        "label": typography("Figtree", "14px", 500, "20px", "computed on header Pricing link and Get started link, default"),
        "caption": typography("Figtree", "14px", 400, "20px", "computed font-size on login email input, resting; line-height not separately recorded, size is"),
    },
    "radius": {
        "nav": dim("core.radius.nav", "6px", "computed border-radius on header Pricing link"),
        "button": dim("core.radius.button", "7px", "computed border-radius on .login-btn.px-common-btn"),
        "loginItem": dim("core.radius.loginItem", "8px", "computed border-radius on .login-item wrapping Log in"),
        "field": dim("core.radius.field", "6px", "computed border-radius on contact name input, default"),
        "loginField": dim("core.radius.loginField", "8px", "computed border-radius on login email input, resting"),
    },
    "space": {
        "headerX": dim("core.space.headerX", "32px", "computed padding-left on .pxn-bar"),
        "navY": dim("core.space.navY", "10px", "computed padding-top on header Pricing link"),
        "navX": dim("core.space.navX", "11px", "computed padding-left on header Pricing link"),
        "buttonY": dim("core.space.buttonY", "6px", "computed padding-top on .login-btn.px-common-btn"),
        "buttonX": dim("core.space.buttonX", "15px", "computed padding-left on .login-btn.px-common-btn"),
        "fieldX": dim("core.space.fieldX", "16px", "computed padding-left on contact name input"),
    },
    "size": {
        "header": dim("core.size.header", "54px", "css-var --header-height on :root; painted .pxn-bar height was 53px"),
        "navItem": dim("core.size.navItem", "40px", "computed height of header Pricing link"),
        "button": dim("core.size.button", "34px", "computed height of .login-btn.px-common-btn"),
        "field": dim("core.size.field", "40px", "computed height of contact name input and login email input"),
        "content": dim("core.size.content", "1380px", "css-var --content-max-width on :root"),
    },
    "border": {
        "field": dim("core.border.field", "1px", "computed border-top-width on login email input, resting"),
        "focus": dim("core.border.focus", "2px", "computed border-top-width on login email input, focus, before blur"),
    },
    "breakpoint": {
        "sm": dim("core.breakpoint.sm", "576px", "css-var --breakpoint-sm on :root"),
        "md": dim("core.breakpoint.md", "768px", "css-var --breakpoint-md on :root"),
        "lg": dim("core.breakpoint.lg", "992px", "css-var --breakpoint-lg on :root"),
        "xl": dim("core.breakpoint.xl", "1280px", "css-var --breakpoint-xl on :root"),
        "xxl": dim("core.breakpoint.xxl", "1600px", "css-var --breakpoint-xxl on :root"),
    },
}

light = {
    "background": {
        "page": alias("light.background.page", "{core.color.page}"),
        "surface": alias("light.background.surface", "{core.color.field}"),
        "button": alias("light.background.button", "{core.color.button}"),
        "brand": alias("light.background.brand", "{core.color.brand}"),
    },
    "text": {
        "primary": alias("light.text.primary", "{core.color.text}"),
        "ink": alias("light.text.ink", "{core.color.ink}"),
        "muted": alias("light.text.muted", "{core.color.muted}"),
        "onButton": alias("light.text.onButton", "{core.color.buttonText}"),
        "link": alias("light.text.link", "{core.color.brand}"),
    },
    "border": {
        "default": alias("light.border.default", "{core.color.border}"),
        "rule": alias("light.border.rule", "{core.color.rule}"),
        "field": alias("light.border.field", "{core.color.fieldBorder}"),
        "focus": alias("light.border.focus", "{core.color.focus}"),
    },
    "status": {
        "success": alias("light.status.success", "{core.color.success}"),
        "warning": alias("light.status.warning", "{core.color.warning}"),
        "danger": alias("light.status.danger", "{core.color.danger}"),
        "info": alias("light.status.info", "{core.color.info}"),
    },
}

doc = {
    "$description": "Pixso public site tokens, measured 2026-11-21 from https://pixso.net/. One light theme.",
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
}

# Validate every colour and dimension.
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{"):
            return
        if ty == "color":
            norm_color(val)
        if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?px", str(val)):
            raise SystemExit(f"bad dimension {path} {val}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)

walk(doc)
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out)
