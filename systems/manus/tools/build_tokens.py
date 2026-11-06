#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from manus.im/app on 2026-10-04 and refreshed on 2026-10-17:
  raw/css-vars.json          every custom property Manus's stylesheets declare, by file, selector and
                             enclosing condition (tools/capture/vars.mjs)
  raw/css-rules.json         utility-class values (named shadows, spacing, z-index, border widths,
                             focus and reduced-motion rules) and the shadows the measured components
                             paint (tools/capture/rules.py, added 2026-10-17)
  raw/components-computed.json  the measured components, for the `component` group of each theme
  raw/component-tokens.json  values that are not variables: measured on the real elements, each with
                             the measurement it came from ("source")

Manus declares its palette twice in one stylesheet, `:root` (light) and `.dark` (dark), and every
component colour is a var() of one of them. Those two blocks become the `light` and `dark` sets,
grouped by the role each name carries (text, background, border, icon, fill, function, button, tab,
shadow, accent, activity-indicator, illustration, game, misc). A name declared on `:root` and not on
`.dark` keeps its light value in dark, as the browser does. The seven accent palettes
(`.accent-custom[data-accent-color=...]`, light and dark pairs) are the `accent` group of each set.

`core` holds what does not change with the theme: the type scale (`--ui-font-size-*`,
`--ui-line-height-*`) as sizes, line heights and composite type styles; the density scale
(`--ui-density-*`, with the compact value Manus sets under `data-interface-density="compact"` in
`$extensions.compact`); font families; radii; durations and easings; and the measured layout.

A value the DTCG types cannot carry (a multi-layer background, a radial gradient, an env()) stays in
raw/css-vars.json and is listed under `$extensions.notTokenised` of the set, by name, so nothing is
silently dropped. Every token carries `$extensions.source`. Deterministic: same inputs, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
THEME_SHEET = "0l0v22wndw5xb.css"  # the chunk names changed between the 2026-10-04 read and the 2026-10-17 refresh
UI_SHEET = "1bc8iqysa6nev.css"
RULES = json.loads((RAW / "css-rules.json").read_text())
COMPS = json.loads((RAW / "components-computed.json").read_text())["components"]

rules = [r for r in V["rules"] if "selector" in r]


def block(selector, file=None, context=()):
    out = {}
    for r in rules:
        if r["selector"] == selector and (file is None or r["file"] == file) and tuple(r["context"]) == tuple(context):
            out.update(r["properties"])
    return out


LIGHT = block(":root", THEME_SHEET)
DARK = block(".dark", THEME_SHEET)
UI = block(":root", UI_SHEET)
COMPACT = block('html.is-desktop[data-interface-density="compact"]', UI_SHEET)
STANDARD = block('html.is-desktop[data-interface-density="standard"]', UI_SHEET)

ACCENTS = {}
for r in rules:
    m = re.fullmatch(r'(\.dark)?\.accent-custom\[data-accent-color="(\w+)"\]', r["selector"])
    if m and r["file"] == THEME_SHEET:
        ACCENTS.setdefault(m.group(2), {})["dark" if m.group(1) else "light"] = r["properties"]
ACCENT_ROLES = block(".accent-custom", THEME_SHEET)


# ---------- value parsing ----------

def norm_color(v):
    """#rgb/#rgba/#rrggbb/#rrggbbaa -> #rrggbb or rgba(r, g, b, a)."""
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if not m:
        raise ValueError("not a colour: " + v)
    h = m.group(1)
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    if len(h) == 8:
        a = round(int(h[6:8], 16) / 255, 3)
        if a != 1:
            return "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
    return "#%02x%02x%02x" % (r, g, b)


VAR = re.compile(r"var\(--([A-Za-z0-9-]+)\)")


def alias_of(name, sets):
    """{group.token} for a variable name, looked up in the given set trees."""
    for s in sets:
        path = s.get("_index", {}).get(name)
        if path:
            return "{" + path + "}"
    raise KeyError(f"alias to --{name}, which is not a token")


def parse_gradient(v):
    """linear-gradient(<angle>, <stop> <pos>, ...) with hex or var() stops -> (angle, stops)."""
    m = re.fullmatch(r"linear-gradient\((.*)\)", v.strip())
    if not m:
        return None
    parts = split_top(m.group(1))
    angle = "180deg"
    if re.fullmatch(r"-?[\d.]+deg", parts[0].strip()):
        angle = parts.pop(0).strip()
    stops = []
    for i, p in enumerate(parts):
        bits = p.strip().split()
        if len(bits) == 1:
            bits.append("%g%%" % (100 * i / max(1, len(parts) - 1)))
        col, pos = bits[0], bits[1]
        if not pos.endswith("%"):
            return None
        stops.append({"color": col, "position": round(float(pos[:-1]) / 100, 4)})
    return angle, stops


