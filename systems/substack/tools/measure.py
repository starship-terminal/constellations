#!/usr/bin/env python3
"""Read a native app's values out of the full-colour iPhone Mirroring captures (native kit).

    python3 tools/measure.py ~/.design-systems/<slug>/raw-shots

Adapted from the native kit (tools/kit/native, from systems/grokbot): NAME and the reading table R,
marked PRODUCT (adapt), are Substack's. The ops below are the kit's, plus ring.

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
  ring    the same for an outlined shape, walking in from its outer corner  Derived (about +-2 pt)
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

NAME = "Substack"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# Capture names, shortened. Dark has all 19; light has 16 (no 01, 10 or 19).
PRE = "01-notification-preprompt-sheet"
HOME = "02-home-feed-notes-stories-fab-tabbar"
READ = "03-read-tabs-featured-card-inbox-unread"
SAVED = "04-saved-tab-progress-rows"
POST = "05-post-reader-serif-subscribe-action-bar"
OPTS = "06-post-options-sheet-destructive"
DISP = "07-display-settings-option-buttons-selected"
SFOC = "08-search-focused-chips-trending"
STYP = "09-search-typed-highlighted-results"
SNONE = "10-search-no-results-find-people"
POD = "11-podcasts-cards-play-pills"
ACT = "12-activity-feed-primary-secondary-buttons"
PROF = "13-profile-share-edit-tabs-note"
SET = "14-settings-sheet-grouped-icons"
PAY = "15-payments-empty-state-link-button"
ENG = "16-notification-checkbox-grid-destructive-button"
APP = "17-appearance-switches-checklists"
CHAT = "18-chat-list-warning-banner-unread"
NOTE = "19-note-longpress-options-destructive-group"

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            (SAVED, "fill", (300, 1200, 200, 50), "Tab screens (Home, Read, Search, Chat, Activity) and the post reader"),
    "bg.grouped":         (PAY, "fill", (300, 1200, 200, 100), "Settings sheet and its pushed pages, behind the grouped cards"),
    "surface.card":       (PAY, "fill", (300, 820, 200, 20), "Grouped card in Settings ('No subscriptions yet')"),
    "surface.cardSettings": (SET, "fill", (450, 690, 150, 10), "Grouped card on the Settings sheet (Saved row)"),
    "surface.sheet":      (OPTS, "fill", (400, 1650, 200, 30), "Options sheet"),
    "surface.sheetDisplay": (DISP, "fill", (300, 1460, 200, 20), "Display Settings sheet"),
    "surface.sheetPrompt": ("dark/" + PRE, "fill", (400, 1430, 30, 10), "Notifications pre-prompt sheet"),
    "surface.raised":     (SAVED, "fill", (400, 470, 200, 10), "'View saved notes' row and the 'Find people you know' card"),
    "surface.banner":     (CHAT, "fill", (480, 760, 200, 10), "'Notifications are off' banner card"),
    "surface.secondary":  (CHAT, "fill", (180, 690, 20, 20), "'Later' button in the banner"),
    "surface.tile":       (PROF, "fill", (400, 920, 200, 10), "Creator stats card and the Listen pill"),
    "surface.chip":       (PROF, "fill", (60, 610, 8, 8), "'1 recommendation' chip on the profile"),
    "surface.iconTile":   (SET, "fill", (76, 650, 8, 8), "Rounded tile behind a settings row icon"),
    "surface.glass":      (CHAT, "fill", (600, 450, 100, 20), "Chat search field (glass over a flat page, so it reads flat)"),
    "surface.glassButton": (POST, "fill", (60, 230, 10, 10), "Round glass back button (centre reading)"),
    "surface.tabBar":     (SAVED, "fill", (100, 1700, 20, 10), "Floating tab bar (glass)"),
    "surface.tabBarSelected": (SAVED, "fill", (210, 1620, 20, 10), "Selected item's pill inside the tab bar"),
    "surface.tabSelected": (READ, "fill", (55, 340, 10, 10), "Selected top tab pill ('For you', glass)"),
    "surface.optionSelected": (DISP, "fill", (320, 1640, 20, 8), "Selected option button ('Default') fill"),
    "surface.highlight":  (STYP, "fill", (340, 815, 6, 6), "Highlight behind the matched word in a search result"),
    "surface.promptButton": ("dark/" + PRE, "fill", (80, 1600, 30, 10), "'Enable notifications' button (orange tint)"),
    "surface.activityIcon": (ACT, "fill", (56, 415, 6, 6), "Circle behind the orange + on a subscribe activity row"),
    "surface.activityIconNote": (ACT, "fill", (56, 1115, 6, 6), "Circle behind the purple sparkle on a first-note activity row"),
    "scrim.ref":          (POST, "fill", (300, 300, 20, 20), "Post reader page, undimmed"),
    "scrim.sheet":        (OPTS, "fill", (300, 300, 20, 20), "The same point under the Options sheet's scrim"),
    "border.divider":     (READ, "fill", (300, 1224, 200, 1), "Hairline between inbox rows (one pixel row)"),
    "border.dividerGrouped": (SET, "fill", (300, 730, 200, 1), "Hairline between rows in a grouped card"),
    "border.dividerSheet": (OPTS, "fill", (300, 709, 200, 1), "Hairline under the Options sheet header"),
    "border.raised":      (SAVED, "fill", (300, 398, 200, 1), "Top rim of the 'View saved notes' row"),
    "border.option":      (DISP, "text", (330, 1330, 120, 4), "Rim of an unselected option button (Messina), the pixel furthest from the sheet"),
    "border.outlineButton": (ACT, "text", (621, 850, 4, 20), "Rim of the outlined 'Message' button"),
    # ---------------------------------------------------------------- text
    "text.primary":       (READ, "text", (55, 1100, 300, 35), "Inbox row title"),
    "text.reader":        (POST, "text", (57, 1005, 690, 35), "Serif body of a post"),
    "text.secondary":     (POST, "text", (57, 465, 670, 35), "Post subtitle under the title"),
    "text.kicker":        (POST, "text", (57, 320, 420, 25), "Publication name above a post title"),
    "text.byline":        (POST, "text", (57, 890, 260, 30), "Post date in the byline"),
    "text.handle":        (PROF, "text", (50, 385, 160, 30), "Profile handle line"),
    "text.tertiary":      (READ, "text", (110, 1035, 260, 35), "Publication name on an inbox row"),
    "text.meta":          (READ, "text", (52, 1165, 95, 30), "Read time and counts on an inbox row"),
    "text.date":          (READ, "text", (685, 1040, 70, 25), "Date on an inbox row"),
    "text.sectionHeader": (APP, "text", (50, 345, 120, 25), "Grouped section header ('PLAYBACK')"),
    "text.seeAll":        (READ, "text", (670, 965, 95, 30), "'See all' beside a section title"),
    "text.tabInactive":   (READ, "text", (215, 315, 80, 30), "Unselected top tab ('Latest')"),
    "text.tabActive":     (READ, "text", (70, 312, 95, 30), "Selected top tab ('For you')"),
    "text.tabBarActive":  (SAVED, "text", (250, 1678, 50, 22), "Selected tab bar label ('Read')"),
    "text.tabBarInactive": (SAVED, "text", (120, 1678, 60, 22), "Unselected tab bar label ('Home')"),
    "text.placeholder":   (CHAT, "text", (130, 437, 95, 30), "Chat search placeholder"),
    "text.placeholderSearch": (SFOC, "text", (245, 198, 130, 35), "Search screen placeholder ('Search...')"),
    "text.optionValue":   (DISP, "text", (625, 1265, 130, 25), "Current value beside a Display Settings header ('NEW YORK')"),
    "text.optionInactive": (DISP, "text", (345, 1365, 125, 35), "Label of an unselected option button ('Messina')"),
    "text.footnote":      (PAY, "text", (65, 520, 660, 25), "Helper text under a grouped card"),
    "text.rowSubtitle":   (APP, "text", (160, 580, 390, 25), "Subtitle under a settings row"),
    "text.email":         (SET, "text", (192, 530, 395, 25), "Email line on the Settings account card"),
    "text.noteAction":    (PROF, "text", (50, 1335, 40, 35), "Like icon under a note (outline glyph)"),
    "text.onBrand":       (CHAT, "text", (535, 695, 105, 35, "light"), "'Turn on' label on the orange button"),
    "text.onPublication": (POST, "text", (330, 1180, 150, 35, "light"), "'Subscribe' label on the publication-coloured button"),
    "text.link":          (PAY, "text", (230, 918, 350, 30), "'Restore in-app purchases' link button"),
    "text.linkInline":    (PAY, "text", (177, 588, 135, 25), "'Learn more' inline link"),
    "text.highlight":     (STYP, "text", (338, 805, 95, 30), "Matched word in a search result"),
    "text.selected":      (DISP, "text", (98, 1365, 140, 35), "Label of the selected option button ('New York')"),
    "text.danger":        (OPTS, "text", (148, 1550, 95, 35), "'Report' in the Options sheet"),
    "text.dangerButton":  (ENG, "text", (335, 1210, 145, 35), "'Disable all' button label"),
    "text.liked":         (SAVED, "text", (258, 905, 20, 20), "Filled heart on a liked post"),
    "text.brand":         (PROF, "text", (240, 1535, 100, 25), "Orange 'Subscribe' link on a note header"),
    "text.check":         (APP, "text", (705, 1195, 32, 30), "Tick on the chosen row of a checklist (Default tab: Home)"),
    "text.listen":        (POST, "text", (600, 775, 140, 40), "'Listen' label and play glyph"),
    # ---------------------------------------------------------------- accent and controls
    "brand.primary":      (CHAT, "fill", (470, 690, 30, 20), "'Turn on' button: the orange primary"),
    "brand.fab":          (HOME, "fill", (660, 1520, 10, 10), "Floating compose button"),
    "brand.share":        (PROF, "fill", (100, 765, 50, 10), "'Share' on the owner's profile (a lighter orange)"),
    "brand.dot":          (HOME, "fill", (700, 293, 6, 6), "Unread dot on a publication avatar"),
    "brand.promptLabel":  ("dark/" + PRE, "text", (255, 1605, 300, 40), "'Enable notifications' label"),
    "brand.activityIcon": (ACT, "text", (68, 415, 22, 25), "Orange + on a subscribe activity row"),
    "publication.button": (POST, "fill", (310, 1160, 30, 20), "'Subscribe' button in a post: the publication's own colour"),
    "publication.navPill": (POST, "fill", (470, 195, 20, 10), "'Subscribe' pill in the reader's nav bar (glass tint)"),
    "focus.caret":        (SFOC, "text", (238, 200, 5, 30), "Text caret in the focused search field"),
    "control.switchOn":   (APP, "fill", (630, 440, 15, 10), "Switch on"),
    "control.switchThumb": (APP, "fill", (680, 440, 20, 10), "Switch thumb"),
    "control.optionBorder": (DISP, "fill", (297, 1600, 1, 30), "Selected option button rim (one pixel column)"),
    "control.checkbox":   (ENG, "fill", (585, 625, 8, 8), "Checkbox, checked"),
    "control.checkboxTick": (ENG, "text", (590, 628, 30, 30, "inverse"), "Tick inside a checked checkbox"),
    "control.progressTrack": (SAVED, "fill", (103, 673, 18, 1), "Reading-progress track (one pixel row)"),
    "control.progressFill": (SAVED, "fill", (68, 673, 12, 1), "Reading-progress fill (one pixel row)"),
    # ---------------------------------------------------------------- sizes
    "size.tabBar.h":      (SAVED, "extent", ("col", 400, 1580, 1764, (400, 1580), 12), "Floating tab bar height"),
    "size.tabBar.w":      (SAVED, "extent", ("row", 1640, 20, 790, (30, 1640), 12), "Floating tab bar width"),
    "size.tabBarItem":    (SAVED, "bbox", ((275, 1612), (180, 1600, 200, 120), 6), "Selected item's pill inside the tab bar"),
    "size.navButton":     (POST, "extent", ("row", 215, 20, 200, (30, 300), 10), "Round glass back button, width"),
    "size.navSubscribe":  (POST, "bbox", ((470, 195), (430, 160, 240, 110), 30), "'Subscribe' pill in the nav bar"),
    "size.tabSelected.w": ("dark/" + READ, "extent", ("row", 340, 40, 200, (30, 380), 10), "Selected top tab pill, width"),
    "size.tabSelected.h": ("dark/" + READ, "extent", ("col", 60, 280, 380, (60, 380), 10), "Selected top tab pill, height"),
    "size.fab":           (HOME, "bbox", ((660, 1520), (600, 1420, 200, 200), 8), "Floating compose button"),
    "size.buttonLarge":   (PROF, "bbox", ((100, 765), (30, 720, 400, 120), 8), "'Share' button"),
    "size.buttonPublication": (POST, "bbox", ((310, 1160), (250, 1120, 320, 150), 8), "'Subscribe' button in a post"),
    "size.buttonSmall":   (ACT, "bbox", ((545, 430), (500, 380, 300, 100), 6), "'Subscribe back' button"),
    "size.buttonBanner":  (CHAT, "bbox", ((470, 690), (430, 650, 330, 120), 6), "'Turn on' button in the banner"),
    "size.searchField":   ("dark/" + CHAT, "bbox", ((600, 450), (30, 390, 760, 130), 3), "Chat search field"),
    "size.switch":        (APP, "bbox", ((630, 440), (590, 400, 180, 90), 20), "Switch track"),
    "size.checkbox":      (ENG, "bbox", ((585, 625), (560, 600, 90, 90), 6), "Checkbox"),
    "size.option":        (DISP, "bbox", ((320, 1640), (280, 1540, 260, 140), 3), "Option button fill, inside its rim"),
    "size.chip":          (SFOC, "bbox", ((60, 310), (30, 280, 230, 110), 6), "'Suggested' chip, selected"),
    "size.raisedRow":     (SAVED, "bbox", ((400, 470), (10, 380, 800, 140), 3), "'View saved notes' row"),
    "size.card":          (SET, "bbox", ((450, 690), (20, 610, 780, 370), 3), "Settings card with three rows"),
    "size.banner":        ("dark/" + CHAT, "bbox", ((480, 760), (30, 520, 760, 290), 3), "'Notifications are off' banner"),
    "size.progress":      (SAVED, "bbox", ((100, 673), (40, 660, 120, 30), 20), "Reading-progress bar"),
    "size.avatarStory":   ("dark/" + HOME, "extent", ("row", 300, 30, 230, (35, 300), 12), "Publication avatar in the top row, width"),
    "size.thumbnail.w":   (READ, "extent", ("row", 1150, 620, 790, (630, 1150), 12), "Post thumbnail on an inbox row, width"),
    "size.thumbnail.h":   (READ, "extent", ("col", 700, 1070, 1215, (630, 1150), 12), "Post thumbnail on an inbox row, height"),
    "rows.settings":      (SET, "find", ("col", 400, 600, 1300, None, 0), "Row edges down the Settings cards"),
    # ---------------------------------------------------------------- radii
    "radius.card":        (SET, "diag", (400, 640, 70, 700), "Settings card"),
    "radius.cardEmpty":   (PAY, "diag", (400, 720, 70, 780), "'No subscriptions yet' card"),
    "radius.buttonLarge": (PROF, "diag", (200, 760, 60, 780), "'Share' button"),
    "radius.buttonBanner": (CHAT, "diag", (550, 685, 460, 710), "'Turn on' button"),
    "radius.buttonPublication": (POST, "diag", (400, 1165, 300, 1195), "'Subscribe' button in a post"),
    "radius.buttonSmall": (ACT, "diag", (650, 405, 550, 425), "'Subscribe back' button"),
    "radius.checkbox":    (ENG, "diag", (603, 630, 587, 640), "Checkbox"),
    "radius.raisedCard":  ("dark/" + SNONE, "diag", (400, 450, 60, 495), "'Find people you know' card"),
    "radius.option":      (DISP, "ring", ((296, 1560), (5, 120, 248), 60), "Selected option button, outer edge of its rim"),
    "radius.sheet":       (OPTS, "diag", (250, 600, 60, 700), "Options sheet top corner"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.largeTitle":    ("dark/" + SET, "cap", (48, 335, 80, 390), "'S' of the Settings sheet title"),
    "type.screenTitle":   ("dark/" + READ, "cap", (50, 185, 80, 245), "'R' of a tab screen title ('Read')"),
    "type.postTitle":     ("dark/" + POST, "cap", (57, 365, 92, 425), "'H' of a post title"),
    "type.sectionTitle":  ("dark/" + READ, "cap", (48, 950, 80, 1000), "'Y' of a section title ('Your inbox')"),
    "type.sectionTitleB": ("dark/" + POD, "cap", (48, 410, 75, 450), "'N' of a section title ('Next up')"),
    "type.readerBody":    ("dark/" + POST, "cap", (553, 995, 578, 1045), "'F' of serif body text ('FREE')"),
    "type.postSubtitle":  ("dark/" + POST, "cap", (128, 458, 150, 500), "'L' of a post subtitle ('Learn')"),
    "type.noteBody":      ("dark/" + HOME, "cap", (48, 635, 67, 680), "'F' of note text"),
    "type.rowTitle":      ("dark/" + READ, "cap", (52, 1095, 72, 1140), "'B' of an inbox row title"),
    "type.settingsRow":   ("dark/" + SET, "cap", (160, 1590, 175, 1630), "'T' of a settings row ('Translations')"),
    "type.navTitle":      ("dark/" + PAY, "cap", (336, 228, 354, 265), "'P' of a nav title ('Payments')"),
    "type.sheetTitle":    ("dark/" + DISP, "cap", (56, 1095, 77, 1135), "'D' of a sheet title ('Display Settings')"),
    "type.button":        ("dark/" + PROF, "cap", (562, 760, 580, 800), "'E' of a button label ('Edit')"),
    "type.searchTitle":   ("dark/" + STYP, "cap", (160, 800, 183, 835), "'T' of a search result title"),
    "type.bannerTitle":   ("dark/" + CHAT, "cap", (160, 568, 182, 600), "'N' of the banner title"),
    "type.menuItem":      ("dark/" + OPTS, "cap", (147, 1190, 172, 1232), "'D' of an Options sheet item ('Download')"),
    "type.listen":        ("dark/" + POST, "cap", (645, 780, 667, 812), "'L' of 'Listen'"),
    "type.link":          ("dark/" + PAY, "cap", (228, 918, 246, 948), "'R' of a link button ('Restore')"),
    "type.emptyTitle":    ("dark/" + PAY, "cap", (262, 738, 284, 778), "'N' of an empty-state title"),
    "type.tabActive":     ("dark/" + READ, "cap", (70, 310, 90, 345), "'F' of the selected top tab"),
    "type.tabInactive":   ("dark/" + READ, "cap", (214, 310, 233, 345), "'L' of an unselected top tab"),
    "type.chip":          ("dark/" + SFOC, "cap", (272, 312, 292, 350), "'T' of a chip ('Technology')"),
    "type.meta":          ("dark/" + READ, "cap", (112, 1035, 132, 1072), "'D' of the publication name on an inbox row"),
    "type.searchSubtitle": ("dark/" + STYP, "cap", (160, 850, 175, 878), "'P' of a search result subtitle"),
    "type.kicker":        ("dark/" + POST, "cap", (57, 315, 72, 350), "'T' of the publication name above a post title"),
    "type.byline":        ("dark/" + POST, "cap", (57, 858, 75, 882), "'N' of the byline names"),
    "type.bannerSubtitle": ("dark/" + CHAT, "cap", (160, 620, 175, 645), "'T' of the banner subtitle"),
    "type.podcastMeta":   ("dark/" + POD, "cap", (64, 722, 85, 750), "'Y' of a podcast card title line"),
    "type.helper":        ("dark/" + PAY, "cap", (63, 512, 88, 550), "'A' of helper text under a card"),
    "type.sectionHeader": ("dark/" + APP, "cap", (48, 342, 64, 372), "'P' of a grouped section header ('PLAYBACK')"),
    "type.rowSubtitle":   ("dark/" + APP, "cap", (160, 582, 175, 605), "'W' of a settings row subtitle"),
    "type.tabBar":        ("dark/" + SAVED, "cap", (119, 1672, 137, 1700), "'H' of a tab bar label ('Home')"),
    "lines.noteBody":     ("dark/" + HOME, "lines", (48, 1250, 770, 1450), "Five lines of note text"),
    "lines.readerBody":   ("dark/" + POST, "lines", (57, 1000, 750, 1100), "Two lines of serif post text"),
    "lines.postSubtitle": ("dark/" + POST, "lines", (57, 460, 740, 710), "Five lines of post subtitle"),
    "lines.footnote":     ("dark/" + PAY, "lines", (64, 515, 740, 615), "Three lines of helper text"),
    "lines.rowSubtitle":  ("dark/" + APP, "lines", (160, 580, 560, 640), "Two lines of a settings row subtitle"),
    "lines.bio":          ("dark/" + PROF, "lines", (48, 465, 760, 580), "Three lines of the profile bio"),
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


def op_ring(rows, corner, ref, tol):
    """Corner radius of an outlined shape: corner is the top-left of the outline's bounding box; walk
    its diagonal to the first pixel within tol of the outline colour ref."""
    x0, y0 = corner
    t = 0
    while d(rows[y0 + t][x0 + t], ref) > tol:
        t += 1
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
