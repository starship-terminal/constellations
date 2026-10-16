#!/usr/bin/env python3
"""Build components.md for TokenTracker from raw/components-computed.json, tokens.json, icons/INDEX.tsv
and screenshots/.

One entry per component: what it is, its crops in dark and light, and a compact table of the values
that change between states (size, padding, fill, border, radius, text, shadow, transition). Every
value is written as the token in tokens.json that holds it (semantic names from the theme's set
first, then core); a value no token holds is shown raw and marked "untokenised". Run build_tokens.py
first. The full property dump per state is raw/measurements.md. Deterministic: same inputs,
byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
J = json.loads((HERE / "raw" / "components-computed.json").read_text())
C = J["components"]
SHOTS = sorted(p.name for p in (HERE / "screenshots").glob("*.png"))
ICONS = [l.split("\t") for l in (HERE / "icons" / "INDEX.tsv").read_text().splitlines()[1:] if l.strip()]
TOK = json.loads((HERE / "tokens.json").read_text())


def _leaves(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from _leaves(v, prefix + k + ".")


CORE = dict(_leaves(TOK["core"]))


def _resolve(v):
    while isinstance(v, str) and v.startswith("{"):
        v = CORE[v[1:-1]]["$value"]
    return v


def _shadow(v):
    """A computed box-shadow -> comparable layers, without Tailwind's transparent placeholders."""
    out = []
    for c, x, y, b, sp in re.findall(r"(rgba?\([^)]*\)) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px)", v or ""):
        if c.startswith("rgba") and float(c.rstrip(")").split(",")[-1]) == 0:
            continue
        if b == sp == x == y == "0px":
            continue
        out.append((x, y, b, sp, _hex8(c)))
    return out


def _hex8(c):
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", c or "")
    if not m:
        return c
    h = "#" + "".join("%02x" % round(float(x)) for x in m.groups()[:3])
    a = m.group(4)
    return h if a is None or float(a) >= 1 else h + "%02x" % round(float(a) * 255)


# Reverse indexes: value -> token names, semantic (per theme) before core, in tokens.json order.
COLOUR = {}
for theme in ("light", "dark"):
    idx = {}
    for name, t in _leaves(TOK[theme]):
        if t["$type"] == "color":
            idx.setdefault(_resolve(t["$value"]), []).append((name, t["$extensions"]["source"]))
    for name, t in CORE.items():
        if t["$type"] == "color" and not re.search(r"\.(light|dark)(\.|$)", name) or (t["$type"] == "color" and f".{theme}" in name):
            idx.setdefault(t["$value"], []).append((name, t["$extensions"]["source"]))
    COLOUR[theme] = idx
DIM = {}
for group in ("radius", "space.scale", "size", "focusRing", "border.width"):
    for name, t in CORE.items():
        if name.startswith(group + ".") and t["$type"] == "dimension":
            DIM.setdefault((group, t["$value"]), name)
TYPE = {}
for name, t in CORE.items():
    if name.startswith("typography."):
        v = t["$value"]
        TYPE.setdefault((_resolve(v["fontSize"]), _resolve(v["lineHeight"]), str(_resolve(v["fontWeight"]))), name)
SHADOW = {}
for name, t in CORE.items():
    if t["$type"] == "shadow":
        SHADOW.setdefault(tuple((l["offsetX"], l["offsetY"], l["blur"], l["spread"], l["color"]) for l in t["$value"] if not l.get("inset")), name)
DUR = {}
for name, t in CORE.items():
    if name.startswith("motion.duration."):
        DUR.setdefault(t["$value"], name)
UNTOK = "untokenised"


def ctok(c, theme, key, state="default"):
    """A computed colour as the token that holds it."""
    if not c or c in ("transparent", "rgba(0, 0, 0, 0)"):
        return "transparent"
    h = _hex8(c)
    hits = COLOUR[theme].get(h)
    if hits:
        k = key if theme == "dark" else f"{key}.light"
        exact = [n for n, src in hits if f" {k} {state} " in src]
        own = [n for n, src in hits if f" {k} " in src]
        return f"`{(exact or own or [hits[0][0]])[0]}`"
    if len(h) == 9 and COLOUR[theme].get(h[:7]):
        return f"`{COLOUR[theme][h[:7]][0][0]}` @ {round(int(h[7:], 16) / 255, 2):g}"
    return f"{h} ({UNTOK})"


def dtok(v, *groups):
    for g in groups:
        if (g, v) in DIM:
            return f"`{DIM[(g, v)]}`"
    return v if v in ("0px", "auto") else f"{v} ({UNTOK})"


def hexa(c):
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", c or "")
    if not m:
        return c
    h = "#" + "".join("%02x" % round(float(x)) for x in m.groups()[:3])
    a = m.group(4)
    if a is None or float(a) >= 1:
        return h
    return "transparent" if float(a) == 0 else f"{h} @ {float(a):g}"


def _scale(transform):
    m = re.match(r"matrix\(([\d.]+), 0, 0, ([\d.]+), 0, 0\)", transform or "")
    return m.group(1) if m and m.group(1) == m.group(2) and m.group(1) != "1" else None


