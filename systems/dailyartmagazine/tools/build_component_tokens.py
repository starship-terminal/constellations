#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dailyartmagazine.com is a WordPress art-history magazine (idvetmp theme +
child). Its stylesheets declare almost no design layer on :root — the only
custom properties resolved (raw/css-vars.json) are the stock WordPress
Gutenberg presets (--wp--preset--color-*, --wp--preset--gradient-*,
--wp--preset--font-size-*, --wp--preset--spacing-*, --wp--preset--shadow-*)
plus a few ad-slot internals. The design itself is literal CSS, so almost
every leaf below is a measured computed style from
raw/components-computed.json.

What was measured (desktop 1440x900 unless noted):

  #19191c   the near-black ink behind the top nav, the hero band and the
            mid-page dark sections (donation/long-reads)
  #c6002f   the crimson accent — chips/tags, ghost-button borders, footer
            links, the Search button hover fill
  #f3003a   the brighter red on inline article links
  #4d5761   the slate body/muted text (article paragraphs, meta)
  #2e2e32   the dark hairline inside dark regions and the hero-tag rules
  #989da7   the contact-submit border grey

  Typography: Basier for UI/body (nav 14px/600, body 16-18px/400, chips
  10px/700), RoslindaleCondensed for display (hero + article 56px/500,
  section 32px, feed tabs 28px), RoslindaleNarrow for card titles
  (20px/700) and category-menu items (16px/600).

