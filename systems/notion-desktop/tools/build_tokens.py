#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Notion 7.40.0 for macOS (Electron 44.9.1) on 2026-10-25 over the remote-debugging
port (tools/capture/electron/):
  raw/css-vars.<theme>.json      every custom property the tab's stylesheets declare, by sheet, selector and
                                 condition, and each name as it computes on <body> and paints on a probe
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)

How Notion's colours work, and so how this file is laid out. Notion's web app (the desktop app loads
app.notion.com in each tab) declares its theme as about 760 custom properties: `:root, .notion-light-theme`
holds the light values and `.notion-dark-theme` (on <body> and the app root) overrides them for dark. Names
are camelCase abbreviations behind a prefix that says how the value is written (--c- an opaque hex, --ca-
one with alpha, --cl- and --cd- values tuned for one theme): --c-texPri is the primary text colour,
--c-bluBacAccPri the blue accent background, --c-shaOutMd a medium outlined shadow. This builder expands the
abbreviations into words (ABBR) and files each name into a group: the neutral roles (text, icon, border, bg),
the ten hue families (blue.text-primary ...), the palette steps, shadows, and everything else under misc.
Every token keeps the CSS name it came from in $extensions.css. role.* maps the checklist roles onto those;
component.* holds measured component values, aliased to a token whenever the painted value matches.

Notion declares no type, spacing, radius or size scale as custom properties: its components set those inline.
Those groups in core are measured from computed styles of named parts (raw/components.*.json) and say which.

Every token carries $extensions.source = {evidence, from}. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import color, is_color, ms, px, shadow, split_top  # noqa: E402
from prefer import skip  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = PKG / "raw"
THEMES = ["light", "dark"]
DATE = "2026-10-25"

# ---------------------------------------------------------------- PRODUCT (adapt): what the readings are

THEME_NAME = {"light": "Light (Settings > Preferences > Theme: Light)",
              "dark": "Dark (Settings > Preferences > Theme: Dark)"}
# Notion's three-letter abbreviations, as words. A segment not listed stays as it is.
ABBR = {
    "tex": "text", "ico": "icon", "bor": "border", "bac": "bg", "pri": "primary", "sec": "secondary", "ter": "tertiary",
    "dis": "disabled", "acc": "accent", "inv": "inverse", "str": "strong", "ele": "elevated", "int": "interactive",
    "tra": "translucent", "hov": "hover", "pre": "pressed", "sel": "selected", "sha": "shadow", "out": "outline",
    "bas": "base", "dif": "diffuse", "scr": "screen", "col": "color", "foc": "focus", "rin": "ring", "but": "button",
    "inp": "input", "pop": "popover", "sid": "sidebar", "ite": "item", "top": "topbar", "pag": "page", "tit": "title",
    "pla": "placeholder", "pil": "pill", "men": "menu", "tab": "table", "row": "row", "hea": "header", "cod": "code",
    "blo": "block", "cal": "calendar", "eve": "event", "car": "card", "hom": "home", "emb": "embed", "gla": "glass",
    "was": "wash", "ove": "overlay", "smo": "smoke", "mod": "modal", "und": "underlay", "whi": "white", "bla": "black",
    "blu": "blue", "bro": "brown", "gra": "gray", "gre": "green", "ora": "orange", "pin": "pink", "pur": "purple",
    "red": "red", "yel": "yellow", "tea": "teal", "pal": "palette", "ava": "avatar", "use": "user", "ui": "ui",
    "lin": "line", "dec": "decoration", "opa": "opaque", "reg": "regular", "emo": "emoji", "fav": "favorite",
    "boa": "board", "def": "default", "gal": "gallery", "fro": "frozen", "fil": "filled", "div": "divider",
    "key": "keyboard", "don": "done", "bar": "bar", "act": "action", "ass": "assistant", "cor": "corner",
    "lig": "light", "gro": "group", "tim": "timeline", "pee": "peek", "dar": "dark", "ban": "banner", "bei": "beige",
    "box": "box", "bot": "bottom", "sta": "state", "swi": "switch", "tog": "toggle", "des": "destructive",
    "fin": "find", "hig": "highlight", "mat": "match", "uns": "unselected", "mar": "marker", "edi": "edit",
    "ill": "illustration", "vie": "view", "all": "all", "dro": "dropdown", "cha": "chat", "ai": "ai", "con": "content",
    "til": "tile", "cov": "cover", "pho": "photo", "tem": "template", "emp": "empty", "joi": "join", "ind": "indicator",
    "per": "person", "sit": "site", "chr": "chrome", "win": "window", "seo": "seo", "bui": "builder", "ins": "insert",
    "ste": "step", "sus": "suspended", "idl": "idle", "inn": "inner", "equ": "equation", "tok": "token",
    "pap": "paper", "wax": "wax", "res": "resize", "cre": "credit", "pro": "promo", "rev": "review", "thi": "thick",
    "sti": "sticky", "and": "and", "in": "in", "sm": "sm", "md": "md", "lg": "lg", "bg": "bg", "var": "variant",
}
HUES = ["blu", "bro", "gra", "gre", "ora", "pin", "pur", "red", "yel", "tea"]
ROLE_GROUPS = {"tex": "text", "ico": "icon", "bor": "border", "bac": "bg"}


