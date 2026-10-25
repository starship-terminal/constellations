#!/usr/bin/env python3
"""Read Raycast's sizes, a few type sizes and a sample of its colours out of the full-colour window captures.

    python3 tools/measure.py ~/.design-systems/raycast-desktop/raw-shots

Adapted from the native kit (systems/grokbot, by way of systems/zed-desktop). RAW holds dark/ and
light/ sRGB captures written by tools/capture/shot.sh: the launcher ("Main Window", 1500 x 950 px,
the 750 x 475 pt window at 2 px per pt) and the Settings window (1600 x 1728 px). Writes
raw/readings.json (every reading with its file, box, method, value and evidence label) and
raw/raycast-desktop-measured.md (the same as tables). tools/build_tokens.py reads raw/readings.json.

Colours do not come from here: they come from Raycast's own shipped theme definitions and
stylesheet (raw/bundled-themes.json, raw/css-tokens.json, written by tools/capture/read_bundle.py).
The `px.*` readings below are the pixel check of those declarations: build_tokens.py composites
each declared translucent role over the window fill it sits on and compares the result with the
pixel, writing raw/pixel-check.json.

Ops:
  fill   the dominant colour of a box and its share                       Sampled when share >= 90%
  text   the anti-aliased pixel furthest from the fill (a glyph colour)    Sampled (text)
  span   the run of pixels within tol of the colour at a point, along a
         row or column: a bar's or a control's size in pt                  Sampled
  bbox   the bounding box of pixels within tol of the colour at a point   Sampled
  corner corner radius fitted to the insets of the corner's first rows  Derived (about +-0.5 pt)
  cap    a capital's ink height less one pixel of anti-aliasing           Derived (the size it implies
                                                                           depends on the font's cap ratio)
  dims   the capture's size in pt                                         Sampled
Standard library only (tools/capture/native/sample.py). Deterministic.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(HERE / "capture" / "native"))
import sample  # noqa: E402

NAME = "Raycast"
SLUG = PKG.name
SCALE = 2

# id: (capture, op, args, note). "dark/..." or "light/..." reads one theme; otherwise both.
# Boxes are capture pixels. Launcher and Settings layouts are the same in both themes, except that
# the light pass ran with Follow System Appearance off, so Settings > General shows one Theme row
# where dark shows Dark Theme and Light Theme (only the first card is read).
R = {
    # ------------------------------------------------ pixel check of the declared roles (launcher)
    "px.window.main":       ("00-root", "fill", (700, 100, 300, 20), "Launcher window behind the search field"),
    "px.list.selected":     ("00-root", "fill", (900, 140, 300, 40), "Selected row (the first result)"),
    "px.list.hover":        ("04-root-hover", "fill", (900, 520, 200, 30), "Hovered row (Orca), pointer over it"),
    "px.text.primary":      ("00-root", "text", (100, 290, 300, 40), "Row title ('Telegram')"),
    "px.text.secondary":    ("00-root", "text", (1320, 290, 150, 40), "Row accessory ('Application')"),
    "px.text.sectionHeader": ("00-root", "text", (30, 225, 150, 35), "Section header ('Suggestions')"),
    "px.text.placeholder":  ("00-root", "text", (110, 40, 500, 50), "Search field placeholder"),
    "px.actionBar.pill":    ("00-root", "fill", (1300, 880, 150, 10), "Action bar pill (macOS glass), right of the primary action"),
    "px.actionBar.button":  ("00-root", "fill", (40, 870, 20, 10), "Round menu button left of the action bar"),
    # ------------------------------------------------ pixel check (settings window)
    "px.window.settings":   ("20-settings-general", "fill", (1200, 40, 200, 40), "Settings window behind the cards"),
    "px.settings.card":     ("20-settings-general", "fill", (1200, 240, 200, 40), "Settings card (section content)"),
    "px.settings.separator": ("20-settings-general", "fill", (1000, 196, 300, 2), "Line between two card rows"),
    "px.sidebar":           ("20-settings-general", "fill", (380, 1100, 60, 30), "Settings sidebar, right of a row label"),
    "px.sidebar.selected":  ("20-settings-general", "fill", (360, 336, 60, 30), "Selected sidebar row ('General')"),
    "px.switch.on":         ("20-settings-general", "fill", (1478, 140, 18, 18), "Switch on (Open at Login), track left of the thumb"),
    "px.switch.off":        ("20-settings-general", "fill", (1528, 238, 8, 12), "Switch off (Show In Menu Bar), track right of the thumb"),
    # ------------------------------------------------ launcher layout
    "size.window.main":     ("00-root", "dims", (), "Launcher window"),
    "box.row":              ("00-root", "bbox", ((900, 165), (0, 110, 1500, 100), 3), "Selected row: its box (the top is the search header's height, the left the list inset)"),
    "size.row":             ("00-root", "span", ("col", 900, 165, 3), "Selected row height"),
    "radius.row":           ("00-root", "corner", (16, 128), "Selected row corner (top left)"),
    "cap.input":            ("00-root", "cap", (104, 40, 128, 95), "'S' of the search placeholder"),
    "cap.rowTitle":         ("00-root", "cap", (100, 285, 118, 330), "'T' of 'Telegram'"),
    "cap.sectionHeader":    ("00-root", "cap", (32, 225, 47, 262), "'S' of 'Suggestions'"),
    # ------------------------------------------------ settings layout
    "size.window.settings": ("20-settings-general", "dims", (), "Settings window"),
    "size.settings.row":    ("20-settings-general", "span", ("col", 1200, 150, 3), "Settings card row height"),
    "radius.settings.card": ("dark/20-settings-general", "corner", (504, 104), "Settings card corner (top left; dark only, light's card is 2.5% off white and the fit fails)"),
    "size.switch":          ("20-settings-general", "bbox", ((1480, 150), (1460, 125, 100, 50), 12), "Switch on, accent-coloured box"),
    "size.sidebarSearch.h": ("20-settings-general", "span", ("col", 300, 120, 3), "Sidebar search field height"),
    "size.sidebarSearch.w": ("20-settings-general", "span", ("row", 120, 300, 3), "Sidebar search field width"),
    "size.sidebar.selected": ("20-settings-general", "span", ("col", 400, 350, 3), "Selected sidebar row height"),
    "size.sidebar":         ("20-settings-general", "span", ("row", 1100, 400, 3), "Settings sidebar width (an inset panel inside the window)"),
}


def op_dims(rows):
    return {"value": f"{len(rows[0]) / SCALE:g}x{len(rows) / SCALE:g}pt", "evidence": "Sampled"}


def d(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def hexof(p):
    return "#{:02X}{:02X}{:02X}".format(*p[:3])


def op_fill(rows, x, y, w, h):
    colour, share = sample.fill(rows, x, y, w, h)
    return {"value": hexof(colour), "share": round(share, 2), "evidence": "Sampled" if share >= 0.9 else "Derived"}


def op_text(rows, x, y, w, h, dark=False):
    return {"value": hexof(sample.text(rows, x, y, w, h, dark=dark)), "evidence": "Sampled (text)"}


def op_span(rows, axis, line, at, tol):
    pix = (lambda i: rows[line][i]) if axis == "row" else (lambda i: rows[i][line])
    n = len(rows[0]) if axis == "row" else len(rows)
    ref = pix(at)
    a = at
    while a > 0 and d(pix(a - 1), ref) <= tol:
        a -= 1
    b = at
    while b < n - 1 and d(pix(b + 1), ref) <= tol:
        b += 1
    return {"value": f"{(b - a + 1) / SCALE:g}pt", "from": a, "to": b, "colour": hexof(ref), "evidence": "Sampled"}


def op_bbox(rows, point, window, tol):
    ref = rows[point[1]][point[0]]
    x0, y0, w, h = window
    xs, ys = [], []
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            if d(rows[y][x], ref) <= tol:
                xs.append(x)
                ys.append(y)
    bw, bh = (max(xs) - min(xs) + 1) / SCALE, (max(ys) - min(ys) + 1) / SCALE
    return {"value": f"{bw:g}x{bh:g}pt", "box": [min(xs), min(ys), max(xs), max(ys)], "colour": hexof(ref), "evidence": "Sampled"}


def op_outer(rows, axis, line, a, b, refpt, tol):
    """First and last pixel along a line, between a and b, within tol of a border colour: the
    outer size of a control drawn as a 1 pt border on a fill like its surroundings."""
    ref = rows[refpt[1]][refpt[0]]
    pix = (lambda i: rows[line][i]) if axis == "row" else (lambda i: rows[i][line])
    hits = [i for i in range(a, b) if d(pix(i), ref) <= tol]
    return {"value": f"{(hits[-1] - hits[0] + 1) / SCALE:g}pt", "from": hits[0], "to": hits[-1], "colour": hexof(ref), "evidence": "Sampled"}


def op_corner(rows, x, y, tol=3):
    """Corner radius fitted to the corner's outline. (x, y) is the top-left pixel of the box's outer
    edge. For each of the first 20 rows, find how far in from x the shape starts (the first pixel that
    differs from the background just outside the corner); fit the circle r - sqrt(r^2 - (r - i - 0.5)^2)
    to those insets, r in quarter pixels."""
    bg = rows[y - 3][x - 3]
    ins = []
    for i in range(20):
        j = 0
        while j < 30 and d(rows[y + i][x + j], bg) <= tol:
            j += 1
        ins.append(j)

    def model(r, i):
        return r - (r * r - (r - i - 0.5) ** 2) ** 0.5 if i + 0.5 < r else 0.0

    best = min((sum((model(q / 4, i) - o) ** 2 for i, o in enumerate(ins)), q / 4) for q in range(0, 121))
    return {"value": f"{best[1] / SCALE:g}pt", "insets": ins[:8], "evidence": "Derived"}


def op_inset(rows, axis, line, start, thr=40):
    """Distance from a start pixel to the first pixel that differs from it by more than thr (ink)."""
    pix = (lambda i: rows[line][i]) if axis == "row" else (lambda i: rows[i][line])
    ref = pix(start)
    i = start
    while d(pix(i), ref) <= thr:
        i += 1
    return {"value": f"{(i - start) / SCALE:g}pt", "from": start, "to": i, "evidence": "Sampled"}


def op_cap(rows, x0, y0, x1, y1):
    bg = rows[y0][x0]
    ys = [y for y in range(y0, y1) if any(d(rows[y][x], bg) > 30 for x in range(x0, x1))]
    ink = ys[-1] - ys[0] + 1
    return {"value": f"{(ink - 1) / SCALE:g}pt", "inkPx": ink, "top": ys[0], "evidence": "Derived"}


def run(raw):
    raw = pathlib.Path(raw).expanduser()
    if not (raw / "dark").is_dir():
        raise SystemExit(f"{raw}: no dark/ captures; nothing written")
    # One decoded capture at a time: a decoded capture is several hundred MB as Python tuples, so
    # the readings are grouped by capture and each image is released before the next is read.
    jobs = {}
    for rid, (cap, op, args, note) in R.items():
        name = cap.split("/")[-1]
        for theme in required_themes(cap):
            jobs.setdefault(f"{theme}/{name}", []).append((rid, op, args, note))
    out = {}
    for key in sorted(jobs):
        theme, name = key.split("/")
        png = raw / theme / f"{name}.png"
        if not png.exists():
            continue
        rows = sample.read_png(png)[2]
        for rid, op, args, note in jobs[key]:
            if op == "text":
                res = op_text(rows, *args, dark=(theme == "dark"))
            else:
                res = globals()["op_" + op](rows, *args)
            res.update({"capture": f"screenshots/{theme}/{name}.png", "op": op,
                        "args": json.loads(json.dumps(args)), "note": note})
            out.setdefault(rid, {})[theme] = res
        del rows
    return out


def required_themes(cap):
    """A capture named "dark/..." or "light/..." is read in that theme only; any other in both."""
    return [cap.split("/")[0]] if "/" in cap else ["dark", "light"]


def write(readings):
    (PKG / "raw").mkdir(exist_ok=True)
    (PKG / "raw" / "readings.json").write_text(json.dumps(readings, indent=1, sort_keys=True) + "\n")
    lines = [f"# {NAME}: measured readings", "",
             "Generated by `tools/measure.py` from the full-colour window captures (1500 x 950 px for the launcher, "
             "1600 x 1728 px for the Settings window, 2 px per pt). Boxes are capture pixels; the committed screenshots are "
             "the same captures quantised to 256 colours, so a box can be checked against them, but values were read from "
             "the full-colour copies. `px.*` readings are the pixel check of the declared theme; see `pixel-check.json`.", "",
             "| Reading | Theme | Value | Evidence | Method | Capture | Note |", "|---|---|---|---|---|---|---|"]
    for rid in sorted(readings):
        for theme, r in sorted(readings[rid].items()):
            extra = f" ({round(r['share'] * 100)}% of box)" if "share" in r else ""
            lines.append(f"| `{rid}` | {theme} | {r['value']}{extra} | {r['evidence']} | {r['op']} {r['args']} | "
                         f"[{r['capture'].split('/')[-1]}](../{r['capture']}) | {r['note']} |")
    (PKG / "raw" / f"{SLUG}-measured.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    readings = run(sys.argv[1] if len(sys.argv) > 1 else f"~/.design-systems/{SLUG}/raw-shots")
    missing = sorted(f"{rid} ({theme})" for rid, (cap, *_) in R.items() for theme in required_themes(cap)
                     if theme not in readings.get(rid, {}))
    if missing:   # every reading in every theme it needs, or nothing is written
        raise SystemExit(f"no capture for {len(missing)} readings ({', '.join(missing[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
