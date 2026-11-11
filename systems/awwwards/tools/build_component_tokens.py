#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

awwwards.com is a custom web-awards directory: its design tokens are
hand-named custom properties declared on :root (raw/css-vars.json's `app`
bin) — a neutral ramp (--bg-primary #f8f8f8, --bg-3rd #ededed, ink #222),
category accent triads (--color-connect/-inspire/-awards/-read/-learn/-jobs),
named font weights (--font-light..--font-black on Inter Tight), text sizes,
radii and control heights. Each declared colour keeps its own name under a
descriptive core.color.<family> bucket — no role is claimed there.

Roles are only asserted where a measurement backs them: every leaf in the
`light` set resolves through a css var whose resolved value equals the colour
measured on a real component (raw/components-computed.json). The pairings:

  text.primary       --color-primary        #222   all measured text
  text.inverse       --button-color         #fff   label on #222 Be Pro button
  surface.page       --bg-white             #fff   the white page
  surface.subtle     --bg-primary           #f8f8f8 filter bar / mobile header
  surface.mist       --bg-3rd               #ededed filter-option hover
  action.primary     --button-bg            #222   Be Pro pill; Submit outline fills #383838 on hover
  action.primaryText --button-color         #fff   Be Pro label
  action.accent      --color-orange         #FA5D29 brand accent (errors/links)
  action.award       (measured)             #e3c352 gold Vote button fill
  border.default     --border-gray          #ededed hairlines
  focus.ring         (measured)             #005fcc browser focus ring on nav/footer links

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints one
light theme; no dark mode exists, so `dark` is empty and the export holds
core and light only.

Not tokenised: --*-rgb channel triplets (the same colours as numbers),
--nf-* (the footer's own scheme), --check-toggle-* (a settings control never
reached signed-out), aspect ratios like --img-resizing-site ("16 / 12" is
not a DTCG type), --modal-alpha internals.
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
    "The token tree build_tokens.py turns into tokens.json. awwwards.com "
    "declares its palette as semantic custom properties on :root "
    "(css-vars.json's `app` bin); they land under descriptive core.color "
    "families. The light set holds only roles a measurement verified — each "
    "resolves through a var whose value equals a colour read off a live "
    "component. The site paints one light theme (a .dark probe resolves "
    "identically), so dark is empty. A leaf with \"var\" resolves through "
    "the live document; \"value\" leaves are measured on the running page."),
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


# ------------------------------------------------------------- core palette
# The declared colours, under descriptive families. Hex values on :root.
PALETTE = {
    "neutral": {
        "--color-primary": "ink",
        "--color-white": "paper",
        "--bg-primary": "wash",
        "--bg-secondary": "coal",
        "--bg-3rd": "mist",
        "--bg-4rd": "washAlt",
        "--border-gray": "hairline",
        "--color-featured": "featured",
        "--color-odd-rows": "oddRow",
        "--avatar-bg": "avatarBg",
        "--hf-bg": "headFootBg",
        "--sf-bg": "searchFieldBg",
        "--ch-bg": "chipBg",
        "--bg-input": "fieldBg",
        "--bg-input-hover": "fieldBgHover",
        "--border-input": "fieldBorder",
        "--color-input": "fieldText",
        "--button-bg": "buttonInk",
        "--button-color": "buttonLabel",
        "--button-border-color": "buttonBorder",
        "--alert-green": "ok",
        "--alert-yellow": "warn",
    },
    "accent": {
        "--color-orange": "orange",
        "--color-errors": "error",
        "--color-blue": "blue",
        "--color-connect": "connect",
        "--color-connect-2": "connect2",
        "--color-connect-3": "connect3",
        "--color-inspire": "inspire",
        "--color-inspire-2": "inspire2",
        "--color-inspire-3": "inspire3",
        "--color-awards": "awards",
        "--color-awards-2": "awards2",
        "--color-awards-3": "awards3",
        "--color-read": "read",
        "--color-read-2": "read2",
        "--color-read-3": "read3",
        "--color-learn": "learn",
        "--color-learn-2": "learn2",
        "--color-learn-3": "learn3",
        "--color-jobs": "jobs",
        "--color-jobs-2": "jobs2",
        "--color-jobs-3": "jobs3",
    },
}
for fam, names in PALETTE.items():
    for name, alias in sorted(names.items(), key=lambda kv: kv[1]):
        if name not in R:
            continue
        SPEC["core"].setdefault("color", {}).setdefault(fam, {})[alias] = \
            {"value": R[name], "type": "color",
             "source": f"css-var {name} ({R[name]})"}