def split_top(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        if ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def parse_shadow(v):
    layers = []
    for part in split_top(v):
        bits = part.strip().split()
        inset = False
        if bits and bits[0] == "inset":
            inset = True
            bits = bits[1:]
        col = bits[-1]
        nums = bits[:-1]
        if len(nums) < 2 or len(nums) > 4 or not re.fullmatch(r"#[0-9a-f]{3,8}", col):
            return None
        nums += ["0"] * (4 - len(nums))
        layers.append({"offsetX": px(nums[0]), "offsetY": px(nums[1]), "blur": px(nums[2]), "spread": px(nums[3]), "color": norm_color(col), "inset": inset})
    return layers


def px(n):
    n = n.strip()
    if re.fullmatch(r"-?\d*\.?\d+", n):
        return ("%g" % float(n)) + "px"
    if re.fullmatch(r"-?\d*\.?\d+px", n):
        return ("%g" % float(n[:-2])) + "px"
    raise ValueError("not a px length: " + n)


# ---------- the themed sets ----------

GROUPS = [
    ("activity-indicator-", "activity-indicator"), ("illustration-", "illustration"), ("Button-", "button"),
    ("shadows-", "shadow"), ("shadow-", "shadow"), ("background-game-", "game"), ("border-game-", "game"),
    ("game-", "game"), ("text-game-", "game"), ("accent-", "accent"), ("text-", "text"), ("theme-text-", "text"),
    ("background-", "background"), ("border-", "border"), ("icon-", "icon"), ("function-", "function"),
    ("fill-", "fill"), ("tab-", "tab"), ("gradual-", "gradient"), ("gradient-", "gradient"), ("overlay-", "overlay"),
    ("ansi-", "ansi"), ("brand-", "brand"), ("invitation-", "background"),
]


def group_of(name):
    if name.startswith("theme-text-"):
        return "text", "theme-" + name[len("theme-text-"):]
    if name == "invitation-background":
        return "background", "invitation"
    if name == "logo-color":
        return "text", "logo"
    for prefix, g in GROUPS:
        if name.startswith(prefix):
            # game and illustration names keep their whole name, since the prefix is part of the meaning
            return g, name[len(prefix):]
    return "misc", name


def themed_set(decls, theme, fallback=None):
    """Turn one palette block into a token tree. Aliases resolve inside the same set; a name only
    the light block declares is copied into dark with the light value."""
    merged = {k[2:]: v for k, v in (fallback or {}).items()}
    merged.update({k[2:]: v for k, v in decls.items()})
    decls = {k[2:]: v for k, v in decls.items()}
    tree = {"_index": {}}
    not_tokenised = []
    pending = []
    for name, raw in merged.items():
        g, leaf_name = group_of(name)
        where = "dark" if name in decls and theme == "dark" else "light"
        src = f"css-var --{name} ({'.dark' if where == 'dark' else ':root'}, {THEME_SHEET})"
        if theme == "dark" and name not in decls:
            src += "; not redeclared for dark, so the light value applies"
        pending.append((name, g, leaf_name, raw, src))
    # first pass: literal values, so aliases can resolve in the second
    for name, g, leaf_name, raw, src in pending:
        tok = literal(raw, src)
        if tok is None:
            continue
        tree.setdefault(g, {})[leaf_name] = tok
        tree["_index"][name] = f"{g}.{leaf_name}"
    for name, g, leaf_name, raw, src in pending:
        if name in tree["_index"]:
            continue
        tok = with_aliases(raw, src, [tree])
        if tok is None:
            not_tokenised.append({"name": "--" + name, "value": raw})
            continue
        tree.setdefault(g, {})[leaf_name] = tok
        tree["_index"][name] = f"{g}.{leaf_name}"
    return tree, not_tokenised


def literal(raw, src):
    v = raw.strip()
    if v == "transparent":
        return {"$value": "rgba(0, 0, 0, 0)", "$type": "color", "$extensions": {"source": src + "; declared as `transparent`"}}
    if re.fullmatch(r"#[0-9a-fA-F]{3,8}", v):
        return {"$value": norm_color(v), "$type": "color", "$extensions": {"source": src}}
    if re.fullmatch(r"-?\d*\.?\d+px", v):
        return {"$value": px(v), "$type": "dimension", "$extensions": {"source": src}}
    if v.startswith("inset") or re.match(r"-?\d", v) and "#" in v:
        layers = parse_shadow(v)
        if layers:
            return {"$value": layers, "$type": "shadow", "$extensions": {"source": src}}
    if v.startswith("linear-gradient(") and "var(" not in v and v.count("linear-gradient(") == 1:
        g = parse_gradient(v)
        if g:
            angle, stops = g
            return {"$value": [{"color": norm_color(s["color"]), "position": s["position"]} for s in stops], "$type": "gradient", "$extensions": {"source": src, "angle": angle}}
    return None


def with_aliases(raw, src, sets):
    v = raw.strip()
    m = re.fullmatch(r"var\(--([A-Za-z0-9-]+)\)", v)
    if m:
        try:
            return {"$value": alias_of(m.group(1), sets), "$type": type_of_alias(m.group(1), sets), "$extensions": {"source": src}}
        except KeyError:
            return None
    if v.startswith("linear-gradient(") and v.count("linear-gradient(") == 1:
        g = parse_gradient(v)
        if g:
            angle, stops = g
            out = []
            for s in stops:
                c = s["color"]
                mm = re.fullmatch(r"var\(--([A-Za-z0-9-]+)\)", c)
                try:
                    c = alias_of(mm.group(1), sets) if mm else norm_color(c)
                except (KeyError, ValueError):
                    return None
                out.append({"color": c, "position": s["position"]})
            return {"$value": out, "$type": "gradient", "$extensions": {"source": src, "angle": angle}}
    return None


def type_of_alias(name, sets):
    for s in sets:
        path = s.get("_index", {}).get(name)
        if path:
            node = s
            for k in path.split("."):
                node = node[k]
            return node["$type"]
    raise KeyError(name)


light, light_skipped = themed_set(LIGHT, "light")
dark, dark_skipped = themed_set(DARK, "dark", fallback=LIGHT)

# accent palettes: light values in light, dark values (falling back to light) in dark
for colour, pair in sorted(ACCENTS.items()):
    for theme, tree in (("light", light), ("dark", dark)):
        vals = dict(pair.get("light", {}))
        if theme == "dark":
            vals.update(pair.get("dark", {}))
        for name, raw in vals.items():
            sel = f'{".dark" if theme == "dark" and name in pair.get("dark", {}) else ""}.accent-custom[data-accent-color="{colour}"]'
            tree.setdefault("accent", {}).setdefault(colour, {})[name[len("--accent-"):]] = {
                "$value": norm_color(raw), "$type": "color", "$extensions": {"source": f"css-var {name} ({sel}, {THEME_SHEET})"}}
# which roles an accent takes over
for tree in (light, dark):
    tree["accent"]["$description"] = ("With `.accent-custom` on <html>, " + ", ".join(f"{k} becomes {v}" for k, v in ACCENT_ROLES.items()) +
                                      "; the default (no class) is the blue the text.blue, icon.blue, border.blue and fill.blue tokens hold.")

for tree in (light, dark):
    tree.pop("_index")

# ---------- core ----------

core = {}
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI Variable Display', 'Segoe UI', Helvetica, 'Apple Color Emoji', Arial, sans-serif, 'Segoe UI Emoji', 'Segoe UI Symbol'"
core["fontFamily"] = {
    "sans": {"$value": SANS, "$type": "fontFamily", "$extensions": {"source": f"body font-family and .font-serif's first declaration in {UI_SHEET}; Manus has no web font for UI text, it is the system face"}},
    "serif": {"$value": "LibreBaskerville, Georgia, Cambria, ui-serif, 'Times New Roman', Times, serif", "$type": "fontFamily", "$extensions": {"source": f".font-serif in {UI_SHEET} (the last of three declarations wins); LibreBaskerville is self-hosted at 400 and 700; the CJK locales swap in Noto Serif SC/TC/JP through --font-noto-serif-*"}},
    "mono": {"$value": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", "$type": "fontFamily", "$extensions": {"source": f".font-mono in {UI_SHEET}"}},
    "math": {"$value": "KaTeX_Main, 'Times New Roman', serif", "$type": "fontFamily", "$extensions": {"source": "KaTeX's own faces, 44 @font-face rules"}},
}
core["fontWeight"] = {k: {"$value": v, "$type": "fontWeight", "$extensions": {"source": f".font-{k} in {UI_SHEET}"}} for k, v in (("regular", 400), ("medium", 500), ("semibold", 600), ("bold", 700))}

steps = ["xs", "label", "sm", "body-sm", "base", "title-base", "lg", "title-lg", "xl", "headline-sm", "2xl", "headline-base", "headline-lg", "3xl"]
core["fontSize"], core["lineHeight"], core["typography"] = {}, {}, {}
for s in steps:
    fs, lh = UI[f"--ui-font-size-{s}"], UI[f"--ui-line-height-{s}"]
    core["fontSize"][s] = {"$value": px(fs), "$type": "dimension", "$extensions": {"source": f"css-var --ui-font-size-{s} (:root, {UI_SHEET})"}}
    core["lineHeight"][s] = {"$value": px(lh), "$type": "dimension", "$extensions": {"source": f"css-var --ui-line-height-{s} (:root, {UI_SHEET})"}}
    weight = "medium" if s.startswith(("title", "headline")) else "regular"
    core["typography"][s] = {"$value": {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.%s}" % s, "lineHeight": "{lineHeight.%s}" % s, "fontWeight": "{fontWeight.%s}" % weight, "letterSpacing": "0px"},
                             "$type": "typography", "$extensions": {"source": f"--ui-font-size-{s} with --ui-line-height-{s}; the weight is the one the measured elements of that size carry"}}
core["typography"]["$description"] = ("The scale pairs a `*-xs/sm/base/lg/xl/2xl/3xl` step for body text with `label`, `body-sm` (14/22, used for chat and the composer on desktop: `.chat-message-body, .chat-input-editor` set --ui-font-size-base to it), "
                                      "`title-base`, `title-lg` and `headline-sm/base/lg` steps with tighter leading. Serif display text (the home's 'What can I do for you?', the wordmark, the share banner's title, the document previewer's title) uses fontFamily.serif at these sizes.")

dens = {}
for name, raw in UI.items():
    if not name.startswith("--ui-density-"):
        continue
    key = name[len("--ui-density-"):]
    ty = "number" if key == "nav-icon-scale" else "dimension"
    val = float(raw) if ty == "number" else px(raw)
    tok = {"$value": val, "$type": ty, "$extensions": {"source": f"css-var {name} (:root, {UI_SHEET})"}}
    if name in COMPACT:
        tok["$extensions"]["compact"] = float(COMPACT[name]) if ty == "number" else px(COMPACT[name])
    if name in STANDARD:
        tok["$extensions"]["standardDesktop"] = float(STANDARD[name]) if ty == "number" else px(STANDARD[name])
    dens[key] = tok
dens["$description"] = ("Manus's density scale: row heights, radii, paddings and gaps the sidebar, menus, composer and chat read through var(). The desktop app offers Standard and Compact (`html.is-desktop[data-interface-density]`); "
                        "`compact` and `standardDesktop` in $extensions are those overrides, the web default is the $value.")
core["density"] = dens
core["radius"] = {
    "row": {"$value": "{density.row-radius}", "$type": "dimension", "$extensions": {"source": "--ui-density-row-radius; nav tabs, list rows, menu items"}},
    "small": {"$value": "{density.small-radius}", "$type": "dimension", "$extensions": {"source": "--ui-density-small-radius; icon buttons, chips, the segmented control"}},
    "card": {"$value": "{density.card-radius}", "$type": "dimension", "$extensions": {"source": "--ui-density-card-radius; cards, dialogs, deliverable cards"}},
    "composer": {"$value": "{density.composer-radius}", "$type": "dimension", "$extensions": {"source": "--ui-density-composer-radius; the task composer"}},
}
core["size"] = {
    "row": {"$value": "{density.row-height}", "$type": "dimension", "$extensions": {"source": "--ui-density-row-height"}},
    "row-small": {"$value": "{density.small-row-height}", "$type": "dimension", "$extensions": {"source": "--ui-density-small-row-height"}},
    "control-large": {"$value": "{density.large-control-height}", "$type": "dimension", "$extensions": {"source": "--ui-density-large-control-height"}},
    "nav-icon-box": {"$value": "{density.nav-icon-box-size}", "$type": "dimension", "$extensions": {"source": "--ui-density-nav-icon-box-size"}},
}
core["duration"] = {
    "resize": {"$value": "300ms", "$type": "duration", "$extensions": {"source": "css-var --resize-dur (.t-resize, 0p0dbh3-6xn1t.css); the sidebar's width transition is duration-200 on <nav>"}},
    "sidebar": {"$value": "200ms", "$type": "duration", "$extensions": {"source": "duration-200 on <nav> (transition-[width,transform])"}},
    "page-fade": {"$value": "150ms", "$type": "duration", "$extensions": {"source": "css-var --page-fade-dur (.connector-detail-page)"}},
    "theme": {"$value": "500ms", "$type": "duration", "$extensions": {"source": "transition-colors duration-500 on the task page's main column"}},
    "streamer": {"$value": "260ms", "$type": "duration", "$extensions": {"source": "css-var --ppt-streamer-move-ms (.ppt-streamer-overlay)"}},
}
core["easing"] = {
    "resize": {"$value": [0.22, 1, 0.36, 1], "$type": "cubicBezier", "$extensions": {"source": "css-var --resize-ease (.t-resize)"}},
    "standard": {"$value": [0.4, 0, 0.2, 1], "$type": "cubicBezier", "$extensions": {"source": "Tailwind's ease-in-out, used by the window-controls padding transition and every `transition-*` utility"}},
    "streamer": {"$value": [0.22, 0.61, 0.36, 1], "$type": "cubicBezier", "$extensions": {"source": "css-var --ppt-streamer-ease"}},
}
core["breakpoint"] = {k: {"$value": v, "$type": "dimension", "$extensions": {"source": "Tailwind's screens as used in the utilities (sm:, md:, lg:, xl:)"}} for k, v in (("sm", "640px"), ("md", "768px"), ("lg", "1024px"), ("xl", "1280px"))}


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        ty, val = node["type"], node["value"]
        if ty == "dimension" and isinstance(val, (int, float)):
            val = ("%g" % val) + "px"
        if ty == "color":
            val = norm_color(val) if not str(val).startswith("{") else val
        t = {"$value": val, "$type": ty, "$extensions": {"source": node["source"]}}
        if node.get("description"):
            t["$description"] = node["description"]
        return t
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


for k, v in build(SPEC.get("core", {})).items():
    core[k] = {**core.get(k, {}), **v} if isinstance(core.get(k), dict) else v
for setname, tree in (("light", light), ("dark", dark)):
    for k, v in build(SPEC.get(setname, {})).items():
        tree[k] = {**tree.get(k, {}), **v} if isinstance(tree.get(k), dict) else v

# ---------- 2026-10-17 refresh: palette ramps, roles, elevation, spacing, shape, focus, motion, layers

def rgb_of(hexv):
    h = norm_color(hexv)
    return None if h.startswith("rgba") else tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])


