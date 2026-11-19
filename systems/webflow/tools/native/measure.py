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

NAME = "Grok Bot"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            ("01-home", "fill", (300, 1150, 200, 20), "Home and chat background"),
    "bg.thread":          ("30-group-chat", "fill", (690, 900, 80, 200), "Chat thread background, right of the bubbles"),
    "bg.sheet":           ("19-account-menu", "fill", (400, 300, 300, 30), "Settings sheet background"),
    "bg.sheetNewBot":     ("03-new-bot", "fill", (100, 450, 100, 50), "Create New Bot sheet background"),
    "bg.detail":          ("13-routines", "fill", (300, 1000, 200, 100), "Pushed detail page background (Routines)"),
    "bg.profile":         ("12-bot-profile", "fill", (300, 1500, 300, 50), "Bot profile background"),
    "surface.card":       ("12-bot-profile", "fill", (330, 1200, 220, 60), "Grouped card (bot profile, Notifications row)"),
    "surface.cardSettings": ("19-account-menu", "fill", (560, 330 + 260, 30, 30), "Grouped card in Settings (Usage row)"),
    "surface.field":      ("03-new-bot", "fill", (80, 860, 150, 15), "Name field"),
    "surface.textArea":   ("dark/23-feedback", "fill", (300, 550, 200, 50), "Feedback text area"),
    "surface.bubble":     ("30-group-chat", "fill", (560, 620, 100, 20), "Bot message bubble (group chat)"),
    "surface.bubbleDirect": ("dark/07-chat-bubbles", "fill", (650, 700, 20, 300), "Bot message bubble (one-to-one chat), right padding"),
    "surface.bubbleDirectLight": ("light/06-chat", "fill", (650, 400, 20, 300), "Bot message bubble (one-to-one chat), right padding"),
    "surface.chip":       ("25-connect-apps", "fill", (320, 695, 10, 10), "Account chip in Connect apps"),
    "surface.pill":       ("12-bot-profile", "fill", (365, 610, 10, 30), "Edit pill on the bot profile"),
    "surface.composer":   ("06-chat", "fill", (470, 1620, 80, 15), "Composer field (glass; centre reading)"),
    "surface.menu":       ("02-plus-menu", "fill", (300, 270, 20, 20), "Menu (glass; picks up colour from what is behind)"),
    "scrim.ref":          ("01-home", "fill", (300, 180, 20, 20), "Home behind the context menu, undimmed"),
    "scrim.context":      ("33-bot-context-menu", "fill", (300, 180, 20, 20), "Home under the context-menu scrim"),
    "scrim.sheet":        ("03-new-bot", "fill", (300, 250, 200, 20), "Home under a sheet"),
        "border.dividerColour": ("12-bot-profile", "fill", (300, 822, 300, 1), "Divider colour (one pixel row)"),
    "border.card":        ("12-bot-profile", "fill", (64, 900, 2, 60), "Card rim, left edge"),
    "surface.ownBubble":  ("dark/37-own-bubble", "fill", (600, 352, 120, 8), "The owner's own message bubble ([Tutor] bot, amber)"),
    "surface.code":       ("dark/36-tutor-chat-mid", "fill", (560, 470, 60, 10), "Code block inside a bot bubble"),
    "text.onOwnBubble":   ("dark/37-own-bubble", "text", (180, 365, 560, 160), "Text on the owner's bubble"),
    "text.code":          ("dark/36-tutor-chat-mid", "text", (100, 395, 120, 30), "Monospace text in a code block"),
    "size.ownBubble":     ("dark/37-own-bubble", "bbox", ((600, 352), (100, 320, 700, 250), 6), "The owner's bubble"),
    "size.code":          ("dark/36-tutor-chat-mid", "bbox", ((560, 470), (60, 360, 680, 170), 4), "Code block"),
    "radius.ownBubble":   ("dark/37-own-bubble", "diag", (600, 360, 180, 450), "The owner's bubble"),
    "radius.code":        ("dark/36-tutor-chat-mid", "diag", (560, 390, 80, 470), "Code block"),
    # ---------------------------------------------------------------- text
    "text.primary":       ("01-home", "text", (181, 1470, 120, 35), "Home row title"),
    "text.body":          ("30-group-chat", "text", (130, 540, 300, 30), "Bubble text"),
    "text.gridLabel":     ("01-home", "text", (77, 540, 140, 35), "Bot name under a home grid avatar"),
    "text.preview":       ("01-home", "text", (181, 1520, 100, 30), "Home row preview line"),
    "text.rowValue":      ("19-account-menu", "text", (624, 575, 50, 35), "Settings row value ('0%')"),
    "text.rowSubtitle":   ("19-account-menu", "text", (87, 980, 350, 30), "Settings row subtitle"),
    "text.timestamp":     ("01-home", "text", (600, 1470, 150, 35), "Home row timestamp"),
    "text.sectionHeader": ("19-account-menu", "text", (85, 1100, 45, 35), "Settings section header ('Bot')"),
    "text.folderCount":   ("01-home", "text", (162, 1200, 30, 35), "Folder count"),
    "text.footnote":      ("12-bot-profile", "text", (103, 1300, 600, 70), "Helper text under a card"),
    "text.fieldLabel":    ("17-edit-bot", "text", (100, 550, 80, 30), "Form field label ('Name')"),
    "text.placeholder":   ("03-new-bot", "text", (260, 880, 290, 45), "Name field placeholder"),
    "text.composerPlaceholder": ("06-chat", "text", (225, 1640, 200, 35), "Composer placeholder"),
    "text.systemTime":    ("06-chat", "text", (310, 1368, 190, 32), "Thread timestamp line"),
    "text.systemLine":    ("06-chat", "text", (225, 1445, 130, 30), "Thread system line ('Messaged ...')"),
    "text.senderLabel":   ("30-group-chat", "text", (127, 470, 150, 30), "Sender label above a group bubble"),
    "text.disabled":      ("25-connect-apps", "text", (640, 688, 90, 30), "'Added' label on a disabled button"),
    "text.destructive":   ("11-chat-more-menu", "text", (410, 465, 100, 40), "'Delete' menu item"),
    "text.link":          ("30-group-chat", "text", (170, 1075, 170, 40), "Inline link in a bubble"),
    "text.success":       ("25-connect-apps", "text", (290, 688, 30, 25), "Tick in a connected-account chip"),
    "text.onPill":        ("01-home", "text", (365, 1490, 120, 35, "light"), "Label on the blue unread pill"),
    # ---------------------------------------------------------------- accent and controls
    "accent.dot":         ("01-home", "fill", (488, 550, 10, 10), "Unread dot"),
    "accent.pill":        ("01-home", "fill", (305, 1500, 15, 15), "'3 unread' pill"),
    "accent.caret":       ("05-new-bot-typed", "fill", (447, 888, 1, 25), "Text caret, one pixel column"),
    "button.primary":     ("05-new-bot-typed", "fill", (150, 1620, 150, 15), "Create, enabled"),
    "button.primaryLabel": ("05-new-bot-typed", "text", (355, 1630, 100, 40, "inverse"), "Create label, enabled"),
    "button.disabled":    ("03-new-bot", "fill", (150, 1620, 150, 15), "Create, disabled (glass; dominant pixel)"),
    "button.disabledLabel": ("03-new-bot", "text", (355, 1630, 100, 40, "inverse"), "Create label, disabled"),
    "button.secondary":   ("25-connect-apps", "fill", (622, 690, 12, 20), "'Added' button fill"),
    "button.secondaryLabel": ("32-connect-apps-add", "text", (675, 885, 70, 50), "'Add' label"),
    "button.send":        ("10-composer-typed", "fill", (650, 1640, 15, 15), "Send button"),
    "button.sendGlyph":   ("10-composer-typed", "text", (665, 1630, 30, 50, "inverse"), "Send arrow"),
    "button.voice":       ("06-chat", "fill", (650, 1640, 15, 15), "Voice button"),
    "switch.onBot":       ("12-bot-profile", "fill", (600, 1215, 20, 15), "Switch on, Bot color accent (purple bot)"),
    "switch.onNeutral":   ("19-account-menu", "fill", (608, 1200, 20, 15), "Switch on in Settings"),
    "switch.off":         ("20-settings-mid", "fill", (690, 1310, 25, 15), "Switch off (Notifications)"),
    "switch.thumb":       ("12-bot-profile", "fill", (680, 1222, 10, 10), "Switch thumb"),
    "badge.star":         ("01-home", "fill", (462, 486, 3, 3), "Star badge on a pinned bot"),
    # ---------------------------------------------------------------- avatar palette (Create New Bot)
    **{f"palette.{i + 1}": ("03-new-bot", "fill", (x - 6, y - 6, 12, 12), f"Avatar colour swatch {i + 1}")
       for i, (x, y) in enumerate([(148, 1424), (251, 1424), (354, 1424), (457, 1424), (560, 1424), (663, 1424),
                                   (200, 1509), (303, 1509), (406, 1509), (509, 1509), (612, 1509)])},
    "avatar.eye":         ("01-home", "fill", (414, 413, 4, 8), "Avatar eye (a cut-out showing the page)"),
    # ---------------------------------------------------------------- sizes
    "size.navButton.w":   ("13-routines", "extent", ("row", 226, 20, 200, (250, 160), 12), "Round glass back button, width"),
    "size.navButton.h":   ("13-routines", "extent", ("col", 96, 150, 300, (250, 160), 12), "Round glass back button, height"),
    "size.composer.h":    ("dark/06-chat", "extent", ("col", 470, 1570, 1764, (470, 1570), 12), "Composer field height"),
    "size.composerPlus.w": ("dark/06-chat", "extent", ("row", 1655, 20, 185, (30, 1580), 12), "Composer + button width"),
    "size.searchBar.h":   ("dark/01-home", "extent", ("col", 465, 1570, 1764, (465, 1580), 14), "Home search bar height"),
    "size.menu.w":        ("dark/02-plus-menu", "extent", ("row", 280, 220, 812, (240, 280), 30), "Menu width"),
    "size.menu.h":        ("dark/02-plus-menu", "extent", ("col", 560, 150, 420, (560, 160), 30), "Menu height, two items"),
    "size.switch":        ("12-bot-profile", "bbox", ((600, 1215), (560, 1180, 220, 100), 10), "Switch track"),
    "size.switchThumb":   ("dark/12-bot-profile", "bbox", ((680, 1222), (600, 1195, 130, 70), 6), "Switch thumb"),
    "size.button":        ("dark/05-new-bot-typed", "bbox", ((150, 1625), (40, 1580, 740, 140), 8), "Full-width primary button"),
    "size.field":         ("03-new-bot", "bbox", ((80, 860), (40, 830, 740, 140), 3), "Single-line field"),
    "size.textArea":      ("dark/23-feedback", "bbox", ((300, 550), (30, 340, 760, 400), 3), "Text area"),
    "size.pill":          ("12-bot-profile", "bbox", ((365, 610), (330, 580, 160, 110), 4), "Edit pill"),
    "size.chip":          ("25-connect-apps", "bbox", ((320, 695), (160, 668, 190, 70), 3), "Account chip"),
    "size.secondaryButton": ("25-connect-apps", "bbox", ((622, 690), (600, 650, 170, 100), 3), "'Added' button"),
    "size.sendButton.w":  ("dark/10-composer-typed", "extent", ("row", 1655, 626, 734, (610, 1655), 40), "Send button width"),
    "size.sendButton.h":  ("dark/10-composer-typed", "extent", ("col", 678, 1612, 1720, (678, 1614), 40), "Send button height"),
    "size.avatarGrid":    ("01-home", "bbox", ((390, 380), (290, 320, 230, 220), 10), "Home grid avatar (pink bot)"),
    "size.avatarGridB":   ("01-home", "bbox", ((620, 450), (550, 320, 250, 220), 10), "Home grid avatar (orange bot)"),
    "size.swatch":        ("03-new-bot", "bbox", ((251, 1424), (210, 1385, 85, 80), 10), "Avatar colour swatch"),
    "size.cardSettings":  ("19-account-menu", "bbox", ((560, 590), (20, 340, 780, 320), 3), "Settings card"),
    "size.cardProfile":   ("12-bot-profile", "bbox", ((400, 760), (30, 700, 760, 440), 3), "Bot profile card"),
    "size.bubbleGroup":   ("30-group-chat", "bbox", ((560, 620), (90, 495, 600, 230), 3), "Group bubble"),
    "size.bubbleDirect":  ("dark/07-chat-bubbles", "bbox", ((300, 640), (30, 470, 700, 190), 3), "One-to-one bot bubble"),
    "rows.profile":       ("12-bot-profile", "find", ("col", 400, 700, 1300, None, 0), "Row edges down the bot profile card"),
    # ---------------------------------------------------------------- radii
    "radius.card":        ("19-account-menu", "diag", (560, 380, 60, 560), "Settings card"),
    "radius.cardProfile": ("12-bot-profile", "diag", (400, 740, 80, 920), "Bot profile card"),
    "radius.field":       ("03-new-bot", "diag", (600, 870, 72, 903), "Name field"),
    "radius.textArea":    ("dark/23-feedback", "diag", (600, 370, 56, 550), "Text area"),
    "radius.bubble":      ("30-group-chat", "diag", (600, 520, 110, 640), "Group bubble, first in a run"),
    "radius.bubbleJoined": ("dark/07-chat-bubbles", "diag", (600, 670, 56, 900), "Bubble whose top follows another bubble"),
    "radius.sheet":       ("03-new-bot", "diag", (500, 300, 45, 600), "Sheet top corner"),
    "radius.menu":        ("dark/02-plus-menu", "diag", (560, 200, 300, 280), "Pull-down menu"),
    "radius.chip":        ("25-connect-apps", "diag", (320, 690, 174, 701), "Chip (capsule)"),
    "radius.secondaryButton": ("25-connect-apps", "diag", (690, 690, 624, 702), "'Added' button (capsule)"),
    "radius.button":      ("05-new-bot-typed", "diag", (300, 1615, 105, 1648), "Create button (capsule)"),
    "radius.composer":    ("dark/06-chat", "diag", (500, 1615, 205, 1656), "Composer field (capsule)"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.fieldText":     ("dark/05-new-bot-typed", "cap", (362, 875, 392, 930), "'T' of typed text in the name field"),
    "type.profileTitle":  ("dark/12-bot-profile", "cap", (405, 525, 430, 570), "'L' of the bot name on its profile"),
    "type.rowTitle":      ("dark/01-home", "cap", (178, 1462, 208, 1512), "'H' of a home row title"),
    "type.settingsRow":   ("dark/19-account-menu", "cap", (84, 565, 112, 620), "'U' of a settings row ('Usage')"),
    "type.navTitle":      ("dark/13-routines", "cap", (333, 200, 362, 255), "'R' of a nav title ('Routines')"),
    "type.sheetTitle":    ("dark/03-new-bot", "cap", (178, 345, 208, 395), "'C' of a sheet title"),
    "type.bubble":        ("dark/07-chat-bubbles", "cap", (72, 495, 90, 540), "'I' of bubble text"),
    "type.button":        ("dark/05-new-bot-typed", "cap", (350, 1620, 383, 1675), "'C' of 'Create'"),
    "type.emptyState":    ("dark/16-coding", "cap", (82, 875, 112, 925), "'C' of an empty-state line"),
    "type.preview":       ("dark/01-home", "cap", (178, 1515, 207, 1558), "'N' of a home row preview"),
    "type.menuItem":      ("dark/02-plus-menu", "cap", (334, 212, 365, 255), "'N' of a menu item"),
    "type.composer":      ("dark/06-chat", "cap", (222, 1630, 258, 1685), "'A' of the composer placeholder"),
    "type.gridLabel":     ("dark/01-home", "cap", (74, 535, 98, 578), "'E' of a home grid label"),
    "type.subtitle":      ("dark/19-account-menu", "cap", (84, 975, 107, 1015), "'T' of a settings row subtitle"),
    "type.sectionHeader": ("dark/19-account-menu", "cap", (82, 1095, 104, 1140), "'B' of a section header"),
    "type.timestamp":     ("dark/01-home", "cap", (596, 1465, 640, 1508), "'W' of a row timestamp"),
    "type.footnote":      ("dark/12-bot-profile", "cap", (98, 1300, 127, 1345), "'G' of helper text"),
    "type.systemLine":    ("dark/06-chat", "cap", (306, 1362, 333, 1402), "'T' of the thread timestamp"),
    "type.senderLabel":   ("dark/30-group-chat", "cap", (224, 468, 240, 500), "'L' of a sender label"),
    "lines.bubble":       ("dark/30-group-chat", "lines", (125, 520, 620, 700), "Text lines in a four-line group bubble"),
    "lines.subtitle":     ("dark/19-account-menu", "lines", (85, 1235, 560, 1300), "Two-line settings row subtitle"),
    "lines.footnote":     ("dark/12-bot-profile", "lines", (100, 1300, 720, 1380), "Two-line helper text"),
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


def at(rows, x, y):
    """rows[y][x], refusing a coordinate off the image: a negative index would
    silently wrap to the far edge and a walk would read the wrong pixels."""
    if not (0 <= y < len(rows) and 0 <= x < len(rows[y])):
        raise ValueError(f"walked off the capture at ({x}, {y}); check the reading's box")
    return rows[y][x]


def op_diag(rows, cx, cyc, cxr, cy):
    f = at(rows, cxr, cy)
    x = cxr
    while d(at(rows, x - 1, cy), f) <= 3:
        x -= 1
    bg = at(rows, x - 5, cy)
    tol = max(2, d(bg, f) // 2)
    while d(at(rows, x - 1, cy), f) <= tol:
        x -= 1
    x0, y = x, cyc
    while d(at(rows, cx, y - 1), f) <= tol:
        y -= 1
    t = 0
    while d(at(rows, x0 + t, y + t), f) > tol:
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
    missing = sorted(rid for rid in R if rid not in readings)
    if missing:   # a light-only gap is fine; a reading with no theme at all means a capture is absent
        raise SystemExit(f"no capture for {len(missing)} readings ({', '.join(missing[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
