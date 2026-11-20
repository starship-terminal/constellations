"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

homerun.co is a Webflow marketing build plus three sibling surfaces on the
same design system: jobs.homerun.co (the employer careers site),
app.homerun.co/login (the Angular ATS sign-in card) and
app.homerun.hr/Account/Logon (the .NET HR sign-in card).

The marketing sheet declares its palette two ways on :root
(raw/css-vars.json, surface `www`):

  the current layer, --_updated-colors-v2---*:
    primary--beige-400..800      #faf9f7 .. #dbd9d5, the tinted grounds
    primary--blue-300..700       #eef2ff .. #0b247f — blue-500 #4f75fe is
                                 the brand blue of every primary button
    primary--brown-100..700      #a3a2a2 .. #131313 — the warm ink scale:
                                 300 #4a3e3e body text, 400 #382d2d
                                 headings, 500 #2d2323 the dark button/CTA
    primary--white               #ffffff  the page ground
    secondary--green/lilac/orange/red/yellow
    tertiary--blood-orange/light-green/navy/pink/purple/warm-grey

  the legacy layer it replaced, still declared alongside:
    coffee-50..950, coffee-black, dark-roasted-coffee-black (the same warm
    browns under old names), beige-*, brown-*, hr--500/700/800 (the HR
    product green), homerun-blue #09f and royal-blue #4f75fe (the same
    brand blue), plus ~60 one-off colour names. They are kept under
    color.named.* verbatim — declared evidence, not curated tokens.

