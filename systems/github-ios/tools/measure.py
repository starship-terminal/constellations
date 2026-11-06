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

NAME = "GitHub Mobile"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
HOME, INBOX, EXPLORE, COPILOT = "01-home-my-work-favorites-empty-shortcuts", "03-inbox-chips-banner-unread-rows", \
    "05-explore-activity-card-merged-badge-code", "06-copilot-promo-card-status-badges"
SEARCH, TYPED, RESULTS, REPO = "07-search-focused-empty-qualifier-chips", "08-search-typed-scope-rows", \
    "10-repo-results-list", "11-repo-page-archived-banner-star-button-rows"
MENU, ISSUES, POPUP, ISSUE = "12-repo-overflow-menu", "13-issues-list-filter-chips-labels", \
    "14-state-filter-popup-menu", "15-issue-page-open-locked-badges-comment"
PRS, PR, DIFF, EMPTY = "16-pull-requests-list-draft-icons", "17-pr-page-draft-branch-pills-diffstat", \
    "18-files-changed-diff-view", "19-search-no-repositories-empty"
PROFILE, SETTINGS, CODEOPT, APPEAR = "20-profile-status-achievements-rows", "21-settings-grouped-values-new-badge", \
    "22-code-options-preview-switches-on-off", "23-appearance-choice-list"
