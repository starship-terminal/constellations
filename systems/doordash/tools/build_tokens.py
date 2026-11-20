#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from archived doordash.com SSR pages on 2026-11-13:
  raw/css-vars.json          the custom properties DoorDash's stylesheets declare —
                             the prism token system on :where(.prism-theme)
                             (--base-* primitives, --usage-* semantic roles,
                             --comp-* component tokens), resolved by
                             tools/capture/vars.mjs in a probe carrying the real
                             sheets on a body.prism-theme scope
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py):
                             each leaf either names a variable ("var") resolved
                             from css-vars.json, is a {path} alias preserving the
                             prism comp→usage→base chain, or carries a measured
                             value and the measurement it came from ("source")
Every token carries $extensions.source.

doordash.com's consumer surface paints a single light theme — the prism
sheet ships sibling brand themes (deliveroo, plus, each light and dark)
under [data-dt-theme][data-dt-mode] scopes no doordash.com visitor gets —
so tokens.json holds `core` and `light` only. Careers (careersatdoordash.com) is a separate
WordPress/Tailwind stack documented in components.md, not tokenised.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# resolved.light: each custom property as the browser computes it on the
# prism scope at 1440 x 900 (colours as sRGB hex, lengths as px).
DECL = {n: v.get("value", v["raw"]) for n, v in V["resolved"]["light"].items()}


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
        norm_color(val)
    if ty == "shadow" and isinstance(val, list):
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+(\.\d+)?ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "gradient":
        for stop in val:
            if not str(stop["color"]).startswith("{"):
                norm_color(stop["color"])
            if not 0 <= stop["position"] <= 1:
                raise ValueError(f"{path}: gradient position {stop['position']!r}")


def split_top(s):
    """Split a computed list on its top-level commas (not the ones inside rgb(...))."""
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += (ch == "(") - (ch == ")")
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return out + [cur.strip()] if cur.strip() else out


SHADOW_COLOUR = re.compile(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}")


def parse_shadow(path, val):
    """A box-shadow string -> DTCG shadow layers. Paren-aware; keeps `inset` wherever it sits;
    accepts unitless 0 and negative lengths; raises on a layer it cannot read instead of dropping it.
    Fully transparent layers are left out, but a declaration made only of them (prism's
    elevation-none, `0px 0px 0px 0px #19191900`) keeps its transparent layer: DTCG has no "none"."""
    if val.strip() == "none":
        raise ValueError(f"{path}: shadow 'none' is not a DTCG shadow; declare the transparent layer instead")
    layers = []
    for part in split_top(val):
        inset = bool(re.search(r"(^|\s)inset(\s|$)", part))
        rest = re.sub(r"(^|\s)inset(\s|$)", " ", part).strip()
        m = SHADOW_COLOUR.search(rest)
        nums = (rest[:m.start()] + " " + rest[m.end():]).split() if m else []
        if not m or not 2 <= len(nums) <= 4 or not all(re.fullmatch(r"-?[\d.]+(px)?", n) for n in nums):
            raise ValueError(f"{path}: shadow layer did not parse: {part!r}")
        nums = [n if n.endswith("px") else n + "px" for n in nums] + ["0px"] * (4 - len(nums))
        layer = {"color": norm_color(m.group(0)), "offsetX": nums[0], "offsetY": nums[1], "blur": nums[2], "spread": nums[3]}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    seen = [l for l in layers if not (l["color"].startswith("rgba(") and l["color"].endswith(", 0)"))]
    return seen or layers[:1]


def leaf(path, spec):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL:
            raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json")
        val = DECL[name]
        src = spec.get("source") or f"css-var {name} (resolved on .prism-theme)"
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "cubicBezier" and isinstance(val, str):
        m = re.fullmatch(r"cubic-bezier\(\s*([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)\s*\)", val.strip())
        if m:
            val = [float("%g" % float(x)) for x in m.groups()]
        elif val.strip() in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
            val = {"ease": [.25, .1, .25, 1], "ease-in": [.42, 0, 1, 1], "ease-out": [0, 0, .58, 1],
                   "ease-in-out": [.42, 0, .58, 1], "linear": [0, 0, 1, 1]}[val.strip()]
    if ty == "shadow" and isinstance(val, str):
        val = parse_shadow(path, val)
    if ty in ("fontWeight", "number") and isinstance(val, str):
        m = re.fullmatch(r"calc\((-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\)", val)
        if m:
            val = round(float(m.group(1)) / float(m.group(2)), 4)
        elif re.fullmatch(r"-?\d+(\.\d+)?", val):
            val = float(val) if "." in val else int(val)
    if ty == "duration" and isinstance(val, str):
        m = re.fullmatch(r"([\d.]+)(m?s)", val.strip())
        if m:
            val = ("%g" % (float(m.group(1)) * (1 if m.group(2) == "ms" else 1000))) + "ms"
    if ty == "dimension":
        if isinstance(val, (int, float)):
            val = "%gpx" % val
        elif isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
            val = val.strip() + "px"
    if ty in ("number", "fontWeight") and ty == "fontWeight" and isinstance(val, float):
        val = int(val)
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    if spec.get("responsive"):
        t["$extensions"]["responsive"] = spec["responsive"]
    return t


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        if k == "$description":
            out[k] = v
            continue
        out[k] = build(v, f"{path}.{k}" if path else k)
    return out


core = build(SPEC["core"])
light = build(SPEC["light"])
# The component tokens live in their own top-level spec tree but belong to the
# exported theme the components were measured on: light.component.*
light["component"] = build(SPEC["component"])


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)}
NAMES_L = NAMES | {n for n, _ in tokens_of(light)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for n, t in list(tokens_of(core)):
    for a in aliases(t["$value"]):
        if a not in NAMES:
            raise KeyError(f"core.{n}: alias {{{a}}} points at nothing")
for n, t in list(tokens_of(light)):
    for a in aliases(t["$value"]):
        if a not in NAMES_L:
            raise KeyError(f"light.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only theme the signed-out consumer surface paints. No dark or "
                          "high-contrast variant is published on the captured pages; every "
                          "measurement was taken on the single light scheme."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if "$value" in v else count(v) for v in d.values() if isinstance(v, dict))


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)} tokens, 1 theme")
