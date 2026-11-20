#!/usr/bin/env python3
"""Build tokens.json from raw/computed.json.

ZARA's public storefront (www.zara.com/us, stylesheet 10.21.1) declares its
system as custom properties on :root. Those resolved values, plus computed
styles of the controls that were on screen, live in raw/computed.json. This
script only copies them into DTCG. It does not invent a dark palette: the
public storefront had no theme switch.

Every token carries $extensions.source. A dimension is one px or rem length.
"""
from __future__ import annotations

import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "computed.json").read_text())

SRC_ROOT = RAW["source"]["root"]
SRC_EL = RAW["source"]["elements"]


def to_hex(value: str) -> str:
    """A CSS colour as #rrggbb, or #rrggbbaa when translucent; refuses anything else.
    tools/catalog.py and the contrast check read only hex, so hsla()/rgba() were skipped."""
    v = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})", v)
    if m:
        h = m.group(1)
        h = "".join(c * 2 for c in h) if len(h) in (3, 4) else h
        return "#" + (h[:6] if h[6:] == "ff" else h)
    m = re.fullmatch(r"(rgba?|hsla?)\((.*)\)", v)
    if not m:
        raise SystemExit(f"not a colour: {value!r}")
    fn, parts = m.group(1), [x for x in re.split(r"[\s,/]+", m.group(2).strip()) if x]
    if len(parts) not in (3, 4):
        raise SystemExit(f"not a colour: {value!r}")
    pct = lambda x, scale: float(x[:-1]) / 100 * scale if x.endswith("%") else float(x)
    a = pct(parts[3], 1) if len(parts) == 4 else 1.0
    if fn.startswith("rgb"):
        r, g, b = (pct(x, 255) for x in parts[:3])
    else:
        hh, ss, ll = float(parts[0]) % 360 / 30, pct(parts[1], 1), pct(parts[2], 1)
        f = lambda n: ll - ss * min(ll, 1 - ll) * max(-1, min((n + hh) % 12 - 3, 9 - (n + hh) % 12, 1))
        r, g, b = (f(n) * 255 for n in (0, 8, 4))
    out = "#" + "".join("%02x" % max(0, min(255, round(c))) for c in (r, g, b))
    return out if a >= 1 else out + "%02x" % round(a * 255)


def color(value: str, source: str) -> dict:
    if value.startswith("{"):
        return {"$type": "color", "$value": value, "$extensions": {"source": source}}
    hexed = to_hex(value)
    if hexed != value.strip().lower():
        source = f"{source} (declared {value.strip()}, written as hex)"
    return {"$type": "color", "$value": hexed, "$extensions": {"source": source}}


def dim(value: str, source: str) -> dict:
    text = value.strip()
    ok = re.fullmatch(r"-?\d*\.?\d+(px|rem)", text) or text in {"0px", "0rem"}
    if not ok:
        raise SystemExit(f"not a px/rem dimension: {value}")
    return {"$type": "dimension", "$value": text, "$extensions": {"source": source}}


def font(value: str, source: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def resolve_calc(value: str) -> str:
    """The browser's calc(Nrem * 1) and calc(0 * 1) resolve to the inner length."""
    text = value.strip()
    m = re.fullmatch(r"calc\(([0-9.]+)rem \* 1\)", text)
    if m:
        return f"{m.group(1)}rem"
    if text in {"calc(0 * 1)", "calc(0rem * 1)"}:
        return "0px"
    return text


def typography(family: str, size: str, weight: str, line: str, tracking: str, source: str) -> dict:
    weight = {"normal": "400", "bold": "700"}.get(weight, weight)
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": resolve_calc(size),
            "fontWeight": weight,
            "lineHeight": resolve_calc(line),
            "letterSpacing": resolve_calc(tracking),
        },
        "$extensions": {"source": source + " (calc(Nrem * 1) stored resolved)"},
    }


def number(value, source: str) -> dict:
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def text(value: str, source: str) -> dict:
    return {"$type": "other", "$value": value, "$extensions": {"source": source}}


