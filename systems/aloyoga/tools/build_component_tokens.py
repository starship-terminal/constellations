#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

aloyoga.com is Shopify + Builder.io; its theme.css declares on :root
(raw/css-vars.json, read by tools/capture/vars.mjs):

  --alto/-charcoal/-chicago/-dawn/-mercury/-mine/-smoke/-sand/-white
                   the shop's named greys and neutrals -> core.color.neutral
  --accent-*, --alert-*, --highlight-*, --success-*, --primary
                   the semantic roles -> light set
  --primary-font   "proxima-nova", Helvetica, sans-serif -> core.font
  --spacing-*      the 0…9xl spacing scale -> core.spacing
  --shadow-level-1…4 -> core.shadow
  --color-*/--border-stroke-opacity
                   these names are declared ONLY by the embedded Sierra chat
                   widget's stylesheet (sierra.chat, the vendor bin) — a
                   chat widget's design tokens, not Alo's. Recorded in
                   css-vars.json, never tokenised.
  --osano-*/--swiper-*/--spinner-*/--app-only-*/--sign-in-modal-*/--status-*
                   vendor and widget vars: recorded in css-vars.json, not
                   tokenised

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The shop paints one
light theme; the `dark` set is left empty so build_tokens.py emits core and
light only.

Only names declared by rules in css-vars.json's `app` bin are tokenised:
resolved.light mixes every loaded sheet, so without the bin check the Sierra
chat widget's :host/:root declarations would be exported as Alo's palette.
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
    "The token tree build_tokens.py turns into tokens.json. aloyoga.com styles "
    "itself with the --color-* design-system ramps and the shop's named "
    "neutrals on :root; semantic roles land in the light set (the only theme "
    "the shop paints). A leaf with \"var\" resolves through the live document "
    "(css-vars.json resolved light); \"value\" leaves are measured on the "
    "running page."),
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


# Names the shop's own stylesheets declare (the `app` bin in css-vars.json);
# everything else resolved — Sierra's chat widget, Osano, Swiper — is vendor.
APP = {n for r in V["app"] for n in r["properties"]}

NEUTRAL = {"--alto", "--charcoal", "--chicago", "--dawn", "--mercury", "--mine", "--smoke", "--sand", "--white"}
ROLE = {"--accent-light", "--accent-medium", "--accent-dark", "--alert-light", "--alert-medium", "--alert-dark",
        "--highlight-light", "--highlight-medium", "--highlight-dark", "--success-light", "--success-medium",
        "--success-dark", "--primary"}
SKIP = re.compile(r"^--(osano|swiper|spinner|app-only|sign-in-modal|status-dot|s-|lightningcss|tw)-")

# --------------------------------------------------------------- core ramps

# --color-* names are gated on the app bin: today every one of them is
# Sierra's widget palette, so the loop emits nothing until Alo's own sheets
# declare a ramp.
for name in sorted(n for n in R if n.startswith("--color-") and n in APP):
    emit(SPEC["core"], name, var(name))
for name in sorted(NEUTRAL):
    if name in R:
        emit(SPEC["core"].setdefault("color", {}), "--neutral-" + name[2:], var(name))

# -------------------------------------------------------------------- roles

for name in sorted(ROLE):
    if name in R:
        emit(SPEC["light"], name, var(name))

# -------------------------------------------------------------------- fonts

if "--primary-font" in R:
    SPEC["core"].setdefault("font", {}).setdefault("family", {})["primary"] = var("--primary-font", "fontFamily")

# ------------------------------------------------------------------- scales

for name in sorted(n for n in R if n.startswith("--spacing-")):
    SPEC["core"].setdefault("spacing", {})[name[len("--spacing-"):]] = var(name, "dimension")
def parse_shadow(v):
    """'rgba(0,0,0,.06) 0px 2px 6px 0px, ...' -> DTCG shadow array."""
    import re as _re
    out = []
    depth = 0
    parts, cur = [], ""
    for ch in str(v):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    for p in parts:
        m = _re.match(r"^\s*(rgba?\([^)]*\)|okl[ca]h?\([^)]*\)|#[0-9a-fA-F]{3,8}|[a-zA-Z]+)\s+(-?\S+)\s+(-?\S+)\s+(-?\S+)\s*(-?\S+)?\s*$", p)
        if m:
            out.append({"offsetX": m.group(2), "offsetY": m.group(3), "blur": m.group(4),
                        "spread": m.group(5) or "0px", "color": m.group(1)})
    return out


for name in sorted(n for n in R if n.startswith("--shadow-level-")):
    arr = parse_shadow(R[name])
    SPEC["core"].setdefault("shadow", {}).setdefault("level", {})[name[len("--shadow-level-"):]] = \
        {"value": arr if arr else str(R[name]), "type": "shadow",
         "source": f"css-var {name}"}
if "--border-stroke-opacity" in R and "--border-stroke-opacity" in APP:
    SPEC["core"].setdefault("border", {}).setdefault("opacity", {})["stroke"] = \
        {"value": val("--border-stroke-opacity"), "type": "number", "source": "css-var --border-stroke-opacity"}

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})


def st(comp, state):
    return C[comp]["states"][state]["style"]


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
    ("nav-item", "focus-visible", "focus-outline", "outlineColor", "The keyboard-focus ring on nav items."),
    ("hero-button", "hover", "button-hover", "backgroundColor", "The hero button's hover fill."),
    ("add-to-bag", "default", "action-bg", "backgroundColor", "The Add to bag fill."),
    ("add-to-bag", "hover", "action-bg-hover", "backgroundColor", "Add to bag on hover."),
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
    ("control.height", "add-to-bag", "default", "height", "The buy button is 52px."),
    ("control.heightSmall", "size-button", "default", "height", "Size chips are 40px."),
    ("control.fieldHeight", "newsletter-input", "default", "height", "The footer newsletter field height. The login form was not measured."),
    ("control.radius", "hero-button", "default", "borderTopLeftRadius", "The hero/buy button corner."),
    ("swatch.size", "pdp-swatch", "default", "width", "The PDP colour tile is square."),
    ("header.height", "header", "default", "height", "The desktop header height at 1440px."),
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