def words(abbr):
    """`bluBacAccPri` -> ['blue', 'bg', 'accent', 'primary']; digits stay whole (`palUiBlu700` -> ... 'blue', '700')."""
    out = []
    for seg in re.findall(r"[A-Z]{2,}(?=[A-Z][a-z]|\d|$)|[A-Z]?[a-z]+|\d+", abbr):
        out.append(ABBR.get(seg.lower(), seg.lower()))
    return out


def path_of(name):
    """A Notion custom property -> (group, key)."""
    m = re.fullmatch(r"--c[adl]?-(\w+)", name)
    if not m:
        raise KeyError(name)
    raw = m.group(1)
    segs = re.findall(r"[A-Z]{2,}(?=[A-Z][a-z]|\d|$)|[A-Z]?[a-z]+|\d+", raw)
    first = segs[0].lower()
    w = words(raw)
    if first == "pal":
        return ("palette", "-".join(w[1:]))
    if first in ROLE_GROUPS and len(segs) > 1:
        return (ROLE_GROUPS[first], "-".join(w[1:]))
    if first in HUES and len(segs) > 1 and segs[1].lower() in ROLE_GROUPS:
        return (ABBR[first], "-".join(w[1:]))
    if first == "sha":
        return ("shadow", "-".join(w[1:]))
    return ("misc", "-".join(w))


def load(name):
    return json.loads((RAW / name).read_text())


V = {t: load(f"css-vars.{t}.json") for t in THEMES}
C = {t: load(f"components.{t}.json") for t in THEMES}

# ---------------------------------------------------------------- helpers


def tok(value, ty, evidence, where, **ext):
    t = {"$value": value, "$type": ty, "$extensions": {"source": {"evidence": evidence, "from": where}}}
    t["$extensions"].update({k: v for k, v in ext.items() if v is not None})
    return t


def put(tree, path, t):
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    node[path[-1]] = t


def get(tree, path):
    node = tree
    for k in path.split("."):
        if not isinstance(node, dict) or k not in node:
            return None
        node = node[k]
    return node


def computed(t):
    return V[t]["computed"]["body"]


def declared(t, name):
    """The declaration that sets `name` in theme t: the dark rule in dark when there is one, else :root's."""
    ds = [d for d in V[t]["decls"] if d["name"] == name]
    dark = [d for d in ds if "notion-dark-theme" in d["selector"]]
    light = [d for d in ds if "notion-light-theme" in d["selector"] or d["selector"].startswith(":root")]
    pick = (dark if t == "dark" and dark else light) or ds
    return pick[-1] if pick else None


def where(t, name):
    d = declared(t, name)
    sel = d["selector"] if d else "?"
    return f"{name} on <body> ({sel}), {THEME_NAME[t]}, {DATE}"


def is_shadow(v):
    try:
        layers = shadow(v)
        return bool(layers) and all(re.fullmatch(r"-?[\d.]+px", l["blur"]) for l in layers)
    except ValueError:
        return False


# ---------------------------------------------------------------- semantic sets: every colour and shadow, per theme

