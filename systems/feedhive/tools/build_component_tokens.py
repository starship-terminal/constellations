#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

feedhive.com signed out is two surfaces:

  www.feedhive.com — a light-only Next.js marketing site built on Tailwind
  CSS v4. Its declared custom-property layer (raw/css-vars.json) is thin:
  the Tailwind theme defaults (--font-sans/--font-mono stacks, --color-black/
  --color-white, --spacing, --text-sm/--text-lg with --line-height
  companions, --font-weight-*, --leading-tight, --radius-md/lg/xl,
  --container-xs, --ease-out, --default-transition-*, --animate-*) plus
  FeedHive's own .cta-gradient-ring custom properties (--cta-border-angle,
  --cta-ring-*, --cta-glow-*), and a themed vendor layer (vanilla-
  cookieconsent's --cc-*, whose --cc-btn-primary-bg confirms the brand
  indigo #4457ff). There is no data-mode, no user theme toggle and no
  dark set — nearly every real value rides arbitrary-value utilities
  (bg-[#4457ff], text-[#23252b], rounded-[15px]), so the measured
  computed styles in raw/components-computed.json carry most of the
  evidence.

  app.feedhive.com — a separate Chakra-UI (Emotion css-*) sign-in/sign-up
  app that shares no token layer with the marketing site: a white 512px
  card (20px radius) over a pale field, 9999px-pill controls, a #3b82f6
  submit blue and a #5d60ec link violet. Its values land under
  component.login.* as measured literals, honestly labelled.

Measured structure (desktop 1440 x 900, mobile 390 x 844):

  fonts   Inter (UI/body, next/font variable wght 100-900 + "Inter
          Fallback"), Plus Jakarta Sans (display headings: h1s, plan
          names), Sometype Mono (tracked caps eyebrows and card labels);
          the Chakra app uses a plain "Inter, sans-serif" stack
  ramp    arbitrary px sizes — 68/64/62/60/58/55px display headings
          (46px at 390 wide), 31px plan names, 15-16px body/CTA, 14px
          UI, 13px micro, 12px dropdown labels, 11px mono labels; the
          Chakra app paints 14.72px controls
  colour  brand indigo #4457ff (bg-primary, hover #3347fb), selected
          tint #eef2ff with #5a84ff ink and #84a1ff border, inks
          #23252b/#20232b/#17191f/#22252d, muted grays #666c77-#8b9098,
          warm subtle surfaces #f4f3f2/#f4f2f0/#f6f6f8/#fbfaf7, hairline
          borders #dfdfe4/#d8dbe2/#e6e2dc
  shape   11px nav/secondary pills, 15px hero/plan CTAs, 9px option
          chips, 12px fields, 16px cards and media clips, 18px dropdown
          items, 20px Chakra card, full pills (Tailwind rounded-full
          serialises to 3.35544e+07px; Chakra paints literal 9999px)
  motion  the declared 0.15s cubic-bezier(.4,0,.2,1) control transition;
          the cta-gradient-ring border angle animates 0deg -> 1turn
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. feedhive.com's "
    "declared custom-property layer (raw/css-vars.json) is thin — the "
    "Tailwind-v4 theme defaults, FeedHive's .cta-gradient-ring properties "
    "and the themed cookie-consent vendor vars — so declared scales land "
    "under core.* as {var} leaves where they resolve, and everything the "
    "site paints through arbitrary-value utilities lands as measured "
    "literals carrying the component/state they were read from. The site "
    "is light-only: the dark set stays empty."),
    "core": {}, "light": {}, "dark": {}, "component": {}}



def gradient_stops(body):
    """The colour stops of a linear-gradient() body after its angle, split on
    top-level commas only (rgb(), oklab() keep their commas) and keeping an
    explicit stop position; stops without one are spread evenly, as CSS does
    between known neighbours (2026-11 audit, finding 14-29)."""
    parts, depth, cur = [], 0, ""
    for ch in body:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            parts.append(cur.strip()); cur = ""
        else:
            cur += ch
    parts.append(cur.strip())
    stops = []
    for p in parts:
        m = re.fullmatch(r"(.+?\)|#[0-9a-fA-F]{3,8}|[a-z]+)(?:\s+(-?[\d.]+)%)?", p)
        if not m:
            raise ValueError(f"unreadable gradient stop {p!r}")
        stops.append([m.group(1), None if m.group(2) is None else float(m.group(2)) / 100])
    if stops[0][1] is None:
        stops[0][1] = 0.0
    if stops[-1][1] is None:
        stops[-1][1] = 1.0
    # CSS: a position smaller than an earlier one is moved up to it, before
    # the missing positions are spread
    top = float("-inf")
    for st in stops:
        if st[1] is not None:
            st[1] = max(st[1], top)
            top = st[1]
    i = 0
    while i < len(stops):
        if stops[i][1] is None:
            j = i
            while stops[j][1] is None:
                j += 1
            a, b = stops[i - 1][1], stops[j][1]
            for k in range(i, j):
                stops[k][1] = a + (b - a) * (k - i + 1) / (j - i + 1)
            i = j
        i += 1
    return [(c, round(pos, 4)) for c, pos in stops]

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
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


EMITTED = {}
_OWNER = {}


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf):
    node = root
    parts = name[2:].split("-")
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


