#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from apollographql.com on 2026-11-10:
  raw/css-vars.json          every custom property the Next.js/Tailwind build declares, binned by
                             owner, plus `resolved`: each name as the browser resolves it at :root
                             (tools/capture/vars.mjs). The site ships a real token layer —
                             --color-*, --font-*, --radius-*, --duration-* — so palette, radius and
                             duration leaves name the variable ("var").
  raw/component-tokens.json  the token tree: each leaf either names a variable ("var") whose value
                             is read from css-vars.json's resolved map — or carries a measured
                             value and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

apollographql.com paints two themes across its pages: dark navy/near-black marketing surfaces
(home, graphos, pricing, customers, why-apollo) and light surfaces (blog, contact-sales top). The
stylesheet's [data-theme="dark"] block re-binds the semantic --color-* names for dark sections.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations, looked up by name. vars.mjs resolves each custom property on a live
# :root, so DECL[name] is what the browser actually paints.
DECL = {n: v.get("value", v["raw"]) for n, v in V["resolved"].items()}


def norm_color(v):
    """#rgb, #rrggbb, #rrggbbaa, rgb(), rgba(), hsla() -> #rrggbb or rgba(r, g, b, a)."""
    v = v.strip().lower()
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
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a == 1 else "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    m = re.fullmatch(r"hsla?\(\s*0\s*,\s*0%\s*,\s*([\d.]+)%\s*(?:,\s*([\d.]+))?\)", v)
    if m:
        lvl = round(float(m.group(1)) * 2.55)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    """Refuse a value that is not the DTCG type it claims. An alias is checked by the alias pass."""
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val) if not str(val).startswith("{") else None
    if ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "gradient":
        for stop in val:
            if not str(stop["color"]).startswith("{"):
                norm_color(stop["color"])
            if not 0 <= stop["position"] <= 1:
                raise ValueError(f"{path}: gradient position {stop['position']!r}")


# The app stylesheet declares [data-theme="dark"] overrides inside @layer
# utilities. vars.mjs bins them under theme[]; resolve each override's raw
# declaration (often var(--x)) against the :root resolved map.
DARK = {}
for bin_ in V.get("theme", []):
    if bin_.get("selector") == '[data-theme="dark"]':
        DARK = dict(bin_.get("properties", {}))
VAR_REF = re.compile(r"^var\((--[A-Za-z0-9_-]+)\)$")


def resolve_dark(name):
    raw = DARK[name]
    m = VAR_REF.match(raw.strip())
    if m and m.group(1) in DECL:
        return DECL[m.group(1)]
    m = re.search(r"hsla?\(\s*var\((--[A-Za-z0-9_-]+)\)\s*,\s*([\d.]+)\s*\)", raw)
    if m and m.group(1) in DECL:
        hsl = DECL[m.group(1)]  # "H, S%, L%" triple
        parts = [p.strip() for p in str(hsl).split(",")]
        if len(parts) == 3:
            return f"hsla({parts[0]}, {parts[1]}, {parts[2]}, {m.group(2)})"
    return raw


def leaf(path, spec):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if spec.get("theme") == "dark":
            if name not in DARK:
                raise KeyError(f"{path}: {name} is not declared in the [data-theme=\"dark\"] block")
            val = resolve_dark(name)
            src = f"css-var {name} [data-theme=dark]"
        else:
            if name not in DECL:
                raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json")
            val = DECL[name]
            src = f"css-var {name}"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty in ("fontWeight", "number") and isinstance(val, str):
        m = re.fullmatch(r"calc\((-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\)", val)
        if m:  # Tailwind v4 emits line-heights as calc(a/b) ratios
            val = round(float(m.group(1)) / float(m.group(2)), 4)
        elif re.fullmatch(r"-?\d+(\.\d+)?", val):
            val = float(val) if "." in val else int(val)
    if ty == "gradient" and isinstance(val, str):
        m = re.fullmatch(r"linear-gradient\(\s*(\d+)deg\s*,\s*(.+)\s*\)", val)
        if m:
            stops = []
            for part in m.group(2).split(","):
                cm = re.match(r"\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|[a-zA-Z]+)\s*([\d.]+)%\s*$", part)
                if not cm:
                    raise ValueError(f"{path}: cannot parse gradient stop {part!r}")
                stops.append({"color": cm.group(1), "position": round(float(cm.group(2)) / 100, 4)})
            val = stops
            spec = {**spec, "angle": int(m.group(1))}
    if ty == "cubicBezier" and isinstance(val, str):
        m = re.fullmatch(r"cubic-bezier\(\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\)", val)
        if m:
            val = [float(x) for x in m.groups()]
    if ty == "duration" and isinstance(val, str):
        m = re.fullmatch(r"(\d*\.?\d+)s", val)  # the site's vars are seconds; DTCG wants ms
        if m:
            val = f"{round(float(m.group(1)) * 1000)}ms"
    if ty == "dimension" and isinstance(val, str):
        if re.fullmatch(r"-?\d+(\.\d+)?", val):
            val += "px"
        elif re.fullmatch(r"-?\.\d+(px|rem)", val):  # "-.41px" -> "-0.41px"
            val = ("-0" + val[1:]) if val.startswith("-") else "0" + val
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    if spec.get("responsive"):
        t["$extensions"]["responsive"] = spec["responsive"]
    if spec.get("angle"):
        t["$extensions"]["angle"] = spec["angle"]
    return t


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node)
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"])
# The spec's top-level "component" section holds the measured component values;
# in the output it is a group inside the core set (core.component.*).
if "component" in SPEC:
    core["component"] = build(SPEC["component"])
light = build(SPEC["light"])
dark = build(SPEC["dark"]) if "dark" in SPEC else {}


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)} | {n for n, _ in tokens_of(light)} | {n for n, _ in tokens_of(dark)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for n, t in list(tokens_of(core)) + list(tokens_of(light)) + list(tokens_of(dark)):
    for a in aliases(t["$value"]):
        if a not in NAMES:
            raise KeyError(f"{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The blog and contact-sales light surfaces"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The marketing pages' dark navy/near-black sections; the stylesheet re-binds the semantic --color-* names under [data-theme=dark]"},
    ] if dark else [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only theme painted"},
    ],
}
if dark:
    tokens["dark"] = dark
    tokens["$metadata"] = {"tokenSetOrder": ["core", "light", "dark"]}
else:
    tokens["$metadata"] = {"tokenSetOrder": ["core", "light"]}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
