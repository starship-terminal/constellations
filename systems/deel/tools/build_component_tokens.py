#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

deel.com is a Next.js + MUI + Tailwind marketing site (the app lives
behind app.deel.com and was never reached). Its stylesheets resolve only
six :root vars (--font-inter, --font-bagoss-condensed/standard/extended,
--swiper-theme-color) — the design itself is Tailwind utilities plus MUI
emotion classes, so every leaf below is a measured computed style from
raw/components-computed.json.

What was measured (desktop 1440x900 unless noted):

  #1b1b1b   the near-black ink — primary button fills, nav text, promo strip
  #201547   the deep purple hero panel behind the home h1 and action tiles
  #141414   the near-black video card inside the reviews band
  #ffffff   white — nav field, price cards, hero/demo button fills
  rgba(0,0,0,.87)  MUI's standard body text on white
  #faf4ee   the latte/cream — footer column headings, FAQ hairline at 16-40%
  #4e4e4e / #3f3f3f   muted grey text / pressed button fill
  #b1d8fc   the sky-blue promo chip and price-card accent strip
  oklab white @0.04/@0.1   the hero tiles' glass fill and hairline on purple

  Typography: Inter for UI/body (16px/400 body, 18px/600 CTAs, 14px/600
  tiles), BagossStandardVF for the small pill buttons and nav (14-15px/500),
  BagossCondensedFont for every display heading (hero 60px/500, section
  44px, about display 160px/600).

The page paints ONE theme: a white field with a #1b1b1b promo strip, a
#201547 purple hero and dark video cards. There is no theme switch; the
export keeps `dark` empty and the dark regions are recorded as surfaces
inside the single theme.
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
    "deel.com is a single-theme Next.js + MUI marketing site: a white "
    "field, a #1b1b1b promo strip, a #201547 purple hero and a sky-blue "
    "accent chip. It declares only font-family vars on :root, so every "
    "design value is a measured computed style."),
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
fam["sans"] = lit('"Inter", sans-serif', "fontFamily",
    "computed fontFamily of promo-banner, hero-demo, price-card, footer-link (raw/components-computed.json); --font-inter on :root (raw/css-vars.json)",
    "Inter — body copy, CTAs, tiles, footer links and every form control.")
fam["brand"] = lit('"BagossStandardVF", sans-serif', "fontFamily",
    "computed fontFamily of nav-link, nav-demo, price-cta, promo-cta (raw/components-computed.json); --font-bagoss-standard on :root (raw/css-vars.json)",
    "Bagoss Standard VF — the nav items and small pill buttons.")
