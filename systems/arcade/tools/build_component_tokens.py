#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

arcade.software is a Webflow build; its stylesheets declare on :root
(raw/css-vars.json, read by tools/capture/vars.mjs):

  --primary-500/-600/-700   the brand blue ramp (#4460ed -> #182fa5)
  --neutral-50/-200/-300, --gray700/--gray-800, --100/--500/--600
                           grey ramps (Tailwind values under Webflow names)
  --black/--white/--dim-grey/--new-text-dim-black/--arcade-dark/--opacity
                           the ink roles: pure black is the CTA ink, #111827
                           the dark-surface tone
  --gold/--green/--red + --light-* + --card-bg-* + --alice-blue/--light-blue
                           status hues and pastel card washes
  --_new-brand---50...--900/--white
                           the brand's own 10-step grey ramp and paper white
  --_new-brand---heading/--content/--header-size
                           the real font stacks ("Inter Display",Arial,... /
                           "Inter Variable",Arial,...) and the 72px header
  --marginanim, --progressive*
                           scatter-section and player-control layout metrics

The site paints one light theme (the .dark probe changes nothing), so the
dark set is not emitted. A leaf is {"var": "--name"} (resolved by
build_tokens.py) or {"value": ..., "source": "..."} for a measured value.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def val(name):
    if name not in R:
        raise KeyError(name + " not in resolved vars")
    return R[name]


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. arcade.software "
    "is a Webflow site declaring a Tailwind-shaped palette on :root plus "
    "scatter/player layout metrics; every colour name is kept flat under "
    "core (the --_new-brand---* ramp lands as core.brand.*), the site roles "
    "are the light set, and measured values that "
    "no variable declares (surfaces, focus ring, radii, control heights, "
    "the black ink of the CTAs) come from raw/components-computed.json. "
    "\"var\" leaves resolve through the live document; \"value\" leaves are "
    "measured."),
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


# --------------------------------------------------------------- core ramps

for name in sorted(n for n in R if n.startswith("--")):
    if re.match(r"--(marginanim|progressive)", name):
        emit(SPEC["core"], name, var(name, "dimension"))
        continue
    if name.startswith("--_new-brand---"):
        # Webflow prefixes project vars --_new-brand---<name>: a 10-step grey
        # ramp (50..900), --white, the real font stacks and the header size.
        # Map them under core.brand.* by their resolved kind.
        suffix = name[len("--_new-brand---"):]
        key = re.sub(r"-(\w)", lambda m: m.group(1).upper(), suffix)
        kind = RL[name].get("kind")
        ty = {"color": "color", "dimension": "dimension", "fontFamily": "fontFamily",
              "duration": "duration", "shadow": "shadow"}.get(kind, "other")
        SPEC["core"].setdefault("brand", {})[key] = var(name, ty)
        continue
    leaf = var(name)
    if name == "--opacity":  # a colour var despite the name
        leaf = var(name, "color")
    emit(SPEC["core"], name, leaf)

# ------------------------------------------------------------- light roles

LIGHT = [
    # no body component was measured: the page field is the declared --white
    ("page", var("--white", description="The page field: pure white.")),
    ("surface", {"read": [('plan-card-pro', 'default'), ('field-text', 'default')], "prop": "backgroundColor", "type": "color",
                 "source": "computed backgroundColor of plan-card-pro/field-text (raw/components-computed.json)",
                 "description": "The card and input fill (plan cards, .ds-input fields, ask-ai chips)."}),
    ("text", var("--black", description="The primary ink: pure black headings, black CTA fills.")),
    ("muted", {"read": [('nav-link', 'default')], "prop": "color", "type": "color",
               "source": "computed color of nav-link (raw/components-computed.json)",
               "description": "The secondary ink: nav links at 70% black; deeper mute is --500 #6b7280, footer links #717171."}),
    ("accent", var("--primary-600", description="The brand blue: url-to-demo button, links inside the demo pages; main CTAs are black.")),
    ("border", var("--neutral-200", description="The hairline: plan-card edges, spotlight arrows, radios.")),
    ("ink", var("--black", description="Primary button fill (Sign up, Get started, submits).")),
    ("on-ink", var("--white", description="Text on the black CTAs.")),
    ("surface-hover", {"read": [('nav-link', 'hover'), ('nav-login', 'hover')], "prop": "backgroundColor", "type": "color",
                       "source": "computed backgroundColor of nav-link/nav-login on hover (raw/components-computed.json)",
                       "description": "Ghost hover wash on nav actions and links."}),
    ("ink-hover", {"read": [('nav-signup', 'hover'), ('plan-cta-pro', 'hover')], "prop": "backgroundColor", "type": "color",
                   "source": "computed backgroundColor of nav-signup/plan-cta-pro on hover (raw/components-computed.json)",
                   "description": "The black buttons lift to #404040 on hover — never a colour change."}),
    ("focus-ring", {"read": [('nav-link', 'focus-visible'), ('nav-signup', 'focus-visible'), ('cta-large', 'focus-visible')], "prop": "outlineColor", "type": "color",
                    "source": "computed outlineColor of nav-link/nav-signup/cta-large on focus-visible (raw/components-computed.json)",
                    "description": "Webflow's 1px #005fcc focus ring (offset 1px); the prompt send uses 2px black offset 2px."}),
    ("chip-text", {"read": [('suggestion-chip', 'default')], "prop": "color", "type": "color",
                   "source": "computed color of suggestion-chip (raw/components-computed.json)",
                   "description": "Suggestion-chip and secondary-label ink."}),
    ("footer-muted", {"read": [('footer-link', 'default')], "prop": "color", "type": "color",
                      "source": "computed color of footer-link (raw/components-computed.json)",
                      "description": "Footer link ink."}),
]
# (assigned below, once the readers are defined)

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})