DECL_SRC = "declared custom property in the site's css bundle (raw/css-vars.json)"


def declared(name):
    v = R.get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


def decl(name, ty="dimension"):
    v = declared(name)
    desc = f"The declared `{name}`."
    if ty == "dimension":
        nv = norm_len(v)
        if nv != v:
            raw = (RL.get(name) or {}).get("raw")
            desc = f"The declared `{name}` — `{raw}`, which Chromium resolves to {nv} (effectively a full pill)."
            v = nv
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
            ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", desc)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")


def decl_color(name):
    v = declared(name)
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def ratio(name):
    v = declared(name)
    m = re.fullmatch(r"calc\(\s*(-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\s*\)", str(v))
    if m:
        return lit(round(float(m.group(1)) / float(m.group(2)), 4), "number",
                   f"{DECL_SRC}: {name}", f"The declared `{name}` line-height ratio.")
    return decl(name, "other")


def painted(comp, state, key, node=None):
    """The painted layer's reading for key. node pins the layer (a regex on its
    tag+classes) when the token names a specific child — without it the
    size-matched preference returns the component's own box, which is the
    wrong layer for a value measured on an inner element."""
    c = C[comp]["states"][state]
    entries = [p for p in c.get("paint") or [] if p.get(key)]
    if node is not None:
        entries = [p for p in entries if re.search(node, p.get("node") or "")]
    if not entries:
        raise KeyError(key)
    rect = c.get("rect") or {}
    for p in entries:
        m = re.fullmatch(r"([\d.]+)x([\d.]+)", str(p.get("size") or ""))
        if m and abs(float(m.group(1)) - rect.get("w", -9)) <= 1 and abs(float(m.group(2)) - rect.get("h", -9)) <= 1:
            return p[key]
    return entries[0][key]


# ------------------------------------------------------------------- fonts
#
# The marketing site loads three next/font faces: Inter (every control and
# body), Plus Jakarta Sans (display headings and plan names) and Sometype
# Mono (tracked caps eyebrows/labels). The declared --font-sans/--font-mono
# are only the Tailwind default stacks — kept as the system fallbacks they
# are. The Chakra sign-in/up app uses a plain "Inter, sans-serif" stack.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("sans", "promo-bar", "default",
     "Inter — every control and body on the marketing site (next/font variable wght 100-900, with the local \"Inter Fallback\" metrics face)."),
    ("display", "hero-h1", "default",
     "Plus Jakarta Sans — display headings, section titles and plan names."),
    ("mono", "feat-eyebrow", "default",
     "Sometype Mono — the tracked caps eyebrow labels and card kicker labels."),
]:
    try:
        fam[key] = lit(st(comp, state)["fontFamily"], "fontFamily",
                       f"computed fontFamily of {comp} {state} (raw/components-computed.json); @font-face declared in the site's css bundle (raw/css-vars.json fonts list)", desc)
    except KeyError:
        pass
if declared("--font-sans") is not None:
    fam["sansSystem"] = var("--font-sans", "fontFamily",
                            description="The declared Tailwind default sans stack — the fallback the site never reaches behind its next/font Inter.")
if declared("--font-mono") is not None:
    fam["monoSystem"] = var("--font-mono", "fontFamily",
                            description="The declared Tailwind default mono stack — the fallback behind Sometype Mono.")
