#!/usr/bin/env python3
"""Read a native app's values out of the full-colour iPhone Mirroring captures (native kit).

    python3 tools/measure.py ~/.design-systems/<slug>/raw-shots

Copied from systems/grokbot. Adapt the blocks marked PRODUCT (adapt): NAME and the reading table R,
whose boxes are capture pixels on this product's screens. The ops below are generic.

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
  diag    corner radius from the inset along the corner's diagonal        Derived (about +-2 pt)
  rimdiag the same for an outlined shape (fill = page): the inset to the rim Derived (about +-2 pt)
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

NAME = "Notion"    # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
H, CH, SR, AI, SH, SO, MP, CS, TH, PG = ("01-home-sidebar-tree", "02-chats-tab-list", "08-search-no-results-empty",
                                          "11-ai-chat-empty-composer", "09-search-filters-sheet-switch-off",
                                          "10-sort-radio-list", "13-model-picker-menu", "15-chats-sheet-primary-button",
                                          "16-ai-chat-thread-bubbles", "17-page-headings-table")
AC, DB, ST, ST2, TS = ("19-page-actions-sheet", "20-database-cover-inline-view", "25-settings-notifications-switches-off",
                       "26-settings-select-and-secondary-button", "29-theme-choice-sheet")
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.sidebar":         (H, "fill", (300, 1300, 200, 20), "Home (the sidebar tree), Chats, Meetings and Inbox tabs, Settings"),
    "bg.page":            (PG, "fill", (400, 1030, 200, 20), "A page: the document canvas"),
    "bg.chat":            (AI, "fill", (400, 800, 100, 100), "Notion AI chat canvas"),
    "bg.search":          (SR, "fill", (400, 600, 100, 100), "Search results canvas"),
    "bg.sheet":           (SH, "fill", (400, 1500, 200, 50), "Small sheet (search Filters)"),
    "bg.sheetLarge":      (AC, "fill", (400, 310, 100, 20), "Large sheet (page Actions), behind its grouped cards"),
    "bg.sheetTheme":      (TS, "fill", (400, 1000, 100, 100), "Large sheet (Theme choice)"),
    "bg.behindPushed":    (AI, "fill", (400, 100, 100, 10), "The screen behind a pushed card (AI chat), above its top edge"),
    "surface.card":       (AC, "fill", (500, 600, 200, 20), "Grouped card in a large sheet (Actions)"),
    "surface.cardTheme":  (TS, "fill", (400, 450, 100, 10), "Grouped card in the Theme sheet"),
    "surface.cardInSheet": ("dark/" + SO, "fill", (400, 1080, 200, 6), "Grouped card inside the small sheet (Sort)"),
    "surface.tableHeader": (PG, "fill", (200, 1440, 100, 8), "Table header row in a page"),
    "surface.bubble":     (TH, "fill", (222, 720, 15, 90), "The owner's message bubble in an AI chat, left padding"),
    "surface.code":       (TH, "fill", (300, 1078, 4, 30), "Inline code behind red text ('Distance from Home (km)')"),
    "surface.tabSelected": (H, "fill", (360, 180, 20, 10), "Selected top tab (Home pill)"),
    "surface.tab":        (H, "fill", (460, 180, 30, 8), "Unselected top tab (a circle)"),
    "surface.glass":      (SR, "fill", (300, 1620, 100, 10), "Glass search bar at the bottom of search"),
    "surface.glassBar":   (H, "fill", (450, 1630, 100, 10), "Glass 'Ask AI' pill in the bottom bar"),
    "surface.composer":   (AI, "fill", (400, 1520, 100, 10), "Expanded AI composer"),
    "surface.menu":       (MP, "fill", (650, 1250, 20, 40), "Pop-up menu (AI model picker)"),
    "surface.viewChip":   (DB, "fill", (130, 830, 20, 8), "Database view chip ('Areas')"),
    "surface.icon":       (H, "fill", (60, 1072, 6, 6), "Teamspace icon tile"),
    "surface.grabber":    (SH, "fill", (360, 876, 80, 4), "Sheet grabber"),
    "scrim.ref":          (SR, "fill", (600, 350, 20, 20), "Search canvas, undimmed"),
    "scrim.sheet":        (SH, "fill", (600, 350, 20, 20), "Search canvas under the Filters sheet"),
    # ---------------------------------------------------------------- database group colours
    "group.blue":         (DB, "fill", (500, 935, 150, 10), "Group background, blue ('Mind (Self)')"),
    "group.green":        (DB, "fill", (500, 1175, 150, 10), "Group background, green ('Building (Action)')"),
    "group.pink":         (DB, "fill", (500, 1415, 150, 10), "Group background, pink ('Relationships (1-to-1)')"),
    "group.orange":       (DB, "fill", (500, 1570, 150, 10), "Group background, orange ('Travel')"),
    # ---------------------------------------------------------------- borders
    "border.divider":     (AC, "text", (300, 630, 200, 12), "Divider between grouped rows (darkest or lightest pixel of the hairline)"),
    "border.settings":    (ST, "text", (300, 530, 200, 12), "Divider between settings rows"),
    "border.control":     (ST, "text", (690, 1560, 30, 10), "Rim of the 'Off' select"),
    "border.card":        (TH, "text", (400, 1218, 200, 12), "Rim of an AI result card"),
    "border.table":       (PG, "text", (200, 1420, 100, 10), "Table rim, top edge"),
    "border.frame":       (DB, "text", (400, 712, 100, 12), "Rim of an inline database"),
    # ---------------------------------------------------------------- text
    "text.primary":       (H, "text", (125, 495, 240, 40), "Sidebar row title ('Setup call Logs')"),
    "text.pageBody":      (PG, "text", (68, 728, 570, 35), "Page body text"),
    "text.settingsRow":   (ST, "text", (53, 373, 350, 35), "Settings row title"),
    "text.prose":         (TH, "text", (49, 978, 650, 35), "AI chat answer text"),
    "text.bubble":        (TH, "text", (247, 722, 470, 35), "Text in the owner's bubble"),
    "text.inbox":         ("04-inbox-tab", "text", (125, 445, 475, 35), "Inbox notification body"),
    "text.sheetTitle":    (SH, "text", (360, 922, 95, 32), "Small sheet title ('Filters')"),
    "text.secondary":     (H, "text", (57, 305, 110, 35), "Sidebar section header ('Recents')"),
    "text.subtitle":      (ST, "text", (53, 420, 425, 32), "Settings row subtitle"),
    "text.searchSub":     ("dark/06-search-focused-recents", "text", (120, 458, 265, 35), "Search result location line"),
    "text.emptyBody":     (SR, "text", (213, 972, 385, 65), "Empty-state lines"),
    "text.askPlaceholder": (H, "text", (290, 1645, 95, 35), "'Ask AI' in the bottom bar"),
    "text.tertiary":      ("04-inbox-tab", "text", (655, 385, 78, 35), "Inbox date ('5 Sep')"),
    "text.sortValue":     ("22-filter-sheet-properties", "text", (582, 375, 97, 32), "Row value ('bucket')"),
    "text.placeholder":   (AI, "text", (80, 1540, 90, 35), "Composer placeholder ('Ask AI')"),
    "text.searchPlaceholder": ("dark/06-search-focused-recents", "text", (155, 1632, 215, 35), "Search bar placeholder"),
    "text.propertySearch": ("22-filter-sheet-properties", "text", (145, 498, 330, 32), "'Search for a property...' placeholder"),
    "text.menu":          (MP, "text", (355, 1180, 175, 35), "Menu item ('GPT-6.1 Sol')"),
    "text.menuDesc":      (MP, "text", (355, 1068, 270, 30), "Menu item description"),
    "text.code":          (TH, "text", (155, 1080, 400, 30), "Inline code text (red)"),
    "text.danger":        (AC, "text", (141, 1115, 178, 40), "'Move to Bin'"),
    "text.accent":        ("22-filter-sheet-properties", "text", (145, 375, 62, 32), "Accent text ('Sort', an active sort)"),
    "text.accentSel":     (AC, "text", (140, 385, 55, 45), "Selected segment glyph ('Ag', Default)"),
    "text.onAccent":      (CS, "text", (160, 1643, 75, 35, "light"), "Label on the blue '+ Chat' button"),
    "text.icon":          (AC, "text", (80, 665, 32, 35), "Row icon (Share)"),
    "text.iconMuted":     (H, "text", (440, 195, 45, 40), "Unselected tab icon"),
    "text.typed":         ("dark/12-ai-composer-typed-send-enabled", "text", (73, 1540, 70, 35), "Text typed in the composer"),
    # ---------------------------------------------------------------- accent and controls
    "accent.fill":        (DB, "fill", (588, 845, 12, 40), "'+' new-row button on a database"),
    "accent.button":      (CS, "fill", (250, 1650, 8, 8), "'+ Chat' button (glass over blue)"),
    "accent.radio":       ("dark/" + SO, "fill", (692, 1046, 3, 3), "Selected radio (Best matches)"),
    "accent.caret":       ("dark/12-ai-composer-typed-send-enabled", "fill", (145, 1540, 2, 30), "Text caret"),
    "accent.caretLight":  ("light/" + AI, "fill", (71, 1540, 2, 30), "Text caret in the focused composer"),
    "accent.dot":         (H, "fill", (108, 190, 7, 5), "Red dot on the avatar button (unread)"),
    "switch.off":         (SH, "fill", (730, 1145, 15, 10), "Switch off track (search Filters, Title only)"),
    "switch.offSettings": (ST, "fill", (735, 425, 15, 10), "Switch off track (Settings)"),
    "switch.thumb":       (SH, "fill", (660, 1145, 10, 10), "Switch thumb"),
    "radio.off":          ("dark/" + SO, "text", (685, 1125, 40, 40), "Unselected radio ring"),
    # ---------------------------------------------------------------- sizes
    "size.avatarButton.w": (H, "extent", ("row", 215, 30, 150, (35, 215), 12), "Avatar button in the top bar, width"),
    "size.tabSelected.w": (H, "extent", ("row", 215, 145, 400, (147, 215), 8), "Selected tab pill, width"),
    "size.tabSelected.h": (H, "extent", ("col", 300, 150, 280, (300, 155), 8), "Selected tab pill, height"),
    "size.tab.w":         (H, "extent", ("row", 215, 400, 525, (402, 215), 6), "Unselected tab, width"),
    "size.tab.h":         (H, "extent", ("col", 461, 150, 280, (461, 155), 6), "Unselected tab, height"),
    "size.barButton.w":   (H, "extent", ("row", 1660, 40, 185, (42, 1660), 12), "Round glass search button in the bottom bar, width"),
    "size.barPill.h":     (H, "extent", ("col", 450, 1580, 1745, (450, 1585), 10), "'Ask AI' glass pill, height"),
    "size.barPill.w":     (H, "extent", ("row", 1660, 180, 630, (182, 1660), 10), "'Ask AI' glass pill, width"),
    "size.navButton.w":   (AI, "extent", ("row", 245, 30, 160, (35, 245), 10), "Round glass button on the AI chat (history), width"),
    "size.composer.h":    (AI, "extent", ("col", 400, 1470, 1720, (400, 1480), 10), "Expanded composer, height"),
    "size.composerCompact.h": ("14-ai-composer-unfocused", "extent", ("col", 400, 1590, 1735, (400, 1595), 10), "Unfocused composer, height"),
    "size.send":          ("dark/12-ai-composer-typed-send-enabled", "bbox", ((728, 1600), (680, 1575, 100, 105), 24), "Blue send button"),
    "size.chatButton":    (CS, "bbox", ((250, 1650), (50, 1590, 250, 130), 14), "'+ Chat' button"),
    "size.switch.w":      (SH, "extent", ("row", 1148, 600, 775, (610, 1148), 10), "Switch, width"),
    "size.switch.h":      (SH, "extent", ("col", 735, 1095, 1200, (735, 1100), 10), "Switch, height"),
    "size.switchThumb":   ("dark/" + SH, "bbox", ((668, 1148), (620, 1100, 110, 100), 8), "Switch thumb"),
    "size.radio":         ("dark/" + SO, "extent", ("row", 1047, 670, 740, (672, 1047), 30), "Radio, outer diameter"),
    "size.dbAdd":         (DB, "bbox", ((640, 850), (570, 820, 150, 100), 30), "Database '+' split button"),
    "size.viewChip.w":    (DB, "extent", ("row", 865, 100, 340, (102, 865), 6), "Database view chip, width"),
    "size.viewChip.h":    (DB, "extent", ("col", 300, 815, 905, (300, 817), 6), "Database view chip, height"),
    "size.control.h":     ("dark/" + ST2, "extent", ("col", 622, 1405, 1495, (622, 1410), 6), "'Connect' button, height"),
    "size.select.h":      (ST, "extent", ("col", 660, 1550, 1630, (660, 1552), 6), "'Off' select, height"),
    "size.selectWide.h":  ("dark/28-settings-preferences-theme-select", "extent", ("col", 430, 1410, 1510, (430, 1412), 6), "Theme select, height"),
    "size.cardSeg":       (AC, "bbox", ((300, 360), (30, 330, 760, 200), 2), "Segmented font card (Actions)"),
    "space.sidebarText":  (H, "extent", ("row", 320, 17, 120, (20, 320), 30), "First ink of a sidebar section header from the screen edge"),
    "space.pageText":     (PG, "extent", ("row", 745, 17, 120, (20, 745), 30), "First ink of page body text from the screen edge"),
    "space.settingsText": (ST, "extent", ("row", 385, 17, 120, (20, 385), 30), "First ink of a settings row title from the screen edge"),
    "lines.sheetRows":    (AC, "lines", (141, 560, 441, 1160), "Rows of a grouped card in the Actions sheet"),
    "lines.sidebarRows":  (H, "lines", (125, 490, 575, 720), "Sidebar rows under Favourites"),
    "lines.chatRows":     (CH, "lines", (57, 640, 677, 1140), "Rows in the Chats list"),
    "lines.searchRows":   ("dark/06-search-focused-recents", "lines", (52, 410, 97, 1310), "Icons down the search results"),
    "lines.dbRows":       (DB, "lines", (176, 925, 206, 1150), "Rows in a database group"),
    "lines.pageBody":     (PG, "lines", (69, 725, 709, 995), "Page body, a six-line block"),
    "lines.prose":        (TH, "lines", (49, 975, 709, 1205), "AI answer, a five-line block"),
    "lines.subtitle":     (ST, "lines", (53, 420, 503, 490), "Two-line settings subtitle"),
    # ---------------------------------------------------------------- radii
    "radius.card":        (AC, "diag", (600, 560, 65, 700), "Grouped card (Actions)"),
    "radius.cardSeg":     (AC, "diag", (600, 355, 60, 430), "Segmented font card"),
    "radius.cardInSheet": ("dark/" + SO, "diag", (400, 1010, 70, 1095), "Grouped card in the small sheet (Sort)"),
    "radius.sheet":       (SH, "diag", (200, 880, 45, 1000), "Small sheet, top corner"),
    "radius.menu":        ("dark/" + MP, "diag", (450, 990, 210, 1300), "Pop-up menu (model picker)"),
    "radius.bubble":      (TH, "diag", (500, 705, 225, 760), "The owner's bubble"),
    "radius.composer":    (AI, "diag", (400, 1512, 50, 1600), "Expanded composer"),
    "radius.dbAdd":       (DB, "diag", (640, 840, 595, 865), "Database '+' split button"),
    "radius.viewChip":    (DB, "diag", (300, 836, 118, 865), "Database view chip"),
    "radius.resultCard":  (TH, "rimdiag", (60, 1300, 400, 1240, 6), "AI result card (outlined)"),
    "radius.frame":       (DB, "rimdiag", (80, 1000, 400, 730, 6), "Inline database frame (outlined)"),
    "radius.control":     ("dark/" + ST2, "rimdiag", (618, 1448, 686, 1430, 6), "'Connect' button (outlined)"),
    "radius.select":      (ST, "rimdiag", (656, 1592, 700, 1572, 6), "'Off' select (outlined)"),
    # ---------------------------------------------------------------- type (cap heights)
    "type.pageTitle":     (DB, "cap", (72, 570, 114, 640), "'D' of a page title"),
    "type.h1":            (PG, "cap", (71, 545, 99, 605), "'L' of a heading 1"),
    "type.h2":            (PG, "cap", (70, 1088, 106, 1140), "'M' of a heading 2"),
    "type.settingsTitle": (ST, "cap", (54, 298, 79, 345), "'N' of a settings section title"),
    "type.body":          (PG, "cap", (70, 722, 87, 770), "'E' of page body text"),
    "type.rowTitle":      (H, "cap", (125, 490, 145, 545), "'S' of a sidebar row"),
    "type.chatRow":       (CH, "cap", (58, 635, 75, 690), "'F' of a Chats row"),
    "type.sheetRow":      (SH, "cap", (122, 1025, 140, 1075), "'S' of a sheet row"),
    "type.actionItem":    (AC, "cap", (141, 575, 175, 615), "'A' of an Actions row"),
    "type.navTitle":      (ST, "cap", (344, 175, 363, 215), "'S' of a nav title"),
    "type.sheetTitle":    (AC, "cap", (345, 230, 375, 270), "'A' of a large sheet title"),
    "type.bubble":        (TH, "cap", (249, 718, 269, 765), "'N' of bubble text"),
    "type.prose":         (TH, "cap", (49, 975, 70, 1020), "'A' of AI answer text"),
    "type.menuItem":      ("dark/05-inbox-filter-menu", "cap", (242, 475, 263, 520), "'U' of a menu item"),
    "type.button":        (CS, "cap", (161, 1638, 183, 1685), "'C' of '+ Chat'"),
    "type.tab":           (H, "cap", (258, 190, 278, 240), "'H' of a tab label"),
    "type.composer":      (AI, "cap", (80, 1535, 94, 1585), "'A' of the composer placeholder"),
    "type.modelItem":     (MP, "cap", (355, 1020, 376, 1065), "'A' of 'Auto' in the model picker"),
    "type.sheetTitleSmall": (SH, "cap", (361, 915, 377, 960), "'F' of a small sheet title"),
    "type.sectionHeader": (H, "cap", (58, 300, 75, 345), "'R' of a sidebar section header"),
    "type.settingsRow":   (ST, "cap", (54, 368, 76, 410), "'M' of a settings row title"),
    "type.empty":         (SR, "cap", (298, 915, 316, 960), "'N' of an empty-state title"),
    "type.control":       ("dark/" + ST2, "cap", (631, 1430, 649, 1470), "'C' of 'Connect'"),
    "type.date":          ("04-inbox-tab", "cap", (655, 380, 669, 420), "'5' of an inbox date"),
    "type.done":          ("dark/21-views-sheet", "cap", (688, 250, 708, 290), "'D' of 'Done'"),
    "type.subtitle":      (ST, "cap", (53, 415, 70, 455), "'G' of a settings subtitle"),
    "type.segLabel":      (AC, "cap", (123, 445, 140, 480), "'D' of a segment label"),
    "type.searchSub":     ("dark/06-search-focused-recents", "cap", (150, 455, 166, 495), "'D' of a search result location"),
    "type.menuHeader":    ("dark/05-inbox-filter-menu", "cap", (242, 315, 254, 345), "'F' of a menu header"),
    "type.menuDesc":      (MP, "cap", (356, 1065, 370, 1100), "'B' of a menu item description"),
    "type.tableHeader":   (PG, "cap", (100, 1445, 114, 1480), "'R' of a table header"),
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


def op_rimdiag(rows, xin, ymid, xcol, yin, thr):
    """diag for an outlined shape whose fill is the page: walk out to the rim, not to a fill edge."""
    f = rows[ymid][xin]
    x = xin
    while d(rows[ymid][x - 1], f) <= thr:
        x -= 1
        if x == 0:
            raise ValueError(f"rimdiag: no rim left of ({xin}, {ymid})")
    x0 = x - 1
    y = yin
    while d(rows[y - 1][xcol], f) <= thr:
        y -= 1
        if y == 0:
            raise ValueError(f"rimdiag: no rim above ({xcol}, {yin})")
    y0 = y - 1
    t = 0                                     # page-coloured steps outside the arc; 0 for a square corner
    while d(rows[y0 + t][x0 + t], f) <= thr:
        t += 1
        if y0 + t >= ymid or x0 + t >= xin:
            raise ValueError(f"rimdiag: no corner rim between ({x0}, {y0}) and ({xin}, {ymid})")
    r = t / (1 - 2 ** -0.5) / SCALE
    return {"value": f"{r:.1f}pt", "inset": t, "corner": [x0, y0], "evidence": "Derived"}


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