# ------------------------------------------------------------------- fonts
# --font-1 is Inter Tight; --font-light..--font-black name the weight ramp
# and --text-size-* the four named sizes.
SPEC["core"]["font"] = {
    "family": {
        "primary": {"value": R.get("--font-1", "Inter Tight"), "type": "fontFamily",
                    "source": "--font-1 on :root; computed on every measured component",
                    "description": "Inter Tight everywhere — headings, UI and body."},
    },
    "weight": {},
    "size": {},
    "tracking": {},
}
for k, name in [("light", "--font-light"), ("regular", "--font-normal"),
                ("medium", "--font-medium"), ("semibold", "--font-bold"),
                ("bold", "--font-extrabold"), ("black", "--font-black")]:
    if name in R:
        SPEC["core"]["font"]["weight"][k] = {"value": R[name], "type": "fontWeight",
            "source": f"css-var {name}",
            "description": f"Inter Tight {k} (the declared {name})."}
for k, name, desc in [
    ("small", "--text-size-small", "The 11px micro size."),
    ("primary", "--text-size-primary", "The 14px UI/body size."),
    ("medium", "--text-size-medium", "The 18px medium size."),
    ("large", "--text-size-large", "The 22px large size."),
]:
    if name in R:
        SPEC["core"]["font"]["size"][k] = {"value": R[name], "type": "dimension",
            "source": f"css-var {name}", "description": desc}
for comp, key, desc in [
    ("grid-title", "xs", "13.3px filter-bar text."),
    ("nav-item", "sm", "14px header nav."),
    ("grid-card-link", "base", "15px card captions and footer links."),
    ("tag-chip", "md", "18px tag chips."),
    ("site-card", "lg", "~20.6px card titles."),
    ("submit-title", "xl", "~41.9px page headings."),
    ("site-title", "display", "~126.7px site-detail display title."),
]:
    try:
        st0 = C[comp]["states"]["default"]
        fs = (st0.get("textStyle") or {}).get("fontSize") or st0["style"]["fontSize"]
        SPEC["core"]["font"]["size"][key] = {
            "value": fs, "type": "dimension",
            "source": f"computed fontSize of {comp} (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------- radius
rad = SPEC["core"].setdefault("radius", {})
for k, name, desc in [
    ("small", "--rounded-small", "4px — grid cards."),
    ("normal", "--rounded-normal", "8px — buttons, pills, score box."),
    ("large", "--rounded-large", "14px — site cards."),
    ("full", "--button-rounded-full", "72px — tag chips and fully-round pills."),
]:
    if name in R:
        rad[k] = {"value": R[name], "type": "dimension",
                  "source": f"css-var {name}", "description": desc}

# ------------------------------------------------------------------- roles
# Only what a measurement verified (see module docstring for the pairings).
ROLES = {
    "text-primary": "--color-primary",
    "text-inverse": "--button-color",
    "surface-page": "--bg-white",
    "surface-subtle": "--bg-primary",
    "surface-mist": "--bg-3rd",
    "action-primary": "--button-bg",
    "action-primaryText": "--button-color",
    "accent-brand": "--color-orange",
    "accent-blue": "--color-blue",
    "accent-awards": "--color-awards",
    "border-default": "--border-gray",
    "border-field": "--border-input",
}
ROLE_DESC = {
    "text-primary": "rgb(34,34,34) ink on every measured component — resolved from {v}.",
    "text-inverse": "White labels on the ink buttons — resolved from {v}.",
    "surface-page": "The white page surface — resolved from {v}.",
    "surface-subtle": "#f8f8f8 filter bar and mobile header — resolved from {v}.",
    "surface-mist": "#ededed hover fill inside the filter dropdown — resolved from {v}.",
    "action-primary": "#222 Be Pro pill; the Submit Website outline fills #383838 on hover — resolved from {v}.",
    "action-primaryText": "White text on the ink actions — resolved from {v}.",
    "accent-brand": "#FA5D29 orange — brand accent, links and error state — resolved from {v}.",
    "accent-blue": "#49B3FC blue accent — resolved from {v}.",
    "accent-awards": "#502BD8 awards purple (the category triads live in core.color.accent) — resolved from {v}.",
    "border-default": "#ededed hairlines — resolved from {v}.",
    "border-field": "#ededed field borders — resolved from {v}.",
}
for role, name in sorted(ROLES.items()):
    if name in R:
        node, last = descend(SPEC["light"], role.split("-"))
        node[last] = {"value": R[name], "type": "color",
                      "source": f"css-var {name} resolved ({R[name]})",
                      "description": ROLE_DESC[role].format(v=name)}

# ------------------------------------------- measured-only colours (no var)
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
    ("vote-button", "default", "action-award", "backgroundColor", "The #e3c352 gold fill of the Vote button — no var declares it."),
    ("submit-cta", "hover", "action-hover", "backgroundColor", "The #383838 fill the outlined Submit Website button picks up on hover/pressed."),
    ("nav-item", "focus-visible", "focus-ring", "outlineColor", "The #005fcc browser focus ring on header and footer links (outline auto 1px)."),
]:
    try:
        raw_v = st(comp, state).get(prop, "")
        m_col = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", raw_v)
        v = norm_color(m_col.group(0) if m_col else raw_v)
        if v and v != "transparent" and v != "none":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ layout/motion