try:
    fam["app"] = lit(st("login-panel", "default")["fontFamily"], "fontFamily",
                     "computed fontFamily of login-panel default on app.feedhive.com/signin (raw/components-computed.json)",
                     "The Chakra sign-in/up app's plain Inter stack — a different font layer from the marketing site.")
except KeyError:
    pass

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    weights[name[len("--font-weight-"):]] = decl(name, "fontWeight")

# ------------------------------------------------------------- type ramp
#
# The marketing site spells its ramp in arbitrary px utilities. Declared
# --text-sm/--text-lg are the only named steps; the display sizes are
# measured per headline. Letter spacing rides the same utilities (-0.02em
# to -0.04em on most text, +~0.14em on the mono caps labels).

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in sorted(k for k in R if re.fullmatch(r"--text-(sm|lg)", k)):
    sizes[name[len("--text-"):]] = var(name, "dimension")

measured_sizes = SPEC["core"]["font"]["size"].setdefault("measured", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The 55px home hero masthead (Plus Jakarta Sans 600)."),
    ("h1Blog", "blog-h1", "default", "The 68px blog masthead."),
    ("h1Pricing", "price-h1", "default", "The 64px pricing masthead."),
    ("h1Feature", "feat-h1", "default", "The 62px feature-page masthead."),
    ("h1Tool", "bio-h1", "default", "The 60px tool-page masthead."),
    ("h2Section", "section-h2", "default", "The 58px marketing section heading."),
    ("h1Mobile", "m-hero-h1", "default", "The 46px mobile hero masthead at 390 wide."),
    ("planName", None, None, "The 31px plan-card name (Business/Creator/Agency/Brand)."),
    ("body", "mkt-header", "default", "The 16px default body size."),
    ("cta", "hero-cta", "default", "The 15px CTA/plan-button size."),
    ("ui", "nav-link", "default", "The 14px UI/nav size."),
    ("micro", "bio-tone", "default", "The 13px micro size (tone options, blog meta)."),
    ("appControl", "login-google", "default", "The 14.72px Chakra control size."),
]:
    try:
        if comp is None:
            raw = ts("plan-card", "default", "fontSize")
            src = "the first text node's fontSize on plan-card default (raw/components-computed.json)"
        else:
            raw = st(comp, state)["fontSize"]
            src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        measured_sizes[key] = lit(raw, "dimension", src, desc)
    except (KeyError, TypeError):
        pass

lineheights = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
if declared("--leading-tight") is not None:
    lineheights["tight"] = decl("--leading-tight", "number")
for name in sorted(k for k in R if re.fullmatch(r"--text-(sm|lg)--line-height", k)):
    lineheights[name[len("--text-"):].replace("--line-height", "")] = ratio(name)

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The -0.035em display tracking (-1.925px at 55px)."),
    ("lede", "hero-sub", "default", "The -0.026em lede tracking (-0.416px at 16px)."),
    ("body", "nav-login", "default", "The -0.02em body/UI tracking (-0.28px at 14px)."),
    ("button", "hero-cta", "default", "The -0.03em button tracking (-0.45px at 15px)."),
    ("nav", "nav-link", "default", "The -0.01em nav tracking (-0.14px at 14px)."),
    ("caps", "feat-eyebrow", "default", "The +0.14em tracked caps eyebrow (+1.96px at 14px)."),
    ("capsMenu", None, None, "The +0.2em tracked caps dropdown-group label (+2.4px at 12px)."),
]:
    try:
        if comp is None:
            raw = ts("nav-panel", "default", "letterSpacing")
            src = "the first text node's letterSpacing on nav-panel default (raw/components-computed.json)"
        else:
            raw = st(comp, state)["letterSpacing"]
            src = f"computed letterSpacing of {comp} {state} (raw/components-computed.json)"
        tracking[key] = lit(raw, "other", src, desc)
    except (KeyError, TypeError):
        pass

# ---------------------------------------------------------- core scales
#
# The declared layer: Tailwind theme defaults plus FeedHive's
# .cta-gradient-ring properties.

colors = SPEC["core"].setdefault("color", {})
if declared("--color-white") is not None:
    colors["white"] = decl_color("--color-white")
if declared("--color-black") is not None:
    colors["black"] = decl_color("--color-black")

if declared("--spacing") is not None:
    SPEC["core"].setdefault("spacing", {})["base"] = decl("--spacing")

radii = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if re.fullmatch(r"--radius-[a-z]+", k)):
    radii[name[len("--radius-"):]] = decl(name)