def ramp(values, src):
    """{hex: [where, ...]} -> numbered steps, lightest first."""
    out = {}
    for i, (hexv, where) in enumerate(sorted(values.items(), key=lambda x: (-lum(rgb_of(x[0])), x[0])), 1):
        out["%02d" % i] = {"$value": hexv, "$type": "color", "$extensions": {"source": src, "declaredAs": sorted(where)}}
    return out


import colorsys

FAMILIES = (("red", 345, 360), ("red", 0, 12), ("orange", 12, 38), ("yellow", 38, 65), ("green", 65, 170), ("teal", 170, 200),
            ("blue", 200, 250), ("purple", 250, 290), ("pink", 290, 345))


def family(rgb):
    r, g, b = (c / 255 for c in rgb)
    h, l_, sat = colorsys.rgb_to_hls(r, g, b)
    if max(rgb) - min(rgb) <= 8 or sat < 0.12:
        return "neutral"
    return next(name for name, lo, hi in FAMILIES if lo <= h * 360 < hi)


# Every colour literal the theme blocks and the accent palettes declare, opaque or not. A translucent
# value contributes its base colour, so each declared colour is a ramp step or a step at an alpha.
declared = []
for where, decls in ((":root", LIGHT), (".dark", DARK)):
    declared += [(name, raw, where) for name, raw in decls.items()]
