#!/usr/bin/env python3
"""Read a native app's values out of the full-colour iPhone Mirroring captures (native kit).

    python3 tools/measure.py ~/.design-systems/<slug>/raw-shots

Copied from the native kit (systems/grokbot). Adapted for Grab: NAME and the reading table R, and
light/ only, since Grab has no dark UI. The ops below are generic.

RAW holds light/ sRGB captures (812 x 1780 px, the 390 x 844 pt screen at 2 px per pt,
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

NAME = "Grab"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# id: (capture, op, args, note). Grab has no dark UI, so every capture is read from light/.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures. No box sits
# inside a region tools/masks.json paints over.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            ("21-cart-empty-state", "fill", (300, 400, 200, 20), "Page background (empty cart)"),
    "bg.section":         ("14-account-cards-list", "fill", (300, 1000, 200, 10), "Grey band between account sections"),
    "bg.tint":            ("14-account-cards-list", "fill", (300, 150, 200, 20), "Mint header behind the account card"),
    "bg.headerHome":      ("01-home-tiles-search", "fill", (30, 160, 8, 8), "Home header, top (a vertical gradient)"),
    "bg.headerHomeEnd":   ("01-home-tiles-search", "fill", (30, 272, 8, 8), "Home header, bottom of the gradient"),
    "bg.headerFood":      ("20-food-home-chips-categories-tabbar", "fill", (300, 150, 20, 20), "Food home header"),
    "bg.promoPeach":      ("22-offer-zone-grid", "fill", (700, 170, 20, 20), "Offer Zone header"),
    "bg.promoCream":      ("23-pickup-promo-interstitial", "fill", (600, 300, 20, 20), "Pickup promo interstitial"),
    "bg.flash":           ("19-food-flash-deals-sheet-timer", "fill", (300, 350, 20, 20), "Flash deals sheet header"),
    "surface.card":       ("01-home-tiles-search", "fill", (600, 770, 100, 20), "Ride to card"),
    "surface.field":      ("17-search-focused-chips-recent-pills", "fill", (300, 330, 20, 20), "Search field (food search)"),
    "surface.pill":       ("17-search-focused-chips-recent-pills", "fill", (450, 1250, 5, 5), "Recent-search pill"),
    "surface.tooltip":    ("13-moments-feed-tabs-chips-tooltip", "fill", (140, 318, 10, 10), "Tooltip (Save posts)"),
    "surface.coachmark":  ("09-activity-coachmark-tooltip", "fill", (300, 330, 20, 10), "Coach mark card"),
    "surface.sheet":      ("11-notification-preprompt-sheet-yes-later", "fill", (300, 1700, 200, 20), "Pre-prompt sheet"),
    "surface.timer":      ("19-food-flash-deals-sheet-timer", "fill", (318, 380, 6, 50), "Flash deal countdown digit box"),
    "scrim.ref":          ("12-messages-toast-fab", "fill", (300, 500, 200, 20), "Messages, undimmed"),
    "scrim.dialog":       ("11-notification-preprompt-sheet-yes-later", "fill", (300, 500, 200, 20), "Messages under the pre-prompt sheet"),
    "scrim.coachmark":    ("09-activity-coachmark-tooltip", "fill", (300, 1640, 20, 20), "Activity under the coach mark"),
    "scrim.sheetRef":     ("20-food-home-chips-categories-tabbar", "fill", (400, 180, 20, 20), "Food header, undimmed"),
    "scrim.sheet":        ("19-food-flash-deals-sheet-timer", "fill", (400, 180, 20, 20), "Food header under the flash deals sheet"),
    "border.card":        ("01-home-tiles-search", "fill", (100, 732, 200, 1), "Card border, top edge (Finance card, one pixel row)"),
    "border.divider":     ("12-messages-toast-fab", "fill", (300, 428, 200, 1), "Divider under a list row (one pixel row)"),
    "border.control":     ("16-checkboxes-disabled-save", "fill", (705, 795, 2, 10), "Checkbox border, left edge"),
    "border.chip":        ("13-moments-feed-tabs-chips-tooltip", "fill", (400, 555, 100, 1), "Outlined filter chip border, top edge (one pixel row)"),
    "border.selected":    ("07-ride-options-book-button-not-pressed", "fill", (300, 838, 200, 1), "Selected ride option border, top edge (one pixel row)"),
    "border.field":       ("04-destination-focused-recent-tabs", "fill", (300, 334, 200, 1), "Text field border, unfocused (pickup field, top edge)"),
    "focus.ring":         ("04-destination-focused-recent-tabs", "fill", (300, 439, 200, 1), "Focused text field border (destination field, top edge)"),
    "focus.glow":         ("04-destination-focused-recent-tabs", "fill", (300, 435, 200, 1), "Soft green glow outside the focused field"),
    "focus.caret":        ("17-search-focused-chips-recent-pills", "fill", (129, 325, 2, 10), "Text caret in a focused field"),
    # ---------------------------------------------------------------- text
    "text.primary":       ("08-merchant-page-tabs-voucher-buy", "text", (50, 955, 170, 45), "Section title ('Vouchers')"),
    "text.body":          ("14-account-cards-list", "text", (55, 1355, 160, 40), "Settings row label"),
    "text.secondary":     ("10-activity-list-status-labels", "text", (165, 770, 230, 35), "Trip date in Activity"),
    "text.label":         ("01-home-tiles-search", "text", (80, 758, 90, 28), "Card label ('Finance')"),
    "text.rowValue":      ("14-account-cards-list", "text", (540, 1358, 145, 30), "Row value ('0 GrabCoins')"),
    "text.placeholder":   ("01-home-tiles-search", "text", (120, 210, 190, 35), "Search placeholder on the home header"),
    "text.placeholderField": ("17-search-focused-chips-recent-pills", "text", (140, 315, 150, 35), "Search placeholder in a grey field"),
    "text.disabled":      ("16-checkboxes-disabled-save", "text", (365, 1575, 80, 35), "Disabled Save label"),
    "text.tab":           ("13-moments-feed-tabs-chips-tooltip", "text", (100, 455, 125, 35), "Inactive tab label ('Following')"),
    "text.tabActive":     ("13-moments-feed-tabs-chips-tooltip", "text", (355, 455, 105, 35), "Active tab label ('For you')"),
    "text.navInactive":   ("12-messages-toast-fab", "text", (60, 1660, 65, 25), "Inactive tab bar label ('Home')"),
    "text.navActive":     ("01-home-tiles-search", "text", (65, 1660, 60, 25), "Active tab bar label ('Home')"),
    "text.link":          ("10-activity-list-status-labels", "text", (590, 355, 175, 35), "Link ('View History')"),
    "text.linkBrand":     ("21-cart-empty-state", "text", (235, 1212, 345, 35), "Green text link ('Explore Available Options')"),
    "text.danger":        ("10-activity-list-status-labels", "text", (165, 452, 140, 35), "Status label 'Cancelled'"),
    "text.success":       ("10-activity-list-status-labels", "text", (165, 1148, 110, 35), "Status label 'Bill paid'"),
    "text.new":           ("14-account-cards-list", "text", (630, 1462, 55, 30), "'New' marker on a settings row"),
    "text.promo":         ("13-moments-feed-tabs-chips-tooltip", "text", (48, 195, 90, 35), "Orange highlight ('3.2M+')"),
    "text.onPrimary":     ("11-notification-preprompt-sheet-yes-later", "text", (370, 1445, 70, 45, "light"), "Primary button label ('Yes')"),
    "text.onSecondary":   ("11-notification-preprompt-sheet-yes-later", "text", (360, 1590, 90, 40), "Secondary button label ('Later')"),
    "text.onTooltip":     ("13-moments-feed-tabs-chips-tooltip", "text", (158, 335, 200, 35, "light"), "Tooltip text"),
    "text.chip":          ("17-search-focused-chips-recent-pills", "text", (246, 448, 135, 38), "Unselected chip label ('Transport')"),
    # ---------------------------------------------------------------- brand and controls
    "button.primary":     ("11-notification-preprompt-sheet-yes-later", "fill", (300, 1450, 20, 20), "Primary button ('Yes')"),
    "button.secondary":   ("11-notification-preprompt-sheet-yes-later", "fill", (300, 1590, 20, 30), "Secondary button ('Later')"),
    "button.disabled":    ("16-checkboxes-disabled-save", "fill", (60, 1560, 100, 15), "Disabled primary button ('Save')"),
    "button.compact":     ("08-merchant-page-tabs-voucher-buy", "fill", (690, 1145, 10, 20), "Compact buy button ('Buy')"),
    "chip.selected":      ("17-search-focused-chips-recent-pills", "fill", (60, 440, 10, 10), "Selected chip ('All')"),
    "chip.default":       ("17-search-focused-chips-recent-pills", "fill", (180, 436, 10, 10), "Unselected chip ('Transport')"),
    "nav.scan":           ("01-home-tiles-search", "fill", (395, 1600, 20, 10), "Centre scan button in the tab bar"),
    "fab":                ("12-messages-toast-fab", "fill", (700, 1460, 10, 10), "Floating action button (new chat)"),
    "tab.indicator":      ("13-moments-feed-tabs-chips-tooltip", "fill", (400, 519, 20, 2), "Active tab underline"),
    "badge.new":          ("13-moments-feed-tabs-chips-tooltip", "fill", (586, 582, 5, 15), "'New' badge on a chip, right padding"),
    "badge.discount":     ("20-food-home-chips-categories-tabbar", "fill", (300, 1525, 20, 20), "Flash deals bar"),
    # ---------------------------------------------------------------- sizes
    "size.buttonPrimary": ("11-notification-preprompt-sheet-yes-later", "bbox", ((300, 1450), (40, 1390, 740, 150), 8), "Primary button"),
    "size.buttonSecondary": ("11-notification-preprompt-sheet-yes-later", "bbox", ((300, 1600), (40, 1540, 740, 140), 3), "Secondary button"),
    "size.buttonDisabled": ("16-checkboxes-disabled-save", "bbox", ((200, 1560), (40, 1520, 740, 140), 2), "Disabled primary button"),
    "size.buttonCompact": ("08-merchant-page-tabs-voucher-buy", "bbox", ((690, 1150), (630, 1130, 130, 90), 12), "Compact Buy button"),
    "size.chip":          ("17-search-focused-chips-recent-pills", "bbox", ((60, 440), (40, 415, 130, 100), 10), "Selected chip ('All')"),
    "size.chipDefault":   ("17-search-focused-chips-recent-pills", "bbox", ((180, 436), (155, 415, 270, 100), 3), "Unselected chip ('Transport')"),
    "size.searchField":   ("17-search-focused-chips-recent-pills", "bbox", ((300, 330), (30, 280, 760, 110), 2), "Search field (grey)"),
    "size.searchHome":    ("01-home-tiles-search", "bbox", ((100, 225), (40, 175, 540, 100), 3), "Search field on the home header"),
    "size.scan":          ("01-home-tiles-search", "bbox", ((395, 1600), (340, 1570, 140, 130), 30), "Centre scan button"),
    "size.fab":           ("12-messages-toast-fab", "bbox", ((700, 1460), (630, 1420, 160, 160), 30), "Floating action button"),
    "size.field":         ("04-destination-focused-recent-tabs", "extent", ("col", 400, 320, 430, (400, 320), 12), "Text field height (pickup field)"),
    "size.checkbox":      ("16-checkboxes-disabled-save", "extent", ("row", 800, 690, 760, (690, 800), 12), "Checkbox width"),
    "size.cardW":         ("01-home-tiles-search", "extent", ("row", 790, 400, 790, (400, 790), 12), "Ride to card width"),
    "size.cardH":         ("01-home-tiles-search", "extent", ("col", 600, 700, 880, (600, 700), 12), "Ride to card height"),
    "size.tooltip":       ("13-moments-feed-tabs-chips-tooltip", "bbox", ((140, 318), (110, 280, 680, 170), 10), "Tooltip"),
    "size.tabBar":        ("12-messages-toast-fab", "find", ("col", 200, 1560, 1600, None, 0), "Tab bar top edge"),
    "rows.settings":      ("14-account-cards-list", "lines", (55, 1350, 260, 1720), "Settings row labels: their pitch is the row height"),
    # ---------------------------------------------------------------- radii
    "radius.button":      ("11-notification-preprompt-sheet-yes-later", "diag", (300, 1440, 80, 1465), "Primary button (capsule)"),
    "radius.buttonSecondary": ("11-notification-preprompt-sheet-yes-later", "diag", (300, 1570, 80, 1610), "Secondary button (capsule)"),
    "radius.card":        ("14-account-cards-list", "diag", (300, 320, 60, 340), "Account card over the mint header"),
    "radius.promo":       ("01-home-tiles-search", "diag", (200, 930, 60, 1000), "Promo card (insurance)"),
    "radius.sheet":       ("11-notification-preprompt-sheet-yes-later", "diag", (400, 700, 40, 720), "Sheet top corner"),
    "radius.sheetFlash":  ("19-food-flash-deals-sheet-timer", "diag", (200, 300, 30, 300), "Flash deals sheet top corner"),
    "radius.chip":        ("17-search-focused-chips-recent-pills", "diag", (100, 435, 60, 470), "Chip (capsule)"),
    "radius.searchField": ("17-search-focused-chips-recent-pills", "diag", (300, 300, 60, 330), "Search field"),
    "radius.tooltip":     ("13-moments-feed-tabs-chips-tooltip", "diag", (300, 318, 135, 340), "Tooltip"),
    # ---------------------------------------------------------------- type (cap heights)
    "type.largeTitle":    ("12-messages-toast-fab", "cap", (48, 200, 96, 262), "'M' of a page title ('Messages')"),
    "type.title":         ("16-checkboxes-disabled-save", "cap", (143, 205, 170, 262), "'D' of a pushed page title ('Dietary preferences')"),
    "type.sectionTitle":  ("14-account-cards-list", "cap", (48, 1235, 68, 1290), "'F' of a section title ('For more value')"),
    "type.sectionHeader": ("10-activity-list-status-labels", "cap", (48, 345, 72, 390), "'R' of a list header ('Recent')"),
    "type.sheetTitle":    ("11-notification-preprompt-sheet-yes-later", "cap", (63, 1135, 90, 1190), "'T' of a sheet title"),
    "type.display":       ("20-food-home-chips-categories-tabbar", "cap", (48, 465, 76, 520), "'N' of a banner title ('Night munchies')"),
    "type.body":          ("14-account-cards-list", "cap", (55, 1555, 80, 1610), "'R' of a settings row ('Rewards')"),
    "type.listTitle":     ("19-food-flash-deals-sheet-timer", "cap", (253, 555, 272, 595), "'P' of a merchant name"),
    "type.subhead":       ("16-checkboxes-disabled-save", "cap", (152, 1032, 177, 1068), "'M' of a row subtitle"),
    "type.label":         ("01-home-tiles-search", "cap", (80, 755, 93, 790), "'F' of a card label ('Finance')"),
    "type.button":        ("11-notification-preprompt-sheet-yes-later", "cap", (378, 1445, 402, 1488), "'Y' of 'Yes'"),
    "type.chip":          ("17-search-focused-chips-recent-pills", "cap", (246, 448, 266, 485), "'T' of 'Transport'"),
    "type.tab":           ("13-moments-feed-tabs-chips-tooltip", "cap", (100, 455, 116, 492), "'F' of 'Following'"),
    "type.caption":       ("01-home-tiles-search", "cap", (66, 1658, 82, 1690), "'H' of a tab bar label"),
    "lines.body":         ("11-notification-preprompt-sheet-yes-later", "lines", (65, 1270, 630, 1360), "Two-line sheet body"),
    "lines.paragraph":    ("16-checkboxes-disabled-save", "lines", (48, 618, 715, 722), "Three-line intro paragraph"),
    "lines.sheetTitle":   ("11-notification-preprompt-sheet-yes-later", "lines", (65, 1138, 620, 1240), "Two-line sheet title"),
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
    if not (raw / "light").is_dir():
        raise SystemExit(f"{raw}: no light/ captures; nothing written")
    cache, out = {}, {}
    for rid, (cap, op, args, note) in R.items():
        themes = [cap.split("/")[0]] if "/" in cap else ["light"]   # Grab has no dark UI
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
    # Grab has no dark UI: a reading without a theme prefix is read in light; missing it means a capture is absent.
    short = sorted(rid for rid, (cap, *_) in R.items()
                   if set(readings.get(rid, {})) != ({cap.split("/")[0]} if "/" in cap else {"light"}))
    if short:
        raise SystemExit(f"{len(short)} readings lack a theme they need ({', '.join(short[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
