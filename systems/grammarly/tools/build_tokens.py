#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, all read from www.grammarly.com, signed out, by tools/capture/*:
  raw/css-vars.json            every custom property the public stylesheets declare, plus the
                               values resolved on the home page at 1440 ("resolved.home.1440",
                               the painted light theme) and the same names re-resolved with the
                               declared dark scopes set on <html> ("resolved.home.dark": a
                               synthetic mount of [data-gds-theme="dark"] +
                               [data-origin-theme="grammarly"][data-origin-mode="dark"] that no
                               public page ever applies — declared evidence, never painted)
  raw/layout.json              measured geometry at 1440/1920/1024/390 (header height,
                               containers, h1 metrics)
  raw/components-computed.json measured component styles (button radius, heights, colours)

Grammarly's public stylesheets carry three layered token sets:
  --<hue>-*            legacy GDS primitives: 8-14 step ramps (green, blue, purple, gold, red,
                        teal, magenta, neutral-gray, blue-gray) plus --white/--transparent
  --origin-<hue>-*    the newer Origin primitives: same ramps (blue, green, gold-pro, mulberry,
                        neutral, orange, purple, red, teal, yellow) plus scale, type and shadow
                        primitives (--origin-space-*, --origin-radius-*, --origin-font-*,
                        --origin-heading-*, --origin-elevation-*, --origin-z-index-*, ...)
  --color-*,          the semantic layers. --color-* and --button-* belong to the GDS theme
  --button-*, --tag-* ([data-gds-theme="light"|"dark"]); --origin-color-* belongs to the Origin
                      theme ([data-origin-theme="grammarly"][data-origin-mode="light"|"dark"]).

Both themes ship three brand palettes (grammarly, superhuman, coda); the resolved values here
are the grammarly ones. The public site paints light only — there is no theme switch and
prefers-color-scheme changes nothing (themeChecks in raw/css-vars.json) — so the `dark` token
set is labelled declared-only on every value.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion  # product-free: raw/motion.json -> the core.motion token group

V = json.loads((RAW / "css-vars.json").read_text())
LAYOUT = json.loads((RAW / "layout.json").read_text())
COMPONENTS = json.loads((RAW / "components-computed.json").read_text()).get("components", {})

RESL = V["resolved"]["home"]["1440"]   # painted light theme
RESD = V["resolved"]["home"]["dark"]   # declared dark theme, resolved synthetically

# --------------------------------------------------------------------------- declared records
# For provenance pick the declaration that matches the grammarly light scope, then any grammarly
# scope, then a plain :root. Superhuman/coda-scoped and non-root declarations lose to all of these.


def rank(sel):
    s = sel or ""
    if "superhuman" in s or "coda" in s or "checkout-ui" in s:
        return 9
    if 'data-gds-theme="light"' in s:
        return 0
    if 'data-origin-theme="grammarly"' in s and '"light"' in s:
        return 0
    if 'data-origin-theme="grammarly"' in s:
        return 1
    if re.fullmatch(r":where\(:root, :host\)|:root, \[data-gds-theme=\"light\"\]|:root|:host|:root, :host|:host, :root", s.strip()):
        return 1
    if ":root" in s or ":host" in s:
        return 2
    return 4


DECL = {}
for d in V["decls"]:
    if d["owner"] != "grammarly" or d["media"]:
        continue
    r = rank(d["selector"])
    cur = DECL.get(d["name"])
    if cur is None or r < cur[0]:
        DECL[d["name"]] = (r, d)


def decl(name):
    return DECL.get(name, (None, None))[1]


def dark_decl(name):
    """The grammarly declaration of `name` in a dark scope, if one exists."""
    for dd in V["decls"]:
        if dd["name"] != name or dd["owner"] != "grammarly" or dd["media"]:
            continue
        s = dd["selector"] or ""
        if ('data-gds-theme="dark"' in s or 'data-origin-mode="dark"' in s) and not any(x in s for x in ("superhuman", "coda", "checkout-ui")):
            return dd
    return None


