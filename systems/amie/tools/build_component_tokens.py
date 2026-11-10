#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

amie.so is a Tailwind + Radix build; its stylesheets declare on :root
(raw/css-vars.json, read by tools/capture/vars.mjs):

  --color-*        full Tailwind-style ramps stored as RGB triplets
                   ("253,43,56") for <alpha-value> utilities, plus the hex
                   --color-amie-pink and the --color-accent/-background/-black
                   singles -> core.color; the triplets are converted to hex
                   by build_tokens.py
  --foreground     ink -> light.foreground
  --shadow-wysiwyg-inner/-outer -> core.shadow.wysiwyg
  --grid-*/--nav-width/--inbox-width/--sidebar-*-width/-height
                   the product's own layout metrics (declared for the app the
                   marketing site ships in the bundle) -> core.layout
  .dark            only --foreground and the two wysiwyg shadows re-declare;
                   the site paints light on every captured route, so the dark
                   set is recorded but not emitted

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value.
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
    "The token tree build_tokens.py turns into tokens.json. amie.so styles "
    "itself with Tailwind ramp vars stored as RGB triplets (converted to hex "
    "here), the --color-accent/-background/-amie-pink singles, the app's own "
    "layout metrics (--nav-width, --inbox-width, --grid-*, --sidebar-*), and "
    "a light theme only: .dark re-declares just --foreground and two wysiwyg "
    "shadow vars and is never applied on the captured routes. \"var\" leaves "
    "resolve through the live document; \"value\" leaves are measured."),
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

for name in sorted(n for n in R if n.startswith("--color-")):
    emit(SPEC["core"], name, var(name))

# ------------------------------------------------------------- light roles

if "--foreground" in R:
    emit(SPEC["light"], "--foreground", var("--foreground"))
if "--color-background" in R:
    emit(SPEC["light"], "--background", var("--color-background"))
if "--color-accent" in R:
    emit(SPEC["light"], "--accent", var("--color-accent"))
if "--color-amie-pink" in R:
    emit(SPEC["light"], "--amie-pink", var("--color-amie-pink"))
if "--color-black" in R:
    emit(SPEC["light"], "--ink", var("--color-black"))

# -------------------------------------------------------------------- misc

for name in sorted(n for n in R if n.startswith("--shadow-")):
    emit(SPEC["core"], name, {"value": str(R[name]), "type": "color", "source": f"css-var {name}"})
for name in sorted(n for n in R if re.match(r"--(grid|nav|inbox|sidebar)-", n)):
    emit(SPEC["core"], name, var(name, "dimension"))

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


for comp, state, key, prop, desc in [
    ("nav-cta", "focus-visible", "focus-outline", "outlineColor", "The keyboard-focus ring on the nav CTA."),
    ("cta-primary", "hover", "cta-hover", "backgroundColor", "The blue Get started on hover."),
    ("cta-secondary", "default", "ghost-bg", "backgroundColor", "The Download ghost's fill."),
    ("plan-cta", "default", "plan-cta-bg", "backgroundColor", "The black trial button fill."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "cta-primary", "default", "height", "Hero CTAs are ~50px rounded-xl."),
    ("control.heightSmall", "nav-link", "default", "height", "Nav controls are 32px."),
    ("control.fieldHeight", "contact-field", "default", "height", "The contact field height."),
    ("control.heightPlan", "plan-cta", "default", "height", "The black trial CTA height."),
    ("control.radius", "cta-primary", "default", "borderTopLeftRadius", "The hero CTA corner."),
    ("control.radiusSmall", "nav-cta", "default", "borderTopLeftRadius", "The nav CTA corner."),
    ("header.height", "header", "default", "height", "The floating header height at 1440px."),
    ("faq.height", "faq-question", "default", "height", "The FAQ accordion row height."),
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
