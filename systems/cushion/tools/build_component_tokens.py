#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cushion.so is a light-only Tailwind marketing site for an async-messaging
app. Its sheets declare a real var layer on :root, harvested into
raw/css-vars.json:

  --color-accent #00a6f4 / --color-accent-dark #0085c3   the brand blue + hover
  --color-background #fcfcfc, --color-foreground #000
  --color-gray-1..-12    the neutral ramp (#fafafa panel, #f5f5f5 page,
                         #858585 muted, #1f1f1f ink)
  --color-feature-*      the product-feature hues (posts/inbox/checkins/agents)
  Tailwind --color-<hue>-<step> palettes
  --font-inter-tight / --font-sans / --font-mono, --font-weight-*,
  --text-<step>(+line-height), --tracking-*, --leading-*
  --radius-sm..-3xl, --shadow-button/-floating/-popover/-raised,
  --border rgba(33,33,33,.1)
  --page-max-width 1280px, --page-padding-inline 16px, --container-*,
  --spacing 4px, --default-transition-*, --ease-*, --animate-*

Those become {"var": ...} leaves resolved by build_tokens.py. What the
vars do not name is a measured computed style
(raw/components-computed.json): the 72px sticky nav, the 44px/12px-radius
primary CTA, the 209x32 mock controls, the focus ring (2px white + 4px
#c2c2c2) and the opened-FAQ fill.

The sheets also declare a `.dark` block, but the public page never paints
it (body stays #f5f5f5); the export keeps the dark set empty and the gap
is documented, not promoted to a theme.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. cron.com's public "
    "surface splits in two: the dark marketing home (literal CSS, measured "
    "computed values) and the light Next.js content pages whose declared "
    "var layer (raw/css-vars.json: the 14-step gray ramp, --chronos brand, "
    "--elevation-*, --material-*/--object-* roles) is var-referenced "
    "wherever it names a value."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


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


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}

# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
# Read from the hero heading, not typed in: a recapture with another stack changes the token.
fam["display"] = {"value": st("hero-h1", "default")["fontFamily"],
    "type": "fontFamily",
    "source": "computed fontFamily of hero-h1 / feature-h2 / m-hero-h1 (raw/components-computed.json); css-var --font-inter-tight (raw/css-vars.json)",
    "description": "Inter Tight — every heading (hero 60px, sections 36px)."}
if "--font-sans" in R:
    fam["sans"] = var("--font-sans", "fontFamily",
        source="css-var --font-sans resolved (raw/css-vars.json)",
        description="The ui-sans-serif/system-ui stack on body, nav, buttons and cards.")
if "--font-mono" in R:
    fam["mono"] = var("--font-mono", "fontFamily",
        source="css-var --font-mono resolved (raw/css-vars.json)",
        description="The declared monospace stack.")
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, n, desc in [
    ("normal", "--font-weight-normal", "400 — body copy."),
    ("medium", "--font-weight-medium", "500 — nav links, CTAs, mock controls."),
    ("semibold", "--font-weight-semibold", "600 — every heading, the pricing CTA."),
    ("bold", "--font-weight-bold", "The declared 700 weight."),
]:
    if n in R:
        weights[key] = var(n, "fontWeight",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ----------------------------------------------------- declared palettes

col = SPEC["core"].setdefault("color", {})
brand = col.setdefault("cushion", {})
for key, n, desc in [
    ("accent", "--color-accent", "The #00a6f4 brand blue — primary CTAs."),
    ("accent-dark", "--color-accent-dark", "The #0085c3 hover/pressed blue."),
    ("background", "--color-background", "The #fcfcfc card/input surface."),
    ("foreground", "--color-foreground", "The declared #000 ink (page computes #1f1f1f)."),
]:
    if n in R:
        brand[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
feat = col.setdefault("feature", {})
for n in sorted(R):
    if n.startswith("--color-feature-"):
        feat[n[len("--color-feature-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Product-feature hue {n} (posts/inbox/checkins/agents).")
gray = col.setdefault("gray", {})
for n in sorted(R):
    if re.fullmatch(r"--color-gray-\d+", n):
        gray[n[len("--color-gray-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Neutral ramp step {n}.")
tail = col.setdefault("tailwind", {})
for n in sorted(R):
    if n.startswith("--color-") and not n.startswith(("--color-gray-", "--color-accent", "--color-background", "--color-foreground", "--color-feature-", "--color-black", "--color-white")):
        tail[n[len("--color-"):]] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)",
            description=f"Tailwind palette step {n}.")
for n, key, desc in [("--color-black", "black", "Declared #000."), ("--color-white", "white", "Declared #fff.")]:
    if n in R:
        col[key] = var(n, "color", source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ----------------------------------------------------- semantic roles (declared)

sem = SPEC["light"].setdefault("color", {})
for key, n, group, desc in [
    ("page", "--color-gray-2", "background", "The #f5f5f5 page field the body paints."),
    ("surface", "--color-background", "background", "The #fcfcfc surface (CTAs' secondary fill, FAQ rows, mock)."),
    ("panel", "--color-gray-1", "background", "The #fafafa plan-panel fill."),
    ("text", "--color-gray-12", "text", "The #1f1f1f ink on every page."),
    ("muted", "--color-gray-10", "text", "The #858585 hero-sub/muted text."),
    ("accent", "--color-accent", "action", "The #00a6f4 primary action."),
    ("accent-dark", "--color-accent-dark", "action", "The #0085c3 hover/pressed accent."),
    ("border", "--border", "border", "The rgba(33,33,33,.1) hairline on panels, CTAs, mock controls."),
    ("on-accent", "--color-white", "text", "White text on the accent."),
]:
    if n in R:
        sem.setdefault(group, {})[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ------------------------------------------------- measured color corrections

try:
    sem.setdefault("background", {})["faq-open"] = lit(
        st("faq-item", "opened")["backgroundColor"], "color",
        "computed backgroundColor of faq-item opened (raw/components-computed.json)",
        "The #ebebeb fill an opened FAQ row paints.")
except KeyError:
    pass
try:
    sem.setdefault("border", {})["focus-ring"] = lit(
        "rgb(194, 194, 194)", "color",
        "computed boxShadow of cta-start/signup-btn focus-visible (raw/components-computed.json): 2px white + 4px #c2c2c2 ring",
        "The #c2c2c2 outer focus ring (with a 2px white inner offset).")
except KeyError:
    pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, n, desc in [
    ("xs", "--text-xs", "The 12px step."), ("sm", "--text-sm", "The 14px mock-control/meta size."),
    ("base", "--text-base", "The 16px body/nav/CTA size."), ("lg", "--text-lg", "The 18px card-title step."),
    ("xl", "--text-xl", "The 20px hero-sub/pricing-CTA size."), ("2xl", "--text-2xl", "The 24px step."),
    ("3xl", "--text-3xl", "The 30px step."), ("4xl", "--text-4xl", "The 36px section/problem heading."),
    ("5xl", "--text-5xl", "The 48px mobile hero."), ("6xl", "--text-6xl", "The 60px desktop hero."),
    ("7xl", "--text-7xl", "The declared 72px step."),
]:
    if n in R:
        ty[key] = var(n, "fontSize",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
lead = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for n in sorted(R):
    if n.startswith("--leading-") or n.startswith("--tracking-"):
        grp = lead if n.startswith("--leading-") else SPEC["core"]["font"].setdefault("tracking", {})
        grp[n.split("-", 2)[-1]] = var(n, "other",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=f"Declared {n}.")

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, n, desc in [
    ("sm", "--radius-sm", "The declared 4px radius."),
    ("md", "--radius-md", "The 6px mock-control radius."),
    ("lg", "--radius-lg", "The 8px nav-button radius."),
    ("xl", "--radius-xl", "The 12px CTA/blog-card/mock-frame radius."),
    ("2xl", "--radius-2xl", "The 16px plan-panel/pricing-CTA radius."),
    ("3xl", "--radius-3xl", "The declared 24px radius."),
]:
    if n in R:
        radii[key] = var(n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
for key, n, desc in [
    ("button", "--shadow-button", "The 3-layer button shadow (1px drop + inset edges)."),
    ("floating", "--shadow-floating", "The floating-panel shadow stack."),
    ("popover", "--shadow-popover", "The popover shadow stack."),
    ("raised", "--shadow-raised", "The raised inset-edge shadow."),
]:
    if n in R:
        sh[key] = {"value": R[n], "type": "other",
                   "source": f"css-var {n} resolved (raw/css-vars.json)", "description": desc}

# ---------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
for key, n, desc in [
    ("unit", "--spacing", "The 4px spacing unit."),
    ("page-max", "--page-max-width", "The 1280px page column."),
    ("page-gutter", "--page-padding-inline", "The 16px page gutter."),
]:
    if n in R:
        sp[key] = var(n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
cont = sp.setdefault("container", {})
for n in sorted(R):
    if n.startswith("--container-"):
        cont[n[len("--container-"):]] = var(n, "dimension",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=f"Max-width step {n}.")

# ----------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
for key, n, ty_, desc in [
    ("default-duration", "--default-transition-duration", "duration", "The 150ms default."),
    ("default-easing", "--default-transition-timing-function", "cubicBezier", "The default cubic-bezier(.4,0,.2,1)."),
    ("ease-out", "--ease-out", "cubicBezier", "The declared ease-out."),
    ("animate-pulse", "--animate-pulse", "other", "The pulse keyframe binding."),
    ("animate-spin", "--animate-spin", "other", "The spin keyframe binding."),
    ("animate-blink", "--animate-blink", "other", "The blink keyframe binding."),
]:
    if n in R:
        mo[key] = var(n, ty_,
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, prop, ty_, desc in [
    ("nav-height", "nav-bar", "h", "dimension", "The 72px sticky nav."),
    ("nav-logo-width", "nav-logo", "w", "dimension", "The 112px wordmark."),
    ("nav-link-height", "nav-link", "h", "dimension", "The 40px nav link."),
    ("signup-height", "signup-btn", "h", "dimension", "The 40px nav sign-up button."),
    ("cta-height", "cta-start", "h", "dimension", "The 44px primary CTA."),
    ("cta-radius", "cta-start", "borderTopLeftRadius", "dimension", "The 12px CTA radius."),
    ("cta-human-width", "cta-human", "w", "dimension", "The 154px secondary CTA."),
    ("pricing-cta-height", "pricing-cta", "h", "dimension", "The 56px pricing CTA."),
    ("faq-row-height", "faq-item", "h", "dimension", "The 72px FAQ accordion row."),
    ("plan-panel-radius", "plan-panel", "borderTopLeftRadius", "dimension", "The 16px plan-panel radius."),
    ("blog-card-radius", "blog-card", "borderTopLeftRadius", "dimension", "The 12px blog-card radius."),
    ("mock-frame-width", "mock-frame", "w", "dimension", "The 1280px app-mock window."),
    ("mock-control-height", "mock-newpost", "h", "dimension", "The 32px mock button/row height."),
    ("mock-post-height", "mock-post", "h", "dimension", "The 108px mock post card."),
    ("m-hero-size", "m-hero-h1", "fontSize", "fontSize", "The 48px mobile hero."),
]:
    try:
        s_ = C[cname]["states"]["default"]
        if prop in ("w", "h"):
            v = s_["rect"][prop]
        elif prop == "bg":
            v = s_["style"]["backgroundColor"]
        else:
            v = s_["style"][prop]
        if v and v not in ("0px", "auto", "rgba(0, 0, 0, 0)"):
            comp[name] = lit(v, ty_,
                f"computed {prop} of {cname} default (raw/components-computed.json)", desc)
    except KeyError:
        pass
# measured state moves on the interactive controls
for name, cname, desc in [
    ("cta-state-track", "cta-start",
     "Primary CTA: #00a6f4 at rest, #0085c3 (--color-accent-dark) on hover and pressed; pressed also shrinks ~2%."),
    ("nav-state-track", "nav-link",
     "Nav link: transparent at rest, 5% black fill on hover and pressed."),
    ("faq-state-track", "faq-item",
     "FAQ row: #fcfcfc at rest, #ebebeb when opened."),
]:
    try:
        comp.setdefault("state-track", {})[name] = {
            "type": "other",
            "value": {s2: {p: st(cname, s2)[p] for p in ("backgroundColor", "color", "transform") if st(cname, s2).get(p)}
                      for s2 in ("default", "hover", "pressed", "opened") if s2 in C[cname]["states"]},
            "source": f"computed styles of {cname} across states (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass
# the shared focus ring
try:
    comp["focus-ring"] = lit(
        st("cta-start", "focus-visible")["boxShadow"],
        "other",
        "computed boxShadow of cta-start focus-visible (raw/components-computed.json)",
        "2px white + 4px #c2c2c2 ring plus a rgb(0,95,204) outline — identical on every measured control.")
except KeyError:
    pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
