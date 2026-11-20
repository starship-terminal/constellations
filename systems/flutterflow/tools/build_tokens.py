#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, all read from flutterflow.io on 2026-03-01:
  raw/css-vars.json          every custom property the site's Astro sheets declare, by stylesheet,
                             selector and @layer/@media context (tools/capture/vars.mjs), plus the
                             resolved passes: light and dark at 1440, both again at 390
  raw/component-tokens.json  the token tree: a leaf either names a variable ("var") whose value is
                             resolved per theme from css-vars.json, or carries a measured value and
                             the measurement it came from ("source")
  raw/motion.json            the motion probe (tools/capture/motion-probe.mjs), turned into
                             core.motion by tools/motion.py

flutterflow.io paints two themes: the footer theme switch writes ff-theme to localStorage and sets
html[data-theme]; :root[data-theme="dark"] and the prefers-color-scheme rule rebind every --ff-* and
the legacy page shorthand. The "themed" tree in component-tokens.json expands into the light and
dark sets, each resolved from that theme's own pass — never one theme guessed from the other.

Every token carries $extensions.source: "css-var <name> (<selector>)" or "measured <where>".

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motion

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
RES = V["resolved"]  # light | dark | light390 | dark390: name -> {raw, kind, value?}

# ---------------------------------------------------------------- declarations, for provenance
def decls_of(name):
    """Every declaration of a custom property, as (theme, selector-plus-context)."""
    out = []
    for d in V["ff"] + V["app"]:
        if name not in d.get("properties", {}):
            continue
        sel = d["selector"]
        ctx = " ".join(d.get("context") or [])
        theme = "dark" if 'data-theme="dark"' in sel else "media-dark" if "prefers-color-scheme: dark" in ctx \
            else "light" if 'data-theme="light"' in sel else "base"
        out.append((theme, f'{sel} ({ctx})' if ctx else sel))
    return out

DECLS = {}
for theme_map in RES.values():
    for n in theme_map:
        if n not in DECLS:
            DECLS[n] = decls_of(n)


def var_source(name, theme):
    """The selector to cite for a var in this set: the theme's own declaration first,
    the data-theme attribute rule before the OS-level prefers-color-scheme one."""
    opts = DECLS.get(name) or []
    pick = next((s for t, s in opts if t == theme), None) or \
        next((s for t, s in opts if t == "media-dark" and theme == "dark"), None) or \
        next((s for t, s in opts if t == "base"), None) or \
        (opts[0][1] if opts else "unresolved")
    return f"css-var {name} ({pick})"


def resolve(name, theme):
    e = RES[theme].get(name)
    if e is None:
        raise KeyError(f"{name} is not a flutterflow.io variable in raw/css-vars.json")
    return e.get("value") or e["raw"]


# ---------------------------------------------------------------- value helpers
def norm_color(v):
    """#rgb/#rrggbb/#rrggbbaa, rgb()/rgba(), hsla() -> #rrggbb or rgba(r, g, b, a)."""
    v = str(v).strip().lower()
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
    m = re.fullmatch(r"oklab\(\s*([\d.]+)\s+([-\d.e]+)\s+([-\d.e]+)(?:\s*/\s*([\d.]+))?\s*\)", v)
    if m:
        L, A, B, al = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.291485548 * B) ** 3
        gam = lambda x: 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
        r, g, b = (round(min(1, max(0, gam(c))) * 255) for c in
                   (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
                    -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
                    -0.0041960863 * l_ - 0.7034186147 * m_ + 1.707614701 * s_))
        a = float(al) if al is not None else 1
        return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def split_top(s):
    """Split a comma list on top-level commas only (rgba() carries commas inside)."""
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return [x.strip() for x in out]


COLOR_RE = r"(#[0-9a-fA-F]{3,8}|(?:rgba?|oklab|oklch|color|lab|lch)\([^)]*\))"


def shadow(v):
    """A computed box-shadow -> DTCG shadow layers."""
    layers = []
    for layer in split_top(v):
        m = re.match(COLOR_RE + r"\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?(\s+inset)?$", layer.strip())
        if not m:
            return None
        layers.append({"color": norm_color(m.group(1)), "offsetX": m.group(2) + "px",
                       "offsetY": m.group(3) + "px", "blur": m.group(4) + "px",
                       "spread": (m.group(5) or "0") + "px", "inset": bool(m.group(6))})
    return layers


