#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

www.hbomax.com ships a real design-token stylesheet
(/dotcom/generated/css/ds/hbomax/design-systems.*.css) that declares on
:root, .spacer-tokens, .border-tokens and .font-english-like-slate3
(raw/css-vars.json, read by tools/capture/vars.mjs):

  --color_<family>_<role>[_<state>]   379 semantic colours: action, card,
                                      captions, component, general, indicator,
                                      input, scrim, surface, tile and utility
                                      families — already role names, so the
                                      tree keeps them under dark.color.*
  --spacer-(space|size)-<...>         528 spacing dimensions
  --border-(corner|stroke)-<...>      448 radii and stroke widths
  --font_<role>_<size>_bp_NN_<prop>-slate3
                                      434 type tokens: font_size (px) and
                                      line_height (%) for each text role,
                                      each redeclared at seven breakpoints
                                      (-bp-01..07 = 440/600/800/1100/1400/
                                      1800px media steps) — bp-05 is the
                                      step painted at the 1440px probe width
  --x-scale-factor, --scrollbar-width, --col-width, --size
                                      app internals, recorded in css-vars.json
                                      but not tokenised

A leaf is {"var": "--name"} (resolved by build_tokens.py) or {"value": ...,
"source": "..."} for a measured value. The site paints one dark theme
(html data-theme="max"), so the colour roles sit in the `dark` set — the
bezi/spotify convention for a single painted dark surface — and the
dimension/type scales sit in `core`.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = {n: v.get("value", v.get("raw")) for n, v in V["resolved"]["dark"].items()}
C = (json.loads((RAW / "components-computed.json").read_text())["components"]
     if (RAW / "components-computed.json").exists() else {})
L = json.loads((RAW / "layout.json").read_text()) if (RAW / "layout.json").exists() else {}

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. www.hbomax.com's "
    "own token sheet declares the --color_* semantic roles (kept under "
    "dark.color.*) and the --spacer-*/--border-*/--font_* scales (kept under "
    "core.*, each breakpoint step as .bpNN — resolved at 1440px). \"var\" "
    "leaves resolve through the live document; \"value\" leaves are measured."),
    "core": {}, "dark": {}, "component": {}}


def descend(root, parts):
    # One name is a prefix of another (--color_component_toggle_indicator_icon
    # vs ..._icon_focus): a leaf hit on the way down is hoisted to `.self`.
    node = root
    for p in parts[:-1]:
        nxt = node.setdefault(p, {})
        if "var" in nxt or "value" in nxt:
            node[p] = {"self": nxt}
            nxt = node[p]
        node = nxt
    node[parts[-1]] = None
    return node, parts[-1]


# ---------------------------------------------------------------- colours
# --color_action_link_text_base -> dark.color.action.link.text.base
for name in sorted(n for n in R if n.startswith("--color_")):
    path = name[len("--color_"):].split("_")
    node, last = descend(SPEC["dark"].setdefault("color", {}), path)
    node[last] = {"var": name, "type": "color"}

# ------------------------------------------------------------- dimensions
# --spacer-space-horizontal-far-sm-bp-03 -> core.spacer.space.horizontal.far.sm.bp.03
# --border-corner-action-lg-bp-01        -> core.border.corner.action.lg.bp.01
# The -bp-NN suffix splits into its own group levels (bp.03): folding it into
# the size key ("sm.bp03") would leave a literal period inside a token name,
# which DTCG reserves as the path separator.
for name in sorted(n for n in R if n.startswith("--spacer-") or n.startswith("--border-")):
    fam = "spacer" if name.startswith("--spacer-") else "border"
    rest = name[len("--" + fam + "-"):]
    path = [fam] + rest.split("-")
    node, last = descend(SPEC["core"], path)
    node[last] = {"var": name, "type": "dimension"}