def prov(name, dark=False, d=None):
    """Provenance string for a css-var token. A dark token cites its dark-scope
    declaration when there is one (the light one otherwise: the value is inherited)."""
    d = d or (dark and dark_decl(name)) or decl(name)
    sel = (d["selector"] if d else ":root")
    sel = re.sub(r"\s+", " ", sel).strip()
    if len(sel) > 110:
        sel = sel[:107] + "..."
    base = f"css-var {name} ({sel})"
    if dark:
        base += ("; declared dark scope resolved synthetically on home@1440 "
                 "(data-gds-theme=dark + data-origin-theme=grammarly data-origin-mode=dark) — "
                 "the public site never paints a dark theme")
    else:
        base += "; resolved on home@1440 (painted light theme)"
    return base


# --------------------------------------------------------------------------- value helpers
def norm_color(v):
    """#rgb, #rrggbb(aa), rgb(a)(), hsla(), transparent -> #rrggbb or rgba(r, g, b, a)."""
    v = str(v).strip().lower()
    if v == "transparent":
        return "rgba(0, 0, 0, 0)"
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
    m = re.fullmatch(r"hsla?\(\s*0\s*,\s*0%\s*,\s*([\d.]+)%\s*(?:[,/]\s*([\d.]+%?))?\)", v)
    if m:
        lvl = round(float(m.group(1)) * 2.55)
        a = m.group(2)
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
    raise ValueError("not a colour: " + v)


def px(v):
    """'calc(1px * 16)' / '16px' / '16' -> '16px'."""
    v = str(v).strip()
    m = re.fullmatch(r"calc\(\s*(-?[\d.]+)px?\s*\*\s*(?:var\(--rem,\s*)?([\d.]+)\s*\)\s*", v)
    if m:
        val = round(float(m.group(1)) * float(m.group(2)))
        return f"{val}px"
    m = re.fullmatch(r"(-?[\d.]+)(px|rem)?", v)
    if m:
        return f"{m.group(1)}{m.group(2) or 'px'}"
    return v


def ms(v):
    v = str(v).strip()
    if v.endswith("s") and not v.endswith("ms"):
        return f"{round(float(v[:-1]) * 1000)}ms"
    return v


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


tokens = {"core": {}, "light": {}, "dark": {}}


def put(set_name, path, ty, value, source, desc=None, extra=None):
    """Insert a token at dotted path; value may be a literal or an {alias}."""
    if not str(value).startswith("{"):
        if ty == "color":
            value = norm_color(value)
        elif ty == "dimension":
            value = px(value)
        elif ty == "duration":
            value = ms(value)
        elif ty in ("fontWeight", "number"):
            if isinstance(value, str) and re.fullmatch(r"-?\d+", value):
                value = int(value)
            elif isinstance(value, str) and re.fullmatch(r"-?\d+\.\d+", value):
                value = float(value)
    check(f"{set_name}.{path}", ty, value)
    node = tokens[set_name]
    parts = path.split(".")
    for i, p in enumerate(parts[:-1]):
        if "$value" in node.get(p, {}):
            # a token is never also a group (catalog flatten stops at $value, so
            # children would vanish): --x-default-f3 becomes a sibling, default-f3
            parts = parts[:i] + ["-".join(parts[i:])]
            break
        node = node.setdefault(p, {})
    if any(not k.startswith("$") for k in node.get(parts[-1], {})):
        raise ValueError(f"{set_name}.{path}: a group already sits at this path")
    leaf = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if desc:
        leaf["$description"] = desc
    if extra:
        leaf["$extensions"].update(extra)
    node[parts[-1]] = leaf
    return leaf


def var(set_name, path, ty, name, desc=None, dark=False, extra=None):
    """A token whose value is a css-var's resolved value."""
    res = RESD if dark else RESL
    # never fill one theme from the other's resolution: a missing reading is an error
    if res.get(name) is None:
        raise KeyError(f"{set_name}.{path}: {name} not resolved in the {'dark' if dark else 'light'} pass")
    return put(set_name, path, ty, res[name], prov(name, dark), desc, extra)