def ms(v):
    m = re.fullmatch(r"([\d.]+)(m?s)", str(v).strip())
    return "%gms" % (float(m.group(1)) * (1000 if m.group(2) == "s" else 1)) if m else v


def bezier(v):
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.e]+)\s*,\s*([-\d.e]+)\s*,\s*([-\d.e]+)\s*,\s*([-\d.e]+)\s*\)", str(v).strip())
    if not m:
        raise ValueError("not cubic-bezier: " + str(v))
    return [float(x) for x in m.groups()]


# border declarations whose colour is a themed colour the sets already carry
BORDER_ALIAS = {"--ff-border-rule": "color.line", "--rule": "legacy.line-1"}


def border(path, raw, name):
    m = re.fullmatch(r"([\d.]+)px\s+(\w+)\s+(.+)", str(raw).strip())
    if not m:
        raise ValueError(f"{path}: border not readable: {raw!r}")
    col = ("{%s}" % BORDER_ALIAS[name]) if name in BORDER_ALIAS else norm_color(m.group(3))
    return {"width": m.group(1) + "px", "style": m.group(2), "color": col}


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "shadow":
        for layer in val:
            if not str(layer["color"]).startswith("{"):
                norm_color(layer["color"])
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
    if ty == "border":
        if not DIM.fullmatch(val["width"]):
            raise ValueError(f"{path}: border width {val['width']!r}")
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


def leaf(path, spec, theme):
    ty = spec["type"]
    ext = {}
    if "var" in spec:
        name = spec["var"]
        # provenance from the same pass as the value: a dark token cites the
        # dark resolution's declaration and its own 390-px pass, never light's
        own = RES[theme].get(name, {})
        raw = own.get("raw")
        val = resolve(name, theme)
        src = var_source(name, theme)
        if spec.get("source"):
            src += "; " + spec["source"]
        if raw and raw != val:
            ext["declared"] = raw
        r390 = RES.get(theme + "390", {}).get(name, {})
        if r390 and own and (r390.get("value") or r390["raw"]) != (own.get("value") or own["raw"]):
            ext["responsive"] = {"390px": r390.get("value") or r390["raw"]}
    else:
        name = None
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    elif ty == "dimension":
        val = str(val)
        if re.fullmatch(r"-?\d+(\.\d+)?", val):
            val += "px"
    elif ty == "duration":
        val = ms(val)
    elif ty == "cubicBezier":
        val = bezier(val)
    elif ty == "shadow":
        val = shadow(val) if not isinstance(val, list) else val
        if val is None:
            raise ValueError(f"{path}: shadow of {name} not readable")
    elif ty == "border":
        val = border(path, val, name)
    elif ty in ("fontWeight", "number"):
        val = int(val) if isinstance(val, str) and val.lstrip("-").isdigit() else (float(val) if isinstance(val, str) else val)
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    t["$extensions"].update(ext)
    if spec.get("description"):
        t["$description"] = spec["description"]
    return t


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


def merge(a, b):
    for k, v in b.items():
        a[k] = merge(a[k], v) if k in a and isinstance(a[k], dict) and isinstance(v, dict) and "$value" not in a[k] else v
    return a


# ---------------------------------------------------------------- core
core = build(SPEC["core"], "light")

# typography: the --ff-text-<role> shorthand vars (weight size/lh family) + the -tracking companions
TYPE_RE = re.compile(r"^(\d+)\s+(.+?)/(\S+)\s+(.+)$")  # the size may be a clamp() with spaces


def px_at(v, vw):
    """Resolve a px or vw length (or a clamp() of them) at a viewport width."""
    def one(x):
        x = x.strip()
        if x.endswith("px"):
            return float(x[:-2])
        if x.endswith("vw"):
            return float(x[:-2]) * vw / 100
        return float(x)
    m = re.fullmatch(r"clamp\(([^,]+),\s*([^,]+),\s*([^)]+)\)", v)
    if m:
        return min(max(one(m.group(2)), one(m.group(1))), one(m.group(3)))
    return one(v)