root = RAW["root"]
el = RAW["elements"]


def rv(name: str) -> str:
    return root[name]


def core() -> dict:
    spacing = {}
    for i in range(17):
        key = f"{i:02d}"
        spacing[f"s{key}"] = dim(rv(f"--spacing-{key}"), f"{SRC_ROOT} --spacing-{key}")
    radius = {
        "none": dim("0px", f"{SRC_EL} zds-button, size list, search input, dialog wrapper all computed border-radius 0px"),
    }
    type_styles = {
        "label-l": typography(rv("--font-family-label-l"), rv("--font-size-label-l"), rv("--font-weight-label-l"), rv("--line-height-label-l"), rv("--letter-spacing-label-l"), f"{SRC_ROOT} --font-*-label-l"),
        "label-m": typography(rv("--font-family-label-m"), rv("--font-size-label-m"), rv("--font-weight-label-m"), rv("--line-height-label-m"), rv("--letter-spacing-label-m"), f"{SRC_ROOT} --font-*-label-m"),
        "label-s": typography(rv("--font-family-label-s"), rv("--font-size-label-s"), rv("--font-weight-label-s"), rv("--line-height-label-s"), rv("--letter-spacing-label-s"), f"{SRC_ROOT} --font-*-label-s"),
        "label-xs": typography(rv("--font-family-label-xs"), rv("--font-size-label-xs"), rv("--font-weight-label-xs"), rv("--line-height-label-xs"), rv("--letter-spacing-label-xs"), f"{SRC_ROOT} --font-*-label-xs"),
        "label-m-highlight": typography(rv("--font-family-label-m-highlight"), rv("--font-size-label-m-highlight"), rv("--font-weight-label-m-highlight"), rv("--line-height-label-m-highlight"), rv("--letter-spacing-label-m-highlight"), f"{SRC_ROOT} --font-*-label-m-highlight"),
        "body-l": typography(rv("--font-family-body-l"), rv("--font-size-body-l"), rv("--font-weight-body-l"), rv("--line-height-body-l"), rv("--letter-spacing-body-l"), f"{SRC_ROOT} --font-*-body-l"),
        "body-m": typography(rv("--font-family-body-m"), rv("--font-size-body-m"), rv("--font-weight-body-m"), rv("--line-height-body-m"), rv("--letter-spacing-body-m"), f"{SRC_ROOT} --font-*-body-m"),
        "body-s": typography(rv("--font-family-body-s"), rv("--font-size-body-s"), rv("--font-weight-body-s"), rv("--line-height-body-s"), rv("--letter-spacing-body-s"), f"{SRC_ROOT} --font-*-body-s"),
        "title-l": typography(rv("--font-family-title-l"), rv("--font-size-title-l"), rv("--font-weight-title-l"), rv("--line-height-title-l"), rv("--letter-spacing-title-l"), f"{SRC_ROOT} --font-*-title-l"),
        "title-m": typography(rv("--font-family-title-m"), rv("--font-size-title-m"), rv("--font-weight-title-m"), rv("--line-height-title-m"), rv("--letter-spacing-title-m"), f"{SRC_ROOT} --font-*-title-m"),
        "title-alt-l": typography(rv("--font-family-title-alt-l"), rv("--font-size-title-alt-l"), rv("--font-weight-title-alt-l"), rv("--line-height-title-alt-l"), rv("--letter-spacing-title-alt-l"), f"{SRC_ROOT} --font-*-title-alt-l"),
    }
    return {
        "font": {
            "family": {
                "main": font(rv("--font-family-main"), f"{SRC_ROOT} --font-family-main"),
                "alt": font(rv("--font-family-alt"), f"{SRC_ROOT} --font-family-alt"),
                "title-alt": font(rv("--font-family-title-alt-l"), f"{SRC_ROOT} --font-family-title-alt-l"),
            }
        },
        "weight": {
            "light": number(300, f"{SRC_ROOT} --font-weight-light = 300"),
            "regular": number(400, f"{SRC_ROOT} --font-weight-regular = normal, computed as 400 on category links"),
            "medium": number(500, f"{SRC_ROOT} --font-weight-medium = 500"),
            "bold": number(700, f"{SRC_ROOT} --font-weight-bold = bold"),
        },
        "spacing": spacing,
        "radius": radius,
        "line": {
            "thin": dim(rv("--zds-line-width"), f"{SRC_ROOT} --zds-line-width"),
            "thick": dim(rv("--zds-line-width-thick"), f"{SRC_ROOT} --zds-line-width-thick"),
        },
        "layout": {
            "actionable-height": dim(rv("--layout-actionable-height"), f"{SRC_ROOT} --layout-actionable-height"),
            "actionable-size": dim(rv("--layout-actionable-size"), f"{SRC_ROOT} --layout-actionable-size"),
            "horizontal-padding": dim(rv("--layout-horizontal-padding"), f"{SRC_ROOT} --layout-horizontal-padding"),
            "lateral-margin": dim(rv("--layout-lateral-margin"), f"{SRC_ROOT} --layout-lateral-margin"),
            "grid-gutter": dim(rv("--grid-column-gutter"), f"{SRC_ROOT} --grid-column-gutter"),
            "grid-columns": number(12, f"{SRC_ROOT} --grid-columns = 12"),
        },
        "motion": {
            "category": text(f"{rv('--category-transition-duration')} {rv('--category-transition-easing')}", f"{SRC_ROOT} --category-transition-duration and --category-transition-easing"),
        },
        "typography": type_styles,
    }


