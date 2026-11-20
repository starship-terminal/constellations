#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

LottieFiles marketing (lottiefiles.com) is a Tailwind v4 / shadcn site. Semantic
roles live as oklch custom properties on :root, and the stylesheet also ships a
.dark block. The public site painted light only: no control switched the theme.
The dark set resolves that declared block (html.dark forced in vars.mjs) and
every dark colour says so in its source.

Computed colours are oklch(). This builder converts them to sRGB hex so the
catalog can resolve swatches. A value that cannot be converted is skipped, not
invented.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json
import math
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]


def lin(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def oklab_to_srgb(L, a, b):
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
    g = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
    bch = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
    return [round(min(1, max(0, lin(x))) * 255) for x in (r, g, bch)]


def oklch_to_srgb(L, C, H):
    h = math.radians(H)
    return oklab_to_srgb(L, C * math.cos(h), C * math.sin(h))


def fmt(rgb, a):
    a = round(float(a), 3)
    if a >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %g)" % (rgb[0], rgb[1], rgb[2], a)


def color(c):
    c = c.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h)
        rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        return fmt(rgb, a)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", c)
    if m:
        return fmt([int(m.group(i)) for i in (1, 2, 3)], m.group(4) or 1)
    # oklch(L% C H) or oklch(L C H) with optional / alpha. Percent L is 0-100.
    m = re.fullmatch(
        r"oklch\(\s*([\d.]+)%?\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)",
        c,
    )
    if m:
        L = float(m.group(1))
        if c.split("(")[1].strip().startswith(m.group(1) + "%") or "%" in c.split()[0] or "%" in m.group(0).split()[0] or (L > 1 and "%" in c[:c.find(m.group(2))]):
            L = L / 100
        elif L > 1:
            L = L / 100
        C = float(m.group(2))
        H = float(m.group(3))
        a = m.group(4)
        if a is None:
            alpha = 1
        elif a.endswith("%"):
            alpha = float(a[:-1]) / 100
        else:
            alpha = float(a)
        return fmt(oklch_to_srgb(L, C, H), alpha)
    raise ValueError("colour not understood: " + c)


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def put(tree, path, t):
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    node[path[-1]] = t


def getv(theme, name):
    item = RES.get(theme, {}).get(name)
    if not item:
        return None
    return item.get("value") or item.get("raw")


# Roles the public stylesheet declares on :root and again under .dark.
ROLES = [
    ("page", "--background"),
    ("surface", "--card"),
    ("raised", "--popover"),
    ("faint", "--faint"),
    ("muted", "--muted"),
    ("inverse", "--background-inverse"),
    ("sidebar", "--sidebar-background"),
]
TEXT = [
    ("primary", "--foreground"),
    ("secondary", "--muted-foreground"),
    ("on-accent", "--primary-foreground"),
    ("inverse", "--foreground-inverse"),
    ("card", "--card-foreground"),
]
ACCENT = [
    ("default", "--primary"),
    ("on", "--primary-foreground"),
    ("secondary", "--brand-secondary"),
    ("soft", "--accent"),
]
BORDER = [
    ("default", "--border"),
    ("input", "--input"),
    ("focus", "--ring"),
]
STATUS = [
    ("danger", "--destructive"),
    ("danger-foreground", "--destructive-foreground"),
    ("warning", "--warning"),
]

core = {}
# fonts
def need(theme, name):
    """A declared value the token cites. A missing reading fails the build: a literal default
    under a css-var source would read as measured."""
    raw = getv(theme, name)
    if not raw:
        raise SystemExit(f"{name} missing from raw/css-vars.json resolved.{theme}")
    return raw


def rem(v):
    """'.25rem' -> '0.25rem': a DTCG dimension is a number and a unit."""
    return "0" + v if v.startswith(".") else v


def font_stack(name):
    return need("light", name).replace('\\"', '"')

put(core, ["font", "family", "sans"], tok(font_stack("--font-sans"), "fontFamily", "css-var --font-sans on :root"))
put(core, ["font", "family", "display"], tok(font_stack("--font-dm"), "fontFamily", "css-var --font-dm on :root"))
put(core, ["font", "family", "mono"], tok(font_stack("--font-code"), "fontFamily", "css-var --font-code on :root"))

