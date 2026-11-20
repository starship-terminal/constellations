#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

gladia.io is four public surfaces signed out. The marketing site on
www.gladia.io declares its design-token layer on :root:

  --color-neutral-0..1000    the gray ramp (12 stops: 0,50,100..900,1000)
  --color-<hue>-<step>       the purple/blue/green/red/yellow/orange/pink ramps,
                             plus the hue defaults (--color-purple, --color-blue)
  --color-white              the literal white
  --alpha-white-*/--alpha-black-*  translucent overlays
  --space-0..48              the 4px spacing scale plus --space-page-x,
                             --space-section-y(-sm), --space-card-gap
  --radius-0..6, --radius-full
  --shadow-none/sm/md/lg/xl
  --font-sans/--font-mono    'Suisse Intl' and 'Geist Mono' stacks
  --font-size-10..80         the type ramp (px steps)
  --font-weight-*, --line-height-*, --letter-spacing-*
  --duration-0..480          the transition-duration ramp (ms)
  --ease-linear/in/out/in-out/spring
  --label-<hue>, --badge-<hue>(-bg)   semantic label and badge colours
  --text-body-*, --filter-icon-*, --gradient-*, --max-w-*, --nb-*/,
  --nav-bar-*, --hero-*, --cta-*      layout, type-role and effect vars

and the semantic roles every component consumes:

  --text-primary/-secondary/-tertiary/-disabled/-inverse/-link/-brand/
      -success/-warning/-error
  --bg-primary/-secondary/-tertiary/-inverse/-elevated/-sunken/-glass/
      -glass-light/-brand
  --border-primary/-secondary/-tertiary/-card/-subtle/-transparent(-subtle)/
      -active/-focus/-brand

:root paints dark (bg-primary #000, text-primary #fff) — the theme every
marketing page paints. body.light-mode re-points 19 roles to the light values
the /library page paints; .section--white re-points 5 for white sections
inside dark pages. vars.mjs resolves all four scopes (light, dark,
lightMode, sectionWhite); build_tokens.py maps the token `dark` set to the
:root pass and `light` to the .light-mode pass.

docs.gladia.io is a Mintlify site with its own token layer and a real
light/dark preference — its values land under component.*. app.gladia.io /
and /signup are the product shell's signed-out surfaces — also component.*
(their measurements travel in raw/components-computed.json).

Each leaf: {"type": ..., "var": "--name"} resolved per theme by
build_tokens.py, or a measured {"type", "value", "source"} for geometry the
DOM measurement pass recorded. Every leaf carries $extensions.source.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V["resolved"]["dark"]
RM = {n: v.get("value", v["raw"]) for n, v in V["resolved"]["dark"].items()}
TREE = {"core": {}, "light": {}, "dark": {}, "component": {}}


def _leaf(d, *path):
    cur = TREE[d]
    for p in path[:-1]:
        cur = cur.setdefault(p, {})
    return cur, path[-1]


def emit_at(root, path, leaf):
    cur = TREE[root]
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = leaf


def have_var(name):
    return name in R


def var(name, ty="color", root="core", path=None, desc=None):
    """Leaf resolved per theme from the var's declaration."""
    leaf = {"type": ty, "var": name}
    if desc:
        leaf["description"] = desc
    emit_at(root, path or name.lstrip("-").replace("--", ".").replace("-", "."), leaf)


def lit(value, ty, src, root="core", path=None, desc=None):
    leaf = {"type": ty, "value": value, "source": src}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)


# Names whose :root declaration is overridden in a @media (min|max-width)
# block — the resolved value is the 1440px view; the override list travels on
# $extensions.responsive.
RESP = {}
for rule in V.get("theme", []):
    for name in rule.get("properties", {}):
        media = [c for c in rule.get("context", []) if c.startswith("@media")]
        if media and rule["selector"].strip() == ":root":
            RESP.setdefault(name, set()).update(media)


def resp(leaf, name):
    if name in RESP:
        leaf = dict(leaf)
        leaf["responsive"] = sorted(RESP[name])
    return leaf


def VAR(name, ty, path, root="core", desc=None):
    leaf = {"type": ty, "var": name}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, resp(leaf, name))


def cam(name):
    """--foo-bar-baz -> fooBarBaz (a token key, not a CSS name)."""
    parts = name.lstrip("-").split("-")
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


KIND_TY = {"color": "color", "dimension": "dimension", "duration": "duration",
           "easing": "cubicBezier", "number": "number", "fontFamily": "fontFamily"}

# ---------------------------------------------------------------- palette
emitted = set()

