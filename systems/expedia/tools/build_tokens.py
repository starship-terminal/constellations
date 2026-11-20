#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read through expedia.com's public surfaces on the capture date:
  raw/css-vars.json          every custom property the EGDS/UITK stylesheets declare, by stylesheet,
                             selector and media condition, sorted by owner (egds, palette, legacy,
                             app, uitk), plus each name as the browser resolves it on six roots:
                             the five themes seen on the pages (light-1, dark-1, dark-2,
                             marketing-3, bright-1) and the actually-painted one
  raw/component-tokens.json  the token tree tools/build_component_tokens.py writes: each leaf
                             either names a variable ("var") resolved through the cascade, or
                             carries a measured value and the component it came from ("source"),
                             or is a ready DTCG node for the type composites

expedia.com returns a 429 "Bot or Not?" wall to automation, so the DOM was a
Wayback snapshot of the public home and hotel-search pages served locally;
the CSS is Expedia's live travel-assets.com output (raw/css-vars.json, "pages").

The sheets layer three things. The literal role palettes (--light_1__primary
... the 57-colour sets for light-1, dark-1, dark-2, marketing-1..3, bright-1,
ai-local-1, romie and the global-loyalty tiers) are declared once on :root and
become core.color.palette. The --egds-* semantic names rebind per
[data-theme-light|dark="<id>"] selector to var(--<theme>__*) and become the
light/dark/dark2/marketing3/bright1 sets, aliasing into the palette where the
resolved literal matches. Everything theme-invariant (the --spacing__*,
--sizing__*, --corner_radius__*, --elevation__*, --duration__*, --easing__*
scales, the --egds-type-style-* type system, the older --font__*/--typography__*
scales and the ~2400 --<component>__* variables) is core, one token per
declaration, typed by its resolved value.