SETS = {t: {} for t in THEMES}
SKIPPED = {t: [] for t in THEMES}
for t in THEMES:
    comp, painted = computed(t), V[t]["colors"]
    owner = {}   # token path -> the custom property that took it
    for n in sorted(comp):
        if not re.match(r"--c[adl]?-", n):
            continue
        v = comp[n]
        try:
            group, key = path_of(n)
        except KeyError:
            continue
        # Two properties that shorten to the same path (--c-x and --ca-x, say) would silently overwrite each other.
        if owner.setdefault((group, key), n) != n:
            raise SystemExit(f"{t}: {n} and {owner[(group, key)]} both map to {group}.{key}; extend path_of or ABBR")
        if n in painted and is_color(painted[n]) and is_color(v):
            put(SETS[t], (group, key), tok(color(painted[n]), "color", "Measured", where(t, n), css=n))
        elif is_shadow(v):
            put(SETS[t], ("shadow" if group == "shadow" else "shadow", key if group == "shadow" else "-".join(words(n[n.index("-", 2) + 1:]))),
                tok(shadow(v), "shadow", "Measured", where(t, n), css=n, declared=v))
        else:
            SKIPPED[t].append({"name": n, "value": v[:120], "why": "not a colour or a box-shadow (a gradient or a keyword)"})


def resolve(t, value, depth=0):
    m = re.fullmatch(r"\{([^{}]+)\}", value) if isinstance(value, str) else None
    if not m or depth > 20:
        return value
    node = get(SETS[t], m.group(1)) or get(CORE, m.group(1))
    if node is None:
        raise KeyError(f"{t}: {value} points at nothing")
    return resolve(t, node["$value"], depth + 1)


# ---------------------------------------------------------------- core: measured scales


def parts(t):
    """{(part, state): (shot, style)} from the first shot that measured it."""
    out = {}
    for shot, d in C[t].items():
        for part, v in d["parts"].items():
            if "style" in v and not skip(shot, part, d["state"]):
                out.setdefault((part, d["state"]), (shot, v["style"]))
    return out


P = {t: parts(t) for t in THEMES}


def style(t, part, state="default"):
    hit = P[t].get((part, state))
    if not hit and state == "default":
        hit = next((v for (p, s), v in sorted(P[t].items()) if p == part), None)
    return hit if hit else (None, None)


CORE = {}
FAMILY = "dark"


def stack(v):
    return [f.strip().strip("'\"") for f in split_top(v)]


# Families, from the computed font-family of the page's text and of inline code.
for key, part in (("sans", "paragraph"), ("serif", None), ("mono", "inline-code")):
    if not part:
        continue
    shot, s = style(FAMILY, part)
    if s:
        put(CORE, ("fontFamily", key), tok(stack(s["font-family"]), "fontFamily", "Measured", f"computed font-family of {part} in {shot}, dark, {DATE}"))

# PRODUCT (adapt): type roles, measured on real elements.
ROLES = [("page-title", "page-title", "Page titles (the h1 of a page)"),
         ("heading-1", "heading-1", "Heading 1 blocks"),
         ("heading-2", "heading-2", "Heading 2 blocks"),
         ("heading-3", "heading-3", "Heading 3 blocks"),
         ("body", "paragraph", "Text blocks"),
         ("sidebar", "page-row-selected-fill", "Sidebar page rows"),
         ("section", "section-label", "Sidebar section labels (Favorites, Private, Teamspaces)"),
         ("menu", "menu-row", "Menu rows"),
         ("button", "button-new", "Button labels"),
         ("caption", "tooltip", "Tooltips"),
         ("table", "table-cell", "Database table cells"),
         ("settings-title", "settings-page-title", "Settings pane titles"),
         ("code", "code", "Code blocks"),
         ("inline-code", "inline-code", "Inline code")]
SIZES_SEEN = {}
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s or not s["font-size"].endswith("px"):
        continue
    fam = "{fontFamily.mono}" if "code" in role and get(CORE, "fontFamily.mono") else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(float(s["font-weight"])),
           "lineHeight": px(lh) if lh.endswith("px") else px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 2)),
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}",
        note=None if lh.endswith("px") else "computed line-height is normal; 1.2 x the size is used here"))
    SIZES_SEEN.setdefault(px(s["font-size"]), (part, shot))
for v, (part, shot) in sorted(SIZES_SEEN.items(), key=lambda kv: float(kv[0][:-2])):
    put(CORE, ("fontSize", v.replace("px", "").replace(".", "-")), tok(v, "dimension", "Measured", f"font-size of {part} in {shot}, dark, {DATE}"))
for w in sorted({int(float(s["font-weight"])) for (_, _), (_, s) in P["dark"].items()}):
    put(CORE, ("fontWeight", str(w)), tok(w, "fontWeight", "Measured", f"a font-weight seen on the captured parts (computed), {DATE}"))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    v = (s or {}).get(prop, "")
    return (shot, v) if v.endswith("px") else (None, None)