The app surface (app.homerun.co) declares a real token layer of its own —
--ui-* roles over the same palette (radius 10px, input-height 44px,
input-bg #f5f3ef, color-text-default #4a3e3e, button-focus ring) — and the
sign-in card paints exactly those values. A handful are promoted as
component tokens; the full harvest stays in raw/css-vars.json.

Every semantic role in the `light` set is measured on the painted chrome
in raw/components-computed.json and aliases the core when the value
matches: declarations say what Homerun named, measurements say what it
paints. The site shows ONE light theme — the .dark/.darkbg classes name
dark content bands inside it, not a switchable theme, so no dark set is
fabricated.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
# name -> resolved value, per surface (www / jobs / app / apphr)
R = {s: {n: v.get("value", v.get("raw")) for n, v in RES.get(s, {}).items()} for s in RES}
SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. homerun.co is a "
    "Webflow build: its palette lives in --_updated-colors-v2---* (the "
    "current layer, promoted into color.* families) plus a large legacy "
    "named layer kept under color.named.*. Semantic roles are measured on "
    "the painted chrome in raw/components-computed.json and alias the core "
    "when the value matches. One theme exists (light); dark bands live "
    "inside it. The app.homerun.co sign-in shares the palette and declares "
    "its own --ui-* control roles."),
    "core": {}, "light": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `paint.N.prop` (the Nth
    painted child layer), `ancestors.N.prop` or the special `ringShadow`:
    resolve the dotted path inside the measured state. A component flagged
    missing or recaptureMissed is refused here too, as in st()."""
    if C[comp].get("missing") or C[comp].get("recaptureMissed"):
        raise KeyError(comp)
    d = C[comp]["states"][state]
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
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
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and ("var" in v or "value" in v):
            val = norm_color(R["www"].get(v.get("var"), "")) if "var" in v else norm_color(v.get("value", ""))
            BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")


core_color = SPEC["core"].setdefault("color", {})

# ------------------------------------------------------------ core palette
# The current layer: --_updated-colors-v2---<band>--<name>(-<step>).
# Beige/blue/brown carry numbered steps; secondary and tertiary are flat.
V2 = "--_updated-colors-v2---"
V2_DESCS = {
    "beige": "the tinted band grounds (beige-500 #f5f3ef is the input fill and soft section tint)",
    "blue": "the brand blue ramp — blue-500 #4f75fe is every primary button, 300/400 its tints",
    "brown": "the warm ink scale — 200 muted, 300 body text, 400 headings, 500 the dark button/CTA fill",
    "white": "the page ground",
    "secondary": "the secondary accent set (green is the HR accent family)",
    "tertiary": "the tertiary scene colours for illustrations and bands",
}
for n in sorted(R["www"]):
    if not n.startswith(V2):
        continue
    rest = n[len(V2):]                     # e.g. primary--beige-500 / secondary--green
    band, _, name = rest.partition("--")
    if band == "primary":
        fam, _, step = name.partition("-")
        path = f"{fam}.{step}" if step else fam
    else:
        path = f"{band}.{name.replace('-', '_')}"
    node, last = descend(core_color, path.split("."))
    desc = V2_DESCS.get(fam if band == "primary" else band, band)
    node[last] = {"value": norm_color(R["www"][n]), "type": "color",
                  "source": f"declared {n} (raw/css-vars.json)",
                  "description": f"Updated-palette {rest}: {desc}."}

# The legacy named layer: every other :root colour name, slugged under
# color.named.* — declared evidence, the names Homerun's stylesheet uses.
for n in sorted(R["www"]):
    if n.startswith(V2):
        continue
    slug = n[2:].replace("--", ".").replace("_", "-")
    node, last = descend(core_color, ("named",) + tuple(slug.split(".")))
    node[last] = {"value": norm_color(R["www"][n]), "type": "color",
                  "source": f"declared {n} (raw/css-vars.json)",
                  "description": f"Legacy palette name {n[2:]}."}
collect(core_color, "color.")


# ------------------------------------------------------------- light roles
def role(path, comp, state, prop, desc):
    v = stprop(comp, state, prop)
    if "shadow" in prop.lower():
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    theme, _, rest = path.partition(":")
    node = SPEC[theme or "light"]
    parts = rest.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


for path, comp, state, prop, desc in [
    # ----- the single light surface (marketing routes)
    ("light:surface.page", "page-ground", "default", "backgroundColor", "The page ground, painted by the body."),
    ("light:surface.card", "plan-card", "default", "backgroundColor", "A card ground (plan card, FAQ items)."),
    ("light:surface.band", "testimonial-card", "default", "backgroundColor", "The tinted testimonial/band ground."),
    ("light:surface.dark", "cta-band", "default", "backgroundColor", "A dark content band inside the light theme (the closing CTA)."),
    ("light:surface.field", "newsletter-field", "default", "backgroundColor", "The newsletter input's tinted fill (brown at 10%)."),
    ("light:text.primary", "page-ground", "default", "color", "The body ink (= brown-300 #4a3e3e)."),
    ("light:text.heading", "hero-title", "default", "color", "The display ink (= brown-400 #382d2d)."),
    ("light:text.heading2", "section-h2", "default", "color", "Section headings paint a slightly deeper ink than brown-400."),
    ("light:text.muted", "footer-link", "default", "color", "Muted text on footer links and small print (= brown-200 #736b6b)."),
    ("light:text.onDark", "cta-band", "default", "color", "Text on the dark bands."),
    ("light:text.onAccent", "hero-cta", "default", "color", "Text on the brand-blue controls."),
    ("light:accent", "hero-cta", "default", "backgroundColor", "The brand blue where a solid fill shows (= blue-500 #4f75fe)."),
    ("light:accentHover", "hero-cta", "hover", "backgroundColor", "The primary button's hover fill."),
    ("light:accentPressed", "hero-cta", "pressed", "backgroundColor", "The primary button's pressed fill."),
    ("light:darkFill", "nav-demo", "default", "backgroundColor", "The dark brown button fill (= brown-500 #2d2323)."),
    ("light:darkFillHover", "nav-demo", "hover", "backgroundColor", "The dark button's hover fill."),
    ("light:border.subtle", "plan-card", "default", "borderTopColor", "The card hairline (= beige-700 #e3e1dd)."),
    ("light:border.demo", "hero-demo", "default", "borderTopColor", "The secondary button's border (= beige-600 #edebe7)."),
    ("light:focus", "hero-cta", "focus-visible", "outlineColor", "The focus ring on the surface's controls."),
    ("light:nav.link", "nav-link", "default", "color", "Nav link ink at rest."),
    ("light:nav.linkHover", "nav-link", "hover", "color", "Nav link ink on hover."),
    # ----- careers surface (jobs.homerun.co)
    ("light:careers.accent", "careers-all-jobs", "default", "backgroundColor", "The careers site's own button blue (#466af6 — a step between the brand blue and its hover)."),
    ("light:careers.link", "careers-job-card", "default", "textStyle.color", "The job-title link ink on the careers site."),
    ("light:careers.text", "careers-header", "default", "color", "Careers body ink."),
    # ----- the sign-in boundaries
    ("light:app.accent", "signin-button", "default", "backgroundColor", "The ATS sign-in button — the same brand blue-500."),
    ("light:app.field", "signin-email", "default", "backgroundColor", "The sign-in input fill (= beige-500 #f5f3ef)."),
    ("light:app.ssoBorder", "signin-sso", "default", "borderTopColor", "The SSO button's hairline."),
    ("light:app.hrAccent", "hr-button", "default", "backgroundColor", "The HR sign-in button — the HR product green (= secondary--green #00b16b)."),
    ("light:apply.field", "apply-field", "default", "backgroundColor", "The application-form input ground."),
    ("light:apply.border", "apply-field", "default", "borderTopColor", "The application-form input hairline."),
    ("light:apply.accent", "apply-next", "default", "backgroundColor", "The application wizard's Next fill — the brand blue again."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass


# The one painted elevation: the open nav panel's drop shadow.
for _cname in ("nav-resources-panel", "nav-login-panel", "cookie-banner"):
    try:
        _sh = stprop(_cname, "default", "boxShadow") or ""
        if _sh and _sh != "none":
            _layers = []
            for _ly in re.split(r",(?![^(]*\))", _sh):
                m = re.match(
                    r"\s*(rgb[a]?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px",
                    _ly)
                if m:
                    _layers.append({"color": m.group(1), "offsetX": m.group(2) + "px",
                                    "offsetY": m.group(3) + "px", "blur": m.group(4) + "px",
                                    "spread": m.group(5) + "px"})
            if _layers:
                SPEC["light"].setdefault("shadow", {})[_cname.replace("-", "_").split("_")[0] or "panel"] = {
                    "type": "shadow", "value": _layers,
                    "source": f"computed boxShadow of {_cname} default (raw/components-computed.json)",
                    "description": f"The {_cname}'s drop shadow."}
            break
    except KeyError:
        continue


# ------------------------------------------------------------- radii, type
# Every radius below is measured on the component named; Webflow declares
# no radius variables of its own.
rad = SPEC["core"].setdefault("radius", {})
for key, cname, desc in [
    ("button", "hero-cta", "Primary buttons (the large 12px corner)."),
    ("card", "plan-card", "Plan-card corners."),
    ("band", "cta-band", "The closing CTA band's pill-like corner."),
    ("field", "newsletter-field", "Rounded inputs (newsletter)."),
    ("accordion", "feature-accordion", "Feature/FAQ accordion corners."),
    ("testimonial", "testimonial-card", "Testimonial card corners."),
    ("control", "signin-button", "The app surface's control corner (declared --ui-button-radius = 10px)."),
]:
    try:
        v = stprop(cname, "default", "borderTopLeftRadius")
        if v:
            rad[key] = {"type": "dimension", "value": v,
                        "source": f"computed borderTopLeftRadius of {cname} default (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# The app surface's declared --ui-* roles, promoted where the sign-in card
# paints them (raw/css-vars.json, surface app).
for key, var, desc in [
    ("ui.radiusButton", "--ui-button-radius", "declared 10px — the sign-in button paints it"),
    ("ui.radiusInput", "--ui-input-border-radius", "declared 10px — the inputs paint it"),
    ("ui.heightInput", "--ui-input-height", "declared 44px — the email/password inputs paint it"),
    ("ui.heightButton", "--ui-button-min-height", "declared 44px — the sign-in buttons paint it"),
]:
    v = R["app"].get(var)
    if v:
        node = SPEC["component"]
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"declared {var} on app.homerun.co (raw/css-vars.json)",
                           "description": desc}
for key, var, comp, desc in [
    ("ui.fieldBg", "--ui-input-bg", "signin-email", "the input fill, declared #f5f3ef — the fields paint it"),
    ("ui.textDefault", "--ui-color-text-default", "signin-sso", "the default app ink, declared #4a3e3e"),
    ("ui.textHeading", "--ui-color-text-heading", "signin-email", "the app heading ink, declared #2d2323"),
]:
    v = R["app"].get(var)
    if not v:
        continue
    try:
        painted = norm_color(stprop(comp, "default", "color" if "text" in key else "backgroundColor"))
    except KeyError:
        painted = ""
    leaf = {"type": "color", "description": desc,
            "source": f"declared {var} on app.homerun.co (raw/css-vars.json)" + (f"; the {comp} paints {painted}" if painted else "")}
    val = norm_color(v)
    leaf["value"] = "{%s}" % BY_VALUE[val] if val in BY_VALUE else val
    node = SPEC["component"].setdefault("ui", {})
    node[key.split(".")[-1]] = leaf

# Type: GT America is the UI face (measured on buttons, nav, body), GT
# Walsheim the display face (measured on hero/section titles); the careers
# site paints GTAmerica-Regular and Inter in the apply wizard.
font = SPEC["core"].setdefault("font", {})
for key, cname, prop, desc in [
    ("family.sans", "hero-sub", "fontFamily", "The UI face — GT America (Grilli Type, self-hosted CDN webfont), measured on body/nav/button text."),
    ("family.display", "hero-title", "fontFamily", "The display face — GT Walsheim (measured on the hero and section titles, weight 900)."),
    ("family.app", "signin-button", "fontFamily", "The sign-in surface's stack — the same GT America (named GT-America in the app bundle)."),
    ("family.careers", "careers-all-jobs", "fontFamily", "The careers site's face (GTAmerica-Regular)."),
    ("family.apply", "apply-field", "fontFamily", "The application wizard's face — Inter."),
]:
    try:
        f = (stprop(cname, "default", prop) or "").strip()
        if f:
            node = font.setdefault("family", {})
            node[key.split(".")[-1]] = {"type": "fontFamily", "value": f,
                                        "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass
for key, cname, desc in [
    ("size.hero", "hero-title", "The hero display headline at 1440px."),
    ("size.h2", "section-h2", "Section headings."),
    ("size.heroSub", "hero-sub", "The hero subline."),
    ("size.body", "page-ground", "Body/UI base."),
    ("size.nav", "nav-link", "Nav labels and nav buttons."),
    ("size.cta", "hero-cta", "The large primary CTA label."),
    ("size.faq", "faq-item", "The pricing FAQ question."),
    ("size.footer", "footer-link", "Footer links."),
    ("size.mHero", "m-hero", "The hero headline at 390px."),
]:
    try:
        sz = stprop(cname, "default", "textStyle.fontSize") or stprop(cname, "default", "fontSize")
        if sz:
            font.setdefault("size", {})[key.split(".")[-1]] = {"type": "dimension", "value": sz,
                                        "source": f"computed fontSize of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass
for key, cname, desc in [
    ("display", "hero-title", "Display headlines (GT Walsheim 900)."),
]:
    try:
        w = stprop(cname, "default", "fontWeight")
        if w:
            font.setdefault("weight", {})[key] = {"type": "fontWeight", "value": int(w),
                                        "source": f"computed fontWeight of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except (KeyError, ValueError):
        pass

# ---------------------------------------------------------------- component
comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-trial", "default", "height", "The nav Start-free-trial button."),
    ("control.heightHeroCta", "hero-cta", "default", "height", "The large hero CTA."),
    ("control.heightField", "newsletter-field", "default", "height", "The newsletter input."),
    ("control.heightStepper", "plan-stepper-plus", "default", "height", "The pricing job-slot stepper icon."),
    ("control.heightSso", "signin-sso", "default", "height", "The sign-in SSO button."),
    ("control.widthField", "signin-email", "default", "width", "The sign-in email input at 1440px."),
    ("nav.height", "header", "default", "height", "The sticky top nav at 1440px."),
    ("nav.panelWidth", "nav-resources-panel", "default", "width", "The open Resources mega-panel."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("menu.height", "m-menu-open", "default", "height", "The opened mobile menu sheet at 390px."),
    ("heroTitle.width", "hero-title", "default", "width", "The hero headline's measure at 1440px."),
    ("planCard.width", "plan-card", "default", "width", "A pricing plan card."),
    ("jobCard.width", "careers-job-card", "default", "width", "A careers job row at 1440px."),
]:
    try:
        v = stprop(cname, state, prop)
        if not v:
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# Motion: the two durations the measured chrome actually transitions with.
for key, cname, state, prop in [
    ("normal", "hero-cta", "default", "transitionDuration"),
    ("fast", "nav-link", "default", "transitionDuration"),
]:
    try:
        v = stprop(cname, state, prop)
        if v and v != "0s":
            SPEC["core"].setdefault("motion", {}).setdefault("duration", {})[key] = {
                "type": "duration", "value": v,
                "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                "description": f"Transition duration on the {cname}."}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