def alias_var(set_name, path, name, desc=None, dark=False):
    """A token whose declared value is var(--x): emit {alias} when --x maps to a palette token."""
    alias_map = PALETTE_VAR
    d = decl(name)
    val = d["value"].strip() if d else ""
    m = re.fullmatch(r"var\((--[\w-]+)\)", val)
    target = hit = None
    if m:
        # pick the decl that matches this theme
        for dd in V["decls"]:
            if dd["name"] != name or dd["owner"] != "grammarly" or dd["media"]:
                continue
            s = dd["selector"] or ""
            is_dark_sel = 'data-gds-theme="dark"' in s or 'data-origin-mode="dark"' in s
            if bool(is_dark_sel) == bool(dark) and "superhuman" not in s and "coda" not in s and "checkout-ui" not in s:
                mm = re.fullmatch(r"var\((--[\w-]+)\)", dd["value"].strip())
                if mm:
                    target = alias_map.get(mm.group(1))
                    if target:
                        hit = (dd, mm.group(1))
                        break
    if target:
        # cite the declaration the alias was built from, not the light one
        return put(set_name, path, "color", "{" + target + "}", prov(name, dark, hit[0]) + f"; declared as var({hit[1]})", desc)
    return var(set_name, path, "color", name, desc, dark)


# --------------------------------------------------------------------------- core.palette
PALETTE_VAR = {}  # css var name -> token path, for aliases


def ramp(set_path, var_prefix, steps, dark=False, label=None):
    for st in steps:
        name = f"{var_prefix}{st}"
        if name in RESL:
            PALETTE_VAR[name] = f"palette.{set_path}.{st}"
            var("core", PALETTE_VAR[name], "color", name,
                desc=label and f"{label} {st}" or None)


RAMP_STEPS = ["0", "5", "10", "15", "20", "30", "35", "40", "50", "60", "70", "80", "85", "90", "95", "100"]

# Origin ramps (the newer Origin primitives, theme-independent)
ORIGIN_RAMPS = {
    "blue": "--origin-blue-", "green": "--origin-green-", "gold": "--origin-gold-pro-",
    "mulberry": "--origin-mulberry-", "neutral": "--origin-neutral-", "orange": "--origin-orange-",
    "purple": "--origin-purple-", "red": "--origin-red-", "teal": "--origin-teal-",
    "yellow": "--origin-yellow-",
}
for hue, pre in ORIGIN_RAMPS.items():
    ramp(hue, pre, RAMP_STEPS, label=f"the Origin {hue} ramp")
ramp("green.grammarly", "--origin-green-grammarly-", ["0"], label="Grammarly's brand green")
ramp("orange.coda", "--origin-orange-coda-", ["0"], label="Coda's brand orange (sibling theme in the same Origin system)")
ramp("purple.enterprise", "--origin-purple-enterprise-", RAMP_STEPS, label="the enterprise purple ramp")
ramp("lightgreen", "--origin-lightgreen-", ["0"], label="Origin lightgreen")
ramp("yellowgreen", "--origin-yellowgreen-", ["0"], label="Origin yellowgreen")

# Legacy GDS ramps (the older primitives the semantic layer references)
GDS_RAMPS = {
    "blue": "--blue-", "blue-gray": "--blue-gray-", "gold": "--gold-", "green": "--green-",
    "magenta": "--magenta-", "neutral-gray": "--neutral-gray-", "purple": "--purple-",
    "red": "--red-", "teal": "--teal-", "yellow": "--yellow-",
}
for hue, pre in GDS_RAMPS.items():
    ramp("gds." + hue, pre, RAMP_STEPS, label=f"the legacy GDS {hue} ramp")
var("core", "palette.gds.yellow-green", "color", "--yellow-green", desc="legacy GDS yellow-green")
var("core", "palette.white", "color", "--white")
var("core", "palette.transparent", "color", "--transparent")
PALETTE_VAR["--white"] = "palette.white"
PALETTE_VAR["--transparent"] = "palette.transparent"
tokens["core"]["palette"]["$description"] = (
    "Two primitive layers: the Origin ramps (--origin-*) and the legacy GDS ramps under `gds` "
    "(--*). Both are declared :root-wide; the semantic sets reference the GDS names."
)

# --------------------------------------------------------------------------- core type/space/etc
var("core", "fontFamily.heading", "fontFamily", "--origin-font-family-heading-default",
    desc="Matter, Grammarly's display face: hero titles, big headings")