The page paints ONE theme: a white editorial field crossed by dark bands.
There is no dark class/theme switch; the export keeps `dark` empty and the
dark regions are recorded as surfaces inside the single theme.
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
    "dailyartmagazine.com is a single-theme WordPress magazine: a white "
    "editorial field with #19191c dark bands (top nav, hero, mid-page "
    "sections) and a #c6002f crimson accent. The theme declares only stock "
    "WordPress --wp--preset--* variables, so design values are measured "
    "computed styles, wp presets are var-referenced where declared."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def rc(comp, state, key):
    return C[comp]["states"][state]["rect"][key]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one."""
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


fam["sans"] = lit(family(["nav-link", "art-para", "nl-send"]), "fontFamily",
    "computed fontFamily of nav-link, art-para, nl-send (raw/components-computed.json); @font-face Basier in idvetmp-child style.css",
    "Basier — every UI string, body copy, buttons, chips, meta.")
fam["display"] = lit(family(["hero-h1", "art-h1", "section-heading", "feed-tab"]), "fontFamily",
    "computed fontFamily of hero-h1, art-h1, section-heading, feed-tab (raw/components-computed.json); @font-face RoslindaleCondensed in style.css",
    "RoslindaleCondensed — hero/article 56px, section headings 32px, feed tabs 28px.")
fam["narrow"] = lit(family(["post-card-title", "cat-nav-item"]), "fontFamily",
    "computed fontFamily of post-card-title, cat-nav-item (raw/components-computed.json); @font-face RoslindaleNarrow in style.css",
    "RoslindaleNarrow — card titles 20px/700, category-menu items 16px/600.")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, val, src_c, desc in [
    ("normal", "400", "art-para", "400 — body copy, inputs."),
    ("medium", "500", "hero-h1", "500 — every display heading."),
    ("semibold", "600", "nav-link", "600 — nav links, buttons, card meta labels."),
    ("bold", "700", "hero-tag", "700 — chips/tags, card titles (RoslindaleNarrow)."),
]:
    try:
        weights[key] = lit(st(src_c, "default")["fontWeight"], "fontWeight",
            f"computed fontWeight of {src_c} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------ wp presets

wp = SPEC["core"].setdefault("wp-preset", {})
for n in sorted(R):
    grp, _, leaf = n[len("--wp--preset--"):].partition("--")
    val = R[n]
    ty_ = "color" if grp == "color" else ("dimension" if grp in ("font-size", "spacing") else "other")
    wp.setdefault(grp.replace("-", "_"), {})[leaf.replace("-", "_")] = var(n, ty_,
        source=f"css-var {n} resolved (raw/css-vars.json)",
        description=f"Stock WordPress Gutenberg preset {n} — declared for the block editor; theme styles do not consume it.")

# -------------------------------------------------- measured semantic roles

sem = SPEC["light"]
for key, comp, state, prop, group, desc in [
    ("dark-band", "nav-bar", "default", "backgroundColor", "background",
     "The #19191c near-black behind the top nav, the hero band and the mid-page dark sections."),
    ("page", "cat-nav", "opened", "backgroundColor", "background",
     "The #fff page field — body declares no background and paints the default canvas white; verified against the white mega-menu, feed and field surfaces."),
    ("menu-panel", "cat-nav", "opened", "backgroundColor", "background",
     "The white mega-menu panel the Art Movements dropdown paints (#fff, over the dark bar)."),
    ("ink", "post-card-title", "default", "color", "text",
     "The #000 ink on every light-surface heading and label."),
    ("muted", "art-para", "default", "color", "text",
     "The #4d5761 slate of article paragraphs, card excerpts and meta."),
    ("on-dark", "nav-link", "default", "color", "text",
     "White text on the #19191c bands."),
    ("accent", "hero-tag", "default", "backgroundColor", "action",
     "The #c6002f crimson — chips, tags, ghost-button borders, footer links, hover fills."),
    ("link-bright", "art-inline-link", "default", "color", "action",
     "The #f3003a brighter red the theme paints on inline article links."),
    ("accent-ghost-border", "search-btn", "default", "borderTopColor", "border",
     "The 1px #c6002f border of the ghost buttons (Search, Send, Load more)."),
    ("hairline-dark", "cat-nav-item", "default", "borderTopColor", "border",
     "The #2e2e32 dark hairline — menu-item rules and the hero-tag flanking lines."),
    ("submit-border", "cf7-send", "default", "borderTopColor", "border",
     "The #989da7 grey border on the black contact-submit button."),
    ("field-surface", "nl-email", "default", "backgroundColor", "background",
     "White input fill (newsletter email, contact fields)."),
]:
    try:
        sem.setdefault(group, {})[key] = lit(st(comp, state)[prop], "color",
            f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# the modal overlay, recorded on the nl-modal ancestors list
try:
    scrim = next(a["bg"] for a in C["nl-modal"]["states"]["default"]["ancestors"] if a.get("bg", "").startswith("rgba(0, 0, 0"))
    sem.setdefault("background", {})["scrim"] = lit(scrim, "color",
        "computed backgroundColor of the .modal-r overlay ancestor of nl-modal default (raw/components-computed.json)",
        "The rgba(0,0,0,.9) overlay the newsletter modal's ancestor paints behind the panel.")
except (KeyError, StopIteration):
    pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("chip", "hero-tag", "default", "The 10px/700 uppercase chip text."),
    ("ui", "nav-link", "default", "The 14px nav/button/meta size."),
    ("body", "nl-modal", "default", "The 16px body size (modal copy, menus)."),
    ("article", "art-para", "default", "The 18px article paragraph."),
    ("card-title", "post-card-title", "default", "The 20px RoslindaleNarrow card title."),
    ("tab", "feed-tab", "default", "The 28px RoslindaleCondensed feed tab."),
    ("section", "section-heading", "default", "The 32px section heading."),
    ("display", "hero-h1", "default", "The 56px hero/article display heading."),
]:
    try:
        ty[key] = lit(st(comp, state)["fontSize"], "fontSize",
            f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("article", "art-para", "default", "Article paragraph line-height."),
    ("display", "hero-h1", "default", "Display heading line-height."),
    ("modal-copy", "nl-modal", "default", "The 21.6px modal copy line-height (textStyle)."),
]:
    try:
        v = ts(comp, state, "lineHeight")
        if v:
            lh[key] = lit(v, "other",
                f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("sm", "cf7-send", "default", "borderTopLeftRadius", "The 2px contact-submit radius."),
    ("md", "hero-tag", "default", "borderTopLeftRadius", "The 3px chip/button/input radius."),
]:
    try:
        radii[key] = lit(st(comp, state)[prop], "dimension",
            f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
try:
    sh["menu"] = lit(st("cat-nav", "opened")["boxShadow"], "other",
        "computed boxShadow of cat-nav opened (raw/components-computed.json)",
        "The rgba(0,0,0,.25) 0 16px 48px drop under the mega-menu.")
except KeyError:
    pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("search-btn", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["hover"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of search-btn default (raw/components-computed.json)",
            "The hover fill transition shared by the ghost buttons.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("nav-height", "nav-bar", "default", "h", "dimension", "The 65px fixed top nav."),
    ("nav-cluster-width", "nav-cluster", "default", "w", "dimension", "The 300px primary-nav cluster."),
    ("logo-width", "nav-logo", "default", "w", "dimension", "The 111px wordmark."),
    ("hamburger-size", "hamburger", "default", "h", "dimension", "The 20x15 hamburger trigger."),
    ("cat-nav-height", "cat-nav", "opened", "h", "dimension", "The 633px mega-menu panel."),
    ("cat-nav-item-height", "cat-nav-item", "default", "h", "dimension", "The 59px category-menu row."),
    ("search-btn-height", "search-btn", "default", "h", "dimension", "The 38px header Search button."),
    ("hero-height", "hero-block", "default", "h", "dimension", "The ~799px dark hero band."),
    ("chip-height", "hero-tag", "default", "h", "dimension", "The 20.25px crimson category chip."),
    ("card-h-width", "post-card-h", "default", "w", "dimension", "The 760px horizontal feed card."),
    ("card-h-height", "post-card-h", "default", "h", "dimension", "The 194px feed card height."),
    ("card-img-width", "post-card-img", "default", "w", "dimension", "The 260x177 card thumbnail."),
    ("card-v-height", "post-card-v", "default", "h", "dimension", "The 292.75px vertical card."),
    ("load-more-height", "load-more", "default", "h", "dimension", "The 38px full-width Load more ghost button."),
    ("nl-send-height", "nl-send", "default", "h", "dimension", "The 38px newsletter Send button."),
    ("nl-email-height", "nl-email", "default", "h", "dimension", "The 40px email input."),
    ("nl-checkbox-input", "nl-checkbox", "default", "w", "dimension", "The 13px invisible input box (opacity:0); the painted checkbox is the label's ::after."),
    ("nl-modal-width", "nl-modal", "default", "w", "dimension", "The 720px slide-down newsletter modal."),
    ("article-column", "art-para", "default", "w", "dimension", "The 648px article text column."),
    ("article-header-width", "art-h1", "default", "w", "dimension", "The 1152px article header row."),
    ("figure-width", "art-figure", "default", "w", "dimension", "The 648px article figure."),
    ("contact-form-width", "cf7-form", "default", "w", "dimension", "The 669px Contact Form 7 form."),
    ("contact-input-width", "cf7-name", "default", "w", "dimension", "The half-width 319.5px name/email field."),
    ("contact-send-height", "cf7-send", "default", "h", "dimension", "The 46px black Send button."),
    ("footer-height", "footer", "default", "h", "dimension", "The 842px footer block."),
    ("ad-slot-height", "ad-slot", "default", "h", "dimension", "The 98px leaderboard ad slot."),
]:
    try:
        s_ = C[cname]["states"][state]
        if prop in ("w", "h"):
            v = s_["rect"][prop]
        elif prop == "bg":
            v = s_["style"]["backgroundColor"]
        else:
            v = s_["style"][prop]
        if v and v not in ("0px", "auto", "rgba(0, 0, 0, 0)"):
            comp[name] = lit(v, ty_,
                f"computed {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# the painted checkbox box: the input sits at opacity 0 (13x13) and the
# visible box is the label's ::after — 16x16, #fff, 1px #989da7, 2px radius.
# A probe read it with getComputedStyle(label, '::after') on the live home
# page, but that reading was never saved: no file in raw/ holds it, so the
# value is labelled as typed.
comp["nl-checkbox-box"] = lit("16px", "dimension",
    "entered by hand at capture time, not measured: a probe of the .checkbox-style label's ::after (16x16 #fff, 1px solid #989da7, 2px radius) "
    "was never saved to raw/; raw/components-computed.json holds only the 13x13 input (nl-checkbox); recapture needed",
    "The 16px painted checkbox box (white, 1px #989da7 border, 2px radius) — the 13px input is opacity:0.")

# the hero-tag flanking rules (measured pseudo-elements)
try:
    pseudo = C["hero-tag"]["states"]["default"]["::before"]
    comp["chip-flanking-rule"] = lit(
        f"{pseudo['width']} x {pseudo['height']}", "other",
        "computed ::before/::after of hero-tag default (raw/components-computed.json)",
        "The 41x1 #2e2e32 rules the hero tag paints on both sides.")
except KeyError:
    pass

# measured state moves on the interactive controls; a state that failed to
# capture (an 'error' entry, no 'style') is skipped, not allowed to drop the rest
for name, cname, desc in [
    ("ghost-dark-track", "search-btn",
     "Ghost button on the dark bar (Search): transparent + 1px #c6002f border with WHITE text at rest, fills #c6002f on hover/pressed."),
    ("ghost-light-track", "nl-send",
     "Ghost button on white (newsletter Send, Load more): transparent + 1px #c6002f border with #000 text at rest, fills #c6002f with white text on hover/pressed."),
    ("nav-link-state-track", "nav-link",
     "Nav link: white at rest; no background/color change on hover or pressed — focus shows a dotted white outline."),
    ("cat-item-state-track", "cat-nav-item",
     "Category-menu item: #000 RoslindaleNarrow on the white panel with a #2e2e32 1px bottom rule; hover state not captured (item leaves the viewport as the panel opens)."),
]:
    try:
        states = {s2: {p: C[cname]["states"][s2]["style"][p] for p in ("backgroundColor", "color", "transform", "outlineStyle") if C[cname]["states"][s2]["style"].get(p)}
                  for s2 in ("default", "hover", "pressed", "focus-visible")
                  if s2 in C[cname]["states"] and C[cname]["states"][s2].get("style")}
        comp.setdefault("state-track", {})[name] = {
            "type": "other",
            "value": states,
            "source": f"computed styles of {cname} across states (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass

# the shared dotted focus outline
try:
    comp["focus-ring"] = lit(
        f"{st('nav-link', 'focus-visible')['outlineStyle']} {st('nav-link', 'focus-visible')['outlineColor']}",
        "other",
        "computed outline of nav-link/footer-link/art-inline-link focus-visible (raw/components-computed.json)",
        "The browser's dotted outline in the element's own colour — no custom focus ring is painted.")
except KeyError:
    pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
