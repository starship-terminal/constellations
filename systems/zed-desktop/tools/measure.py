#!/usr/bin/env python3
"""Read Zed's sizes, type and a sample of its colours out of the full-colour window captures.

    python3 tools/measure.py ~/.design-systems/zed-desktop/raw-shots

Adapted from the native kit (systems/grokbot). RAW holds dark/ and light/ sRGB captures of Zed's
main window, 3024 x 1898 px (the 1512 x 949 pt window at 2 px per pt), or of its Settings window
(1800 x 1500 px), written by tools/capture/shot.sh. Writes raw/readings.json (every reading with
its file, box, method, value and evidence label) and raw/zed-desktop-measured.md (the same as
tables). tools/build_tokens.py reads raw/readings.json.

Colours do not come from here: they come from Zed's own theme file (raw/one.json). The `fill`
readings below are the pixel check of that file: build_tokens.py compares each with the theme
key it names and writes the result to raw/pixel-check.json.

Ops:
  fill   the dominant colour of a box and its share                       Sampled when share >= 90%
  text   the anti-aliased pixel furthest from the fill (a glyph colour)    Sampled (text)
  span   the run of pixels within tol of the colour at a point, along a
         row or column: a bar's or a control's size in pt                  Sampled
  bbox   the bounding box of pixels within tol of the colour at a point   Sampled
  corner corner radius fitted to the insets of the corner's first rows  Derived (about +-0.5 pt)
  outer  first and last pixel of a border colour along a line: a
         bordered control's outer size in pt                         Sampled
  inset  pixels from a start point to the first ink                    Sampled
  cap    a capital's ink height less one pixel of anti-aliasing           Derived (the size it implies
                                                                           depends on the font's cap ratio)
Standard library only (tools/capture/native/sample.py). Deterministic.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(HERE / "capture" / "native"))
import sample  # noqa: E402

NAME = "Zed"
SLUG = PKG.name
SCALE = 2

# id: (capture, op, args, note). "dark/..." or "light/..." reads one theme; otherwise both.
# Boxes are capture pixels. The main window's layout is the same in both themes except the
# file tree, which gained hello.txt (written by the dark run's agent prompt) before the light run.
R = {
    # ------------------------------------------------ pixel check of the theme file (fill = key)
    "px.title_bar.background":       ("01-editor-python", "fill", (1500, 16, 300, 40), "Title bar"),
    "px.border":                     ("01-editor-python", "fill", (1500, 68, 300, 2), "Line under the title bar (2 px = 1 pt)"),
    "px.tab_bar.background":         ("01-editor-python", "fill", (1300, 80, 300, 40), "Tab bar right of the only tab"),
    "px.tab.active_background":      ("01-editor-python", "fill", (500, 74, 120, 8), "Active tab, above its label"),
    "px.panel.background":           ("01-editor-python", "fill", (100, 1200, 300, 300), "Project panel below the rows"),
    "px.editor.background":          ("01-editor-python", "fill", (1600, 1300, 600, 300), "Editor below the last line"),
    "px.editor.gutter.background":   ("01-editor-python", "fill", (490, 1300, 60, 300), "Gutter below the last line number"),
    "px.editor.active_line.background": ("01-editor-python", "fill", (2400, 228, 400, 20), "Line 1 (the cursor's line), right of the inline blame"),
    "px.toolbar.background":         ("01-editor-python", "fill", (1200, 140, 300, 10), "Breadcrumb toolbar"),
    "px.status_bar.background":      ("01-editor-python", "fill", (1000, 1845, 400, 10), "Status bar"),
    "px.border.variant":             ("01-editor-python", "fill", (1500, 222, 300, 2), "Line under the breadcrumb toolbar"),
    "px.elevated_surface.background": ("05-command-palette", "fill", (1700, 700, 300, 200), "Command palette list, right of the labels"),
    "px.element.selected":           ("05-command-palette", "fill", (1500, 250, 300, 50), "Command palette, selected row"),
    "px.terminal.background":        ("13-terminal-panel", "fill", (1500, 1500, 600, 200), "Terminal panel, empty area"),
    "px.version_control.modified":   ("01-editor-python", "fill", (481, 310, 5, 24), "Gutter bar, modified line 4"),
    "px.version_control.added":      ("01-editor-python", "fill", (481, 648, 5, 76), "Gutter bar, added lines 16 to 18"),
    "px.text":                       ("05-command-palette", "text", (930, 390, 400, 40), "Command palette item label"),
    "px.text.status":                ("01-editor-python", "text", (2170, 1850, 90, 34), "Status bar cursor position ('1:1')"),
    # ------------------------------------------------ window layout (main window, column x=2000)
    "size.titleBar":   ("01-editor-python", "span", ("col", 2000, 30, 3), "Title bar height"),
    "size.tabBar":     ("01-editor-python", "span", ("col", 2000, 100, 3), "Tab bar height"),
    "size.toolbar":    ("01-editor-python", "span", ("col", 2000, 180, 3), "Breadcrumb toolbar height"),
    "size.statusBar":  ("01-editor-python", "span", ("col", 2000, 1860, 3), "Status bar height"),
    "size.projectPanel": ("01-editor-python", "span", ("row", 1200, 200, 3), "Project panel width, border excluded"),
    "size.activeTab":  ("01-editor-python", "span", ("row", 76, 600, 3), "Active tab width ('inventory.py')"),
        "size.treeRow":    ("light/01-editor-python", "span", ("col", 300, 150, 3), "Selected file-tree row (light; in dark the first row's fill runs into the title bar's border)"),
    "size.gutterLine": ("01-editor-python", "span", ("col", 483, 320, 12), "One buffer line, from the modified bar on line 4"),
    # ------------------------------------------------ palette, menu, tooltip, button
    "size.palette.w":      ("05-command-palette", "span", ("row", 240, 1500, 3), "Command palette inner width"),
    "size.palette.query":  ("05-command-palette", "span", ("col", 1500, 200, 3), "Palette query field height"),
    "size.palette.row":    ("05-command-palette", "span", ("col", 2060, 270, 3), "Palette row height (selected row)"),
    "radius.palette":      ("05-command-palette", "corner", (902, 160), "Palette corner (top left)"),
    "size.menu.w":         ("16-context-menu-file", "outer", ("row", 700, 100, 560, (120, 700), 4), "File context menu width, border to border"),
    "radius.menu":         ("18-context-menu-tab", "corner", (940, 100), "Tab context menu corner (top left)"),
    "size.tooltip.h":      ("20-tooltip", "outer", ("col", 2800, 1780, 1870, (2800, 1799), 4), "Tooltip height, border to border"),
    "radius.tooltip":      ("20-tooltip", "corner", (2678, 1799), "Tooltip corner (top left)"),
    "size.button.h":       ("00-launch", "outer", ("col", 2850, 0, 68, (2850, 10), 4), "'Restart to Update' button height, border to border"),
    "size.button.w":       ("00-launch", "outer", ("row", 15, 2600, 2950, (2665, 15), 4), "'Restart to Update' button with its dismiss part, border to border"),
    "radius.button":       ("00-launch", "corner", (2664, 10), "'Restart to Update' corner (top left)"),
    # ------------------------------------------------ settings window controls
    "size.switch.w":       ("32-settings-general", "outer", ("row", 506, 1600, 1760, (1666, 506), 4), "Switch track width, border to border"),
    "size.switch.h":       ("32-settings-general", "outer", ("col", 1718, 470, 540, (1718, 488), 4), "Switch track height, border to border"),
    "size.switch.thumb":   ("32-settings-general", "span", ("row", 506, 1680, 3), "Switch thumb width (off)"),
    "size.select.h":       ("32-settings-general", "outer", ("col", 1600, 650, 740, (1600, 667), 4), "Select ('Platform Default') height, border to border"),
    "size.navRow.h":       ("32-settings-general", "outer", ("col", 200, 150, 230, (200, 160), 4), "Settings nav, selected row height, border to border"),
    "size.search.h":       ("32-settings-general", "outer", ("col", 300, 60, 150, (300, 80), 4), "Settings search field height, border to border"),
    "radius.select":       ("32-settings-general", "corner", (1460, 667), "Select corner (top left)"),
    "radius.switch":       ("32-settings-general", "corner", (1666, 488), "Switch track corner (top left)"),
    "px.switch.on":        ("32-settings-general", "fill", (1670, 1300, 24, 10), "Switch on, track (Use System Path Prompts)"),
    "px.switch.off":       ("32-settings-general", "fill", (1700, 498, 24, 6), "Switch off, track"),
    # ------------------------------------------------ agent panel
    "size.userMessage.h":  ("52-agent-result", "outer", ("col", 2600, 140, 240, (2600, 150), 4), "User message box height, border to border"),
    "radius.userMessage":  ("52-agent-result", "corner", (1770, 150), "User message corner (top left)"),
    "radius.navRow":       ("32-settings-general", "corner", (20, 160), "Settings nav, selected row corner (top left)"),
    "size.toolCardHeader": ("dark/52-agent-result", "span", ("col", 2600, 290, 3), "Terminal tool card header (dark)"),
    "size.sendButton":     ("44-agent-thread-empty", "bbox", ((2965, 1780), (2940, 1760, 84, 70), 3), "Send button"),
    # ------------------------------------------------ insets (spacing)
    "inset.paletteRowMargin": ("dark/05-command-palette", "span", ("row", 276, 906, 3), "Palette border to the selected row's fill"),
    "inset.paletteRowText": ("dark/05-command-palette", "inset", ("row", 276, 912), "Selected row's left edge to its label"),
    "inset.menuItem":    ("dark/16-context-menu-file", "inset", ("row", 396, 122), "Menu border to an item label"),
    "inset.tabLabel":    ("dark/01-editor-python", "inset", ("row", 100, 481), "Tab's left edge to its label (close button slot on the left)"),
    "inset.treeIcon":    ("dark/01-editor-python", "inset", ("row", 148, 2), "Window edge to a file-tree icon"),
    "inset.userMessage": ("dark/52-agent-result", "inset", ("row", 190, 1772), "User message border to its text"),
    "inset.settingsPage": ("dark/32-settings-general", "inset", ("row", 290, 452), "Settings sidebar border to the page title"),
    "size.settingsSidebar": ("dark/32-settings-general", "span", ("row", 1300, 300, 3), "Settings sidebar width, border excluded"),
    # ------------------------------------------------ type: capital ink heights
    "cap.tree":       ("dark/01-editor-python", "cap", (59, 125, 73, 175), "'N' of 'NOTES.md' in the file tree"),
    "cap.treeL":      ("light/01-editor-python", "cap", (59, 177, 73, 227), "'N' of 'NOTES.md' in the file tree"),
    "cap.buffer":     ("01-editor-python", "cap", (610, 300, 624, 345), "'M' of 'MAX_ITEMS' in the buffer (Menlo)"),
    "cap.settingsTitle": ("32-settings-general", "cap", (516, 265, 528, 320), "'G' of the 'General' page title"),
    "cap.settingsRow": ("32-settings-general", "cap", (518, 425, 532, 470), "'A' of the 'Accessible Mode' row label"),
    "cap.settingsDesc": ("32-settings-general", "cap", (516, 470, 532, 510), "'O' of the row description"),
    "cap.mdH1":       ("26-markdown-preview", "cap", (1808, 160, 1820, 225), "'C' of the Markdown preview's H1"),
    "cap.mdBody":     ("26-markdown-preview", "cap", (1811, 262, 1823, 300), "'A' of a Markdown preview paragraph"),
    "cap.agentBody":  ("dark/52-agent-result", "cap", (1795, 700, 1809, 745), "'T' of an agent reply paragraph"),
    "cap.agentHeading": ("dark/52-agent-result", "cap", (1795, 640, 1807, 690), "'D' of an agent reply heading ('Done')"),
}


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
    cache, out = {}, {}
    for rid, (cap, op, args, note) in R.items():
        themes = [cap.split("/")[0]] if "/" in cap else ["dark", "light"]
        name = cap.split("/")[-1]
        for theme in themes:
            png = raw / theme / f"{name}.png"
            if not png.exists():
                continue
            key = f"{theme}/{name}"
            if key not in cache:
                cache[key] = sample.read_png(png)[2]
            rows = cache[key]
            if op == "text":
                res = op_text(rows, *args, dark=(theme == "dark"))
            else:
                res = globals()["op_" + op](rows, *args)
            res.update({"capture": f"screenshots/{theme}/{name}.png", "op": op,
                        "args": json.loads(json.dumps(args)), "note": note})
            out.setdefault(rid, {})[theme] = res
    return out


def write(readings):
    (PKG / "raw").mkdir(exist_ok=True)
    (PKG / "raw" / "readings.json").write_text(json.dumps(readings, indent=1, sort_keys=True) + "\n")
    lines = [f"# {NAME}: measured readings", "",
             "Generated by `tools/measure.py` from the full-colour window captures (3024 x 1898 px for the main window, "
             "1800 x 1500 px for the Settings window, 2 px per pt). Boxes are capture pixels; the committed screenshots are "
             "the same captures quantised to 256 colours, so a box can be checked against them, but values were read from "
             "the full-colour copies. `px.*` readings are the pixel check of the theme file; see `pixel-check.json`.", "",
             "| Reading | Theme | Value | Evidence | Method | Capture | Note |", "|---|---|---|---|---|---|---|"]
    for rid in sorted(readings):
        for theme, r in sorted(readings[rid].items()):
            extra = f" ({round(r['share'] * 100)}% of box)" if "share" in r else ""
            lines.append(f"| `{rid}` | {theme} | {r['value']}{extra} | {r['evidence']} | {r['op']} {r['args']} | "
                         f"[{r['capture'].split('/')[-1]}](../{r['capture']}) | {r['note']} |")
    (PKG / "raw" / f"{SLUG}-measured.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    readings = run(sys.argv[1] if len(sys.argv) > 1 else f"~/.design-systems/{SLUG}/raw-shots")
    missing = sorted(rid for rid in R if rid not in readings)
    if missing:
        raise SystemExit(f"no capture for {len(missing)} readings ({', '.join(missing[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