def color_names(prefix):
    out = {}
    for n in R:
        if n.startswith(prefix + "-"):
            out[n[len(prefix) + 1:]] = n
    return out


for hue in ["neutral", "purple", "blue", "green", "red", "yellow", "orange", "pink"]:
    steps = color_names(f"--color-{hue}")
    for step, n in sorted(steps.items(), key=lambda kv: (len(kv[0]), kv[0])):
        VAR(n, "color", f"color.{hue}.{step}")
        emitted.add(n)
    if f"--color-{hue}" in R:
        VAR(f"--color-{hue}", "color", f"color.{hue}.default")
        emitted.add(f"--color-{hue}")
if "--color-white" in R:
    VAR("--color-white", "color", "color.white")
    emitted.add("--color-white")
for n in sorted(k for k in R if re.fullmatch(r"--alpha-(white|black)-\d+", k)):
    VAR(n, "color", f"color.alpha.{cam(n.replace('--alpha-', '--'))}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--label-[a-z]+", k)):
    VAR(n, "color", f"color.label.{n[len('--label-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--badge-[a-z]+(-bg)?", k)):
    hue, _, bg = n[len("--badge-"):].partition("-")
    VAR(n, "color", f"color.badge.{hue}.{'bg' if bg else 'fg'}")
    emitted.add(n)

# ------------------------------------------------------------ type scales
for n in sorted(k for k in R if k in ("--font-sans", "--font-mono")):
    VAR(n, "fontFamily", f"font.family.{n[len('--font-'):]}")
    emitted.add(n)
for n in sorted((k for k in R if re.fullmatch(r"--font-size-\d+", k)), key=lambda s: int(s.rsplit("-", 1)[1])):
    VAR(n, "dimension", f"font.size.{n[len('--font-size-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    VAR(n, "fontWeight", f"font.weight.{n[len('--font-weight-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--line-height-[a-z]+", k)):
    VAR(n, "number", f"font.lineHeight.{n[len('--line-height-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--letter-spacing-[a-z]+", k)):
    # em-valued tracking keeps its declared unit (type "other"): a px bake
    # would stop scaling with the element's font size.
    VAR(n, "other", f"font.letterSpacing.{n[len('--letter-spacing-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--text-body-(size|sm|md|lg)", k)):
    VAR(n, "dimension", f"font.text.body.{cam(n[len('--text-body-'):])}")
    emitted.add(n)
if "--text-body-lh" in R:
    VAR("--text-body-lh", "number", "font.text.body.lh")
    emitted.add("--text-body-lh")

# ------------------------------------------------------------- core scales
for n in sorted((k for k in R if re.fullmatch(r"--space-\d+", k)), key=lambda s: int(s.rsplit("-", 1)[1])):
    VAR(n, "dimension", f"space.{n[len('--space-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--space-(page-x|section-y|section-y-sm|card-gap)", k)):
    VAR(n, "dimension", f"space.{cam(n[len('--space-'):])}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--radius-\d+", k)):
    VAR(n, "dimension", f"radius.{n[len('--radius-'):]}")
    emitted.add(n)
if "--radius-full" in R:
    VAR("--radius-full", "dimension", "radius.full")
    emitted.add("--radius-full")
for n in sorted(k for k in R if re.fullmatch(r"--shadow-[a-z]+", k)):
    VAR(n, "other", f"shadow.{n[len('--shadow-'):]}",
        desc="Box-shadow stack, kept as the computed string — the site declares single-layer rgba shadows.")
    emitted.add(n)
for n in sorted((k for k in R if re.fullmatch(r"--duration-\d+", k)), key=lambda s: int(s.rsplit("-", 1)[1])):
    VAR(n, "duration", f"duration.{n[len('--duration-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--ease-[a-z-]+", k)):
    VAR(n, "cubicBezier", f"ease.{n[len('--ease-'):]}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--max-w-[a-z-]+", k)):
    VAR(n, "dimension", f"layout.maxW.{cam(n[len('--max-w-'):])}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--nb-[a-z-]+", k)):
    VAR(n, "dimension" if R[n]["kind"] == "dimension" else "other", f"layout.navbar.{cam(n[len('--nb-'):])}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--nav-bar-[a-z-]+", k)):
    VAR(n, "dimension" if R[n]["kind"] == "dimension" else "other", f"layout.navbar.{cam(n[len('--nav-bar-'):])}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--hero-[a-z-]+", k)):
    VAR(n, "dimension" if R[n]["kind"] == "dimension" else "other", f"layout.hero.{cam(n[len('--hero-'):])}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--cta-[a-z-]+", k)):
    VAR(n, "dimension" if R[n]["kind"] == "dimension" else "other", f"layout.cta.{cam(n[len('--cta-'):])}")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--filter-icon-[a-z]+", k)):
    VAR(n, "other", f"filter.icon.{cam(n[len('--filter-icon-'):])}",
        desc="A CSS filter() that recolours a raster icon to the role.")
    emitted.add(n)