def light() -> dict:
    c = {
        "page": color(rv("--color-background-base"), f"{SRC_ROOT} --color-background-base; body computed rgb(255, 255, 255)"),
        "wash": color(rv("--color-background-low"), f"{SRC_ROOT} --color-background-low"),
        "wash-alt": color(rv("--color-background-low-alt"), f"{SRC_ROOT} --color-background-low-alt"),
        "mid": color(rv("--color-background-mid"), f"{SRC_ROOT} --color-background-mid"),
        "inverse": color(rv("--color-background-high"), f"{SRC_ROOT} --color-background-high"),
        "inverse-alt": color(rv("--color-background-high-alt"), f"{SRC_ROOT} --color-background-high-alt"),
        "overlay": color(rv("--color-background-overlay"), f"{SRC_ROOT} --color-background-overlay"),
        "overlay-light": color(rv("--color-background-overlay-alt"), f"{SRC_ROOT} --color-background-overlay-alt"),
        "surface": color(rv("--color-background-surface"), f"{SRC_ROOT} --color-background-surface"),
        "base-alt": color(rv("--color-background-base-alt"), f"{SRC_ROOT} --color-background-base-alt"),
    }
    text_c = {
        "primary": color(rv("--color-content-high"), f"{SRC_ROOT} --color-content-high; body computed rgb(0, 0, 0)"),
        "secondary": color(rv("--color-content-mid"), f"{SRC_ROOT} --color-content-mid"),
        "secondary-alt": color(rv("--color-content-mid-alt"), f"{SRC_ROOT} --color-content-mid-alt"),
        "muted": color(rv("--color-content-low"), f"{SRC_ROOT} --color-content-low"),
        "inverse": color(rv("--color-content-inverse"), f"{SRC_ROOT} --color-content-inverse"),
    }
    border = {
        "default": color(rv("--color-main-020"), f"{SRC_ROOT} --color-main-020; dialog wrapper computed 1px solid rgb(204, 204, 204)"),
        "strong": color(rv("--color-main"), f"{SRC_ROOT} --color-main; secondary button computed 0.5px solid rgb(0, 0, 0)"),
        "hairline": color("#000000", f"{SRC_EL} secondary zds-button border-top-color rgb(0, 0, 0) at --zds-line-width 0.5px"),
        "field": color(rv("--form-input-label-border-color-unfocused"), f"{SRC_ROOT} --form-input-label-border-color-unfocused"),
        "field-account": color("#797979", f"{SRC_EL} account.zara.com .mds-base-field__control border rgb(121, 121, 121)"),
    }
    action = {
        "primary": color("#000000", f"{SRC_EL} geolocation primary button and account CONTINUE computed background rgb(0, 0, 0)"),
        "primary-text": color("#ffffff", f"{SRC_EL} those buttons computed color rgb(255, 255, 255)"),
        "secondary": color("#ffffff", f"{SRC_EL} secondary zds-button computed background rgb(255, 255, 255)"),
        "secondary-text": color("#000000", f"{SRC_EL} secondary zds-button computed color rgb(0, 0, 0)"),
    }
    status = {
        "done": color(rv("--color-done"), f"{SRC_ROOT} --color-done"),
        "emphasis": color(rv("--color-emphasis"), f"{SRC_ROOT} --color-emphasis"),
        "emphasis-bg": color(rv("--color-emphasis-background"), f"{SRC_ROOT} --color-emphasis-background"),
        "sales": color(rv("--color-sales"), f"{SRC_ROOT} --color-sales"),
        "notification": color(rv("--color-notification"), f"{SRC_ROOT} --color-notification"),
        "notification-bg": color(rv("--color-notification-background"), f"{SRC_ROOT} --color-notification-background"),
        "focus": color(rv("--color-focus-ring"), f"{SRC_ROOT} --color-focus-ring"),
        "info": color(rv("--color-semantic-info-high"), f"{SRC_ROOT} --color-semantic-info-high"),
        "info-low": color(rv("--color-semantic-info-low"), f"{SRC_ROOT} --color-semantic-info-low"),
        "danger": color(rv("--color-semantic-danger-high"), f"{SRC_ROOT} --color-semantic-danger-high"),
        "danger-low": color(rv("--color-semantic-danger-low"), f"{SRC_ROOT} --color-semantic-danger-low"),
        "success": color(rv("--color-semantic-success-high"), f"{SRC_ROOT} --color-semantic-success-high"),
        "success-low": color(rv("--color-semantic-success-low"), f"{SRC_ROOT} --color-semantic-success-low"),
        "warning": color(rv("--color-semantic-warning-high"), f"{SRC_ROOT} --color-semantic-warning-high"),
        "warning-low": color(rv("--color-semantic-warning-low"), f"{SRC_ROOT} --color-semantic-warning-low"),
    }
    scale = {}
    for step, name in (("000", "000"), ("005", "005"), ("010", "010"), ("020", "020"), ("040", "040"), ("060", "060"), ("080", "080")):
        scale[f"s{name}"] = color(rv(f"--color-main-{step}"), f"{SRC_ROOT} --color-main-{step}")
    component = {
        "button-primary": {
            "bg": color("{action.primary}", f"{SRC_EL} .zds-button--primary and .mds-button--primary"),
            "text": color("{action.primary-text}", f"{SRC_EL} primary button text"),
            "radius": dim("0px", f"{SRC_EL} primary button border-radius 0px"),
            "height": dim(el["buttonPrimary"]["height"], f"{SRC_EL} geolocation primary button height"),
            "padding": text(el["buttonPrimary"]["padding"], f"{SRC_EL} geolocation primary button padding"),
        },
        "button-secondary": {
            "bg": color("{action.secondary}", f"{SRC_EL} .zds-button--secondary"),
            "text": color("{action.secondary-text}", f"{SRC_EL} secondary button text"),
            "radius": dim("0px", f"{SRC_EL} secondary button border-radius 0px"),
            "height": dim(el["buttonSecondary"]["height"], f"{SRC_EL} ADD button height 40px (large); small secondary is 32px"),
        },
        "nav-link": {
            "text": color("{text.primary}", f"{SRC_EL} header SEARCH/LOG IN/HELP"),
            "size": dim(el["navLink"]["fontSize"], f"{SRC_EL} header actionable font-size"),
        },
        "product-name": {
            "text": color("{text.primary}", f"{SRC_EL} .product-detail-info__header-name"),
            "size": dim(el["productName"]["fontSize"], f"{SRC_EL} product name font-size"),
        },
        "price": {
            "text": color("{text.primary}", f"{SRC_EL} .money-amount--highlight"),
            "size": dim(el["price"]["fontSize"], f"{SRC_EL} highlighted price font-size"),
        },
        "dialog": {
            "bg": color("#ffffff", f"{SRC_EL} .zds-dialog__wrapper background rgb(255, 255, 255)"),
            "radius": dim("0px", f"{SRC_EL} dialog wrapper border-radius 0px"),
        },
        "field": {
            "text": color("{text.primary}", f"{SRC_EL} search and help inputs"),
            "radius": dim("0px", f"{SRC_EL} search-home-input and help input border-radius 0px"),
        },
    }
    return {
        "color": {"bg": c, "text": text_c, "border": border, "action": action, "status": status, "scale": scale},
        "surface": {"page": color("{color.bg.page}", SRC_ROOT), "wash": color("{color.bg.wash}", SRC_ROOT)},
        "text": {"primary": color("{color.text.primary}", SRC_ROOT), "secondary": color("{color.text.secondary}", SRC_ROOT), "muted": color("{color.text.muted}", SRC_ROOT)},
        "border": {"default": color("{color.border.default}", SRC_ROOT)},
        "action": action,
        "component": component,
    }


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        if "$value" in value:
            yield path + key, value
        else:
            yield from walk(value, path + key + ".")