# PRODUCT (adapt): radius, spacing, sizes and layout by use, each from one measured part.
RADII = [("xs", "checkbox-box", "border-top-left-radius", "The to-do checkbox"),
         ("sm", "select-pill", "border-top-left-radius", "Select option pills"),
         ("row", "page-row-selected-fill", "border-top-left-radius", "Sidebar rows"),
         ("button", "button-share", "border-top-left-radius", "Topbar buttons"),
         ("control", "sidebar-search", "border-top-left-radius", "Sidebar search and navigation tabs"),
         ("block", "callout-fill", "border-top-left-radius", "Callout and code blocks"),
         ("menu", "menu", "border-top-left-radius", "Menus and popovers"),
         ("dialog", "dialog", "border-top-left-radius", "Confirmation dialogs"),
         ("settings", "settings-dialog", "border-top-left-radius", "The settings window"),
         ("toolbar", "toolbar", "border-top-left-radius", "The text formatting toolbar"),
         ("ai-input", "ai-input", "border-top-left-radius", "The AI panel's input")]
for key, part, prop, use in RADII:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, ("radius", key), tok(px(v), "dimension", "Measured", f"computed {prop} of {part} in {shot}, dark, {DATE} ({use})"))
put(CORE, ("radius", "full"), tok("9999px", "dimension", "Measured", f"the AI button and avatars are circles (border-radius 100%), {DATE}"))
SPACES = [("row-x", "page-row-selected-fill", "padding-left", "Sidebar row inset"),
          ("button-x", "button-share", "padding-left", "Topbar button inset"),
          ("menu-row-x", "menu-row", "padding-left", "Menu row inset"),
          ("block-y", "callout-fill", "padding-top", "Callout inset"),
          ("block-x", "callout-fill", "padding-left", "Callout inset"),
          ("code-y", "code-fill", "padding-top", "Code block inset"),
          ("code-x", "code-fill", "padding-left", "Code block inset"),
          ("menu-y", "menu", "padding-top", "Menu inset"),
          ("table-cell-x", "table-cell", "padding-left", "Table cell inset"),
          ("dialog", "dialog", "padding-top", "Dialog inset")]
for key, part, prop, use in SPACES:
    shot, v = dim_of(part, prop)
    if v and v != "0px":
        put(CORE, ("spacing", key), tok(px(v), "dimension", "Measured", f"computed {prop} of {part} in {shot}, dark, {DATE} ({use})"))
HEIGHTS = [("tab", "tab-selected", "Tabs in the tab strip"),
           ("topbar", "topbar", "The page topbar"),
           ("nav-tab", "nav-tab", "The sidebar's Home, Chat and Meetings tabs"),
           ("row", "page-row-selected-fill", "Sidebar rows"),
           ("button", "button-share", "Topbar buttons"),
           ("button-new", "button-new", "The database New button"),
           ("icon-button", "topbar-icon-button", "Icon buttons"),
           ("menu-row", "menu-row", "Menu rows"),
           ("table-row", "table-row", "Database table rows"),
           ("select", "select", "Settings selects"),
           ("switch", "switch-on", "Switches"),
           ("ai-button", "ai-button", "The floating Notion AI button")]
for key, part, use in HEIGHTS:
    shot, v = dim_of(part, "height")
    if v:
        put(CORE, ("controlHeight", key), tok(px(v), "dimension", "Measured", f"computed height of {part} in {shot}, dark, {DATE} ({use})"))
LAYOUT = [("sidebar", "sidebar", "width", "The docked sidebar (270px is the owner's width)"),
          ("tab-max", "tab-selected", "width", "A tab in the tab strip"),
          ("menu", "menu", "width", "The page actions menu"),
          ("dialog", "dialog", "width", "The delete-property confirmation"),
          ("settings", "settings-dialog", "width", "The settings window"),
          ("ai-panel", "ai-panel", "width", "The Notion AI side panel"),
          ("peek", "peek", "width", "A database row's side peek"),
          ("palette", "palette", "width", "The search palette")]
for key, part, prop, use in LAYOUT:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, ("layout", key), tok(px(v), "dimension", "Measured", f"computed {prop} of {part} in {shot}, dark, {DATE} ({use})"))
# The page column: Notion's own layout properties.
for key, n in (("content", "--content-width"), ("margin", "--margin-width")):
    d = next((d for d in V["dark"]["decls"] if d["name"] == n and d["selector"] == ".layout"), None)
    if d:
        m = re.search(r"(\d+)px", d["value"])
        put(CORE, ("layout", key), tok(f"{m.group(1)}px", "dimension", "Measured", f"{n} in .layout ({d['value']}), {d['sheet']}, {DATE}", css=d["value"]))