A token is an alias ({color.palette.light1.primary}) when its var() chain ends
at a literal a core token already holds. A value DTCG cannot carry (a
linear-gradient scrim, a url() font, an [object Object] composite, a keyword)
is kept under type "other" or listed in $extensions.notTokenised. The builder
refuses an alias that points at nothing and a dimension that is not one px or
rem length. Deterministic: same inputs, byte-identical output. Edit the raw
inputs or the builders, never tokens.json.
"""
import json
import math
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
RES = V["resolved"]

# token set -> EGDS theme id / [data-theme-*] value
THEMES = {"light": "light-1", "dark": "dark-1", "dark2": "dark-2",
          "marketing3": "marketing-3", "bright1": "bright-1"}
CORE_THEME = "light-1"

THEME_SEL = {tid: (f'[data-theme-light="{tid}"]', f'[data-theme-dark="{tid}"]') for tid in THEMES.values()}


def rank(decl, tid):
    """0 = declared for this theme's attribute, 1 = a global/root-ish block,
    2 = a narrower context (a component class or a media-prefixed rule)."""
    sel = decl["selector"]
    if sel in THEME_SEL.get(tid, ()):
        return 0
    if "data-theme-light" in sel or "data-theme-dark" in sel:
        return 2
    if ":root" in sel or sel in ("html", "body", "*", ".uitk-theme"):
        return 1
    return 2 if decl.get("media") else 1.5


# The winning declaration of each name per theme: theme attribute first, then
# the global blocks; for ties the later rule in stylesheet order wins (the
# cascade). Ranked per theme id; core resolves under light-1.
DECL = {}
for tid in list(THEMES.values()) + [CORE_THEME]:
    DECL.setdefault(tid, {})
for d in V["decls"]:
    for tid in DECL:
        r = rank(d, tid)
        cur = DECL[tid].get(d["name"])
        # later declaration of equal rank wins (stylesheet order in decls)
        if cur is None or r <= cur[0]:
            DECL[tid][d["name"]] = (r, d)


def resolve(theme, name, seen=None):
    """Follow var() chains inside the theme's winning declarations.
    Returns (literal value, chain of (name, selector))."""
    seen = seen or []
    if name in seen:
        raise ValueError("var() cycle: " + " -> ".join(seen + [name]))
    seen = seen + [name]
    d = DECL[theme].get(name) or DECL[CORE_THEME].get(name)
    if not d:
        raise KeyError(f"{name} is not declared in raw/css-vars.json")
    val, sel = d[1]["value"].strip(), d[1]["selector"]
    m = re.fullmatch(r"var\((--[\w-]+)\)", val)
    if m:
        v2, chain = resolve(theme, m.group(1), seen)
        return v2, chain + [(name, sel)]
    return val, [(name, sel)]


# ---------------------------------------------------------------- helpers


def srgb_chan(c):
    c = max(0.0, min(1.0, c))
    return round((12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055) * 255)


def oklab_rgb(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
    return [srgb_chan(x) for x in rgb]


def fmt_color(rgb, a):
    a = round(float(a), 3)
    if a >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %s)" % (rgb[0], rgb[1], rgb[2], "%g" % a)


def norm_color(v):
    """Any colour string -> '#rrggbb' or 'rgba(r, g, b, a)'."""
    v = v.strip().lower()
    if v == "transparent":
        return "rgba(0, 0, 0, 0)"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            return fmt_color((r, g, b), round(int(h[6:8], 16) / 255, 3))
        return fmt_color((r, g, b), 1)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        return fmt_color((int(r), int(g), int(b)), a)
    m = re.fullmatch(r"hsla?\(\s*([\d.]+)[,\s]+([\d.]+)%[,\s]+([\d.]+)%(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        h, s, l, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        h, s, l = float(h) / 360, float(s) / 100, float(l) / 100
        if s == 0:
            return fmt_color((round(l * 255),) * 3, a)
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q

        def hue(t):
            t %= 1
            if t < 1 / 6:
                return p + (q - p) * 6 * t
            if t < 1 / 2:
                return q
            if t < 2 / 3:
                return p + (q - p) * (2 / 3 - t) * 6
            return p
        return fmt_color([round(hue(h + d) * 255) for d in (1 / 3, 0, -1 / 3)], a)
    m = re.fullmatch(r"oklab\(\s*([-\d.e]+)\s+([-\d.e]+)\s+([-\d.e]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        return fmt_color(oklab_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3))),
                         float(m.group(4) or 1))
    m = re.fullmatch(r"color-mix\(in srgb,\s*(#[0-9a-f]{3,8}|[a-z]+)\s+([\d.]+)%,\s*transparent\)", v)
    if m:
        base, pct = norm_color(m.group(1)), float(m.group(2)) / 100
        h = base.lstrip("#")[:6]
        return fmt_color(tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), pct)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d*\.?\d+(px|rem|em)")
LEN = r"-?\d*\.?\d+(?:px|rem|em)"
COLOR_RE = r"#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|color\([^)]*\)|oklab\([^)]*\)|oklch\([^)]*\)|transparent"


def split_top(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


def shadow(v):
    """A box-shadow string -> DTCG shadow layers; None if it cannot be read."""
    layers = []
    for part in split_top(v):
        inset = bool(re.search(r"\binset\b", part))
        part = re.sub(r"\binset\b", "", part).strip()
        m = re.search(COLOR_RE, part)
        if not m:
            return None
        try:
            col = norm_color(m.group(0))
        except ValueError:
            return None
        nums = (part[:m.start()] + " " + part[m.end():]).split()
        if not 2 <= len(nums) <= 4 or not all(re.fullmatch(LEN, n) for n in nums):
            return None
        nums += ["0px"] * (4 - len(nums))
        if col == "rgba(0, 0, 0, 0)" and all(float(re.match(r"-?\d*\.?\d+", n).group()) == 0 for n in nums):
            continue
        layers.append({"color": col, "offsetX": nums[0], "offsetY": nums[1],
                       "blur": nums[2], "spread": nums[3], "inset": inset})
    return layers


def duration(v):
    m = re.fullmatch(r"([\d.]+)(m?s)", v.strip())
    if not m:
        raise ValueError("not a duration: " + v)
    return ("%g" % round(float(m.group(1)) * (1 if m.group(2) == "ms" else 1000), 3)) + "ms"


BEZIER_KW = {"linear": [0, 0, 1, 1], "ease": [0.25, 0.1, 0.25, 1], "ease-in": [0.42, 0, 1, 1],
             "ease-out": [0, 0, 0.58, 1], "ease-in-out": [0.42, 0, 0.58, 1]}


def bezier(v):
    v = v.strip()
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)\s*\)", v)
    if m:
        return [float("%g" % float(x)) for x in m.groups()]
    if v in BEZIER_KW:
        return BEZIER_KW[v]
    raise ValueError("not a cubic-bezier: " + v)


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if isinstance(val, dict):
        return  # composite (typography): aliases checked globally below
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px/rem/em length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(str(layer[k])):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
            norm_color(layer["color"])
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


# ---------------------------------------------------------------- leaves

NOT_TOKENISED = []


def leaf(path, spec, theme):
    tid = THEMES.get(theme, theme)
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        try:
            val, chain = resolve(tid, name)
        except KeyError:
            # not declared: fall back to the browser-resolved value
            val = RES[tid].get(name)
            if val is None:
                NOT_TOKENISED.append({"name": name, "set": theme, "why": "not declared"})
                return None
            chain = [(name, "resolved on the page")]
        raw = val.strip()
        if raw == "[object Object]" or raw.startswith("url(") or raw == "":
            NOT_TOKENISED.append({"name": name, "set": theme, "value": raw[:80],
                                  "why": "a composite or url() the resolver cannot read"})
            return None
        src = "css-var " + " -> ".join(f"{n} ({s})" for n, s in reversed(chain))
        if spec.get("source"):
            src += "; " + spec["source"]
        if ty == "color":
            try:
                nv = norm_color(raw)
            except ValueError:
                ty = "other"
                val = raw
            else:
                # an alias when the var() chain ends at a palette token that holds
                # this literal; else when any core token holds it (first wins)
                tok = NAME_ALIAS.get(chain[0][0]) if nv == ALIAS_VAL.get(NAME_ALIAS.get(chain[0][0])) else VAL_ALIAS.get(nv)
                val = "{" + tok + "}" if tok and tok != path else nv
        elif ty == "dimension":
            val = raw if DIM.fullmatch(raw) else None
            if val is None:
                NOT_TOKENISED.append({"name": name, "set": theme, "value": raw[:80], "why": "not a px/rem/em length"})
                return None
        elif ty == "duration":
            try:
                val = duration(raw)
            except ValueError:
                ty, val = "other", raw
        elif ty == "cubicBezier":
            val = bezier(raw)
        elif ty == "number":
            val = float(raw) if not raw.isdigit() else int(raw)
        elif ty == "percent":
            val = float(raw[:-1]) / 100
            ty = "number"
            src += " (declared %s)" % raw
        elif ty == "shadow":
            layers = shadow(raw)
            if layers is None:
                NOT_TOKENISED.append({"name": name, "set": theme, "value": raw[:80], "why": "shadow not readable"})
                return None
            if not layers:
                return None
            val = layers
        elif ty == "fontWeight":
            val = int(float(raw))
        else:
            val = raw
    else:
        val, src = spec["value"], spec.get("source", "")
        if ty == "color" and not str(val).startswith("{"):
            val = norm_color(str(val))
        if ty == "percent":
            val = float(str(val).rstrip("%")) / 100
            ty = "number"
        if ty == "dimension" and isinstance(val, (int, float)):
            val = ("%g" % val) + "px"
        if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
            val += "px"
        if ty == "fontWeight" and isinstance(val, str):
            val = int(float(val))
    if isinstance(val, (int, float)) and ty == "number":
        pass
    elif ty in ("fontWeight", "number") and isinstance(val, str) and val.lstrip("-").isdigit():
        val = int(val)
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    return t


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        if k == "$description":
            out[k] = v
            continue
        b = build(v, theme, f"{path}.{k}" if path else k)
        if b is not None:
            out[k] = b
    return out


# css-var name -> core token path (the palette leaves a theme set may alias
# into), and resolved value -> path for the literal fallback
NAME_ALIAS = {}


def _names(node, path=""):
    for k, v in node.items():
        if k.startswith("_"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "type" in v and "var" in v:
            NAME_ALIAS.setdefault(v["var"], p)
        elif isinstance(v, dict):
            _names(v, p)


_names(SPEC["core"])

ALIAS_VAL = {}
VAL_ALIAS = {}
core = build(SPEC["core"], "light")


def _vals(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            if isinstance(v["$value"], str) and not v["$value"].startswith("{"):
                ALIAS_VAL[prefix + k] = v["$value"]
                VAL_ALIAS.setdefault(v["$value"], prefix + k)
        elif isinstance(v, dict):
            _vals(v, prefix + k + ".")
_vals(core)

sets = {name: build(SPEC[name], name) for name in THEMES}


# ---------------------------------------------------------------- checks


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


CORE_TOK = dict(tokens_of(core))
for setname, tree in sets.items():
    names_ = dict(CORE_TOK)
    names_.update(dict(tokens_of(tree)))
    for n, t in tokens_of(tree):
        for a in aliases(t["$value"]):
            if a not in names_:
                raise KeyError(f"{setname}.{n}: alias {{{a}}} points at nothing")
            if t["$type"] in ("color", "dimension") and names_[a]["$type"] != t["$type"]:
                raise TypeError(f"{setname}.{n}: alias {{{a}}} is a {names_[a]['$type']}")

# a role only one theme has leaves the other unstyled
ref = {n for n, _ in tokens_of(sets["light"])}
for setname in THEMES:
    gap = ref ^ {n for n, _ in tokens_of(sets[setname])}
    if gap:
        print(f"warning: {setname} parity gap: {sorted(gap)[:10]}", file=sys.stderr)

desc_themes = {
    "light": "The signed-out theme expedia.com paints: body carries data-theme-light=\"light-1\" on every captured page (themeChecks in raw/css-vars.json).",
    "dark": "The values declared for data-theme-*=\"dark-1\": the dark role bindings. Not applied on the captured pages; kept for reference.",
    "dark2": "data-theme-*=\"dark-2\": a teal-grounded dark variant. Not applied on the captured pages.",
    "marketing3": "data-theme-*=\"marketing-3\": the pale-blue marketing palette, applied to the promo sections under the search form (the marketing-band component).",
    "bright1": "data-theme-*=\"bright-1\": the yellow Expedia-brand campaign palette. Seen on marketing surfaces.",
}
tokens = {
    "core": core,
    "$metadata": {"tokenSetOrder": ["core"] + list(THEMES)},
    "$themes": [{"id": s, "name": n, "selectedTokenSets": {"core": "source", s: "enabled"},
                 "$description": desc_themes[s]}
                for s, n in (("light", "Light (light-1)"), ("dark", "Dark (dark-1)"), ("dark2", "Dark 2 (dark-2)"),
                             ("marketing3", "Marketing (marketing-3)"), ("bright1", "Bright (bright-1)"))],
}
tokens.update(sets)
core["$extensions"] = {"notTokenised": NOT_TOKENISED}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for k, v in d.items() if not k.startswith("$")) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", *THEMES)}, "not tokenised:", len(NOT_TOKENISED))
