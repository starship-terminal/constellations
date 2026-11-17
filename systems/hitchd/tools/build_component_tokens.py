#!/usr/bin/env python3
"""Build raw/component-tokens.json — the token tree build_tokens.py turns
into tokens.json.

hitchd.com declares almost no custom properties (~10 radio-control display
flags in the guest registry app — see raw/css-vars.json), so the token layer
is measured: every leaf below is a computed style or a bounding-box reading
taken from a real element on a signed-out public page, labelled with the
measurement it came from. Nothing here is invented; a component the capture
could not measure simply produces no token.

Shape: SPEC["core"] holds the theme-independent layer (palette, type, radius,
spacing, shadow, grid, measured component geometry), SPEC["light"] the
colour roles every public page paints (Hitchd ships one light theme — no
dark variant or theme control exists anywhere, so there is no dark set).
Measured role values that equal a palette colour alias to `{palette.<n>}`;
the palette itself carries the first measurement that produced each colour.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]
V = json.loads((RAW / "css-vars.json").read_text())
FONTS = V.get("fonts", [])

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. hitchd.com "
    "declares almost no custom properties, so the layer is measured: every "
    "value is a computed style or bounding-box reading from a signed-out "
    "public page (raw/components-computed.json), with the measurement named "
    "in each leaf's source. One light theme exists; no dark variant or "
    "theme control was found on any surface, so no dark set ships."),
    "core": {}, "light": {}, "component": {}}


def st(comp, part):
    return C[comp]["states"][part]["style"]


def rc(comp, part, key):
    return C[comp]["states"][part]["rect"][key]


def ts(comp, part, prop):
    """The first text node's reading (textStyle) when the kit recorded one."""
    c = C[comp]["states"][part]
    t = c.get("textStyle") or {}
    return t.get(prop) or c["style"].get(prop)


def have(comp, part, prop=None):
    try:
        s = st(comp, part)
        return prop is None or bool((s.get(prop) or "").strip())
    except (KeyError, TypeError):
        return False


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),?\s+([\d.]+),?\s+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, a = m.groups()
        a = 1 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        if a >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    return v


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


def put(node, path, leaf):
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def M(comp, part, prop):
    return f"computed {prop} of {comp} {part} (raw/components-computed.json)"


def R(comp, part, key):
    return f"measured rect {key} of {comp} {part} (raw/components-computed.json)"


# ---------------------------------------------------------------- palette
# name -> (component, part, css prop, description). Values are read from the
# measurement file, so an element that was not captured yields no token.
def read_prop(comp, part, prop):
    """A prop's measured value: for color, the painted text node's reading
    (textStyle) when the kit recorded one — a wrapper can report a colour its
    visible text overrides; otherwise the element's own computed style."""
    if prop == "color":
        return ts(comp, part, "color")
    return st(comp, part)[prop]


PAL = [
    ("ink", "announcement-banner", "text", "color", "The near-black ink of the closure strip and body copy."),
    ("cream", "announcement-banner", "banner", "backgroundColor", "The warm paper of the closure strip."),
    ("heroInk", "hero", "h1", "color", "The white of the hero display type over the video/photo."),
    ("muted", "auth-link", "muted", "color", "The grey of helper and secondary copy."),
    ("paper", "auth-layout", "page", "backgroundColor", "The page field behind the auth card and content."),
    ("fieldLine", "auth-field", "input", "borderTopColor", "The input border grey."),
    ("disabled", "auth-button", "button", "backgroundColor", "The disabled Continue fill."),
    ("registryInk", "registry-hero", "heading", "color", "The registry display ink."),
    ("giftPrice", "gift-card", "price", "color", "The gift price colour."),
    ("menuBg", "mobile-menu", "menu", "backgroundColor", "The phone drawer fill."),
]
pal = SPEC["core"].setdefault("palette", {})
for name, comp, part, prop, desc in PAL:
    if have(comp, part, prop):
        put(pal, name, lit(read_prop(comp, part, prop), "color", M(comp, part, prop), desc))