# type scale from Tailwind --text-* (declared, not measured per element)
TYPE = [
    ("caption", "--text-xs", "400"),
    ("label", "--text-sm", "500"),
    ("body", "--text-base", "400"),
    ("body-lg", "--text-lg", "400"),
    ("heading-sm", "--text-xl", "600"),
    ("heading", "--text-2xl", "600"),
    ("heading-lg", "--text-3xl", "600"),
    ("display", "--text-5xl", "600"),
]
for role, name, weight in TYPE:
    size = getv("light", name)
    lh = getv("light", name + "--line-height")
    if not size:
        continue
    put(core, ["typography", role, "fontFamily"], tok("{font.family.sans}", "fontFamily", "css-var --font-sans; body computed Inter LF"))
    put(core, ["typography", role, "fontSize"], tok(rem(size) if size.endswith(("rem", "px")) else rem(size) + "rem", "dimension", f"css-var {name} on :root"))
    # The weight per role was typed in by hand at capture time; no element was read for it.
    put(core, ["typography", role, "fontWeight"], tok(int(weight), "fontWeight", "Reconstruction: entered by hand at capture time as the Tailwind font-weight step this role appears to use; no element's weight was read for it"))
    if lh and re.fullmatch(r"[\d.]+", lh):
        put(core, ["typography", role, "lineHeight"], tok(float(lh) if "." in lh else int(lh), "number", f"css-var {name}--line-height on :root"))

# spacing: Tailwind --spacing is 0.25rem
spacing = rem(need("light", "--spacing"))
put(core, ["spacing", "unit"], tok(spacing, "dimension", "css-var --spacing on :root (Tailwind spacing unit)"))
unit = re.fullmatch(r"([\d.]+)rem", spacing)
if not unit:
    raise SystemExit(f"--spacing is not a rem length: {spacing!r}")
for step, mult in (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("6", 6), ("8", 8)):
    put(core, ["spacing", step], tok(f"{float(unit.group(1)) * mult:g}rem", "dimension", f"derived: css-var --spacing ({spacing}) multiplied by the Tailwind step {mult}"))

radius = rem(need("light", "--radius"))
put(core, ["radius", "md"], tok(radius, "dimension", "css-var --radius on :root"))
# --radius-sm is calc(var(--radius) - 4px). That is not one length, so it is not a token.
# DTCG dimension must be one length. Use the computed px form from the browser if present.
# --radius-sm computed? We only have the calc. Record the declared --radius and the
# button's measured 12px separately if the computed custom property exists.
for name, key in (("--radius-lg", "lg"), ("--radius-xl", "xl"), ("--radius-2xl", "2xl")):
    raw = getv("light", name)
    if raw and re.fullmatch(r"[\d.]+rem", raw if not raw.startswith(".") else "0" + raw):
        val = raw if not raw.startswith(".") else "0" + raw
        put(core, ["radius", key], tok(val, "dimension", f"css-var {name} on :root"))

# elevation from --shadow-sm / md / lg
LENGTH = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(?:px|rem|em)|-?0")


def split_top(raw, sep):
    """Split at sep outside parentheses."""
    parts, depth, cur = [], 0, ""
    for ch in raw:
        depth += ch == "("
        depth -= ch == ")"
        if ch == sep and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def parse_shadow(raw):
    """Every layer of a CSS box-shadow as a DTCG shadow layer. Keeps inset wherever the keyword
    sits, takes unitless 0 and negative lengths as written, and raises on anything else."""
    layers = []
    for part in split_top(raw, ","):
        inset, col, nums = False, None, []
        for word in split_top(part, " "):
            if word == "inset":
                inset = True
            elif LENGTH.fullmatch(word):
                nums.append("0px" if word in ("0", "-0") else word)
            elif col is None:
                col = color(word)
            else:
                raise ValueError(f"shadow layer not understood: {part!r}")
        if col is None or not 2 <= len(nums) <= 4:
            raise ValueError(f"shadow layer not understood: {part!r}")
        nums += ["0px"] * (4 - len(nums))
        layer = {"color": col, "offsetX": nums[0], "offsetY": nums[1], "blur": nums[2], "spread": nums[3]}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    return layers

for key, name in (("sm", "--shadow-sm"), ("md", "--shadow-md"), ("lg", "--shadow-lg")):
    put(core, ["elevation", key], tok(parse_shadow(need("light", name)), "shadow", f"css-var {name} on :root"))

# motion: the declared default transition duration, and Tailwind's animation-delay steps as delays
def ms(raw):
    m = re.fullmatch(r"(\d*\.?\d+)(m?s)", raw.strip())
    if not m:
        raise SystemExit(f"not a time: {raw!r}")
    return ("%g" % round(float(m.group(1)) * (1 if m.group(2) == "ms" else 1000), 3)) + "ms"

put(core, ["motion", "duration", "base"], tok(ms(need("light", "--default-transition-duration")), "duration",
    "css-var --default-transition-duration on :root (Tailwind default transition duration)"))
