#!/usr/bin/env python3
"""Read ChatGPT for iOS's values out of the full-colour iPhone Mirroring captures (native kit).

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

NAME = "ChatGPT for iOS"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
# The captures, by number. Dark and light share names; 17 and 20 are dark only, and 18 is a different
# screen in each theme, so neither is read here.
C = {
    "01": "01-work-mode-segmented-composer-focused", "02": "02-chat-mode-suggestions-composer",
    "03": "03-composer-typed-send", "04": "04-plus-menu-selected-item", "05": "05-sidebar-nav-recents-unread-dot",
    "06": "06-chat-thread-blue-bubble-math", "07": "07-chat-menu-destructive-glass", "08": "08-find-in-chat-no-results",
    "09": "09-settings-grouped-popup-values", "10": "10-accent-color-popup-menu", "11": "11-general-switches-on-popup-rows",
    "12": "12-error-dialog-cancel-retry", "13": "13-personalization-popups-text-field-empty", "14": "14-usage-progress-bar",
    "15": "15-work-mode-suggestions-model-pill", "16": "16-effort-slider-stepped",
    "19": "19-search-no-results-empty-state", "20": "20-search-focused-empty-prompt",
    "21": "21-scheduled-tabs-cards-primary-pill",
    "22": "22-scheduled-paused-empty-tab-selected",
}
D = {k: "dark/" + v for k, v in C.items()}   # dark only
L = {k: "light/" + v for k, v in C.items()}  # light only

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            (C["02"], "fill", (300, 700, 200, 20), "New chat page, above the suggestions"),
    "bg.thread":          (C["06"], "fill", (300, 1500, 200, 20), "Chat thread background, below the action row"),
    "bg.sidebar":         (C["05"], "fill", (300, 1550, 200, 20), "Sidebar background"),
    "bg.grouped":         (C["09"], "fill", (300, 250, 200, 20), "Settings page behind the grouped cards"),
    "surface.card":       (C["09"], "fill", (420, 375, 250, 20), "Grouped card (Personalization row, right of the label)"),
    "surface.composer":   (C["02"], "fill", (400, 1540, 100, 10), "Composer (glass; centre reading above the placeholder)"),
    "surface.segmentTrack": (C["02"], "fill", (470, 240, 40, 6), "Chat / Work control, the unselected half"),
    "surface.segmentThumb": (C["02"], "fill", (300, 240, 40, 6), "Chat / Work control, the selected thumb"),
    "surface.glassButton": (C["09"], "fill", (690, 245, 60, 6), "Round glass close button, below its glyph"),
    "surface.menu":       (C["04"], "fill", (400, 1040, 100, 20), "Plus menu (glass over the page)"),
    "surface.menuIcon":   (C["04"], "fill", (80, 1100, 20, 10), "Round icon well beside a plus-menu item"),
    "surface.menuOverBubble": (C["07"], "fill", (560, 300, 150, 20), "Chat menu over the blue bubble: the glass takes its colour"),
    "surface.userBubble": (C["06"], "fill", (600, 560, 100, 20), "The owner's message bubble"),
    "surface.dialog":     (C["12"], "fill", (400, 955, 200, 10), "Alert card (glass), between body and buttons"),
    "surface.dialogButton": (C["12"], "fill", (140, 995, 40, 15), "Cancel button inside the alert"),
    "scrim.ref":          (C["13"], "fill", (500, 1265, 200, 15), "Custom instructions field, undimmed"),
    "scrim.dim":          (C["12"], "fill", (500, 1265, 200, 15), "The same field under the alert's scrim"),
    "surface.tabSelected": (C["21"], "fill", (85, 320, 20, 8), "Selected tab pill (Active)"),
    "surface.taskCard":   (C["21"], "fill", (715, 640, 30, 60), "Recommended task card, right padding"),
    "border.taskCard":    (D["21"], "fill", (251, 543, 14, 1), "One dash of a recommended task card's rim, one pixel row"),
    "border.taskCardLight": (L["21"], "fill", (251, 542, 14, 1), "One dash of a recommended task card's rim, one pixel row"),
    "surface.searchTile": (C["19"], "fill", (370, 520, 70, 10), "Rounded tile behind the empty-state magnifier"),
    "surface.searchBar":  (D["20"], "fill", (300, 1590, 300, 10), "Search field at the bottom of search (glass)"),
    "surface.progressTrack": (C["14"], "fill", (600, 472, 100, 8), "Usage meter track, unfilled part"),
    "surface.sliderTrack": (C["16"], "fill", (470, 1580, 150, 8), "Effort slider track (glass)"),
    "border.divider":     (C["09"], "fill", (300, 461, 200, 1), "Hairline between grouped rows, one pixel row"),
    "border.sidebar":     (C["05"], "fill", (200, 893, 200, 1), "Rule between sidebar nav and recents"),
    "surface.banner":     (L["06"], "fill", (420, 315, 250, 10), "'Share Message' banner over the thread"),
    "text.bannerTitle":   (L["06"], "text", (76, 335, 195, 35), "Banner title"),
    "text.bannerBody":    (L["06"], "text", (76, 372, 300, 30), "Banner body"),
    # ---------------------------------------------------------------- text
    "text.primary":       (C["09"], "text", (160, 395, 230, 40), "Settings row label ('Personalization')"),
    "text.thread":        (C["06"], "text", (50, 905, 240, 45), "Assistant reply text"),
    "text.onUserBubble":  (C["06"], "text", (250, 445, 470, 40), "Text in the owner's bubble"),
    "text.value":         (C["09"], "text", (515, 1030, 210, 40), "Settings row value ('Premium seat')"),
    "text.sectionHeader": (C["09"], "text", (88, 300, 320, 40), "Settings section header"),
    "text.footnote":      (C["11"], "text", (88, 475, 600, 30), "Helper text under a card"),
    "text.chevron":       (C["09"], "text", (700, 395, 30, 35), "Disclosure chevron"),
    "text.placeholder":   (C["02"], "text", (75, 1550, 200, 40), "Composer placeholder"),
    "text.fieldPlaceholder": (C["13"], "text", (80, 1275, 370, 40), "Custom instructions placeholder"),
    "text.suggestion":    (C["02"], "text", (135, 1235, 500, 40), "Suggestion row above the composer"),
    "text.seeAll":        (C["05"], "text", (80, 1455, 140, 40), "'See all...' under the recents"),
    "text.timestamp":     (D["08"], "text", (330, 300, 150, 30), "Thread date line ('Today 15:42')"),
    "text.emptyTitle":    (C["19"], "text", (330, 575, 155, 35), "Empty-state title ('No results')"),
    "text.emptyBody":     (C["19"], "text", (195, 625, 425, 35), "Empty-state body"),
    "text.emptyLine":     (C["22"], "text", (280, 920, 255, 35), "One-line empty state ('No paused tasks')"),
    "text.tabUnselected": (C["21"], "text", (258, 340, 115, 35), "Unselected tab label ('Paused')"),
    "text.modelName":     (C["15"], "text", (355, 1632, 90, 30), "Model pill, model name"),
    "text.modelEffort":   (C["15"], "text", (455, 1632, 110, 30), "Model pill, effort ('Medium')"),
    "text.findCount":     (C["08"], "text", (405, 200, 155, 35), "Find in chat result count ('No results')"),
    "text.danger":        (C["07"], "text", (390, 895, 110, 40), "'Delete' in the chat menu"),
    "text.menuSelected":  (C["04"], "text", (190, 1600, 230, 45), "Selected plus-menu item ('Think harder'), accent-tinted"),
    "text.menuHeader":    (C["07"], "text", (320, 195, 150, 30), "Chat menu header (chat title)"),
    "text.dialogBody":    (C["12"], "text", (147, 865, 510, 35), "Alert body"),
    "text.dialogTitle":   (C["12"], "text", (147, 808, 80, 40), "Alert title"),
    "text.taskBody":      (C["21"], "text", (168, 625, 520, 35), "Task card description"),
    # ---------------------------------------------------------------- accent and controls
    "accent.send":        (C["03"], "fill", (705, 1660, 15, 10), "Send button"),
    "accent.sendGlyph":   (C["03"], "text", (705, 1610, 40, 60, "light"), "Send arrow"),
    "accent.voice":       (C["02"], "fill", (705, 1665, 15, 8), "Voice button (the composer's blue circle when empty)"),
    "accent.chatPill":    (C["05"], "fill", (130, 1615, 20, 10), "Sidebar 'Chat' (new chat) pill"),
    "accent.chatPillLabel": (C["05"], "text", (190, 1625, 80, 45, "light"), "Sidebar 'Chat' label"),
    "accent.newTask":     (C["21"], "fill", (530, 1615, 12, 20), "'New task' pill"),
    "accent.newTaskLabel": (C["21"], "text", (545, 1615, 150, 50, "light"), "'New task' label"),
    "accent.slider":      (C["16"], "fill", (110, 1595, 20, 10), "Effort slider, filled part"),
    "accent.progress":    (C["14"], "fill", (200, 472, 200, 8), "Usage meter fill"),
    "accent.caret":       (D["19"], "fill", (203, 1608, 2, 35), "Search field caret, two pixel columns"),
    "accent.caretLight":  (L["02"], "fill", (71, 1550, 2, 38), "Composer caret, two pixel columns"),
    "accent.swatchBlue":  (C["10"], "fill", (327, 685, 12, 12), "Accent colour menu, Blue swatch"),
    "accent.unread":      (C["05"], "fill", (556, 1082, 12, 12), "Unread dot after a recent chat"),
    "button.ink":         (C["19"], "fill", (318, 740, 15, 25), "'New chat' pill on the empty state"),
    "button.inkLabel":    (C["19"], "text", (340, 752, 135, 40, "inverse"), "'New chat' label"),
    "button.dialogLabel": (C["12"], "text", (505, 1005, 95, 45), "'Retry' label"),
    "switch.on":          (C["11"], "fill", (615, 700, 20, 15), "Switch on (Auto-correct spelling)"),
    "switch.thumb":       (C["11"], "fill", (670, 700, 30, 15), "Switch thumb"),
    "slider.thumb":       (C["16"], "fill", (345, 1615, 15, 15), "Effort slider thumb"),
    "slider.step":        (C["16"], "fill", (455, 1620, 6, 6), "Effort slider step dot"),
    # ---------------------------------------------------------------- accent palette (Accent color menu)
    **{f"palette.{name}": (C["10"], "fill", (327, y - 6, 12, 12), f"Accent colour menu, {name} swatch")
       for name, y in [("blue", 691), ("cyan", 775), ("green", 859), ("lime", 943), ("yellow", 1027),
                       ("orange", 1111), ("pink", 1195), ("magenta", 1279), ("purple", 1363), ("ink", 1447)]},
    # ---------------------------------------------------------------- sizes
    "size.navButton.w":   (D["09"], "extent", ("row", 215, 650, 790, (655, 215), 12), "Round glass close button, width"),
    "size.segmented.w":   (D["02"], "extent", ("row", 215, 225, 590, (230, 215), 12), "Chat / Work control, width"),
    "size.segmented.h":   (D["02"], "extent", ("col", 400, 140, 290, (400, 145), 12), "Chat / Work control, height"),
    "size.segmentThumb":  (D["02"], "bbox", ((300, 240), (240, 160, 180, 110), 3), "Chat / Work thumb"),
    "size.composer.w":    (D["02"], "extent", ("row", 1600, 20, 800, (25, 1600), 12), "Composer, width"),
    "size.composer.h":    (D["02"], "extent", ("col", 400, 1480, 1740, (400, 1490), 12), "Composer, height"),
    "size.sendButton":    (C["03"], "bbox", ((705, 1660), (670, 1590, 110, 120), 20), "Send button"),
    "size.card":          (C["09"], "bbox", ((420, 375), (30, 340, 760, 350), 3), "Settings card, three rows"),
    "size.cardOneRow":    (C["11"], "bbox", ((450, 370), (30, 330, 760, 140), 3), "One-row card (Start screen)"),
    "rows.settings":      (C["09"], "find", ("col", 400, 340, 700, None, 0), "Row edges down the first settings card"),
    "size.switch":        (C["11"], "bbox", ((615, 700), (580, 660, 180, 100), 20), "Switch track"),
    "size.switchThumb":   (D["11"], "bbox", ((670, 700), (640, 670, 100, 80), 10), "Switch thumb"),
    "size.chatPill":      (C["05"], "bbox", ((130, 1615), (60, 1580, 270, 140), 24), "Sidebar 'Chat' pill"),
    "size.newTask":       (C["21"], "bbox", ((530, 1615), (480, 1570, 290, 140), 24), "'New task' pill"),
    "size.inkButton":     (C["19"], "bbox", ((318, 740), (290, 710, 240, 120), 24), "'New chat' pill"),
    "size.tab":           (D["21"], "extent", ("row", 330, 30, 240, (40, 290), 12), "Selected tab pill, width"),
    "size.tab.h":         (D["21"], "extent", ("col", 90, 290, 420, (90, 292), 12), "Selected tab pill, height"),
    "size.menuIcon":      (D["04"], "bbox", ((80, 1100), (55, 1015, 130, 130), 6), "Round icon well in the plus menu"),
    "size.menu.w":        (D["04"], "extent", ("row", 1150, 20, 800, (700, 1150), 12), "Plus menu, width"),
    "size.dialog.w":      (D["12"], "extent", ("row", 955, 50, 760, (60, 955), 6), "Alert, width"),
    "size.dialog.h":      (D["12"], "extent", ("col", 400, 745, 1109, (400, 745), 6), "Alert, height"),
    "size.dialogButton":  (D["12"], "bbox", ((140, 995), (100, 960, 310, 130), 6), "Alert button (Cancel)"),
    "size.searchBar.h":   (D["20"], "extent", ("col", 400, 1540, 1720, (400, 1545), 12), "Search field, height"),
    "size.searchBar.w":   (D["20"], "extent", ("row", 1590, 20, 665, (25, 1590), 12), "Search field, width"),
    "size.searchTile":    (C["19"], "bbox", ((370, 520), (350, 440, 110, 110), 6), "Empty-state magnifier tile"),
    "size.progress.h":    (C["14"], "extent", ("col", 600, 455, 500, (600, 458), 6), "Usage meter track, height"),
    "size.userBubble":    (D["08"], "bbox", ((600, 560), (200, 360, 600, 600), 4), "The owner's bubble (nine lines)"),
    "size.slider.h":      (D["16"], "extent", ("col", 500, 1530, 1700, (500, 1535), 12), "Effort slider track, height"),
    "size.sliderThumb":   (D["16"], "bbox", ((345, 1615), (300, 1560, 110, 120), 20), "Effort slider thumb"),
    # ---------------------------------------------------------------- radii
    "radius.card":        (C["09"], "diag", (400, 380, 150, 455), "Settings card"),
    "radius.composer":    (D["02"], "diag", (400, 1540, 60, 1600), "Composer"),
    "radius.userBubble":  (D["08"], "diag", (700, 395, 240, 450), "The owner's bubble"),
    "radius.dialog":      (D["12"], "diag", (400, 790, 110, 950), "Alert"),
    "radius.menuPlus":    (D["04"], "diag", (300, 1010, 50, 1150), "Plus menu"),
    "radius.menuChat":    (D["07"], "diag", (500, 185, 290, 860), "Chat menu"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.navTitle":      (D["13"], "cap", (285, 195, 308, 240), "'P' of a nav title ('Personalization')"),
    "type.sidebarTitle":  (D["05"], "cap", (232, 195, 264, 240), "'T' of the sidebar title ('ChatGPT')"),
    "type.body":          (D["09"], "cap", (160, 395, 183, 435), "'P' of a settings row"),
    "type.sectionHeader": (D["09"], "cap", (88, 1262, 112, 1300), "'T' of a section header ('Theme')"),
    "type.footnote":      (D["13"], "cap", (88, 470, 115, 505), "'M' of helper text"),
    "type.composer":      (D["02"], "cap", (74, 1550, 100, 1590), "'A' of the composer placeholder"),
    "type.suggestion":    (D["02"], "cap", (135, 1235, 160, 1275), "'S' of a suggestion"),
    "type.thread":        (D["06"], "cap", (50, 908, 76, 950), "'A' of reply text"),
    "type.threadBold":    (D["06"], "cap", (50, 1308, 74, 1345), "'K' of bold reply text"),
    "type.userBubble":    (D["08"], "cap", (257, 410, 292, 445), "'W' of bubble text"),
    "type.sidebarItem":   (D["05"], "cap", (153, 303, 178, 338), "'Y' of a sidebar item"),
    "type.recent":        (D["05"], "cap", (80, 975, 104, 1012), "'T' of a recent chat"),
    "type.segment":       (D["02"], "cap", (450, 200, 486, 235), "'W' of a segment label"),
    "type.menuItem":      (D["07"], "cap", (393, 393, 411, 428), "'P' of a chat-menu item"),
    "type.plusItem":      (D["04"], "cap", (193, 1332, 212, 1368), "'F' of a plus-menu item"),
    "type.menuHeader":    (D["07"], "cap", (320, 198, 338, 226), "'T' of the chat-menu header"),
    "type.dialogTitle":   (D["12"], "cap", (148, 810, 170, 845), "'E' of the alert title"),
    "type.dialogBody":    (D["12"], "cap", (147, 903, 166, 935), "'P' of the alert body"),
    "type.dialogButton":  (D["12"], "cap", (513, 1010, 533, 1045), "'R' of 'Retry'"),
    "type.emptyTitle":    (D["19"], "cap", (330, 575, 352, 608), "'N' of an empty-state title"),
    "type.emptyBody":     (D["19"], "cap", (195, 625, 217, 656), "'Y' of an empty-state body"),
    "type.tab":           (D["21"], "cap", (82, 340, 110, 372), "'A' of a tab label"),
    "type.cardTitle":     (D["21"], "cap", (170, 585, 200, 617), "'M' of a task-card title"),
    "type.cardBody":      (D["21"], "cap", (170, 872, 187, 902), "'E' of a task-card description"),
    "type.pillButton":    (D["21"], "cap", (546, 1622, 570, 1656), "'N' of 'New task'"),
    "type.timestamp":     (D["08"], "cap", (330, 302, 349, 330), "'T' of the thread date line"),
    "type.usageRow":      (D["14"], "cap", (89, 413, 126, 447), "'W' of a usage row"),
    "type.usageFoot":     (D["14"], "cap", (89, 506, 104, 533), "'R' of 'Resets'"),
    "lines.thread":       (D["06"], "lines", (50, 905, 290, 1045), "Three lines of reply text"),
    "lines.userBubble":   (D["08"], "lines", (257, 405, 737, 905), "Lines in the owner's bubble"),
    "lines.sidebar":      (D["05"], "lines", (80, 290, 330, 830), "Sidebar nav items"),
    "lines.recents":      (D["05"], "lines", (80, 970, 540, 1400), "Recent chats"),
    "lines.suggestions":  (D["02"], "lines", (135, 1230, 755, 1470), "Suggestion rows"),
    "lines.taskBody":     (D["21"], "lines", (168, 625, 693, 735), "Three-line task description"),
    "lines.footnote":     (D["13"], "lines", (88, 470, 718, 530), "Two-line helper text"),
    "lines.dialogBody":   (D["12"], "lines", (147, 862, 667, 942), "Two-line alert body"),
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
    if start == a or end == b - 1:   # the control runs to the scan's end, so the scan did not find its edge
        raise ValueError(f"extent reached the scan limit ({a} to {b - 1}): widen the scan or move the background point")
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
    # A reading without a theme prefix is read in both themes; a theme missing for one means a capture is absent.
    short = sorted(rid for rid, (cap, *_) in R.items()
                   if set(readings.get(rid, {})) != ({cap.split("/")[0]} if "/" in cap else {"dark", "light"}))
    if short:
        raise SystemExit(f"{len(short)} readings lack a theme they need ({', '.join(short[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
