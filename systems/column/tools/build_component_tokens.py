"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

column.com is a Gatsby marketing build styled with styled-components plus a
Tailwind-style layer — and it ships a real named token system in its sheets:
`:root` custom properties for the whole scale layer

  --color-<family>-<50..900>   ten colour ramps (blue, cyan, gray, green,
                               orange, pink, purple, red, seafoam, yellow)
                               + --color-0/1000 (white/black)
  --space-*                    a 71-step spacing scale
  --text-*                     the font-size scale, --lh-b-*/--lh-h-* the
                               body/heading line-heights, --letter-spacing-*
  --font-{sans,mono,ui} + --font-{book,regular,medium,semibold,bold}
  --radii-*, --screen-*, --cols-*/--span-*, --shadow-product(-border)

and a semantic layer that `.color-palette--<family>` (primary = blue) and
`.color-palette-inverted--*` classes rebind per band:

  --bg-color-*/--bg-gradient-primary, --text-color-*, --btn-* (bg/border/
  text/focus-ring x primary/secondary x hover/active), --form-*, --link-*,
  --icon-gradient-stop-*, --list-item-*

vars.mjs resolves every var() chain, so `raw/css-vars.json`'s `resolved.light`
carries both the declared raw and the computed value per name; the tokens
below cite the custom property as provenance (declared) or the measured
element (computed, raw/components-computed.json).

The site paints ONE light theme; the infrastructure band and footer sit on
`color-palette-inverted` dark islands inside it. dashboard.column.com/login
is a separate app surface (the sign-in boundary), measured at rest and
never submitted.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# column paints light only (catalog theme list): resolve against the light pass, never a dark probe.
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}
RAW_DECL = {n: v.get("raw") for n, v in RL.items()}


def dvar(name):
    """Resolved value of declared custom property `name` (`--color-blue-800`),
    None when the sheets don't declare it."""
    return R.get(name)


