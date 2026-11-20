#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from getfernand.com, app.getfernand.com and help.getfernand.com:
  raw/css-vars.json          the custom properties the three public hosts'
                             stylesheets declare — the flat :root palette
                             (--white/--grey*/--black/--blue*/--orange*/
                             --red*/--green*/--border*), the app's
                             --viewport-height and scoped sidebar
                             overrides, and the body.dark-mode remaps the
                             docs site paints through its real "Switch to
                             dark mode" link (tools/capture/vars.mjs),
                             binned theme / app / vendor / utility
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py): each leaf either
                             names a variable ("var") resolved per theme, or carries a measured
                             value and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

Fernand's public surfaces share one palette declared on :root, with real
host-level divergence the sets keep honest: the app stylesheet declares the
same names with different values for --grey/--grey-medium/--grey-strong plus
--viewport-height and scoped overrides, and the docs site redeclares the
palette under body.dark-mode behind a real user-facing toggle. Sets:
  core      theme-independent scales (Inter + the measured type/shape/motion)
  light     the marketing/docs light palette and roles (marketing resolution)
  app       the SPA's own palette resolution and
            --viewport-height — a separate theme, not mixed into marketing light
  dark      the docs dark palette/roles, resolved under body.dark-mode
Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations per theme. vars.mjs resolves each custom property in a
# probe document carrying one host's real sheets: "light" is the marketing
# shell, "app" the SPA shell, "help" the docs shell in light, "dark" the docs
# shell under body.dark-mode (its real toggle) and "appDark" the SPA's
# declared-but-gated remap (unused: the app dark surface is never painted
# signed out, so no theme ships it — it stays in raw/css-vars.json as declared
# evidence). Each surface set resolves only its own host's declarations.
RV = V["resolved"]
def decl_of(*shells):
    out = {}
    for s in shells:
        for n, v in RV.get(s, {}).items():
            out[n] = v.get("value", v["raw"])
    return out
DECL = {
    "light": decl_of("light"),
    "help": decl_of("help"),
    "app": decl_of("app"),
    "dark": decl_of("dark"),
}


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


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL[theme]:
            raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json ({theme})")
        val = DECL[theme][name]
        src = f"css-var {name} ({theme})"
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
        if m:  # a calc(a/b) line-height ratio
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
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    if spec.get("responsive"):
        t["$extensions"]["responsive"] = spec["responsive"]
    if spec.get("angle"):
        t["$extensions"]["angle"] = spec["angle"]
    return t


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites)
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"], "light")  # scales + the canonical (marketing) palette
light = build(SPEC["light"], "light")
help_ = build(SPEC["help"], "help")
app = build(SPEC["app"], "app")
dark = build(SPEC["dark"], "dark")
# The component tokens live in their own top-level spec tree but are
# theme-independent measured geometry (header height, card widths, field
# heights, the launcher bubble size), so they hang off core and reach every
# theme.
core["component"] = build(SPEC["component"], "light")


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)}
NAMES_L = NAMES | {n for n, _ in tokens_of(light)}
NAMES_H = NAMES | {n for n, _ in tokens_of(help_)}
NAMES_A = NAMES | {n for n, _ in tokens_of(app)}
NAMES_D = NAMES | {n for n, _ in tokens_of(dark)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for setname, tree, names in (("core", core, NAMES), ("light", light, NAMES_L), ("help", help_, NAMES_H), ("app", app, NAMES_A), ("dark", dark, NAMES_D)):
    for n, t in list(tokens_of(tree)):
        for a in aliases(t["$value"]):
            if a not in names:
                raise KeyError(f"{setname}.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "help": help_,
    "app": app,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The marketing surface: getfernand.com paints this palette on :root (color-scheme: light, --grey-light #f4f5f7); it is the only surface the marketing site ships."},
        {"id": "help", "name": "Docs", "selectedTokenSets": {"core": "source", "help": "enabled"},
         "$description": "The docs light surface: help.getfernand.com declares the same palette names with its own resolutions (--grey-light #f7fafc, --grey-medium #5f667d, --border-strong #d1d5e6)."},
        {"id": "app", "name": "App", "selectedTokenSets": {"core": "source", "app": "enabled"},
         "$description": "The app surface: app.getfernand.com declares the same palette names with its own resolutions (--grey #e6e9eb, --grey-medium #5e6271, --grey-strong #9fa3b5) plus --viewport-height and scoped sidebar overrides; the signed-out /auth/login and /create forms paint it."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The docs dark surface: help.getfernand.com redeclares the palette under body.dark-mode behind its real 'Switch to dark mode' link (white #161618, black #f7f8f8); the SPA declares a parallel remap that is gated sign-in and was not painted."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "help", "app", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "help", "app", "dark")})
