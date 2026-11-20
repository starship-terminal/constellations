#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Fourthwall's signed-out public surfaces are five different products that do not
share one stylesheet — each host declares its own layer, so each gets its own
token set:

  fourthwall.com          Webflow marketing — a layered Webflow DS on :root:
                          --_primitives---* (ink/paper colour ramps, Suisse
                          Intl / Saans stacks, fluid type sizes, radius, space,
                          weights), --_surface---* (the semantic bg/text/
                          border/icon layer), --_rhythm---* (section/stack/grid
                          spacing) and the flat legacy ramps --gs*/--b*/--g*/
                          --r*/--y*/--twitch*. Light only; dark "on-ink"
                          sections (.on-ink/.site-footer/.leg-section...) are
                          scoped redeclarations, not a user theme — the `ink`
                          set carries them.
  products.fourthwall.com React catalogue — its own styled-components DS:
                          --color-*/--bg-*/--text-*/--border-*/--icon-*/
                          --input-*/--button-*/--panel-*/--font-*/--space-*/
                          --radius-*/--shadow-*/--motion-*/--blur-*. The
                          semantic names are light-dark() functions — `catalog`
                          resolves the light branch (what every visitor paints),
                          `catalogDark` the dark branch under a forced
                          color-scheme (declared, never painted signed out).
  auth.fourthwall.com     /get-started's Keycloak signup — the SAME catalogue
                          DS, resolved in its light branch: the capture painted
                          it light and the `signup` set is that resolution
                          (its light-dark() pairs follow the visitor's
                          colour-scheme like the catalogue's).
  docs.fourthwall.com     Mintlify — --gray-*/--primary*/--color-*/tailwind-ish
                          --container-*/--ease-*/--leading-*/--font-*. Channel
                          triplets ("238 238 238") are emitted as colours.
                          `docsDark` is the real html.dark resolution behind the
                          site's own "Change theme preference" menu.
  help.fourthwall.com     Docusaurus — the --ifm-* Infima layer plus the
                          product's --fw-*/--docusaurus-*/--doc-* names;
                          `helpDark` the data-theme="dark" resolution behind
                          the navbar's real colour-mode toggle.

Measured computed styles from raw/components-computed.json fill the rest:
  core      the measured cross-surface scales — the Suisse Intl/Saans families,
            the type ramp, the control transition, component geometry
  every set a small block of measured semantic roles (text.ink, surface.*,
            action.*) aliased back to that surface's own declared values
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RV = V.get("resolved", {})


def pool(shell):
    return {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v)
            for n, v in RV.get(shell, {}).items()}


R = pool("light")        # marketing :root, light
RI = pool("ink")         # marketing body.on-ink — the dark-section scope
RC = pool("catalog")     # products shell, light
RCD = pool("catalogDark")  # products shell, forced dark color-scheme
RA = pool("signup")      # the auth shell — the catalogue DS resolved light
RD = pool("docs")        # Mintlify, light
RDD = pool("docsDark")   # Mintlify, html.dark
RH = pool("help")        # Docusaurus, data-theme=light
RHD = pool("helpDark")   # Docusaurus, data-theme=dark
C = json.loads((RAW / "components-computed.json").read_text())["components"]