def st(comp, state):
    c = C[comp]
    # A component that was not found on the last run carries missing (no
    # states) or recaptureMissed (earlier states kept under their own
    # provenance): neither is a current reading, so refuse it as a source.
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


def reading(leaf):
    """A role read from the components its source names: every one must give the same value."""
    if "read" not in leaf:
        return leaf
    vals = {norm_color(st(comp, state)[leaf["prop"]]) for comp, state in leaf["read"]}
    if len(vals) != 1:
        raise ValueError(f"{leaf['source']}: readings differ: {sorted(vals)}")
    return {"value": vals.pop(), "type": leaf["type"], "source": leaf["source"], "description": leaf["description"]}


for key, leaf in LIGHT:
    SPEC["light"][key] = reading(leaf)

for comp, state, key, prop, desc in [
    ("cta-secondary", "default", "chip-border", "borderTopColor", "The outlined CTA / suggestion-chip hairline (#e7e7e7 vs rgba(0,0,0,0.2))."),
    ("field-text", "default", "input-fill", "backgroundColor", "The .ds-input fill."),
    ("plan-card-pro", "default", "card-fill", "backgroundColor", "The plan card fill."),
    ("nav-link", "hover", "hover-wash", "backgroundColor", "The ghost hover wash on nav actions."),
    ("nav-signup", "hover", "ink-hover", "backgroundColor", "The black CTA on hover."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ type + shape
#
# Scales measured from components-computed.json (computed styles), families
# from the @font-face faces in raw/css-vars.json.

font = SPEC["core"].setdefault("font", {})
font["family"] = {
    "display": {"value": "{brand.heading}", "type": "fontFamily",
                "source": 'computed fontFamily of hero-title/plan-price: "Inter Display",Arial,sans-serif, declared by --_new-brand---heading; the 400-700 static faces in raw/css-vars.json',
                "description": "Display headings (56px hero, 36px plan price)."},
    "ui": {"value": "{brand.content}", "type": "fontFamily",
           "source": 'computed fontFamily on every control: "Inter Variable",Arial,sans-serif, declared by --_new-brand---content; the 100-900 variable face in raw/css-vars.json',
           "description": "All UI text, body, fields, buttons."},
    "mono": {"value": '"Geist Mono Variable", monospace', "type": "fontFamily",
             "source": "@font-face in raw/css-vars.json (100-900 variable); code and timestamps on the page",
             "description": "The mono face (changelog timestamps, code)."},
    "script": {"value": '"Balig Script", cursive', "type": "fontFamily",
               "source": "@font-face in raw/css-vars.json",
               "description": "The handwritten accent (marginalia on the page)."},
    "serif": {"value": "Ptserif, serif", "type": "fontFamily",
              "source": "@font-face in raw/css-vars.json",
              "description": "The editorial serif."},
}

def tstyle(key, comp, state, desc):
    s = st(comp, state)
    fam = s["fontFamily"].split(",")[0].strip('"')
    return {
        "fontFamily": "{" + ("font.family.display" if "Display" in fam else "font.family.ui") + "}",
        "fontSize": s["fontSize"],
        "lineHeight": s["lineHeight"],
        "fontWeight": int(s["fontWeight"]),
        # computed "normal" is no tracking; DTCG wants a px or rem dimension, so 0px, not 0em
        "letterSpacing": "0px" if s.get("letterSpacing") in (None, "normal") else s["letterSpacing"],
    }, f"computed type of {comp} {state} (raw/components-computed.json); {desc}"


typo = SPEC["core"].setdefault("typography", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "the 56px Inter Display hero line"),
    ("title", "pricing-title", "default", "the page h1/h2 scale"),
    ("price", "plan-price", "default", "the 36px plan numeral"),
    ("body", "hero-subtitle", "default", "the 16px body line"),
    ("ui", "nav-signup", "default", "the 14px/500 control label"),
    ("small", "suggestion-chip", "default", "the 12px/500 chip"),
    ("mobile-nav", "m-nav-link", "default", "the 24px mobile menu link"),
]:
    try:
        v, src = tstyle(key, comp, state, desc)
        typo[key] = {"$value": v, "$type": "typography", "$extensions": {"source": src}}
    except KeyError:
        pass

rad = SPEC["core"].setdefault("radius", {})
for key, comp, prop, desc in [
    ("control", "nav-signup", "borderTopLeftRadius", "nav pills and .btn (12px)"),
    ("field", "field-text", "borderTopLeftRadius", ".ds-input fields (12px)"),
    ("card", "cta-large", "borderTopLeftRadius", "large CTAs, prompt box, FAQ rows (16px)"),
    ("panel", "plan-card-pro", "borderTopLeftRadius", "plan cards (24px)"),
    ("pill", "url-button", "borderTopLeftRadius", "the url-to-demo arrow pill (72px)"),
]:
    try:
        rad[key] = {"type": "dimension", "value": st(comp, "default")[prop],
                    "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        pass

dur = SPEC["core"].setdefault("duration", {})
for key, comp, desc in [
    ("ui", "header", "the standard 150ms UI ease (header bg, fields)"),
    ("pop", "prompt-send", "the 160ms press/ease on chips and the prompt send"),
    ("cta", "demo-signup", "the 350ms CTA sweep on the demo pages"),
]:
    try:
        dur[key] = {"type": "duration", "value": st(comp, "default")["transitionDuration"].split(",")[0].strip(),
                    "source": f"computed transitionDuration of {comp} default (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        pass

ease = SPEC["core"].setdefault("easing", {})
for key, comp, desc in [
    ("standard", "header", "the site's ease-in default"),
    ("out", "url-button", "the expo-out used on the demo buttons"),
]:
    try:
        # transitionTimingFunction can be a comma list of per-property easings;
        # take the first whole easing (a cubic-bezier holds commas of its own).
        tf = st(comp, "default")["transitionTimingFunction"]
        m = re.search(r"cubic-bezier\([^)]*\)|ease-in-out|ease-in|ease-out|ease|linear", tf)
        ease[key] = {"type": "cubicBezier", "value": m.group(0) if m else tf,
                     "source": f"computed transitionTimingFunction of {comp} default (raw/components-computed.json)",
                     "description": desc}
    except KeyError:
        pass

lay = SPEC["core"].setdefault("layout", {})
for key, comp, prop, desc in [
    ("header-height", "header", "height", "the fixed top bar"),
    ("content-gutter", "plan-card-pro", "width", "a plan card column (~437px of the 3-up grid)"),
]:
    try:
        lay[key] = {"type": "dimension", "value": st(comp, "default")[prop],
                    "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "nav-signup", "default", "height", "Nav pills are 32px."),
    ("control.heightLarge", "cta-large", "default", "height", "Large CTAs are 42px."),
    ("control.fieldHeight", "field-text", "default", "height", ".ds-input fields are 40px."),
    ("control.submitHeight", "form-submit", "default", "height", "The contact submit height."),
    ("control.iconButton", "prompt-send", "default", "height", "The 32px square prompt send/plus."),
    ("control.chip", "suggestion-chip", "default", "height", "Suggestion chips are 32px."),
    ("control.arrow", "spotlight-next", "default", "height", "Spotlight arrows are 40px."),
    ("card.height", "plan-card-pro", "default", "height", "A plan card at 1440."),
    ("prompt.height", "prompt-box", "default", "height", "The hero composer height."),
    ("prompt.width", "prompt-box", "default", "width", "The hero composer width."),
    ("faq.rowHeight", "faq-question", "default", "height", "The FAQ accordion row."),
    ("footer.linkHeight", "footer-link", "default", "height", "Footer link rows."),
    ("menu.linkHeight", "m-nav-link", "default", "height", "The 52px mobile menu rows."),
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
