#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

thenavia.com is a Webflow + Relume marketing site. tools/capture/vars.mjs
read the live stylesheets on 2026-11-21. The design layer is:

  --color-scheme-1--background / foreground   cream #faf4e6
  --color-scheme-1--text                      ink #36312a
  --color-scheme-1--border                    #cdc7b8
  --color-scheme-1--accent                    chartreuse #e8ff39
  --_primitives---colors--orange              #f88450
  --_primitives---colors--purple              #c99ddd
  --_typography---font-styles--heading        Lora
  --_typography---font-styles--body           Public Sans
  --_typography---font-styles--handwriting    Notemakersmark
  --_ui-styles---radius--small/medium/large   0.25rem / 0.5rem / 1rem

.color-scheme-2 through 10 are Relume slot swaps, not a dark theme. A
probe with html.dark resolves the same values. The dark set is not emitted.

A leaf is {"var": "--name"} or {"value": ..., "source": "..."}.
"""
import json
import pathlib
import re

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


def declared(name):
    """The stylesheet text of a custom property that vars.mjs did not resolve.

    The probe only stores names it could compute on an element. Font stacks and
    radius steps are declared on :root and used as font-family / border-radius
    keywords, so they never appear in resolved.light. Reading the declaration
    is the evidence; inventing a resolved colour is not.
    """
    for rule in V.get("app", []):
        props = rule.get("properties") or {}
        if name in props and rule.get("selector") == ":root":
            return props[name]
    raise KeyError(name)


def declared_leaf(name, ty, description):
    value = declared(name)
    if ty == "dimension" and isinstance(value, str) and value.startswith("."):
        value = "0" + value
    return {
        "type": ty,
        "value": value,
        "source": (
            f"declared on :root in the Webflow stylesheet as {name}; "
            "vars.mjs did not resolve it onto the probe element"
        ),
        "description": description,
    }


SPEC = {
    "_about": (
        "The token tree build_tokens.py turns into tokens.json. thenavia.com "
        "declares Relume --color-scheme-1 slots (cream page, ink text, "
        "chartreuse accent) and --_primitives---colors--* hues. The light set "
        "holds the roles the public site paints. Measured control sizes come "
        "from raw/components-computed.json. No dark theme is bound."
    ),
    "core": {},
    "light": {},
    "dark": {},
    "component": {},
}


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


VENDOR = re.compile(r"chat|bubble|flodesk|cky", re.I)
CLEAN = re.compile(r"<deleted\|[^>]*>")
SKIP_KIND = {"other"}


def clean(name):
    return CLEAN.sub("", name)


KEEP_PREFIX = (
    "--color-scheme-1--",
    "--_primitives---colors--",
    "--_primitives---opacity--",
    "--_typography---font-styles--",
    "--_ui-styles---radius--",
    "--_ui-styles---stroke--",
    "--base-color-neutral--",
)

for name in sorted(n for n in R if n.startswith("--")):
    if VENDOR.search(name):
        continue
    if not name.startswith(KEEP_PREFIX) and not name.startswith("--color-scheme-1"):
        # Keep scheme-1 aliases and primitives. Skip responsive type clamps
        # and one-off component vars that are not a scale.
        if not any(name.startswith(p) for p in KEEP_PREFIX):
            continue
    kind = RL[name].get("kind")
    if kind in SKIP_KIND or kind is None:
        continue
    ty = {
        "fontFamily": "fontFamily",
        "color": "color",
        "dimension": "dimension",
        "number": "number",
    }.get(kind, "other")
    if ty == "other":
        continue
    leaf = var(name, ty)
    if clean(name) != name:
        leaf["note"] = "the var name carries a deleted Relume variable tombstone"
    emit(SPEC["core"], clean(name), leaf)

# ------------------------------------------------------------- light roles

LIGHT = [
    ("page", var("--color-scheme-1--background", description="The page field: cream #faf4e6.")),
    ("surface", var("--color-scheme-1--foreground", description="The scheme-1 foreground, the same cream as the page.")),
    ("text", var("--color-scheme-1--text", description="Ink #36312a.")),
    ("muted", {"value": "#36312a", "type": "color", "source": "Not captured as a separate muted role. Body copy uses the same ink as headings; opacity is set per block and was not tokenised.", "description": "No dedicated muted colour was declared."}),
    ("accent", var("--color-scheme-1--accent", description="Chartreuse #e8ff39, the primary button fill on the marketing nav and hero.")),
    ("accent-pressed", {"value": "#36312a", "type": "color", "source": "computed backgroundColor of submit hover (raw/components-computed.json): the orange submit inverts to ink. The chartreuse button's hover overlay was not isolated as its own token.", "description": "Pressed/hover fill observed on the contact submit."}),
    ("on-accent", var("--color-scheme-1--text", description="Ink on the chartreuse button.")),
    ("border", var("--color-scheme-1--border", description="The declared border #cdc7b8.")),
    ("field", {"value": "#faf4e6", "type": "color", "source": "computed backgroundColor of text-field default (raw/components-computed.json)", "description": "Contact field fill, the page cream."}),
    ("field-focus", {"value": "#ffffff", "type": "color", "source": "computed backgroundColor of text-field focus-visible (raw/components-computed.json)", "description": "Contact field fill when focused."}),
    ("orange", {"value": "#f88450", "type": "color", "source": "css-var --_primitives---colors--orange, also computed backgroundColor of submit default", "description": "The contact submit and the contact-page nav button."}),
    ("focus", {"value": "#005fcc", "type": "color", "source": "Not captured as a designed ring. Keyboard focus on the measured controls did not paint a site-authored outline; Chromium's default auto outline is recorded as Not captured rather than sampled.", "description": "No designed focus colour was read."}),
]
# Fix muted and focus: they must not invent a value. Use a note token only if the builder accepts color.
# The instruction says unread values are Not captured. Do not emit a fake hex for muted or focus.
# Drop those two leaves and record them as notTokenised instead.
LIGHT = [item for item in LIGHT if item[0] not in ("muted", "focus")]
SPEC["light"]["$extensions"] = {
    "notTokenised": [
        "text.muted: Not captured. No secondary text colour is declared; body uses --color-scheme-1--text.",
        "text.disabled: Not captured. No disabled control was shown.",
        "border.focus: Not captured. Measured focus-visible states did not paint a site-authored ring.",
        "status.success, status.warning, status.danger, status.info: Not captured. The public site shows none.",
        "color.dark: Not captured. prefers-color-scheme: dark still paints the cream page. html.dark resolves the same custom properties.",
    ]
}
for key, leaf in LIGHT:
    SPEC["light"][key] = leaf

# ------------------------------------------------------------------ type


def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def text_of(comp, state):
    node = C[comp]["states"][state]
    return node.get("textStyle") or {}


def tstyle(comp, state, family_token, desc):
    s = st(comp, state)
    ts = text_of(comp, state)
    return {
        "fontFamily": family_token,
        "fontSize": ts.get("fontSize") or s["fontSize"],
        "lineHeight": ts.get("lineHeight") or s["lineHeight"],
        "fontWeight": int(float(ts.get("fontWeight") or s["fontWeight"])),
        "letterSpacing": "0em",
    }, f"computed type of {comp} {state} (raw/components-computed.json); {desc}"


font = SPEC["core"].setdefault("font", {}).setdefault("family", {})
font["heading"] = declared_leaf(
    "--_typography---font-styles--heading",
    "fontFamily",
    "Lora, the display face. Computed fontFamily on hero-title matches this stack.",
)
font["body"] = declared_leaf(
    "--_typography---font-styles--body",
    "fontFamily",
    "Public Sans, the UI face. Computed fontFamily on nav-link and submit matches this stack.",
)
font["handwriting"] = declared_leaf(
    "--_typography---font-styles--handwriting",
    "fontFamily",
    "Notemakersmark, declared for handwritten accents. No captured control computed this family.",
)

radius = SPEC["core"].setdefault("radius", {})
radius["small"] = declared_leaf("--_ui-styles---radius--small", "dimension", "0.25rem. Fields measure 4px, which is this step at 16px root.")
radius["medium"] = declared_leaf("--_ui-styles---radius--medium", "dimension", "0.5rem. Declared. No captured control measured 8px.")
radius["large"] = declared_leaf("--_ui-styles---radius--large", "dimension", "1rem. Declared. Primary buttons measure 64px, not this step.")

typo = SPEC["core"].setdefault("typography", {})
for key, comp, state, fam, desc in [
    ("display", "blog-title", "default", "{font.family.heading}", "the 80px blog h1"),
    ("heading", "contact-title", "default", "{font.family.heading}", "the 64px contact h1"),
    ("title", "hero-title", "default", "{font.family.heading}", "the 56px hero h1"),
    ("section", "section-title", "default", "{font.family.heading}", "the 48px section h2"),
    ("feature", "feature-item", "default", "{font.family.heading}", "the 22.4px feature label"),
    ("body", "text-field", "default", "{font.family.body}", "the 16px field"),
    ("label", "nav-link", "default", "{font.family.body}", "the 16px nav label"),
    ("button", "submit", "default", "{font.family.body}", "the 16px submit label"),
]:
    try:
        v, src = tstyle(comp, state, fam, desc)
        typo[key] = {"$value": v, "$type": "typography", "$extensions": {"source": src}}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
rows = [
    ("control.height", "submit", "default", "height", "The contact submit is 48px."),
    ("control.field", "text-field", "default", "height", "Contact fields are 44px."),
    ("control.area", "text-area", "default", "height", "The message field is 180px."),
    ("control.select", "select", "default", "height", "The topic select is 44px."),
    ("control.radius", "submit", "default", "borderTopLeftRadius", "The submit is a 64px pill."),
    ("field.radius", "text-field", "default", "borderTopLeftRadius", "Fields are 4px, the small radius step."),
    ("shell.header", "header", "default", "height", "The desktop nav is 72px."),
    ("shell.headerMobile", "m-header", "default", "height", "The phone nav is 61px."),
]
for key, cname, state, prop, desc in rows:
    try:
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {
            "type": "dimension",
            "value": st(cname, state)[prop],
            "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
            "description": desc,
        }
    except KeyError:
        pass

# Button fill lives on .button-base, not the anchor. Record the declared accent.
comp.setdefault("button", {})["fill"] = var(
    "--color-scheme-1--accent",
    description="The chartreuse fill painted on .button-base inside the nav and hero CTAs.",
)
comp["button"]["radius"] = {
    "type": "dimension",
    "value": "64px",
    "source": "computed borderRadius of .button-base inside the Get started anchor, read live on / on 2026-11-21 (the anchor itself is transparent)",
    "description": "Primary buttons are 64px pills.",
}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values() if not str(v).startswith("_") or True)


print({k: count(v) if isinstance(v, dict) else v for k, v in SPEC.items() if not k.startswith("_")})