radius_alias = {norm_len(R[n]): n[len("--radius-"):] for n in R if re.fullmatch(r"--radius-[a-z]+", n)}

containers = SPEC["core"].setdefault("container", {})
for name in sorted(k for k in R if re.fullmatch(r"--container-[a-z0-9]+", k)):
    containers[name[len("--container-"):]] = decl(name)

easing = SPEC["core"].setdefault("easing", {})
for name in sorted(k for k in R if k.startswith("--ease-")):
    easing[name[len("--ease-"):]] = decl(name, "cubicBezier")
if declared("--default-transition-timing-function") is not None:
    easing["default"] = decl("--default-transition-timing-function", "cubicBezier")
if declared("--default-transition-duration") is not None:
    SPEC["core"].setdefault("duration", {})["default"] = decl("--default-transition-duration", "duration")

anim = SPEC["core"].setdefault("animate", {})
for name in sorted(k for k in R if k.startswith("--animate-")):
    anim[name[len("--animate-"):]] = decl(name, "other")

# The .cta-gradient-ring custom properties — declared on the ring class,
# not :root, so they are emitted as literals sourced to the declaration.
cta_ring = SPEC["core"].setdefault("ctaRing", {})
app_props = {}
for rule in V.get("app", []):
    sel = rule.get("selector") or ""
    for k, v in (rule.get("properties") or {}).items():
        if k.startswith("--cta-"):
            app_props.setdefault(k, {})[sel] = v
for name, key, desc in [
    ("--cta-ring-inset", "ringInset", "The gradient ring's -4px outset around squared CTAs (-3px on pill badges)."),
    ("--cta-ring-radius", "ringRadius", "The 18px ring radius for squared CTAs (9999px on pill badges)."),
    ("--cta-glow-inset", "glowInset", "The glow layer's -6px outset (-5px on pills)."),
    ("--cta-glow-radius", "glowRadius", "The 20px glow radius (9999px on pills)."),
    ("--cta-border-angle", "borderAngle", "The conic-gradient angle, animated 0deg -> 1turn by the cta-gradient-shift keyframes."),
]:
    if name in app_props:
        vals = app_props[name]
        leaf_ = lit(vals.get(".cta-gradient-ring", next(iter(vals.values()))), "other",
                    f"{DECL_SRC}: {name} on .cta-gradient-ring"
                    + (f" (overridden to {vals['.cta-gradient-ring-pill']} on .cta-gradient-ring-pill)" if ".cta-gradient-ring-pill" in vals else ""),
                    desc)
        if name == "--cta-border-angle":
            leaf_["angle"] = "animated to 1turn by @keyframes cta-gradient-shift (raw/css-vars.json skins bin)"
        cta_ring[key] = leaf_

# --------------------------------------------- measured roles (light)
#
# Roles measured on the real pages. The site is light-only: SPEC['dark']
# stays empty and the tokens.json $themes entry says so.

sem = SPEC["light"]


def msrc(comp, state, prop, extra=""):
    return f"computed {prop} of {comp} {state} (raw/components-computed.json){extra}"