FILTERS = "04-inbox-filters-sheet-checked"
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            (HOME, "fill", (300, 1170, 200, 20), "Page behind grouped cards (Home, Explore, Settings, Appearance)"),
    "bg.list":            (INBOX, "fill", (300, 870, 200, 20), "Full-bleed list page (Inbox, Issues, Pull Requests, repository, issue and PR pages)"),
    "bg.groupedSystem":   (CODEOPT, "fill", (300, 280, 200, 30), "Code Options page background (a system grouped table)"),
    "bg.sheet":           ("dark/" + FILTERS, "fill", (300, 1400, 200, 40), "Inbox Filters sheet background"),
    "surface.card":       (HOME, "fill", (300, 690, 200, 10), "Grouped card (My Work)"),
    "surface.cardSettings": (SETTINGS, "fill", (300, 985, 200, 4), "Grouped card in Settings, below the last row"),
    "surface.cardSystem": (CODEOPT, "fill", (60, 1100, 20, 60), "Grouped card on Code Options, left margin"),
    "surface.button":     (HOME, "fill", (200, 1035, 60, 10), "Add Favorites button"),
    "surface.buttonRepo": (REPO, "fill", (300, 840, 40, 8), "Star button on a repository"),
    "surface.status":     (PROFILE, "fill", (300, 575, 200, 10), "Profile status card ('locked in')"),
    "surface.glass":      (APPEAR, "fill", (560, 1700, 30, 8), "Tab bar glass over an empty page"),
    "surface.navButton":  (APPEAR, "fill", (66, 232, 12, 10), "Round glass back button, below the chevron"),
    "surface.tabSelected": (APPEAR, "fill", (125, 1655, 14, 14), "Selected tab's pill inside the tab bar"),
    "surface.menu":       ("dark/" + MENU, "fill", (600, 470, 60, 10), "Pull-down menu (glass; takes colour from what is behind)"),
    "surface.fab":        (COPILOT, "fill", (640, 1515, 8, 14), "New Session floating button, right of its label"),
    "surface.code":       (DIFF, "fill", (400, 512, 40, 12), "Unchanged line in the Files Changed diff"),
    "surface.gutter":     (DIFF, "fill", (22, 512, 22, 12), "Line-number gutter of an unchanged line"),
    "border.divider":     (HOME, "fill", (300, 483, 300, 1), "Divider between card rows (one pixel row)"),
    "border.section":     (INBOX, "fill", (300, 942, 300, 1), "Full-width separator between list sections"),
    # ---------------------------------------------------------------- text
    "text.primary":       (HOME, "text", (176, 405, 100, 40), "Card row title ('Issues')"),
    "text.secondary":     (INBOX, "text", (128, 975, 360, 30), "Inbox row repository line"),
    "text.rowValue":      (SETTINGS, "text", (530, 385, 160, 35), "Settings row value"),
    "text.emptyBody":     (HOME, "text", (130, 1450, 330, 25), "Shortcuts empty-state body"),
    "text.time":          (INBOX, "text", (698, 972, 66, 32), "Inbox row age ('3mo')"),
    "text.sectionHeader": (CODEOPT, "text", (88, 340, 130, 35), "Grouped section header ('Preview')"),
    "text.placeholder":   ("dark/" + SEARCH, "text", (140, 200, 220, 30), "Search field placeholder"),
    "text.link":          (COPILOT, "text", (612, 812, 115, 35), "'View All' link"),
    "text.danger":        (PR, "text", (676, 1030, 52, 35), "Deletions in a diffstat ('-26')"),
    "text.success":       (PR, "text", (612, 1030, 60, 35), "Additions in a diffstat ('+30')"),
    "text.attention":     (REPO, "text", (210, 304, 440, 35), "Archived banner text"),
    "text.done":          (COPILOT, "text", (175, 686, 110, 32), "'Dismiss' text button on the Copilot card"),
    "text.onEmphasis":    (EXPLORE, "text", (136, 1126, 96, 28, "light"), "'Merged' label on its badge"),
    "text.onDone":        (COPILOT, "text", (356, 686, 360, 32, "light"), "Label on the purple Copilot button"),
    "text.onFab":         (COPILOT, "text", (448, 1503, 182, 38, "light"), "'New Session' label"),
    "text.tab":           (HOME, "text", (296, 1676, 58, 24), "Unselected tab label ('Inbox')"),
    "text.tabSelected":   (HOME, "text", (130, 1676, 62, 24), "Selected tab label ('Home')"),
    "text.lineNumber":    (DIFF, "text", (50, 503, 40, 30), "Line number in the diff gutter"),
    "text.hunk":          (DIFF, "text", (160, 402, 110, 28), "Hunk header text"),
    "syntax.keyword":     (CODEOPT, "text", (108, 520, 50, 32), "Code preview keyword ('def')"),
    "syntax.entity":      (CODEOPT, "text", (174, 520, 140, 32), "Code preview function name ('fibonacci')"),
    "syntax.constant":    (CODEOPT, "text", (366, 562, 16, 24), "Code preview number ('0..1')"),
    "icon.success":       ("dark/" + ISSUES, "text", (50, 385, 44, 44), "Open-issue icon"),
    "icon.danger":        (COPILOT, "text", (94, 1172, 38, 40), "Failed agent-session icon"),
    # ---------------------------------------------------------------- accent and status
    "accent.fg":          (INBOX, "fill", (66, 1033, 10, 10), "Unread dot"),
    "accent.emphasis":    (CODEOPT, "fill", (608, 812, 22, 22), "Switch on"),
    "accent.subtle":      (INBOX, "fill", (588, 860, 150, 8), "Configure button fill, under its label"),
    "accent.text":        (INBOX, "text", (600, 822, 142, 38), "Configure label"),
    "accent.branch":      (EXPLORE, "fill", (300, 1118, 30, 6), "Branch-name pill ('main')"),
    "accent.caret":       ("dark/" + SEARCH, "fill", (135, 202, 1, 26), "Text caret, one pixel column"),
    "success.emphasis":   ("dark/" + ISSUE, "fill", (183, 588, 12, 14), "'Open' state badge"),
    "neutral.emphasis":   (PR, "fill", (180, 533, 12, 14), "'Draft' state badge"),
    "neutral.muted":      (PR, "fill", (222, 536, 10, 12), "'Locked' badge"),
    "neutral.chip":       (COPILOT, "fill", (168, 1053, 8, 8), "'Completed' status chip"),
    "done.emphasis":      (EXPLORE, "fill", (238, 1130, 8, 18), "'Merged' state badge, right of its label"),
    "done.button":        (COPILOT, "fill", (338, 690, 12, 25), "'Email me a download link' button"),
    "attention.subtle":   (REPO, "fill", (100, 316, 40, 12), "Archived banner"),
    "diff.addition":      (DIFF, "fill", (400, 888, 40, 12), "Added line"),
    "diff.additionGutter": (DIFF, "fill", (22, 888, 22, 12), "Added line's gutter"),
    "diff.deletion":      (DIFF, "fill", (140, 598, 30, 8), "Deleted line"),
    "diff.deletionGutter": (DIFF, "fill", (22, 598, 22, 12), "Deleted line's gutter"),
    "diff.hunk":          (DIFF, "fill", (300, 385, 40, 6), "Hunk header row"),
    "switch.off":         (CODEOPT, "fill", (700, 1030, 12, 12), "Switch off track"),
    "switch.thumb":       (CODEOPT, "fill", (636, 1030, 12, 12), "Switch thumb"),
    # ---------------------------------------------------------------- icon tiles (Home, repository, profile)
    "tile.green":         (HOME, "fill", (93, 401, 8, 8), "Issues tile"),
    "tile.gray":          (HOME, "fill", (93, 515, 8, 8), "Top Repositories tile"),
    "tile.yellow":        (HOME, "fill", (93, 629, 8, 8), "Starred tile"),
    "tile.blue":          (REPO, "fill", (53, 1037, 8, 8), "Pull Requests tile"),
    "tile.purple":        (REPO, "fill", (53, 1151, 8, 8), "Discussions tile"),
    "tile.gold":          (REPO, "fill", (53, 1265, 8, 8), "Actions tile"),
    "tile.pink":          (REPO, "fill", (53, 1379, 8, 8), "Agents tile"),
    "tile.red":           (EXPLORE, "fill", (84, 621, 8, 8), "Awesome Lists tile"),
    "tile.orange":        (PROFILE, "fill", (53, 1247, 8, 8), "Organizations tile"),
    # ---------------------------------------------------------------- sizes
    "size.navButton.w":   (APPEAR, "extent", ("row", 214, 20, 200, (30, 300), 12), "Round glass back button, width"),
    "size.navButton.h":   (APPEAR, "extent", ("col", 92, 150, 300, (92, 300), 12), "Round glass back button, height"),
    "size.tabBar.h":      ("dark/" + EMPTY, "extent", ("col", 400, 1560, 1764, (400, 1570), 12), "Tab bar height"),
    "size.tabBar.w":      ("dark/" + EMPTY, "extent", ("row", 1700, 16, 796, (30, 1580), 12), "Tab bar width"),
    "size.search.h":      ("dark/" + SEARCH, "extent", ("col", 300, 150, 275, (300, 155), 10), "Search field height"),
    "size.chip.h":        (INBOX, "extent", ("col", 300, 370, 462, (300, 372), 8), "Filter chip height ('Focused')"),
    "size.button":        (HOME, "bbox", ((200, 1035), (70, 1010, 680, 110), 3), "Add Favorites button"),
    "size.buttonRepo":    (REPO, "bbox", ((300, 840), (40, 760, 520, 120), 3), "Star button"),
    "size.iconButtonRepo": (REPO, "bbox", ((580, 840), (555, 760, 110, 120), 3), "Fork button beside Star"),
    "size.doneButton":    (COPILOT, "bbox", ((340, 700), (320, 650, 430, 100), 10), "Purple Copilot button"),
    "size.configure":     (INBOX, "bbox", ((590, 862), (565, 795, 210, 90), 4), "Configure button"),
    "size.fab":           ("light/" + COPILOT, "bbox", ((640, 1520), (360, 1465, 310, 115), 10), "New Session floating button"),
    "size.switch":        (CODEOPT, "bbox", ((612, 823), (580, 780, 170, 90), 10), "Switch track, on"),
    "size.switchThumb":   ("dark/" + CODEOPT, "bbox", ((640, 1036), (590, 1000, 150, 75), 6), "Switch thumb"),
    "size.badge":         ("dark/" + ISSUE, "bbox", ((190, 596), (40, 560, 180, 75), 12), "'Open' badge"),
    "size.draft":         (PR, "bbox", ((185, 540), (40, 505, 175, 80), 12), "'Draft' badge"),
    "size.branch":        (EXPLORE, "bbox", ((300, 1118), (262, 1100, 130, 80), 4), "Branch-name pill"),
    "size.chipStatus":    (COPILOT, "bbox", ((170, 1056), (150, 1025, 190, 65), 4), "'Completed' chip"),
    "size.newBadge":      (SETTINGS, "bbox", ((95, 722), (80, 695, 80, 60), 4), "'New' badge"),
    "size.tile":          (HOME, "bbox", ((93, 401), (75, 385, 95, 95), 14), "Icon tile (Issues)"),
    "size.label":         ("dark/" + ISSUES, "bbox", ((398, 580), (120, 555, 300, 55), 14), "Issue label ('area: documentation')"),
    "size.avatarHeader":  (HOME, "extent", ("row", 214, 30, 170, (32, 214), 14), "Account avatar on Home"),
    "size.avatarComment": ("dark/" + ISSUE, "extent", ("row", 750, 30, 150, (32, 750), 14), "Comment author avatar"),
    "size.avatarProfile": (PROFILE, "extent", ("row", 375, 30, 200, (32, 375), 14), "Profile avatar"),
    "rows.home":          (HOME, "find", ("col", 600, 372, 712, None, 0), "Edges down the My Work card"),
    "rows.settings":      (SETTINGS, "find", ("col", 400, 350, 990, None, 0), "Edges down the first Settings card"),
    "rows.search":        (TYPED, "find", ("col", 300, 280, 1080, None, 0), "Edges down the search scope list"),
    # ---------------------------------------------------------------- radii
    "radius.card":        (HOME, "diag", (400, 380, 60, 550), "My Work card"),
    "radius.cardSettings": (SETTINGS, "diag", (400, 360, 60, 520), "Settings card"),
    "radius.button":      (HOME, "diag", (200, 1032, 88, 1070), "Add Favorites button"),
    "radius.buttonRepo":  (REPO, "diag", (180, 780, 58, 816), "Star button"),
    "radius.tile":        (HOME, "diag", (100, 400, 92, 440), "Icon tile (Issues)"),
    "radius.status":      (PROFILE, "diag", (400, 488, 58, 560), "Profile status card"),
    "radius.codeCard":    ("dark/" + CODEOPT, "diag", (400, 396, 58, 470), "Code preview card"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.largeTitle":    ("dark/" + INBOX, "cap", (48, 296, 66, 356), "'I' of the large title 'Inbox'"),
    "type.title2":        ("dark/" + HOME, "cap", (48, 306, 85, 350), "'M' of a Home section title ('My Work')"),
    "type.title1":        ("dark/" + ISSUE, "cap", (455, 390, 503, 435), "'F' of an issue title"),
    "type.navTitle":      ("dark/" + ISSUES, "cap", (355, 196, 364, 234), "'I' of a nav title ('Issues')"),
    "type.headline":      ("dark/" + HOME, "cap", (176, 408, 184, 446), "'I' of a card row title ('Issues')"),
    "type.settingsRow":   ("dark/" + SETTINGS, "cap", (87, 384, 111, 420), "'A' of a Settings row"),
    "type.body":          ("dark/" + ISSUE, "cap", (48, 832, 56, 866), "'I' of comment body text"),
    "type.button":        ("dark/" + HOME, "cap", (301, 1048, 342, 1084), "'A' of 'Add Favorites'"),
    "type.emptyTitle":    ("dark/" + EMPTY, "cap", (114, 884, 142, 928), "'T' of an empty-state line"),
    "type.meta":          ("dark/" + RESULTS, "cap", (111, 318, 156, 350), "'W' of a result's owner line"),
    "type.time":          ("dark/" + INBOX, "cap", (699, 972, 718, 1003), "'3' of a row age"),
    "type.chip":          ("dark/" + INBOX, "cap", (221, 400, 236, 432), "'F' of a filter chip ('Focused')"),
    "type.inboxTitle":    ("dark/" + INBOX, "cap", (128, 1060, 136, 1094), "'I' of an Inbox row title"),
    "type.badge":         ("dark/" + EXPLORE, "cap", (136, 1125, 157, 1152), "'M' of 'Merged'"),
    "type.footnote":      ("dark/" + PR, "cap", (176, 682, 196, 707), "'M' of the 'Member' label"),
    "type.tab":           ("dark/" + HOME, "cap", (131, 1676, 147, 1700), "'H' of a tab label"),
    "type.sectionHeader": ("dark/" + CODEOPT, "cap", (88, 340, 110, 372), "'P' of a grouped section header"),
    "type.mono":          ("dark/" + DIFF, "cap", (181, 455, 195, 484), "'I' of diff code ('Install')"),
    "lines.body":         ("dark/" + EXPLORE, "lines", (73, 1310, 710, 1505), "Four lines of Markdown body text"),
    "lines.title1":       ("dark/" + ISSUE, "lines", (48, 390, 740, 548), "Three-line issue title"),
    "lines.subhead":      ("dark/" + INBOX, "lines", (48, 700, 745, 778), "Two-line banner text"),
    "lines.headline":     ("dark/" + INBOX, "lines", (128, 1020, 600, 1135), "Three-line Inbox row title"),
    "lines.diff":         ("dark/" + DIFF, "lines", (50, 455, 95, 590), "Diff line numbers 9 to 11 (one row each)"),
    "lines.code":         ("dark/" + CODEOPT, "lines", (100, 520, 560, 672), "Four lines of the code preview"),
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
