#!/usr/bin/env python3
"""Read a native app's values out of the full-colour iPhone Mirroring captures (native kit).

    python3 tools/measure.py ~/.design-systems/<slug>/raw-shots

Copied from the native kit (tools/kit/native, from systems/grokbot) and adapted for Arc Search: NAME,
the capture names and the reading table R, whose boxes are capture pixels on Arc Search's screens. Two
additions come from systems/youtube: an entry can give a box per theme (the light captures are laid out
differently), and a `corner` op reads the radius of a corner with no flat fill inside it.

RAW holds dark/ and light/ sRGB captures (812 x 1780 px, the 390 x 844 pt screen at 2 px per pt,
offset 16, 76 inside the PNG), as written by tools/capture/native/shot.sh. Writes raw/readings.json
(every reading with its file, box, method, value and evidence label) and raw/<slug>-measured.md
(the same as tables). tools/build_tokens.py reads only raw/readings.json.

Each reading is one of:
  fill    the dominant colour of a box and its share of the box            Sampled when share >= 90%
  text    the anti-aliased pixel furthest from the fill (a glyph colour)    Sampled (text)
  bbox    the bounding box of pixels close to the colour at a point,
          inside a window: a control's width and height in pt             Sampled
  extent  first and last pixel along a line that differs from a
          background point: the size of a glass control                    Sampled
  find    positions along a line whose colour is close to a reference      Sampled
  span    first and last sharp step along a line: the size of a glass
          control whose fill drifts (about +-1 pt)                         Derived
  mean    the mean colour of a box: glass over content, or a gradient     Derived
  diag    corner radius from the inset along the corner's diagonal        Derived (about +-2 pt)
  corner  the same for a picture's corner, from where its straight edges meet, against the page
                                                                            Derived (about +-2 pt)
  lines   ink bands in a block of text: the line pitch (line height)         Derived (about +-1 pt)
  cap     the ink height of one capital letter less one pixel of anti-aliasing, and the font
          size it implies at a cap height of 0.72 em, rounded to a point    Derived (about +-1 pt)

Standard library only (tools/capture/native/sample.py). Deterministic.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(HERE / "capture" / "native"))
import sample  # noqa: E402

NAME = "Arc Search"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# The captures, by short name. Both themes have all 24 under the same names; 01, 02, 18 (the page behind the
# launcher), 03 and 11 (the page) and 06, 07 (scroll position) differ between them.
LAUNCH, TYPED, PAGE, TABS, SETTINGS, SCROLLED = ("01-launch-search-focused-pinned", "02-search-typed-suggestions",
                                                 "03-page-bottom-toolbar", "04-tab-switcher-cards", "05-settings-sheet",
                                                 "06-settings-scrolled-header-blur")
POPUP, ENGINE, SITE, ICON, MENU, MENUC = ("07-popup-menu-archive-tabs", "08-settings-search-engine-checklist",
                                          "09-site-settings-switches", "10-app-icon-sheet", "12-page-menu-address-actions",
                                          "13-page-menu-collapsed")
FIND, FINDM, FINDN, SPACE, LONG = ("14-find-bar-focused", "15-find-bar-typed-match", "16-find-bar-no-results",
                                   "17-space-sheet-gradient", "19-longpress-favorite-menu")
ARCHIVE, EDIT, ASEARCH, ABLANK = ("20-archive-history-list", "21-edit-menu-destructive-item", "22-archive-search-typed",
                                  "23-archive-search-no-results-blank")

# id: (capture, op, args, note), or {"dark": (capture, op, args), "light": (capture, op, args), "note": note}
# when the two themes need different boxes. Captures without a theme prefix are read in both themes when
# the file exists in both; "dark/..." or "light/..." reads one theme only. No box touches the regions masked
# in 19, 20, 21 and 24 (a hostname and two history rows).
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- settings sheet
    "bg.sheet":           (SETTINGS, "fill", (100, 990, 600, 16), "Settings sheet, between two groups"),
    "bg.behindSheet":     (SETTINGS, "mean", (60, 140, 200, 20), "The page behind the Settings sheet, dimmed (above the sheet's top edge)"),
    "surface.group":      (SETTINGS, "fill", (420, 1045, 120, 40), "Grouped list card (Search Engine row, between label and value)"),
    "surface.button":     (SETTINGS, "fill", (350, 340, 50, 50), "Downloads button, right of its label"),
    "surface.navButton":  (SETTINGS, "mean", (636, 225, 10, 20), "Done button left of its label (glass)"),
    "border.separator":   (SETTINGS, "text", (300, 728, 40, 16), "Hairline between Set Arc as Default Browser and Change App Icon"),
    "text.navTitle":      (SETTINGS, "text", (338, 225, 140, 45), "Nav title 'Settings'"),
    "text.navButton":     (SETTINGS, "text", (648, 225, 85, 45), "'Done' label"),
    "text.row":           (SETTINGS, "text", (160, 1048, 210, 42), "Row label 'Search Engine'"),
    "text.value":         (SETTINGS, "text", (575, 1048, 115, 42), "Row value 'Google'"),
    "text.chevron":       (SETTINGS, "text", (700, 1050, 30, 36), "Disclosure chevron after 'Google'"),
    "text.button":        (SETTINGS, "text", (165, 345, 175, 45), "'Downloads' label"),
    "switch.onTrack":     (SETTINGS, "fill", (615, 1330, 30, 30), "Auto-Open Keyboard switch, on: track left of the thumb"),
    "switch.thumb":       (SETTINGS, "fill", (680, 1335, 30, 20), "Switch thumb (on)"),
    "tile.blue":          (SETTINGS, "fill", (79, 1080, 8, 8), "Icon tile of Search Engine"),
    "tile.green":         (SETTINGS, "fill", (82, 1146, 6, 5), "Icon tile of Languages"),
    "tile.yellow":        (SETTINGS, "fill", (82, 1321, 6, 5), "Icon tile of Auto-Open Keyboard"),
    "tile.purple":        (SETTINGS, "fill", (82, 1426, 6, 6), "Icon tile of Archive Inactive Tabs"),
    "tile.red":           (SETTINGS, "fill", (79, 1634, 8, 8), "Icon tile of Clear Browsing Data"),
    "size.tile":          (SETTINGS, "bbox", ((80, 1080), (60, 1020, 90, 95), 6), "Search Engine icon tile"),
    "text.helper":        (SITE, "text", (76, 320, 560, 75), "Helper text over the Default Site Settings groups"),
    "text.subtitle":      {"dark": (SCROLLED, "text", (155, 1650, 300, 28)), "light": (SCROLLED, "text", (155, 1685, 300, 28)),
                           "note": "Second line of Export Data ('Share your open tab URLs')"},
    "accent.check":       (ENGINE, "text", (690, 515, 40, 40), "Tick on the chosen search engine (Google)"),
    "accent.link":        (ENGINE, "text", (150, 1145, 280, 40), "'Add Search Engine' link"),
    "size.group":         (SETTINGS, "bbox", ((420, 1045), (30, 1000, 752, 230), 3), "Search Engine and Languages group (two rows)"),
    "size.button":        (SETTINGS, "bbox", ((60, 365), (30, 300, 375, 130), 3), "Downloads button"),
    "size.buttonRight":   (SETTINGS, "bbox", ((440, 366), (405, 300, 387, 130), 3), "Archive button, right of Downloads"),
    "size.switch":        (SETTINGS, "bbox", ((620, 1345), (590, 1300, 170, 100), 12), "Switch track (thumb included where it is white over the track)"),
    "size.switchThumb":   ("dark/" + SETTINGS, "bbox", ((690, 1345), (640, 1310, 120, 80), 12), "Switch thumb (the light thumb's shadow joins the white sheet)"),
    "edges.groups":       ("dark/" + SETTINGS, "find", ("col", 145, 400, 1700, None, 0), "Every edge down x = 145, between the icon tiles and the labels (group tops and bottoms, separators)"),
    "rows.settings":      (SETTINGS, "lines", (75, 1300, 130, 1700), "Icon tiles down the last group (the pitch is the row height)"),
    "radius.tile":        (SETTINGS, "corner", (76, 1038, (70, 1032), 12), "Search Engine icon tile, top-left corner against the group"),
    "radius.group":       (SETTINGS, "diag", (400, 1035, 100, 1120), "Search Engine group, top-left corner"),
    "radius.sheet":       ("light/" + SETTINGS, "diag", (400, 185, 40, 300), "Settings sheet, top-left corner against the dimmed page (the dark sheet is too close to the dimmed page to bound)"),
    "radius.button":      (SETTINGS, "diag", (250, 335, 70, 366), "Downloads button, top-left corner"),
    # ---------------------------------------------------------------- app icon sheet, pop-up and context menus
    "surface.iconSheet":  (ICON, "fill", (300, 1320, 200, 20), "App Icon sheet over Settings"),
    "surface.close":      (ICON, "fill", (676, 1250, 6, 8), "Round close button in the App Icon sheet, left of its x"),
    "text.close":         (ICON, "text", (690, 1240, 30, 32), "The x in the close button"),
    "size.close":         ("dark/" + ICON, "bbox", ((678, 1254), (650, 1200, 110, 110), 8), "Round close button (the light one is white glass on a white sheet)"),
    "surface.popup":      {"dark": (POPUP, "mean", (420, 940, 80, 20)), "light": (POPUP, "mean", (420, 970, 80, 20)),
                           "note": "Pop-up menu of Archive Inactive Tabs (glass), right of '12 hours'"},
    "text.popupItem":     {"dark": (POPUP, "text", (238, 925, 135, 45)), "light": (POPUP, "text", (238, 955, 135, 45)),
                           "note": "Pop-up menu item '12 hours'"},
    "text.destructive":   (LONG, "text", (170, 1305, 260, 45), "'Remove Favorite' in the long-press menu"),
    "text.destructiveEdit": (EDIT, "text", (150, 262, 135, 40), "'Clear All' in the Archive Edit menu"),
    # ---------------------------------------------------------------- launcher and search
    "surface.launcher":   (LAUNCH, "mean", (400, 1310, 200, 14), "Launcher sheet under the search field (glass over the page)"),
    "surface.search":     (LAUNCH, "mean", (250, 1212, 300, 12), "Search field in the launcher (glass)"),
    "text.placeholder":   (LAUNCH, "text", (100, 1222, 90, 45), "'Search...' placeholder, right of the caret"),
    "text.launcherRow":   (LAUNCH, "text", (112, 1350, 140, 50), "Launcher row 'RedeemSG'"),
    "text.pin":           (LAUNCH, "text", (690, 1352, 30, 40), "Pin glyph at the end of a pinned row"),
    "text.searchIcon":    (TYPED, "text", (60, 1340, 40, 40), "Magnifier before a suggestion"),
    "text.suggestion":    (TYPED, "text", (110, 1338, 115, 42), "Suggestion 'design' (the typed text)"),
    "text.completion":    (TYPED, "text", (225, 1440, 210, 42), "The completed part of a suggestion ('ation meaning')"),
    "text.typedPrefix":   (TYPED, "text", (110, 1440, 105, 42), "The typed part of a later suggestion ('desig' of 'designation meaning')"),
    "focus.caret":        {"dark": (TYPED, "fill", (216, 1225, 2, 30)), "light": (LAUNCH, "fill", (97, 1225, 2, 30)),
                           "note": "Text caret in the search field (two pixel columns; dark: typed field, light: empty field)"},
    "surface.pill":       (TYPED, "fill", (565, 1355, 6, 8), "Browse for Me button, left of its label"),
    "text.pill":          (TYPED, "text", (575, 1342, 170, 36), "'Browse for Me' label"),
    "size.search":        ("dark/" + LAUNCH, "bbox", ((250, 1215), (20, 1170, 772, 140), 6), "Search field (the light one is too close to its sheet to bound)"),
    "size.pill":          (TYPED, "bbox", ((566, 1358), (540, 1310, 240, 100), 6), "Browse for Me button"),
    "rows.launcher":      (LAUNCH, "lines", (112, 1340, 134, 1740), "First letters of the launcher rows (the pitch is the row height)"),
    "radius.search":      ("dark/" + LAUNCH, "diag", (250, 1200, 80, 1240), "Search field, top-left corner"),
    "radius.pill":        ("dark/" + TYPED, "diag", (660, 1333, 566, 1358), "Browse for Me button, top-left corner"),
    # ---------------------------------------------------------------- bottom toolbar, page menu, find bar
    "surface.toolbar":    (PAGE, "mean", (500, 1730, 100, 10), "Bottom toolbar below the + button (glass over the page)"),
    "surface.plus":       (PAGE, "mean", (345, 1660, 20, 10), "+ (new tab) button, left of its glyph"),
    "text.plus":          (PAGE, "text", (380, 1650, 50, 50), "The + glyph"),
    "size.plus":          ("dark/" + PAGE, "bbox", ((345, 1665), (300, 1610, 220, 120), 6), "+ button"),
    "surface.menu":       (MENU, "mean", (400, 1570, 100, 10), "Page menu sheet between its last two panels (glass)"),
    "surface.address":    (MENU, "mean", (230, 600, 50, 20), "Address bar in the page menu"),
    "text.address":       (MENU, "text", (300, 600, 200, 45), "'m.youtube.com'"),
    "surface.tileButton": (MENU, "mean", (60, 720, 20, 20), "Find on Page square button (glass)"),
    "text.tileLabel":     (MENU, "text", (40, 875, 170, 30), "'Find on Page' label under its button"),
    "surface.menuGroup":  (MENU, "mean", (400, 1100, 100, 10), "List panel (Translate row)"),
    "text.menuRow":       (MENU, "text", (150, 1065, 140, 40), "Menu row 'Translate'"),
    "surface.notice":     (MENU, "mean", (600, 1610, 100, 20), "Notice card at the bottom of the page menu"),
    "text.notice":        (MENU, "text", (85, 1605, 450, 35), "'Arc scrubbed 5 ads and trackers'"),
    "text.noticeSub":     (MENU, "text", (85, 1645, 450, 35), "'Problems? Tap to restore original page'"),
    "size.address":       (MENU, "span", ("col", 230, 565, 690, 10), "Address bar height: its rims down x = 230"),
    "size.tileButton":    ("dark/" + MENU, "bbox", ((60, 730), (30, 690, 190, 190), 8), "Find on Page square button"),
    "rows.menu":          ("dark/" + MENU, "lines", (150, 960, 175, 1205), "First letters of the first three list rows (the pitch is the row height)"),
    "radius.address":     ("dark/" + MENU, "diag", (400, 595, 80, 628), "Address bar, top-left corner"),
    "radius.tileButton":  (MENU, "corner", (48, 705, (42, 700), 6), "Find on Page button, top-left corner against the menu"),
    "radius.menuGroup":   (MENU, "corner", (46, 936, (40, 930), 6), "List panel, top-left corner against the menu"),
    "surface.findField":  (FINDM, "mean", (180, 1650, 20, 10), "Find field (glass)"),
    "text.findCount":     (FINDM, "text", (425, 1665, 85, 40), "Match count '1 of 2'"),
    "text.findQuery":     (FINDM, "text", (285, 1660, 80, 45), "Query 'food' (dark) or 'asmr' (light)"),
    "size.findField":     (FINDM, "span", ("col", 250, 1615, 1760, 10), "Find field height: its rims down x = 250"),
    "size.findClose":     (FINDM, "span", ("row", 1688, 30, 160, 10), "Close button of the find bar: its rims across the middle"),
    # ---------------------------------------------------------------- spaces
    "gradient.top":       (SPACE, "mean", (400, 350, 100, 20), "Space sheet (Main), near the top"),
    "gradient.bottom":    (SPACE, "mean", (400, 1500, 100, 20), "Space sheet (Main), near the bottom"),
    "text.spaceTitle":    (SPACE, "text", (60, 230, 100, 50), "Space name 'Main'"),
    # ---------------------------------------------------------------- archive
    "bg.page":            (ARCHIVE, "fill", (300, 330, 200, 30), "Archive page, between the header and 'Today'"),
    "surface.card":       (ARCHIVE, "fill", (500, 445, 100, 10), "Archive list card, above its first row"),
    "surface.edit":       (ARCHIVE, "fill", (58, 262, 10, 10), "Edit button, left of its label"),
    "accent.default":     (ARCHIVE, "fill", (682, 262, 8, 8), "Round confirm button at the top right of the Archive"),
    "text.onAccent":      (ARCHIVE, "text", (700, 245, 45, 45, "light"), "Tick on the confirm button"),
    "text.title":         (ARCHIVE, "text", (345, 245, 125, 45), "Page title 'Archive'"),
    "text.section":       (ARCHIVE, "text", (90, 390, 100, 40), "Section header 'Today' (light: 'Yesterday')"),
    "text.rowTitle":      (ARCHIVE, "text", (140, 455, 300, 35), "History row title"),
    "text.rowUrl":        (ARCHIVE, "text", (140, 495, 300, 25), "History row URL"),
    "surface.searchBar":  (ARCHIVE, "mean", (300, 1640, 150, 10), "Search field at the bottom of the Archive (glass over the list)"),
    "size.edit":          ("dark/" + ARCHIVE, "bbox", ((60, 266), (30, 200, 180, 130), 6), "Edit button"),
    "size.confirm":       (ARCHIVE, "bbox", ((684, 266), (650, 200, 130, 130), 12), "Confirm button"),
    "size.searchBar":     ("dark/" + ASEARCH, "bbox", ((300, 1660), (40, 1600, 600, 130), 6), "Archive search field, typed"),
    "rows.archive":       (ARCHIVE, "lines", (50, 450, 90, 820), "Favicons down the first card (the pitch is the row height)"),
    "radius.card":        (ARCHIVE, "diag", (500, 440, 70, 640), "Archive card, top-left corner"),
    "bg.searchPage":      (ABLANK, "fill", (300, 600, 200, 400), "Archive search with no results: a blank page"),
    # ---------------------------------------------------------------- type (cap heights, dark),
    "type.navTitle":      ("dark/" + SETTINGS, "cap", (338, 225, 362, 270), "'S' of the nav title 'Settings'"),
    "type.title":         ("dark/" + ARCHIVE, "cap", (345, 245, 372, 290), "'A' of the page title 'Archive'"),
    "type.row":           ("dark/" + SETTINGS, "cap", (160, 1048, 180, 1090), "'S' of 'Search Engine'"),
    "type.navButton":     ("dark/" + SETTINGS, "cap", (648, 225, 672, 270), "'D' of 'Done'"),
    "type.button":        ("dark/" + SETTINGS, "cap", (165, 345, 192, 390), "'D' of 'Downloads'"),
    "type.launcherRow":   ("dark/" + LAUNCH, "cap", (112, 1345, 134, 1400), "'R' of 'RedeemSG'"),
    "type.search":        ("dark/" + LAUNCH, "cap", (98, 1218, 122, 1268), "'S' of 'Search...'"),
    "type.pill":          ("dark/" + TYPED, "cap", (575, 1342, 590, 1378), "'B' of 'Browse for Me'"),
    "type.tileLabel":     ("dark/" + MENU, "cap", (55, 875, 70, 905), "'F' of 'Find on Page'"),
    "type.menuRow":       ("dark/" + MENU, "cap", (150, 1065, 172, 1105), "'T' of 'Translate'"),
    "type.notice":        ("dark/" + MENU, "cap", (85, 1605, 108, 1640), "'A' of 'Arc scrubbed'"),
    "type.noticeSub":     ("dark/" + MENU, "cap", (85, 1645, 103, 1680), "'P' of 'Problems?'"),
    "type.section":       ("dark/" + ARCHIVE, "cap", (90, 390, 110, 430), "'T' of 'Today'"),
    "type.rowTitle":      ("dark/" + ARCHIVE, "cap", (140, 455, 162, 492), "'A' of 'Asking'"),
    "type.subtitle":      ("dark/" + SCROLLED, "cap", (155, 1646, 168, 1676), "'S' of 'Share your open tab URLs'"),
    "type.helper":        ("dark/" + SITE, "cap", (76, 320, 96, 360), "'S' of 'Settings will apply'"),
    "type.sheetTitle":    ("dark/" + ICON, "cap", (335, 1235, 360, 1280), "'A' of 'App Icon'"),
    "type.spaceTitle":    ("dark/" + SPACE, "cap", (60, 230, 92, 280), "'M' of the space name 'Main'"),
    "type.destructive":   ("dark/" + LONG, "cap", (170, 1305, 192, 1350), "'R' of 'Remove Favorite'"),
    "lines.helper":       ("dark/" + SITE, "lines", (76, 320, 640, 400), "Two-line helper text"),
}

def d(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def hexof(p):
    return "#{:02X}{:02X}{:02X}".format(*p[:3])


def op_fill(rows, x, y, w, h):
    colour, share = sample.fill(rows, x, y, w, h)
    return {"value": hexof(colour), "share": round(share, 2),
            "evidence": "Sampled" if share >= 0.9 else "Derived"}


def op_text(rows, x, y, w, h, ink=None, dark=False):
    """ink: "inverse" reads the theme's opposite ink (a label on a filled button); "light"/"dark" fix it."""
    if ink == "inverse":
        dark = not dark
    elif ink in ("light", "dark"):
        dark = ink == "light"
    return {"value": hexof(sample.text(rows, x, y, w, h, dark=dark)), "evidence": "Sampled (text)"}