WINDOW = C["dark"]["page-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"the tab's viewport, {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']:.2f} (the owner's 90% zoom on a 2x display), {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"the tab's viewport height (the tab strip's 36px is above it), {DATE}"))
put(CORE, ("layout", "tab-strip"), tok("36px", "dimension", "Measured", f"the tab strip page's viewport height (renderer/tabs/index.html), {DATE}"))
# Breakpoints Notion's stylesheets switch at (width conditions), the ones used by more than a few rules.
widths = {}
for cond, v in V["dark"]["conditions"].items():
    for m in re.finditer(r"width\s*(<=|>=|<|>)\s*([\d.]+)px", cond):
        widths[float(m.group(2))] = widths.get(float(m.group(2)), 0) + v["rules"]
for w, n in sorted(widths.items()):
    if n >= 5 and w >= 300:
        put(CORE, ("breakpoint", "%g" % w), tok("%gpx" % w, "dimension", "Measured", f"a width condition in Notion's stylesheets, {n} rules, {DATE}"))
# Border widths and the focus ring.
put(CORE, ("borderWidth", "default"), tok("1px", "dimension", "Measured", f"Notion draws edges as 1px box-shadow rings (shadow.outline-*, the menu's ring) and 1px borders (table cells), {DATE}"))
for part in ("button-share", "sidebar-search", "topbar-icon-button", "page-row", "select", "checkbox"):
    shot, s = style("dark", part, "focus-visible")
    if not s:
        continue
    # A transparent outline is a forced-colors fallback, not the ring Notion paints (that is a box-shadow).
    if s["outline-style"] not in ("none", "") and s["outline-width"] not in ("0px", "") and not color(s["outline-color"]).endswith(", 0)"):
        put(CORE, ("focusRing", "width"), tok(px(s["outline-width"]), "dimension", "Measured", f"outline-width of {part} in {shot}, dark, {DATE}", css=f"{s['outline-width']} {s['outline-style']} {s['outline-color']}"))
        put(CORE, ("focusRing", "offset"), tok(px(s["outline-offset"]), "dimension", "Measured", f"outline-offset of {part} in {shot}, dark, {DATE}"))
        break
    layers = [l for l in shadow(s["box-shadow"]) if not l["color"].endswith(", 0)")] if s["box-shadow"] != "none" else []
    if layers:
        # Notion stacks spread rings: a page-coloured gap, the blue ring, a page-coloured halo. The ring is the
        # first layer whose colour differs from the innermost one; its offset is the gap inside it.
        rings = sorted(layers, key=lambda l: float(l["spread"][:-2]))
        ring = next((l for l in rings if l["color"] != rings[0]["color"]), rings[-1])
        gap = rings[rings.index(ring) - 1]["spread"] if ring is not rings[0] else "0px"
        width = px("%gpx" % (float(ring["spread"][:-2]) - float(gap[:-2])))
        put(CORE, ("focusRing", "width"), tok(width, "dimension", "Measured", f"the coloured layer of the focus box-shadow of {part} in {shot} ({ring['color']}), less the gap inside it, dark, {DATE}", css=s["box-shadow"]))
        put(CORE, ("focusRing", "offset"), tok(gap, "dimension", "Measured", f"the page-coloured gap inside the ring, a box-shadow layer ({shot}), {DATE}"))
        break
if get(CORE, "focusRing.width"):
    put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring's width"))
# Motion: the transitions the captured parts declare.
seen = {}
for (part, state), (shot, s) in sorted(P["dark"].items()):
    for d_, e_ in zip(s["transition-duration"].split(","), s["transition-timing-function"].split(",") if "cubic" not in s["transition-timing-function"] else [s["transition-timing-function"]]):
        d_, e_ = d_.strip(), e_.strip()
        if d_ in ("0s", ""):
            continue
        seen.setdefault((d_, e_), (part, shot))
durs, eases = {}, {}
for (d_, e_), (part, shot) in sorted(seen.items(), key=lambda kv: (ms(kv[0][0]) if False else float(re.sub(r'm?s$', '', kv[0][0])), kv[0][1])):
    v = ms(d_)
    durs.setdefault(v, (part, shot))
    eases.setdefault(e_, (part, shot))
for v, (part, shot) in durs.items():
    put(CORE, ("duration", v.replace("ms", "")), tok(v, "duration", "Measured", f"transition-duration of {part} in {shot}, dark, {DATE}"))
NAMED = {"ease": [0.25, 0.1, 0.25, 1], "ease-in": [0.42, 0, 1, 1], "ease-out": [0, 0, 0.58, 1], "ease-in-out": [0.42, 0, 0.58, 1], "linear": [0, 0, 1, 1]}
for e_, (part, shot) in eases.items():
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", e_)
    val = [float("%g" % float(x)) for x in m.group(1).split(",")] if m else NAMED.get(e_)
    if val:
        key = e_ if not m else "spring"
        put(CORE, ("easing", key), tok(val, "cubicBezier", "Measured", f"transition-timing-function of {part} in {shot}, dark, {DATE}", css=e_))
cond = V["dark"]["conditions"]
CORE.setdefault("duration", {})["$extensions"] = {"reducedMotion": {"rules": {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k},
    "how": "Notion's stylesheets carry prefers-reduced-motion conditions (shimmer text, enter animations); no duration custom property changes"}}
for key, part in (("menu", "menu"), ("dialog", "dialog"), ("tooltip", "tooltip"), ("ai-button", "ai-button"), ("topbar", "topbar")):
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))
put(CORE, ("zoom",), tok(0.9, "number", "Measured", f"the app's zoomFactor (state.json appState.zoomFactor, the owner's View zoom), which makes devicePixelRatio 1.8 on a 2x display, {DATE}"))

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{bg.primary}", "the page and the main pane"),
    "surface": ("{bg.secondary}", "the sidebar and the tab strip"),
    "raised": ("{misc.popover-bg}", "menus, popovers, dialogs and the settings window"),
    "overlay": ("{bg.tertiary}", "a second raised level: hover fills on raised surfaces, the code block"),
    "scrim": ("{misc.modal-underlay-bg}", "the dimmed backdrop under dialogs and the settings window"),
    "text.primary": ("{text.primary}", ""), "text.secondary": ("{text.secondary}", ""), "text.disabled": ("{text.disabled}", ""),
    "text.on-accent": ("{blue.text-inverse-primary}", "text on the blue accent fill (the New button)"),
    "text.link": ("{text.primary}", "links are the body colour, underlined (misc.line-decoration-color)"),
    "border.default": ("{border.primary}", "dividers, table cells, the menu's ring"), "border.strong": ("{border.strong}", ""),
    "border.focus": ("{blue.border-accent-primary}", "the focus ring colour (Notion's focus shadows are the blue accent)"),
    "accent.default": ("{blue.bg-accent-primary}", "the one accent: the New button, switches on, checked checkboxes, links in settings"),
    "accent.subtle": ("{blue.bg-secondary}", "the accent's tint (selection, the blue pill)"),
}
STATUS = {"success": "green", "warning": "orange", "danger": "red", "info": "blue"}
for s_, hue in STATUS.items():
    ROLE[f"status.{s_}.fill"] = ("{%s.bg-accent-primary}" % hue, "")
    ROLE[f"status.{s_}.text"] = ("{%s.text-secondary}" % hue, "")
    ROLE[f"status.{s_}.subtle"] = ("{%s.bg-secondary}" % hue, "")
    ROLE[f"status.{s_}.border"] = ("{%s.border-primary}" % hue, "")

