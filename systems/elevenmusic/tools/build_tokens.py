#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from elevenmusic.io on the capture date:
  raw/css-vars.json          the custom properties elevenmusic.io's stylesheets
                             declare — the shadcn-style semantic layer
                             (--background/--foreground/--card/--primary/
                             --muted/--border/--sidebar-*) plus the app's own
                             --surface-*, --lighten-*, --darken-*, --lift-*,
                             --composer-* and --gray-alpha-* extensions and the
                             Tailwind --color-* / --text-* / --radius-* scales,
                             read from the same-origin Next.js bundles and
                             resolved once per painted theme (light and dark)
                             by tools/capture/vars.mjs
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py):
                             each leaf either names a variable ("var") resolved
                             per theme or carries a measured value and the
                             measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

elevenmusic.io paints dark by default (html.dark, color-scheme: dark); the
footer's System/Light/Dark control remaps the same roles to a warm-paper
light theme. The export holds core, light and dark: scales that read
identically in both themes live in core, and the re-bound roles live in the
two theme sets (the --lighten-* white-alpha ramp resolves in the dark pass
only).

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations per theme. vars.mjs resolves each custom property on
# two probe documents: the page once painted light (:root) and once dark
# (.dark / html.dark — the app's default paint). DECL[theme][name] is what the
# browser paints there. A leaf may set "resolve": "<pass>" to look its var up
# on a different pass than the theme it sits in.
DECL = {t: {n: v.get("value", v["raw"]) for n, v in V["resolved"][t].items()}
        for t in V["resolved"]}


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


class NotTokenised(Exception):
    """A value DTCG cannot hold under its type; listed in the set's $extensions.notTokenised."""


# A DTCG dimension holds px or rem. The declared em tracking (which scales with
# the text it sits on) has no DTCG form, so it is listed under notTokenised with
# its value instead of being published as a dimension strict consumers reject.
DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")
EM = re.compile(r"-?(\d+(\.\d+)?|\.\d+)em")


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


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        surface = spec.get("resolve", theme)
        if name not in DECL[surface]:
            raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json ({surface})")
        val = DECL[surface][name]
        src = f"css-var {name} ({surface})"
        if spec.get("source"):
            src += "; " + spec["source"]
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
    if ty in ("fontWeight", "number") and isinstance(val, str):
        m = re.fullmatch(r"calc\((-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\)", val)
        if m:  # Tailwind v4 emits line-heights as calc(a/b) ratios
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
        elif isinstance(val, str) and EM.fullmatch(val.strip()):
            raise NotTokenised("an em length, relative to the element's own font size; a DTCG dimension holds px or rem")
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    if spec.get("responsive"):
        t["$extensions"]["responsive"] = spec["responsive"]
    if spec.get("angle"):
        t["$extensions"]["angle"] = spec["angle"]
    return t


def is_leaf(node):
    return isinstance(node, dict) and "type" in node and ("value" in node or "var" in node)


def build(node, theme, path="", skipped=None):
    """The DTCG tree for a spec subtree. A leaf whose value DTCG cannot hold is left out and
    recorded in `skipped` (the set's $extensions.notTokenised) with its value and why."""
    if is_leaf(node):
        return leaf(path, node, theme)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        p = f"{path}.{k}" if path else k
        try:
            sub = build(v, theme, p, skipped)
        except NotTokenised as e:
            raw = DECL[v.get("resolve", theme)].get(v["var"]) if "var" in v else v["value"]
            skipped.append({"name": p, "value": raw, "source": f"css-var {v['var']}" if "var" in v else v["source"],
                            "why": str(e)})
            continue
        if sub or not v or is_leaf(v):  # a group left empty only by skipped leaves is dropped
            out[k] = sub
    return out


SKIPPED = {"core": [], "light": [], "dark": []}
core = build(SPEC["core"], "light", skipped=SKIPPED["core"])  # scales are theme-independent
light = build(SPEC["light"], "light", skipped=SKIPPED["light"])
dark = build(SPEC["dark"], "dark", skipped=SKIPPED["dark"])
# The component tokens live in their own top-level spec tree; they are
# geometry and type readings (theme-independent), exported under
# light.component.* to keep the usual set layout.
light["component"] = build(SPEC["component"], "light", "component", SKIPPED["light"])
for name, tree in (("core", core), ("light", light), ("dark", dark)):
    if SKIPPED[name]:
        tree["$extensions"] = {"notTokenised": SKIPPED[name]}


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)}
NAMES_L = NAMES | {n for n, _ in tokens_of(light)}
NAMES_D = NAMES | {n for n, _ in tokens_of(dark)}


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
for n, t in list(tokens_of(dark)):
    for a in aliases(t["$value"]):
        if a not in NAMES_D:
            raise KeyError(f"dark.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The light theme: the footer's theme control remaps the roles to a warm-paper field (#fdfcfb) with warm-grey alphas."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The default paint (html.dark): true-black field, white-alpha ramps and the --lighten-* overlay steps that resolve in this pass only."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
