#!/usr/bin/env python3
"""Read a native app's values out of the full-colour iPhone Mirroring captures (native kit).

    python3 tools/measure.py ~/.design-systems/<slug>/raw-shots

Copied from tools/kit/native (Grok Bot's). Adapt the blocks marked PRODUCT (adapt): NAME and the reading table R,
whose boxes are capture pixels on this product's screens. The ops below are generic.

RAW holds dark/ and light/ sRGB captures (812 x 1780 px, the 390 x 844 pt screen at 2 px per pt,
offset 16, 76 inside the PNG), as written by tools/capture/native/shot.sh. Writes raw/readings.json
(every reading with its file, box, method, value and evidence label) and raw/<slug>-measured.md
(the same as tables). tools/build_tokens.py reads only raw/readings.json.

Each reading is one of:
  fill    the dominant colour of a box and its share of the box            Sampled when share >= 90%
  mean    the average colour of a box and its largest channel spread: small
          tinted fills where stream noise leaves no dominant pixel          Derived
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

NAME = "Luma"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only. A dict entry
# {"dark": (capture, op, args), "light": (capture, op, args), "note": ...} reads a different box per
# theme, for a state that sits in a different place in each (the selected Colour Scheme card).
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
HOME, EVENT, EVMAP, EVABOUT, EVMORE = "01-home-your-events-calendars", "05-event-page-cover-tinted-actions", \
    "06-event-location-map-weather-hosts", "07-event-compact-nav-hosts-about", "08-event-more-menu-destructive-item"
DISC, DISC2, CAT, SEARCH, TYPED = "09-discover-popular-category-chips", "10-discover-cities-featured-calendars", \
    "11-category-page-subscribe-badges", "12-search-focused-filter-chips-recent", "13-search-typed-results-waitlist-badge"
DATES, LOCMENU, NOTIF, CREATE, TICKET = "14-date-range-sheet-calendar-confirm", "15-location-filter-popup-menu", \
    "17-notifications-list-unread-tint", "18-create-event-form-cover-tinted", "19-create-event-ticketing-options-switch-popups"
NAMED, CAL, UNFOLLOW, SETTINGS, APPEAR = "20-create-event-name-typed-confirm-enabled", "21-calendar-page-banner-following-button", \
    "22-following-menu-destructive-unfollow", "23-settings-root-grouped-rows", "24-appearance-scheme-cards-icon-grid"
NOTIFSET, ACCOUNT, PROFILE, CHATS, THREAD = "25-notification-settings-banner-popup-values", "26-account-settings-destructive-row", \
    "27-edit-profile-fields-social-handles", "28-chat-list-unread-dot", "29-chat-thread-image-bubble-composer"
TYPEDMSG, UPCOMING, PAST, FILTER = "30-chat-composer-typed-send-enabled", "31-your-events-segmented-upcoming-soldout-badge", \
    "32-your-events-segmented-past", "33-your-events-filter-menu-icons"
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            (CHATS, "fill", (300, 1200, 200, 100), "Page behind full-bleed lists (Home, Discover, Chat, Your Events); the chat list's empty lower half"),
    "bg.grouped":         (SETTINGS, "fill", (300, 530, 200, 30), "Page behind grouped cards (Settings and its pushed pages), between two cards"),
    "surface.card":       (SETTINGS, "fill", (500, 440, 200, 30), "Grouped card (Settings, Edit Profile row)"),
    "surface.banner":     (NOTIFSET, "fill", (600, 400, 120, 8), "Push Notifications Disabled banner card"),
    "surface.field":      (PROFILE, "fill", (250, 576, 100, 8), "Name field on Edit Profile"),
    "surface.glass":      (CHATS, "fill", (300, 1700, 30, 8), "Tab bar glass over an empty page"),
    "surface.navButton":  (SETTINGS, "fill", (110, 232, 20, 10), "Round glass back button, below the chevron"),
    "surface.search":     (SEARCH, "fill", (500, 236, 200, 10), "Search field (glass capsule)"),
    "surface.chip":       (SEARCH, "fill", (230, 288, 30, 6), "'Near you' filter chip (glass), above its label"),
    "surface.selected":   (CHATS, "fill", (520, 1700, 20, 10), "Selected tab's pill inside the tab bar ('Chat')"),
    "surface.segmentSelected": (UPCOMING, "fill", (300, 178, 30, 6), "Selected segment's pill ('Upcoming'), above its label"),
    "surface.menu":       (FILTER, "fill", (640, 300, 80, 8), "Pull-down menu (glass; takes colour from what is behind)"),
    "surface.popup":      (LOCMENU, "fill", (400, 380, 80, 8), "Pop-up menu (glass), right of 'Near you'"),
    "surface.sheet":      (DATES, "mean", (600, 560, 120, 20), "Date Range sheet (glass over the search page)"),
    "surface.composer":   (THREAD, "fill", (420, 1612, 100, 8), "Message composer field (glass)"),
    "surface.bubble":     (THREAD, "fill", (106, 1516, 8, 20), "Message bubble ('FOOD IS OUT'), left padding"),
    "surface.primary":    (DATES, "fill", (200, 1600, 60, 8), "Confirm button: the theme's ink"),
    "scrim.ref":          (SEARCH, "fill", (500, 236, 100, 8), "Search field, undimmed"),
    "scrim.sheet":        (DATES, "fill", (500, 236, 100, 8), "The same search field behind the Date Range sheet (dimmed)"),
    "border.divider":     (HOME, "fill", (300, 557, 300, 1), "Hairline between event rows (one pixel row)"),
    "border.cardDivider": (SETTINGS, "fill", (300, 669, 300, 1), "Hairline between rows in a grouped card (one pixel row)"),
    "border.selected":    {"dark": (APPEAR, "fill", (130, 438, 40, 1)), "light": (APPEAR, "fill", (380, 438, 40, 1)),
                           "note": "Selected Colour Scheme card outline, top edge (System in dark, Light in light)"},
    "border.control":     {"dark": (APPEAR, "fill", (380, 438, 40, 1)), "light": (APPEAR, "fill", (130, 438, 40, 1)),
                           "note": "Unselected Colour Scheme card outline, top edge"},
    "border.chip":        (DISC, "fill", (120, 1217, 60, 1), "Category chip outline, top edge (one pixel row)"),
    # ---------------------------------------------------------------- text
    "text.primary":       (HOME, "text", (280, 425, 280, 40), "Event row title ('Fri/Sat Gamenight')"),
    "text.secondary":     (HOME, "text", (282, 485, 330, 34), "Event row meta line ('Yesterday, 19:00 GMT-7')"),
    "text.host":          (HOME, "text", (282, 372, 130, 34), "Event row host line (a host's name)"),
    "text.tertiary":      (UPCOMING, "text", (150, 290, 160, 34), "Weekday after a date section ('/ Saturday')"),
    "text.sectionHeader": (SETTINGS, "text", (88, 816, 200, 36), "Grouped section header ('Preferences')"),
    "text.placeholder":   (PROFILE, "text", (88, 790, 450, 36), "Bio text area placeholder"),
    "text.time":          (CHATS, "text", (636, 312, 92, 30), "Chat row date ('12 Oct')"),
    "text.navTitle":      (SETTINGS, "text", (340, 196, 140, 36), "Nav title ('Settings')"),
    "text.link":          (NOTIFSET, "text", (160, 464, 200, 34), "'Open Settings' link in the banner"),
    "text.linkDate":      (DATES, "text", (98, 718, 72, 34), "'Now' in the Date Range sheet"),
    "text.onPrimary":     (DATES, "text", (346, 1620, 120, 36, "inverse"), "'Confirm' label on the ink button"),
    "text.onAccent":      (CAT, "text", (82, 776, 136, 32, "light"), "'Subscribe' label on the purple button"),
    "text.tab":           (CHATS, "text", (364, 1676, 84, 24), "Unselected tab label ('Discover')"),
    "text.tabSelected":   (CHATS, "text", (550, 1676, 60, 24), "Selected tab label ('Chat')"),
    "text.disabled":      (DATES, "text", (130, 1205, 40, 30), "A past day in the Date Range calendar ('18'), greyed"),
    "text.danger":        (ACCOUNT, "text", (88, 1312, 240, 34), "'Delete Account' row"),
    "text.dangerMenu":    (UNFOLLOW, "text", (408, 564, 140, 34), "'Unfollow' in the Following menu"),
    # ---------------------------------------------------------------- accent and status
    "accent.subtle":      (HOME, "mean", (110, 510, 50, 4), "'Invited' badge fill, above its label"),
    "accent.fg":          (HOME, "text", (98, 512, 76, 26), "'Invited' badge label"),
    "accent.emphasis":    (CAT, "fill", (64, 786, 12, 14), "'Subscribe' button, left of its label"),
    "accent.tile":        (CAT, "mean", (72, 340, 8, 10), "Category icon disc (Family), inside its left edge"),
    "success.subtle":     (HOME, "mean", (700, 375, 40, 4), "Price pill fill ('US$15'), above its label"),
    "success.fg":         (HOME, "text", (676, 376, 76, 30), "Price pill label"),
    "danger.subtle":      (UPCOMING, "mean", (670, 1089, 60, 4), "'Sold Out' pill fill, above its label"),
    "danger.fg":          (UPCOMING, "text", (656, 1088, 90, 30), "'Sold Out' label"),
    "danger.badge":       (HOME, "mean", (600, 1628, 6, 8), "Unread count badge on the Chat tab, left of the '1'"),
    "danger.dot":         (CHATS, "mean", (742, 374, 4, 4), "Unread dot in a chat row"),
    "warning.subtle":     (CAT, "mean", (620, 1363, 100, 4), "'Near Capacity' pill fill, above its label"),
    "warning.fg":         (CAT, "text", (600, 1362, 150, 32), "'Near Capacity' label"),
    "info.subtle":        (TYPED, "mean", (630, 441, 100, 4), "'Waitlist Open' pill fill, above its label"),
    "info.fg":            (TYPED, "text", (604, 440, 146, 32), "'Waitlist Open' label"),
    "info.emphasis":      (TYPEDMSG, "mean", (712, 1652, 12, 8), "Send button, below its arrow"),
    "focus.caret":        (TYPED, "fill", (343, 200, 2, 30), "Text caret after 'design' in the search field, a two-pixel column"),
    "switch.thumb":       (TICKET, "fill", (622, 1218, 10, 10), "Switch thumb (off) on the Create Event sheet"),
    "switch.off":         (TICKET, "mean", (700, 1218, 10, 12), "Switch off track (over the cover-tinted sheet)"),
    # ---------------------------------------------------------------- cover-tinted pages (one cover each)
    "tint.eventPage":     (EVENT, "mean", (560, 1230, 160, 20), "Event page background beside the host line (TEDxSingapore cover)"),
    "tint.eventButton":   (EVENT, "mean", (300, 1420, 24, 40), "Contact button on the event page, left padding"),
    "tint.createPage":    (CREATE, "mean", (600, 1540, 100, 10), "Create Event sheet background between sections (random cover)"),
    "tint.createField":   (CREATE, "mean", (650, 896, 80, 10), "Event Name field on the Create Event sheet"),
    # ---------------------------------------------------------------- sizes
    "size.tabBar.h":      ("dark/" + CHATS, "extent", ("col", 400, 1560, 1770, (400, 1570), 12), "Tab bar height"),
    "size.tabBar.w":      ("dark/" + CHATS, "extent", ("row", 1661, 100, 720, (110, 1661), 12), "Tab bar width"),
    "size.tabSelected":   ("dark/" + CHATS, "extent", ("row", 1661, 440, 676, (460, 1661), 10), "Selected tab pill width"),
    "size.navButton.w":   ("dark/" + SETTINGS, "extent", ("row", 214, 30, 200, (40, 214), 12), "Round glass back button, width"),
    "size.navButton.h":   ("dark/" + SETTINGS, "extent", ("col", 100, 150, 270, (100, 160), 12), "Round glass back button, height"),
    "size.headerButtons.w": ("dark/" + HOME, "extent", ("row", 214, 540, 780, (550, 214), 12), "Glass pair of header buttons (+ and bell), width"),
    "size.search.h":      ("dark/" + SEARCH, "extent", ("col", 500, 150, 268, (500, 155), 12), "Search field height"),
    "size.chip.h":        ("dark/" + SEARCH, "extent", ("col", 230, 265, 345, (230, 268), 12), "Filter chip height ('Near you')"),
    "size.chip.w":        ("dark/" + SEARCH, "extent", ("row", 288, 40, 280, (45, 288), 12), "Filter chip width ('Near you')"),
    "size.categoryChip.h": (DISC, "extent", ("col", 150, 1205, 1310, (150, 1210), 8), "Outlined category chip height ('Family')"),
    "size.segmented.h":   ("dark/" + UPCOMING, "extent", ("col", 300, 150, 280, (300, 155), 12), "Segmented control height"),
    "size.segmented.w":   ("dark/" + UPCOMING, "extent", ("row", 214, 150, 640, (160, 214), 12), "Segmented control width"),
    "size.segmentPill.w": ("dark/" + UPCOMING, "extent", ("row", 180, 216, 520, (215, 180), 6), "Selected segment pill width ('Upcoming')"),
    "size.segmentPill.h": ("dark/" + UPCOMING, "extent", ("col", 300, 170, 258, (300, 170), 6), "Selected segment pill height"),
    "size.thumb":         (HOME, "extent", ("row", 450, 30, 230, (40, 450), 12), "Event cover thumbnail in a row, width"),
    "size.badge":         (HOME, "bbox", ((88, 520), (70, 495, 140, 60), 6), "'Invited' badge on a thumbnail"),
    "size.pill":          (HOME, "bbox", ((668, 390), (640, 360, 130, 60), 4), "Price pill ('US$15')"),
    "size.primary":       (DATES, "bbox", ((200, 1600), (40, 1560, 740, 150), 4), "Confirm button"),
    "size.subscribe.w":   (CAT, "extent", ("row", 794, 30, 250, (35, 794), 12), "Subscribe button width"),
    "size.subscribe.h":   (CAT, "extent", ("col", 150, 740, 840, (150, 745), 12), "Subscribe button height"),
    "size.eventAction":   (EVENT, "bbox", ((70, 1420), (40, 1380, 280, 150), 4), "Register button on the event page"),
    "size.field":         (PROFILE, "bbox", ((250, 580), (40, 540, 740, 140), 2), "Name field"),
    "size.switch":        (TICKET, "bbox", ((700, 1224), (580, 1180, 170, 90), 10), "Switch track"),
    "size.switchThumb":   (TICKET, "bbox", ((626, 1224), (590, 1185, 100, 80), 6), "Switch thumb"),
    "size.avatarHeader":  (HOME, "extent", ("row", 214, 30, 150, (40, 214), 14), "Account avatar at the top left of a tab root"),
    "size.send":          (TYPEDMSG, "bbox", ((712, 1656), (690, 1600, 90, 90), 30), "Send button"),
    "size.composer.h":    ("dark/" + THREAD, "extent", ("col", 420, 1570, 1720, (420, 1580), 10), "Composer field height"),
    "size.calendarTile":  ("light/" + HOME, "extent", ("row", 1300, 225, 400, (228, 1300), 12), "Calendar tile in Your Calendars"),
    "size.settingsIcon":  (SETTINGS, "extent", ("row", 622, 70, 170, (75, 622), 30), "Coloured icon tile in a Settings row (Account Settings)"),
    "size.tabBadge":      (HOME, "bbox", ((600, 1630), (580, 1600, 70, 60), 40), "Unread count badge on a tab"),
    "size.dot":           (CHATS, "bbox", ((744, 376), (730, 360, 30, 30), 40), "Unread dot in a chat row"),
    "size.statusPill.h":  (UPCOMING, "extent", ("col", 700, 1070, 1130, (700, 1072), 3), "'Sold Out' pill height"),
    "size.icon.meta":     (HOME, "extent", ("row", 502, 236, 276, (238, 502), 30), "Clock icon before an event meta line, width"),
    "size.icon.tab":      (CHATS, "extent", ("row", 1646, 372, 440, (374, 1646), 30), "Discover tab icon, width"),
    "rows.settings":      (SETTINGS, "find", ("col", 600, 280, 1170, None, 0), "Edges down the first three Settings cards"),
    "rows.notifSettings": (NOTIFSET, "find", ("col", 500, 690, 1180, None, 0), "Edges down the Events You Attend card"),
    "rows.events":        (UPCOMING, "find", ("col", 500, 360, 1400, None, 0), "Edges down the Your Events list"),
    # ---------------------------------------------------------------- radii
    "radius.card":        (SETTINGS, "diag", (400, 300, 70, 470), "Settings card"),
    "radius.banner":      (NOTIFSET, "diag", (400, 300, 70, 440), "Push Notifications Disabled banner"),
    "radius.textArea":    (PROFILE, "diag", (650, 780, 70, 900), "Bio text area"),
    "radius.thumb":       (UPCOMING, "diag", (150, 1420, 70, 1480), "Event thumbnail with a flat cream cover (Founders House)"),
    "radius.eventAction": (EVENT, "diag", (160, 1410, 70, 1470), "Register button on the event page"),
    "radius.calendarTile": ("light/" + HOME, "diag", (330, 1240, 245, 1300), "Calendar tile in Your Calendars"),
    "radius.settingsIcon": (SETTINGS, "diag", (108, 598, 92, 640), "Coloured icon tile in a Settings row"),
    "radius.formGroup":   (CREATE, "diag", (400, 970, 70, 1050), "Start and End group on the Create Event sheet"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.largeTitle":    ("dark/" + DISC, "cap", (158, 190, 184, 240), "'D' of a tab root title ('Discover')"),
    "type.title1":        ("dark/" + CAT, "cap", (54, 455, 80, 515), "'F' of a category title ('Family')"),
    "type.eventTitle":    ("dark/" + EVENT, "cap", (54, 1080, 74, 1135), "'T' of an event page title"),
    "type.title2":        ("dark/" + HOME, "cap", (56, 285, 82, 330), "'Y' of a section title ('Your Events')"),
    "type.headline":      ("dark/" + HOME, "cap", (238, 890, 268, 935), "'M' of an event row title ('Mahjong')"),
    "type.navTitle":      ("dark/" + NOTIF, "cap", (304, 192, 326, 238), "'N' of a nav title ('Notifications')"),
    "type.body":          ("dark/" + SETTINGS, "cap", (166, 598, 190, 645), "'A' of a Settings row ('Account Settings')"),
    "type.meta":          ("dark/" + HOME, "cap", (282, 482, 302, 524), "'Y' of an event meta line ('Yesterday')"),
    "type.host":          ("dark/" + UPCOMING, "cap", (280, 1086, 296, 1118), "'E' of a host line ('Emergent')"),
    "type.sectionHeader": ("dark/" + SETTINGS, "cap", (86, 815, 106, 855), "'P' of a grouped section header ('Preferences')"),
    "type.dateSection":   ("dark/" + UPCOMING, "cap", (54, 290, 72, 324), "'T' of a date section ('Today')"),
    "type.caption":       ("dark/" + HOME, "cap", (96, 512, 104, 542), "'I' of the 'Invited' badge"),
    "type.pill":          ("dark/" + HOME, "cap", (678, 378, 694, 404), "'U' of a price pill ('US$15')"),
    "type.tab":           ("dark/" + HOME, "cap", (202, 1676, 218, 1700), "'H' of a tab label ('Home')"),
    "type.button":        ("dark/" + EVENT, "cap", (118, 1462, 134, 1488), "'R' of an event action label ('Register')"),
    "type.chatTitle":     ("dark/" + CHATS, "cap", (166, 444, 186, 482), "'P' of a chat row title ('Poker With Friends')"),
    "type.timestamp":     ("dark/" + THREAD, "cap", (288, 712, 302, 738), "'T' of a thread timestamp ('Thu')"),
    "type.aboutHeading":  ("dark/" + EVABOUT, "cap", (54, 1100, 74, 1145), "'T' of the bold opening line of About Event"),
    "type.placeholderLarge": ("dark/" + CREATE, "cap", (86, 850, 106, 895), "'E' of the Event Name placeholder"),
    "type.description":   ("dark/" + CAT, "cap", (54, 605, 72, 637), "'F' of a category description ('From')"),
    "type.footnote":      ("dark/" + ACCOUNT, "cap", (86, 1168, 110, 1194), "'W' of a footnote under a card"),
    "lines.headline":     ("dark/" + HOME, "lines", (240, 890, 560, 1000), "Two-line event row title ('Mahjong After Dark: / Spooky Edition')"),
    "lines.body":         ("dark/" + CAT, "lines", (56, 600, 750, 720), "Three lines of category description"),
    "lines.aboutHeading": ("dark/" + EVABOUT, "lines", (56, 1100, 750, 1260), "Three lines of the bold About Event opening"),
    "lines.notification": ("dark/" + NOTIF, "lines", (152, 355, 640, 480), "Three-line notification text"),
}


def d(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def hexof(p):
    return "#{:02X}{:02X}{:02X}".format(*p[:3])


def op_fill(rows, x, y, w, h):
    colour, share = sample.fill(rows, x, y, w, h)
    return {"value": hexof(colour), "share": round(share, 2),
            "evidence": "Sampled" if share >= 0.9 else "Derived"}


def op_mean(rows, x, y, w, h):
    """The average colour of a box and the largest channel spread inside it. For small tinted fills
    (badges, pills, glass) where the mirroring stream leaves a few levels of noise, so no one pixel
    value dominates."""
    px = sample.region(rows, x, y, w, h)
    mean = tuple(round(sum(p[i] for p in px) / len(px)) for i in range(3))
    spread = max(max(p[i] for p in px) - min(p[i] for p in px) for i in range(3))
    return {"value": hexof(mean), "spread": spread, "evidence": "Derived"}


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
    for rid, entry in R.items():
        if isinstance(entry, dict):   # a different box per theme: {"dark": (capture, op, args), "light": ..., "note"}
            plan = [(t, *entry[t]) for t in ("dark", "light") if t in entry]
            note = entry["note"]
        else:
            cap, op, args, note = entry
            themes = [cap.split("/")[0]] if "/" in cap else ["dark", "light"]
            plan = [(t, cap, op, args) for t in themes]
        for theme, cap, op, args in plan:
            name = cap.split("/")[-1]
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
            extra += f" (mean, spread {r['spread']})" if "spread" in r else ""
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
