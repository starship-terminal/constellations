#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

artboard.studio is a Webflow marketing site built on the Relume component
library; its stylesheet declares ~95 :root vars (raw/css-vars.json, read by
tools/capture/vars.mjs):

  --color-scheme-1--text/background/foreground/border/accent
                              the Relume slot vars: near-black olive ink
                              #0d1400 on white, #eee foreground washes
  --color-scheme-2..10--*     nine more schemes swapping the same slots
                              (each section can pick its scheme class)
  --base-color-neutral--*     black/white/neutral-lightest primitives
  --background-color--*, --border-color--*, --text-color--*
                              deleted-Relume aliases still referenced
  --mg-*                      the editor's own palette: mg-gree #aaff00
                              (the ARKET-bright brand green), mg-darkest,
                              hover states, white-alpha washes
  --font-sans-serif/-serif/-monospace
                              the three generic fallback stacks
  misc palette hexes          --4c657e, --c5d4e8, --ecf1f7, --dark-text

The Brevo chat widget's --chat-*/--agent-*/--client-* vars are vendor
binning, not the site's palette. The site paints one light theme (the
.color-scheme-* classes are section washes, not themes), so the dark set
is not emitted. A leaf is {"var": "--name"} (resolved by build_tokens.py)
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
    "The token tree build_tokens.py turns into tokens.json. artboard.studio "
    "is a Webflow + Relume marketing site: the --color-scheme-1..10 slot "
    "vars (text/background/foreground/border/accent, the ink #0d1400), the "
    "--mg-* editor palette (mg-gree #aaff00 brand green), the generic font "
    "stacks and a handful of palette hexes. The light set holds the site's "
    "roles; measured values that no variable declares (radii, control "
    "heights) come from raw/components-computed.json. \"var\" leaves resolve "
    "through the live document; \"value\" leaves are measured."),
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


VENDOR = re.compile(r"chat|bubble|agent|client")
CLEAN = re.compile(r"<deleted\|[^>]*>")


def clean(name):
    # Relume keeps deleted-variable provenance inside the var name
    # itself: --foo--bar<deleted|relume-variable-baz>. The readable token
    # path drops the tombstone; the original name stays in $extensions.var.
    return CLEAN.sub("", name)


for name in sorted(n for n in R if n.startswith("--")):
    if VENDOR.search(name):
        continue
    kind = RL[name].get("kind")
    ty = "fontFamily" if kind == "fontFamily" else ("color" if kind == "color" else "other")
    leaf = var(name, ty)
    if clean(name) != name:
        leaf["note"] = "the var name carries a deleted Relume variable tombstone"
    emit(SPEC["core"], clean(name), leaf)

# ------------------------------------------------------------- light roles

def _norm(v):
    """rgb()/rgba() -> #hex, or rgba(r, g, b, a) when translucent."""
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", (v or "").strip())
    if not m:
        return (v or "").strip().lower()
    r, g, b, a = m.groups()
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
    return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"


def _rd(reads, prop):
    """The computed value every (component, state) named here reads; refuse a missing or stale
    component and readings that disagree, instead of typing the value in."""
    vals = set()
    for comp, state in reads:
        c = C[comp]
        if c.get("missing") or c.get("recaptureMissed"):
            raise KeyError(comp)
        vals.add(_norm(c["states"][state]["style"][prop]))
    if len(vals) != 1:
        raise ValueError(f"{reads} {prop}: readings differ: {sorted(vals)}")
    return vals.pop()