var("core", "fontFamily.sans", "fontFamily", "--origin-font-family-sans-default",
    desc="Inter: UI and body text")
var("core", "fontFamily.sans-secondary", "fontFamily", "--origin-font-family-sans-secondary",
    desc="Matter as a secondary sans")
var("core", "fontFamily.mono", "fontFamily", "--origin-font-family-mono-default",
    desc="Super Sans Mono VF over ui-monospace fallbacks")
var("core", "fontFamily.serif", "fontFamily", "--origin-font-family-serif-default",
    desc="Super Serif VF over Charter/Cambria/Georgia")
var("core", "fontFamily.gds-matter", "fontFamily", "--font-stack-matter", desc="the legacy GDS Matter stack")
var("core", "fontFamily.gds-inter", "fontFamily", "--font-stack-inter", desc="the legacy GDS Inter stack")
var("core", "fontFamily.glyph", "fontFamily", "--font-stack-glyph", desc="the legacy GDS icon-glyph stack")

for w, nm in [("light", "light"), ("regular", "regular"), ("medium", "medium"), ("semibold", "semibold"), ("bold", "bold")]:
    var("core", f"fontWeight.{w}", "fontWeight", f"--origin-font-weight-{nm}")
tokens["core"]["fontWeight"]["$description"] = "Origin font weights; headings draw at 600."

for role in ["xxsmall", "xsmall", "small", "medium", "large", "xlarge"]:
    var("core", f"fontSize.heading-{role}", "dimension", f"--origin-heading-size-{role}")
for role in ["xsmall", "small", "medium", "large"]:
    var("core", f"fontSize.text-{role}", "dimension", f"--origin-text-size-{role}")
for role in ["xsmall", "small", "medium", "large"]:
    var("core", f"fontSize.paragraph-{role}", "dimension", f"--origin-paragraph-{role}")
tokens["core"]["fontSize"]["$description"] = (
    "Origin type sizes: heading roles (14-28px, Matter by default), text roles (12-18px, Inter) "
    "and the paragraph sizes (16-36px) the marketing pages use for ledes."
)

for role in ["xxsmall", "xsmall", "small", "medium", "large", "xlarge"]:
    var("core", f"lineHeight.heading-{role}", "dimension", f"--origin-line-height-heading-{role}")
for role in ["xsmall", "small", "medium", "large"]:
    var("core", f"lineHeight.text-{role}", "dimension", f"--origin-line-height-text-{role}")
for role in ["xxsmall", "xsmall", "small", "medium", "large", "xlarge"]:
    var("core", f"letterSpacing.heading-{role}", "dimension", f"--origin-letter-spacing-heading-{role}")
for role in ["xsmall", "small", "medium", "large"]:
    var("core", f"letterSpacing.text-{role}", "dimension", f"--origin-letter-spacing-text-{role}")
tokens["core"]["letterSpacing"]["$description"] = "All Origin tracking values resolve to 0."

# Origin spacing scale + the gap/shortcut roles
for n in sorted(RESL):
    if re.fullmatch(r"--origin-space-[\w-]+", n):
        var("core", f"spacing.{n[len('--origin-space-'):]}", "dimension", n)
tokens["core"]["spacing"]["$description"] = (
    "The Origin spacing scale: space-N is N x 4px (space-4 = 16px), plus the gap, shortcut-gap "
    "and x-padding roles (--origin-space-gap-*, --origin-space-shortcut-gap-*, --origin-space-x-*)."
)
# Legacy GDS space scale (calc(N * --rem)); resolved to px here.
for n in sorted(RESL):
    if re.fullmatch(r"--space-[\w-]+", n):
        path = n[len("--space-"):]
        var("core", f"space.gds.{path}", "dimension", n)
put("core", "space.rem-base", "number", 16, "css-var --rem (:root); resolved on home@1440",
    desc="the multiplier in the legacy --space-* calc()s")
tokens["core"]["space"]["$description"] = "The legacy GDS spacing scale: --space-N = N x 4px written as calc(Npx * var(--rem, 16)); values resolved to px."