for colour, pair in sorted(ACCENTS.items()):
    for th, props in pair.items():
        declared += [(name, raw, f"{'.dark' if th == 'dark' else ''}.accent-custom[data-accent-color={colour}]") for name, raw in props.items()]
steps, alpha_uses, total = {}, 0, 0
for name, raw, where in declared:
    raw = raw.strip()
    if not re.fullmatch(r"#[0-9a-fA-F]{3,8}", raw):
        continue
    total += 1
    h = raw[1:].lower()
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    base = "#" + h[:6]
    if len(h) == 8 and h[6:] != "ff":
        alpha_uses += 1
        label = f"{name} ({where}) at alpha {round(int(h[6:], 16) / 255, 2):g}"
    else:
        label = f"{name} ({where})"
    steps.setdefault(base, set()).add(label)
palette = {}
for base, where in steps.items():
    palette.setdefault(family(rgb_of(base)), {})[base] = where
ORDER = ["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"]
STOPS = [("50", 0.97), ("100", 0.93), ("200", 0.86), ("300", 0.76), ("400", 0.64), ("500", 0.53), ("600", 0.43), ("700", 0.34), ("800", 0.25), ("900", 0.16), ("950", 0.09)]


def condensed(values, fam):
    """The 50 to 950 view of a family: for each stop, the declared colour whose HLS lightness is
    nearest the stop's target, if one is within 0.06; a stop with none is left out."""
    light = {hexv: colorsys.rgb_to_hls(*(c / 255 for c in rgb_of(hexv)))[1] for hexv in values}
    out, used = {}, set()
    for stop, target in STOPS:
        best = min((v for v in light if v not in used), key=lambda v: (abs(light[v] - target), v), default=None)
        if best is None or abs(light[best] - target) > 0.06:
            continue
        used.add(best)
        out[stop] = {"$value": best, "$type": "color", "$extensions": {"source": f"Derived: the declared {fam} colour nearest lightness {target:g} (HLS); it also appears in `{fam}-all`", "lightness": round(light[best], 3), "declaredAs": sorted(values[best])}}
    return out


core["palette"] = {}
for fam in ORDER:
    if fam in palette:
        core["palette"][fam] = condensed(palette[fam], fam)
for fam in ORDER:
    if fam in palette:
        core["palette"][fam + "-all"] = ramp(palette[fam], f"Derived: every {fam} colour the {THEME_SHEET} :root and .dark blocks and the accent palettes declare, as itself or as the base of a translucent value, ordered lightest to darkest by luminance. Manus declares no ramp; `declaredAs` names the variables that hold each step")
core["palette"]["$description"] = (f"Primitive ramps, assembled (Derived): Manus ships Tailwind 3 without its colour palette and declares only semantic variables, so every colour literal it declares ({total} declarations, {alpha_uses} of them translucent) is placed on the ramp of its hue, neutral first. "
                                   "A translucent token is its ramp step at that alpha, so every declared colour sits on a ramp. Hue families: neutral (channels within 8, or saturation under 12%), then red, orange, yellow, green, teal, blue, purple and pink by hue angle. "
                                   "Each hue has two views: `<hue>` is a 50 to 950 ramp (up to 11 stops, each the declared colour nearest that lightness) and `<hue>-all` lists every declared colour of the hue, lightest first. "
                                   "The user-selectable accent palettes (blue, green, yellow, pink, orange, purple, black) fold into these ramps; each step's `declaredAs` says which palette or variable holds it.")
core["palette"]["$extensions"] = {"declarations": total, "translucent": alpha_uses, "steps": {f: len(palette.get(f, {})) for f in ORDER if f in palette}}

# shadow layers from the stylesheet, colours aliased to the theme's shadow.* tokens
def css_layers(value, tree_index):
    layers = []
    for part in split_top(value):
        bits = part.strip().replace("var(", " var(").split()
        inset = "inset" in bits
        bits = [b for b in bits if b != "inset"]
        col = bits[-1]
        nums = bits[:-1] + ["0"] * (4 - len(bits[:-1]))
        m = re.fullmatch(r"var\(--([A-Za-z0-9-]+)\)", col)
        if m:
            col = "{" + tree_index[m.group(1)] + "}"
        elif re.fullmatch(r"#[0-9a-f]{3,8}", col):
            col = norm_color(col)
        else:
            return None
        layers.append({"offsetX": px(nums[0]), "offsetY": px(nums[1]), "blur": px(nums[2]), "spread": px(nums[3]), "color": col, "inset": inset})
    return layers