def aliases(value, where="value"):
    """Every alias inside a value, at any depth. A string holding a brace must be one whole alias."""
    if isinstance(value, str):
        if "{" not in value and "}" not in value:
            return []
        m = re.fullmatch(r"\{([A-Za-z0-9_.-]+)\}", value)
        if not m:
            raise SystemExit(f"{where}: malformed alias {value!r}")
        return [m.group(1)]
    if isinstance(value, dict):
        return [a for v in value.values() for a in aliases(v, where)]
    if isinstance(value, list):
        return [a for v in value for a in aliases(v, where)]
    return []


def follow(ref, own, core, where, chain=()):
    """Resolve ref in its own set, then core; follow the target's aliases and refuse a cycle."""
    if ref in chain:
        raise SystemExit(f"{where}: alias cycle through {{{ref}}}")
    scope = own if ref in own else core
    if ref not in scope:
        raise SystemExit(f"{where}: alias {{{ref}}} points at nothing")
    for nxt in aliases(scope[ref]["$value"], where):
        follow(nxt, scope, core, where, (*chain, ref))


def check(doc: dict) -> None:
    """Refuse a token with no source, a colour that is not hex, a dimension that is not one px or
    rem length, a malformed alias, an alias that does not resolve in its own set or in core (the
    Resolver's order), and an alias chain that loops."""
    core_names = dict(walk(doc["core"]))
    for set_name in ("core", "light"):
        own = dict(walk(doc[set_name]))
        for path, token in walk(doc[set_name]):
            where = f"{set_name}.{path}"
            if not token.get("$extensions", {}).get("source"):
                raise SystemExit(f"{where}: no source")
            refs = aliases(token["$value"], where)
            for a in refs:
                follow(a, own, core_names, where, (path,))
            value = token["$value"]
            if isinstance(value, str) and refs:
                continue
            if token["$type"] == "color" and not re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", value):
                raise SystemExit(f"{where}: colour {value!r} is not hex")
            if token["$type"] == "dimension" and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", value):
                raise SystemExit(f"{where}: dimension {value!r}")


def build() -> dict:
    doc = {
        "$schema": "https://tr.designtokens.org/format/",
        "core": core(),
        "light": light(),
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    check(doc)
    return doc


def render() -> str:
    """tokens.json's exact text; nothing is written."""
    return json.dumps(build(), indent=2) + "\n"


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(render())
    print("tokens.json written")
