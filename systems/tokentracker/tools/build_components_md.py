#!/usr/bin/env python3
"""Build components.md for TokenTracker from raw/components-computed.json, icons/INDEX.tsv and screenshots/.

One entry per component: what it is, its crops in dark and light, and a compact table of the values
that change between states (size, padding, fill, border, radius, text, transition). The full
property dump per state is raw/measurements.md. Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
J = json.loads((HERE / "raw" / "components-computed.json").read_text())
C = J["components"]
SHOTS = sorted(p.name for p in (HERE / "screenshots").glob("*.png"))
ICONS = [l.split("\t") for l in (HERE / "icons" / "INDEX.tsv").read_text().splitlines()[1:] if l.strip()]


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


def row(v):
    if "error" in v:
        return {"error": v["error"]}
    s = v["style"]
    # The visible label's font: the first text node's parent when it is a child, else the element.
    f = v.get("textStyle") or s
    top, right, bottom, left = (s[f"padding{side}"] for side in ("Top", "Right", "Bottom", "Left"))
    if top == right == bottom == left:
        pad = top
    elif top == bottom and right == left:
        pad = f"{top} {right}"
    else:
        pad = f"{top} {right} {bottom} {left}"
    bw = s["borderTopWidth"]
    border = f"{bw} {hexa(s['borderTopColor'])}" if bw != "0px" and s["borderTopStyle"] != "none" else "none"
    if border == "none" and s["borderBottomWidth"] != "0px" and s["borderBottomStyle"] != "none":
        border = f"bottom {s['borderBottomWidth']} {hexa(s['borderBottomColor'])}"
    shadow = "none" if s["boxShadow"] == "none" or not re.search(r"rgba?\((?!0, 0, 0, 0\))", s["boxShadow"]) else "yes"
    font = f"{f['fontSize']}/{f['lineHeight']} {f['fontWeight']}"
    ls = f.get("letterSpacing", "normal")
    if ls != "normal":
        font += f", tracking {ls}"
    if f.get("textTransform", "none") != "none":
        font += f", {f['textTransform']}"
    out = {
        "size": f"{v['rect']['w']:g} x {v['rect']['h']:g}" + (f", scale {scale}" if (scale := _scale(s["transform"])) else ""),
        "padding": pad,
        "fill": hexa(s["backgroundColor"]),
        "border": border,
        "radius": s["borderTopLeftRadius"],
        "text": f"{font}, {hexa(f['color'])}",
        "shadow": shadow,
        "transition": "none" if s["transitionDuration"] in ("0s", "") else f"{s['transitionProperty'][:48]} {s['transitionDuration']}",
    }
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
        rows = {st: row(c["states"][st]) for st in states}
        props = [p for p in ["size", "padding", "fill", "border", "radius", "text", "shadow", "icon", "transition", "error"] if any(p in r for r in rows.values())]
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
W(f"What TokenTracker v1.3.5's dashboard is built from, read on {J['_meta']['read']} from the local server the CLI runs (127.0.0.1:7680), no account signed in, in headless Chromium at 1440 x 900 and 2x. Every component was measured in dark (the default) and light. Each table shows the values that change across states; `=` repeats the first state. The full computed styles are in [raw/measurements.md](raw/measurements.md); the tokens in [tokens.json](tokens.json).")
W("")
W("States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`:active:hover`), so nothing was pressed; `focused` and `filled` are a field clicked into and typed into, then cleared; `open` is a menu or dialog the page opened itself. Private text (paths, session titles, skill names) was replaced in the page before any crop.")
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
W("- **Focus.** None. TokenTracker's stylesheet removes every Tailwind focus ring, so `focus-visible` reads the same as `default` in every table below.")
W("- **Pressed** looks like hover: no scale, no darker fill.")
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
W("- **Not captured: signed-in pages.** Cloud, Leaderboard and the account half of Settings need a TokenTracker account; none was signed in. Leaderboard would also show other people's handles.")
W("- **Not captured: toasts and validation errors.** No action that raises a toast or a form error was taken (nothing was saved, copied or submitted).")
W("- **Not captured: destructive confirmation.** The dashboard has no delete flow reachable without changing data.")
W("- **Not captured: phone-width components.** The 390-wide layouts are in the `mobile-*` screenshots only; no component was measured at that width.")
W("- **Not tokenised: provider colours.** The per-tool colours in the share bar, tiles and charts come from `getProviderColor()` in the dashboard source.")
W("- **Status badge** (`STALE`, `RE-AUTH`) was found by text and its reading is the badge's wrapper; read its dot and pill from the crops and screenshots.")
(HERE / "components.md").write_text("\n".join(L) + "\n")
print("components.md:", len(L), "lines,", sum(1 for k in C if not k.endswith(".light")), "components")