for key, comp, state, prop, group, desc in [
    ("page", None, None, "value:#ffffff", "background", "The white page field every marketing page paints."),
    ("subtle", "promo-bar", "default", "backgroundColor", "background", "The warm off-white #f4f3f2 of the promo bar."),
    ("card", "agent-card", "default", "backgroundColor", "background", "The #f6f6f8 card fill (agent cards, blog archive rows)."),
    ("cardHover", "agent-card", "hover", "backgroundColor", "background", "The #f0f1f6 card hover fill."),
    ("pillNeutral", "nav-login", "default", "backgroundColor", "background", "The #f4f2f0 neutral pill behind the Login button."),
    ("pillNeutralHover", "nav-login", "hover", "backgroundColor", "background", "The #efedeb neutral-pill hover fill."),
    ("menuItemHover", "nav-menu-item", "hover", "backgroundColor", "background", "The #f8f8f7 dropdown item hover fill."),
    ("drawer", "m-drawer", "default", "backgroundColor", "background", "The #fbfaf7 mobile nav overlay fill."),
    ("selectedTint", "tab-pill", "selected", "backgroundColor", "background", "The #eef2ff selected-pill tint."),
    ("ink", "hero-h1", "default", "textColor", "text", "The #23252b heading ink (display copy, card titles)."),
    ("body", "mkt-header", "default", "color", "text", "The #20232b default body ink."),
    ("mobile", "m-menu-btn", "default", "textColor", "text", "The #17191f ink on the mobile menu rows."),
    ("muted", "hero-sub", "default", "textColor", "text", "The #666c77 muted lede gray."),
    ("gray", "billing-monthly", "default", "color", "text", "The #757b86 unselected-toggle gray."),
    ("linkInk", "nav-dropdown", "default", "textColor", "text", "The #4f5562 nav-pill ink."),
    ("navHover", "nav-dropdown", "hover", "textColor", "text", "The #22252d nav ink on hover/open."),
    ("faint", "nav-panel", "default", "text", "text", "The #8b9098 faint dropdown-group label."),
    ("meta", "blog-row", "default", "text", "text", "The #6c7280 blog-meta gray."),
    ("monoLabel", "agent-card", "default", "text", "text", "The #4457ff mono kicker label inside feature cards (brand indigo on light tint)."),
]:
    try:
        if prop == "value:#ffffff":
            sem.setdefault(group, {})[key] = lit("#ffffff", "color",
                "computed backgroundColor of the <main> page wrapper and every white surface (raw/components-computed.json ancestors/paint lists)",
                desc)
            continue
        if prop == "text":
            raw = ts(comp, state, "color")
            src = f"the first text node's color on {comp} {state} (raw/components-computed.json)"
        elif prop == "textColor":
            raw = ts(comp, state, "color")
            src = f"the first text node's color on {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = msrc(comp, state, prop)
        if raw in (None, ""):
            raise KeyError(prop)
        sem.setdefault(group, {})[key] = lit(raw, "color", src, desc)
    except (KeyError, TypeError):
        pass

for key, comp, state, prop, group, desc in [
    ("fill", "nav-signup", "default", "backgroundColor", "action",
     "The #4457ff brand indigo — bg-primary on CTAs, the Business plan card, the selected billing toggle; also the declared vendor --cc-btn-primary-bg and the Tailwind ring-primary/20 source."),
    ("fillHover", "nav-signup", "hover", "backgroundColor", "action",
     "The #3347fb indigo hover step — also the declared vendor --cc-btn-primary-hover-bg."),
    ("ink", "nav-signup", "default", "color", "action", "The white ink on indigo fills."),
    ("selectedInk", "tab-pill", "selected", "color", "action", "The #5a84ff ink on the selected tab pill."),
    ("selectedBorder", "tab-pill", "selected", "borderTopColor", "action", "The #84a1ff border on the selected tab pill."),
    ("selectedBg", "billing-monthly", "selected", "backgroundColor", "action", "The #3347fb selected billing-toggle fill (the darker indigo step)."),
    ("disabledFill", "bio-submit", "default", "backgroundColor", "action", "The #b9c0f5 desaturated indigo of the at-rest (disabled-looking) Generate button."),
]:
    try:
        raw = st(comp, state)[prop]
        if raw in (None, ""):
            raise KeyError(prop)
        sem.setdefault(group, {})[key] = lit(raw, "color", msrc(comp, state, prop), desc)
    except KeyError:
        pass

for key, comp, state, prop, group, desc in [
    ("input", "bio-tone", "default", "borderTopColor", "border", "The #dfdfe4 input/badge hairline."),
    ("tab", "tab-pill", "default", "borderTopColor", "border", "The #d8dbe2 dashed tab-pill border at rest."),
    ("panel", "nav-panel", "default", "paint:border", "border", "The #efefed hairline on the open nav panel."),
    ("iconTile", "nav-menu-item", "default", "paint:border", "border", "The #e8e7e4 border on the 48px dropdown icon tiles."),
    ("rule", "blog-row", "default", "paint:border", "border", "The #e7e8ec divider inside the blog rows."),
    ("footerRule", None, None, "value:#e6e2dc", "border", "The #e6e2dc footer top rule (border-[#e6e2dc], visible in footer-light crops)."),
    ("badgeChip", "hero-badge", "default", "paint:border", "border", "The #cfd1d9 border on the inner rounded chip of the gradient-ring badge."),
]:
    # Painted-layer picks that must not fall back to the component's own box:
    # badgeChip names the inner rounded chip (the span inside the badge pill),
    # whose #cfd1d9 border is not the outer pill's #dfdfe4 hairline.
    PAINT_NODE = {"badgeChip": r"^span\."}
    try:
        if prop == "paint:border":
            raw = painted(comp, state, "border", PAINT_NODE.get(key))
            m = re.search(COLOR_V.pattern, raw)
            raw = m.group(1) if m else raw
            src = f"the painted border layer on {comp} {state} (raw/components-computed.json paint list)"
        elif prop == "value:#e6e2dc":
            raw = "#e6e2dc"
            src = "the border-[#e6e2dc] utility on the footer's top rule (painted layer in raw/components-computed.json paint lists)"
        else:
            raw = st(comp, state)[prop]
            src = msrc(comp, state, prop)
        if raw in (None, ""):
            raise KeyError(prop)
        sem.setdefault(group, {})[key] = lit(raw, "color", src, desc)
    except (KeyError, TypeError):
        pass