# ------------------------------------------------------------------- type
# --font_action_md_bp_01_font_size-slate3 -> core.font.action.md.bp01.fontSize
# --font_action_md_bp_01_line_height-slate3 -> core.font.action.md.bp01.lineHeight
for name in sorted(n for n in R if n.startswith("--font_")):
    m = re.fullmatch(r"--font_(.+?)_bp_(\d+)_(font_size|line_height)-slate3", name)
    if not m:
        raise SystemExit("unmapped --font name: " + name)
    role_size, bp, prop = m.groups()
    path = ["font"] + role_size.split("_") + ["bp" + bp, "fontSize" if prop == "font_size" else "lineHeight"]
    node, last = descend(SPEC["core"], path)
    if prop == "font_size":
        node[last] = {"var": name, "type": "dimension"}
    else:
        # the sheet declares line-height as a percent (135%/136%/156%): emit
        # the unitless ratio DTCG number tokens carry.
        raw = R[name].strip()
        pct = float(raw[:-1]) / 100 if raw.endswith("%") else float(raw)
        node[last] = {"value": round(pct, 4), "type": "number",
                      "source": f"css-var {name}: {raw} (dark)",
                      "description": "Line-height ratio the token sheet declares for this role at this breakpoint."}

# The brand face the site paints: the token sheet's @font-face is "Max Sans"
# (woff2, weights 300/400/600 — proprietary, not committed); the body computes
# the full stack.
fam = (L.get("home@1440", {}).get("body", {}) or {}).get("font") or ""
SPEC["core"].setdefault("font", {})["family"] = {
    "primary": {"value": fam or "Max Sans,Inter,sans-serif", "type": "fontFamily",
                "source": ("computed font-family of body at 1440px (raw/layout.json home@1440)" if fam
                           else "the sheet's @font-face \"Max Sans\" (raw/css-vars.json fonts) with the documented fallback stack"),
                "description": "Max Sans over the site's system fallback; the woff2 faces are proprietary and not committed."}}


