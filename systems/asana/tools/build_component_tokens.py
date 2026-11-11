#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

asana.com is a Next.js marketing site that ships Asana's real design-token
layer in its stylesheets (raw/css-vars.json, read by tools/capture/vars.mjs):

  --black-20..1100, --blue-0..980, --coral-*, --green*, --purple-*,
  --gold-1..5, --teal-1..5, --orange-*, --bright-*-1..4, --glow-*,
  --chartreuse-*, --fuchsia-*, --command-*, --amber, --red, --green,
  --google-sign-up-blue[-light]
                              full colour ramps, hundreds of steps
  --lightmode-* (62 names)    the light semantic layer: bg/med/strong,
                              text/weak/strong, border/weak/strong,
                              button-primary/secondary + hover/disabled,
                              link, icon, accent-*, error/success/warning,
                              a11y-focus-*
  --darkmode-* (62 names)     the same roles darkened — declared in the
                              shipped CSS; the marketing pages don't bind a
                              dark theme, but the vars are real product
                              tokens and are emitted as the dark set
  --fontSize-*/--fontWeight-*/--fontFamily-*
                              the type scale (base 16, h1-h6 56..16, xl 82,
                              larger 51px) and weights 300..700
  --spacing-0..10             the 16px-base spacing scale
  --border-radius             3px
  --shadow-10..40 + --shadow-color
                              four real elevation levels
  --media-xsmall..xxxlarge    breakpoints 480..1920 (16px-base rem widths)
  --grid-columns/-gutter-width 12-column grid, 32px gutters
  --zIndex-1..10              the stacking scale 100..1000
  --transition-duration[-short/-med/-long/-xlong]
                              75/150/225/300/450ms motion tokens
  [data-theme] blocks         section colour schemes (white/gray/dark-blue/
                              dark-coral/dark-green/dark-purple/light-blue/
                              light-coral...) that re-slot the semantic vars

The marketing surface paints light; the dark set is emitted from the
declared --darkmode-* vars (declared in the shipped CSS, unbound on the
captured routes). A leaf is {"var": "--name"} (resolved by build_tokens.py)
or {"value": ..., "source": "..."} for a measured value.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. asana.com ships "
    "Asana's design-token layer in the marketing CSS: full colour ramps, the "
    "--lightmode-*/--darkmode-* semantic role sets, type/spacing/breakpoint/"
    "grid/zIndex/shadow/transition scales and section [data-theme] schemes. "
    "The light set aliases the --lightmode-* vars; the dark set aliases the "
    "declared --darkmode-* vars (unbound on the captured surface); measured "
    "component values come from raw/components-computed.json."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        node.setdefault("default", None)
        last = "default"
    return node, last


def emit(root, name, leaf):
    node, last = descend(root, name[2:].split("-"))
    node[last] = leaf


KIND = {"color": "color", "dimension": "dimension", "fontFamily": "fontFamily",
        "duration": "duration", "easing": "cubicBezier", "number": "number",
        "shadow": "other"}

for name in sorted(n for n in R if n.startswith("--")):
    if name.startswith(("--lightmode-", "--darkmode-")):
        continue  # emitted into the theme sets below
    kind = RLK = RL[name].get("kind")
    ty = KIND.get(kind, "other")
    if name.startswith("--fontWeight-"):
        v = R[name]
        if not (isinstance(v, (int, float)) or str(v).isdigit()):
            continue  # 'normal' is not a numeric weight
        ty = "fontWeight"
    leaf = var(name, ty)
    emit(SPEC["core"], name, leaf)

# ------------------------------------------------------------- theme sets

LM = re.compile(r"^--lightmode-")
DM = re.compile(r"^--darkmode-")
for name in sorted(n for n in R if LM.match(n)):
    key = LM.sub("", name)
    emit(SPEC["light"], "--" + key, var(name, "color"))
for name in sorted(n for n in R if DM.match(n)):
    key = DM.sub("", name)
    emit(SPEC["dark"], "--" + key, var(name, "color",
        note="declared in the shipped stylesheet; not bound on the captured marketing routes"))