def row(v, theme, key, state="default"):
    if "error" in v:
        return {"error": v["error"]}
    s = v["style"]
    # The visible label's font: the first text node's parent when it is a child, else the element.
    f = v.get("textStyle") or s
    top, right, bottom, left = (dtok(s[f"padding{side}"], "space.scale") for side in ("Top", "Right", "Bottom", "Left"))
    if top == right == bottom == left:
        pad = top
    elif top == bottom and right == left:
        pad = f"{top} {right}"
    else:
        pad = f"{top} {right} {bottom} {left}"
    bw = s["borderTopWidth"]
    border = f"{dtok(bw, 'border.width')} {ctok(s['borderTopColor'], theme, key, state)}" if bw != "0px" and s["borderTopStyle"] != "none" else "none"
    if border == "none" and s["borderBottomWidth"] != "0px" and s["borderBottomStyle"] != "none":
        border = f"bottom {dtok(s['borderBottomWidth'], 'border.width')} {ctok(s['borderBottomColor'], theme, key, state)}"
    layers = tuple(_shadow(s["boxShadow"]))
    shadow = "none" if not layers else (f"`{SHADOW[layers]}`" if layers in SHADOW else f"{s['boxShadow'][-60:]} ({UNTOK})")
    font = TYPE.get((f["fontSize"], f["lineHeight"], str(f["fontWeight"])))
    font = f"`{font}`" if font else f"{f['fontSize']}/{f['lineHeight']} {f['fontWeight']} ({UNTOK})"
    if f.get("textTransform", "none") != "none":
        font += f", {f['textTransform']}"
    ol = ""
    if s.get("outlineStyle") not in (None, "none") and s.get("outlineWidth") not in ("0px", None) and not s["outlineColor"].endswith(", 0)"):
        ol = f"{dtok(s['outlineWidth'], 'focusRing')} {ctok(s['outlineColor'], theme, key, state)}, offset {dtok(s['outlineOffset'], 'focusRing')}"
    dur = s["transitionDuration"].split(",")[0].strip()
    ms = f"{round(float(dur[:-1]) * 1000)}ms" if dur.endswith("s") and not dur.endswith("ms") else dur
    out = {
        "size": f"{v['rect']['w']:g} x {v['rect']['h']:g}" + (f", scale {scale}" if (scale := _scale(s["transform"])) else ""),
        "padding": pad,
        "fill": ctok(s["backgroundColor"], theme, key, state),
        "border": border,
        "radius": dtok(s["borderTopLeftRadius"], "radius"),
        "text": f"{font}, {ctok(f['color'], theme, key, state)}",
        "shadow": shadow,
        "transition": "none" if s["transitionDuration"] in ("0s", "") else f"{s['transitionProperty'][:40]} " + (f"`{DUR[ms]}`" if ms in DUR else f"{ms} ({UNTOK})"),
    }
    if ol:
        out["focus ring"] = ol
    if v.get("icon"):
        out["icon"] = f"{v['icon']['w']:g}px"
    return out


def table(key):
    lines = []
    for theme, k in (("dark", key), ("light", f"{key}.light")):
        c = C.get(k)
        if not c or c.get("missing"):
            lines.append(f"{theme.capitalize()}: not found at capture time.")
            lines.append("")
            continue
        states = list(c["states"])
        rows = {st: row(c["states"][st], theme, key, st) for st in states}
        props = [p for p in ["size", "padding", "fill", "border", "radius", "text", "shadow", "focus ring", "icon", "transition", "error"] if any(p in r for r in rows.values())]
        lines.append(f"| {theme} | " + " | ".join(states) + " |")
        lines.append("|---|" + "---|" * len(states))
        for p in props:
            first = rows[states[0]].get(p, "-")
            cells = [str(rows[st].get(p, "-")) if i == 0 or rows[st].get(p, "-") != first else "=" for i, st in enumerate(states)]
            lines.append(f"| {p} | " + " | ".join(cells) + " |")
        crops = [c["states"][st].get("crop") for st in states if c["states"][st].get("crop")]
        if crops:
            lines.append("")
            lines.append("Crops: " + ", ".join(f"[{pathlib.Path(x).stem}]({x})" for x in crops) + ".")
        lines.append("")
    return lines