# PRODUCT (adapt): measured components -> the part that shows each, and the properties kept.
COMPONENTS = [
    ("button-new", "button-new", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-share", "button-share", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-danger", "button-danger", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-secondary", "button-secondary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("icon-button", "topbar-icon-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("sidebar", "sidebar-surface", {"bg": "background-color"}),
    ("sidebar-search", "sidebar-search", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("nav-tab", "nav-tab", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("nav-tab-selected", "nav-tab-selected", {"bg": "background-color", "text": "color"}),
    ("page-row", "page-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("page-row-selected", "page-row-selected-fill", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("section-label", "section-label", {"text": "color"}),
    ("tab-strip", "tabbar", {"bg": "background-color"}),
    ("tab", "tab", {"bg": "background-color", "text": "color", "height": "height"}),
    ("tab-selected", "tab-selected", {"bg": "background-color", "text": "color"}),
    ("menu", "menu", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("menu-row", "menu-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("dialog", "dialog", {"bg": "background-color", "radius": "border-top-left-radius", "padding": "padding-top"}),
    ("settings", "settings-dialog", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("settings-nav", "settings-nav", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color"}),
    ("select", "select", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "width": "width", "height": "height"}),
    ("switch-off", "switch-off", {"bg": "background-color"}),
    ("text-field", "text-field", {"bg": "background-color", "text": "color", "height": "height"}),
    ("palette", "palette", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("palette-row-selected", "palette-row-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("callout", "callout-fill", {"bg": "background-color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("code-block", "code-fill", {"bg": "background-color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("inline-code", "inline-code", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("checkbox", "checkbox-box", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("select-pill", "select-pill", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("table-cell", "table-cell", {"text": "color", "border": "border-bottom-color"}),
    ("table-header", "table-header-cell", {"text": "color"}),
    ("board-card", "board-card", {"bg": "background-color"}),
    ("toolbar", "toolbar", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("ai-button", "ai-button", {"bg": "background-color", "text": "color"}),
    ("ai-panel", "ai-panel", {"bg": "background-color"}),
    ("ai-input", "ai-input", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("toast", "toast", {"text": "color"}),
    ("peek", "peek", {"bg": "background-color"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "outline-focus", "outline-color")]
PREFER = ["role", "bg", "text", "border", "icon", "blue", "misc", "gray", "palette"]
AWKWARD = re.compile(r"marker|pill|home|site|seo|calendar|timeline|swi|credit|banner|keyboard|emoji|avatar|find|equation|token|illustration|frozen")


def index(t):
    idx = {}

    def walk(node, path):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and "$value" in v:
                if v["$type"] == "color":
                    idx.setdefault(resolve(t, v["$value"]), []).append(".".join(path + [k]))
            elif isinstance(v, dict):
                walk(v, path + [k])
    walk(SETS[t], [])
    for vals in idx.values():
        vals.sort(key=lambda p: (bool(AWKWARD.search(p)), PREFER.index(p.split(".")[0]) if p.split(".")[0] in PREFER else 99, len(p), p))
    return idx


def build_roles_and_components(t):
    tree = SETS[t]
    for key, spec in ROLE.items():
        target = spec[0][1:-1]
        if get(tree, target) is None:
            raise KeyError(f"role.{key}: {target} missing in {t}")
        put(tree, ("role",) + tuple(key.split(".")), tok(spec[0], "color", "Derived", f"the checklist role, mapped to {target}" + (f"; {spec[1]}" if spec[1] else "")))
    idx = index(t)
    counts = {"measured": 0, "aliased": 0}

    def value_for(part, shot, prop, raw):
        src = f"computed {prop} of {part} in {shot}, {THEME_NAME[t]}, {DATE}"
        if is_color(raw):
            v = color(raw)
            counts["measured"] += 1
            if v in idx:
                kinds = {"color": ("text", "icon", "blue", "misc", "gray", "red"), "background-color": ("bg", "misc", "blue", "gray", "red", "palette", "border"),
                         "border-top-color": ("border", "misc"), "border-bottom-color": ("border", "misc"),
                         "outline-color": ("border", "blue", "misc")}[prop]
                fits = [x for x in idx[v] if x.split(".")[0] in kinds]
                if fits:
                    counts["aliased"] += 1
                    first = {"color": "text", "background-color": "bg", "border-top-color": "border", "border-bottom-color": "border",
                             "border-right-color": "border", "outline-color": "border"}[prop]
                    pref = [x for x in fits if x.split(".")[0] == first]
                    return tok("{%s}" % (pref or fits)[0], "color", "Measured", src, painted=v)
            return tok(v, "color", "Measured", src)
        return tok(px(raw), "dimension", "Measured", src)
    for name, part, props in COMPONENTS:
        shot, s = style(t, part)
        if not s:
            continue
        for key, prop in props.items():
            raw = s.get(prop, "")
            if prop in ("background-color", "border-top-color", "border-bottom-color") and is_color(raw) and color(raw) == "rgba(0, 0, 0, 0)":
                continue
            if prop == "border-top-left-radius" and raw.endswith("%"):
                raw = "9999px"
            if not (raw.endswith("px") or is_color(raw)):
                continue
            put(tree, ("component", name, key), value_for(part, shot, prop, raw))
        for state, key, prop in STATES:
            sh, ss = style(t, part, state)
            if ss and ss[prop] != s[prop] and is_color(ss[prop]) and color(ss[prop]) != "rgba(0, 0, 0, 0)":
                if prop == "outline-color" and ss.get("outline-style") in ("none", ""):
                    continue
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
    for key, (comp_path, why) in {"accent.hover": ("component.button-new.bg-hover", "the New button under the pointer"),
                                  "accent.pressed": ("component.button-new.bg-pressed", "the New button while pressed")}.items():
        hit = get(tree, comp_path)
        if hit:
            put(tree, ("role",) + tuple(key.split(".")), tok(hit["$value"], "color", "Measured", hit["$extensions"]["source"]["from"] + f"; {why}"))
        else:
            put(tree, ("role",) + tuple(key.split(".")), tok("{blue.bg-accent-secondary}", "color", "Derived", f"{why} was not captured; Notion's second blue accent step stands in"))
    tree["$extensions"] = {"componentValues": counts}


for t in THEMES:
    build_roles_and_components(t)

# ---------------------------------------------------------------- checks


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


def check():
    core_names = dict(tokens_of(CORE))
    for setname, tree in [("core", CORE)] + [(t, SETS[t]) for t in THEMES]:
        names = dict(core_names)
        names.update(dict(tokens_of(tree)))
        for n, t in tokens_of(tree):
            if not (t.get("$extensions") or {}).get("source"):
                raise ValueError(f"{setname}.{n}: no source")
            for a in aliases(t["$value"]):
                if a not in names:
                    raise KeyError(f"{setname}.{n}: alias {{{a}}} points at nothing")
                if t["$type"] in ("color", "dimension") and names[a]["$type"] != t["$type"]:
                    raise TypeError(f"{setname}.{n}: alias {{{a}}} is a {names[a]['$type']}")
            if t["$type"] == "dimension" and not aliases(t["$value"]) and not re.fullmatch(r"-?\d*\.?\d+(px|rem|em)", t["$value"]):
                raise ValueError(f"{setname}.{n}: dimension {t['$value']!r}")
            if t["$type"] == "color" and not aliases(t["$value"]) and not re.fullmatch(r"#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)", t["$value"]):
                raise ValueError(f"{setname}.{n}: colour {t['$value']!r}")
    a, b = {n for n, _ in tokens_of(SETS["light"])}, {n for n, _ in tokens_of(SETS["dark"])}
    if a != b:
        raise ValueError(f"light and dark differ: only light {sorted(a - b)[:5]}, only dark {sorted(b - a)[:5]}")


def reconcile():
    """A name present in only one theme is not a theme token: move it out (an alias to it becomes its value)."""
    for _ in range(5):
        names = {t: {n for n, _ in tokens_of(SETS[t])} for t in THEMES}
        moved = False
        for t in THEMES:
            other = names["dark" if t == "light" else "light"]
            for n in sorted(names[t] - other):
                path = n.split(".")
                node = SETS[t]
                for k in path[:-1]:
                    node = node[k]
                v = node.pop(path[-1])
                SETS[t].setdefault("$extensions", {}).setdefault("notTokenised", []).append(
                    {"name": n, "value": v["$value"], "css": v["$extensions"].get("css"), "why": f"present only while capturing {t}; not in the other theme"})
                moved = True
            for n, v in list(tokens_of(SETS[t])):
                for a in aliases(v["$value"]):
                    if get(SETS[t], a) is None and get(CORE, a) is None:
                        v["$extensions"]["aliasOf"] = a
                        v["$value"] = v["$extensions"].get("painted") or resolve_removed(t, a)
        if not moved:
            break


def resolve_removed(t, a):
    for item in SETS[t].get("$extensions", {}).get("notTokenised", []):
        if item["name"] == a:
            return resolve(t, item["value"]) if isinstance(item["value"], str) else item["value"]
    raise KeyError(a)


reconcile()
for t in THEMES:
    def prune(node):
        for k in [k for k, v in node.items() if isinstance(v, dict) and "$value" not in v and not k.startswith("$")]:
            prune(node[k])
            if not [x for x in node[k] if not x.startswith("$")]:
                del node[k]
    prune(SETS[t])
    if SKIPPED[t]:
        SETS[t].setdefault("$extensions", {})["skipped"] = SKIPPED[t]
check()
tokens = {
    "core": CORE, "light": SETS["light"], "dark": SETS["dark"],
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Settings > Preferences > Theme: Light (.notion-light-theme, :root)"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Preferences > Theme: Dark (.notion-dark-theme on <body>)"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
