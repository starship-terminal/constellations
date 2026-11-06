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

NAME = "Gemini"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

HOME = "04-home-greeting-chat-task-toggle-composer"
TYPED = "05-composer-typed-send"
PLUS = "06-plus-sheet-tiles-tools-list"
MODEL = "07-model-picker-menu"
TASK = "08-task-mode-suggestions-purple"
SIDEBAR = "09-sidebar-nav-notebooks-account"
THREAD = "10-chat-thread-media-bubble-actions"
CHATMENU = "11-chat-menu-destructive"
SETTINGS = "12-settings-sheet-grouped"
USAGE = "13-usage-limits-badge-progress"
MEMORY = "14-memory-switch-on-tonal-button-empty"
VOICE = "15-voice-settings-switch-on"
SEARCH = "17-search-focused-recent-list"
NORESULT = "18-search-no-results-empty"
STUDENTS = "19-students-cards-empty-notebook-card"
SCHEDULED = "20-scheduled-suggestion-cards"
IMAGES = "21-images-intro-sheet-glass"
ACCOUNT = "23-account-sheet-pro-badge"

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            (HOME, "fill", (300, 400, 200, 50), "Home background, above the greeting"),
    "bg.glow":            (HOME, "fill", (300, 1740, 200, 10), "Home background at the bottom edge, where the glow is strongest"),
    "bg.glowTask":        (TASK, "fill", (300, 1740, 200, 10), "Task mode background at the bottom edge (the purple glow)"),
    "bg.sheet":           (SETTINGS, "fill", (300, 300, 200, 30), "Settings sheet background"),
    "bg.sheetAccount":    (ACCOUNT, "fill", (300, 1200, 200, 50), "Account sheet background"),
    "scrim.refDark":      ("dark/" + HOME, "fill", (100, 225, 15, 15), "Menu button glass, undimmed"),
    "scrim.dimDark":      ("dark/" + PLUS, "fill", (100, 225, 15, 15), "Menu button glass under the + sheet's scrim"),
    "scrim.refLight":     ("light/" + HOME, "fill", (300, 400, 200, 50), "Home background, undimmed"),
    "scrim.dimLight":     ("light/" + PLUS, "fill", (300, 400, 200, 50), "Home background under the + sheet's scrim"),
    "surface.card":       (VOICE, "fill", (200, 500, 350, 12), "Grouped settings card (Voice), between the divider and the next row"),
    "surface.cardAccount": (ACCOUNT, "fill", (600, 560, 100, 20), "Row card on the account sheet (Manage your Google Account)"),
    "surface.cardSuggestion": (SCHEDULED, "fill", (600, 540, 100, 15), "Suggestion card (Scheduled)"),
    "surface.cardNotebook": (STUDENTS, "fill", (650, 1220, 80, 15), "Empty study-notebook card (Students)"),
    "surface.cardUsage":  (USAGE, "fill", (400, 700, 150, 10), "Usage card"),
    "surface.bubble":     ("dark/" + THREAD, "fill", (600, 1135, 100, 12), "The owner's message bubble, below the text"),
    "surface.bubbleLight": ("light/" + THREAD, "fill", (600, 1260, 100, 12), "The owner's message bubble, below the text"),
    "surface.composer":   (HOME, "fill", (420, 1665, 100, 15), "Composer capsule (glass; centre reading)"),
    "surface.glass":      (HOME, "fill", (100, 225, 15, 15), "Round glass menu button (centre reading)"),
    "surface.segment":    (HOME, "fill", (372, 1490, 20, 15), "Selected Chat pill of the Chat / Task toggle"),
    "surface.menu":       (MODEL, "fill", (550, 300, 80, 40), "Model picker menu (glass; centre reading)"),
    "surface.menuPopup":  ("16-theme-popup-menu", "fill", (620, 1300, 80, 30), "Theme pop-up menu over the settings card (light)"),
    "surface.menuPopupDark": ("dark/16-theme-popup-menu-not-changed", "fill", (620, 1300, 80, 30), "Theme pop-up menu over the settings card"),
    "surface.sheetPlus":  (PLUS, "fill", (650, 1250, 100, 30), "+ sheet (glass over the page)"),
    "surface.tile":       (PLUS, "fill", (80, 925, 30, 30), "Photos tile on the + sheet"),
    "surface.track":      (USAGE, "fill", (400, 780, 200, 8), "Usage progress track (0% used)"),
    "surface.badge":      (USAGE, "fill", (478, 398, 6, 30), "PRO badge beside the Usage limits title"),
    "surface.navSelected": ("dark/" + SIDEBAR, "fill", (500, 345, 200, 40), "Current row in the sidebar (New chat)"),
    "surface.signIn":     ("dark/01-onboarding-sign-in-gate", "fill", (300, 1470, 200, 20), "Google sign-in sheet at onboarding"),
    "surface.alert":      ("dark/03-system-notification-permission-alert", "fill", (650, 790, 40, 40), "iOS permission alert (system glass)"),
    "border.divider":     (VOICE, "fill", (300, 489, 300, 1), "Hairline between grouped rows (one pixel row)"),
    # ---------------------------------------------------------------- text
    "text.primary":       (HOME, "text", (172, 865, 130, 60), "Greeting ('Let's')"),
    "text.body":          ("dark/" + THREAD, "text", (64, 1238, 400, 35), "Gemini's reply text"),
    "text.bodyLight":     ("light/" + THREAD, "text", (64, 1363, 400, 35), "Gemini's reply text"),
    "text.onBubble":      ("dark/" + THREAD, "text", (168, 1038, 300, 35), "Text in the owner's bubble"),
    "text.onBubbleLight": ("light/" + THREAD, "text", (168, 1162, 300, 35), "Text in the owner's bubble"),
    "text.menuItem":      (MODEL, "text", (290, 215, 200, 35), "Model name in the picker"),
    "text.modelName":     (HOME, "text", (298, 195, 140, 40), "Model name beside 'Gemini' in the title ('Flash-Lite')"),
    "text.menuSubtitle":  (MODEL, "text", (288, 258, 195, 30), "Model description in the picker ('Fastest answers')"),
    "text.rowSubtitle":   (VOICE, "text", (160, 425, 410, 35), "Settings row subtitle"),
    "text.sectionHeader": (SETTINGS, "text", (88, 470, 112, 32), "Settings section header ('Account')"),
    "text.timestamp":     (SEARCH, "text", (678, 330, 85, 35), "Search result age ('3 days')"),
    "text.cardBody":      (SCHEDULED, "text", (88, 620, 500, 32), "Suggestion card description"),
    "text.helper":        (USAGE, "text", (80, 612, 235, 35), "Helper line ('Updated just now')"),
    "text.disclaimer":    ("dark/" + THREAD, "text", (64, 1445, 435, 30), "Disclaimer under the thread"),
    "text.placeholder":   (HOME, "text", (224, 1608, 175, 40), "Composer placeholder ('Ask Gemini')"),
    "text.searchPlaceholder": (SEARCH, "text", (142, 1608, 96, 35), "Search field placeholder"),
    "text.segmentOff":    (HOME, "text", (448, 1486, 55, 30), "Unselected segment label ('Task')"),
    "text.badge":         (USAGE, "text", (413, 398, 60, 30), "PRO badge label"),
    "text.link":          (USAGE, "text", (537, 545, 150, 30), "Inline link ('Learn more')"),
    "text.action":        (ACCOUNT, "text", (678, 215, 78, 35), "Text button in a sheet header ('Done')"),
    "text.danger":        (CHATMENU, "text", (395, 720, 95, 35), "Destructive menu item ('Delete')"),
    "text.onAlert":       ("dark/03-system-notification-permission-alert", "text", (148, 870, 440, 30), "Alert message (iOS system text)"),
    # ---------------------------------------------------------------- accent and controls
    "accent.dot":         ("dark/" + HOME, "fill", (504, 210, 6, 6), "Blue dot after the model name"),
    "accent.ring":        (ACCOUNT, "fill", (74, 380, 4, 20), "Ring around the account avatar"),
    "accent.caret":       ("light/" + HOME, "fill", (217, 1606, 2, 44), "Text caret in the focused composer"),
    "button.primary":     ("dark/02-onboarding-get-started-terms", "fill", (100, 1550, 100, 15), "Get started (capsule on the onboarding glow)"),
    "button.primaryLabel": ("dark/02-onboarding-get-started-terms", "text", (320, 1550, 170, 40), "Get started label"),
    "button.signIn":      ("dark/01-onboarding-sign-in-gate", "fill", (100, 1640, 100, 10), "Continue as Kai (Google sign-in button)"),
    "button.signInLabel": ("dark/01-onboarding-sign-in-gate", "text", (305, 1640, 200, 40, "inverse"), "Continue as Kai label"),
    "button.tonal":       (MEMORY, "fill", (210, 878, 20, 12), "Add button (filled capsule)"),
    "button.tonalLabel":  (MEMORY, "text", (140, 892, 58, 38, "inverse"), "Add label"),
    "button.send":        (TYPED, "fill", (660, 1598, 12, 12), "Send button, with text typed"),
    "button.sendGlyph":   (TYPED, "text", (676, 1598, 30, 55), "Send arrow"),
    "button.voice":       (HOME, "fill", (628, 1600, 10, 10), "Voice (Live) button, empty composer"),
    "button.voiceTask":   (TASK, "fill", (628, 1600, 10, 10), "Voice (Live) button in Task mode"),
    "button.voiceGlyph":  (HOME, "text", (640, 1600, 40, 55), "Voice glyph (bars)"),
    "switch.on":          (MEMORY, "fill", (662, 415, 14, 30), "Switch on, Material style (Memory): track"),
    "switch.thumb":       (MEMORY, "fill", (735, 412, 6, 6), "Switch on, Material style: thumb, beside the tick"),
    "switch.tick":        (MEMORY, "text", (705, 415, 40, 30), "Tick on the Material switch's thumb"),
    "switch.onSystem":    (VOICE, "fill", (612, 575, 20, 15), "Switch on, iOS style (Voice): track"),
    "switch.thumbSystem": (VOICE, "fill", (680, 570, 20, 10), "Switch on, iOS style: thumb"),
    # ---------------------------------------------------------------- sizes
    "size.navButton.w":   ("dark/" + HOME, "extent", ("row", 214, 20, 180, (25, 214), 12), "Round glass menu button, width"),
    "size.navButton.h":   ("dark/" + HOME, "extent", ("col", 92, 150, 290, (92, 155), 12), "Round glass menu button, height"),
    "size.closeButton.h": ("dark/" + SETTINGS, "extent", ("col", 720, 180, 320, (720, 185), 12), "Round glass close button, height"),
    "size.composer.w":    ("dark/" + HOME, "find", ("row", 1627, 20, 790, (29, 31, 38), 8), "Composer capsule, empty: pixels along a row close to its fill"),
    "size.composer.h":    ("dark/" + HOME, "find", ("col", 420, 1520, 1760, (29, 31, 38), 8), "Composer capsule: pixels down a column close to its fill"),
    "size.composerTyped.w": ("dark/" + TYPED, "find", ("row", 1627, 20, 790, (29, 31, 38), 8), "Composer capsule, with text: pixels along a row close to its fill"),
    "size.sendButton.w":  ("dark/" + TYPED, "extent", ("row", 1627, 630, 760, (640, 1627), 12), "Send button width"),
    "size.sendButton.h":  ("dark/" + TYPED, "extent", ("col", 690, 1570, 1690, (690, 1575), 12), "Send button height"),
    "size.voiceButton.w": ("dark/" + HOME, "extent", ("row", 1627, 600, 720, (610, 1627), 12), "Voice button width"),
    "size.segment.w":     ("light/" + HOME, "find", ("row", 1500, 250, 430, (255, 255, 255), 2), "Selected segment pill (Chat): white pixels along a row"),
    "size.segment.h":     ("light/" + HOME, "find", ("col", 300, 1440, 1550, (255, 255, 255), 2), "Selected segment pill: white pixels down a column"),
    "size.switch":        (MEMORY, "bbox", ((662, 415), (630, 380, 150, 100), 12), "Material switch track"),
    "size.switchSystem":  (VOICE, "bbox", ((612, 575), (580, 540, 170, 90), 12), "iOS switch track"),
    "size.tonalButton":   (MEMORY, "bbox", ((210, 878), (40, 850, 230, 120), 12), "Add button"),
    "size.card":          (VOICE, "bbox", ((200, 505), (20, 320, 780, 380), 3), "Voice settings card (two rows)"),
    "size.cardSuggestion": (SCHEDULED, "bbox", ((600, 540), (20, 500, 780, 250), 3), "Suggestion card"),
    "size.cardAccount":   (ACCOUNT, "bbox", ((600, 560), (30, 500, 760, 150), 3), "Account sheet row card"),
    "size.bubble":        ("dark/" + THREAD, "bbox", ((600, 1135), (90, 970, 690, 220), 4), "The owner's two-line bubble"),
    "size.videoCard.w":   ("dark/" + THREAD, "extent", ("row", 630, 20, 800, (30, 630), 30), "Video result card, width"),
    "size.primaryButton": ("dark/02-onboarding-get-started-terms", "bbox", ((100, 1550), (40, 1500, 730, 140), 6), "Get started button"),
    "size.signInButton":  ("dark/01-onboarding-sign-in-gate", "bbox", ((100, 1640), (30, 1600, 750, 110), 6), "Continue as Kai button"),
    "size.grabber.w":     ("dark/" + SETTINGS, "extent", ("row", 186, 320, 490, (330, 186), 12), "Sheet grabber width"),
    "size.grabber.h":     ("dark/" + SETTINGS, "extent", ("col", 405, 170, 200, (405, 172), 12), "Sheet grabber height"),
    "size.menu.w":        ("dark/" + MODEL, "extent", ("row", 450, 100, 750, (110, 450), 12), "Model picker menu width"),
    "size.menu.h":        ("dark/" + MODEL, "extent", ("col", 600, 150, 860, (600, 155), 12), "Model picker menu height (four models and a row)"),
    "rows.settings":      ("dark/" + SETTINGS, "find", ("col", 600, 860, 1500, None, 0), "Row edges down the Preferences card"),
    # ---------------------------------------------------------------- radii
    "radius.card":        (VOICE, "diag", (300, 360, 70, 420), "Voice settings card"),
    "radius.cardSuggestion": (SCHEDULED, "diag", (400, 545, 75, 640), "Suggestion card"),
    "radius.cardAccount": (ACCOUNT, "diag", (400, 535, 64, 574), "Account sheet row card"),
    "radius.bubble":      ("dark/" + THREAD, "diag", (400, 1012, 150, 1080), "The owner's bubble"),
    "radius.bubbleLight": ("light/" + THREAD, "diag", (400, 1137, 150, 1205), "The owner's bubble"),
    "radius.menu":        ("dark/" + MODEL, "diag", (400, 185, 185, 400), "Model picker menu"),
    "radius.sheet":       ("dark/" + ACCOUNT, "diag", (400, 190, 40, 260), "Account sheet top corner"),
    "radius.composer":    ("dark/" + HOME, "diag", (420, 1575, 120, 1627), "Composer (capsule)"),
    "radius.alert":       ("dark/03-system-notification-permission-alert", "diag", (400, 735, 110, 900), "iOS permission alert"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.greeting":      ("dark/" + HOME, "cap", (168, 860, 200, 925), "'L' of the greeting"),
    "type.onboarding":    ("dark/02-onboarding-get-started-terms", "cap", (114, 470, 141, 532), "'L' of the onboarding title"),
    "type.taskGreeting":  ("dark/" + TASK, "cap", (144, 675, 205, 740), "'W' of the Task mode greeting"),
    "type.largeTitle":    ("dark/" + SETTINGS, "cap", (47, 330, 88, 395), "'S' of the Settings title"),
    "type.pageTitle":     ("dark/" + STUDENTS, "cap", (126, 448, 150, 502), "'L' of the Students page title"),
    "type.navTitle":      ("dark/" + VOICE, "cap", (360, 225, 392, 268), "'V' of a nav title ('Voice')"),
    "type.rowTitle":      ("dark/" + SETTINGS, "cap", (158, 885, 182, 930), "'N' of a settings row ('Notifications')"),
    "type.sectionHeader": ("dark/" + SETTINGS, "cap", (86, 465, 112, 505), "'A' of a section header ('Account')"),
    "type.menuItem":      ("dark/" + CHATMENU, "cap", (392, 295, 412, 338), "'P' of a menu item ('Pin')"),
    "type.menuSubtitle":  ("dark/" + MODEL, "cap", (286, 255, 302, 291), "'F' of a model description"),
    "type.body":          ("dark/" + THREAD, "cap", (62, 1235, 73, 1275), "'I' of Gemini's reply"),
    "type.bubble":        ("dark/" + THREAD, "cap", (165, 1032, 197, 1078), "'O' of the owner's bubble"),
    "type.disclaimer":    ("dark/" + THREAD, "cap", (62, 1440, 87, 1480), "'G' of the disclaimer"),
    "type.composer":      ("dark/" + HOME, "cap", (215, 1600, 244, 1650), "'A' of the composer placeholder"),
    "type.sidebarItem":   ("dark/" + SIDEBAR, "cap", (144, 345, 170, 392), "'N' of a sidebar row ('New chat')"),
    "type.sidebarHeader": ("dark/" + SIDEBAR, "cap", (63, 900, 87, 945), "'N' of the sidebar section header"),
    "type.searchRow":     ("dark/" + SEARCH, "cap", (118, 325, 146, 368), "'A' of a search result title"),
    "type.cardTitle":     ("dark/" + SCHEDULED, "cap", (86, 795, 108, 840), "'B' of a suggestion card title"),
    "type.cardBody":      ("dark/" + SCHEDULED, "cap", (86, 845, 105, 885), "'T' of a suggestion card description"),
    "type.usageTitle":    ("dark/" + USAGE, "cap", (78, 915, 112, 955), "'W' of a usage card title ('Weekly limit')"),
    "type.button":        ("dark/" + IMAGES, "cap", (370, 1545, 393, 1590), "'T' of a full-width button ('Try it')"),
    "type.subtitle":      ("dark/" + VOICE, "cap", (158, 570, 177, 612), "'T' of a settings row subtitle"),
    "type.segment":       ("dark/" + HOME, "cap", (445, 1480, 467, 1520), "'T' of a segment label ('Task')"),
    "type.emptyTitle":    ("dark/" + NORESULT, "cap", (327, 838, 351, 880), "'N' of an empty-state title"),
    "type.emptyBody":     ("dark/" + NORESULT, "cap", (182, 885, 204, 925), "'N' of an empty-state line"),
    "type.badge":         ("dark/" + USAGE, "cap", (412, 395, 431, 432), "'P' of the PRO badge"),
    "lines.body":         ("dark/" + THREAD, "lines", (64, 1235, 740, 1325), "Two lines of Gemini's reply"),
    "lines.bubble":       ("dark/" + THREAD, "lines", (168, 1035, 690, 1125), "Two lines in the owner's bubble"),
    "lines.subtitle":     ("dark/" + VOICE, "lines", (160, 575, 520, 645), "Two-line settings row subtitle"),
    "lines.cardBody":     ("dark/" + SCHEDULED, "lines", (88, 620, 600, 690), "Two-line suggestion card description"),
    "lines.greeting":     ("dark/" + TASK, "lines", (145, 680, 670, 822), "Two-line Task mode greeting"),
    "lines.menu":         ("dark/" + CHATMENU, "lines", (390, 205, 425, 430), "First letters of the first three menu items (above the video): the row pitch"),
    "lines.sidebar":      ("dark/" + SIDEBAR, "lines", (145, 340, 450, 830), "Sidebar row labels: the row pitch"),
    "lines.search":       ("dark/" + SEARCH, "lines", (120, 320, 520, 1490), "Search result titles: the row pitch"),
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
    if not hits:
        raise ValueError(f"extent: nothing on {axis} {line} from {a} to {b - 1} differs from the background by more than {thr}")
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
    if not xs:
        raise ValueError(f"bbox: no pixel within {tol} of {hexof(ref)} in window {window}")
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
    while x > 0 and d(rows[cy][x - 1], f) <= 3:
        x -= 1
    if x < 5:
        raise ValueError(f"diag: no edge with background beyond it left of ({cxr}, {cy})")
    bg = rows[cy][x - 5]
    tol = max(2, d(bg, f) // 2)
    while x > 0 and d(rows[cy][x - 1], f) <= tol:
        x -= 1
    x0, y = x, cyc
    while y > 0 and d(rows[y - 1][cx], f) <= tol:
        y -= 1
    if x0 == 0 or y == 0:
        raise ValueError(f"diag: the fill at ({cxr}, {cy}) runs to the image edge")
    t = 0
    while d(rows[y + t][x0 + t], f) > tol:
        t += 1
        if y + t >= len(rows) or x0 + t >= len(rows[0]):
            raise ValueError(f"diag: no fill on the diagonal from corner ({x0}, {y})")
    r = t / (1 - 2 ** -0.5) / SCALE
    return {"value": f"{r:.1f}pt", "inset": t, "corner": [x0, y], "evidence": "Derived"}


def op_cap(rows, x0, y0, x1, y1):
    bg = rows[y0][x0]
    ys = [y for y in range(y0, y1) if any(d(rows[y][x], bg) > 30 for x in range(x0, x1))]
    if not ys:
        raise ValueError(f"cap: no ink in ({x0}, {y0}, {x1}, {y1})")
    ink = ys[-1] - ys[0] + 1
    cap = (ink - 1) / SCALE          # one pixel of the ink height is anti-aliasing
    return {"value": f"{round(cap / CAP_EM)}pt", "capHeight": f"{cap:g}pt", "inkPx": ink, "top": ys[0],
            "evidence": "Derived"}


def op_lines(rows, x0, y0, x1, y1):
    bg = rows[y0][x0]
    ink = [y for y in range(y0, y1) if any(d(rows[y][x], bg) > 30 for x in range(x0, x1))]
    if not ink:
        raise ValueError(f"lines: no ink in ({x0}, {y0}, {x1}, {y1})")
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
    pending, out = {}, {}
    for rid, (cap, op, args, note) in R.items():
        themes = [cap.split("/")[0]] if "/" in cap else ["dark", "light"]
        name = cap.split("/")[-1]
        for theme in themes:
            png = raw / theme / f"{name}.png"
            if not png.exists():
                continue
            pending.setdefault(f"{theme}/{name}", []).append((rid, op, args, note))
    # One decoded capture at a time: a decoded capture is several hundred MB as Python tuples, so
    # the readings are grouped by capture and each image is released before the next is read.
    for key in sorted(pending):
        theme, name = key.split("/")
        rows = sample.read_png(raw / theme / f"{name}.png")[2]
        for rid, op, args, note in pending[key]:
            if op == "fill":
                res = op_fill(rows, *args)
            elif op == "text":
                res = op_text(rows, *args, dark=(theme == "dark"))
            else:
                res = globals()["op_" + op](rows, *args)
            res.update({"capture": f"screenshots/{theme}/{name}.png", "op": op,
                        "args": json.loads(json.dumps(args)), "note": note})
            out.setdefault(rid, {})[theme] = res
        del rows   # released before the next capture is decoded
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