PAL_VAL = {name: norm_color(read_prop(comp, part, prop)) for name, comp, part, prop, _ in PAL if have(comp, part, prop)}


def role(value, ty, src, desc):
    """A measured role: alias to the palette token it matches, else literal."""
    v = norm_color(value) if ty == "color" else value
    for name, pv in PAL_VAL.items():
        if ty == "color" and pv == v:
            return lit("{palette." + name + "}", ty, src + "; matches palette." + name, desc)
    return lit(value, ty, src, desc)


# ---------------------------------------------------------------- light.color
L = SPEC["light"].setdefault("color", {})
# (path, component, part, prop, description) — all measured
ROLES = [
    ("surface.page", "auth-layout", "page", "backgroundColor", "The field every page paints behind content."),
    ("surface.cream", "announcement-banner", "banner", "backgroundColor", "The announcement strip fill."),
    ("surface.modal", "gift-modal", "modal", "backgroundColor", "The gift modal fill."),
    ("surface.menu", "mobile-menu", "menu", "backgroundColor", "The phone menu drawer fill."),
    ("surface.footer", "marketing-footer", "footer", "backgroundColor", "The footer fill."),
    ("text.ink", "announcement-banner", "text", "color", "Primary ink."),
    ("text.muted", "auth-link", "muted", "color", "Secondary and helper copy."),
    ("text.inverse", "hero", "h1", "color", "Type over photography/video."),
    ("text.link", "marketing-footer", "link", "color", "Inline links."),
    ("text.hashtag", "registry-nav", "hashtag", "color", "The registry #hashtag link."),
    ("text.price", "gift-card", "price", "color", "A gift's price."),
    ("text.lead", "hero", "lead", "color", "The hero supporting paragraph."),
    ("border.field", "auth-field", "input", "borderTopColor", "Text field borders."),
    ("action.ctaInk", "registry-nav", "cta", "color", "The 'Try It Free' pill's label ink on the sample banner (the painted desktop link — the hidden phone variant is never measured)."),
    ("action.ctaFill", "registry-nav", "cta", "backgroundColor", "The 'Try It Free' pill's fill."),
    ("action.giveInk", "gift-modal", "give", "color", "The Give button label."),
    ("action.giveFill", "gift-modal", "giveWrap", "backgroundColor", "The Give pill's fill, painted on its .pay wrapper (disabled at rest until an amount exists)."),
    ("action.disabledFill", "auth-button", "button", "backgroundColor", "A disabled submit fill."),
    ("action.disabledInk", "auth-button", "button", "color", "A disabled submit label."),
    ("nav.ink", "marketing-nav", "loginLink", "color", "The Log In link on the hero header."),
    ("nav.bar", "registry-nav", "bar", "backgroundColor", "The registry sample banner fill."),
]
for path, comp, part, prop, desc in ROLES:
    if have(comp, part, prop):
        put(L, path, role(read_prop(comp, part, prop), "color", M(comp, part, prop), desc))

# ---------------------------------------------------------------- type
F = SPEC["core"].setdefault("font", {})
FAM_SRC = "computed fontFamily per element (raw/components-computed.json); faces declared by @font-face rules in raw/css-vars.json"
FAMILY = [
    ("display", "hero", "h1", "The hairline display serif (DDNR) of the hero and marketing display type."),
    ("text", "announcement-banner", "text", "The UI/body face (Inter Variable)."),
    ("auth", "auth-layout", "h1", "The couple app's UI stack."),
    ("registry", "registry-hero", "heading", "The guest registry's display stack."),
    ("article", "article-type", "body", "Longform body copy."),
]
for name, comp, part, desc in FAMILY:
    if have(comp, part):
        put(F, "family." + name, lit(ts(comp, part, "fontFamily"), "fontFamily", f"computed fontFamily of {comp} {part} (raw/components-computed.json)", desc))
