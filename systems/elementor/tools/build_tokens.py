#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from elementor.com on the capture date in raw/css-vars.json:
  raw/css-vars.json          every custom property the site's stylesheets declare, by selector
                             and enclosing condition, plus `resolved`: each name as the browser
                             resolves it on a plain root (light) and inside <body
                             class="dark-mode"> (the .dark-mode island re-binding)
  raw/component-tokens.json  semantic roles and component measures read on the real elements,
                             each with its measurement ("source")

Elementor's public token layer is small and named, not cds-style roles: a :root
palette (--Kernel-Black, --Blank-Canvas-White, --Grey-200..800, --Neon-Loop,
--Pink-200, --Pixel-Blush, --Syntax-Glow, --Startup-Lime, --Seedling-Spark,
--Vision-Violet, --Founder-Forest, --Codeberry, --Deep-Burgundy, --Transparent,
--Roobert), the kit globals on .elementor-kit-35 (--e-global-color-*,
--e-global-typography-*), the --s8..--s160 spacing primitives and the
--sm*/--md*/--lg* semantic steps (re-mapped at the 1024px and 767px
breakpoints). `.dark-mode *` re-binds three names for the dark islands (hero,
dark sections, footer).

Layout: `core` holds the declared primitives; `light` holds the semantic roles
measured on the real elements; `dark` holds the island scope (measured/declared
re-bindings). Every token carries $extensions.source. Deterministic: same
inputs, same bytes.
"""
import json
import re
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
CT = json.loads((RAW / "component-tokens.json").read_text())
RES = V["resolved"]
RULES = [r for r in V["theme"] + V["app"] + V["darkscope"] if r.get("selector")]


def decl_src(name):
    """The selector(s) that declare a name, for the source note."""
    sels = [r["selector"] + ((" " + " ".join(r["context"])) if r["context"] else "") for r in RULES if name in r["properties"]]
    return ("; declared " + "; ".join(sels[:3])) if sels else ""


def tok(value, ty, source, **ext):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    t["$extensions"].update(ext)
    return t


def put(tree, path, t):
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    node[path[-1]] = t


def rsrc(name, where="light"):
    return "css-var %s%s" % (name, decl_src(name))


def resv(name, where="light"):
    return RES[where][name]["value"]


# ---------------------------------------------------------------- palette

NAMED = [
    ("kernel-black", "--Kernel-Black", "#000000: the text and primary-action fill; rebounds to #fff inside .dark-mode islands"),
    ("blank-canvas-white", "--Blank-Canvas-White", "#ffffff: the page field and text-on-dark; rebounds to #000 inside .dark-mode islands"),
    ("transparent", "--Transparent", "fully transparent"),
]
for n in (200, 300, 400, 500, 600, 700, 800):
    NAMED.append((f"grey-{n}", f"--Grey-{n}", f"the neutral ramp step; Grey-800 #212121 is the strong text, Grey-500 #d1d1d1 the field border, Grey-200 #f6f6f6 the subtle surface"))
NAMED += [
    ("neon-loop", "--Neon-Loop", "#ed01ee: the magenta hover state on every dark button"),
    ("pink-200", "--Pink-200", "#ff7be5: accent pink (badges, highlights)"),
    ("pink-200-hover", "--Pink-200-hover", "#ffa8ee: its hover step"),
    ("pixel-blush", "--Pixel-Blush", "#f2adf3: blush surface"),
    ("syntax-glow", "--Syntax-Glow", "#fae4fa: the pale-magenta hover tint on nav triggers and menu links"),
    ("startup-lime", "--Startup-Lime", "#d5ff45: lime highlight (the stat/label chips)"),
    ("seedling-spark", "--Seedling-Spark", "#82f545: its deeper step"),
    ("vision-violet", "--Vision-Violet", "#9800ff: violet accent"),
    ("founder-forest", "--Founder-Forest", "#00452e: deep green accent"),
    ("codeberry", "--Codeberry", "#620856: deep purple (menu feature tile gradient)"),
    ("deep-burgundy", "--Deep-Burgundy", "#290027: darkest purple (the feature tile gradient edge)"),
    ("blush-bordeaux", "--wp--preset--gradient--blush-bordeaux", "named brand gradient (declared, angle/stops in raw/css-vars.json)"),
    ("electric-grass", "--wp--preset--gradient--electric-grass", "named brand gradient (declared)"),
    ("luminous-dusk", "--wp--preset--gradient--luminous-dusk", "named brand gradient (declared)"),
]

core = {}
palette = {}
pal_index = {}  # value -> token path
for key, name, desc in NAMED:
    r = RES["light"].get(name)
    if not r or r.get("kind") == "other" and not r.get("value"):
        # gradients resolve as 'other' with raw kept
        raw = (r or {}).get("raw", "")
        if raw:
            palette[key] = tok(raw if len(raw) < 300 else raw[:300] + "…", "other", rsrc(name))
            palette[key]["$description"] = desc
        continue
    palette[key] = tok(r["value"], r["kind"] if r["kind"] in ("color", "dimension") else "other", rsrc(name))
    palette[key]["$description"] = desc
    if r["kind"] == "color":
        pal_index[r["value"].lower()] = "palette." + key
palette["$description"] = ("The :root named palette declared by the site's own sheets (post-35.css and the inline token block), "
                           "resolved by the browser. .dark-mode islands re-bind kernel-black, blank-canvas-white and grey-800.")
core["palette"] = palette

# The kit globals (.elementor-kit-35): the four named roles only; the hashed
# e-global-color-<hash> declarations stay in raw/css-vars.json.
gl = {}
for k, name in (("primary", "--e-global-color-primary"), ("secondary", "--e-global-color-secondary"), ("text", "--e-global-color-text"), ("accent", "--e-global-color-accent")):
    rule = next((r for r in RULES if name in r["properties"]), None)
    v = rule["properties"][name] if rule else None
    gl[k] = tok(v, "color", "css-var %s (.elementor-kit-35)" % name)
gl["$description"] = "Elementor's kit globals on .elementor-kit-35 (the site kit's named colour roles). The hashed --e-global-color-* siblings are in raw/css-vars.json."
core["globalColor"] = gl

# ---------------------------------------------------------------- type

core["fontFamily"] = {
    "roobert": tok(resv("--Roobert"), "fontFamily", rsrc("--Roobert") + "; measured as the computed fontFamily on headings, buttons and form fields"),
    "roboto": tok("Roboto, sans-serif", "fontFamily", "declared: fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700 pulled by the page CSS"),
    "$description": "Roobert (self-hosted under wp-content/fonts) is the site face; Roboto comes from Google Fonts. Some unstyled wrappers compute to Times, the UA serif default — not a shipped token.",
}
tt = CT["component"]["type"]
core["typeScale"] = {
    "display": tok(tt["display"]["$value"], "dimension", tt["display"]["$extensions"]["source"], weight=tt["display"]["$extensions"].get("weight"), lineHeight=tt["display"]["$extensions"].get("lineHeight")),
    "section": tok(tt["section"]["$value"], "dimension", tt["section"]["$extensions"]["source"], weight=tt["section"]["$extensions"].get("weight")),
    "planPrice": tok(tt["planPrice"]["$value"], "dimension", tt["planPrice"]["$extensions"]["source"], weight=tt["planPrice"]["$extensions"].get("weight")),
    "body": tok(tt["body"]["$value"], "dimension", tt["body"]["$extensions"]["source"], lineHeight=tt["body"]["$extensions"].get("lineHeight")),
    "small": tok(tt["small"]["$value"], "dimension", tt["small"]["$extensions"]["source"]),
    "$description": "The measured type steps. The declared e-global-typography ladder (5.5rem/4.5rem/4rem/3.5rem/2.5rem/1.25rem/1.125rem/1rem/0.875rem, all Roobert) is in raw/css-vars.json.",
}

# ---------------------------------------------------------------- spacing

sp = {}
for name in sorted(RES["light"]):
    m = re.fullmatch(r"--s(\d+)", name)
    if m:
        sp[m.group(1)] = tok(resv(name), "dimension", rsrc(name) + "; spacing primitive")
sp["$description"] = "The --s8..--s160 spacing primitives (px steps), declared in the inline token block on :root."
core["spacePrimitive"] = sp

ssc = {}
for name in sorted(RES["light"]):
    m = re.fullmatch(r"--(sm|md|lg)(\d+)", name)
    if m:
        ssc[name[2:]] = tok(resv(name), "dimension", rsrc(name) + "; re-mapped smaller at the 1024px and 767px breakpoints (raw/css-vars.json)")
ssc["$description"] = "The sm/md/lg semantic spacing steps used by the dsm-* components (--sm100 12px .. --lg400 160px at desktop)."
core["spaceScale"] = ssc

# ---------------------------------------------------------------- radius, shadow, motion

rc = CT["component"]
core["radius"] = {
    "field": rc["field"]["radius"],
    "control": rc["buttonPrimary"]["radius"],
    "card": rc["card"]["radius"],
    "planCard": rc["planCard"]["radius"],
    "pill": rc["header"]["radius"],
    "$description": "Measured radii: 4px fields, 8px buttons and plan cards, 16px dsm cards, 24px the floating header pill.",
}
core["shadow"] = {
    "header": rc["header"]["shadow"],
    "$description": "The floating header's soft shadow; cards and buttons paint no shadow.",
}
core["motion"] = {
    "button": rc["motion"]["button"],
    "link": rc["motion"]["link"],
    "panel": rc["motion"]["panel"],
    "$description": "Computed transitions on the real components.",
}
core["component"] = {
    "headerHeight": rc["header"]["height"],
    "buttonHeight": rc["buttonPrimary"]["height"],
    "heroButtonHeight": rc["buttonHero"]["height"],
    "fieldHeight": rc["field"]["height"],
    "fieldBorder": rc["field"]["border"],
    "planCtaBorder": rc["planCta"]["border"],
    "checkboxSize": rc["checkbox"]["size"],
    "$description": "Component measures read on the live elements.",
}

# ---------------------------------------------------------------- light / dark semantic sets


def alias(v):
    return "{" + pal_index[v.lower()] + "}" if v.lower() in pal_index else v


def sem(node):
    """component-tokens entry -> token with alias where the value is a palette step."""
    t = dict(node)
    if t["$type"] == "color" and isinstance(t["$value"], str):
        t["$value"] = alias(t["$value"])
    return t


light = {}
for k, v in CT["light"].items():
    light[k] = sem(v)
light["$description"] = "Semantic roles measured on the live elements (each source names the component and page); aliased to the palette where the value matches."
dark = {}
for k, v in CT["dark"].items():
    if k == "$description":
        dark[k] = v
    else:
        dark[k] = sem(v)
dark["$description"] = "The .dark-mode island scope — the hero, dark sections and footer. `.dark-mode *` re-binds kernel-black->#fff, blank-canvas-white->#000, grey-800->grey-200; not a user toggle."

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The marketing surface paints light: white ground, Kernel-Black text and actions, Neon-Loop on hover, Syntax-Glow tints."},
        {"id": "dark", "name": "Dark (island)", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Not a user theme — the .dark-mode islands inside the page (photo hero, dark sections, footer) re-bind the same named vars."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

# ---------------------------------------------------------------- checks

def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


paths = {n for st_ in (core, light, dark) for n, _ in flat(st_)}
bad = []
for st_ in (core, light, dark):
    for n, t in flat(st_):
        v = t["$value"]
        if isinstance(v, str):
            for m in re.finditer(r"\{([^}]+)\}", v):
                tgt = m.group(1)
                if tgt not in paths:
                    bad.append((n, tgt))
assert not bad, f"aliases point at nothing: {bad}"

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
n = sum(1 for _ in flat(core)) + sum(1 for _ in flat(light)) + sum(1 for _ in flat(dark))
print("tokens.json:", n, "tokens")
