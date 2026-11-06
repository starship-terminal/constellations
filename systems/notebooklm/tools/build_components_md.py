#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json and tokens.json.

    python3 tools/build_components_md.py

Every measured value is written as the token that holds it, looked up in tokens.json: colours
against the theme's semantic set first (then the core palettes), radii, spacing, sizes, type roles
and shadows against core. A value no token holds is written raw and marked so. A cell that names
one token holds for both themes (the token resolves per theme); where dark and light resolve to
different tokens both are given. Crops are linked from components/crops/.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((HERE / "tokens.json").read_text())
DATA = json.loads((HERE / "raw" / "components-computed.json").read_text())
COMP = DATA["components"]
CROPS = HERE / "components" / "crops"

def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")

def norm_color(c):
    if c is None:
        return None
    c = c.strip()
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", c) or re.match(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", c)
    if not m:
        return c.lower()
    vals = [float(x) for x in m.groups()[:3]]
    if c.startswith("color("):
        vals = [v * 255 for v in vals]
    a = float(m.group(4)) if m.group(4) else 1.0
    r, g, b = (round(v) for v in vals)
    if a >= 1:
        return "#%02x%02x%02x" % (r, g, b)
    if a == 0:
        return "transparent"
    return "rgba(%d,%d,%d,%s)" % (r, g, b, ("%.2f" % a).rstrip("0").rstrip("."))

# Reverse maps: value -> token path, in priority order.
PRIORITY = ["text", "surface", "bg", "accent", "border", "state", "status", "icon", "skeleton", "tile", "code", "pastel", "dataviz"]
# Each property looks a colour up in the groups whose role fits it first, so a fill is named by a
# surface token and a label by a text token even where two roles share a value.
ROLE = {"fill": ["surface", "bg", "accent", "state", "status", "skeleton", "tile"],
        "text": ["text", "icon", "accent", "status", "studio", "code"],
        "border": ["border", "status", "state"]}
def color_map(theme, role):
    m = {}
    order = ROLE[role] + [g for g in PRIORITY if g not in ROLE[role]]
    items = list(flat(TOK[theme]))
    items.sort(key=lambda kv: order.index(kv[0].split(".")[0]) if kv[0].split(".")[0] in order else 99)
    for k, t in items:
        if t["$type"] == "color":
            m.setdefault(norm_color(t["$value"]), f"{k}")
    for k, t in flat(TOK["core"]["palette"], "palette."):
        m.setdefault(norm_color(t["$value"]), f"core.{k}")
    return m
CMAP = {(th, r): color_map(th, r) for th in ("dark", "light") for r in ROLE}

def dim_map(group, prefer=()):
    m = {}
    for k, t in flat(TOK["core"][group]):
        if k in prefer:
            m[str(t["$value"])] = f"{group}.{k}"
    for k, t in flat(TOK["core"][group]):
        m.setdefault(str(t["$value"]), f"{group}.{k}")
    return m
RADIUS = dim_map("radius", prefer=("full", "xs", "sm", "md", "lg", "lg-increased", "lg-max", "xl", "xl-increased", "xl-max", "xxl"))
SPACE = dim_map("spacing")
SIZE = {v: k for v, k in dim_map("size").items() if not k.startswith("size.icon-")}
for _k, _t in flat(TOK["core"]["size"]):
    if not _k.startswith("icon-"):
        SIZE.setdefault(str(_t["$value"]), f"size.{_k}")
# A type role matches only when family, size, weight and line height all match.
FAMILY = {k: t["$value"][0] for k, t in flat(TOK["core"]["fontFamily"])}
TYPE = {}
for k, t in flat(TOK["core"]["typography"]):
    v = t["$value"]
    fam = FAMILY[v["fontFamily"].strip("{}").split(".")[1]]
    TYPE.setdefault((fam, v["fontSize"], str(v["fontWeight"]), v["lineHeight"]), f"typography.{k}")
SHADOW = {}
for theme in ("dark", "light"):
    for k, t in flat(TOK[theme]["shadow"]):
        sig = ";".join(f'{p["offsetX"]} {p["offsetY"]} {p["blur"]} {p["spread"]} {norm_color(p["color"])}' for p in t["$value"])
        SHADOW[(theme, sig)] = f"shadow.{k}"

RAW_COUNT = {"n": 0, "tok": 0}
def tok(path):
    RAW_COUNT["tok"] += 1
    return f"`{path}`"
def raw(v):
    RAW_COUNT["n"] += 1
    return f"{v} (raw)"

def color_cell(c, theme, role="text"):
    n = norm_color(c)
    if n in (None, "transparent"):
        return "none"
    p = CMAP[(theme, role)].get(n)
    return tok(p) if p else raw(n)