lay = SPEC["core"].setdefault("layout", {})
for name, key, desc in [
    ("--innerWidth", "page-width", "The 1816px max content width."),
    ("--gutter", "gutter", "The 20px page gutter."),
    ("--pad-inner", "pad-inner", "The 40px inner padding."),
    ("--header-height", "header-var", "The declared 71px header height (the measured bar is 54px — see component.header)."),
    ("--nf-height", "navFooter-height", "The 54px bar height the header actually paints."),
    ("--sf-height", "filter-height", "The 42px filter/search field height."),
    ("--height-input", "field-height", "The 48px input height."),
    ("--button-height", "button-height", "The declared 48px button height."),
    ("--button-pad", "button-pad", "The 24px horizontal button padding."),
    ("--border-thin", "hairline", "The 0.5px hairline width."),
    ("--pad-input", "field-pad", "The 16px field padding."),
]:
    if name in R:
        v = R[name].strip()
        if v and v != "''":
            lay[key] = {"value": v, "type": "dimension",
                        "source": f"css-var {name}", "description": desc}
mot = SPEC["core"].setdefault("motion", {})
for name, key in [("--duration-short", "short"), ("--duration-default", "default"), ("--duration-long", "long")]:
    if name in R:
        mot[key] = {"value": R[name].strip(), "type": "duration",
                    "source": f"css-var {name}",
                    "description": f"The declared {key} duration."}
# Transition timings are read off components instead (sheetsFor in
# raw/components-computed.json lists the declared transitions).

# ------------------------------------------------------------------ component
comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "vote-button", "default", "height", "The Vote CTA is 60px; declared --button-height is 48px."),
    ("control.filterHeight", "filter-item", "default", "height", "Filter tabs are 42px (= --sf-height)."),
    ("control.pillHeight", "tag-chip", "default", "height", "Tag chips are 48px."),
    ("header.height", "header", "default", "height", "The desktop header bar is 54px."),
    ("header.heightMobile", "m-header", "default", "height", "The mobile header is 54px."),
    ("card.width", "site-card", "default", "width", "Home site cards are ~658px at 1440."),
    ("card.gridWidth", "grid-card", "default", "width", "Winners-grid cards are 432px."),
    ("card.mobileWidth", "m-site-card", "default", "width", "Mobile cards are ~358px."),
    ("score.width", "score-box", "default", "width", "The jury score box is ~69px wide."),
    ("dropdown.width", "filter-dropdown", "default", "width", "The filter dropdown is 280px."),
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