# Which host's sheets declare each theme-bin name — vars.mjs stamps the file
# label with the host word.
HOST_NAMES = {"marketing": set(), "catalog": set(), "signup": set(), "docs": set(), "help": set()}
for rule in V.get("theme", []):
    host = (rule.get("file") or "").split(" ", 1)[0]
    if host in HOST_NAMES:
        HOST_NAMES[host].update(rule.get("properties") or {})

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Fourthwall's five "
    "public hosts each declare their own layer (raw/css-vars.json): the Webflow "
    "marketing --_primitives---/--_surface---/--_rhythm---/ramp vocabulary in "
    "light (+ the on-ink dark-section resolutions in ink), the catalogue's "
    "--color-/--bg-/--text-/... names in catalog (light-dark() light branch), "
    "catalogDark (the dark branch under a forced color-scheme — declared, not "
    "painted) and signup (the same DS resolved light on /get-started), the Mintlify "
    "--gray-/--primary vocabulary in docs/docsDark (the real theme menu) and "
    "the Docusaurus --ifm-/--fw- layer in help/helpDark (the real toggle). "
    "Measured roles alias to the declared values they match."),
    "core": {}, "light": {}, "ink": {}, "catalog": {}, "catalogDark": {},
    "signup": {}, "docs": {}, "docsDark": {}, "help": {}, "helpDark": {},
    "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def rc(comp, state, key):
    return C[comp]["states"][state]["rect"][key]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def norm_color(v):
    v = str(v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or (not str(a).endswith("%") and float(a) >= 1) or (str(a).endswith("%") and float(a[:-1]) >= 100):
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        a = float(a[:-1]) / 100 if str(a).endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    m = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", v)
    if m:  # the Mintlify "R G B" channel triplets — the colour's channels
        r, g, b = (int(x) for x in m.groups())
        return "#%02x%02x%02x" % (r, g, b)
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


# Per set: variable name -> dotted token path it was actually written to, and
# dotted path -> variable name holding it. Kept per set so a later set's
# re-homing (a leaf moved under `default`) never moves an earlier set's entry.
EMITTED_BY = {}
OWNER_BY = {}


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def path_parts(name):
    """--_primitives---color--ink-alpha-06 -> _primitives.color.ink.alpha.06;
    --gs100 -> gs.100; --ifm-hero-background-color -> ifm.hero.background.color.
    The Webflow layer names keep their `_` prefix — that is how the sheet
    namespaces its own layers, and the style-guide scopes match."""
    parts = [p for p in name[2:].split("-") if p]
    out = []
    for p in parts:
        m = re.fullmatch(r"(gs|b|g|r|y)(\d+)", p)  # the flat legacy ramps
        if m:
            out += [m.group(1), m.group(2)]
        else:
            out.append(p)
    return out


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path; a leaf that later needs children
    moves inside its group under `default`/`base`/`self`."""
    node = root
    EMITTED = EMITTED_BY.setdefault(id(root), {})
    _OWNER = OWNER_BY.setdefault(id(root), {})
    parts = path_parts(name)
    for i, p in enumerate(parts[:-1]):
        nxt = node.get(p)
        prefix = ".".join(parts[:i + 1])
        if nxt is None:
            nxt = node[p] = {}
        elif _leaf(nxt):
            owner = _OWNER.pop(prefix, None)
            nxt = node[p] = {"default": nxt}
            if owner:
                EMITTED[owner] = prefix + ".default"
                _OWNER[prefix + ".default"] = owner
        node = nxt
    last = parts[-1]
    path = ".".join(parts)
    if last in node and not _leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                path += "." + key
                break
        else:
            raise ValueError(f"{name}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{name}: duplicate token path {path}")
        node[last] = leaf
    EMITTED[name] = path
    _OWNER[path] = name


def transition(s):
    """The CSS transition shorthand from the computed longhands, one entry per
    property; each property takes the duration/easing/delay at its index,
    the lists repeating as CSS repeats them."""
    def items(v, d):
        out = []
        depth, cur = 0, ""
        for ch in str(v or d):
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            if ch == "," and depth == 0:
                out.append(cur.strip()); cur = ""
            else:
                cur += ch
        out.append(cur.strip())
        return [x for x in out if x] or [d]
    props = items(s.get("transitionProperty"), "all")
    durs = items(s.get("transitionDuration"), "0s")
    eases = items(s.get("transitionTimingFunction"), "ease")
    delays = items(s.get("transitionDelay"), "0s")
    out = []
    for i, p in enumerate(props):
        part = [p, durs[i % len(durs)], eases[i % len(eases)]]
        if delays[i % len(delays)] not in ("0s", "0ms"):
            part.append(delays[i % len(delays)])
        out.append(" ".join(part))
    return ", ".join(out)


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")
TRIPLET = re.compile(r"\d{1,3}\s+\d{1,3}\s+\d{1,3}")


def leaf_type(name, val):
    """The DTCG type a declared value honestly is; names outside the useful
    types return None and are left in raw/css-vars.json only."""
    v = str(val or "").strip()
    if not v or v in ("initial", "inherit", "unset", "none", "normal", "auto", "revert"):
        return None
    if COLOR_V.fullmatch(v) or TRIPLET.fullmatch(v):
        return "color"
    if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", v):
        return "dimension"
    if re.fullmatch(r"[\d.]+m?s", v):
        return "duration"
    if re.fullmatch(r"cubic-bezier\([^)]*\)", v) or v in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
        return "cubicBezier"
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        return "number" if "weight" not in name else "fontWeight"
    if ("font-family" in name or re.search(r"font-(inter|paper|body|heading|mono|display)", name)) and ("'" in v or '"' in v or "," in v):
        return "fontFamily"
    return None


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted."""
    c = C[comp]["states"][state]
    entries = [p for p in c.get("paint") or [] if p.get(key)]
    if not entries:
        raise KeyError(key)
    rect = c.get("rect") or {}
    for p in entries:
        m = re.fullmatch(r"([\d.]+)x([\d.]+)", str(p.get("size") or ""))
        if m and abs(float(m.group(1)) - rect.get("w", -9)) <= 1 and abs(float(m.group(2)) - rect.get("h", -9)) <= 1:
            return p[key]
    return entries[0][key]


TRANSPARENT = re.compile(r"transparent|rgba\(\s*[\d.]+[,\s]+[\d.]+[,\s]+[\d.]+\s*[,/]\s*0(\.0+)?%?\s*\)")
NOT_PAINTED = []  # (set, role) rows whose element paints no fill of its own


def own_fill(comp, state):
    """The fill the element itself paints: its backgroundColor unless that is
    transparent, then a paint-list layer the exact size of the element. None
    when the element paints nothing (the fill comes from an ancestor)."""
    v = st(comp, state).get("backgroundColor")
    if v and not TRANSPARENT.fullmatch(str(v).strip()):
        return v
    c = C[comp]["states"][state]
    rect = c.get("rect") or {}
    for p in c.get("paint") or []:
        m = re.fullmatch(r"([\d.]+)x([\d.]+)", str(p.get("size") or ""))
        bg = p.get("bg")
        if bg and not TRANSPARENT.fullmatch(bg) and m and abs(float(m.group(1)) - rect.get("w", -9)) <= 1 \
                and abs(float(m.group(2)) - rect.get("h", -9)) <= 1:
            return bg
    return None


def inset_shadow_color(comp, state):
    sh = painted(comp, state, "shadow")
    m = re.search(COLOR_V.pattern + r"(?:\s+-?[\d.]+px){2,4}\s+inset", sh)
    if not m:
        raise KeyError("insetShadowColor")
    return m.group(1)


# ------------------------------------------------------------------- fonts
#
# The marketing sheet declares the stacks (--_primitives---font-family--*,
# --font-*) — they land in the light set with everything else. core.font keeps
# the measured canonical readings so every theme inherits the family tokens.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("suisse", "hero-sub", "default",
     "Suisse Intl — the body family on every marketing surface (declared --_primitives---font-family--body; the catalogue sets \"Suisse Int'l\" as --font-family-body)."),
    ("saans", "hero-h1", "default",
     "Saans — the display/heading family (declared --_primitives---font-family--display; the catalogue's --font-family-heading \"Saans VF\")."),
    # No mono: every measured element computes to a UI stack; the mono voices
    # are declared per host instead (catalog/signup font.family.mono "Suisse
    # Int'l Mono", docs font.paper.mono, help ifm.font.family.monospace).
]:
    try:
        v = st(comp, state)["fontFamily"]
        fam[key] = lit(v, "fontFamily",
            f"computed fontFamily of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# Leaf keys are role words, not css weight names — the per-host sheets declare
# font.weight.<name>/<n> tokens of their own (catalogue --font-weight-420, docs
# --font-weight-medium) that must not land on the same custom property.
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("body", "hero-sub", "default", "The 400 body weight."),
    ("label", "nav-cta", "default", "The ~500 weight on nav/button labels."),
    ("title", "plan-card", "default", "The weight on plan card titles."),
    ("display", "hero-h1", "default", "The display-heading weight — the masthead."),
]:
    try:
        w = ts(comp, state, "fontWeight") or st(comp, state)["fontWeight"]
        if w:
            weights[key] = lit(int(float(w)), "fontWeight",
                f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero masthead size."),
    ("lede", "hero-sub", "default", "The hero standfirst size."),
    ("body", "footer-link", "default", "The body/nav link size."),
    ("button", "nav-cta", "default", "The button label size."),
    ("price", "price-h1", "default", "The /pricing masthead size."),
    ("mobileHero", "m-hero-h1", "default", "The masthead at 390 wide."),
]:
    try:
        v = ts(comp, state, "fontSize") or st(comp, state)["fontSize"]
        sizes[key] = lit(v, "dimension", f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero masthead leading."),
    ("body", "hero-sub", "default", "The body leading."),
]:
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        fsraw = t.get("fontSize") or c["style"]["fontSize"]
        v = t.get("lineHeight") or c["style"]["lineHeight"]
        fs = float(fsraw[:-2])
        if v == "normal":
            lh[key] = lit("normal", "other", f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)
        elif v.endswith("px"):
            lh[key] = lit(round(float(v[:-2]) / fs, 4), "number", f"computed lineHeight/fontSize of {comp} {state} ({v} over {fsraw}, raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

# ------------------------------------------------------------ vocabularies
#
# Vendor namespaces that ride the same sheets are left in raw/css-vars.json
# only: --hsf-* (the HubSpot forms theme), --cc-* (Klaro cookie consent),
# --toastify-* (react-toastify), --swiper-*, --twoslash-*.

VENDOR = re.compile(r"^--(hsf-|cc-|toastify-|swiper-|twoslash-)")


def host_names(host, *pools):
    """A host's declared names that resolve in the given pools."""
    out = []
    for name in sorted(HOST_NAMES[host]):
        if VENDOR.match(name):
            continue
        for p in pools:
            if name in p and p[name] not in (None, ""):
                out.append(name)
                break
    return out


def emit_named(setroot, name, val):
    ty = leaf_type(name, val)
    if ty:
        emit(setroot, name, var(name, ty))
        return True
    return False


def E(setname):
    """The names emitted in one set and the path each landed at."""
    return EMITTED_BY.get(id(SPEC[setname]), {})


SETS = {"light": R, "ink": RI, "catalog": RC, "catalogDark": RCD, "signup": RA,
        "docs": RD, "docsDark": RDD, "help": RH, "helpDark": RHD}
ALIAS = {}

# The marketing vocabulary is emitted once in the light set (the canonical
# surface) — ink re-emits only the names the on-ink scope actually remaps.
mkt_names = host_names("marketing", R)
for name in mkt_names:
    emit_named(SPEC["light"], name, R.get(name))
ALIAS["light"] = {}
for name in mkt_names:
    if name in E("light"):
        ALIAS["light"].setdefault(norm_color(R.get(name)), E("light")[name])

# ink: the names whose on-ink resolution differs from :root light — the scoped
# .on-ink/.site-footer/.leg-section redeclarations. (Same-path override: a name
# like --_surface---bg--page lands at surface.bg.page in both sets.)
ink_emitted = []
for name in host_names("marketing", RI):
    if name in E("light") and norm_color(RI.get(name)) != norm_color(R.get(name)):
        if emit_named(SPEC["ink"], name, RI.get(name)):
            ink_emitted.append(name)
# ink roles may only alias the ink set's own tokens — a measured ink value
# that happens to equal a :root-only token stays a literal.
ALIAS["ink"] = {}
for name in ink_emitted:
    ALIAS["ink"][norm_color(RI.get(name))] = E("ink")[name]

# The catalogue vocabulary — emitted in all three shells; catalogDark carries
# the light-dark() dark branch (forced color-scheme, declared not painted) and
# auth the light resolution the /get-started capture painted.
for name in host_names("catalog", RC):
    emit_named(SPEC["catalog"], name, RC.get(name))
ALIAS["catalog"] = {}
for name in host_names("catalog", RC):
    if name in E("catalog"):
        ALIAS["catalog"].setdefault(norm_color(RC.get(name)), E("catalog")[name])

# Each set emits only the names its own shell resolves — a var leaf resolved
# under a shell that never declared it would be fiction.
catd_names = [n for n in host_names("catalog", RCD) if n in RCD]
auth_names = sorted({n for n in host_names("catalog", RA) + host_names("signup", RA)
                     if n in RA})
for name in catd_names:
    emit_named(SPEC["catalogDark"], name, RCD.get(name))
ALIAS["catalogDark"] = {}
for name in catd_names:
    if name in E("catalogDark"):
        ALIAS["catalogDark"].setdefault(norm_color(RCD.get(name)), E("catalogDark")[name])

for name in auth_names:
    emit_named(SPEC["signup"], name, RA.get(name))
ALIAS["signup"] = {}
for name in auth_names:
    if name in E("signup"):
        ALIAS["signup"].setdefault(norm_color(RA.get(name)), E("signup")[name])

# The docs (Mintlify) and help (Docusaurus) vocabularies in both painted themes.
for name in host_names("docs", RD):
    emit_named(SPEC["docs"], name, RD.get(name))
ALIAS["docs"] = {}
for name in host_names("docs", RD):
    if name in E("docs"):
        ALIAS["docs"].setdefault(norm_color(RD.get(name)), E("docs")[name])

docsd_names = [n for n in host_names("docs", RDD) if n in RDD]
for name in docsd_names:
    emit_named(SPEC["docsDark"], name, RDD.get(name))
ALIAS["docsDark"] = {}
for name in docsd_names:
    if name in E("docsDark"):
        ALIAS["docsDark"].setdefault(norm_color(RDD.get(name)), E("docsDark")[name])

for name in host_names("help", RH):
    emit_named(SPEC["help"], name, RH.get(name))
ALIAS["help"] = {}
for name in host_names("help", RH):
    if name in E("help"):
        ALIAS["help"].setdefault(norm_color(RH.get(name)), E("help")[name])

helpd_names = [n for n in host_names("help", RHD) if n in RHD]
for name in helpd_names:
    emit_named(SPEC["helpDark"], name, RHD.get(name))
ALIAS["helpDark"] = {}
for name in helpd_names:
    if name in E("helpDark"):
        ALIAS["helpDark"].setdefault(norm_color(RHD.get(name)), E("helpDark")[name])


# emitted-path → resolved value, per theme: lets a measured role alias the
# semantically right variable when several declared names share its value
# (e.g. a measured page field matches bg.page AND text.action; the first-emitted
# name is not always the meaningful one).
POOLS = {"light": R, "ink": RI, "catalog": RC, "catalogDark": RCD, "signup": RA,
         "docs": RD, "docsDark": RDD, "help": RH, "helpDark": RHD}
PATHVAL = {t: {E(t)[n]: norm_color(v) for n, v in p.items() if n in E(t)}
           for t, p in POOLS.items()}


# Which declared names a role may alias when several share its value: a text
# role takes a text/ink name first, a fill a background/surface name, a border
# a border name. Only when no name of the role's own kind matches does any
# declared name do (the first in emit order, as before).
GROUP_WORDS = {
    "text": ("text", "ink", "fg", "foreground", "color.gray", "font.color", "heading", "content"),
    "background": ("bg", "background", "surface", "page"),
    "surface": ("bg", "background", "surface", "panel", "card"),
    "action": ("action", "button", "bg", "primary"),
    "border": ("border", "stroke", "divider", "line"),
}


def ranked_alias(theme, norm, group):
    words = GROUP_WORDS.get(group, ())
    paths = [pth for pth, v in PATHVAL[theme].items() if v == norm]
    for w in words:
        hit = sorted(pth for pth in paths if w in pth.split(".") or pth.startswith(w + ".") or ("." + w) in pth)
        if hit:
            return hit[0]
    return ALIAS[theme].get(norm)


def semcolor(raw, src, desc, theme="light", prefer=None, group=None):
    norm = norm_color(raw)
    alias = prefer if prefer and PATHVAL[theme].get(prefer) == norm else ranked_alias(theme, norm, group)
    value = f"{{{alias}}}" if alias else norm
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


# ------------------------------------------------------- measured roles
#
# (set-root, theme, dotted key under the role group, component, state,
#  style prop, role group, description[, preferred alias path])

for row in [
    # marketing light — measured on the light page sections (the home page's
    # hero and nav are on-ink bands, so they land in the ink set instead)
    (SPEC["light"], "light", "ink", "cmp-h1", "default", "color", "text",
     "The near-black ink on headings and body copy.", "_surface.text.body"),
    (SPEC["light"], "light", "muted", "blog-news", "default", "color", "text",
     "The blue-grey field/secondary ink."),
    # marketing on-ink dark sections — measured on the real dark bands
    (SPEC["ink"], "ink", "ink", "hero-h1", "default", "color", "text",
     "The ink on the dark hero/section bands — white over near-black.", "_surface.text.body"),
    (SPEC["ink"], "ink", "muted", "hero-sub", "default", "color", "text",
     "The translucent white lede on the dark hero.", "_surface.text.soft"),
    (SPEC["ink"], "ink", "page", "wordmark-section", "default", "backgroundColor", "background",
     "The near-black field of the on-ink dark sections.", "_surface.bg.page"),
    (SPEC["ink"], "ink", "fill", "nav-cta", "default", "backgroundColor", "action",
     "The white Start-now pill on the ink surface — the inverted action.", "_surface.bg.action"),
    (SPEC["ink"], "ink", "ink", "nav-cta", "default", "color", "action",
     "The ink label on the white Start-now pill.", "_surface.text.action"),
    (SPEC["ink"], "ink", "footer-bg", "footer", "default", "backgroundColor", "background",
     "The .site-footer field — a warm near-black.", "_surface.bg.page"),
    (SPEC["ink"], "ink", "footer-ink", "footer-link", "default", "color", "text",
     "The footer link ink on the dark field.", "_surface.text.soft"),
    # catalogue light
    (SPEC["catalog"], "catalog", "ink", "pdp-h1", "default", "color", "text",
     "The catalogue primary text ink.", "text.primary.default"),
    (SPEC["catalog"], "catalog", "page", "cat-nav", "default", "backgroundColor", "background",
     "The catalogue page/header field."),
    (SPEC["catalog"], "catalog", "card", "prod-card", "default", "backgroundColor", "surface",
     "A catalogue product-card surface."),
    (SPEC["catalog"], "catalog", "field-bg", "cat-search", "default", "backgroundColor", "surface",
     "The catalogue search field fill."),
    # No catalogue field border: cat-search computes border-style none at 0px
    # on every side, so no border role is read (its borderTopColor is only
    # currentColor).
    # auth — the same catalogue DS painted light at /get-started
    (SPEC["signup"], "signup", "card", "auth-card", "default", "backgroundColor", "surface",
     "The auth card/page field at /get-started — the catalogue DS painted light.", "bg.primary.default"),
    (SPEC["signup"], "signup", "ink", "auth-google", "default", "color", "text",
     "The provider-button ink on the auth surface.", "text.primary.default"),
    (SPEC["signup"], "signup", "fill", "auth-google", "default", "backgroundColor", "action",
     "The provider-button fill.", "bg.secondary.default"),
    # "login-link", not "link": the auth sheet declares --text-link and
    # --text-link-secondary, which already hold signup.text.link.
    (SPEC["signup"], "signup", "login-link", "auth-login", "default", "color", "text",
     "The Log-in link ink on the auth surface.", "text.primary.default"),
    # docs light / dark
    (SPEC["docs"], "docs", "ink", "docs-h1", "default", "color", "text",
     "The docs article heading ink in light."),
    (SPEC["docs"], "docs", "card", "docs-card", "default", "backgroundColor", "surface",
     "A docs card surface in light."),
    (SPEC["docs"], "docs", "sidebar-bg", "docs-sidebar", "default", "backgroundColor", "surface",
     "The docs sidebar field in light."),
    (SPEC["docsDark"], "docsDark", "page", "dd-page", "default", "backgroundColor", "background",
     "The docs page field under html.dark — reached through the site's own theme menu."),
    (SPEC["docsDark"], "docsDark", "ink", "dd-h1", "default", "color", "text",
     "The docs heading ink under html.dark."),
    (SPEC["docsDark"], "docsDark", "card", "dd-card", "default", "backgroundColor", "surface",
     "A docs card surface under html.dark."),
    (SPEC["docsDark"], "docsDark", "code-bg", "dd-code", "default", "backgroundColor", "surface",
     "A code block surface under html.dark."),
    (SPEC["docsDark"], "docsDark", "muted", "dd-prose", "default", "color", "text",
     "The docs body ink under html.dark."),
    # help light / dark
    (SPEC["help"], "help", "ink", "help-h1", "default", "color", "text",
     "The help category heading ink in light."),
    (SPEC["help"], "help", "navbar", "help-navbar", "default", "backgroundColor", "surface",
     "The Docusaurus navbar field in light."),
    (SPEC["help"], "help", "card", "help-card", "default", "backgroundColor", "surface",
     "A help category-card surface in light."),
    (SPEC["help"], "help", "field-bg", "help-search", "default", "backgroundColor", "surface",
     "The help search field fill in light."),
    (SPEC["helpDark"], "helpDark", "page", "hd-page", "default", "backgroundColor", "background",
     "The help page field under data-theme=dark — reached through the site's own toggle."),
    (SPEC["helpDark"], "helpDark", "ink", "hd-h1", "default", "color", "text",
     "The help heading ink under data-theme=dark."),
    (SPEC["helpDark"], "helpDark", "navbar", "hd-navbar", "default", "backgroundColor", "surface",
     "The navbar field under data-theme=dark."),
    (SPEC["helpDark"], "helpDark", "card", "hd-card", "default", "backgroundColor", "surface",
     "A help card surface under data-theme=dark."),
]:
    root, theme, key, comp, state, prop, group, desc, *opt = row
    prefer = opt[0] if opt else None
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "insetShadowColor":
            raw = inset_shadow_color(comp, state)
            src = f"the inset box-shadow layer painted on {comp} {state} (raw/components-computed.json)"
        elif prop == "backgroundColor":
            raw = own_fill(comp, state)
            if raw is None:
                NOT_PAINTED.append(f"{theme}.{group}.{key} ({comp} {state})")
                continue
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, "") or TRANSPARENT.fullmatch(str(raw).strip()):
            raise KeyError(prop)
        if key in root.get(group, {}):
            raise ValueError(f"{theme}.{group}.{key}: a measured role would overwrite a declared token")
        root.setdefault(group, {})[key] = semcolor(raw, src, desc, theme, prefer, group)
    except KeyError:
        pass