ELEVATION = [  # (token, utility or literal value, where it is measured)
    ("card", "shadow-card", "Manus's named `shadow-card` utility; the stylesheet's card treatment (a hairline ring plus two short drops). Not on any element in the captured pages"),
    ("raised", "0 3px 10px 0 var(--shadow-S)", "the Computers page's Customize and Connect bands (measured: computers-connect, computers-customize); the Settings link card on hover is 0 1px 2px + 0 2px 4px of the same colour"),
    ("composer", "0px 12px 32px 0px #00000005", "the task composer on home, a project and a task (measured: composer, project-composer, m-composer); a literal rgba(0,0,0,0.02), the same in both themes"),
    ("layer", "shadow-layer", "Manus's named `shadow-layer` utility: a Library grid card on hover (measured: grid-card, hover:shadow-layer)"),
    ("menu", "shadow-menu", "Manus's named `shadow-menu` utility, on every menu, popover, listbox and dialog measured (17 components: model menu, attach menu, context menu, row popover, select listbox, search dialog, files dialog, confirm dialog, form dialog, invite dialog, ...)"),
    ("panel", "0px 0px 0px 1px var(--shadow-XS), 0px 4px 32px 0px var(--shadow-S)", "the notifications panel (measured: notifications-panel)"),
]
for theme, tree in (("light", light), ("dark", dark)):
    idx = {}
    for g, node in tree.items():
        if isinstance(node, dict):
            for leaf in node:
                if not leaf.startswith("$"):
                    idx_name = {"shadow": "shadow-", "background": "background-", "text": "text-", "border": "border-", "fill": "fill-"}.get(g)
                    if idx_name:
                        idx[idx_name + leaf] = f"{g}.{leaf}"
    el = {}
    for name, util, where in ELEVATION:
        value = RULES["namedShadows"][util]["value"] if util in RULES["namedShadows"] else util
        layers = css_layers(value, idx)
        if layers is None:
            raise ValueError(f"elevation.{name}: cannot parse {value}")
        el[name] = {"$value": layers, "$type": "shadow", "$extensions": {"source": f"Measured: {where}; value from the stylesheet" + (f" (.{util} in {RULES['namedShadows'][util]['file']})" if util in RULES["namedShadows"] else "")}}
    el["$description"] = ("Six levels from flat to floating, each tied to where Manus uses it. Menus, popovers and dialogs share one level (`menu`); dialogs are told apart by the scrim, not a deeper shadow. "
                          "Shadow colours alias this theme's shadow.* tokens, so dark shadows are stronger and dark `menu` and `card` add a white highlight ring (shadow.Highlight).")
    tree["elevation"] = el