# The keyboard focus ring: Tailwind's focus:ring-primary/20 compiles to a
# declared --tw-ring-color literal in the utility layer.
focus_ring = None
for rule in V.get("tailwind", []):
    if "ring-primary" in (rule.get("selector") or ""):
        v = (rule.get("properties") or {}).get("--tw-ring-color")
        if v:
            focus_ring = v
            break
if focus_ring:
    m = re.fullmatch(r"#([0-9a-fA-F]{6})([0-9a-fA-F]{2})", focus_ring)
    if m:
        focus_ring = "rgba(%d, %d, %d, %s)" % (int(m.group(1)[0:2], 16), int(m.group(1)[2:4], 16), int(m.group(1)[4:6], 16), "%g" % (int(m.group(2), 16) / 255))
    sem.setdefault("focus", {})["ring"] = lit(
        focus_ring, "color",
        "the declared --tw-ring-color on .focus:ring-primary/20:focus in the site's css bundle (raw/css-vars.json tailwind bin)",
        "The primary/20 focus ring on keyboard focus.")

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("navPill", "nav-login", "default", "borderTopLeftRadius", "The 11px radius on the header's 40px pills."),
    ("cta", "hero-cta", "default", "borderTopLeftRadius", "The 15px radius on the 50px hero/plan CTAs."),
    ("option", "bio-platform", "default", "borderTopLeftRadius", "The 9px radius on option chips."),
    ("field", "bio-textarea", "default", "borderTopLeftRadius", "The 12px field radius."),
    ("card", "hero-mock", "default", "borderTopLeftRadius", "The 16px card/media radius."),
    ("menuItem", "nav-menu-item", "default", "borderTopLeftRadius", "The 18px dropdown item radius."),
    ("chakraCard", "login-panel", "default", "borderTopLeftRadius", "The 20px Chakra sign-in card radius."),
    ("pill", "tab-pill", "default", "borderTopLeftRadius", "The full pill (Tailwind rounded-full; Chakra spells it 9999px)."),
]:
    try:
        v = norm_len(st(comp, state)[prop])
        dkey = radius_alias.get(v)
        src = msrc(comp, state, prop)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --radius-{dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("nav-login", "hover")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
        val = ", ".join(f"{p} {dur} {ease or ''}".strip() for p in props)
        mo["control"] = lit(val, "other",
            "computed transition of nav-login hover (raw/components-computed.json); the declared --default-transition-duration/.4-0-.2-1 pair",
            "The 0.15s transition on pills and controls.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("promo-height", "promo-bar", "default", "h", "dimension", "The 38px launch promo bar."),
    ("header-height", "mkt-header", "default", "h", "dimension", "The 80px marketing header."),
    ("nav-pill-height", "nav-login", "default", "h", "dimension", "The 40px header pills."),
    ("signup-pill-width", "nav-signup", "default", "w", "dimension", "The ~88px Sign Up pill width."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The 50px hero/plan CTA height."),
    ("hero-cta-width", "hero-cta", "default", "w", "dimension", "The ~196px hero CTA width."),
    ("nav-panel-height", "nav-panel", "default", "h", "dimension", "The open nav dropdown panel height."),
    ("hero-mock-width", "hero-mock", "default", "w", "dimension", "The hero product-mock clip width."),
    ("hero-mock-height", "hero-mock", "default", "h", "dimension", "The hero product-mock clip height."),
    ("agent-card-width", "agent-card", "default", "w", "dimension", "The ~585px agent feature card width."),
    ("agent-card-height", "agent-card", "default", "h", "dimension", "The ~416px agent feature card height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The ~297px plan card width."),
    ("plan-card-height", "plan-card", "default", "h", "dimension", "The ~653px plan card height."),
    ("billing-toggle-width", "billing-monthly", "default", "w", "dimension", "The 112px billing toggle half width."),
    ("billing-toggle-height", "billing-monthly", "default", "h", "dimension", "The 41px billing toggle height."),
    ("tab-pill-height", "tab-pill", "default", "h", "dimension", "The 30px feature tab pill height."),
    ("feature-card-height", "feat-card", "default", "h", "dimension", "The ~225px feature grid card height."),
    ("blog-featured-height", "blog-card", "default", "h", "dimension", "The ~420px featured blog card height."),
    ("bio-field-width", "bio-textarea", "default", "w", "dimension", "The ~362px bio-generator field width."),
    ("bio-submit-height", "bio-submit", "default", "h", "dimension", "The 50px Generate button height."),
    ("footer-height", "footer", "default", "h", "dimension", "The ~814px footer height."),
    ("mobile-header-height", "m-header", "default", "h", "dimension", "The 76px phone header."),
    ("mobile-menu-size", "m-menu-btn", "default", "w", "dimension", "The 44px mobile menu button."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# app.feedhive.com is a separate Chakra-UI app outside the marketing token
# layer; its measured values are kept as literals, honestly labelled.
login = comp.setdefault("login", {})
for name, cname, state, prop, ty_, desc in [
    ("panel-width", "login-panel", "default", "w", "dimension", "The 512px sign-in card."),
    ("panel-height", "login-panel", "default", "h", "dimension", "The ~610px sign-in card height (821px on sign-up)."),
    ("panel-radius", "login-panel", "default", "borderTopLeftRadius", "dimension", "The 20px card radius."),
    ("panel-shadow", "login-panel", "default", "boxShadow", "other", "The card's two-layer lift shadow."),
    ("panel-ink", "login-panel", "default", "color", "color", "The #1a202c card ink."),
    ("field-height", "login-field-email", "default", "h", "dimension", "The ~61px pill field/button height."),
    ("field-border", "login-field-email", "default", "borderTopColor", "color", "The #edf2f7 field outline border."),
    ("field-focus", "login-field-email", "focused", "borderTopColor", "color", "The #3b82f6 focused field border."),
    ("control-shadow", "login-google", "default", "boxShadow", "other", "The rgba(27,25,121,.05) 0 2px 8px resting shadow on outlined controls."),
    ("submit-fill", "login-submit", "default", "backgroundColor", "color", "The #3b82f6 submit blue — Chakra blue, not the marketing #4457ff indigo."),
    ("submit-glow", "login-submit", "default", "boxShadow", "other", "The rgba(89,106,255,.28) 0 0 35px 10px glow behind the submit."),
    ("submit-height", "login-submit", "default", "h", "dimension", "The ~59px submit height."),
    ("google-hover", "login-google", "hover", "backgroundColor", "color", "The #f7fafc Google-button hover fill."),
    ("link", "login-forgot", "default", "color", "color", "The #5d60ec link violet."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            login[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on app.feedhive.com (raw/components-computed.json)", desc)
        else:
            login[name] = lit(st(cname, state)[prop], ty_,
                              f"computed {prop} of {cname} {state} on app.feedhive.com (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The sign-in submit paints an opaque linear-gradient(60deg, #4457ff,
# #7583fd) over its #3b82f6 backgroundColor — keep the gradient as its own
# token so the style-guide mock reproduces the captured fill, not just the
# flat colour underneath.
try:
    bgi = st("login-submit", "default")["backgroundImage"]
    m = re.fullmatch(r"linear-gradient\((-?[\d.]+)deg,\s*(.+)\)", bgi.strip())
    if m:
        login["submit-gradient"] = {
            "$value": [{"color": norm_color(col), "position": pos} for col, pos in gradient_stops(m.group(2))],
            "$type": "gradient",
            "$extensions": {
                "source": "computed backgroundImage of login-submit default on app.feedhive.com (raw/components-computed.json)",
                "angle": m.group(1) + "deg"},
            "$description": "The opaque linear-gradient(60deg, #4457ff, #7583fd) painted over the sign-in submit's #3b82f6 backgroundColor.",
        }
except KeyError:
    pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