# the standard role names the style guide looks for, straight on the
# --lightmode-* vars (and the matching --darkmode-* var on the dark set)
ROLES = [
    ("page", "bg", "The page field."),
    ("surface", "bg-med", "The grey panel surface."),
    ("surface-strong", "bg-strong", "The stronger panel."),
    ("surface-hover", "bg-med-hover", "The hover wash on panels."),
    ("text", "text", "Body ink."),
    ("text-strong", "text-strong", "The strong ink."),
    ("muted", "text-weak", "Secondary ink."),
    ("border", "border", "Default hairline."),
    ("border-strong", "border-strong", "Stronger hairline."),
    ("accent", "button-primary", "The action fill."),
    ("accent-hover", "button-primary-hover", "The lifted action fill."),
    ("on-accent", "button-text-primary", "Text on primary buttons."),
    ("danger", "error", "Error red."),
    ("success", "success", "Success green."),
    ("warning", "warning", "Warning amber."),
    ("link", "link-text", "Inline link ink."),
    ("link-hover", "link-hover", "Link hover ink."),
    ("focus-ring", "a11y-focus-primary", "The a11y focus ring colour."),
    ("field", "button-secondary", "The secondary fill (white fields/buttons)."),
    ("icon", "icon", "Icon ink."),
    ("disabled", "button-disabled", "Disabled control fill."),
    ("text-disabled", "link-disabled", "Disabled ink."),
]
for key, slot, desc in ROLES:
    # emit(), not direct assignment: keys like accent/border/icon/link are
    # already groups emitted from --lightmode-*-hover/-weak/-disabled, so the
    # convenience role lands as the group's `default` child, preserving the
    # captured state colours.
    emit(SPEC["light"], "--" + key, var("--lightmode-" + slot, "color", description=desc))
    if "--darkmode-" + slot in R:
        emit(SPEC["dark"], "--" + key, var("--darkmode-" + slot, "color", description=desc,
                                note="declared in the shipped stylesheet; not bound on the captured marketing routes"))

# ------------------------------------------------------------------ type

def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def tstyle(comp, state, desc):
    s = st(comp, state)
    fam = s["fontFamily"].split(",")[0].strip('"')
    return {
        "fontFamily": "{fontFamily.mono}" if "Consolas" in fam or "mono" in fam.lower() else "{fontFamily.ui}",
        "fontSize": s["fontSize"],
        "lineHeight": s["lineHeight"],
        "fontWeight": int(s["fontWeight"]),
        "letterSpacing": "0em" if s.get("letterSpacing") in (None, "normal") else s["letterSpacing"],
    }, f"computed type of {comp} {state} (raw/components-computed.json); {desc}"


font = SPEC["core"].setdefault("fontFamily", {})
# the site's declared stacks live in --fontFamily-mono/-print; the painted UI
# family is TWK Lausanne (a webfont, loaded via inline @font-face) falling
# back to Helvetica Neue/Helvetica, measured from the live DOM
font["ui"] = {"value": "\"TWK Lausanne\",\"Helvetica Neue\",Helvetica,sans-serif",
              "type": "fontFamily",
              "source": "computed fontFamily of the painted text (raw/components-computed.json); TWK Lausanne is a webfont loaded by the site's inline @font-face",
              "description": "The painted UI stack (webfont + fallbacks)."}
font["fallback"] = {"value": "Helvetica,Arial,sans-serif",
                    "type": "fontFamily",
                    "source": "computed fontFamily painted on elements outside the Lausanne stack (raw/components-computed.json)",
                    "description": "The secondary painted stack."}

typo = SPEC["core"].setdefault("typography", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "the h1 display line"),
    ("heading", "section-title", "default", "the h2 section heading"),
    ("body", "nav-link", "default", "the UI line"),
    ("button", "nav-cta", "default", "the primary CTA label"),
    ("small", "caps-label", "default", "the caps eyebrow label"),
]:
    try:
        v, src = tstyle(comp, state, desc)
        typo[key] = {"$value": v, "$type": "typography", "$extensions": {"source": src}}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "nav-cta", "default", "height", "The primary CTA height."),
    ("control.buttonSecondary", "nav-sales", "default", "height", "The secondary CTA height."),
    ("control.radius", "nav-cta", "default", "borderTopLeftRadius", "CTA corner radius."),
    ("nav.height", "nav-link", "default", "height", "Nav link height."),
    ("shell.header", "header", "default", "height", "The nav block at 1440."),
    ("control.field", "gate-field", "default", "height", "The gate field height."),
    ("control.iconButton", "m-menu-button", "default", "height", "The mobile menu button."),
    ("plan.height", "plan-card", "default", "height", "A pricing plan column."),
    ("footer.linkHeight", "footer-link", "default", "height", "Footer link rows."),
    ("menu.linkHeight", "m-nav-link", "default", "height", "Mobile menu rows."),
]:
    try:
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