# The page fields: marketing paints --_surface---bg--page (#ffffff), the
# catalogue --bg-primary, docs --background-light, help --ifm-background-color —
# the declared names already landed at their paths; alias the role to them.
for theme, name, comp, desc in [
    ("light", "--_surface---bg--page", None, "The marketing page field — every light page paints on it."),
    ("catalog", "--bg-primary", None, "The catalogue page field."),
    ("docs", "--background-light", None, "The docs page field in light."),
    ("docsDark", "--background-dark", None, "The docs page field under html.dark."),
    ("help", "--ifm-background-color", None, "The help page field in light."),
]:
    try:
        if name in E(theme):
            SPEC[theme].setdefault("background", {})["page"] = lit(
                "{%s}" % E(theme)[name], "color",
                f"the page field the surface paints; the declared {name}",
                desc)
    except KeyError:
        pass
# auth page field: the measured auth card already covers the painted field.

# ------------------------------------------------------------------ shape
#
# The catalogue declares --radius-* (emitted in its sets); the marketing sheet
# declares --_primitives---radius--*. core.radius keeps the measured scale on
# real controls.

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("button", "nav-cta", "default", "borderTopLeftRadius", "The radius on the primary Start-now buttons."),
    ("nav", "nav-link", "default", "borderTopLeftRadius", "The radius on nav links/pills."),
    ("card", "tile", "default", "borderTopLeftRadius", "The marketing tile radius."),
    ("plan", "plan-card", "default", "borderTopLeftRadius", "The pricing plan-card radius."),
    ("cat-card", "prod-card", "default", "borderTopLeftRadius", "The catalogue product-card radius."),
    ("field", "cat-search", "default", "borderTopLeftRadius", "The catalogue field radius."),
    ("help-card", "help-card", "default", "borderTopLeftRadius", "The help card radius."),
    ("mobile-nav", "m-cta", "default", "borderTopLeftRadius", "The Start-now pill at 390 wide."),
]:
    try:
        v = norm_len(st(comp, state)[prop])
        radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other",
                         f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for comp in ("nav-cta", "hero-cta", "cmp-card", "prod-card"):
    try:
        s = st(comp, "default")
        dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
        if dur and any(d.strip() not in ("0s", "0ms") for d in dur.split(",")):
            mo["control"] = lit(transition(s), "other",
                f"computed transition of {comp} default (raw/components-computed.json)",
                "The control transition the marketing site puts on buttons and links.")
            break
    except KeyError:
        continue
