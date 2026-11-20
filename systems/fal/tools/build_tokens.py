#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from fal.ai on 2026-11-14:
  raw/css-vars.json          the custom properties fal.ai's three signed-out
                             surfaces declare, resolved per pass by
                             tools/capture/vars.mjs: marketing (the Webflow
                             pages' --brand-colors--*/--size-* layer),
                             appLight/appDark (the Next.js app's Tailwind
                             token layer: --color-* scales, the
                             --primary-*/--secondary-*/--error-*/--info-*/
                             --success-*/--warning-*/--neutral-*/--lightblue-*
                             ramps, the semantic --surface-*/--content-*/
                             --stroke-*/--overlay-*/--shadow-*/--badge-*/
                             --accent-* roles, --product-banner-*, --chart-*,
                             the --text-*/--tracking-*/--leading-* type layer,
                             --radius-*/--spacing/--ease-*/--animate-*/
                             --breakpoint-*/--container-*) and
                             docsLight/docsDark (the fumadocs layer:
                             --primary/-light/-dark, --gray-*, --background-*,
                             --font-family-*-custom, --twoslash-*)
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py): each leaf either
                             names a variable ("var") resolved per theme, or carries a measured
                             value and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name> (<pass>)" or "measured <where>".

fal.ai paints three surfaces signed out: the single-theme Webflow marketing
pages (/, /pricing, /serverless, /contact-sales), the Next.js app (/explore,
/models/*, /login) themed by html.light|html.dark through
prefers-color-scheme, and the fumadocs docs (/docs/*) on their own layer.
tokens.json holds core, light and dark: core carries the theme-invariant
scales (app scales + marketing palette + docs palette), light resolves the
semantic names to the app-light values (with the marketing and docs-light
passes folded in for surface-only names), dark to the app-dark values, and
the measured roles alias the declarations they match.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import colorsys, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations per theme. vars.mjs resolves each surface's
# stylesheet into a pass — the light set merges the app-light pass with the
# docs-light and marketing passes for surface-only names (the app layer wins
# on collisions), the dark set the app-dark and docs-dark passes.
DECL = {"light": {}, "dark": {}}
for _pass, _theme in (("appLight", "light"), ("appDark", "dark"),
                      ("docsLight", "light"), ("docsDark", "dark"),
                      ("marketing", "light")):
    for _n, _v in V["resolved"].get(_pass, {}).items():
        DECL[_theme].setdefault(_n, _v.get("value", _v["raw"]) if isinstance(_v, dict) else _v)


def norm_color(v):
    """#rgb, #rrggbb, #rrggbbaa, the vars.mjs #rr,gg,bb form, raw `R G B` and
    `H S% L%` triplets (fal keeps its scales unwrapped), rgb()/rgba()/hsla()
    -> #rrggbb or rgba(r, g, b, a). Anything else (lab/oklch/… strings that
    only matched a loose colour test) passes through unchanged."""
    v = v.strip().lower()
    # The committed raw/css-vars.json was written before vars.mjs joined its hex digits
    # ("#9b,9b,9b"); the capture script is fixed, and this reading stays until a recapture.
    m = re.fullmatch(r"#([0-9a-f]{2}),([0-9a-f]{2}),([0-9a-f]{2})", v)
    if m:
        return "#" + "".join(m.groups())
    m = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", v)
    if m and all(int(x) <= 255 for x in m.groups()):
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    m = re.fullmatch(r"(-?[\d.]+)\s+([\d.]+)%\s+([\d.]+)%", v)
    if m:
        h, s, l = (float(x) for x in m.groups())
        r, g, b = colorsys.hls_to_rgb((h % 360) / 360, l / 100, s / 100)
        return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))
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
    return v  # a colour function string this does not decompose is kept verbatim


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")
SHADOWISH = re.compile(r"^(inset\s+)?(#[0-9a-f]{2}(,[0-9a-f]{2}){2}|#[0-9a-f]{3,8}|rgba?\(|hsla?\(|(ok)?lab\(|(ok)?lch\(|inset)")


def parse_shadow(v):
    """CSS `box-shadow` text -> the DTCG shadow layer list. fal resolves its
    --shadow-* vars as `rgba(…) x y blur [spread]` lists (leading colour);
    each layer keeps its inset flag and colour."""
    layers = []
    for part in re.split(r",\s*(?![^()]*\))", v):
        part = part.strip()
        # Chromium writes a computed inset last ("rgba(...) 0px 1px 0px 0px inset"); a declaration
        # may put it first. Either way the layer is inset.
        inset = bool(re.search(r"(^|\s)inset(\s|$)", part))
        part = re.sub(r"(^|\s)inset(?=\s|$)", " ", part).strip()
        col = None
        for pat in (r"^(#[0-9a-f]{2}(?:,[0-9a-f]{2}){2}|#[0-9a-f]{3,8})\s+",
                    r"^(rgba?\([^)]*\)|hsla?\([^)]*\)|(?:ok)?lab\([^)]*\)|(?:ok)?lch\([^)]*\))\s+",
                    r"\s+(#[0-9a-f]{2}(?:,[0-9a-f]{2}){2}|#[0-9a-f]{3,8})$",
                    r"\s+(rgba?\([^)]*\)|hsla?\([^)]*\)|(?:ok)?lab\([^)]*\)|(?:ok)?lch\([^)]*\))$"):
            m = re.search(pat, part)
            if m:
                col = m.group(1)
                part = (part[: m.start()] + part[m.end():]).strip()
                break
        words = part.split()
        nums = [w if re.search(r"(px|rem)$", w) else w + "px" for w in words if re.fullmatch(r"-?\d*\.?\d+(?:px|rem)?", w)]
        if len(nums) < 2 or len(nums) != len(words):
            raise ValueError(f"shadow layer is not 2-4 lengths and a colour: {part!r}")
        if col is None:
            raise ValueError(f"shadow layer has no colour: {part!r}")
        layer = {"offsetX": nums[0], "offsetY": nums[1],
                 "blur": nums[2] if len(nums) > 2 else "0px",
                 "spread": nums[3] if len(nums) > 3 else "0px",
                 "color": col}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    return layers


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
    if ty == "shadow" and isinstance(val, str):
        val = parse_shadow(val)
        for layer in val:
            layer["color"] = norm_color(layer["color"]) if not str(layer["color"]).startswith("{") else layer["color"]
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


core = build(SPEC["core"], "light")  # scales are theme-independent
light = build(SPEC["light"], "light")
dark = build(SPEC["dark"], "dark")
# The component tokens live in their own top-level spec tree but are
# theme-independent measured geometry (sidebar width, player-bar height,
# field heights), so they hang off core and reach both themes.
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
         "$description": "The light surface: the Webflow marketing pages (/, /pricing, /serverless, /contact-sales) are single-theme and the app surface paints html.light under a light prefers-color-scheme; the docs layer resolves light the same way. The marketing and docs-light passes are folded into this set for surface-only names."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The dark surface: the app pages (/explore, /models/*, /login) paint html.dark under a dark prefers-color-scheme, and the docs layer resolves its own dark pass; the docs-dark pass is folded into this set for docs-only names. fal ships no manual theme toggle on the app surface."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
    print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
