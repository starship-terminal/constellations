#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

descript.com is a Next.js + Tailwind marketing site (the app lives behind
web.descript.com and was never signed into; its public sign-in card is
measured as a boundary). The site's stylesheets declare a named palette
layer on :root — the Red / Maroon / Lilac / Neutral / Green / Gray scales,
the Core canvas constants and the Tools-Glow pastels
(raw/css-vars.json resolved.light) — so declared scales are exported
under core.color.* and measured computed styles from
raw/components-computed.json alias to them where the values match.

What was measured (desktop 1440x900 unless noted):

  #fff7fa   the blush page field (Neutral-0) — nav, cards, page paint
  #26171d   the marketing ink (Neutral-900) — nav text, story prose
  #1a1a1a   Gray-900 — body text on pricing/templates
  #772a4d   Maroon-700 — the Sign up button, rests; #5b142e Maroon-800 on hover
  #390a1a   Maroon-900 — the pricing plan CTAs
  #f73b3b   Red-450 — the red CTAs and uppercase eyebrow; #8f0c10 pressed
  #5b142e   Maroon-800 — the selected workflow tab fill
  #c4b5bb   muted mauve — unselected workflow-tab text on the dark hero band
  #fff7fd   near-white text over the dark hero band and selected states
  #110a0d   the near-black maroon footer
  #f1eaed   the billing-toggle track and nav-link hover wash
  #3f2a32   the auth card's primary button (web.descript.com)
  #fdfcfc   the auth card's outline-button and field fills

  Typography: booton for UI/body (16px/400-600; auth uses "Booton VF"
  15.75px/500), brett for the 18px uppercase eyebrows, gamuthDisplay for
  every display heading (hero 88px, section 56px/61.6, page 72px/79.2,
  mobile 48px).

The page paints ONE theme: a #fff7fa blush field with a dark maroon hero
band, a #110a0d footer and a light auth card. There is no theme switch;
the export keeps `dark` empty and the dark regions are recorded as
surfaces inside the single theme.
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
    "The token tree build_tokens.py turns into tokens.json. "
    "descript.com is a single-theme Next.js + Tailwind marketing site: a "
    "#fff7fa blush field, maroon CTAs and a deep-maroon hero band. Its "
    "stylesheet declares the Red/Maroon/Lilac/Neutral/Green/Gray palette "
    "scales plus Core canvas constants and Tools-Glow pastels (exported "
    "under core.color.*); the measured roles under light.* alias to the "
    "declared values where they match."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
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


def family(comps):
    """The computed fontFamily stack, verbatim; every cited component must paint the same one."""
    stacks = {st(c, "default")["fontFamily"] for c in comps}
    if len(stacks) != 1:
        raise SystemExit(f"fontFamily differs across {comps}: {sorted(stacks)}")
    return stacks.pop()


fam["sans"] = lit(family(["nav-link", "signup-cta", "flow-tab", "pr-toggle"]), "fontFamily",
    "computed fontFamily of nav-link, signup-cta, flow-tab, pr-toggle (raw/components-computed.json); "
    "pr-card, pr-cta, site-footer and st-prose compute the same stack with Tailwind's fallback list repeated after it",
    "Booton — UI, body copy, nav, buttons and every form control on descript.com.")
fam["auth"] = lit(family(["au-email", "au-email-btn", "au-google", "au-password", "au-sso"]), "fontFamily",
    "computed fontFamily of au-email, au-email-btn, au-google, au-password, au-sso (raw/components-computed.json)",
    "Booton VF — the auth card on web.descript.com names the variable face instead of booton.")
fam["label"] = lit(family(["hero-eyebrow", "pr-eyebrow", "m-eyebrow"]), "fontFamily",
    "computed fontFamily of hero-eyebrow, pr-eyebrow, m-eyebrow (raw/components-computed.json)",
    "Brett — the small uppercase eyebrow labels.")