SIZES = [
    ("display.hero", "hero", "h1", "The home hero display size."),
    ("display.registry", "registry-hero", "heading", "The registry couple-name size."),
    ("h2", "marketing-h2", "h2", "Marketing section heading."),
    ("h3", "gift-card", "title", "A gift tile title."),
    ("authH1", "auth-layout", "h1", "The auth card heading."),
    ("lead", "hero", "lead", "The hero supporting paragraph."),
    ("body", "article-type", "body", "Longform body."),
    ("ui", "announcement-banner", "text", "UI and strip copy."),
    ("small", "auth-link", "muted", "Helper and footer small copy."),
    ("navLink", "marketing-nav", "loginLink", "Header link size."),
]
for name, comp, part, desc in SIZES:
    if have(comp, part):
        put(F, "size." + name, lit(ts(comp, part, "fontSize"), "dimension", f"computed fontSize of {comp} {part} (raw/components-computed.json)", desc))
HEIGHTS = [
    ("display.hero", "hero", "h1", "The hero display line-height."),
    ("display.registry", "registry-hero", "heading", "The registry display line-height."),
    ("h2", "marketing-h2", "h2", "Section heading line-height."),
    ("authH1", "auth-layout", "h1", "Auth heading line-height."),
    ("lead", "hero", "lead", "Hero paragraph line-height."),
    ("body", "article-type", "body", "Longform line-height."),
    ("ui", "announcement-banner", "text", "UI copy line-height."),
]
for name, comp, part, desc in HEIGHTS:
    if have(comp, part):
        v = ts(comp, part, "lineHeight")
        ty = "dimension" if re.fullmatch(r"-?\d+(\.\d+)?px", v or "") else "number"
        put(F, "height." + name, lit(v, ty, f"computed lineHeight of {comp} {part} (raw/components-computed.json)", desc))
WEIGHTS = [
    ("display", "hero", "h1", "The hairline display weight."),
    ("registry", "registry-hero", "heading", "The registry display weight."),
    ("h2", "marketing-h2", "h2", "Section heading weight."),
    ("authH1", "auth-layout", "h1", "Auth heading weight."),
    ("body", "article-type", "body", "Body weight."),
    ("link", "marketing-nav", "loginLink", "Header link weight."),
    ("button", "auth-button", "button", "Button label weight."),
]
for name, comp, part, desc in WEIGHTS:
    if have(comp, part):
        put(F, "weight." + name, lit(ts(comp, part, "fontWeight"), "fontWeight", f"computed fontWeight of {comp} {part} (raw/components-computed.json)", desc))
TRACK = [
    ("display", "hero", "h1", "Hero display tracking."),
    ("button", "auth-button", "button", "Button label tracking."),
]
for name, comp, part, desc in TRACK:
    if have(comp, part):
        v = ts(comp, part, "letterSpacing")
        if v and v != "normal":
            put(F, "tracking." + name, lit(v, "dimension", f"computed letterSpacing of {comp} {part} (raw/components-computed.json)", desc))

# ---------------------------------------------------------------- radius / shadow / spacing / border
RAD = [
    ("field", "auth-field", "input", "borderTopLeftRadius", "Text field corners."),
    ("pill", "auth-button", "button", "borderTopLeftRadius", "The auth submit pill."),
    ("card", "gift-card", "card", "borderTopLeftRadius", "Gift tile corners."),
    ("modal", "gift-modal", "modal", "borderTopLeftRadius", "The gift modal corners."),
    ("cta", "registry-nav", "cta", "borderTopLeftRadius", "The Try It Free pill's corners."),
    ("give", "gift-modal", "give", "borderTopLeftRadius", "The Give pill's corners."),
]
for name, comp, part, prop, desc in RAD:
    if have(comp, part, prop):
        put(SPEC["core"], "radius." + name, lit(st(comp, part)[prop], "dimension", M(comp, part, prop), desc))