def decl_source(name):
    raw = RAW_DECL.get(name)
    return (f"declared {name}" + (f" ({raw})" if raw and raw != R.get(name) else "")
            + " (raw/css-vars.json :root)")


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. column.com "
    "declares a named token layer in its stylesheets (raw/css-vars.json): "
    "ten colour ramps, a 71-step space scale, text/lh/letter-spacing type "
    "scales, font stacks and weights, radii, screens, grid columns and the "
    "product shadow — plus a semantic layer (--bg-color-*, --text-color-*, "
    "--btn-*, --form-*, --link-*) that .color-palette--primary binds for the "
    "light theme and .color-palette-inverted--* rebinds on dark islands. "
    "Semantic roles are emitted as declared (with the var() chain in their "
    "source) beside the roles measured on the painted chrome in "
    "raw/components-computed.json. One theme exists (light); the "
    "infrastructure band and footer are dark islands inside it."),
    "core": {}, "light": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `paint.N.prop` (the Nth
    painted child layer) or the special `ringShadow`: resolve the dotted path
    inside the measured state (the anchors keep UA-default colour, so painted
    text/fill lives on the text child, a sibling layer or a pseudo).
    `ringShadow` returns the colour of the `0 0 0 Npx` ring layer in the
    element's own boxShadow — the hairline many controls paint instead of a
    real border."""
    d = C[comp]["states"][state]
    for suffix, pick in ((".firstColor", 0), (".lastColor", -1)):
        if prop.endswith(suffix):
            v = stprop(comp, state, prop[: -len(suffix)])
            cols = re.findall(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
            return cols[pick] if cols else ""
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
    if "." not in prop:
        return d.get("style", {}).get(prop, "")
    node = d
    for part in prop.split("."):
        if isinstance(node, list) and part.isdigit():
            node = node[int(part)] if int(part) < len(node) else None
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return ""
        if node is None:
            return ""
    if isinstance(node, str) and prop.endswith(".border"):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", node)
        return m.group(0) if m else ""
    return node if isinstance(node, str) else ""


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\)", v)
    if m:
        r, g, b = m.groups()
        return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and ("var" in v or "value" in v):
            val = norm_color(R[v["var"]]) if "var" in v else norm_color(v["value"])
            BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")


# -------------------------------------------------- declared colour ramps
#
# --color-<family>-<50..900> resolves to the sRGB step; emit the whole ramp
# under core.color.<family>.<step> with the custom property as provenance.
core_color = SPEC["core"].setdefault("color", {})
COLOR_FAMILIES = {
    "blue":    "The brand ramp: blue-500 #4575cd, blue-600 #1e4199 (links, focus), blue-800 #111a4a (the navy ink), blue-900 #080b32.",
    "gray":    "The neutral ramp: gray-50 #f6f6f8 (the app page ground), gray-100 #eeeff2 (secondary bg), gray-900 #12161e (the heading ink).",
    "cyan":    "The cyan ramp — cyan-900 #011821 is the dark infrastructure band.",
    "seafoam": "The seafoam ramp — the green accent family.",
    "purple":  "The purple accent ramp.",
    "pink":    "The pink accent ramp.",
    "red":     "The red ramp (errors/danger).",
    "orange":  "The orange ramp (warnings).",
    "yellow":  "The yellow ramp.",
    "green":   "The green ramp (success).",
}
for _fam, _desc in COLOR_FAMILIES.items():
    for _step in sorted({int(re.match(rf"--color-{_fam}-(\d+)$", n).group(1))
                         for n in R if re.match(rf"--color-{_fam}-\d+$", n)}):
        _name = f"--color-{_fam}-{_step}"
        _v = norm_color(dvar(_name))
        if not _v:
            continue
        node, last = descend(core_color, [_fam, str(_step)])
        node[last] = {"value": _v, "type": "color",
                      "source": decl_source(_name),
                      "description": f"Declared {_fam}-{_step}. {_desc}"}
for _path, _name, _desc in [
    ("white", "--color-0", "Declared color-0 / color-white (#fff) — the card ground and inverted ink."),
    ("black", "--color-1000", "Declared color-1000 / color-black (#000)."),
]:
    _v = norm_color(dvar(_name))
    if _v:
        node, last = descend(core_color, [_path])
        node[last] = {"value": _v, "type": "color",
                      "source": decl_source(_name), "description": _desc}

# The declared primary gradient: linear-gradient(165deg, #4575cd 0%, #7ea7e9 92%).
_g = dvar("--bg-gradient-primary") or (RAW_DECL.get("--bg-gradient-primary") or "")
_m = re.match(r"linear-gradient\((\d+)deg,\s*(.+)\)", _g)
if _m:
    _found = re.findall(r"(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})(?:\s+([\d.]+)%)?", _m.group(2))
    _stops = [{"color": norm_color(c), "position": float(p) / 100 if p else round(i / max(len(_found) - 1, 1), 2)} for i, (c, p) in enumerate(_found)]
    if _stops:
        SPEC["core"].setdefault("gradient", {})["primary"] = {
            "type": "gradient", "value": _stops, "angle": _m.group(1) + "deg",
            "source": decl_source("--bg-gradient-primary"),
            "description": "The declared primary brand gradient — blue-500 #4575cd to a lighter blue at 165deg."}

collect(core_color, "color.")


# ------------------------------------------------------------- light roles
#
# Two provenance kinds: `drole` emits the site's own semantic names as
# DECLARED roles (the --text-color-*/--bg-color-*/--btn-*/--form-*/--link-*
# properties), `role` emits MEASURED roles read off the painted chrome. Both
# alias the core ramp when the resolved value matches a declared step.
def role(path, comp, state, prop, desc):
    v = stprop(comp, state, prop)
    if "shadow" in prop.lower():
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    theme, _, rest = path.partition(":")
    node = SPEC[theme or "dark"]
    parts = rest.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def drole(path, name, desc):
    v = norm_color(dvar(name))
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    src = decl_source(name)
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = src + f"; same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = src
    theme, _, rest = path.partition(":")
    node = SPEC[theme or "dark"]
    parts = rest.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


# --- declared semantic layer (`.color-palette--primary`, i.e. the light theme)
for path, name, desc in [
    ("light:surface.page", "--bg-color-primary", "The declared primary background — blue-50 #eef4fb, the site's tinted page ground."),
    ("light:surface.secondary", "--bg-color-secondary", "The declared secondary background — gray-100 #eeeff2 panels."),
    ("light:surface.muted", "--bg-color-muted", "The declared muted background — gray-100."),
    ("light:text.body", "--text-color-body", "The declared body ink — #575a64 on the light ground."),
    ("light:text.heading", "--text-color-heading", "The declared heading ink — gray-900 #12161e."),
    ("light:text.subheading", "--text-color-subheading", "The declared subheading ink — gray-900."),
    ("light:text.duotonePrimary", "--text-color-duotone-primary", "The declared duotone text primary."),
    ("light:text.duotoneSecondary", "--text-color-duotone-secondary", "The declared duotone text secondary."),
    ("light:accent", "--btn-bg-primary", "The primary button fill — blue-800 #111a4a, the navy the CTAs paint."),
    ("light:accentHover", "--btn-bg-primary-hover", "The primary button's declared hover fill."),
    ("light:accentActive", "--btn-bg-primary-active", "The primary button's declared active fill."),
    ("light:border.accent", "--btn-border-primary", "The primary button's declared border."),
    ("light:focus", "--btn-focus-ring-primary", "The declared primary focus ring — blue-100 #d4e3f7."),
    ("light:text.onAccent", "--btn-text-color-primary", "White text on the navy primary buttons."),
    ("light:text.secondaryButton", "--btn-text-color-secondary", "The secondary button's text (#232730)."),
    ("light:surface.secondaryButton", "--btn-bg-secondary", "The secondary button fill — white at 50% over the tinted ground."),
    ("light:border.input", "--form-input-border", "The declared input border — gray-300 #cfd0d8."),
    ("light:border.inputHover", "--form-input-border-hover", "The declared input hover border — gray-500."),
    ("light:border.inputFocus", "--form-input-border-focus", "The declared input focus border — blue-600 #1e4199."),
    ("light:focusInput", "--form-input-focus-ring", "The declared input focus ring — blue-100."),
    ("light:text.placeholder", "--form-placeholder-text", "The declared placeholder ink — gray-500 #7c7f88."),
    ("light:text.label", "--form-label", "The declared form label ink — gray-900."),
    ("light:text.link", "--link-color", "The declared link colour — blue-600 #1e4199."),
    ("light:text.linkHover", "--link-color-hover", "The declared link hover colour."),
]:
    drole(path, name, desc)

# --- measured roles on the painted chrome (verify/extend the declared layer)
for path, comp, state, prop, desc in [
    ("light:surface.card", "page-ground", "default", "backgroundColor", "The marketing page ground — white."),
    ("light:surface.darkBand", "dark-band", "default", "backgroundColor", "The dark infrastructure band's fill — cyan-900 #011821."),
    ("light:surface.banner", "promo-banner", "default", "backgroundImage.firstColor", "The launch banner's painted stop — the first colour of its blue-violet gradient."),
    ("light:text.onDark", "dark-title", "default", "color", "Text on the dark infrastructure band."),
    ("light:text.banner", "promo-banner", "default", "color", "The launch banner's text colour."),
    ("light:text.nav", "nav-item", "default", "color", "The nav-link ink at rest."),
    ("light:text.footer", "footer-link", "default", "color", "Footer link ink."),
    ("light:border.subtle", "header", "default", "paint.0.border", "The 1px hairline under the header."),
    ("light:accentSignin", "signin-submit", "default", "paint.0.bg", "The sign-in submit's painted fill — blue-500 #4575cd on the app surface, lighter than the marketing navy."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass


# The launch banner's measured gradient — linear-gradient(90deg, #3e5199,
# #5568ad) — sits beside the declared primary gradient.
try:
    _img = stprop("promo-banner", "default", "backgroundImage") or ""
    _m = re.match(r"linear-gradient\((\d+)deg,\s*(.+)\)", _img)
    if _m:
        _found = re.findall(r"(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})(?:\s+([\d.]+)%)?", _m.group(2))
        _stops = [{"color": norm_color(c), "position": float(p) / 100 if p else round(i / max(len(_found) - 1, 1), 2)} for i, (c, p) in enumerate(_found)]
        if _stops:
            SPEC["core"].setdefault("gradient", {})["banner"] = {
                "type": "gradient", "value": _stops, "angle": _m.group(1) + "deg",
                "source": "computed backgroundImage of promo-banner default (raw/components-computed.json)",
                "description": "The launch banner's blue-violet sweep at 90deg — #3e5199 to #5568ad."}
except KeyError:
    pass

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})

# The declared product shadow: --shadow-product paints the lifted cards.
for _name, _key, _desc in [
    ("--shadow-product", "product", "The declared five-layer product shadow — the lifted card elevation."),
    ("--shadow-product-border", "productBorder", "The declared 1px black-at-5% ring that edges lifted cards."),
]:
    _sh = RAW_DECL.get(_name) or ""
    if _sh:
        _layers = []
        _dim = r"(-?[\d.]+(?:px)?)"  # declared shadows may use bare 0 for zero lengths
        for _ly in re.split(r",(?![^(]*\))", _sh):
            m = re.match(
                r"\s*" + _dim + r"\s+" + _dim + r"\s+" + _dim + r"\s+(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})",
                _ly) or re.match(
                r"\s*" + _dim + r"\s+" + _dim + r"\s+" + _dim + r"\s+" + _dim + r"\s+(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})",
                _ly)
            if m:
                g = m.groups()
                col = g[-1]
                nums = [n if n.endswith("px") else n + "px" for n in g[:-1]]
                _layers.append({"color": norm_color(col), "offsetX": nums[0],
                                "offsetY": nums[1],
                                "blur": (nums[2] if len(nums) > 2 else "0px"),
                                "spread": (nums[3] if len(nums) > 3 else "0px")})
        if _layers:
            SPEC["light"].setdefault("shadow", {})[_key] = {
                "type": "shadow", "value": _layers,
                "source": decl_source(_name),
                "description": _desc}

# Declared radii: --radii-* names (0/1/sm/2/4/lg/default/pill/round/full).
rad = SPEC["core"].setdefault("radius", {})
for _n in sorted(R):
    m = re.fullmatch(r"--radii-(.+)", _n)
    _rv = dvar(_n)
    if m and _rv is not None:
        key = {"0": "none", "1": "sm", "2": "md", "4": "xl"}.get(m.group(1), m.group(1))
        rad[key] = {"value": "0px" if _rv in (0, "0") else _rv, "type": "dimension",
                    "source": decl_source(_n),
                    "description": f"Declared {_n}."}
for key, cname, desc in [
    ("control", "nav-cta", "The measured CTA corner radius."),
    ("card", "section-box", "The measured product-card corner."),
    ("field", "signin-field", "The measured sign-in field corner."),
]:
    try:
        v = stprop(cname, "default", "borderTopLeftRadius")
        if v:
            rad[key] = {"value": v, "type": "dimension",
                        "source": f"computed borderTopLeftRadius of {cname} default (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# Motion: the sheets declare no duration/ease vars; whatever the chrome
# actually transitions is the whole story (measured).
for key, cname, prop, desc in [
    ("control", "nav-cta", "transitionDuration", "The measured CTA transition."),
    ("nav", "nav-item", "transitionDuration", "The measured nav-link transition."),
    ("menu", "m-menu-link", "transitionDuration", "The measured mobile-menu link transition."),
]:
    try:
        v = stprop(cname, "default", prop)
        if v and v != "0s":
            SPEC["core"].setdefault("motion", {}).setdefault("duration", {})["measured" + key.title()] = {
                "value": v.split(",")[0].strip(), "type": "duration",
                "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass
for key, cname, desc in [
    ("control", "nav-cta", "The measured CTA curve."),
]:
    try:
        v = stprop(cname, "default", "transitionTimingFunction")
        m = re.search(r"cubic-bezier\([^)]+\)", v or "")
        first = (v or "").strip().split(",")[0].strip()
        if m or first in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
            SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
                "value": m.group(0) if m else first, "type": "cubicBezier",
                "source": f"computed transitionTimingFunction of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# Declared spacing: --space-* is a 71-step rem scale including the negative
# --space-n* steps; emit every step plus a unit anchor at --space-1 (.25rem).
sp = SPEC["core"].setdefault("spacing", {})
_LEN = re.compile(r"^-?[\d.]+(px|rem|em)$")
for _n in sorted(R, key=lambda s: [float(x) if x.replace('.', '', 1).isdigit() else 999 for x in re.split(r'(-)', s)]):
    m = re.fullmatch(r"--space-(n?)(.+)", _n)
    if not m or not dvar(_n):
        continue
    v = str(dvar(_n))
    if not _LEN.match(v):
        # A negative step the resolver couldn't compute ("-" raw): negate the
        # positive counterpart's resolved value.
        pos = dvar(f"--space-{m.group(2)}")
        if m.group(1) == "n" and pos and _LEN.match(str(pos)):
            v = "-" + str(pos)
        else:
            continue
    elif not re.fullmatch(r"-?[\d.]+(px|rem|em)", (RAW_DECL.get(_n) or "").strip()):
        # --space-auto's keyword probes to a meaningless 0px width — a keyword
        # is not a length, so it does not publish as a dimension.
        continue
    key = m.group(1) + m.group(2).replace("-", "_")
    sp[key] = {"value": v, "type": "dimension",
               "source": decl_source(_n),
               "description": f"Declared {_n} ({RAW_DECL.get(_n)})."}
if dvar("--space-1"):
    SPEC["core"]["spacingUnit"] = {"value": dvar("--space-1"), "type": "dimension",
        "source": decl_source("--space-1"),
        "description": "The spacing base unit (.25rem = 4px) — every --space-* step multiplies it."}

# Declared screens + the 12-column grid template.
for _n, _key, _desc in [
    ("--screen-nav", "nav", "Declared screen-nav (870px) — the nav layout breakpoint."),
    ("--screen-sm", "sm", "Declared screen-sm (640px)."),
    ("--screen-md", "md", "Declared screen-md (768px)."),
    ("--screen-lg", "lg", "Declared screen-lg (1112px)."),
    ("--screen-xl", "xl", "Declared screen-xl (1280px)."),
]:
    if dvar(_n):
        SPEC["core"].setdefault("breakpoint", {})[_key] = {
            "value": dvar(_n), "type": "dimension",
            "source": decl_source(_n), "description": _desc}
if dvar("--cols-12"):
    SPEC["core"].setdefault("layout", {})["columns12"] = {
        "value": 12, "type": "number",
        "source": decl_source("--cols-12"),
        "description": "The declared 12-column grid (repeat(12, minmax(0, 1fr)))."}

# Declared type scale: --text-* sizes, --lh-b-*/--lh-h-* line-heights,
# --letter-spacing-*, --font-* weights and the sans/mono/ui stacks.
for _n in sorted(R):
    m = re.fullmatch(r"--text-(\d+)", _n)
    if m and dvar(_n) and re.match(r"[\d.]+(px|rem|em)", str(dvar(_n))):
        SPEC["core"].setdefault("fontSize", {})["s" + m.group(1)] = {
            "value": dvar(_n), "type": "dimension",
            "source": decl_source(_n),
            "description": f"Declared {_n} ({RAW_DECL.get(_n)})."}
for _n in sorted(R):
    m = re.fullmatch(r"--lh-(b|h)-(\d+)", _n)
    if m and dvar(_n):
        grp = "body" if m.group(1) == "b" else "heading"
        SPEC["core"].setdefault("lineHeight", {}).setdefault(grp, {})["s" + m.group(2)] = {
            "value": dvar(_n), "type": "dimension",
            "source": decl_source(_n),
            "description": f"Declared {_n} — the {grp} line-height for text-{m.group(2)}."}
for _n in sorted(R):
    m = re.fullmatch(r"--letter-spacing-(\d+)", _n)
    if m and dvar(_n):
        SPEC["core"].setdefault("letterSpacing", {})["s" + m.group(1)] = {
            "value": dvar(_n), "type": "letterSpacing",
            "source": decl_source(_n),
            "description": f"Declared {_n} ({RAW_DECL.get(_n)} — em, relative to the element's font size)."}
for _n, _key in [("--font-book", "book"), ("--font-regular", "regular"),
                 ("--font-medium", "medium"), ("--font-semibold", "semibold"),
                 ("--font-bold", "bold")]:
    if dvar(_n):
        try:
            wv = int(str(dvar(_n)).strip())
        except ValueError:
            continue
        SPEC["core"].setdefault("fontWeight", {})[_key] = {
            "value": wv, "type": "fontWeight",
            "source": decl_source(_n),
            "description": f"Declared {_n}."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-cta", "default", "height", "The nav Sign-up button."),
    ("control.heightNavItem", "nav-item", "default", "height", "Nav links."),
    ("control.heightNavGhost", "nav-ghost", "default", "height", "The nav's ghost button (Get started)."),
    ("control.heightHeroCta", "hero-cta", "default", "height", "The hero CTA."),
    ("control.heightMenuButton", "m-menu-button", "default", "height", "The mobile menu toggle."),
    ("control.radiusCta", "nav-cta", "default", "borderTopLeftRadius", "CTA corner radius."),
    ("control.heightSubmit", "signin-submit", "default", "height", "The sign-in submit button."),
    ("banner.height", "promo-banner", "default", "height", "The launch banner strip."),
    ("nav.height", "header", "default", "height", "The header bar at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("drawer.width", "m-menu-open", "default", "width", "The mobile menu overlay at 390px."),
    ("heroTitle.width", "hero-title", "default", "width", "The hero headline's measure."),
    ("card.widthProduct", "section-box", "default", "width", "A product card at 1440px."),
    ("field.widthSignin", "signin-field", "default", "width", "The sign-in email field."),
    ("band.heightDark", "dark-band", "default", "height", "The dark infrastructure band."),
]:
    try:
        v = stprop(cname, state, prop)
        if not v:
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------- typography
#
# Families are declared as --font-sans/--font-mono/--font-ui stacks
# (SuisseIntl body, SuisseIntlMono code, Inter UI) — the harvest carries
# them verbatim. Measured display sizes sit beside the declared --text-* steps.

font = SPEC["core"].setdefault("font", {})
for key, name, desc in [
    ("sans", "--font-sans", "Declared font-sans: SuisseIntl + system fallbacks — the marketing face."),
    ("mono", "--font-mono", "Declared font-mono: SuisseIntlMono + ui-monospace fallbacks — the code face."),
    ("ui", "--font-ui", "Declared font-ui: Inter + system fallbacks — the dashboard/app face."),
]:
    v = dvar(name)
    if v:
        font.setdefault("family", {})[key] = {"type": "fontFamily", "value": v.replace("'", '"'),
            "source": decl_source(name),
            "description": desc}
try:
    f = (stprop("hero-title", "default", "fontFamily") or "").strip()
    if f:
        font.setdefault("family", {})["displayMeasured"] = {"type": "fontFamily", "value": f,
            "source": "computed fontFamily of hero-title default (raw/components-computed.json)",
            "description": "The face the hero headline actually paints (SuisseIntl)."}
except KeyError:
    pass

for key, cname, desc in [
    ("hero", "hero-title", "The hero headline at 1440px (52px, SuisseIntl 600)."),
    ("h1Product", "ach-title", "Product-page headlines."),
    ("h2", "section-title", "Section headings."),
    ("darkTitle", "dark-title", "Headings on the dark infrastructure band."),
    ("mHero", "m-hero", "The hero headline at 390px."),
    ("nav", "nav-item", "Nav labels."),
    ("footer", "footer-link", "Footer links."),
    ("banner", "promo-banner", "The launch banner line."),
    ("stat", "stat-figure", "The big stat figures."),
    ("cta", "hero-cta", "CTA labels."),
    ("signinLabel", "signin-submit", "The sign-in button label."),
]:
    try:
        sz = stprop(cname, "default", "textStyle.fontSize") or stprop(cname, "default", "fontSize")
        if sz:
            font.setdefault("size", {})[key] = {"type": "dimension", "value": sz,
                "source": f"computed fontSize of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
print("wrote raw/component-tokens.json")