def op_extent(rows, axis, line, a, b, bgpt, thr):
    bg = rows[bgpt[1]][bgpt[0]]
    pix = (lambda i: rows[line][i]) if axis == "row" else (lambda i: rows[i][line])
    hits = [i for i in range(a, b) if d(pix(i), bg) > thr]
    start, end = hits[0], hits[-1]
    return {"value": f"{(end - start + 1) / SCALE:g}pt", "from": start, "to": end, "evidence": "Sampled"}


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
    return {"value": f"{bw:g}x{bh:g}pt", "box": [min(xs), min(ys), max(xs), max(ys)],
            "colour": hexof(ref), "evidence": "Sampled"}


def op_find(rows, axis, line, a, b, ref, tol):
    pix = (lambda i: rows[line][i]) if axis == "row" else (lambda i: rows[i][line])
    if ref is None:   # every colour change along the line
        out, prev = [], pix(a)
        for i in range(a + 1, b):
            if d(pix(i), prev) > 4:
                out.append(i)
            prev = pix(i)
        return {"value": out, "evidence": "Sampled"}
    return {"value": [i for i in range(a, b) if d(pix(i), ref) <= tol], "evidence": "Sampled"}


def op_diag(rows, cx, cyc, cxr, cy):
    f = rows[cy][cxr]
    x = cxr
    while d(rows[cy][x - 1], f) <= 3:
        x -= 1
    bg = rows[cy][x - 5]
    tol = max(2, d(bg, f) // 2)
    while d(rows[cy][x - 1], f) <= tol:
        x -= 1
    x0, y = x, cyc
    while d(rows[y - 1][cx], f) <= tol:
        y -= 1
    t = 0
    while d(rows[y + t][x0 + t], f) > tol:
        t += 1
    r = t / (1 - 2 ** -0.5) / SCALE
    return {"value": f"{r:.1f}pt", "inset": t, "corner": [x0, y], "evidence": "Derived"}


def op_corner(rows, x0, y0, bgpt, thr):
    """A corner with no flat fill inside (a thumbnail): x0, y0 is where its straight edges meet; the
    inset is how far along the diagonal the first pixel that differs from the background sits, less
    half a pixel so it measures to the edge rather than to that pixel's far side."""
    bg = rows[bgpt[1]][bgpt[0]]
    t = 0
    while d(rows[y0 + t][x0 + t], bg) <= thr:
        t += 1
    r = max(t - 0.5, 0) / (1 - 2 ** -0.5) / SCALE
    return {"value": f"{r:.1f}pt", "inset": t, "corner": [x0, y0], "evidence": "Derived"}


def op_span(rows, axis, line, a, b, thr):
    """First and last place along a line where a pixel differs from the one before it by more than thr:
    the rims of a glass control, whose fill drifts too much for a background point."""
    pix = (lambda i: rows[line][i]) if axis == "row" else (lambda i: rows[i][line])
    hits = [i for i in range(a + 1, b) if d(pix(i), pix(i - 1)) > thr]
    return {"value": f"{(hits[-1] - hits[0]) / SCALE:g}pt", "from": hits[0], "to": hits[-1], "evidence": "Derived"}


def op_mean(rows, x, y, w, h):
    """The mean colour of a box: a reading of a gradient or of glass over content, never a flat fill."""
    px = [rows[j][i] for j in range(y, y + h) for i in range(x, x + w)]
    return {"value": hexof([round(sum(p[k] for p in px) / len(px)) for k in range(3)]), "evidence": "Derived"}


def op_cap(rows, x0, y0, x1, y1):
    bg = rows[y0][x0]
    ys = [y for y in range(y0, y1) if any(d(rows[y][x], bg) > 30 for x in range(x0, x1))]
    ink = ys[-1] - ys[0] + 1
    cap = (ink - 1) / SCALE          # one pixel of the ink height is anti-aliasing
    return {"value": f"{round(cap / CAP_EM)}pt", "capHeight": f"{cap:g}pt", "inkPx": ink, "top": ys[0],
            "evidence": "Derived"}


def op_lines(rows, x0, y0, x1, y1):
    bg = rows[y0][x0]
    ink = [y for y in range(y0, y1) if any(d(rows[y][x], bg) > 30 for x in range(x0, x1))]
    bands, start = [], ink[0]
    for a, b in zip(ink, ink[1:] + [None]):
        if b is None or b != a + 1:
            bands.append([start, a])
            start = b
    tops = [b[0] for b in bands if b[1] - b[0] >= 8]
    pitch = [(b - a) / SCALE for a, b in zip(tops, tops[1:])]
    return {"value": f"{(sum(pitch) / len(pitch)):.1f}pt" if pitch else "one line", "bands": bands,
            "evidence": "Derived"}


def run(raw):
    raw = pathlib.Path(raw).expanduser()
    if not (raw / "dark").is_dir():
        raise SystemExit(f"{raw}: no dark/ captures; nothing written")
    cache, out = {}, {}
    for rid, entry in R.items():
        if isinstance(entry, dict):   # a box per theme
            jobs = [(t, *entry[t], entry["note"]) for t in ("dark", "light") if t in entry]
        else:
            cap, op, args, note = entry
            themes = [cap.split("/")[0]] if "/" in cap else ["dark", "light"]
            jobs = [(t, cap.split("/")[-1], op, args, note) for t in themes]
        for theme, name, op, args, note in jobs:
            png = raw / theme / f"{name}.png"
            if not png.exists():
                continue
            key = f"{theme}/{name}"
            if key not in cache:
                cache[key] = sample.read_png(png)[2]
            rows = cache[key]
            if op == "fill":
                res = op_fill(rows, *args)
            elif op == "text":
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
             "Generated by `tools/measure.py` from the full-colour captures (812 x 1780 px, 2 px per pt, the screen at "
             "16, 76 inside each PNG). Boxes are `x, y, w, h` in capture pixels; the committed screenshots are the "
             "same captures quantised to 256 colours, so a box can be checked against them, but values were read "
             "from the full-colour copies. `tools/build_tokens.py` maps these readings to `tokens.json`.", "",
             "| Reading | Theme | Value | Evidence | Method | Capture | Note |", "|---|---|---|---|---|---|---|"]
    for rid in sorted(readings):
        for theme, r in sorted(readings[rid].items()):
            v = r["value"]
            if isinstance(v, list):
                v = ", ".join(map(str, v)) if len(v) <= 12 else f"{len(v)} positions, {v[0]} to {v[-1]}"
            extra = f" ({round(r['share'] * 100)}% of box)" if "share" in r else ""
            lines.append(f"| `{rid}` | {theme} | {v}{extra} | {r['evidence']} | {r['op']} {r['args']} | "
                         f"[{r['capture'].split('/')[-1]}](../{r['capture']}) | {r['note']} |")
    (PKG / "raw" / f"{SLUG}-measured.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    readings = run(sys.argv[1] if len(sys.argv) > 1 else f"~/.design-systems/{SLUG}/raw-shots")
    missing = sorted(rid for rid in R if rid not in readings)
    if missing:   # a light-only gap is fine; a reading with no theme at all means a capture is absent
        raise SystemExit(f"no capture for {len(missing)} readings ({', '.join(missing[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
