#!/usr/bin/env python3
"""Build tokens.json from jace.ai readings taken on 2026-11-18.

Sources:
  raw/css-vars.json   every custom property the marketing stylesheet declares,
                      resolved twice: html.light (the published light override,
                      :root:where(.light)) and bare :root (the dark product
                      theme the sign-in page paints).
  raw/motion.json     motion-probe.mjs, folded in by motion.py.

The marketing site (jace.ai) paints a light cream page with Tailwind utilities
(Geist Sans, Gelica, #2d2d2d). It still ships the product token block. The
product (app.jace.ai) paints the dark :root. Both themes are tokenised from
the declared custom properties, not from screenshots.

Tailwind's default palette (--primitives-tailwind-colors-*) is left out of
the core colour group. Jace's own ramps (sand, obsidian, lemon, ember,
deepsea) and the semantic names are kept.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motion  # noqa: E402

V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]
DATE = "2026-11-18"
SRC = "raw/css-vars.json, jace.ai stylesheet, " + DATE


def lin(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def lab_rgb(L, a, b):
    """CSS lab() to 8-bit sRGB. CSS Lab is CIE Lab on the D50 white with L in 0..100 (a
    percentage reads the same), so XYZ is taken on D50 and Bradford-adapted to D65 before the
    sRGB matrix. L is never rescaled: lab(0.5 ...) is a near-black, not 50% lightness."""
    fy = (L + 16) / 116
    fx = fy + (a / 500)
    fz = fy - (b / 200)

    def f_inv(t):
        return t ** 3 if t > 6 / 29 else 3 * (6 / 29) ** 2 * (t - 4 / 29)
    X = 0.96422 * f_inv(fx)
    Y = 1 * f_inv(fy)
    Z = 0.82521 * f_inv(fz)
    # XYZ (D50) -> linear sRGB through the Bradford-adapted matrix
    rgb = [
        3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z,
        -0.9787684 * X + 1.9161415 * Y + 0.0334540 * Z,
        0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z,
    ]
    return [round(min(1, max(0, lin(x))) * 255) for x in rgb]


def color(c):
    c = (c or "").strip()
    m = re.fullmatch(r"rgb\((\d+), (\d+), (\d+)\)", c)
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    m = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", c)
    if m:
        a = round(float(m.group(4)), 3)
        if a >= 1:
            return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
        return "rgba(%d, %d, %d, %s)" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), "%g" % a)
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", c)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"#([0-9a-fA-F]{3})", c)
    if m:
        return "#" + "".join(ch * 2 for ch in m.group(1).lower())
    m = re.fullmatch(r"#([0-9a-fA-F]{8})", c)
    if m:
        h = m.group(1)
        rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        a = round(int(h[6:8], 16) / 255, 3)
        if a >= 1:
            return "#%02x%02x%02x" % rgb
        return "rgba(%d, %d, %d, %s)" % (*rgb, "%g" % a)
    m = re.fullmatch(r"lab\(([-\d.]+%?) ([-+\d.]+) ([-+\d.]+)(?: / ([\d.]+%?))?\)", c)
    if m:
        L = float(m.group(1).rstrip("%"))
        rgb = lab_rgb(L, float(m.group(2)), float(m.group(3)))
        alpha = m.group(4)
        if not alpha:
            return "#%02x%02x%02x" % tuple(rgb)
        a = float(alpha.rstrip("%")) / 100 if alpha.endswith("%") else float(alpha)
        a = round(a, 3)
        if a >= 1:
            return "#%02x%02x%02x" % tuple(rgb)
        return "rgba(%d, %d, %d, %s)" % (*rgb, "%g" % a)
    return None


def dim_from_raw(raw):
    raw = (raw or "").strip()
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", raw)
    if m:
        return "%grem" % round(float(m.group(1)), 4)
    m = re.fullmatch(r"(-?\d*\.?\d+)px", raw)
    if m:
        return "%gpx" % round(float(m.group(1)), 3)
    if raw in ("0", "0px"):
        return "0px"
    return None


def tok(value, typ, evidence="Measured", note=None):
    ext = {"source": {"evidence": evidence, "capture": SRC}}
    if note:
        ext["source"]["note"] = note
    return {"$value": value, "$type": typ, "$extensions": ext}


def alias(path, typ, note=None):
    return tok("{" + path + "}", typ, evidence="Derived", note=note or "alias of a measured custom property")


def put(group, parts, token):
    node = group
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = token


def split_top(v, sep=","):
    """Split on sep outside parentheses: rgba(0, 0, 0, .1) stays whole."""
    out, depth, cur = [], 0, ""
    for ch in v:
        depth += ch == "("
        depth -= ch == ")"
        if ch == sep and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return out + [cur.strip()] if cur.strip() else out


def shadow_layers(v):
    """A computed box-shadow ("rgba(...) 0px 2px 4px -1px, ...", inset anywhere) as DTCG shadow
    layers. Raises on a layer it cannot read instead of guessing."""
    layers = []
    for layer in split_top(v):
        words = split_top(layer, " ")
        inset = "inset" in words
        words = [w for w in words if w != "inset"]
        colours = [w for w in words if not re.fullmatch(r"-?[\d.]+(px)?", w)]
        lengths = [w if w.endswith("px") else w + "px" for w in words if re.fullmatch(r"-?[\d.]+(px)?", w)]
        if len(colours) != 1 or not 2 <= len(lengths) <= 4:
            raise ValueError(f"cannot read shadow layer: {layer!r}")
        lengths += ["0px"] * (4 - len(lengths))
        if not color(colours[0]):
            raise ValueError(f"cannot read shadow colour: {colours[0]!r}")
        out = {"color": color(colours[0]), "offsetX": lengths[0], "offsetY": lengths[1],
               "blur": lengths[2], "spread": lengths[3]}
        if inset:
            out["inset"] = True
        layers.append(out)
    return layers


def unnest(node):
    """Lift tokens that sit inside another token out as siblings: --theme-primary and
    --theme-primary-foreground would make theme.primary hold theme.primary.foreground, where DTCG
    walkers stop at $value and never look. The child becomes theme.primary-foreground."""
    if not isinstance(node, dict):
        return node
    for k in list(node):
        if k.startswith("$"):
            continue
        v = unnest(node[k])
        if isinstance(v, dict) and "$value" in v:
            kids = [c for c in v if not c.startswith("$")]
            for c in kids:
                lifted = f"{k}-{c}"
                if lifted in node:
                    raise SystemExit(f"cannot lift {k}.{c}: {lifted} exists")
                node[lifted] = v.pop(c)
            if kids:
                unnest(node)
    return node


def name_parts(css_name):
    n = css_name[2:] if css_name.startswith("--") else css_name
    return [p for p in n.split("-") if p]


SKIP_PREFIXES = (
    "--primitives-tailwind-colors-",
    "--primitives-height-",
    "--primitives-width-",
    "--primitives-max-width-",
    "--primitives-opacity-",
    "--primitives-blur-",
    "--primitives-size-",
)


def keep(name):
    if any(name.startswith(p) for p in SKIP_PREFIXES):
        return False
    if name.startswith("--tw-") or name.startswith("--lightningcss"):
        return False
    return True


CORE_ROOTS = {
    "color", "space", "radiusPrimitive", "fontSize", "fontWeight", "lineHeight",
    "letterSpacing", "borderWidth", "font", "motionNamed", "radiusNamed",
}

# Longest prefix first. A name that matches none of these is still kept when
# it resolves to a colour, under component.<name>.
PREFIXES = (
    ("theme-new-colors-", "theme"),
    ("theme-new-alpha-", "alpha"),
    ("platform-new-text-", "type"),
    ("platform-new-border-radius-", "radius"),
    ("platform-new-border-", "platformBorder"),
    ("platform-new-gap-", "gap"),
    ("platform-new-", "platform"),
    ("primitives-color-", "color"),
    ("primitives-radius-", "radiusPrimitive"),
    ("primitives-spacing-", "space"),
    ("primitives-font-size-", "fontSize"),
    ("primitives-font-weight-", "fontWeight"),
    ("primitives-font-line-height-", "lineHeight"),
    ("primitives-font-letter-spacing-", "letterSpacing"),
    ("primitives-border-width-", "borderWidth"),
    ("button-background-", "button.background"),
    ("button-text-", "button.text"),
    ("button-border-", "button.border"),
    ("button-", "button"),
    ("text-body-color-", "text.body"),
    ("text-headline-color-", "text.headline"),
    ("text-label-color-", "text.label"),
    ("text-", "text"),
    ("surface-", "surface"),
    ("input-background-", "input.background"),
    ("input-text-", "input.text"),
    ("input-", "input"),
    ("sidebar-item-background-", "sidebar.item.background"),
    ("sidebar-item-", "sidebar.item"),
    ("sidebar-", "sidebar"),
    ("message-background-", "message.background"),
    ("message-text-", "message.text"),
    ("message-border-", "message.border"),
    ("message-", "message"),
    ("icon-color-", "icon"),
    ("icon-size-", "iconSize"),
    ("border-color-", "border"),
    ("elevation-", "elevation"),
    ("motion-", "motionNamed"),
    ("radius-", "radiusNamed"),
    ("font-family-", "font"),
    ("email-text-", "email"),
    ("context-menu-", "menu"),
    ("navigation-icon-", "nav.icon"),
    ("navigation-text-", "nav.text"),
    ("loader-background-", "loader"),
    ("autosuggest-background-", "autosuggest.background"),
    ("autosuggest-text-", "autosuggest.text"),
)


def semantic_path(name):
    n = name[2:]
    for prefix, root in PREFIXES:
        if n.startswith(prefix):
            rest = n[len(prefix):].replace("-", ".")
            return (root + "." + rest) if rest else root
    return None


def build_core():
    core = {}
    dark = RES["dark"]
    # colour primitives from dark (same values in both themes)
    for name, rec in sorted(dark.items()):
        if not keep(name):
            continue
        if not name.startswith("--primitives-color-"):
            continue
        col = color(rec.get("value") or "") or color(rec.get("raw") or "")
        if not col:
            continue
        path = semantic_path(name)
        put(core, path.split("."), tok(col, "color"))
    # spacing, radii, type sizes from raw rem
    for name, rec in sorted(dark.items()):
        if not keep(name):
            continue
        path = semantic_path(name)
        if not path:
            continue
        root = path.split(".")[0]
        if root in ("space", "radiusPrimitive", "fontSize", "borderWidth", "radiusNamed"):
            d = dim_from_raw(rec.get("raw"))
            if d:
                put(core, path.split("."), tok(d, "dimension"))
        elif root == "fontWeight":
            raw = str(rec.get("raw") or "").strip()
            if re.fullmatch(r"\d+", raw):
                put(core, path.split("."), tok(int(raw), "fontWeight"))
        elif root == "lineHeight":
            raw = str(rec.get("raw") or "").strip()
            if re.fullmatch(r"[\d.]+", raw):
                put(core, path.split("."), tok(float(raw), "number"))
            else:
                d = dim_from_raw(raw)
                if d:
                    put(core, path.split("."), tok(d, "dimension"))
        elif root == "letterSpacing":
            d = dim_from_raw(rec.get("raw")) or ("0px" if str(rec.get("raw")).strip() in ("0", "0px") else None)
            if d:
                put(core, path.split("."), tok(d, "dimension"))
        elif root == "font":
            put(core, path.split("."), tok(rec.get("value") or rec.get("raw"), "fontFamily"))
        elif root == "motionNamed":
            kind = rec.get("kind")
            if kind == "duration":
                ms = motion.parse_time(rec.get("value") or rec.get("raw"))
                if ms is not None:
                    put(core, path.split("."), tok(motion.ms_str(ms), "duration"))
            elif kind == "easing":
                bez = motion.easing_bezier(rec.get("value") or rec.get("raw"))
                if bez:
                    put(core, path.split("."), tok(bez, "cubicBezier"))
    # marketing families measured on the live page, not in the product token block
    live = V.get("liveMarketing") or {}
    put(core, ["font", "marketingSans"], tok(
        live.get("bodyFont") or "GeistSans, \"GeistSans Fallback\"", "fontFamily",
        note="computed font-family on body at jace.ai/"))
    put(core, ["font", "marketingDisplay"], tok(
        live.get("h1Font") or "gelica, \"gelica Fallback\"", "fontFamily",
        note="computed font-family on h1 at jace.ai/"))
    put(core, ["color", "marketing", "ink"], tok("#2d2d2d", "color", note="computed body color rgb(45, 45, 45) on jace.ai/"))
    put(core, ["color", "marketing", "onDark"], tok("#f6f6f6", "color", note="computed color of the Get started pill on jace.ai/"))
    put(core, ["color", "marketing", "page"], tok("#fffefd", "color", note="sand-50, the cream the marketing sections sit on; body itself is transparent"))
    return core


def build_theme(theme):
    recs = RES[theme]
    sem = {}
    not_tok = []
    for name, rec in sorted(recs.items()):
        if not keep(name):
            continue
        if name.startswith("--primitives-"):
            continue
        path = semantic_path(name)
        if not path:
            # still keep a resolved colour under component.<dashed-name>
            if rec.get("kind") == "color":
                col = color(rec.get("value") or "") or color(rec.get("raw") or "")
                if col and not name.startswith("--color-"):
                    put(sem, ["component", name[2:].replace("-", ".")], tok(col, "color", note=name))
            continue
        root = path.split(".")[0]
        if root in CORE_ROOTS:
            continue
        kind = rec.get("kind")
        raw = rec.get("raw") or ""
        if kind == "color" or (kind == "other" and raw.startswith("#")):
            col = color(rec.get("value") or "") or color(raw)
            if col:
                put(sem, path.split("."), tok(col, "color", note=name))
            else:
                not_tok.append(name + " " + str(rec.get("value") or raw)[:40])
        elif kind == "shadow":
            put(sem, path.split("."), tok(shadow_layers(rec.get("value")), "shadow", note=name))
        elif kind == "dimension":
            put(sem, path.split("."), tok(rec.get("value"), "dimension", note=name))
        elif kind == "fontFamily":
            put(sem, path.split("."), tok(rec.get("value") or raw, "fontFamily", note=name))
        else:
            d = dim_from_raw(raw)
            if d and root in ("type", "gap", "radius", "iconSize", "platform"):
                put(sem, path.split("."), tok(d, "dimension", note=name))
    if not_tok:
        sem.setdefault("$extensions", {})["notTokenised"] = not_tok[:30]
    return sem


def build():
    core = build_core()
    light = build_theme("light")
    dark = build_theme("dark")
    # motion group from the probe, product-free
    motion_path = RAW / "motion.json"
    if motion_path.exists():
        # motion.build returns (group, notTokenised); the list goes under core $extensions as
        # the kit does, never into core.motion itself.
        core["motion"], not_tokenised = motion.build(json.loads(motion_path.read_text()))
        if not_tokenised:
            core["$extensions"] = {"notTokenised": not_tokenised}
    for tree in (core, light, dark):
        unnest(tree)
    doc = {
        "$schema": "https://design-tokens.org/schema.json",
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
        "$extensions": {
            "source": SRC,
            "themes": {
                "light": "html.light so :root:where(.light, .light *) wins. The marketing site does not add .light; it paints with Tailwind utilities. These are the product's published light overrides.",
                "dark": "bare :root, the theme app.jace.ai/signin paints on 2026-11-18.",
            },
        },
    }
    return doc


def main():
    doc = build()
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=1) + "\n")
    print("wrote", out, "core groups", list(doc["core"]), "light", len(doc["light"]), "dark", len(doc["dark"]))


if __name__ == "__main__":
    main()