# Radius
for n in sorted(RESL):
    if re.fullmatch(r"--origin-radius-[\w-]+", n):
        var("core", f"radius.{n[len('--origin-radius-'):]}", "dimension", n)
tokens["core"]["radius"]["$description"] = (
    "The Origin radius scale (radius-1 = 4px through radius-25 = 100px) plus the named roles "
    "(small/medium/large and button-small..xlarge: 4/6/8/8px)."
)
for n in sorted(RESL):
    if re.fullmatch(r"--radius-[\w-]+", n):
        var("core", f"radiusGds.{n[len('--radius-'):]}", "dimension", n)
tokens["core"]["radiusGds"]["$description"] = "The legacy GDS radius scale: --radius-N = N x 4px written as calc(); values resolved to px."

# Control sizes
for n in sorted(RESL):
    if re.fullmatch(r"--origin-size-[\w-]+", n):
        var("core", f"size.{n[len('--origin-size-'):]}", "dimension", n)
tokens["core"]["size"]["$description"] = "Origin control heights: small 24, medium 32, large 40, xlarge 48, xxlarge 52px."
for n in sorted(RESL):
    if re.fullmatch(r"--origin-multiselect-checkbox-[\w-]+", n):
        var("core", f"size.multiselect-checkbox.{n.split('-')[-1]}", "dimension", n)

# Elevation / shadows (stored as $type "other": the raw shadow strings carry their own
# comma-separated layers, incl. the 0.5px spreads DTCG shadow objects cannot round-trip)
for n in sorted(RESL):
    if re.fullmatch(r"--origin-elevation-base-[\w-]+", n):
        leaf = {"$value": str(RESL[n]), "$type": "other", "$extensions": {"source": prov(n)}}
        node = tokens["core"].setdefault("elevation", {}).setdefault("base", {})
        node[n[len("--origin-elevation-base-"):]] = leaf
for n in sorted(RESL):
    m = re.fullmatch(r"--origin-elevation-border-(low|medium|high)-(default|subdued)", n)
    if m:
        leaf = {"$value": str(RESL[n]), "$type": "other", "$extensions": {"source": prov(n)},
                "$description": "Origin elevated shadow + 1px outline pair"}
        tokens["core"].setdefault("elevation", {}).setdefault("border", {})[f"{m.group(1)}-{m.group(2)}"] = leaf
for n in sorted(RESL):
    m = re.fullmatch(r"--elevation-(low|medium|high)-(shadow|border)", n)
    if m:
        leaf = {"$value": str(RESL[n]), "$type": "other", "$extensions": {"source": prov(n)}}
        tokens["core"].setdefault("elevation", {}).setdefault("gds", {}).setdefault(m.group(1), {})[m.group(2)] = leaf
for n in sorted(RESL):
    m = re.fullmatch(r"--elevation(\d00)-(shadow|border)", n)
    if m:
        leaf = {"$value": str(RESL[n]), "$type": "other", "$extensions": {"source": prov(n)}}
        tokens["core"].setdefault("elevation", {}).setdefault("gds", {}).setdefault(m.group(1), {})[m.group(2)] = leaf
tokens["core"]["elevation"]["$description"] = (
    "Origin elevations are pure shadows (#1c1c1c at 15%); the `border` variants pair the shadow "
    "with a 1px outline. `gds` holds the legacy --elevation-(low|medium|high|100-300) shadow+border pairs."
)

# Motion
var("core", "duration.fast", "duration", "--animation-duration", desc="the GDS default transition length")
var("core", "duration.accordion", "duration", "--origin-accordion-animation-duration", desc="Origin accordion open/close")
var("core", "duration.multiselect", "duration", "--origin-multiselect-animation-duration")
var("core", "duration.paywall-loading", "duration", "--paywall-loading-time", desc="the paywall's loading shimmer length")
for n, path in [("--origin-accordion-animation-easing", "easing.accordion"),
                ("--origin-multiselect-animation-easing", "easing.multiselect")]:
    m = re.fullmatch(r"cubic-bezier\(([\d.]+),\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\)", str(RESL.get(n, "")))
    if m:
        put("core", path, "cubicBezier", [float(x) for x in m.groups()], prov(n))
