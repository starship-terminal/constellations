#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Macaw's public site (macawhq.com, 2026-11-21) paints one light theme. Declared
custom properties are a Senja widget's Tailwind internals (raw/css-vars.json),
so semantic colours come from computed styles, each with a source string.

Aliases are unprefixed and resolve against core, then the leaf's own set.
The builder refuses a missing source, a broken alias, a colour it cannot
parse, and a dimension that is not one px or rem length.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            return "rgba(%d, %d, %d, %s)" % (*[int(h[i:i + 2], 16) for i in (0, 2, 4)], "%g" % round(int(h[6:8], 16) / 255, 3))
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
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
    if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
        val += "px"
    if ty == "typography":
        check(path, "typography", val)
        t = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
        return t
    if ty == "shadow":
        t = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
        return t
    if ty == "fontFamily":
        t = {"$value": val, "$type": "fontFamily", "$extensions": {"source": spec["source"]}}
        return t
    check(path, ty, val)
    return {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        out[k] = build(v, f"{path}.{k}" if path else k)
    return out


def aliases(node, found=None):
    found = found if found is not None else set()
    if isinstance(node, dict) and "$value" in node:
        val = node["$value"]
        if isinstance(val, str):
            found.update(re.findall(r"\{([^{}]+)\}", val))
        elif isinstance(val, dict):
            for part in val.values():
                if isinstance(part, str):
                    found.update(re.findall(r"\{([^{}]+)\}", part))
        return found
    if isinstance(node, dict):
        for v in node.values():
            aliases(v, found)
    return found


def paths(node, prefix=""):
    out = set()
    if isinstance(node, dict) and "$value" in node:
        out.add(prefix)
        return out
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            out |= paths(v, f"{prefix}.{k}" if prefix else k)
    return out


core = build({k: v for k, v in SPEC.items() if k in ("color", "font", "typography", "radius", "space", "size", "shadow")})
light = {
    "background": {
        "page": leaf("light.background.page", {"type": "color", "value": "{color.page}", "source": "Alias of core.color.page, the body background measured on the home page."}),
        "surface": leaf("light.background.surface", {"type": "color", "value": "{color.white}", "source": "Alias of core.color.white. Cards, the dialog, and the Log in button compute to rgb(255, 255, 255)."}),
        "raised": leaf("light.background.raised", {"type": "color", "value": "{color.row}", "source": "Alias of core.color.row, the pricing comparison row."}),
        "highlight": leaf("light.background.highlight", {"type": "color", "value": "{color.lilac}", "source": "Alias of core.color.lilac, the hero highlight wash."}),
    },
    "text": {
        "primary": leaf("light.text.primary", {"type": "color", "value": "{color.ink}", "source": "Alias of core.color.ink, the h1 colour."}),
        "secondary": leaf("light.text.secondary", {"type": "color", "value": "{color.text}", "source": "Alias of core.color.text, the body colour."}),
        "muted": leaf("light.text.muted", {"type": "color", "value": "{color.muted}", "source": "Alias of core.color.muted."}),
        "onAccent": leaf("light.text.onAccent", {"type": "color", "value": "{color.white}", "source": "Alias of core.color.white, the label on the coral button."}),
        "link": leaf("light.text.link", {"type": "color", "value": "{color.textNav}", "source": "Alias of core.color.textNav. Nav links are the same ink as body headings until hover, when they turn coral. No separate link blue was measured."}),
    },
    "border": {
        "default": leaf("light.border.default", {"type": "color", "value": "{color.planStarter}", "source": "Alias of core.color.planStarter. The Starter card's 1px border computed to the same colour as its fill (rgb(246, 226, 255)). A neutral hairline was not a separate reading."}),
        "strong": leaf("light.border.strong", {"type": "color", "value": "#000000", "source": "Measured: Pro plan card borderTopColor rgb(0, 0, 0), raw/foundations.json extra.cards."}),
        "focus": leaf("light.border.focus", {"type": "color", "value": "{color.focusRing}", "source": "Alias of core.color.focusRing, the 4px contact-field ring."}),
    },
    "accent": {
        "default": leaf("light.accent.default", {"type": "color", "value": "{color.coral}", "source": "Alias of core.color.coral, the primary button fill."}),
        "hover": leaf("light.accent.hover", {"type": "color", "value": "{color.coralHover}", "source": "Alias of core.color.coralHover, the primary button hover fill."}),
        "pressed": leaf("light.accent.pressed", {"type": "color", "value": "{color.coralPressed}", "source": "Alias of core.color.coralPressed. A held press was not captured. This is the nav-link hover, rgb(242, 101, 87), not the button hover."}),
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

# resolve aliases against core then the set
def collect(node, prefix=""):
    out = {}
    if isinstance(node, dict) and "$value" in node:
        out[prefix] = node
        return out
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            out.update(collect(v, f"{prefix}.{k}" if prefix else k))
    return out

core_paths = collect(tokens["core"])
light_paths = collect(tokens["light"])

def resolve(ref, own):
    if ref in own:
        return own[ref]["$value"]
    if ref in core_paths:
        return core_paths[ref]["$value"]
    raise SystemExit(f"alias {{{ref}}} points at nothing")

for name, node in {**core_paths, **light_paths}.items():
    own = core_paths if name in core_paths else light_paths
    val = node["$value"]
    refs = []
    if isinstance(val, str):
        refs = re.findall(r"\{([^{}]+)\}", val)
    elif isinstance(val, dict):
        for part in val.values():
            if isinstance(part, str):
                refs += re.findall(r"\{([^{}]+)\}", part)
    for ref in refs:
        resolve(ref, own)

out = json.dumps(tokens, indent=2) + "\n"
(HERE / "tokens.json").write_text(out)
print("wrote tokens.json", len(core_paths), "core", len(light_paths), "light")