fam["display"] = lit(family(["hero-display", "section-h2", "pr-display", "vid-h1", "tpl-h1"]), "fontFamily",
    "computed fontFamily of hero-display, section-h2, pr-display, vid-h1, tpl-h1 (raw/components-computed.json)",
    "Gamuth Display — every display heading, hero 88px to section 56px.")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, val_c, desc in [
    ("normal", "hero-eyebrow", "400 — eyebrow labels and body copy."),
    ("medium", "au-email-btn", "500 — the auth card's Booton VF buttons."),
    ("semibold", "nav-link", "600 — nav items, CTAs, plan names, section h2s."),
]:
    try:
        weights[key] = lit(st(val_c, "default")["fontWeight"], "fontWeight",
            f"computed fontWeight of {val_c} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------- declared palette (:root)
#
# The stylesheet declares Descript's named palette outright: the Red,
# Maroon, Lilac, Neutral, Green and Gray step scales, the Core canvas
# constants and the Tools-Glow pastel accents (raw/css-vars.json
# resolved.light). Export them under core.color.*; the measured roles
# below alias into them where a computed style resolves to an identical
# value.

DECL_SRC = "declared variable in the site stylesheet (raw/css-vars.json resolved.light)"


def decl(name):
    return lit(R[name], "dimension", f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def decl_color(name):
    v = R[name]
    ty = "color" if re.match(r"(#|rgba?\(|hsla?\(|(ok)?lab\(|(ok)?lch\(|color-mix\()", str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


color_alias = {}   # normalized colour -> 'color.<path>' for aliasing
colors = SPEC["core"].setdefault("color", {})
for name in sorted(k for k in R if re.match(r"--(Red|Maroon|Lilac|Neutral|Green|Gray)-", k)):
    fam_name, step = name[2:].split("-", 1)
    group = colors.setdefault(fam_name.lower(), {})
    group[step.lower()] = decl_color(name)
    if group[step.lower()]["type"] == "color":
        color_alias.setdefault(norm_color(R[name]), f"color.{fam_name.lower()}.{step.lower()}")
for name in sorted(k for k in R if k.startswith("--Core-")):
    key = name[len("--Core-"):].lower()
    colors.setdefault("core", {})[key] = decl_color(name)
    if colors["core"][key]["type"] == "color":
        color_alias.setdefault(norm_color(R[name]), f"color.core.{key}")
for name in sorted(k for k in R if k.startswith("--Tools-")):
    key = name[len("--Tools-"):].lower()
    colors.setdefault("tools", {})[key] = decl_color(name)
    if colors["tools"][key]["type"] == "color":
        color_alias.setdefault(norm_color(R[name]), f"color.tools.{key}")

# -------------------------------------------------- measured semantic roles

sem = SPEC["light"]


def semcolor(group, key, raw, src, desc):
    """A measured colour role; aliases to the declared palette on an exact match."""
    alias = color_alias.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


for key, comp, state, prop, group, desc in [
    ("page", "mkt-header", "default", "backgroundColor", "background",
     "The #fff7fa blush field (Neutral-0) the nav, cards and page paint."),
    ("ink", "nav-link", "default", "color", "text",
     "The #26171d marketing ink (Neutral-900) — nav text, story prose, headings."),
    ("body", "pr-card", "default", "color", "text",
     "The #1a1a1a Gray-900 body text on pricing, templates and the auth card."),
    ("accent", "hero-eyebrow", "default", "color", "text",
     "The #f73b3b Red-450 — the uppercase eyebrow labels and red CTAs."),
    ("on-dark", "hero-display", "default", "color", "text",
     "The #fff8f4 near-white (Red-0) display text over the dark hero band."),
    ("muted-on-dark", "flow-tab", "default", "color", "text",
     "The #c4b5bb muted mauve — unselected workflow-tab text over the dark band."),
    ("focus", "signup-cta", "focus-visible", "outlineColor", "border",
     "The #101010 1px auto focus outline on light controls."),
]:
    try:
        sem.setdefault(group, {})[key] = semcolor(group, key, st(comp, state)[prop],
            f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# the dark hero band + footer + tab/track surfaces are painted on children —
# read them off the paint lists and computed styles of the right nodes.
try:
    sem.setdefault("background", {})["footer"] = semcolor("background", "footer",
        st("site-footer", "default")["backgroundColor"],
        "computed backgroundColor of site-footer default (raw/components-computed.json)",
        "The #110a0d near-black maroon footer.")
except KeyError:
    pass
try:
    sem.setdefault("background", {})["toggle-track"] = semcolor("background", "toggle-track",
        st("pr-toggle", "default")["backgroundColor"],
        "computed backgroundColor of pr-toggle default (raw/components-computed.json)",
        "The #f1eaed warm-grey track behind the Monthly/Annual options — the same wash nav links take on hover.")
except KeyError:
    pass
try:
    band = next(pl["bg"] for pl in C["flow-tabs"]["states"]["default"]["paint"] if pl.get("bg") == "rgb(91, 20, 46)")
    sem.setdefault("surface", {})["tab-selected"] = semcolor("surface", "tab-selected", band,
        "painted background of the selected workflow tab inside flow-tabs default (raw/components-computed.json)",
        "The #5b142e Maroon-800 fill the selected workflow tab paints.")
except (KeyError, StopIteration):
    pass
try:
    sem.setdefault("action", {})["primary"] = semcolor("action", "primary",
        st("signup-cta", "default")["backgroundColor"],
        "computed backgroundColor of signup-cta default (raw/components-computed.json)",
        "The #772a4d Maroon-700 — the Sign up button and primary CTA fill.")
    sem.setdefault("action", {})["primary-hover"] = semcolor("action", "primary-hover",
        st("signup-cta", "hover")["backgroundColor"],
        "computed backgroundColor of signup-cta hover (raw/components-computed.json)",
        "The #5b142e Maroon-800 the maroon buttons deepen to on hover/pressed.")
except KeyError:
    pass
try:
    sem.setdefault("action", {})["deep"] = semcolor("action", "deep",
        st("pr-cta", "default")["backgroundColor"],
        "computed backgroundColor of pr-cta default (raw/components-computed.json)",
        "The #390a1a Maroon-900 — the pricing plan CTAs.")
except KeyError:
    pass
try:
    sem.setdefault("action", {})["red"] = semcolor("action", "red",
        st("vid-cta", "default")["backgroundColor"],
        "computed backgroundColor of vid-cta default (raw/components-computed.json)",
        "The #f73b3b Red-450 — the red hero CTAs.")
    sem.setdefault("action", {})["red-hover"] = semcolor("action", "red-hover",
        st("vid-cta", "hover")["backgroundColor"],
        "computed backgroundColor of vid-cta hover (raw/components-computed.json)",
        "The #b81b1e the red CTAs deepen to on hover.")
    sem.setdefault("action", {})["red-pressed"] = semcolor("action", "red-pressed",
        st("vid-cta", "pressed")["backgroundColor"],
        "computed backgroundColor of vid-cta pressed (raw/components-computed.json)",
        "The #8f0c10 Red-700 the red CTAs deepen to when pressed.")
except KeyError:
    pass
try:
    sem.setdefault("action", {})["auth-primary"] = semcolor("action", "auth-primary",
        st("au-email-btn", "default")["backgroundColor"],
        "computed backgroundColor of au-email-btn default (raw/components-computed.json)",
        "The #3f2a32 maroon-grey — the auth card's primary button.")
    sem.setdefault("action", {})["auth-outline"] = semcolor("action", "auth-outline",
        st("au-google", "default")["backgroundColor"],
        "computed backgroundColor of au-google default (raw/components-computed.json)",
        "The #fdfcfc field/outline fill on the auth card's secondary buttons and input.")
except KeyError:
    pass
try:
    sem.setdefault("action", {})["hover-wash"] = semcolor("action", "hover-wash",
        st("nav-link", "hover")["backgroundColor"],
        "computed backgroundColor of nav-link hover (raw/components-computed.json)",
        "The #f1eaed warm-grey wash nav links take on hover — the same as the billing-toggle track.")
except KeyError:
    pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("auth", "au-email-btn", "default", "The 15.75px auth-card control size (Booton VF)."),
    ("body", "st-prose", "default", "The 16px body/nav/CTA size."),
    ("eyebrow", "hero-eyebrow", "default", "The 18px uppercase Brett eyebrow."),
    ("mobile-display", "m-display", "default", "The 48px mobile display heading."),
    ("section", "section-h2", "default", "The 56px Gamuth section/pricing heading."),
    ("page", "vid-h1", "default", "The 72px Gamuth page heading."),
    ("hero", "hero-display", "default", "The 88px Gamuth home display (clamped by viewport)."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        ty[key] = lit(raw, "fontSize",
            f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("body", "st-prose", "default", "The 24px body line-height."),
    ("section", "section-h2", "default", "The 61.6px section-heading line-height (1.1x)."),
    ("page", "vid-h1", "default", "The 79.2px page-heading line-height (1.1x)."),
]:
    try:
        v = st(comp, state)["lineHeight"]
        if v:
            lh[key] = lit(v, "other",
                f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("control", "au-email-btn", "default", "borderTopLeftRadius", "The 8px auth-card button/field radius."),
    ("cta", "signup-cta", "default", "borderTopLeftRadius", "The 12px CTA/plan-card radius."),
    ("nav-item", "nav-link", "default", "borderTopLeftRadius", "The 4px nav-item corner."),
    ("toggle", "pr-toggle", "default", "borderTopLeftRadius", "The 42px billing-toggle track pill."),
]:
    try:
        v = st(comp, state)[prop]
        radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other",
            f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
for key, comp, desc in [
    ("plan-card", "pr-card", "The pricing plan-card elevation."),
    ("header", "mkt-header", "The header's drop over the page."),
]:
    try:
        v = st(comp, "default")["boxShadow"]
        if v and v != "none":
            sh[key] = lit(v, "other",
                f"computed boxShadow of {comp} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for key, comp, desc in [
    ("hover", "signup-cta", "The transition the CTAs run across hover/press."),
    ("tab", "flow-tab", "The workflow-tab state transition."),
]:
    try:
        s = st(comp, "default")
        dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
        if dur and dur != "0s":
            props = s.get('transitionProperty', 'all')
            durs = [d.strip() for d in (dur or '').split(',')]
            timed = ", ".join(f"{prop.strip()} {durs[i] if i < len(durs) else durs[-1]} {ease or ''}".strip() for i, prop in enumerate(props.split(',')))
            mo[key] = lit(timed, "other",
                f"computed transition of {comp} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("header-height", "mkt-header", "default", "h", "dimension", "The 102px floating header bar."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The 98px Descript wordmark."),
    ("nav-item-height", "nav-link", "default", "h", "dimension", "The 32px nav-item hit area."),
    ("signup-size", "signup-cta", "default", "h", "dimension", "The 54px Sign up button (108px wide)."),
    ("flow-tab-height", "flow-tab", "default", "h", "dimension", "The 44px workflow tabs."),
    ("flow-tabs-width", "flow-tabs", "default", "w", "dimension", "The 610px workflow tab strip."),
    ("toggle-size", "pr-toggle", "default", "h", "dimension", "The 50px billing-toggle track (228px wide)."),
    ("toggle-option", "pr-toggle-annual", "default", "h", "dimension", "The 34px toggle option (106px wide)."),
    ("plan-card-size", "pr-card", "default", "h", "dimension", "The 708px-tall pricing plan card (284px wide)."),
    ("plan-cta-size", "pr-cta", "default", "h", "dimension", "The 56px plan-card CTA."),
    ("template-card", "tpl-link", "default", "h", "dimension", "The 381px-tall template card (336px wide)."),
    ("hero-display-size", "hero-display", "default", "h", "dimension", "The 210px-tall hero display block (892px wide)."),
    ("auth-control", "au-email-btn", "default", "h", "dimension", "The 40px auth-card buttons and field (308px wide)."),
    ("footer-height", "site-footer", "default", "h", "dimension", "The 1146px sitemap footer."),
    ("m-header-height", "m-header", "default", "h", "dimension", "The 84px mobile header."),
    ("m-toggle-option", "mp-toggle", "default", "h", "dimension", "The 32.5px mobile billing-toggle option."),
    ("m-plan-cta", "mp-cta", "default", "h", "dimension", "The 52.5px mobile plan CTA (full-width)."),
]:
    try:
        s_ = C[cname]["states"][state]
        v = s_["rect"][prop] if prop in ("w", "h") else s_["style"][prop]
        if v and v not in ("0px", "auto", "rgba(0, 0, 0, 0)"):
            comp[name] = lit(v, ty_,
                f"computed {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# measured state moves on the interactive controls; a state that failed to
# capture (an 'error' entry, no 'style') is skipped, not allowed to drop the rest
for name, cname, desc in [
    ("signup-track", "signup-cta",
     "Sign up button: #772a4d Maroon-700 fill/white text at rest; hover+pressed deepen to #5b142e Maroon-800; focus shows the 1px auto outline."),
    ("red-cta-track", "vid-cta",
     "Red CTA: #f73b3b Red-450 at rest; #b81b1e on hover; #8f0c10 Red-700 pressed; focus shows the 1px auto outline."),
    ("nav-link-track", "nav-link",
     "Nav item: transparent/#26171d at rest; the #f1eaed warm-grey wash on hover/pressed; focus shows the 1px auto outline."),
    ("flow-tab-track", "flow-tab",
     "Workflow tab: muted #c4b5bb text on the dark band at rest; #26171d ink wash on hover; opened selects the #5b142e Maroon-800 fill with #fff7fd text."),
    ("toggle-track", "pr-toggle-annual",
     "Billing-toggle option: transparent/#1a1a1a at rest on the #f1eaed track; opened is the Annual-selected state; focus shows the 1px auto outline."),
    ("auth-primary-track", "au-email-btn",
     "Auth primary: #3f2a32 at rest; a 90%-alpha oklab shade on hover/pressed."),
    ("template-card-track", "tpl-link",
     "Template card overlay: no paint change across hover/pressed; focus-visible paints a 2px inset ring."),
]:
    try:
        states = {s2: {p: C[cname]["states"][s2]["style"][p] for p in ("backgroundColor", "color", "opacity", "transform", "boxShadow", "borderTopColor", "borderRightColor", "borderBottomColor", "borderLeftColor", "outlineColor", "outlineStyle", "outlineWidth", "outlineOffset") if C[cname]["states"][s2]["style"].get(p)}
                  for s2 in ("default", "hover", "pressed", "focus-visible", "opened")
                  if s2 in C[cname]["states"] and C[cname]["states"][s2].get("style")}
        comp.setdefault("state-track", {})[name] = {
            "type": "other",
            "value": states,
            "source": f"computed styles of {cname} across states (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass

# the shared 1px auto focus outline
try:
    comp["focus-ring"] = lit(
        f"{st('signup-cta', 'focus-visible')['outlineStyle']} {st('signup-cta', 'focus-visible')['outlineColor']}",
        "other",
        "computed outline of signup-cta/nav controls focus-visible (raw/components-computed.json)",
        "The browser's 1px auto outline in #101010 — no custom focus ring is painted on buttons; template cards paint a 2px inset ring.")
except KeyError:
    pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