fam["display"] = lit('"BagossCondensedFont", sans-serif', "fontFamily",
    "computed fontFamily of hero-h1, section-heading, price-h1, about-h1, footer-heading (raw/components-computed.json); --font-bagoss-condensed on :root (raw/css-vars.json)",
    "Bagoss Condensed — every display heading, hero 60px to about 160px.")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, val, src_c, desc in [
    ("normal", "400", "footer-link", "400 — body copy and footer links (Inter)."),
    ("medium", "500", "nav-link", "500 — nav items, pill buttons, every display heading."),
    ("semibold", "600", "hero-demo", "600 — CTAs, hero tiles, the about display heading."),
]:
    try:
        weights[key] = lit(st(src_c, "default")["fontWeight"], "fontWeight",
            f"computed fontWeight of {src_c} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

# -------------------------------------------------- measured semantic roles

sem = SPEC["light"]
for key, comp, state, prop, group, desc in [
    ("page", "header-nav", "default", "backgroundColor", "background",
     "The #fff field the nav, price cards and page paint."),
    ("promo-strip", "promo-banner", "default", "color", "background",
     "The #1b1b1b promo strip (painted on the banner's child — see component.promo-strip-paint)."),
    ("ink", "nav-link", "default", "color", "text",
     "The #1b1b1b ink — nav text, pill-button fills, footer links."),
    ("body", "price-card", "default", "color", "text",
     "MUI's rgba(0,0,0,.87) body text on white."),
    ("on-dark", "hero-h1", "default", "color", "text",
     "White text on the #201547 hero panel and dark surfaces."),
    ("cream", "footer-heading", "default", "color", "text",
     "The #faf4ee latte/cream — footer column headings and icon fills."),
    ("focus", "promo-cta", "focus-visible", "outlineColor", "border",
     "The #101010 1px auto focus outline on light controls."),
]:
    try:
        sem.setdefault(group, {})[key] = lit(st(comp, state)[prop], "color",
            f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# purple hero panel + dark video card + promo strip + sky chip are painted
# on children, not the measured roots — read them off the paint lists.
try:
    purple = next(pl["bg"] for pl in C["hero-block"]["states"]["default"]["paint"] if pl.get("bg") == "rgb(32, 21, 71)")
    sem.setdefault("background", {})["hero-panel"] = lit(purple, "color",
        "painted background of the hero panel inside hero-block default (raw/components-computed.json)",
        "The #201547 deep-purple panel behind the home h1 and action tiles.")
except (KeyError, StopIteration):
    pass
try:
    dark = next(pl["bg"] for pl in C["review-band"]["states"]["default"]["paint"] if pl.get("bg") == "rgb(20, 20, 20)")
    sem.setdefault("background", {})["video-card"] = lit(dark, "color",
        "painted background of the video card inside review-band default (raw/components-computed.json)",
        "The #141414 near-black review video card.")
except (KeyError, StopIteration):
    pass
try:
    chip = next(pl["bg"] for pl in C["promo-banner"]["states"]["default"]["paint"] if pl.get("bg") == "rgb(177, 216, 252)")
    sem.setdefault("action", {})["accent-chip"] = lit(chip, "color",
        "painted background of the SPECIAL OFFER chip inside promo-banner default (raw/components-computed.json)",
        "The #b1d8fc sky-blue accent — the promo chip and the price-card top strip.")
except (KeyError, StopIteration):
    pass
try:
    tile_bg = next(pl["bg"] for pl in C["hero-tile"]["states"]["default"]["paint"] if pl.get("bg", "").startswith("oklab"))
    sem.setdefault("background", {})["tile-glass"] = lit(tile_bg, "color",
        "painted oklab background of hero-tile default (raw/components-computed.json)",
        "The 4% white glass fill on the hero action tiles over the purple panel.")
    tile_bd = st("hero-tile", "default")["borderTopColor"]
    sem.setdefault("border", {})["tile-glass"] = lit(tile_bd, "color",
        "computed borderTopColor of hero-tile default (raw/components-computed.json)",
        "The 10% white hairline on the hero action tiles.")
except (KeyError, StopIteration):
    pass
try:
    hairline = st("faq-item", "default")["borderTopColor"]
    sem.setdefault("border", {})["hairline"] = lit(hairline, "color",
        "computed borderTopColor of faq-item default (raw/components-computed.json)",
        "The 1px latte-at-16% hairline the FAQ accordion items separate with.")
except KeyError:
    pass
try:
    pressed = st("promo-cta", "pressed")["backgroundColor"]
    sem.setdefault("action", {})["pressed-fill"] = lit(pressed, "color",
        "computed backgroundColor of promo-cta pressed (raw/components-computed.json)",
        "The #3f3f3f grey the light pill buttons take on hover/pressed.")
except KeyError:
    pass
try:
    hov = st("nav-demo", "hover")["backgroundColor"]
    sem.setdefault("action", {})["hover-fill"] = lit(hov, "color",
        "computed backgroundColor of nav-demo/price-cta hover (raw/components-computed.json)",
        "The #4e4e4e grey the dark #1b1b1b pill buttons lift to on hover/pressed.")
except KeyError:
    pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("chip", "promo-cta", "default", "The 12px promo chip button."),
    ("button", "nav-demo", "default", "The 14px pill-button/nav-demo size."),
    ("nav", "nav-link", "default", "The 15px nav item."),
    ("body", "price-card", "default", "The 16px body/footer-link size."),
    ("cta", "hero-demo", "default", "The 18px hero/section CTA."),
    ("section", "section-heading", "default", "The 44px Bagoss section heading."),
    ("hero", "hero-h1", "default", "The 60px BagossCondensed hero display."),
    ("about-display", "about-h1", "default", "The 160px about-page display numeral."),
]:
    try:
        ty[key] = lit(st(comp, state)["fontSize"], "fontSize",
            f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("body", "price-card", "default", "The 24px body line-height."),
    ("hero", "hero-h1", "default", "The 63px hero display line-height (1.05x)."),
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
    ("chip", "promo-banner", "default", "_chip", "The 2px SPECIAL OFFER chip radius."),
    ("card", "price-card", "default", "borderTopLeftRadius", "The 12px card/tile radius."),
    ("pill", "nav-demo", "default", "borderTopLeftRadius", "The 200px small-pill radius (nav CTAs, promo button)."),
    ("full", "hero-demo", "default", "borderTopLeftRadius", "The rounded-full on hero CTAs — computed as a huge px value (Tailwind !rounded-full)."),
    ("circle", "m-hamburger", "default", "borderTopLeftRadius", "The 50% icon-button circle."),
]:
    try:
        if prop == "_chip":
            chip_r = next(pl["radius"] for pl in C[comp]["states"][state]["paint"] if pl.get("bg") == "rgb(177, 216, 252)")
            radii[key] = lit(chip_r, "dimension",
                f"painted radius of the SPECIAL OFFER chip inside {comp} {state} (raw/components-computed.json)", desc)
        else:
            v = st(comp, state)[prop]
            ty_ = "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other"
            radii[key] = lit(v, ty_,
                f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, StopIteration):
        pass

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
try:
    sh["card"] = lit(st("price-card", "default")["boxShadow"], "other",
        "computed boxShadow of price-card default (raw/components-computed.json)",
        "The MUI elevation-2dp shadow the pricing tier cards carry.")
except KeyError:
    pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("promo-cta", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["hover"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of promo-cta default (raw/components-computed.json)",
            "The 0.1s ease-in-out all-transition the pill buttons run on hover/press.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("promo-banner-height", "promo-banner", "default", "h", "dimension", "The 64px promo strip."),
    ("nav-height", "header-nav", "default", "h", "dimension", "The 80px sticky nav."),
    ("logo-width", "nav-logo", "default", "w", "dimension", "The 78px Deel wordmark."),
    ("nav-item-height", "nav-link", "default", "h", "dimension", "The 40px nav-item hit area."),
    ("nav-demo-height", "nav-demo", "default", "h", "dimension", "The 40px nav Book-a-demo pill."),
    ("promo-cta-height", "promo-cta", "default", "h", "dimension", "The 32px Claim-offer button."),
    ("hero-panel-height", "hero-block", "default", "h", "dimension", "The 732px purple hero block."),
    ("hero-h1-width", "hero-h1", "default", "w", "dimension", "The ~575px hero heading column."),
    ("hero-tile-size", "hero-tile", "default", "h", "dimension", "The 80px hero action tile (181px wide)."),
    ("hero-demo-width", "hero-demo", "default", "w", "dimension", "The 375px hero Book-a-demo pill."),
    ("product-card-size", "product-card", "default", "h", "dimension", "The 438px-tall product card (419px wide)."),
    ("price-card-size", "price-card", "default", "h", "dimension", "The 928px pricing tier card (459px wide)."),
    ("faq-item-height", "faq-item", "default", "h", "dimension", "The 80px FAQ accordion summary row."),
    ("review-band-height", "review-band", "default", "h", "dimension", "The 1206px review video-carousel band."),
    ("footer-height", "footer", "default", "h", "dimension", "The 1015px footer block."),
    ("m-nav-height", "m-nav-bar", "default", "h", "dimension", "The 64px mobile nav."),
    ("m-hamburger-size", "m-hamburger", "default", "w", "dimension", "The 40px mobile hamburger circle."),
    ("m-hero-h1", "m-h1", "default", "h", "dimension", "The mobile hero heading at 38px."),
]:
    try:
        s_ = C[cname]["states"][state]
        v = s_["rect"][prop] if prop in ("w", "h") else s_["style"][prop]
        if v and v not in ("0px", "auto", "rgba(0, 0, 0, 0)"):
            comp[name] = lit(v, ty_,
                f"computed {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# the promo strip's own fill (the banner root reports colour, not bg)
try:
    strip = next(pl["bg"] for pl in C["promo-banner"]["states"]["default"]["paint"] if pl.get("bg") == "rgb(27, 27, 27)")
    comp["promo-strip-paint"] = lit(strip, "color",
        "painted background of the promo-banner MuiBox child (raw/components-computed.json)",
        "The #1b1b1b fill the 64px promo strip paints.")
except (KeyError, StopIteration):
    pass

# measured state moves on the interactive controls; a state that failed to
# capture (an 'error' entry, no 'style') is skipped, not allowed to drop the rest
for name, cname, desc in [
    ("pill-light-track", "promo-cta",
     "Light pill (Claim offer): #fff fill/#1b1b1b text at rest; hover+pressed invert to #3f3f3f fill/#fff text; focus shows the 1px auto outline."),
    ("pill-dark-track", "nav-demo",
     "Dark pill (nav Book a demo): #1b1b1b fill/#fff text at rest; tracks across hover/pressed."),
    ("nav-link-state-track", "nav-link",
     "Nav item: #1b1b1b Bagoss text at rest; tracks across hover/pressed/focus."),
    ("tile-state-track", "hero-tile",
     "Hero tile: 4%-white glass at rest on the purple panel; tracks across hover/pressed/focus."),
    ("faq-state-track", "faq-item",
     "FAQ accordion summary: MUI MuiAccordionSummary at rest and opened via its own click toggle."),
]:
    try:
        states = {s2: {p: C[cname]["states"][s2]["style"][p] for p in ("backgroundColor", "color", "transform", "outlineStyle") if C[cname]["states"][s2]["style"].get(p)}
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
        f"{st('promo-cta', 'focus-visible')['outlineStyle']} {st('promo-cta', 'focus-visible')['outlineColor']}",
        "other",
        "computed outline of promo-cta/nav controls focus-visible (raw/components-computed.json)",
        "The browser's 1px auto outline in #101010/own colour — no custom focus ring is painted.")
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