L = []
W = L.append
W("# TokenTracker components")
W("")
W(f"What TokenTracker v1.4.3's dashboard is built from, read on {J['_meta']['read']} from the local server the CLI runs (127.0.0.1:7680), no account signed in, in headless Chromium at 1440 x 900 and 2x. Every component was measured in dark (the default) and light. Each table shows the values that change across states; `=` repeats the first state.")
W("")
W("Every value is written as the token in [tokens.json](tokens.json) that holds it: semantic names (`bg.card`, `text.secondary`) come from the table's theme set, `color.*`, `space.scale.*`, `radius.*`, `typography.*`, `shadow.*` and `motion.*` from `core`. `@ 0.7` is a token at that opacity. A value no token holds is shown raw and marked untokenised; those are one-off sizes and paddings, not part of the system. `size` is the rendered box of that instance (it follows its content). `python3 tools/catalog.py export tokentracker` resolves every name; the raw computed styles are in [raw/measurements.md](raw/measurements.md).")
W("")
W("States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`:active:hover`), so nothing was pressed; `focused` and `filled` are a field clicked into and typed into, then cleared; `open` is a menu, tooltip, toast or dialog on screen; `disabled` is a control the page itself disables; `loading` and `error` are Sessions with its request held back or aborted in the capture browser; `checked` is a Skills row ticked and then cleared. Every request that is not a read was blocked, so no state saved, synced or removed anything. Private text (paths, session titles, skill names) was replaced in the page before any crop.")
W("")
W("## Pages captured")
W("")
pages = {}
for s in SHOTS:
    m = re.match(r"(mobile-)?(.+?)-(dark|light)-(.+)\.png$", s)
    if m:
        pages.setdefault((m.group(1) or "") + m.group(2), []).append(s)
W("| Page | Shots |")
W("|---|---|")
for p, fs in sorted(pages.items()):
    W(f"| {p} | " + ", ".join(f"[{f[:-4]}](screenshots/{f})" for f in fs) + " |")
W("")
W("## Shared values")
W("")
W("- **Hover** changes colour: nav items and menu options take a translucent neutral wash (`bg.hover`), tabs a solid one, outlined controls a stronger border. Light-theme outlined buttons turn their text and border green on hover. Two things also grow: the primary button scales to 1.03 and a heatmap cell to 1.25.")
W("- **Focus.** Mostly none: the stylesheet removes outlines and Tailwind rings on every element. A few controls override that with a 2px solid outline 2px out in the ink colour (`focusRing.*`, `focus.ring`): the sidebar's theme toggle, star pill and collapse chevron, and the Cloud page's buttons. Light text fields turn their border emerald on focus (`border.focus`). Everything else reads the same at `focus-visible` as at `default`.")
W("- **Pressed** looks like hover: no scale, no darker fill. The primary button is the exception: pressed takes one more neutral step.")
W("- **Disabled** controls are drawn, not faded: a filled neutral with muted text (`button.disabled.bg`, `text.disabled`). Switches are the exception: the whole control drops to 50% opacity.")
W("- **Motion.** Colour transitions run 150ms (nav, tabs, selects) or 200ms (buttons, tiles, fields) on cubic-bezier(0.4, 0, 0.2, 1). The dialog eases in over 260ms on cubic-bezier(0.16, 1, 0.3, 1).")
W("- **Radii** step 2, 4, 6, 8, 12, 16 and full; cards, the content panel and dialogs are 16, controls 8, tiles 12.")
W("")
W("## Components")
groups = []
for c in C.values():
    if c.get("group") and c["group"] not in groups:
        groups.append(c["group"])
for g in groups:
    W("")
    W(f"### {g}")
    for k, c in C.items():
        if k.endswith(".light") or c.get("group") != g:
            continue
        W("")
        W(f"#### {c.get('title') or k}")
        W("")
        desc = c.get("desc")
        W(f"`{k}` on /{c.get('page')}, found by `{c.get('selector')}`." + (f" {desc}" if desc else ""))
        W("")
        L.extend(table(k))
W("")
W("## Icons")
W("")
W(f"{len(ICONS)} Lucide icons (lucide-react, stroke 2, `currentColor`), named by their Lucide class, in [icons/](icons) with [icons/INDEX.tsv](icons/INDEX.tsv). Nav icons render at 15px, control icons at 14 to 16px. Provider logos, the pet and the menu bar art are brand material and were not collected.")
W("")
W("| Icon | Sizes | Where |")
W("|---|---|---|")
for f in ICONS:
    W(f"| [{f[1]}](icons/{f[0]}) | {f[3]} | {f[6]} |")
W("")
W("## Gaps")
W("")
W("- **Not captured: signed-in pages.** The signed-in Cloud page, Leaderboard and the account half of Settings need a TokenTracker account; none was signed in. Leaderboard shows other people's handles and avatars, so it was not captured; the signed-out account control stands in for an avatar.")
W("- **Not present: text area and radio.** No page in v1.4.3 renders either.")
W("- **The toast** is the share card's failure toast: Copy image cannot reach a clipboard in a headless browser, so the product reports \"Couldn't generate image\". The success toast (\"Image copied to clipboard\") was not reached.")
W("- **Switches are disabled** on every page reached: they work only with the Mac app connected. Their hover and focus states are not available.")
W("- **The field error** appears only after Test connection (or Save): the host was typed, Test connection was pressed, the check failed before any request, and the field was cleared. Save was never pressed.")
W("- **Not captured: phone-width components.** The 390-wide layouts are in the `mobile-*` screenshots only; no component was measured at that width.")
W("- **Not tokenised: provider colours.** The per-tool colours in the share bar, tiles and charts come from `getProviderColor()` in the dashboard source.")
W("- **Status badge** reads the `CACHED` pill on Limits; `STALE` and `RE-AUTH` did not appear on this machine.")
(HERE / "components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", sum(1 for k in C if not k.endswith(".light")), "components")
