#!/usr/bin/env python3
"""Build components.md: token-based specs for every checklist component, then the 2026-09 inventory.

Inputs:
  raw/components-computed.json  2026-10 computed styles per component, state and theme (measure.mjs)
  tokens.json                   every value is named by the token that holds it, per theme
  tools/components-2026-09.md   the 2026-09 discovery list, product components and icon index (prose)
Each measured value is looked up in tokens.json (core plus that theme's set, aliases resolved) and
written as the token path; a value no token holds is printed raw and counted in the coverage line.
Deterministic: re-running on the same inputs reproduces components.md byte for byte.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
C = json.loads((HERE / "raw" / "components-computed.json").read_text())
CROPS = HERE / "components" / "crops" / "2026-10"


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def resolver(theme):
    toks = dict(flat(T["core"]))
    toks.update(flat(T[theme]))

    def res(v, depth=0):
        if isinstance(v, str):
            m = re.fullmatch(r"\{([^{}]+)\}", v.strip())
            if m and m.group(1) in toks and depth < 12:
                return res(toks[m.group(1)]["$value"], depth + 1)
        return v
    return toks, res


def rgba(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{6})([0-9a-f]{2})?", v)
    if m:
        h = m.group(1)
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), round(int(m.group(2), 16) / 255, 2) if m.group(2) else 1.0)
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        return (round(float(m.group(1))), round(float(m.group(2))), round(float(m.group(3))), round(float(m.group(4)), 2) if m.group(4) else 1.0)
    m = re.fullmatch(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", v)
    if m:
        return (round(float(m.group(1)) * 255), round(float(m.group(2)) * 255), round(float(m.group(3)) * 255), round(float(m.group(4)), 2) if m.group(4) else 1.0)
    return None


# Which token groups name a colour, most specific first: a role beats a palette step.
COLOR_ORDER = ["accent", "feedback", "bg", "text", "border", "icon", "special", "component", "autoflip", "shadowColor", "status", "palette"]
DIM_GROUPS = {"radius": ["radius"], "size": ["size", "layout", "focusRing"], "space": ["spacing"], "border": ["borderWidth"], "opacity": ["opacity"]}


def px(v):
    v = str(v).strip()
    if v.endswith("rem"):
        return round(float(v[:-3]) * 16, 2)
    if v.endswith("px"):
        return round(float(v[:-2]), 2)
    try:
        return round(float(v), 2)
    except ValueError:
        return None


def build_index(theme):
    toks, res = resolver(theme)
    colors, dims, typo = {}, {}, {}
    for name, t in sorted(toks.items(), key=lambda kv: kv[0]):
        group = name.split(".")[0]
        v = res(t["$value"])
        if t["$type"] == "color" and group in COLOR_ORDER:
            c = rgba(v)
            if c:
                colors.setdefault(c, []).append(name)
        elif t["$type"] in ("dimension", "number"):
            for kind, groups in DIM_GROUPS.items():
                if group in groups and px(v) is not None:
                    dims.setdefault((kind, px(v)), []).append(name)
        elif t["$type"] == "typography":
            fs, fw = px(res(v["fontSize"])), int(res(v["fontWeight"]))
            lhv = str(res(v["lineHeight"])).strip()
            lh = round(fs * float(lhv[:-1]) / 100, 2) if lhv.endswith("%") else px(lhv) if lhv.endswith(("px", "rem")) else round(fs * float(lhv), 2)
            typo.setdefault((fs, lh, fw), []).append(name)
    return colors, dims, {k: sorted(v, key=lambda n: (len(n), n))[0] for k, v in typo.items()}


# Which token group names a colour depends on what the colour paints: a text colour is named from
# text.*, a fill from bg.*, and so on; a palette step is the last resort.
ROLE_ORDER = {
    "text": ["text", "icon", "accent", "feedback", "special", "component", "autoflip", "palette"],
    "fill": ["bg", "accent", "feedback", "special", "component", "autoflip", "palette"],
    "border": ["border", "accent", "feedback", "component", "autoflip", "palette"],
    "ring": ["border", "accent", "shadowColor", "palette"],
}
DIM_PREF = ["size.control", "size.button", "size.icon", "radius", "spacing", "borderWidth", "focusRing", "opacity", "size", "layout"]


# Components whose measured height is not a size to copy: say what decides it instead.
SIZE_NOTE = {
    "menu": "content height, `size.menu-width` wide",
    "tooltip": "content height, at most `size.tooltip-max` wide",
    "dialog": "content height, at most `size.modal-max` wide",
    "dialog-scrim": "the whole viewport (fixed, inset 0)",
    "weekly-summary-card": "content height, full content width",
    "text-area-pill": "68px with one line (no token), grows with the text",
    "link": "inline, the line height of its text",
    "text-area": "one line of `typography.body.base` (24px), grows with the text",
    "card-course": "150px square on Topics (no token; `size.course-tile` on the 2xl course shelf)",
}
# Values a single reading misstates: the skeleton was read mid-pulse, and its .7 matches a button token only by value.
OVERRIDE = {
    ("skeleton-loading", "fill"): "pulses between `component.skeleton.from` and `component.skeleton.to` (read mid-pulse)",
    ("skeleton-loading", "opacity"): ".7 while loading (no token)",
}
# What the measured inner part is called in the spec; button3d parts are its face.
PART_LABEL = {"switch-on": "thumb", "switch-off": "thumb", "radio": "indicator", "checkbox-checked": "checkmark"}
SPEC = [""]  # the spec being written
HINTS = []  # words of the spec being written (switch, radio, avatar, button3d); a token named for the component wins


def pick(names, role=None, prefer=None):
    """Choose among tokens holding the same value: one the other theme also uses (prefer), then one
    named for this component, then the role order."""
    if prefer:
        both = [n for n in names if n in prefer]
        names = both or names
    if role is None:  # sizes, radii, opacities: a token named for this component wins
        hinted = [n for n in names if any(h in n for h in HINTS)]
        names = hinted or names
    else:  # colours: a component token for this component (component.switch.thumb) wins
        hinted = [n for n in names if n.startswith("component.") and any(h in n.split(".")[1] for h in HINTS)]
        names = hinted or names
    if role:
        order = ROLE_ORDER[role]
        names = [n for n in names if n.split(".")[0] in order] or names
        return sorted(names, key=lambda n: (order.index(n.split(".")[0]) if n.split(".")[0] in order else 99, len(n), n))[0]
    return sorted(names, key=lambda n: (next((i for i, p in enumerate(DIM_PREF) if n.startswith(p)), 99), len(n), n))[0]


IDX = {th: build_index(th) for th in ("light", "dark")}
STATS = {"named": 0, "raw": 0}


OTHER = {"dark": "light", "light": "dark"}


def name_color(v, th, role="fill", other=None):
    """other: the same property in the other theme, so one element gets one role name in both."""
    c = rgba(v)
    if c is None:
        return None
    if c[3] == 0:
        return "transparent"
    n = IDX[th][0].get(c)
    prefer = IDX[OTHER[th]][0].get(rgba(other)) if other and rgba(other) else None
    n = pick(n, role, prefer) if n else None
    STATS["named" if n else "raw"] += 1
    return f"`{n}`" if n else f"{v} (no token)"


def name_dim(v, th, kind):
    p = px(v)
    if p is None:
        return v
    if p == 0:
        return "0"
    n = IDX[th][1].get((kind, p)) or next((v for (k, q), v in IDX[th][1].items() if k == kind and abs(q - p) < 0.05), None)
    n = pick(n) if n else None
    STATS["named" if n else "raw"] += 1
    return f"`{n}`" if n else f"{v} (no token)"


def name_shadow(v, th, other=None):
    if v == "none":
        return "none"
    m = re.fullmatch(r"(rgba?\([^)]*\)) 0px 0px 0px 3px", v)
    if m:
        return f"`focusRing.width` in {name_color(m.group(1), th, 'ring', re.sub(r' 0px.*', '', other or ''))}"
    m = re.fullmatch(r"(rgba?\([^)]*\)) 0px 4px 0px 0px", v)
    if m:
        return f"lip 0 4px 0 in {name_color(m.group(1), th, 'ring', re.sub(r' 0px.*', '', other or ''))}"
    m = re.fullmatch(r"(rgba?\([^)]*\)) 0px 0px (\d+)px 0px", v)
    if m:
        lvl = {"15": "shadow.base", "25": "shadow.md"}.get(m.group(2))
        STATS["named" if lvl else "raw"] += 1
        return f"`{lvl}`" if lvl else v
    m = re.fullmatch(r"(rgba?\([^)]*\)) 0px 0px 0px 1px inset", v)
    if m:
        return f"inset 1px in {name_color(m.group(1), th, 'border')} (`shadow.input-focus`)"
    STATS["raw"] += 1
    return v


def name_typo(s, th):
    key = (px(s["font-size"]), px(s["line-height"]), int(s["font-weight"]))
    n = IDX[th][2].get(key)
    STATS["named" if n else "raw"] += 1
    return f"`{n}`" if n else f"{s['font-size']}/{s['line-height']} {s['font-weight']} (no style)"


def describe(s, th, base=None, o=None):
    """The properties worth stating for one element in one state, as token names."""
    out = []
    keep = lambda p: base is None or s[p] != base[p]
    if keep("background-color") and s["background-color"] not in ("rgba(0, 0, 0, 0)",):
        out.append(("fill", name_color(s["background-color"], th, "fill", o and o["background-color"])))
    if keep("background-image") and s["background-image"] != "none":
        out.append(("fill", "gradient (see crop)"))
    if keep("color"):
        out.append(("text", name_color(s["color"], th, "text", o and o["color"])))
    if keep("border-top-color") and s["border-top-width"] not in ("0px",) and s["border-top-style"] != "none":
        out.append(("border", f"{name_dim(s['border-top-width'], th, 'border')} {name_color(s['border-top-color'], th, 'border', o and o['border-top-color'])}"))
    if keep("box-shadow"):
        out.append(("shadow", name_shadow(s["box-shadow"], th, o and o["box-shadow"])))
    if keep("outline-style") or keep("outline-color") or keep("outline-width"):
        if s["outline-style"] == "auto":
            out.append(("focus", "browser default ring (no product style)"))
        elif base is not None and s["outline-color"] not in ("rgba(0, 0, 0, 0)",) and s["outline-style"] != "none":
            out.append(("outline", f"{name_dim(s['outline-width'], th, 'size')} {name_color(s['outline-color'], th, 'ring')}"))
    if keep("opacity") and s["opacity"] != "1":
        op = float(s["opacity"])
        n = next((pick(k) for (kind, v), k in IDX[th][1].items() if kind == "opacity" and v == op), None)
        out.append(("opacity", f"`{n}`" if n else s["opacity"]))
    if keep("transform"):
        tr = describe_transform(s, base is not None)
        if base is not None or tr != "none":
            out.append(("transform", tr))
    if keep("text-decoration-line") and s["text-decoration-line"] != "none":
        out.append(("decoration", s["text-decoration-line"]))
    if base is None and px(s["height"]) == 63:
        out.append(("size", "`size.appBar` less its 1px border (calc(100% - 1px))"))
    elif base is None and SPEC[0] in SIZE_NOTE:
        out.append(("size", SIZE_NOTE[SPEC[0]]))
    elif base is None:
        out.append(("size", f"{name_dim(s['height'], th, 'size')} high"))
    if base is None:
        if s["border-radius"] != "0px":
            out.append(("radius", name_dim(s["border-radius"], th, "radius")))
        pad = [name_dim(p, th, "space") for p in s["padding"].split()]
        if any(p != "0" for p in pad):
            out.append(("padding", " ".join(pad)))
        out.append(("type", name_typo(s, th)))
        out = [(k, OVERRIDE.get((SPEC[0], k), v)) for k, v in out]
    return out


def describe_transform(s, changed):
    """A translate-only matrix as the lift or shift it is; anything else as written."""
    t = s["transform"]
    if t == "none":
        return "none (face drops onto its lip)" if changed else "none"
    m = re.fullmatch(r"matrix\(1, 0, 0, 1, (-?[\d.]+), (-?[\d.]+)\)", t)
    if not m:
        return t
    x, y = float(m.group(1)), float(m.group(2))
    w, h = px(s["width"]) or 0, px(s["height"]) or 0
    if x and y and abs(x + w / 2) < 1 and abs(y + h / 2) < 1:
        return "translate(-50%, -50%) (centred on its anchor)"
    if x == 0 and y == -4:
        return "translateY(-4px) (`size.button3d-lift`: the face rests above its lip)"
    parts = ([f"translateX({x:g}px)"] if x else []) + ([f"translateY({y:g}px)"] if y else [])
    return " ".join(parts) or "none"


def fmt(items):
    return "; ".join(f"{k} {v}" for k, v in items) if items else "no change"


def crop(name, th, st):
    f = CROPS / f"{name}-{th}-{st}.png"
    return f"[{th}](components/crops/2026-10/{f.name})" if f.exists() else ""


STATE_LABEL = {"default": "default", "hover": "hover", "focus-visible": "focus-visible", "active": "pressed"}


def spec_table(name):
    rec = C[name]
    SPEC[0] = name
    HINTS[:] = [w for w in re.split(r"-", name) if w not in ("button", "dark", "light", "on", "off", "selected", "default", "text", "setting", "row", "card")] + [name]
    rows = []
    for st in ("default", "hover", "focus-visible", "active"):
        if st not in rec["dark"]:
            continue
        cells = []
        for th in ("dark", "light"):
            r = rec[th]
            base = None if st == "default" else r["default"]["self"]
            o = rec[OTHER[th]][st]
            items = describe(r[st]["self"], th, base, o["self"])
            if "part" in r[st] and st == "default":
                items = [i for i in items if i[0] not in ("text", "type", "shadow")]
            if "part" in r[st]:
                pb = None if st == "default" else r["default"]["part"]
                pi = describe(r[st]["part"], th, pb, o.get("part"))
                if pi:
                    items = items + [(PART_LABEL.get(name, "face") + ": " + k, v) for k, v in pi]
            cells.append(fmt(items))
        links = " ".join(x for x in (crop(name, "dark", st), crop(name, "light", st)) if x)
        if st != "default" and cells[0] == "no change" and cells[1] == "no change":
            continue
        rows.append(f"| {STATE_LABEL[st]} | {cells[0]} | {cells[1]} | {links} |")
    head = f"**{name}** ({rec['dark'].get('label') or 'no label'!s}; `{rec['dark']['selector']}`)\n\n| State | Dark | Light | Crops |\n|---|---|---|---|\n"
    return head + "\n".join(rows) + "\n"


# PRODUCT (adapt): the checklist, mapped to the measured specs. None = not present or not captured.
CHECKLIST = [
    ("Button", ["button3d-blue", "button3d-neutral", "button3d-disabled", "button-inverse", "button-outline", "button-danger-text", "button-danger", "button-danger-disabled", "button-disabled", "premium-button"],
     "The 3D button (`data-slot=button3d`: a face lifted 4px over a same-hue lip) is the main action; flat buttons (`data-slot=button`) do everything else. "
     "Sizes: `size.control-md` for main and flat buttons, `size.control-sm` for outline buttons inside settings rows. "
     "The solid danger button (\"Deactivate account\") stays disabled, a dark red tint with muted text, until a reason is checked."),
    ("Icon button", ["icon-button", "icon-button-disabled", "icon-button-toggle"], "`data-slot=icon-button`: a 44px round button with a 16px glyph; the star toggle on topics is 40px with `aria-pressed`."),
    ("Link", ["link"], "`data-slot=link`: footer and inline links are quiet (`text.secondary`) until hover, which turns them blue and underlined."),
    ("Text field", ["text-field", "text-field-invalid"], "`data-slot=form-input`. Error state, reached 2026-10-17 by typing `not-an-email` into Settings > Add another email and pressing Add: "
     "the browser blocked the submit and showed its native bubble (\"Please include an '@' in the email address\"), and the field itself looked unchanged (`text-field-invalid` below matches the default). "
     "The stylesheet's `outline-color: border.danger-primary` rule on `:invalid, [data-invalid], [aria-invalid=true]` (raw/css-rules.json) did not paint here, because the field draws a border, not an outline. See raw/live-readings.json."),
    ("Text area", ["text-area", "text-area-pill", "text-area-bordered"], "Two kinds. The Koji prompt is a borderless auto-growing textarea inside a frosted pill (`blur.ask-pill`); it shows no focus ring, so the caret is the only focus cue. "
     "The deactivate form's \"Other\" reason opens a bordered textarea, styled like the text field, whose focus darkens the border and adds an inset ring."),
    ("Select", None, "Not present: no screen reached on a free account uses one. The stylesheet carries a `select-icon` slot, but nothing rendered it."),
    ("Checkbox", ["checkbox", "checkbox-checked"], "`data-slot=checkbox` (Base UI), 20px square with 6px corners and a 2px border; checked fills solid with the inverse colour and draws a 12x9 checkmark in `text.inverse`. Found on Settings > Deactivate account (the reason list); the settings switches elsewhere hide their own checkbox inputs."),
    ("Radio", ["radio", "segment-selected", "segment", "segment-track"], "A real radio (`data-slot=radio`, 20px) in the account's connected-accounts list, and the segmented control, which is a Base UI radio group (`role=radiogroup`) of pill segments."),
    ("Switch", ["switch-on", "switch-off"], "`data-slot=switch`, 48x32 track, 24px thumb; focus is a 3px outline in `border.select`."),
    ("Tabs", ["nav-tab-selected", "nav-tab", "settings-tab-selected", "settings-tab"], "Two tab sets: the app header (Home, Topics, You; selected has an underline bar and `text.primary`) and the settings side menu (selected gets `bg.tertiary`)."),
    ("Menu", ["menu", "menu-item", "menu-item-highlighted"], "Base UI dropdown (`role=menu`). Hover and keyboard focus both set `data-highlighted`, which paints `bg.hover`; the item itself draws no ring."),
    ("Tooltip", ["tooltip", "tooltip-trigger"], "Base UI tooltip on hover or focus of a 12px info icon; `bg.elevated`, `shadow.base`, `typography.body.sm` in `text.secondary`."),
    ("Dialog", ["dialog", "dialog-scrim"], "Base UI dialog (`modal-content`), `shadow.md`, max `size.modal-max`; the scrim is `special.overlay.default`. Used for the destructive quit confirmation."),
    ("Toast", ["toast", "toast-added"], "Sonner (`[data-sonner-toast]`), bottom of the viewport, 356px wide. Fired 2026-10-17 by unstarring then restarring a topic (account left as it was): removing shows the neutral toast, adding shows the success-tinted one."),
    ("Alert", ["alert-info"], "`data-slot=alert role=alert`: the info alert on Settings > Account (no password set). Tinted `bg.blue-secondary`, no border, 16px icon in currentColor. It is the measured source for `feedback.info`."),
    ("Skeleton", ["skeleton-loading"], "`data-slot=skeleton` with `data-loading`: the grey block the You page shows while its chart loads, captured mid-load."),
    ("Card", ["card-course", "weekly-summary-card"], "Course cards are 3D like the button (2px `border.solid` edge plus a 4px lip); summary cards are flat with a 2px border and a tinted gradient."),
    ("List row", ["list-row-setting"], "Settings rows: a 1px `border.primary` box, `radius.xl`, label left and control right."),
    ("Table", None, "Captured 2026-09 on the public `/subscribe/` page (Free vs Premium comparison, both themes): see [raw/pricing-computed.json](raw/pricing-computed.json) and [premium-comparison-dark](components/crops/premium-comparison-dark.png). The You page also renders a screen-reader-only data table (`data-slot=table`, inside `panda-sr_true`) behind its bar chart."),
    ("Avatar", ["avatar"], "An initials tile (48px, `radius.md`, `palette.blue.500`) on the You page at phone width; there is no photo avatar."),
    ("Badge", ["badge-unverified", "badge-primary"], "`.panda-badge` subtle variants: 12/13.2 700 uppercase on a tinted fill, `radius.lg`."),
]

EXTRA = {"Alert", "Skeleton"}


def main():
    out = ["# Brilliant components", "",
           "Token-based specs for every component on the coverage checklist, measured on 2026-10-17 in the signed-in app (free account) in both themes, "
           "then the 2026-09-25 discovery list, product-specific components and icon index. Every value in the specs is the token in [tokens.json](tokens.json) that holds it "
           "for that theme; hover, focus-visible and pressed were forced on the element with the DevTools protocol, so they are the browser's own computed styles. "
           "The raw readings are in [raw/components-computed.json](raw/components-computed.json); crops of every state that changed something are in "
           "[components/crops/2026-10/](components/crops/2026-10).", "",
           "Read a row as: what changes from the default in that state. \"browser default ring\" means the product sets no focus style there, so Chrome draws its own.", ""]
    out += ["## Component specs (2026-10)", ""]
    core = [t for t in CHECKLIST if t[0] not in EXTRA]
    present = sum(1 for _, specs, _ in core if specs) + 1  # Table captured 2026-09
    out += [f"{present} of {len(core)} checklist components are captured; select is not present on any screen a free account reaches. "
            f"Alert and skeleton are extra, outside the checklist.", ""]
    for title, specs, note in CHECKLIST:
        out += [f"### {title}", "", note, ""]
        for s in specs or []:
            out += [spec_table(s)]
    total = STATS["named"] + STATS["raw"]
    out.insert(out.index("## Component specs (2026-10)") + 2, f"{STATS['named']} of {total} values in these specs are named by a token; the {STATS['raw']} others are printed raw and marked \"no token\".")
    out.insert(out.index("## Component specs (2026-10)") + 3, "")
    out += ["## Earlier capture (2026-09-25)", "",
            "Kept as written for the first capture, with values read live in Chrome at 1384x797. Where a 2026-10 spec above covers the same component, the spec wins.", ""]
    out += [(HERE / "tools" / "components-2026-09.md").read_text().split("\n", 1)[1].rstrip(), ""]
    out += [(HERE / "tools" / "components-gaps.md").read_text().rstrip(), ""]
    (HERE / "components.md").write_text("\n".join(out))
    print("components.md:", total, "values,", STATS["named"], "named by a token")


main()
