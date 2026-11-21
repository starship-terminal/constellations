#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Douze declares its palette and type as Shopify :root custom properties
(raw/root-vars.json) and paints them on the public storefront. This builder
emits a core set of those measured primitives and a light semantic set that
aliases them. There is no dark theme on the public site.

Every leaf needs a source. An alias that points at nothing fails the build.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())

DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            return "rgba(%d, %d, %d, %s)" % (
                *[int(h[i:i + 2], 16) for i in (0, 2, 4)],
                "%g" % round(int(h[6:8], 16) / 255, 3),
            )
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % a)
    raise ValueError("not a colour: " + v)


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    if not spec.get("source"):
        raise ValueError(f"{path}: leaf without a source")
    val = spec["value"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "fontWeight" and isinstance(val, str) and val.isdigit():
        val = int(val)
    if ty == "typography":
        for part, pty in (
            ("fontFamily", "fontFamily"),
            ("fontSize", "dimension"),
            ("fontWeight", "fontWeight"),
            ("lineHeight", "dimension"),
            ("letterSpacing", "dimension"),
        ):
            check(path + "." + part, pty, val[part])
    else:
        check(path, ty, val)
    return {
        "$value": val,
        "$type": ty,
        "$extensions": {"source": spec["source"]},
    }


def group(prefix, node):
    out = {}
    for key, spec in node.items():
        path = f"{prefix}.{key}" if prefix else key
        if "type" in spec:
            out[key] = leaf(path, spec)
        else:
            out[key] = group(path, spec)
    return out


core = {
    "$description": "Douze primitives read from drinkdouze.com :root and computed styles, 2026-11-21. One light theme.",
}
core.update(group("", SPEC))

def alias(path, source):
    return {
        "$value": "{" + path + "}",
        "$type": "color",
        "$extensions": {"source": source},
    }


light = {
    "$description": "Semantic roles for the single light storefront. Aliases of core.",
    "background": {
        "page": alias("color.paper", "html background is the declared --background paper"),
        "surface": alias("color.sable", "footer, header bubble and login card use --secondary-background / --color-sable"),
        "inverse": alias("color.dusk", "primary button and selected filter fill"),
    },
    "text": {
        "primary": alias("color.dusk", "body and nav computed color"),
        "onAccent": alias("color.onAccent", "button label color"),
        "onHero": alias("color.heroInk", "hero heading over the product photograph"),
        "muted": alias("color.soldOut", "declared sold-out accent; the only muted grey on :root"),
        "link": alias("color.dusk", "nav and footer links use the same dusk ink"),
    },
    "border": {
        "default": alias("color.border", "declared --border-color"),
        "strong": alias("color.borderStrong", "declared --border-color-darker"),
    },
    "accent": {
        "default": alias("color.dusk", "primary button background; there is no second brand accent"),
    },
    "status": {
        "success": alias("color.sage", "declared --success-color"),
        "inStock": alias("color.inStock", "declared --product-in-stock-text-color"),
        "lowStock": alias("color.lowStock", "declared --product-low-stock-text-color"),
    },
    "component": {
        "button": {
            "bg": alias("color.dusk", "computed background of .button and .product-form__add-button"),
            "text": alias("color.onAccent", "computed color of those buttons"),
            "radius": {
                "$value": "{radius.none}",
                "$type": "dimension",
                "$extensions": {"source": "declared --button-border-radius"},
            },
            "height": {
                "$value": "{size.buttonSmall}",
                "$type": "dimension",
                "$extensions": {"source": "computed height of the small button; --button-height is 52px"},
            },
        },
        "field": {
            "bg": alias("color.paper", "login fields sit on the paper page inside the sable card"),
            "text": alias("color.dusk", "field label and placeholder ink"),
            "radius": {
                "$value": "{radius.blockReduced}",
                "$type": "dimension",
                "$extensions": {"source": "computed border-radius of the login email and password fields is 16px (raw/measurements.json login.email and login.password); matches declared --block-border-radius-reduced"},
            },
        },
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedColor": "#301816", "group": "light"}],
}

# refuse a dangling alias
def walk(node, trail=""):
    if isinstance(node, dict) and "$value" in node:
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
            path = val[1:-1].split(".")
            cur = core
            for part in path:
                if not isinstance(cur, dict) or part not in cur:
                    raise SystemExit(f"dangling alias {trail} -> {val}")
                cur = cur[part]
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, trail + "." + k)

walk(light)
text = json.dumps(tokens, indent=1, ensure_ascii=False) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote", HERE / "tokens.json", "bytes", len(text))