def both(fn, d, l):
    a = fn(d, "dark")
    after_a = dict(RAW_COUNT)
    b = fn(l, "light") if l is not None else None
    if b is None or a == b:
        # One value is written, so only its tokens count.
        RAW_COUNT.update(after_a)
        return a
    return f"{a} / {b}"

def shadow_sig(s):
    if not s or s == "none":
        return None
    parts = []
    for m in re.finditer(r"(rgba?\([^)]*\)) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px)(?: (-?[\d.]+px))?( inset)?", s):
        col, x, y, b, sp, ins = m.groups()
        parts.append(f"{x} {y} {b} {sp or '0px'} {norm_color(col)}")
    return ";".join(parts)

def shadow_cell(s, theme):
    sig = shadow_sig(s)
    if not sig:
        return "none"
    p = SHADOW.get((theme, sig))
    return tok(p) if p else raw(s)

def len_cell(v, table):
    if v in (None, "0px", "auto", "normal"):
        return "0" if v == "0px" else (v or "")
    p = table.get(v)
    return tok(p) if p else raw(v)

def radius_cell(st):
    """CSS order (top-left top-right bottom-right bottom-left), one value when all corners match."""
    cs = [st.get(f"border{k}Radius", "0px") for k in ("TopLeft", "TopRight", "BottomRight", "BottomLeft")]
    if len(set(cs)) == 1:
        return len_cell(cs[0], RADIUS)
    return " ".join(len_cell(c, RADIUS) for c in cs)

def pad_cell(st):
    """CSS order (top right bottom left), shortened only where sides match."""
    t, r, b, l = st["paddingTop"], st["paddingRight"], st["paddingBottom"], st["paddingLeft"]
    if t == r == b == l == "0px":
        return "0"
    sides = [t, r, b, l]
    if t == b and r == l:
        sides = [t, r] if t != r else [t]
    elif r == l:
        sides = [t, r, b]
    return " ".join(len_cell(v, SPACE) for v in sides)

ICON_SIZE = {str(t["$value"]): f"size.{k}" for k, t in flat(TOK["core"]["size"]) if k.startswith("icon-")}
def type_cell(s):
    ts = s.get("textStyle") or {}
    st = s["style"]
    if (ts.get("node") or "").startswith("mat-icon"):
        p = ICON_SIZE.get(ts.get("fontSize"))
        return "icon glyph " + (tok(p) if p else raw(ts.get("fontSize")))
    size, w, lh = ts.get("fontSize") or st["fontSize"], str(int(float(ts.get("fontWeight") or st["fontWeight"]))), ts.get("lineHeight") or st["lineHeight"]
    fam = (ts.get("fontFamily") or st["fontFamily"]).split(",")[0].strip().strip('"')
    p = TYPE.get((fam, size, w, lh))
    if not p:
        return raw(f"{fam} {size}/{lh} {w}")
    return tok(p) if p else raw(f"{size}/{lh} {w}")

def inner_layer(s):
    for p in s.get("paint", []):
        if "ripple" in p["node"] or "state-layer" in p["node"]:
            if p.get("opacity") not in (None, "0"):
                return p.get("bg"), p.get("opacity")
    return None, None

def focus_cell(s, theme, focused=True):
    st = s["style"]
    if st["outlineStyle"] == "auto":
        return "browser default ring (outline auto), no product ring"
    if st["outlineStyle"] != "none" and st["outlineWidth"] != "0px" and not st["outlineColor"].endswith(", 0)"):
        return f'{len_cell(st["outlineWidth"], {"3px": "focusRing.width", "2px": "borderWidth.field-focus", "1px": "borderWidth.hairline"})} {color_cell(st["outlineColor"], theme, "border")} offset {len_cell(st["outlineOffset"], {"2px": "focusRing.offset"})}'
    if not focused:
        return "none"
    for p in s.get("paint", []):
        if "focus-indicator" in p["node"] and p.get("border"):
            m = re.search(r"(\d+px) solid (rgba?\([^)]*\))", p["border"])
            if m:
                return f'{len_cell(m.group(1), {"3px": "focusRing.checkbox-width", "2px": "focusRing.field-width"})} ring {color_cell(m.group(2), theme, "border")} (.mat-focus-indicator)'
        if p.get("outline"):
            m = re.match(r"(\S+) (\S+) (rgba?\([^)]*\)) offset (\S+)", p["outline"])
            if m and m.group(2) == "auto":
                return f"browser default ring on {p['node'].split('.')[0]} (outline auto), no product ring"
            if m and m.group(2) != "none":
                return f"{m.group(1)} {m.group(2)} {color_cell(m.group(3), theme, 'border')} on {p['node'].split('.')[0]}"
        if p.get("border") and "notch" in p["node"] and focused:
            m = re.search(r"(\d+px) solid (rgba?\([^)]*\))", p["border"])
            if m:
                return 'outline thickens to ' + len_cell(m.group(1), {"2px": "borderWidth.field-focus", "1px": "borderWidth.field"}) + ' ' + color_cell(m.group(2), theme, "border")
    return "none painted"