def parse_shadow(css):
    """'rgb(r,g,b) 0px 4px 8px 0px[, ...]' -> DTCG shadow layers.

    Only outer shadows are kept (an inset layer is dropped, an inset-only
    shadow yields no token) — DTCG shadow leaves have no inset field.
    """
    layers = []
    for part in re.split(r",\s*(?![^(]*\))", css or ""):
        if re.search(r"\binset\b", part):
            continue
        nums = re.findall(r"-?\d+(?:\.\d+)?px", part)
        col = re.search(r"(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})", part)
        if len(nums) < 2 or not col:
            continue
        x, y, blur, spread = (nums + ["0px", "0px"])[:4]
        layers.append({"color": norm_color(col.group(0)), "offsetX": x, "offsetY": y, "blur": blur, "spread": spread})
    return layers or None


SH = [
    ("card", "gift-card", "card", "The gift tile shadow."),
    ("modal", "gift-modal", "modal", "The gift modal shadow."),
    ("header", "marketing-nav", "header", "The header's elevation."),
]
for name, comp, part, desc in SH:
    if have(comp, part, "boxShadow") and st(comp, part)["boxShadow"] != "none":
        layers = parse_shadow(st(comp, part)["boxShadow"])
        if layers:
            put(SPEC["core"], "shadow." + name, lit(layers, "shadow", M(comp, part, "boxShadow"), desc))

SPACE = [
    ("strip.y", "announcement-banner", "banner", "paddingTop", "The announcement strip's vertical padding."),
    ("field.x", "auth-field", "input", "paddingLeft", "Text field side padding."),
    ("button.x", "auth-button", "button", "paddingLeft", "Submit button side padding."),
    ("card.pad", "gift-card", "card", "paddingTop", "Gift tile padding."),
    ("modal.pad", "gift-modal", "modal", "paddingTop", "Gift modal padding."),
]
for name, comp, part, prop, desc in SPACE:
    if have(comp, part, prop):
        put(SPEC["core"], "spacing." + name, lit(st(comp, part)[prop], "dimension", M(comp, part, prop), desc))

BORD = [
    ("field", "auth-field", "input", "The 1px field border."),
]
for name, comp, part, desc in BORD:
    if have(comp, part, "borderTopWidth") and float(st(comp, part)["borderTopWidth"].replace("px", "") or 0) > 0:
        s = st(comp, part)
        put(SPEC["core"], "border." + name, lit({"color": norm_color(s["borderTopColor"]), "width": s["borderTopWidth"], "style": s["borderTopStyle"]}, "border", M(comp, part, "borderTopWidth/style/color"), desc))

# ---------------------------------------------------------------- component geometry
comp = SPEC["component"]
GEOM = [
    ("closure-header-height", "marketing-nav", "header", "h", "The closure header bar height."),
    ("announcement-height", "announcement-banner", "banner", "h", "The closure announcement strip height."),
    ("auth-card-width", "auth-layout", "card", "w", "The auth form card width."),
    ("field-height", "auth-field", "input", "h", "Auth text field height."),
    ("field-width", "auth-field", "input", "w", "Auth text field width."),
    ("button-height", "auth-button", "button", "h", "Auth submit button height."),
    ("login-link-height", "marketing-nav", "loginLink", "h", "The header Log In hit height."),
    ("gift-card-width", "gift-card", "card", "w", "A gift tile width at 1440."),
    ("gift-card-height", "gift-card", "card", "h", "A gift tile height at 1440."),
    ("modal-width", "gift-modal", "modal", "w", "The gift modal width."),
    ("registry-banner-height", "registry-nav", "bar", "h", "The registry sample banner height."),
    ("mobile-menu-height", "mobile-menu", "menu", "h", "The phone menu drawer height."),
    ("mobile-gift-card-width", "mobile-gift-card", "card", "w", "A gift tile width at 390."),
]
for name, cname, part, key, desc in GEOM:
    try:
        v = rc(cname, part, key)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         "dimension", R(cname, part, key), desc)
    except (KeyError, TypeError):
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "type" not in d else (1 if isinstance(d, dict) else 0)


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
missing = [c for c in ("marketing-nav", "registry-nav", "gift-card", "gift-modal", "auth-field", "auth-button") if c not in C]
if missing:
    print("note: no measurements for", ", ".join(missing))