for key, name in (("fast", "--animation-delay-75"), ("base", "--animation-delay-150"), ("slow", "--animation-delay-300")):
    put(core, ["motion", "delay", key], tok(ms(need("light", name)), "duration",
        f"css-var {name} on :root (Tailwind animation-delay step: a delay before an animation starts, not a transition duration)"))

# No product easing token was isolated. Do not fill one from Tailwind's default.

# control height from the header button class h-9 = 36px, measured later if present.
# Do not invent. Only record if a component measurement exists.
comp_path = RAW / "components-computed.json"
measured = {}
if comp_path.exists():
    measured = json.loads(comp_path.read_text()).get("components", {})

def measured_px(key, prop):
    st = measured.get(key, {}).get("states", {}).get("default", {})
    if not st or st.get("error"):
        return None
    return st.get(prop)

signup_h = measured_px("nav-signup", "height")
if signup_h and signup_h.endswith("px"):
    put(core, ["size", "control", "header"], tok(signup_h, "dimension", "measured nav-signup default height on lottiefiles.com home, 1440"))
hero_h = measured_px("hero-cta", "height")
if hero_h and hero_h.endswith("px"):
    put(core, ["size", "control", "hero"], tok(hero_h, "dimension", "measured hero-cta default height on lottiefiles.com home, 1440"))
hero_r = measured_px("hero-cta", "borderRadius")
if hero_r and re.fullmatch(r"[\d.]+px", hero_r):
    put(core, ["radius", "button"], tok(hero_r, "dimension", "measured hero-cta border-radius on lottiefiles.com home, 1440"))

# layout breakpoints: Tailwind defaults if declared
for key, name in (("sm", "--breakpoint-sm"), ("md", "--breakpoint-md"), ("lg", "--breakpoint-lg"), ("xl", "--breakpoint-xl")):
    raw = getv("light", name)
    if raw and re.fullmatch(r"[\d.]+(px|rem)", raw if not raw.startswith(".") else "0" + raw):
        val = raw if not raw.startswith(".") else "0" + raw
        put(core, ["layout", "breakpoint", key], tok(val, "dimension", f"css-var {name} on :root"))

def theme_set(theme):
    note = "painted on the public site" if theme == "light" else "stylesheet .dark block, resolved by adding html.dark; the public site did not switch to this theme"
    node = {}
    for role, name in ROLES:
        raw = getv(theme, name)
        if not raw:
            continue
        try:
            val = color(raw)
        except ValueError:
            continue
        put(node, ["background", role], tok(val, "color", f"css-var {name} ({theme}; {note})"))
    for role, name in TEXT:
        raw = getv(theme, name)
        if not raw:
            continue
        try:
            val = color(raw)
        except ValueError:
            continue
        put(node, ["text", role], tok(val, "color", f"css-var {name} ({theme}; {note})"))
    for role, name in ACCENT:
        raw = getv(theme, name)
        if not raw:
            continue
        try:
            val = color(raw)
        except ValueError:
            continue
        put(node, ["accent", role], tok(val, "color", f"css-var {name} ({theme}; {note})"))
    for role, name in BORDER:
        raw = getv(theme, name)
        if not raw:
            continue
        try:
            val = color(raw)
        except ValueError:
            continue
        put(node, ["border", role], tok(val, "color", f"css-var {name} ({theme}; {note})"))
    for role, name in STATUS:
        raw = getv(theme, name)
        if not raw:
            continue
        try:
            val = color(raw)
        except ValueError:
            continue
        put(node, ["status", role], tok(val, "color", f"css-var {name} ({theme}; {note})"))
    # button fills from measurement, light only (the painted theme)
    if theme == "light":
        for key, token_name in (("nav-signup", "signup"), ("hero-cta", "hero"), ("nav-login", "login")):
            bg = measured_px(key, "backgroundColor")
            if not bg:
                continue
            try:
                val = color(bg)
            except ValueError:
                continue
            put(node, ["button", token_name, "background"], tok(val, "color", f"measured {key} default backgroundColor on lottiefiles.com"))
            fg = measured_px(key, "color")
            if fg:
                try:
                    put(node, ["button", token_name, "text"], tok(color(fg), "color", f"measured {key} default color on lottiefiles.com"))
                except ValueError:
                    pass
    return node

light = theme_set("light")
dark = theme_set("dark")

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark (declared, not painted)", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# refuse a colour token that is not hex/rgba
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        if node["$type"] == "color":
            color(node["$value"])
        if "source" not in node.get("$extensions", {}):
            raise SystemExit("missing source at " + path)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)

walk(doc["core"])
walk(doc["light"])
walk(doc["dark"])

out = json.dumps(doc, indent=2) + "\n"
(HERE / "tokens.json").write_text(out)
print("wrote tokens.json", "light roles", len(light), "dark roles", len(dark))