try:
    s = st("cat-tab", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and any(d.strip() not in ("0s", "0ms") for d in dur.split(",")):
        mo["catalog-control"] = lit(
            transition(s), "other",
            "computed transition of cat-tab default (raw/components-computed.json)",
            "The catalogue control transition (its --motion-* durations/easings are declared in the catalog set).")
except KeyError:
    pass

# ------------------------------------------------------------- components
#
# Theme-independent measured geometry.

comp_t = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("nav-height", "mkt-nav", "default", "h", "dimension", "The marketing nav bar height."),
    ("nav-cta-height", "nav-cta", "default", "h", "dimension", "The Start-now pill height."),
    ("hero-width", "hero-h1", "default", "w", "dimension", "The hero masthead measure."),
    ("mega-menu-width", "mega-clip", "default", "w", "dimension", "The Features mega-menu panel width."),
    ("tile-width", "tile", "default", "w", "dimension", "A marketing tile width."),
    ("footer-height", "footer", "default", "h", "dimension", "The marketing footer height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "A pricing plan-card width."),
    ("cat-nav-height", "cat-nav", "default", "h", "dimension", "The catalogue header height."),
    ("cat-search-width", "cat-search", "default", "w", "dimension", "The catalogue search field width."),
    ("prod-card-width", "prod-card", "default", "w", "dimension", "A catalogue product-card width."),
    ("quiz-card-width", "quiz-card", "default", "w", "dimension", "The product-finder card width."),
    ("auth-card-width", "auth-card", "default", "w", "dimension", "The /get-started auth card width."),
    ("docs-nav-height", "docs-nav", "default", "h", "dimension", "The Mintlify navbar height."),
    ("docs-sidebar-width", "docs-sidebar", "default", "w", "dimension", "The docs sidebar width."),
    ("help-nav-height", "help-navbar", "default", "h", "dimension", "The help navbar height."),
    ("help-search-width", "help-search", "default", "w", "dimension", "The help search field width."),
    ("help-card-width", "help-card", "default", "w", "dimension", "A help category-card width."),
    ("mobile-nav-height", "m-nav", "default", "h", "dimension", "The phone nav bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp_t[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                           ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
    if NOT_PAINTED:
        print("no own fill (not tokenised):", ", ".join(NOT_PAINTED))
    print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})