for n in sorted(k for k in R if re.fullmatch(r"--gradient-[a-z-]+", k)):
    VAR(n, "other", f"gradient.{cam(n[len('--gradient-'):])}")
    emitted.add(n)
if "--text-body-color" in R:
    VAR("--text-body-color", "color", "font.text.body.color")
    emitted.add("--text-body-color")

# ------------------------------------------------------- semantic roles
# The :root declarations every component consumes. Resolved per theme:
# the `dark` set reads the :root (dark-painted) pass, `light` reads the
# .light-mode scope pass (what /library paints).
ROLE_GROUPS = [
    ("text", r"--text-(primary|secondary|tertiary|disabled|inverse|link|brand|success|warning|error)"),
    ("bg", r"--bg-(primary|secondary|tertiary|inverse|elevated|sunken|glass|glass-light|brand)"),
    ("border", r"--border-(primary|secondary|tertiary|card|subtle|transparent|transparent-subtle|active|focus|brand)"),
]
for group, pat in ROLE_GROUPS:
    for n in sorted(k for k in R if re.fullmatch(pat, k)):
        role = cam("-" + n[len(group) + 3:])  # '--bg-glass-light' -> 'glassLight'
        for theme in ("dark", "light"):
            VAR(n, "color", f"{group}.{role}", root=theme)
        emitted.add(n)

# ------------------------------------------------------------------ misc
# Every remaining theme-binned name not emitted above keeps its evidence
# under core.misc — page-scoped effect vars (angle stops, draw lengths, the
# benchmark --surf-*/--bar-* names, homepage-v3 vars).
for rule in V.get("theme", []):
    for n in rule.get("properties", {}):
        if n in emitted or n not in R:
            continue
        kind = R[n].get("kind", "other")
        VAR(n, KIND_TY.get(kind, "other"), f"misc.{cam(n)}")
        emitted.add(n)

# ------------------------------------------------- measured component tokens
C_PATH = RAW / "components-computed.json"
if C_PATH.exists():
    C = json.loads(C_PATH.read_text()).get("components", {})

    def geom(comp, state, field, path, label):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        rect = st.get("rect") or {}
        style = st.get("style") or {}
        v = rect.get(field) if field in rect else style.get(field)
        if v is None:
            return
        try:
            px = float(re.fullmatch(r"(-?\d+(?:\.\d+)?)(?:px)?", str(v)).group(1))
        except Exception:
            return
        lit(f"{px:g}px", "dimension",
            f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path)

    geom("mkt-header", "default", "h", "header.height", "site header height")
    geom("mkt-header", "default", "w", "header.width", "site header width")
    geom("mega-panel", "default", "w", "megaMenu.width", "opened mega-menu panel")
    geom("nav-cta", "default", "h", "button.headerCta.height", "header CTA")
    geom("plan-card", "default", "w", "planCard.width", "pricing plan card")
    geom("demo-email", "default", "h", "field.height", "demo-request e-mail field")
    geom("calc-range", "default", "h", "range.height", "calculator range input")
    geom("m-topbar", "default", "h", "mobileHeader.height", "mobile top bar")

    def style_tok(comp, state, prop, path, ty, label):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        if "style" not in st:
            return  # not captured: no token
        v = st["style"].get(prop)
        if v is None:
            # the kit records longhands only (borderTopLeftRadius, not borderRadius): a mapped
            # row that reads nothing on a captured state is a typo, never a silent skip
            raise KeyError(f"{comp} {state} has no computed {prop}")
        if ty == "color" and re.fullmatch(r"rgba\([^)]*,\s*0\)|transparent", str(v).strip()):
            # a transparent fill is not a surface: no token (the painted panel was not read)
            return
        lit(v, ty, f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path)

    style_tok("nav-cta", "default", "borderTopLeftRadius", "button.headerCta.radius", "dimension", "header CTA corner")
    style_tok("plan-card", "default", "borderTopLeftRadius", "planCard.radius", "dimension", "plan card corner")
    style_tok("glass-card", "default", "backgroundColor", "glassCard.bg", "color", "frosted glass card fill")
    style_tok("glass-card", "default", "backdropFilter", "glassCard.backdrop", "other", "frosted glass blur")
    style_tok("login-panel", "default", "backgroundColor", "auth.panel.bg", "color", "app-shell sign-in card")

(RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