# semantic roles over the existing tokens
ROLE_SRC = "Derived: role assignment from the measured components; the value is the token Manus's own classes name there"
for theme, tree in (("light", light), ("dark", dark)):
    hover_base = rgb_of(LIGHT["--background-gray-main"] if theme == "light" else DARK["--background-gray-main"])
    btn = (LIGHT if theme == "light" else DARK)["--Button-black"]
    b = norm_color(btn)
    if b.startswith("rgba"):
        r_, g_, b_, a_ = [float(x) for x in re.findall(r"[\d.]+", b)]
    else:
        r_, g_, b_ = rgb_of(b)
        a_ = 1.0

    def over(alpha):
        a = a_ * alpha
        return "#%02x%02x%02x" % tuple(round(c * a + base * (1 - a)) for c, base in zip((r_, g_, b_), hover_base))
    tree["role"] = {
        "background": {
            "page": {"$value": "{background.gray-main}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": the main column of every page and the Settings dialog (bg-[var(--background-gray-main)])"}},
            "surface": {"$value": "{background.nav}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": the sidebar (measured: sidebar)"}},
            "raised": {"$value": "{background.menu-white}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": the composer, Library grid cards and the Computers bands (measured: composer, grid-card, computers-connect)"}},
            "overlay": {"$value": "{background.menu-white}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": menus, popovers, the select listbox and the search dialog (measured: model-menu, popover-menu, select-listbox, search-dialog)"}},
            "dialog": {"$value": "{background.gray-main}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": modal dialogs use the page colour and float on shadow-menu over the scrim (measured: confirm-dialog, form-dialog, settings-dialog)"}},
            "scrim": {"$value": "{background.dialog-mask}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": the full-screen layer behind a dialog, with backdrop-blur 4px (class bg-[var(--background-dialog-mask)] in the confirm and form dialog copies); the phone drawer uses background.mask-black"}},
        },
        "text": {
            "primary": {"$value": "{text.primary}", "$type": "color", "$extensions": {"source": ROLE_SRC}},
            "secondary": {"$value": "{text.secondary}", "$type": "color", "$extensions": {"source": ROLE_SRC}},
            "tertiary": {"$value": "{text.tertiary}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": table headers, field hints, inactive tabs"}},
            "disabled": {"$value": "{text.disable}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": placeholders (measured: text-field, email-field)"}},
            "on-accent": {"$value": "{text.onblack}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": text on the primary (Button-black) button (measured: button-primary)"}},
            "link": {"$value": "{text.blue}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": the Upgrade link and the Documentation link (measured: upgrade-link)"}},
        },
        "border": {
            "subtle": {"$value": "{border.light}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": table row rules (measured: table-row)"}},
            "default": {"$value": "{border.main}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": dividers, the sidebar rule, card outlines"}},
            "strong": {"$value": "{border.dark}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": control outlines (the composer, outline buttons, the field focus ring colour)"}},
            "focus": {"$value": "{border.input-active}", "$type": "color", "$extensions": {"source": "Measured (stylesheet): focus-within:border-[var(--border-input-active)] and focus-visible:ring-[var(--border-input-active)] are the focus rules that name a dedicated colour; most inputs instead draw a 1px ring in border.strong (focus:ring-[var(--border-dark)])"}},
        },
        "accent": {
            "default": {"$value": "{button.black}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": the primary action is the black (light) / white (dark) button: Create, Copy invitation link, Upgrade (measured: button-primary, button-black-wide, button-white)"}},
            "hover": {"$value": over(0.9), "$type": "color", "$extensions": {"source": "Derived: button.black at opacity 0.9 over role.background.page. Measured: hover:opacity-90 on button-primary (enabled-hover reads opacity 0.9)"}},
            "pressed": {"$value": over(0.9), "$type": "color", "$extensions": {"source": "Derived: as hover. Measured: holding the pointer down reads opacity 0.9, not the 0.8 the active:opacity-80 class asks for, because hover:opacity-90 comes later in the stylesheet and wins (button-primary, button-danger, button-blue: pressed = hover)"}},
            "on-accent": {"$value": "{text.onblack}", "$type": "color", "$extensions": {"source": ROLE_SRC}},
            "brand": {"$value": "{text.blue}", "$type": "color", "$extensions": {"source": "Derived: Manus's blue (--text-blue, --icon-blue, --Button-blue) carries links, the Upgrade text, selection and the user's own accent colour when they pick one; the <meta name=theme-color> is the page colour, not the blue"}},
        },
        "status": {
            "danger": {
                "fill": {"$value": "{function.error-tsp}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": --function-error-tsp"}},
                "text": {"$value": "{function.error}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": the Delete menu item and the danger button fill (measured: menu-item-danger, button-danger)"}},
                "border": {"$value": "{button.border-error}", "$type": "color", "$extensions": {"source": "Measured (stylesheet): --Button-border-error, used as focus-within:shadow-[0px_0px_0px_1px_var(--Button-border-error)] on a field in error"}},
            },
            "success": {
                "fill": {"$value": "{function.success-tsp}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": --function-success-tsp"}},
                "text": {"$value": "{function.success}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": --function-success"}},
            },
            "warning": {
                "fill": {"$value": "{function.warning-tsp}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": --function-warning-tsp"}},
                "text": {"$value": "{function.warning}", "$type": "color", "$extensions": {"source": ROLE_SRC + ": --function-warning"}},
            },
            "$description": "Manus declares fill and text for danger, success and warning, and a border only for danger. It has no info status: no --function-info, and no informational banner uses the blue (the Developers info banner is a neutral fill.tsp-white-light).",
        },
        "$description": "Checklist roles mapped onto Manus's own tokens. Each is an alias, so the value is always the one the product declares; only accent.hover and accent.pressed are computed.",
    }

# spacing, shape, focus, motion, layers, grid
sp, off = {}, {}
for s_ in RULES["spacing"]:
    v = s_["px"]
    if v <= 0:
        continue
    if not (v % 4 == 0 or v in (2, 6, 10, 14)):  # off the 4px grid and Tailwind's half steps (0.5, 1.5, 2.5, 3.5)
        off["%gpx" % v] = s_["elements"]
    else:
        step = ("%g" % (v / 4)).replace(".", "_")
        sp[step] = {"$value": "%gpx" % v, "$type": "dimension", "$extensions": {"source": f"Measured: Tailwind spacing utilities (p-, m-, gap-, space-) resolving to {v:g}px on {s_['elements']} elements across the refresh's page copies (raw/css-rules.json spacing)", "elements": s_["elements"]}}
sp["$description"] = ("Tailwind's spacing scale on a 4px base, as Manus uses it: a key is the class step, so `space.2` is gap-2 / p-2 = 8px, and `space.2_5` is the 10px half step. "
                      "Every step carries its element count. Values off the grid are kept apart in $extensions.offGrid; the density tokens (density.*) hold the component paddings Manus sets by variable.")
# Summed outside the f-string: a same-quote string inside one is a SyntaxError before Python 3.12.
on_scale = sum(x["elements"] for x in RULES["spacing"] if x["px"] > 0)
sp["$extensions"] = {"base": "4px", "offGrid": off,
                     "note": f"{sum(off.values())} of {on_scale} spacing class uses are off the grid (1px rules and arbitrary 7, 9, 11 and 34px values); everything else is on the scale"}
core["space"] = sp
bw = RULES["borderWidth"]
core["radius"]["dialog"] = {"$value": "16px", "$type": "dimension", "$extensions": {"source": "Measured: rounded-[16px] on every role=dialog in the 2026-10-17 copies (confirm, form, invite and Settings dialogs)"}}
core["borderWidth"] = {
    "hairline": {"$value": "0.5px", "$type": "dimension", "$extensions": {"source": "Measured: border-[0.5px] on the share banner and the Library grid card's ring (shadow-layer's 0.5px layer)"}},
    "default": {"$value": "1px", "$type": "dimension", "$extensions": {"source": f"Measured: {len(bw['measured'].get('1px', []))} measured components paint 1px borders (raw/css-rules.json borderWidth.measured); `border` is 1px"}},
    "strong": {"$value": "2px", "$type": "dimension", "$extensions": {"source": "Measured: border-b-[2px] on the active underline tab (tabs-underline selected) and border-2 utilities"}},
    "illustration": {"$value": "1.2px", "$type": "dimension", "$extensions": {"source": f"Measured: border-[1.2px] on {RULES['borderWidth']['utilities'].get('border-[1.2px]', {}).get('elements', 0)} elements in the copies, all frames inside illustrations (the Create card's paper sheets); not used on controls"}},
}
fv = RULES["focusVisible"]
core["focusRing"] = {
    "width": {"$value": "2px", "$type": "dimension", "$extensions": {"source": "Measured (stylesheet): focus-visible:outline-2 and the [&_:is(a,button):focus-visible]:outline-2 rule; .chat-input-url-icon:focus-visible is `outline: 2px solid var(--text-blue)`"}},
    "offset": {"$value": "2px", "$type": "dimension", "$extensions": {"source": "Measured (stylesheet): focus-visible:outline-offset-2 (and -2px, inset, on a few tiles)"}},
    "input-width": {"$value": "1px", "$type": "dimension", "$extensions": {"source": "Measured: fields draw focus as a 1px ring in border.strong (focus:ring-[1px] focus:ring-[var(--border-dark)]; measured on text-field-wrapper and text-field-settings focus-visible)"}},
    "$description": (f"What a ring looks like where Manus draws one. Most controls draw none: {fv.get('focus-visible outline', {}).get('rules', 0)} outline and {fv.get('focus-visible ring', {}).get('rules', 0)} ring rules exist in the stylesheets, "
                     "but nav rows, cards, menu items and the buttons measured keep outline-style none on keyboard focus (checked live with Tab on 2026-10-17, see README)."),
}
rm = RULES["reducedMotion"]
core["duration"]["$extensions"] = {"reducedMotion": (f"{len(rm)} rules under @media (prefers-reduced-motion): animations and hover lifts are written as motion-safe: variants (spin, pulse, bounce, fade-in, slide-in, hover scale and translate), so they do not run at all when reduced motion is on; "
                                                   "motion-reduce: variants hide marquees and stop transforms; .t-resize and .connector-detail-page set transition: none. Colour transitions (transition-colors, 150ms) are not affected.")}
dis = RULES["disabled"]
core["opacity"] = {
    "hover": {"$value": 0.9, "$type": "number", "$extensions": {"source": "Measured: hover:opacity-90 on the filled buttons (button-primary enabled-hover, button-danger, button-blue read opacity 0.9); pressed reads the same, see role.accent.pressed"}},
    "pressed": {"$value": 0.8, "$type": "number", "$extensions": {"source": f"Measured (stylesheet): active:opacity-80 on {RULES['pressed'].get('opacity-80', 0)} elements in the copies; on the filled buttons hover:opacity-90 wins, so they read 0.9 while pressed"}},
    "disabled": {"$value": 0.6, "$type": "number", "$extensions": {"source": f"Measured (stylesheet): disabled:opacity-60 on {dis.get('opacity-60', 0)} elements in the copies"}},
    "disabled-strong": {"$value": 0.5, "$type": "number", "$extensions": {"source": "Measured: the composer's send button while the composer is empty (composer-send default, opacity 0.5)"}},
}
core["duration"]["fast"] = {"$value": "150ms", "$type": "duration", "$extensions": {"source": "Measured: transitionDuration 0.15s on every measured button (Tailwind's transition-colors default)"}}
zu = RULES["zIndex"]["utilities"]
core["zIndex"] = {
    "content": {"$value": 1, "$type": "number", "$extensions": {"source": f"Measured: z-[1] to z-[5] stack layers inside a component ({sum(v['elements'] for k, v in zu.items() if 1 <= v['value'] <= 5)} elements in the copies), e.g. the segmented control's labels over its thumb"}},
    "raised": {"$value": 10, "$type": "number", "$extensions": {"source": f"Measured: z-10 on {zu.get('z-10', {}).get('elements', 0)} elements (sticky rows, hovered cards: group-hover:z-10)"}},
    "sticky": {"$value": 20, "$type": "number", "$extensions": {"source": f"Measured: z-20 on {zu.get('z-20', {}).get('elements', 0)} elements"}},
    "overlay": {"$value": 30, "$type": "number", "$extensions": {"source": f"Measured: z-30 on {zu.get('z-30', {}).get('elements', 0)} elements in the copies"}},
    "tooltip": {"$value": 999, "$type": "number", "$extensions": {"source": "Measured: the tooltip computes z-index 999 from Manus's named `z-tooltip` utility (.z-tooltip{z-index:999})"}},
    "toast": {"$value": 1050, "$type": "number", "$extensions": {"source": "Measured: z-[1050] on the toast viewport (<ol class=\"fixed top-[28px] ... z-[1050]\">) and the role=status notice region"}},
    "$description": "Dialogs, menus and popovers carry no z-index: they mount in portals at the end of <body> and stack in the order they open. Tooltips sit at 999 and toasts and status notices at 1050.",
}
core["layout"] = core.get("layout", {})
core["layout"]["grid"] = {
    "home": {"$value": "490px 270px", "$type": "other", "$extensions": {"source": "Measured (raw/pages.md, layout.json): home, Build and Create cards in a 490 column beside the 270 local-file card, 8 apart", "gap": "8px"}},
    "computers": {"$value": "repeat(3, 312px)", "$type": "other", "$extensions": {"source": "Measured (raw/pages.md): Computers setup cards, 3 columns of 312, 12 apart", "gap": "12px"}},
    "plugins": {"$value": "repeat(2, 378px)", "$type": "other", "$extensions": {"source": "Measured (raw/pages.md): Plugins rows, 2 columns of 378, 12 apart", "gap": "12px"}},
    "project": {"$value": "minmax(0, 1fr) 320px", "$type": "other", "$extensions": {"source": "Measured (raw/pages.md): the project page, a 740 column and a 320 rail 44 apart; the stylesheet's @[700px]:grid-cols-[minmax(0,1fr)_270px] is the same pattern at container width", "gap": "44px"}},
    "$description": "Manus lays pages out on fixed column widths inside a centred max-width box (layout.content-max-width, layout.library-max-width), not a 12-column grid.",
}
core["typography"]["role"] = {
    "display": {"$value": {"fontFamily": "{fontFamily.serif}", "fontSize": "30px", "lineHeight": "39px", "fontWeight": "{fontWeight.semibold}", "letterSpacing": "0px"}, "$type": "typography", "$extensions": {"source": "Measured: the document previewer's title and a document's h1 (doc-h1, previewer-body), LibreBaskerville 30/39 600"}},
    "heading": {"$value": {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.title-lg}", "lineHeight": "{lineHeight.title-lg}", "fontWeight": "{fontWeight.semibold}", "letterSpacing": "0px"}, "$type": "typography", "$extensions": {"source": "Measured: dialog titles, 18/24 600 (confirm-dialog, form-dialog)"}},
    "body": {"$value": {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.sm}", "lineHeight": "{lineHeight.sm}", "fontWeight": "{fontWeight.regular}", "letterSpacing": "0px"}, "$type": "typography", "$extensions": {"source": "Measured: 14/20 400 on 50 components (menus, rows, tabs, table cells)"}},
    "body-long": {"$value": {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.base}", "lineHeight": "{lineHeight.base}", "fontWeight": "{fontWeight.regular}", "letterSpacing": "0px"}, "$type": "typography", "$extensions": {"source": "Measured: assistant and user messages, 16/24 400 (assistant-text, user-bubble)"}},
    "label": {"$value": {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.sm}", "lineHeight": "{lineHeight.sm}", "fontWeight": "{fontWeight.medium}", "letterSpacing": "0px"}, "$type": "typography", "$extensions": {"source": "Measured: button labels, 14/20 500 on 25 components"}},
    "caption": {"$value": {"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.xs}", "lineHeight": "{lineHeight.xs}", "fontWeight": "{fontWeight.regular}", "letterSpacing": "0px"}, "$type": "typography", "$extensions": {"source": "Measured: 12/16 400 meta lines (assistant-header, creation-url, plugin-desc, project-meta)"}},
    "code": {"$value": {"fontFamily": "{fontFamily.mono}", "fontSize": "13.6px", "lineHeight": "{lineHeight.base}", "fontWeight": "{fontWeight.regular}", "letterSpacing": "0px"}, "$type": "typography", "$extensions": {"source": "Measured (stylesheet): .manus-markdown code:not(pre code) is font-size 85% of the 16px message text, on fill.tsp-white-main with radius 4; the family is fontFamily.mono. Not seen on an element in the captured pages"}},
}

# Sizes, radii and type styles the measured components share, counted on their dark default states
# (raw/components-computed.json), so a component entry can name them. Added 2026-10-17.
_defaults = [st for c in COMPS.values() for n, st in c["states"].items() if n == "default" and st.get("theme") == "dark" and "style" in st]


def _count(pred):
    return sum(1 for st in _defaults if pred(st))


for name, px_, what in (("icon-xs", 14, "14px glyphs (file chips, inline icons)"), ("icon-small", 16, "16px Lucide glyphs in menus, settings and buttons"),
                        ("icon", 18, "18px glyphs in the sidebar and headers (as size.nav-icon)"), ("icon-medium", 20, "20px glyphs"), ("icon-large", 24, "24px glyphs and file icons")):
    n = _count(lambda st, v=px_: (st.get("icon") or {}).get("w") == v and (st.get("icon") or {}).get("h") == v)
    core["size"][name] = {"$value": f"{px_}px", "$type": "dimension", "$extensions": {"source": f"Measured: the icon of {n} measured components is {px_} x {px_}: {what}", "components": n}}
core["size"]["control-small"] = {"$value": "28px", "$type": "dimension", "$extensions": {"source": f"Measured: {_count(lambda st: st['rect']['h'] == 28)} measured components are 28px tall (small icon buttons, the desktop and bell buttons, the table row button)"}}
core["size"]["header"] = {"$value": "{layout.header-height}", "$type": "dimension", "$extensions": {"source": "Measured: the 48px page and sidebar header rows (layout.header-height)"}}
core["radius"]["md"] = {"$value": "6px", "$type": "dimension", "$extensions": {"source": f"Measured: {_count(lambda st: st['style']['borderTopLeftRadius'] == '6px')} measured components round at 6px (Tailwind rounded-md and rounded-[6px]: icon buttons, the table row button, the segmented thumb)"}}
core["radius"]["full"] = {"$value": "9999px", "$type": "dimension", "$extensions": {"source": f"Measured: {_count(lambda st: st['style']['borderTopLeftRadius'] == '9999px')} measured components are pills or circles (rounded-full: avatars, the send button, badges)"}}
for name, (fs, lh, fw), what in (("label-compact", ("14px", "18px", 500), "outline and white buttons, Computers and creation actions"),
                                 ("nav", ("14px", "21px", 400), "sidebar nav tabs and task rows"), ("nav-strong", ("14px", "21px", 500), "the files tree and side panel headings"),
                                 ("meta", ("13px", "18px", 400), "small buttons, info banners, Cue links"), ("section-label", ("13px", "18px", 500), "sidebar section headers and small upgrade buttons"),
                                 ("shortcut", ("13px", "19.5px", 400), "side panel tabs, view options, shortcut fields"), ("menu-header", ("12px", "18px", 600), "the account menu and settings account header"),
                                 ("initial", ("12px", "20px", 600), "the avatar initial and the sidebar account row")):
    n = _count(lambda st, k=(fs, lh, str(fw), "normal"): (st.get("textStyle") or {}) and (st["textStyle"]["fontSize"], st["textStyle"]["lineHeight"], st["textStyle"]["fontWeight"], st["textStyle"].get("letterSpacing", "normal")) == k)
    core["typography"]["role"][name] = {"$value": {"fontFamily": "{fontFamily.sans}", "fontSize": fs, "lineHeight": lh, "fontWeight": fw, "letterSpacing": "0px"}, "$type": "typography",
                                        "$extensions": {"source": f"Measured: the text of {n} measured components is {fs}/{lh} {fw} with normal letter spacing: {what}. Off Manus's --ui-* scale, so it is a role of its own; text of this size with negative tracking (the sidebar section labels) is a different style", "components": n}}
# component entries: every var() a measured component's classes name, per state and theme
def component_set(theme):
    tree_index = {}
    t = light if theme == "light" else dark
    for g, node in t.items():
        if isinstance(node, dict):
            for leaf, tok in node.items():
                if isinstance(tok, dict) and "$value" in tok:
                    tree_index.setdefault(g, {})[leaf] = True
    by_name = {}
    for name in (LIGHT if theme == "light" else {**LIGHT, **DARK}):
        g, leaf = group_of(name[2:])
        if leaf in tree_index.get(g, {}):
            by_name[name[2:]] = f"{g}.{leaf}"
    PROP = [("bg", "backgroundColor", r"^(?:[a-z-]+:)*bg-\[var\(--([A-Za-z0-9-]+)\)\]$"), ("text", "color", r"^(?:[a-z-]+:)*text-\[var\(--([A-Za-z0-9-]+)\)\]$"),
            ("border", "borderTopColor", r"^(?:[a-z-]+:)*border(?:-[a-z])?-\[var\(--([A-Za-z0-9-]+)\)\]$"), ("ring", None, r"^(?:[a-z-]+:)*ring-\[var\(--([A-Za-z0-9-]+)\)\]$")]
    out = {}
    for key, c in sorted(COMPS.items()):
        s = c["states"].get("default" if theme == "dark" else "light")
        if not s or "classes" not in s:
            continue
        entry = {}
        for cls in s["classes"].split():
            # Every modifier counts: hover:active:bg-x is the pressed colour, not the hover one. The
            # state key is the whole chain (hover, pressed, hover-pressed, focus-visible, ...); dark:
            # applies only to the dark set, where it is the default.
            mods = cls.split(":")[:-1] if not cls.startswith("[") else []
            if "dark" in mods:
                if theme != "dark":
                    continue
                mods = [x for x in mods if x != "dark"]
            names = {"hover": "hover", "group-hover": "group-hover", "focus": "focus", "focus-visible": "focus-visible", "focus-within": "focus-within",
                     "active": "pressed", "disabled": "disabled", "data-[active]": "selected"}
            if any(x not in names for x in mods):
                continue
            variant = "-".join(names[x] for x in mods) or "default"
            for prop, _, rx in PROP:
                m = re.match(rx, cls.split(":")[-1])
                if m and m.group(1) in by_name:
                    entry.setdefault(variant, {})[prop] = {"$value": "{" + by_name[m.group(1)] + "}", "$type": "color", "$extensions": {"source": f"Measured: class `{cls}` on the measured element ({s['snapshot']})"}}
        if entry:
            out[key] = entry
    out["$description"] = ("One entry per measured component: the colour tokens its own classes name (bg-[var(--x)], text-[var(--x)], border-[var(--x)], ring-[var(--x)]), keyed by the class's whole modifier chain (default, hover, pressed, hover-pressed, focus-visible, disabled, selected, ...), so a pressed colour never stands in for hover. "
                           "Read from the element's class list, so a token here is the one Manus wrote, never a value match. raw/measurements.md has every computed value.")
    return out


for theme, tree in (("light", light), ("dark", dark)):
    tree["component"] = component_set(theme)

light["$extensions"] = {"notTokenised": light_skipped}
dark["$extensions"] = {"notTokenised": dark_skipped}


# every alias must point at a token that exists in core or the same set
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


CORE_NAMES = {n for n, _ in tokens_of(core)}
for setname, tree in (("core", core), ("light", light), ("dark", dark)):
    names = CORE_NAMES | {n for n, _ in tokens_of(tree)}
    for n, t in tokens_of(tree):
        for a in aliases(t["$value"]):
            if a not in names:
                raise KeyError(f"{setname}.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core, "light": light, "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}, "$description": "Manus's `:root` palette; Settings > General > Theme: Light"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}, "$description": "Manus's `.dark` palette; Settings > General > Theme: Dark, or Auto on a dark system (the state every page was captured in)"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for k, v in d.items() if not k.startswith("$")) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")}, "not tokenised:", len(light_skipped), len(dark_skipped))