tokens["core"]["duration"]["$description"] = "The GDS transition is 200ms; the Origin accordion and multiselect use 300ms."
tokens["core"]["easing"]["$description"] = "cubic-bezier(0.87, 0, 0.13, 1) — a hard ease-out the Origin animations share."

# z-index (the 'auto' keyword resolves to a string, so only the numeric rungs land here)
for n in sorted(RESL):
    if re.fullmatch(r"--origin-z-index-[\w-]+", n) and re.fullmatch(r"-?\d+", str(RESL[n])):
        var("core", f"zIndex.{n[len('--origin-z-index-'):]}", "number", n)
for n in sorted(RESL):
    if re.fullmatch(r"--z-index-[\w-]+", n) and re.fullmatch(r"-?\d+", str(RESL[n])):
        var("core", f"zIndex.gds.{n[len('--z-index-'):]}", "number", n)
tokens["core"]["zIndex"]["$description"] = "Origin z scale plus the legacy GDS named layers (modal 1000, popover 1010, tooltip 1020)."

# Blur / axis / spread primitives
for grp, pre in [("blur", "--origin-blur-"), ("axis", "--origin-axis-"), ("spread", "--origin-spread-")]:
    for n in sorted(RESL):
        if re.fullmatch(re.escape(pre) + r"[\w-]+", n):
            var("core", f"{grp}.{n[len(pre):]}", "dimension", n)

# Breakpoints seen in the media conditions
bps = sorted({int(float(x)) for d in V["decls"] if d["owner"] == "grammarly" and d["media"]
              for x in re.findall(r"(?:min|max)-width:\s*([\d.]+)px", d["media"])})
for b in bps:
    put("core", f"breakpoint.w{b}", "dimension", f"{b}px",
        "media condition in the public stylesheets (raw/css-vars.json)")
tokens["core"]["breakpoint"]["$description"] = "Page-level width breakpoints that appear in the public CSS."

# Layout measured on the page (raw/layout.json: keys are "<page>@<width>")
home1440 = LAYOUT.get("home@1440", {})
hdr = home1440.get("header", {})
if isinstance(hdr, dict) and hdr.get("h"):
    put("core", "layout.nav-height", "dimension", f"{round(hdr['h'])}px",
        "measured raw/layout.json home@1440 sticky header height")
seen_mw = set()
for e in home1440.get("maxWidths", []):
    try:
        mw = round(float(str(e.get("max", "")).rstrip("px")))
    except ValueError:
        continue
    if mw in seen_mw:
        continue
    seen_mw.add(mw)
    put("core", f"layout.container-{mw}", "dimension", f"{mw}px",
        f"measured raw/layout.json home@1440 max-width on {e.get('el', 'container')}")
if seen_mw:
    tokens["core"]["layout"]["$description"] = "Measured container widths and the header height at 1440."

# --------------------------------------------------------------------------- semantic sets
# GDS semantic layer (--color-*) -> light.color.* / dark.color.*
for n in sorted(RESL):
    m = re.fullmatch(r"--color-(.*)", n)
    if not m:
        continue
    path = m.group(1).replace("-", ".")
    alias_var("light", f"color.{path}", n)
for n in sorted(RESD):
    m = re.fullmatch(r"--color-(.*)", n)
    if not m:
        continue
    path = m.group(1).replace("-", ".")
    alias_var("dark", f"color.{path}", n, dark=True)
tokens["light"]["color"]["$description"] = (
    "The GDS semantic palette (--color-*), painted on the public pages: background, text, "
    "border, icon, highlight, elevation, illustration and logo roles."
)
tokens["dark"]["color"]["$description"] = (
    "The GDS semantic palette's declared dark values ([data-gds-theme=\"dark\"]). Resolved "
    "synthetically; the public site never mounts the attribute or paints dark."
)

# Origin semantic layer (--origin-color-*) -> light.origin.* / dark.origin.*
for n in sorted(RESL):
    m = re.fullmatch(r"--origin-color-(.*)", n)
    if not m:
        continue
    alias_var("light", f"origin.{m.group(1).replace('-', '.')}", n)