def fam_of(family):
    return "{fontFamily.mono}" if "mono" in family else "{fontFamily.sans}" if "Inter" in family else family


typo = {}
for name, e in sorted(RES["light"].items()):
    m = re.fullmatch(r"--ff-text-(.+)", name)
    if not m or name.endswith("-tracking"):
        continue
    mm = TYPE_RE.match(e["raw"])
    if not mm:
        continue
    role = m.group(1)
    weight, size, lh, family = mm.groups()
    fam = fam_of(family)
    tr = RES["light"].get(f"--ff-text-{role}-tracking", {}).get("raw", "normal")
    size1440 = "%gpx" % px_at(size, 1440)
    comp = {"fontFamily": fam, "fontSize": size1440, "lineHeight": lh, "fontWeight": int(weight),
            "letterSpacing": "0px" if tr == "normal" else tr}
    src = var_source(name, "light")
    t = {"$value": comp, "$type": "typography", "$extensions": {"source": src}}
    if size != size1440:
        t["$extensions"]["declared"] = e["raw"]
    # The 390 reading comes from the captured narrow declarations (RES["light390"]),
    # never the desktop shorthand evaluated at 390: the site rewrites sizes, line
    # heights, tracking and even weights at the narrow breakpoint, and fixed-px
    # roles change too (lede 19/30 -> 16/25). A role the narrow pass does not
    # redeclare keeps its desktop declaration, so only a clamp()/vw size still
    # needs evaluating at 390.
    over = {}
    mm390 = TYPE_RE.match((RES["light390"].get(name) or {}).get("raw") or "")
    if mm390:
        w390, s390, lh390, family390 = mm390.groups()
        c390 = {"fontFamily": fam_of(family390), "fontSize": "%gpx" % px_at(s390, 390),
                "lineHeight": lh390, "fontWeight": int(w390)}
        over = {k: v for k, v in c390.items() if comp[k] != v}
    elif size != size1440:
        s390 = "%gpx" % px_at(size, 390)
        if s390 != size1440:
            over["fontSize"] = s390
    tr390 = RES["light390"].get(f"--ff-text-{role}-tracking", {})
    tr390 = tr390.get("raw") or tr390.get("value")
    if tr390 is not None:
        ls390 = "0px" if tr390 == "normal" else tr390
        if ls390 != comp["letterSpacing"]:
            over["letterSpacing"] = ls390
    if over:
        t["$extensions"]["responsive"] = {"390px": over}
    # only display is the 66px home title; the 48px heading role has no
    # element reading of its own
    if name == "--ff-text-display":
        t["$extensions"]["measured"] = "raw/measurements.md#home-title (66px at 1440, -2.31px tracking)"
    typo[role] = t
typo["$description"] = ("The --ff-text-* type roles, parsed out of their font shorthands: display through "
                        "small, plus prompt. clamp() sizes are resolved at 1440 and the captured 390-px "
                        "declarations ride in $extensions.responsive; tracking is the companion "
                        "--ff-text-*-tracking var.")
core["typography"] = typo

# motion, as measured on the page (raw/motion.json via the probe; motion.py is product-free)
if (RAW / "motion.json").exists():
    core["motion"], motion_not_core = motion.build(json.loads((RAW / "motion.json").read_text()))

# ---------------------------------------------------------------- themed sets
light = merge(build(SPEC["themed"], "light"), build(SPEC.get("light", {}), "light"))
dark = merge(build(SPEC["themed"], "dark"), build(SPEC.get("dark", {}), "dark"))

# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
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


for set_name, tree in (("light", light), ("dark", dark)):
    NAMES = {n for n, _ in tokens_of(core)} | {n for n, _ in tokens_of(tree)}
    for n, t in tokens_of(tree):
        for a in aliases(t["$value"]):
            if a not in NAMES:
                raise KeyError(f"{set_name}.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "html[data-theme=light], or no ff-theme choice on a light OS"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "html[data-theme=dark]: the footer theme switch's Dark pick, or a dark OS with no stored choice"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