def fill_cell(s, theme):
    st = s["style"]
    bg = st["backgroundColor"]
    if norm_color(bg) == "transparent":
        for p in s.get("paint", [])[:3]:
            if p.get("bg") and p.get("opacity") in (None, "1") and "ripple" not in p["node"] and "focus" not in p["node"]:
                return color_cell(p["bg"], theme, "fill") + " (inner)"
        for a in s.get("ancestors", [])[:1]:
            if a.get("bg") and norm_color(a["bg"]) != "transparent":
                return color_cell(a["bg"], theme, "fill") + " (on parent)"
        return "none"
    return color_cell(bg, theme, "fill")

def border_cell(s, theme):
    st = s["style"]
    if st["borderTopWidth"] != "0px" and st["borderTopStyle"] != "none" and norm_color(st["borderTopColor"]) != "transparent":
        return f'{len_cell(st["borderTopWidth"], {"1px": "borderWidth.hairline", "2px": "borderWidth.field-focus"})} {color_cell(st["borderTopColor"], theme, "border")}'
    for p in s.get("paint", [])[:4]:
        # A checkmark is drawn with two border strokes; it is a glyph, not the control's border.
        if re.search(r"pseudo-checkbox|checkmark|__mark", p["node"]):
            continue
        if p.get("border"):
            m = re.search(r"(\d+px) solid (rgba?\([^)]*\))", p["border"])
            if m and norm_color(m.group(2)) != "transparent" and "focus" not in p["node"]:
                return f'{len_cell(m.group(1), {"1px": "borderWidth.hairline", "2px": "borderWidth.field-focus"})} {color_cell(m.group(2), theme, "border")} ({p["node"].split(".")[0]})'
        if p.get("shadow") and "inset" in p["shadow"]:
            m = re.match(r"(rgba?\([^)]*\)) 0px 0px 0px (\d+px) inset", p["shadow"])
            if m and norm_color(m.group(1)) != "transparent":
                return f"{len_cell(m.group(2), {'1px': 'borderWidth.hairline'})} {color_cell(m.group(1), theme, 'border')} (inset shadow)"
    return "none"

def layer_cell(s, theme):
    bg, op = inner_layer(s)
    if not bg:
        return "none"
    return f"{color_cell(bg, theme, 'fill')} at `opacity.{ {'0.08': 'hover', '0.12': 'pressed', '0.16': 'dragged'}.get(op, op) }`"

def size_cell(s):
    w, h = s["rect"]["w"], s["rect"]["h"]
    hh = f"{round(h)}px"
    p = SIZE.get(hh)
    return f"{round(w)} x " + (tok(p) if p else f"{hh}")

ROWS = [("Size (w x h)", lambda s, th: size_cell(s)), ("Fill", fill_cell), ("Text", lambda s, th: color_cell((s.get("textStyle") or {}).get("color") or s["style"]["color"], th)),
        ("Type", lambda s, th: type_cell(s)), ("Border", border_cell), ("Radius", lambda s, th: radius_cell(s["style"])),
        ("Padding", lambda s, th: pad_cell(s["style"])), ("Shadow", lambda s, th: shadow_cell(s["style"]["boxShadow"], th)),
        ("State layer", layer_cell), ("Focus ring", focus_cell)]

ORDER = ["default", "hover", "focus-visible", "pressed"]
def state_names(c):
    names = [k for k in c["states"] if not k.startswith("light")]
    return sorted(names, key=lambda k: (ORDER.index(k) if k in ORDER else 10, k))

def light_of(state):
    return "light" if state == "default" else f"light-{state}"

def crop_link(key, state):
    f = CROPS / f"{key}-{state}.png"
    return f"![{key} {state}](components/crops/{f.name})" if f.exists() else None