for n in sorted(RESD):
    m = re.fullmatch(r"--origin-color-(.*)", n)
    if not m:
        continue
    alias_var("dark", f"origin.{m.group(1).replace('-', '.')}", n, dark=True)
tokens["light"]["origin"]["$description"] = (
    "The Origin semantic palette (--origin-color-*) for data-origin-theme=grammarly, "
    "light mode: background, fill, border, button, text, icon, link, highlight, tag and the "
    "per-hue contrast roles. Declared alongside GDS; resolved on the painted light site."
)
tokens["dark"]["origin"]["$description"] = (
    "The Origin semantic palette's declared dark values ([data-origin-mode=\"dark\"]). Resolved "
    "synthetically; the public site never mounts the attributes or paints dark."
)

# Button layer (--button-*) -> light.button.* / dark.button.*
for n in sorted(RESL):
    m = re.fullmatch(r"--button-(.*)", n)
    if not m:
        continue
    alias_var("light", f"button.{m.group(1).replace('-', '.')}", n)
for n in sorted(RESD):
    m = re.fullmatch(r"--button-(.*)", n)
    if not m:
        continue
    alias_var("dark", f"button.{m.group(1).replace('-', '.')}", n, dark=True)
for s in ("light", "dark"):
    tokens[s]["button"]["$description"] = (
        "The GDS button tokens (--button-*): each variant's background/border/text at "
        "default/hover/active, plus the `shortcut` pairs used inside key-cap hints." + (
            "" if s == "light" else " Declared dark values, resolved synthetically."))

# Tags (--tag-*)
for n in sorted(RESL):
    m = re.fullmatch(r"--tag-(.*)", n)
    if not m:
        continue
    alias_var("light", f"tag.{m.group(1).replace('-', '.')}", n)
for n in sorted(RESD):
    m = re.fullmatch(r"--tag-(.*)", n)
    if not m:
        continue
    alias_var("dark", f"tag.{m.group(1).replace('-', '.')}", n, dark=True)
for s in ("light", "dark"):
    tokens[s]["tag"]["$description"] = "The GDS tag fills (--tag-*-bg) and pro tag text."

# Paywall dims
var("light", "paywall.content-max-width", "dimension", "--paywall-content-max-width")

# --------------------------------------------------------------------------- measured component tokens
def comp_state(key, state="default"):
    return COMPONENTS.get(key, {}).get("states", {}).get(state, {})


def comp_css(key, prop, state="default"):
    return comp_state(key, state).get("style", {}).get(prop)


def comp_rect(key, dim, state="default"):
    v = comp_state(key, state).get("rect", {}).get(dim)
    return round(v) if isinstance(v, (int, float)) else None


def measured(set_name, path, ty, val, src, desc=None):
    if val is None:
        return
    put(set_name, path, ty, val, src, desc)


# Primary button: the hero CTA / nav Sign Up
h = comp_rect("btn-hero", "h") or comp_rect("nav-signup", "h")
measured("light", "component.button.primary.height", "dimension", f"{h}px" if h else None,
         "measured raw/components-computed.json btn-hero/nav-signup height")
r = comp_css("btn-hero", "borderTopLeftRadius") or comp_css("nav-signup", "borderTopLeftRadius")
measured("light", "component.button.primary.radius", "dimension", r,
         "measured raw/components-computed.json btn-hero/nav-signup borderTopLeftRadius")
bg = comp_css("nav-signup", "backgroundColor") or comp_css("btn-hero", "backgroundColor")
if bg:
    measured("light", "component.button.primary.background", "color", bg,
             "measured raw/components-computed.json nav-signup backgroundColor (painted; equals button.primary.background.default)")
# Secondary/Google button
bg2 = comp_css("btn-google", "borderTopColor")
measured("light", "component.button.secondary.border", "color", bg2,
         "measured raw/components-computed.json btn-google border colour")
# Field
fb = comp_css("form-input", "borderTopColor") or comp_css("signin-email", "borderTopColor")
measured("light", "component.field.border", "color", fb,
         "measured raw/components-computed.json form-input border colour")
fr = comp_css("form-input", "borderTopLeftRadius") or comp_css("signin-email", "borderTopLeftRadius")
measured("light", "component.field.radius", "dimension", fr,
         "measured raw/components-computed.json form-input radius")