LIGHT = [
    ("page", var("--color-scheme-1--background", description="The page field: pure white (Relume scheme-1 background).")),
    ("surface", var("--color-scheme-1--foreground", description="The section wash (#eeeeee) the scheme classes swap in.")),
    ("field", {"value": _rd([("search-field", "default")], "backgroundColor"), "type": "color", "source": "computed backgroundColor of search-field (the library search field, raw/components-computed.json)", "description": "The search field fill."}),
    ("text", var("--color-scheme-1--text", description="The ink #0d1400, a near-black olive.")),
    ("muted", var("--mg-border", description="Secondary ink #444444, the site's own dark grey.")),
    ("link-hover", {"value": _rd([("nav-link", "hover"), ("footer-link", "hover")], "color"), "type": "color", "source": "computed color of nav-link/footer-link hover (raw/components-computed.json)", "description": "Text links fade to #aaa on hover."}),
    ("accent", var("--color-scheme-1--accent", description="The accent slot — same near-black #0d1400 on this site.")),
    ("ink", var("--color-scheme-1--text", description="Button fills: near-black #0d1400.")),
    ("ink-hover", {"value": _rd([("plugin-cta", "hover"), ("contact-cta", "hover"), ("filter-chip", "hover")], "backgroundColor"), "type": "color", "source": "computed backgroundColor of plugin-cta/contact-cta/filter-chip hover (raw/components-computed.json)", "description": "Black buttons lift to #222 on hover."}),
    ("on-ink", var("--color-scheme-1--background", description="Text on the black buttons.")),
    ("border", var("--color-scheme-1--border", description="Control borders, near-black.")),
    ("hover-fill", {"value": _rd([("lib-card", "hover")], "backgroundColor"), "type": "color", "source": "computed backgroundColor of lib-card hover (raw/components-computed.json)", "description": "The warm grey row/card hover fill."}),
    ("brand", var("--mg-gree", description="The ARKET-bright brand green #aaff00 (the editor's accent, shown on the site in the logo and highlights).")),
    ("brand-hover", var("--mg-green-hover", description="The green's hover tint #cfff6f.")),
    ("brand-dark", var("--mg-darkest", description="The dark green-black panel #2c2c2c.")),
    ("focus-ring", {"value": _rd([("m-menu-button", "focus-visible")], "outlineColor"), "type": "color",
                    "source": "computed outlineColor of m-menu-button focus-visible (raw/components-computed.json); most controls show the browser's default #005fcc, this indigo ring is the site's own Webflow focus style",
                    "description": "The site-styled 2px #4d65ff focus ring."}),
]
for key, leaf in LIGHT:
    SPEC["light"][key] = leaf

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
        "fontFamily": "{font.family.heading}" if "Vend" in fam else "{font.family.ui}",
        "fontSize": s["fontSize"],
        "lineHeight": s["lineHeight"],
        "fontWeight": int(s["fontWeight"]),
        # computed "normal" is no tracking; DTCG wants a px or rem dimension, so 0px, not 0em
        "letterSpacing": "0px" if s.get("letterSpacing") in (None, "normal") else s["letterSpacing"],
    }, f"computed type of {comp} {state} (raw/components-computed.json); {desc}"


font = SPEC["core"].setdefault("font", {}).setdefault("family", {})
font["heading"] = {"value": "\"Vend Sans\", sans-serif", "type": "fontFamily",
                   "source": "computed fontFamily of h1/h2 headings (raw/components-computed.json); the Google-fonts Vend Sans face (300-700)",
                   "description": "The display face on headings."}
font["ui"] = var("--font-sans-serif", "fontFamily", description="The generic sans stack the body and controls inherit.")
font["mono"] = var("--font-monospace", "fontFamily")

typo = SPEC["core"].setdefault("typography", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "the 60.8px h1"),
    ("title", "lib-title", "default", "the 56px library h1"),
    ("heading", "section-title", "default", "the 19.2px section h2"),
    ("body", "nav-link", "default", "the 16px UI line"),
    ("button", "tab", "default", "the 16px control label"),
]:
    try:
        v, src = tstyle(comp, state, desc)
        typo[key] = {"$value": v, "$type": "typography", "$extensions": {"source": src}}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "nav-link", "default", "height", "Nav links and CTAs are 42px."),
    ("control.tab", "tab", "default", "height", "Category tabs are 50px."),
    ("control.chip", "filter-chip", "default", "height", "Library filter chips are 50px."),
    ("control.field", "search-field", "default", "height", "The library search field is ~65px."),
    ("control.iconButton", "m-menu-button", "default", "height", "Icon buttons are 48px."),
    ("control.radius", "nav-link", "default", "borderTopLeftRadius", "Controls are 8px-radius."),
    ("card.radius", "filter-chip", "default", "borderTopLeftRadius", "Cards/chips are 12px-radius."),
    ("card.size", "mockup-card", "default", "width", "Mockup tiles are ~199px squares."),
    ("shell.header", "header", "default", "height", "The nav block at 1440."),
    ("footer.linkHeight", "footer-link", "default", "height", "Footer link rows."),
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