GROUPS = ["Buttons", "Links", "Inputs", "Navigation", "Overlays", "Lists", "Tables", "Display", "Shell", "Type"]
out = []
W = out.append
W("# NotebookLM components")
W("")
W(f"Built by `tools/build_components_md.py` from [raw/components-computed.json](raw/components-computed.json) (computed styles read on {DATA['_meta']['read']} from redacted copies of the signed-in app, every state in dark and light) and [tokens.json](tokens.json). Every value below is the token that holds it; a value no token holds is written raw and marked `(raw)`. One token name covers both themes, since each semantic token resolves per theme; where the two themes land on different tokens the cell reads `dark / light`. Colour tokens without a set prefix are in the `light` and `dark` sets; `core.palette.*`, `radius.*`, `spacing.*`, `size.*`, `typography.*`, `focusRing.*`, `borderWidth.*` and `opacity.*` are in `core`.")
W("")
W("States are real: `hover` is a pointer hover, `focus-visible` a keyboard focus (Shift+Tab, Tab), `pressed` the mouse held down, each in headless Chromium on the static copy. Other states (`selected`, `open`, `typed`, `error`, `disabled`, ...) are other elements or other copies captured in that state. The full per-state property tables are in [raw/measurements.md](raw/measurements.md).")
W("")
W("## Discovery")
W("")
W("| Checklist component | Entry | States measured |")
W("|---|---|---|")
CHECK = [("Button", ["button-accent", "button-tonal", "button-text", "button-outlined", "button-dialog-primary", "button-disabled", "button-confirm-delete"]),
         ("Icon button", ["icon-button", "icon-button-small"]), ("Link", ["link", "link-inline"]), ("Text field", ["text-field", "search-field"]),
         ("Text area", ["text-area", "text-area-outlined", "text-area-custom"]), ("Select", ["select", "menu-trigger"]), ("Checkbox", ["checkbox"]),
         ("Radio", ["radio"]), ("Switch", ["switch"]), ("Tabs", ["tab", "segmented", "mobile-tab"]), ("Menu", ["menu", "menu-settings"]),
         ("Tooltip", ["tooltip"]), ("Dialog", ["dialog", "dialog-large", "dialog-announcement", "scrim"]), ("Toast", ["toast"]),
         ("Card", ["card", "studio-tile"]), ("List row", ["list-row", "list-row-output", "chat-bubble"]), ("Table", ["table-row", "table-header", "mobile-list-row"]),
         ("Avatar", ["avatar"]), ("Badge", ["badge-pro", "badge-new", "status-chip"])]
for name, keys in CHECK:
    st = sorted({s for k in keys if k in COMP for s in state_names(COMP[k])}, key=lambda k: (ORDER.index(k) if k in ORDER else 10, k))
    W(f"| {name} | " + ", ".join(f"[{COMP[k]['title']}](#{k})" for k in keys if k in COMP) + f" | {', '.join(st)} |")
W("")
for group in GROUPS:
    keys = [k for k, c in COMP.items() if c.get("group") == group]
    if not keys:
        continue
    W(f"## {group}")
    W("")
    for k in keys:
        c = COMP[k]
        W(f'<a id="{k}"></a>')
        W(f"### {c['title']}")
        W("")
        if c.get("desc"):
            W(c["desc"])
            W("")
        names = state_names(c)
        imgs = [x for x in (crop_link(k, s) for s in names) if x]
        limg = crop_link(k, "light")
        if imgs:
            W(" ".join(imgs[:6] + ([limg] if limg else [])))
            W("")
        W("| Property | " + " | ".join(names) + " |")
        W("|---|" + "---|" * len(names))
        for label, fn in ROWS:
            before = dict(RAW_COUNT)
            cells = []
            for s in names:
                d = c["states"].get(s)
                l = c["states"].get(light_of(s))
                if not d or "style" not in d:
                    cells.append((d or {}).get("skipped") or (d or {}).get("error") or "not measured")
                    continue
                f = (lambda x, th, st=s: focus_cell(x, th, "focus" in st)) if label == "Focus ring" else fn
                cells.append(both(f, d, l if l and "style" in l else None))
            if all(x in ("none", "0", "none painted", "") for x in cells) and label not in ("Fill", "Text", "Type"):
                RAW_COUNT.update(before)  # the row is not written, so it counts nothing
                continue
            W(f"| {label} | " + " | ".join(cells) + " |")
        W("")

W("## Gaps")
W("")
W("- **Loading in a component**: no button or field showed a spinner; the only loading state captured is the search results skeleton ([skeleton](#skeleton)).")
W("- **Disabled**: captured on the dialog Save and Insert buttons and on the switch (disabled because the browser blocks notifications). No disabled text field, checkbox or menu item appeared.")
W("- **Error**: captured on the Website URL text area and its message ([text-area-outlined](#text-area-outlined), [error-text](#error-text)); no other field validates before submit.")
W("- **Switch on**: the only switch is disabled and off; its on state was not reachable without granting notification permission.")
W("- **Hover on 390 copies** is not measured (no pointer on a phone).")
W("- **Avatar**: the photo was replaced by a grey disc in the copy, so only its size and shape are the product's.")
W("- **Studio outputs** (Audio and Video Overviews, mind map, flashcards, quiz) open player or iframe views that were not recaptured on 2026-10-17; the 2026-09-25 package measured some from screenshots and those readings are not carried over.")
W("")
W(f"Token coverage: {RAW_COUNT['tok']} written values name a token, {RAW_COUNT['n']} are raw values.")
(HERE / "components.md").write_text("\n".join(out) + "\n")
print(f"wrote components.md: {RAW_COUNT['tok']} token values, {RAW_COUNT['n']} raw")