fh = comp_rect("form-input", "h") or comp_rect("signin-email", "h")
measured("light", "component.field.height", "dimension", f"{fh}px" if fh else None,
         "measured raw/components-computed.json form-input height")
# Focus ring: focus-visible outline on a measured control
fo = comp_css("nav-signup", "outlineColor", "focus-visible") or comp_css("btn-hero", "outlineColor", "focus-visible")
measured("light", "component.focus.color", "color", fo,
         "measured raw/components-computed.json focus-visible outline colour")
# Header / hero
hh = comp_rect("header", "h")
measured("light", "component.header.height", "dimension", f"{hh}px" if hh else None,
         "measured raw/components-computed.json header height@1440")
tokens["light"].get("component", {}).update({})
if "component" in tokens["light"]:
    tokens["light"]["component"]["$description"] = (
        "Values measured on painted components (raw/components-computed.json, "
        "raw/measurements.md); where a semantic token declares the same thing both are kept — "
        "declared under color/button/origin, painted under component."
    )

# --------------------------------------------------------------------------- typography composites
ROLES = [
    ("heading-xlarge", "heading", "xlarge"), ("heading-large", "heading", "large"),
    ("heading-medium", "heading", "medium"), ("heading-small", "heading", "small"),
    ("heading-xsmall", "heading", "xsmall"), ("heading-xxsmall", "heading", "xxsmall"),
    ("text-large", "text", "large"), ("text-medium", "text", "medium"),
    ("text-small", "text", "small"), ("text-xsmall", "text", "xsmall"),
]
for name, kind, role in ROLES:
    fam = "fontFamily.heading" if kind == "heading" else "fontFamily.sans"
    wt = "fontWeight.semibold" if kind == "heading" else "fontWeight.regular"
    put("core", f"typography.{name}", "typography", {
        "fontFamily": "{" + fam + "}",
        "fontSize": "{" + f"fontSize.{kind}-{role}" + "}",
        "fontWeight": "{" + wt + "}",
        "lineHeight": "{" + f"lineHeight.{kind}-{role}" + "}",
        "letterSpacing": "{" + f"letterSpacing.{kind}-{role}" + "}",
    }, f"composed from the Origin {kind} role vars (--origin-{kind}-size-{role} + font/line/letter vars); "
       "weights: Origin headings 600, text 400")
tokens["core"]["typography"]["$description"] = "The Origin heading and text roles composed from the family/size/weight/line tokens."

# Motion, as measured on the page (raw/motion.json via the probe; motion.py is product-free)
if (RAW / "motion.json").exists():
    tokens["core"]["motion"], motion_not_core = motion.build(json.loads((RAW / "motion.json").read_text()))
    # what DTCG cannot carry (steps()/linear() easings, the >60 transitions note) is listed, not dropped
    if motion_not_core:
        tokens["core"].setdefault("$extensions", {}).setdefault("notTokenised", []).extend(motion_not_core)

# --------------------------------------------------------------------------- aliases must resolve
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


NAMES = {n for s in ("core", "light", "dark") for n, _ in tokens_of(tokens[s])}
for s in ("core", "light", "dark"):
    for n, t in tokens_of(tokens[s]):
        for a in aliases(t["$value"]):
            if a not in NAMES:
                raise KeyError(f"{s}.{n}: alias {{{a}}} points at nothing")

out = {
    "core": tokens["core"], "light": tokens["light"], "dark": tokens["dark"],
    "$themes": [
        {"id": "light", "name": "Light",
         "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only theme grammarly.com's public pages paint; no switch, no prefers-color-scheme response"},
        {"id": "dark", "name": "Dark (declared)",
         "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The dark values the public stylesheets declare under [data-gds-theme=\"dark\"] and "
                         "[data-origin-mode=\"dark\"], resolved synthetically. No public page mounts those "
                         "attributes or paints dark — declared evidence, never painted."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")


def count(d):
    if isinstance(d, dict) and "$value" not in d:
        return sum(count(v) for k, v in d.items() if not k.startswith("$"))
    return 1


print({s: count(v) for s, v in out.items() if s in ("core", "light", "dark")})