# ------------------------------------------------------------- dark roles
#
# The --color_* sheet is already semantic, so the role map only records the
# page-level surfaces the chrome actually paints — body ground, the navbar,
# hero CTA, focus ring — as cross-checked anchors, aliased onto the matching
# colour token when the painted value equals one.
def stprop(comp, state, prop):
    """prop may be `styleProp` or `textStyle.prop`/`paint.N.prop`/`ancestors.N.prop`
    — a dotted path into the measured state."""
    d = C[comp]["states"][state]
    if "." not in prop:
        return d.get("style", {}).get(prop, "")
    node = d
    for part in prop.split("."):
        if isinstance(node, list) and part.isdigit():
            node = node[int(part)] if int(part) < len(node) else None
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return ""
        if node is None:
            return ""
    if isinstance(node, str) and prop.endswith(".border"):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", node)
        return m.group(0) if m else ""
    return node if isinstance(node, str) else ""


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a.rstrip("%")) >= (100 if a.endswith("%") else 1):
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    m = re.fullmatch(r"hsla?\(\s*0\s*,\s*0%\s*,\s*([\d.]+)%\s*(?:[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        lvl = round(float(m.group(1)) * 2.55)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else f"rgba({lvl}, {lvl}, {lvl}, {'%g' % a})"
    return v


BY_VALUE = {}


def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "var" in v:
            BY_VALUE.setdefault(norm_color(R[v["var"]]), []).append(prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")


collect(SPEC["dark"]["color"], "color.")


def pick_role(candidates, prop):
    """Several dark roles can share one paint; prefer the path whose role
    matches what was measured (a fill measurement should not cite a
    border token)."""
    is_fill = prop.endswith("backgroundColor") or prop.endswith(".bg") or "fill" in prop
    if is_fill:
        for c in candidates:
            if ".fill." in c or c.endswith(".fill"):
                return c
    else:
        for c in candidates:
            if ".text." in c or c.endswith(".text"):
                return c
    return candidates[0]


def role(path, comp, state, prop, desc):
    v = norm_color(stprop(comp, state, prop))
    if not v or v == "transparent":
        return False
    cands = BY_VALUE.get(v, [])
    target = pick_role(cands, prop) if cands else None
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as dark.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    node = SPEC["dark"]
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


GAPS = []  # mapped rows that yielded no token, printed by the build

for path, comp, state, prop, desc in [
    ("page", "header-bar", "default", "ancestors.0.bg", "The ground the navbar sits on (body's own paint)."),
    ("nav", "header-bar", "default", "backgroundColor", "The navbar's painted surface."),
    ("text", "detail-title", "default", "color", "The display type's white."),
    # The CTA pills paint their fill on ::before — the root box is transparent,
    # so the role must read the painted pseudo-element layer.
    ("accentFill", "hero-cta", "default", "::before.backgroundColor", "The 'Start Subscription' pill's fill (painted on ::before)."),
    ("accentText", "hero-cta", "default", "color", "Text on the primary pill."),
    ("signinFill", "header-signin", "default", "::before.backgroundColor", "The Sign In pill's fill."),
    ("link", "footer-link", "default", "color", "Footer link colour."),
    ("focus", "header-nav-link", "focus-visible", "outlineColor", "The keyboard-focus ring where one is drawn."),
]:
    try:
        if role(path, comp, state, prop, desc) is False:
            GAPS.append(f"dark.{path} ({comp} {state}: transparent or empty)")
    except KeyError:
        GAPS.append(f"dark.{path} ({comp} {state}: not captured)")

# -------------------------------------------------- measured extras (no var)

meas = SPEC["dark"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("hero-cta", "hover", "ctaHover", "::before.backgroundColor", "The CTA fill on hover (painted on ::before)."),
    ("hero-cta", "pressed", "ctaPress", "::before.backgroundColor", "The CTA fill under :active, forced with CDP forcePseudoState."),
    ("header-signin", "hover", "signinHover", "backgroundColor", "The Sign In pill on hover."),
    ("faq-item", "opened", "faqOpen", "color", "The open FAQ item's text colour."),
    ("plan-choose", "default", "chooseFill", "::before.backgroundColor", "A plan card's Choose button fill (painted on ::before)."),
    ("consent-accept", "default", "consentFill", "::before.backgroundColor", "The consent modal's Accept fill (painted on ::before)."),
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
        else:
            err = C[comp]["states"][state].get("error")
            GAPS.append(f"dark.measured.{key} ({comp} {state}: {'the reading is an error' if err else 'transparent or empty'})")
    except KeyError:
        GAPS.append(f"dark.measured.{key} ({comp} {state}: not captured)")

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightCta", "hero-cta", "default", "height", "The 'Start Subscription' pill height."),
    ("control.heightSignin", "header-signin", "default", "height", "The Sign In pill height."),
    ("control.radiusCta", "hero-cta", "default", "borderTopLeftRadius", "The CTA's corner radius."),
    ("nav.height", "header-bar", "default", "height", "The navbar block at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("card.radius", "plan-card", "default", "borderTopLeftRadius", "A plan card's corner radius."),
    ("dialog.radius", "consent-dialog", "default", "borderTopLeftRadius", "The consent modal's corner radius."),
]:
    try:
        v = stprop(cname, state, prop)
        # the capture records the four corners, never the borderRadius
        # shorthand; a radius token needs all four to agree
        if prop == "borderTopLeftRadius":
            st_ = C[cname]["states"][state].get("style", {})
            if len({st_.get(f"border{c}Radius") for c in ("TopLeft", "TopRight", "BottomRight", "BottomLeft")}) != 1:
                GAPS.append(f"component.{key} ({cname} {state}: corners differ)")
                continue
        if not v or v == "0px":
            GAPS.append(f"component.{key} ({cname} {state}: {v or 'no reading'})")
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        GAPS.append(f"component.{key} ({cname} {state}: not captured)")

if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
    print("no token (see README What to distrust):", "; ".join(GAPS))


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
