#!/usr/bin/env python3
"""Read a native app's values out of the full-colour iPhone Mirroring captures (native kit).

    python3 tools/measure.py ~/.design-systems/<slug>/raw-shots

Copied from the native kit (tools/kit/native, from systems/grokbot) and adapted for YouTube: NAME,
the capture names and the reading table R, whose boxes are capture pixels on YouTube's screens. Two
additions to the kit: an entry can give a box per theme (the light captures are laid out differently),
and a `corner` op reads the radius of a corner with no flat fill inside it (a thumbnail).

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

NAME = "YouTube"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# The captures, by short name. 06 and 12 differ between the themes.
UPSELL, HOME, ADSHEET, SEARCH, TYPED = ("01-premium-upsell-interstitial", "02-home-ad-shorts-shelf-tabbar",
                                        "03-ad-centre-sheet-accordions", "04-search-focused-history-rows",
                                        "05-search-typed-suggestions")
SHORTS, YOU, SORT, SETTINGS, GENERAL = ("07-shorts-player-action-rail-subscribe", "08-you-tab-profile-history-library-chips",
                                        "09-sort-bottom-sheet-checked", "10-settings-icon-list", "11-general-switches-on-off")
SUBS, CHIP, OVERFLOW, WATCH, PLAYER, MINI = ("13-subscriptions-avatars-chips", "14-chip-selected-video-cards-preview",
                                             "15-video-overflow-menu", "16-watch-page-actions-comments-teaser",
                                             "17-player-controls-overlay-scrubber", "18-floating-mini-player")
FEED_D, FEED_L = "06-home-scrolled-ad-buttons-shorts-grid", "06-home-feed-video-cards"
APPEAR_D, APPEAR_L = "12-appearance-choice-list-not-changed", "12-appearance-choice-list"

# id: (capture, op, args, note), or {"dark": (capture, op, args), "light": (capture, op, args), "note": note}
# when the two themes need different boxes. Captures without a theme prefix are read in both themes when
# the file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            (SETTINGS, "fill", (600, 1000, 100, 100), "Settings page background"),
    "bg.home":            (HOME, "fill", (300, 1030, 200, 20), "Home feed background between the ad and the Shorts shelf (light: the ad card)"),
    "bg.sheet":           (SORT, "fill", (500, 1500, 200, 50), "Sort bottom sheet"),
    "sheet.grabber":      (SORT, "fill", (385, 1366, 40, 6), "Grabber at the top of the sort sheet"),
    "scrim.ref":          {"dark": (YOU, "fill", (70, 485, 12, 12)), "light": (YOU, "fill", (600, 600, 50, 50)),
                           "note": "You tab undimmed (dark: the white View channel pill; light: the page)"},
    "scrim.dim":          {"dark": (SORT, "fill", (70, 485, 12, 12)), "light": (SORT, "fill", (600, 600, 50, 50)),
                           "note": "The same point under the sort sheet's scrim"},
    "surface.chip":       (SUBS, "fill", (200, 520, 10, 10), "Filter chip, unselected ('Today')"),
    "surface.chipSelected": (SUBS, "fill", (104, 518, 14, 12), "Filter chip, selected ('All')"),
    "surface.search":     (SEARCH, "fill", (400, 212, 100, 10), "Search field"),
    "surface.menu":       {"dark": (OVERFLOW, "fill", (600, 1450, 40, 30)), "light": (OVERFLOW, "fill", (400, 600, 100, 10)),
                           "note": "Video overflow menu"},
    "surface.adCard":     {"dark": (HOME, "fill", (60, 850, 10, 10)), "light": (HOME, "fill", (600, 880, 100, 20)),
                           "note": "Ad card behind the ad's text and buttons (tinted from the ad in dark)"},
    "surface.tabBar":     (YOU, "fill", (400, 1720, 30, 20), "Tab bar, between Shorts and the Create button (material over content)"),
    "surface.createButton": (YOU, "fill", (372, 1660, 12, 12), "Round Create (+) button in the tab bar"),
    "surface.outlined":   (YOU, "fill", (450, 470, 100, 10), "Get Premium outlined button fill"),
    "border.outline":     (YOU, "text", (420, 470, 10, 20), "Get Premium outline (the hairline furthest from the page)"),
    "surface.comments":   ("dark/" + WATCH, "fill", (300, 870, 300, 40), "Comments teaser card on the watch page"),
    "surface.commentField": ("dark/" + WATCH, "fill", (300, 950, 300, 20), "'Comment...' field inside the teaser"),
    "surface.adSheet":    ("dark/" + ADSHEET, "fill", (400, 1580, 100, 10), "My Ad Centre sheet body"),
    "surface.adSheetHeader": (ADSHEET, "fill", (400, 770, 100, 10), "My Ad Centre sheet header row"),
    "border.accordion":   ("dark/" + ADSHEET, "text", (44, 1130, 8, 20), "Accordion outline in My Ad Centre"),
    "surface.safetyCard": ("dark/" + ADSHEET, "fill", (400, 1700, 100, 10), "Privacy card at the bottom of My Ad Centre"),
    "overlay.duration":   ("dark/" + CHIP, "fill", (689, 942, 8, 6), "Duration badge over a white thumbnail area"),
    "overlay.durationRef": ("dark/" + CHIP, "fill", (676, 950, 6, 14), "The white thumbnail beside the duration badge"),
    "surface.subscribe":  ("dark/" + SHORTS, "fill", (370, 1470, 20, 10), "Subscribe pill over a Short"),
    "surface.upsellButton": ("dark/" + UPSELL, "fill", (150, 1380, 30, 10), "'1 month free' button on the Premium interstitial"),
    "button.largeLabel":  ("dark/" + UPSELL, "text", (300, 1360, 210, 45), "'1 month free' label"),
    # ---------------------------------------------------------------- text
    "text.title":         {"dark": (CHIP, "text", (130, 1015, 530, 45)), "light": (CHIP, "text", (128, 1005, 520, 45)),
                           "note": "Video title under a feed card"},
    "text.meta":          {"dark": (CHIP, "text", (130, 1062, 360, 38)), "light": (CHIP, "text", (128, 1095, 360, 45)),
                           "note": "Channel, views and age under a video title"},
    "text.settingsRow":   (SETTINGS, "text", (128, 715, 270, 40), "Settings row label ('Time management')"),
    "text.sectionHeader": (SETTINGS, "text", (52, 330, 145, 40), "Settings section header ('Account')"),
    "text.helper":        (GENERAL, "text", (50, 485, 560, 65), "Helper text under a General row"),
    "text.rowValue":      (GENERAL, "text", (548, 322, 215, 38), "Row value on the right ('Use device theme')"),
    "text.searchRow":     (SEARCH, "text", (145, 300, 75, 35), "Search history row ('asmr')"),
    "text.placeholder":   (SEARCH, "text", (135, 195, 235, 40), "Search field placeholder ('Search YouTube')"),
    "text.suggestionSub": (TYPED, "text", (145, 1220, 155, 32), "Second line of a suggestion ('Thriller series')"),
    "text.chip":          (SUBS, "text", (165, 490, 80, 35), "Unselected chip label ('Today')"),
    "text.chipSelected":  (SUBS, "text", (64, 490, 40, 35, "inverse"), "Selected chip label ('All')"),
    "text.tab":           (YOU, "text", (60, 1662, 62, 26), "Tab bar label ('Home')"),
    "text.channelName":   (SUBS, "text", (40, 420, 110, 30), "Channel name under a subscription avatar"),
    "text.handle":        (YOU, "text", (225, 380, 145, 30), "The owner's handle under their name"),
    "text.menuItem":      {"dark": (OVERFLOW, "text", (288, 640, 360, 40)), "light": (OVERFLOW, "text", (288, 225, 360, 40)),
                           "note": "Overflow menu item ('Play on a different device')"},
    "text.link":          (SUBS, "text", (730, 318, 40, 32), "'All' link at the end of the subscriptions row"),
    "text.linkSheet":     ("dark/" + ADSHEET, "text", (145, 1655, 155, 40), "'Safety Centre' link in My Ad Centre"),
    # ---------------------------------------------------------------- accent, brand and controls
    "accent.unreadDot":   (SUBS, "fill", (132, 370, 6, 6), "Blue new-content dot on a subscription avatar"),
    "brand.red":          (YOU, "fill", (58, 825, 12, 2),
 "Red watch-progress bar along the bottom of a History thumbnail"),
    "brand.badge":        ("dark/" + HOME, "fill", (573, 1618, 10, 8), "Red dot on the Subscriptions tab icon"),
    "button.filled":      (HOME, "fill", (450, 950, 40, 10), "Ad call to action, filled (Install / Shop now)"),
    "button.filledLabel": {"dark": (HOME, "text", (550, 912, 90, 42, "inverse")), "light": (HOME, "text", (525, 952, 135, 42, "inverse")),
                           "note": "Filled button label"},
    "button.tonal":       (HOME, "fill", (100, 950, 40, 10), "Ad Watch button, tonal (tinted from the ad in dark)"),
    "button.tonalLabel":  {"dark": (HOME, "text", (178, 912, 85, 42)), "light": (HOME, "text", (178, 952, 85, 42)),
                           "note": "Tonal button label ('Watch')"},
    "button.pill":        (YOU, "fill", (70, 485, 12, 12), "View channel pill, filled"),
    "button.pillLabel":   (YOU, "text", (145, 480, 155, 35, "inverse"), "View channel label"),
    "switch.offTrack":    (GENERAL, "fill", (740, 437, 10, 6), "Switch off, track"),
    "switch.offThumb":    (GENERAL, "fill", (710, 434, 8, 8), "Switch off, thumb"),
    "switch.onTrack":     (GENERAL, "fill", (708, 851, 10, 6), "Switch on, track"),
    "switch.onThumb":     (GENERAL, "fill", (742, 850, 8, 8), "Switch on, thumb"),
    "focus.caret":        (TYPED, "fill", (232, 200, 2, 30), "Text caret in the focused search field (two pixel columns)"),
    "icon.check":         {"dark": (APPEAR_D, "text", (700, 400, 45, 35)), "light": (APPEAR_L, "text", (700, 580, 45, 35)),
                           "note": "Tick on the chosen appearance (dark: Use device theme; light: Light theme)"},
    # ---------------------------------------------------------------- sizes
    "size.chip":          (SUBS, "bbox", ((200, 520), (135, 460, 150, 100), 10), "Filter chip ('Today')"),
    "size.search":        (SEARCH, "bbox", ((400, 215), (100, 170, 620, 100), 6), "Search field"),
    "size.buttonFilled":  (HOME, "bbox", ((450, 950), (400, 870, 400, 160), 8), "Ad call-to-action button"),
    "size.pill":          (YOU, "bbox", ((150, 495), (40, 450, 380, 100), 8), "View channel pill"),
    "size.sheet":         (SORT, "bbox", ((500, 1500), (25, 1345, 762, 360), 3), "Sort bottom sheet"),
    "size.menu.w":        {"dark": (OVERFLOW, "find", ("row", 1450, 100, 790, (40, 40, 40), 2)),
                           "light": (OVERFLOW, "find", ("row", 600, 190, 790, (255, 255, 255), 0)), "note": "Overflow menu, positions of its fill along a row"},
    "size.menu.h":        {"dark": (OVERFLOW, "find", ("col", 600, 540, 1560, (40, 40, 40), 2)),
                           "light": (OVERFLOW, "find", ("col", 700, 160, 1040, (255, 255, 255), 1)), "note": "Overflow menu, positions of its fill down a column"},
    "size.switch":        (GENERAL, "bbox", ((740, 437), (680, 400, 110, 80), 12), "Switch track and the thumb's edge (its width)"),
    "size.switchTrack.h": (GENERAL, "extent", ("col", 752, 410, 470, (752, 410), 20), "Switch track height, right of the thumb"),
    "size.switchThumb":   {"dark": (GENERAL, "bbox", ((712, 437), (680, 400, 110, 80), 12)),
                           "light": (GENERAL, "bbox", ((712, 437), (680, 400, 110, 80), 3)), "note": "Switch thumb"},
    "size.createButton":  {"dark": (YOU, "extent", ("row", 1648, 345, 470, (345, 1648), 14)),
                           "light": (YOU, "extent", ("row", 1648, 345, 470, (345, 1648), 6)), "note": "Create (+) button width"},
    "size.avatarSub":     (SUBS, "extent", ("row", 333, 320, 450, (316, 333), 25), "Subscription avatar (a flat light-blue channel icon)"),
    "size.avatarProfile": ("dark/" + YOU, "extent", ("row", 360, 30, 210, (36, 360), 20), "The owner's avatar on the You tab"),
    "size.avatarChannel": ("dark/" + CHIP, "extent", ("row", 1052, 30, 125, (34, 1052), 20), "Channel avatar beside a video title"),
    "size.comments":      ("dark/" + WATCH, "bbox", ((300, 870), (20, 840, 772, 190), 4), "Comments teaser card"),
    "size.commentField":  ("dark/" + WATCH, "bbox", ((300, 960), (120, 930, 650, 70), 4), "'Comment...' field"),
    "size.upsellButton":  ("dark/" + UPSELL, "bbox", ((150, 1380), (60, 1300, 700, 170), 6), "'1 month free' button"),
    "size.subscribe":     ("dark/" + SHORTS, "bbox", ((370, 1470), (340, 1430, 220, 100), 10), "Subscribe pill on a Short"),
    "size.accordion":     ("dark/" + ADSHEET, "find", ("col", 60, 1040, 1420, (72, 72, 72), 12), "Accordion and Send feedback outlines down x = 60"),
    "rows.settings":      (SETTINGS, "lines", (128, 400, 160, 1700), "First letters of the settings rows (the pitch is the row height)"),
    "rows.search":        (SEARCH, "lines", (50, 270, 100, 1690), "History icons down the search list (the pitch is the row height)"),
    "rows.tabBar":        (YOU, "find", ("col", 300, 1590, 1764, None, 0), "Edges down the tab bar at x = 300 (its top hairline)"),
    "border.tabBar":      (YOU, "fill", (300, 1600, 40, 2), "Hairline along the top of the tab bar"),
    # ---------------------------------------------------------------- radii
    "radius.chip":        (SUBS, "diag", (200, 480, 141, 520), "Filter chip"),
    "radius.sheet":       (SORT, "diag", (500, 1360, 40, 1500), "Sort sheet top corner"),
    "radius.menu":        ("dark/" + OVERFLOW, "diag", (600, 590, 166, 900), "Overflow menu"),
    "radius.search":      (SEARCH, "diag", (400, 190, 120, 215), "Search field (capsule)"),
    "radius.comments":    ("dark/" + WATCH, "diag", (300, 865, 48, 900), "Comments teaser card"),
    "radius.buttonFilled": {"dark": (HOME, "diag", (600, 905, 420, 950)), "light": (HOME, "diag", (600, 945, 420, 990)),
                           "note": "Ad call to action (capsule)"},
    "radius.thumbnail":   ("dark/" + YOU, "corner", (48, 667, (40, 660), 12), "History thumbnail, top-left corner"),
    "radius.shortsCard":  ("dark/" + FEED_D, "corner", (42, 943, (30, 930), 12), "Shorts shelf card, top-left corner"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.navTitle":      ("dark/" + SETTINGS, "cap", (121, 195, 145, 250), "'S' of the nav title 'Settings'"),
    "type.sheetTitle":    ("dark/" + ADSHEET, "cap", (122, 760, 160, 810), "'M' of 'My Ad Centre'"),
    "type.sectionTitle":  ("dark/" + YOU, "cap", (50, 590, 75, 640), "'H' of the 'History' shelf title"),
    "type.sectionHeader": ("dark/" + SETTINGS, "cap", (53, 330, 80, 375), "'A' of the 'Account' section header"),
    "type.videoTitle":    ("dark/" + CHIP, "cap", (130, 1015, 160, 1060), "'H' of a video title"),
    "type.meta":          ("dark/" + CHIP, "cap", (130, 1065, 152, 1100), "'Y' of 'Y Combinator'"),
    "type.settingsRow":   ("dark/" + SETTINGS, "cap", (128, 715, 152, 760), "'T' of 'Time management'"),
    "type.menuItem":      ("dark/" + OVERFLOW, "cap", (288, 640, 310, 685), "'P' of 'Play on a different device'"),
    "type.searchRow":     ("dark/" + TYPED, "cap", (145, 1172, 172, 1215), "'D' of 'Designated Survivor'"),
    "type.suggestionSub": ("dark/" + TYPED, "cap", (145, 1218, 162, 1250), "'T' of 'Thriller series'"),
    "type.chip":          ("dark/" + SUBS, "cap", (165, 488, 190, 530), "'T' of the 'Today' chip"),
    "type.button":        ("dark/" + HOME, "cap", (178, 915, 218, 955), "'W' of 'Watch'"),
    "type.helper":        ("dark/" + GENERAL, "cap", (50, 485, 70, 520), "'E' of helper text"),
    "type.tab":           ("dark/" + YOU, "cap", (68, 1662, 84, 1690), "'H' of the 'Home' tab label"),
    "type.channelName":   ("dark/" + SUBS, "cap", (43, 418, 66, 450), "'M' of a channel name under an avatar"),
    "type.display":       ("dark/" + UPSELL, "cap", (265, 745, 305, 805), "'P' of 'Premium' on the interstitial"),
    "type.duration":      ("dark/" + CHIP, "cap", (702, 940, 720, 973), "First digit of a duration badge"),
    "type.subscribe":     ("dark/" + SHORTS, "cap", (385, 1462, 405, 1505), "'S' of 'Subscribe'"),
    "lines.helper":       ("dark/" + GENERAL, "lines", (50, 675, 670, 775), "Three-line helper text (Restricted Mode)"),
    "lines.videoTitle":   ("dark/" + WATCH, "lines", (130, 1515, 680, 1600), "Two-line video title on the watch page"),
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


def lacking(readings):
    """The reading ids missing a theme they need, sorted."""
    # A reading without a theme prefix (or a box per theme) is read in each theme it names; a theme
    # missing for one means a capture is absent.
    need = lambda e: ({t for t in ("dark", "light") if t in e} if isinstance(e, dict)
                      else {e[0].split("/")[0]} if "/" in e[0] else {"dark", "light"})
    return sorted(rid for rid, e in R.items() if set(readings.get(rid, {})) != need(e))


if __name__ == "__main__":
    readings = run(sys.argv[1] if len(sys.argv) > 1 else f"~/.design-systems/{SLUG}/raw-shots")
    short = lacking(readings)
    if short:
        raise SystemExit(f"{len(short)} readings lack a theme they need ({', '.join(short[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
