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

NAME = "Cursor for iOS"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only. A capture laid out differently
# per theme takes {"dark": (capture, op, args), "light": (capture, op, args), "note": ...}.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            ("01-repo-agents-list-composer", "fill", (300, 1000, 200, 100), "Repo list, Inbox and agent thread background"),
    "bg.inbox":           ("02-inbox-tiles-projects-workspaces", "fill", (300, 1300, 300, 20), "Inbox background between Projects and Workspaces"),
    "bg.sheet":           ("04-customize-sheet-switches-popups", "fill", (400, 1650, 200, 50), "Customize sheet background (full-height sheet)"),
    "bg.sheetHalf":       ("09-model-sheet-search-field", "fill", (600, 1280, 100, 40), "Model sheet background (half-height sheet)"),
    "bg.sheetGrouped":    ("07-changes-sheet-disclosure-empty-diff", "fill", (300, 1200, 300, 100), "Changes sheet background below its file rows"),
    "scrim.ref":          ("08-composer-expanded-typed-model-send", "fill", (600, 620, 100, 10), "Thread background, undimmed"),
    "scrim.sheet":        ("09-model-sheet-search-field", "fill", (600, 620, 100, 10), "The same thread under the Model sheet's scrim"),
    "scrim.fullSheet":    ("04-customize-sheet-switches-popups", "fill", (400, 100, 100, 30), "Status-bar strip above a full-height sheet"),
    "surface.tile":       ("02-inbox-tiles-projects-workspaces", "fill", (200, 440, 150, 30), "Inbox tile (All Agents)"),
    "surface.card":       ("06-agent-thread-changes-card-diffstat", "fill", (400, 830, 200, 40), "Changes card in the agent thread"),
    "surface.row":        {"dark": ("07-changes-sheet-disclosure-empty-diff", "fill", (300, 380, 200, 10)),
                           "light": ("07-changes-sheet-disclosure-empty-diff", "fill", (300, 500, 100, 10)),
                           "note": "File row in the Changes sheet (the sheet is laid out differently in each theme)"},
    "surface.inset":      {"dark": ("07-changes-sheet-disclosure-empty-diff", "fill", (100, 680, 150, 30)),
                           "light": ("07-changes-sheet-disclosure-empty-diff", "fill", (100, 820, 150, 30)),
                           "note": "Expanded file row: the empty diff band ('Diff not available')"},
    "surface.secondary":  ("13-search-sheet-focused-chips-rows", "fill", (62, 450, 8, 40), "Selected filter chip ('All') in Search"),
    "surface.banner":     ("18-context-sheet-mode-options", "fill", (100, 1020, 80, 20), "Photo-access card in the Context sheet"),
    "surface.code":       ("06-agent-thread-changes-card-diffstat", "fill", (315, 392, 8, 25), "Inline code chip in an agent reply (dominant pixel beside the glyphs)"),
    "surface.avatar":     ("15-profile-sheet-bar-charts", "fill", (330, 380, 40, 40), "Profile avatar circle (initial on grey)"),
    "surface.iconButton": ("12-agent-details-sheet-icon-buttons", "fill", (262, 1262, 6, 10), "Round action button in the agent details sheet (Rename, Unpin, Share)"),
    "surface.continue":   ("18-context-sheet-mode-options", "fill", (325, 1105, 15, 30), "'Continue' capsule in the photo-access card (glass)"),
    "surface.composer":   ("01-repo-agents-list-composer", "fill", (400, 1590, 200, 10), "Composer capsule (glass; centre reading)"),
    "surface.composerOpen": ("08-composer-expanded-typed-model-send", "fill", (400, 1450, 200, 50), "Expanded composer panel"),
    "surface.composerButton": ("01-repo-agents-list-composer", "fill", (70, 1605, 6, 6), "Round + and microphone buttons inside the composer"),
    "surface.navButton":  ("01-repo-agents-list-composer", "fill", (58, 205, 10, 20), "Round glass nav button (back), beside the glyph"),
    "surface.search":     ("13-search-sheet-focused-chips-rows", "fill", (500, 330, 200, 15), "Search field in a sheet (glass capsule)"),
    "surface.menu":       ("11-agent-menu-pulldown", "fill", (600, 250, 100, 20), "Pull-down menu (glass; picks up what is behind)"),
    "surface.popup":      ("05-group-by-popup-menu", "fill", (600, 520, 100, 20), "Pop-up menu over a sheet (Group by)"),
    "surface.grabber":    ("07-changes-sheet-disclosure-empty-diff", "fill", (370, 184, 60, 3), "Sheet grabber"),
    "surface.segment":    ("light/19-pull-requests-sheet-segmented", "fill", (70, 1035, 10, 30), "Selected segment ('All') in the Pull Requests sheet"),
    "border.divider":     ("02-inbox-tiles-projects-workspaces", "find", ("col", 400, 990, 1300, None, 0), "Row edges down the Projects list (dividers)"),
    "border.dividerColour": ("02-inbox-tiles-projects-workspaces", "fill", (300, 1075, 300, 1), "Divider between Projects rows: its darkest pixel row (the line is anti-aliased over two rows)"),
    "border.tile":        ("02-inbox-tiles-projects-workspaces", "fill", (48, 470, 1, 80), "Tile rim, its left pixel column"),
    "border.menuDivider": ("11-agent-menu-pulldown", "fill", (330, 631, 380, 1), "Divider between menu groups (one pixel row)"),
    "border.chartGrid":   ("15-profile-sheet-bar-charts", "text", (400, 1209, 200, 6), "Chart gridline (200M)"),
    # ---------------------------------------------------------------- text
    "text.primary":       ("02-inbox-tiles-projects-workspaces", "text", (120, 1005, 160, 35), "Row title ('toolbox-v1')"),
    "text.largeTitle":    ("02-inbox-tiles-projects-workspaces", "text", (55, 315, 110, 45), "Large page title ('Inbox')"),
    "text.navTitle":      ("09-model-sheet-search-field", "text", (360, 920, 95, 35), "Sheet title ('Model')"),
    "text.body":          ("06-agent-thread-changes-card-diffstat", "text", (57, 650, 680, 120), "Agent reply text"),
    "text.secondary":     ("03-all-agents-grouped-status-dots", "text", (165, 550, 105, 35), "Row subtitle ('Merged')"),
    "text.sectionHeader": ("02-inbox-tiles-projects-workspaces", "text", (55, 935, 115, 35), "Section header ('Projects')"),
    "text.groupHeader":   ("01-repo-agents-list-composer", "text", (55, 420, 70, 35), "Collapsible group header ('Read')"),
    "text.stat":          ("15-profile-sheet-bar-charts", "text", (57, 875, 100, 25), "Stat label ('Tokens')"),
    "text.tertiary":      ("03-all-agents-grouped-status-dots", "text", (440, 550, 300, 35), "Repo name after a row subtitle"),
    "text.count":         ("02-inbox-tiles-projects-workspaces", "text", (205, 815, 25, 35), "Tile count ('0')"),
    "text.chevron":       ("02-inbox-tiles-projects-workspaces", "text", (725, 1005, 25, 35), "Row chevron"),
    "text.icon":          ("02-inbox-tiles-projects-workspaces", "text", (60, 1425, 38, 35), "Outline row icon (folder)"),
    "text.muted":         ("02-inbox-tiles-projects-workspaces", "text", (120, 1225, 180, 35), "'New Project' row: an action label between primary and secondary"),
    "text.chip":          ("13-search-sheet-focused-chips-rows", "text", (168, 458, 380, 35), "Unselected filter chip label"),
    "text.placeholder":   ("01-repo-agents-list-composer", "text", (150, 1600, 250, 40), "Composer placeholder ('Plan, ask, build...')"),
    "text.searchPlaceholder": ("09-model-sheet-search-field", "text", (140, 1025, 140, 35), "Search field placeholder ('Models...')"),
    "text.empty":         ("14-search-no-matches-empty", "text", (90, 1135, 630, 70), "Empty-state body"),
    "text.code":          ("06-agent-thread-changes-card-diffstat", "text", (103, 390, 220, 35), "Inline code text"),
    "text.check":         ("09-model-sheet-search-field", "text", (705, 1210, 35, 35), "Tick on the active model"),
    "text.diffAdd":       ("06-agent-thread-changes-card-diffstat", "text", (645, 925, 50, 35), "Lines added ('+17')"),
    "text.diffDelete":    ("06-agent-thread-changes-card-diffstat", "text", (702, 925, 32, 35), "Lines deleted ('-0')"),
    "text.glyph":         ("01-repo-agents-list-composer", "text", (70, 185, 40, 60), "Back chevron on a glass nav button"),
    "button.clear":       ("10-model-search-no-match", "fill", (586, 1028, 4, 4), "Clear button in a typed search field"),
    "text.onBanner":      ("18-context-sheet-mode-options", "text", (185, 1038, 440, 30), "Text in the photo-access card"),
    "text.version":       ("light/20-profile-bottom-streak-heatmap-support", "text", (255, 1672, 300, 22), "Version footer (monospace, upper case)"),
    "text.segmentOff":    ("light/19-pull-requests-sheet-segmented", "text", (178, 1035, 100, 30), "Unselected segment label ('Merged')"),
    "text.segmentOn":     ("light/19-pull-requests-sheet-segmented", "text", (90, 1035, 30, 30), "Selected segment label ('All')"),
    # ---------------------------------------------------------------- accent, status and controls
    "accent.unread":      ("03-all-agents-grouped-status-dots", "fill", (75, 775, 6, 6), "Unread dot before a Needs Attention agent"),
    "dot.read":           ("03-all-agents-grouped-status-dots", "fill", (75, 511, 6, 6), "Read dot before a read agent"),
    "accent.caret":       ("08-composer-expanded-typed-model-send", "fill", (126, 1346, 1, 40), "Text caret in the typed composer, one pixel column (light: the caret straddles two columns, so it reads paler)"),
    "switch.on":          ("04-customize-sheet-switches-popups", "fill", (650, 1195, 20, 20), "Switch on (Changes)"),
    "switch.off":         ("04-customize-sheet-switches-popups", "fill", (720, 1565, 20, 15), "Switch off (Last Updated)"),
    "switch.thumb":       ("04-customize-sheet-switches-popups", "fill", (700, 1200, 10, 10), "Switch thumb"),
    "button.send":        ("08-composer-expanded-typed-model-send", "fill", (688, 1598, 6, 6), "Send button, enabled"),
    "button.sendGlyph":   ("08-composer-expanded-typed-model-send", "text", (700, 1595, 30, 45, "inverse"), "Send arrow"),
    "button.mic":         ("08-composer-expanded-typed-model-send", "fill", (605, 1605, 6, 6), "Microphone button beside send"),
    "status.merged":      ("03-all-agents-grouped-status-dots", "text", (122, 550, 30, 30), "Merged branch icon"),
    "status.closed":      ("light/19-pull-requests-sheet-segmented", "text", (75, 1450, 35, 40), "Closed pull-request icon"),
    "status.draft":       ("03-all-agents-grouped-status-dots", "text", (122, 813, 30, 35), "Draft pull-request icon"),
    "icon.allAgents":     ("02-inbox-tiles-projects-workspaces", "text", (75, 510, 40, 40), "All Agents tile icon"),
    "icon.attention":     ("02-inbox-tiles-projects-workspaces", "text", (447, 510, 35, 40), "Needs Attention tile icon (bell)"),
    "icon.working":       ("02-inbox-tiles-projects-workspaces", "text", (73, 745, 45, 45), "Working tile icon (dots)"),
    "icon.review":        ("02-inbox-tiles-projects-workspaces", "text", (445, 750, 40, 40), "In Review tile icon"),
    "icon.projectA":      ("02-inbox-tiles-projects-workspaces", "text", (60, 1003, 38, 38), "Project icon, first project (teal wrench)"),
    "icon.projectB":      ("02-inbox-tiles-projects-workspaces", "text", (60, 1113, 38, 38), "Project icon, second project (violet wrench)"),
    "chart.bar":          ("15-profile-sheet-bar-charts", "fill", (230, 1150, 4, 100), "Bar in the Tokens chart"),
    "heat.0":             ("light/20-profile-bottom-streak-heatmap-support", "fill", (82, 507, 6, 6), "Activity heatmap, no activity"),
    "heat.1":             ("light/20-profile-bottom-streak-heatmap-support", "fill", (373, 507, 6, 6), "Activity heatmap, level 1"),
    "heat.2":             ("light/20-profile-bottom-streak-heatmap-support", "fill", (373, 623, 6, 6), "Activity heatmap, level 2"),
    "heat.3":             ("light/20-profile-bottom-streak-heatmap-support", "fill", (432, 565, 6, 6), "Activity heatmap, level 3"),
    "heat.4":             ("light/20-profile-bottom-streak-heatmap-support", "fill", (432, 681, 6, 6), "Activity heatmap, level 4 (busiest)"),
    # ---------------------------------------------------------------- sizes
    "size.navButton.w":   ("01-repo-agents-list-composer", "extent", ("row", 215, 20, 200, (300, 215), 12), "Round glass nav button, width"),
    "size.navButton.h":   ("01-repo-agents-list-composer", "extent", ("col", 92, 150, 290, (300, 215), 12), "Round glass nav button, height"),
    "size.composer.h":    ("01-repo-agents-list-composer", "extent", ("col", 400, 1530, 1740, (400, 1530), 12), "Composer capsule height"),
    "size.composer.w":    ("01-repo-agents-list-composer", "extent", ("row", 1616, 20, 790, (400, 1530), 12), "Composer capsule width (the scan stops inside the screen, which ends at x 795)"),
    "size.composerOpen.h": ("08-composer-expanded-typed-model-send", "extent", ("col", 550, 1230, 1740, (550, 1230), 12), "Expanded composer height"),
    "size.composerButton": ("01-repo-agents-list-composer", "extent", ("row", 1616, 45, 145, (300, 1600), 6), "Round + button inside the composer, width"),
    "size.send":          ("08-composer-expanded-typed-model-send", "bbox", ((688, 1598), (650, 1560, 120, 115), 6), "Send button"),
    "size.search.h":      ("13-search-sheet-focused-chips-rows", "extent", ("col", 600, 290, 420, (600, 290), 12), "Search field height"),
    "size.chip.w":        ("13-search-sheet-focused-chips-rows", "extent", ("row", 472, 40, 160, (300, 445), 4), "Selected filter chip ('All'), width through its centre"),
    "size.chip.h":        ("13-search-sheet-focused-chips-rows", "extent", ("col", 95, 420, 530, (95, 420), 4), "Selected filter chip, height through its centre"),
    "size.segment.w":     ("light/19-pull-requests-sheet-segmented", "extent", ("row", 1049, 40, 170, (300, 1022), 4), "Selected segment ('All'), width through its centre"),
    "size.segment.h":     ("light/19-pull-requests-sheet-segmented", "extent", ("col", 105, 995, 1110, (105, 995), 4), "Selected segment, height through its centre"),
    "size.switch":        ("04-customize-sheet-switches-popups", "bbox", ((650, 1195), (610, 1160, 180, 90), 10), "Switch track"),
    "size.switchThumb":   ("dark/04-customize-sheet-switches-popups", "bbox", ((700, 1200), (650, 1170, 130, 80), 6), "Switch thumb"),
    "size.tile.x":        ("02-inbox-tiles-projects-workspaces", "find", ("row", 470, 20, 790, None, 0), "Tile edges across the first row of Inbox tiles (rim pixels included)"),
    "size.tile.y":        ("02-inbox-tiles-projects-workspaces", "find", ("col", 300, 380, 920, None, 0), "Tile edges down the left column of Inbox tiles"),
    "size.card":          ("06-agent-thread-changes-card-diffstat", "bbox", ((400, 830), (40, 790, 730, 540), 2), "Changes card"),
    "size.iconButton":    ("12-agent-details-sheet-icon-buttons", "bbox", ((262, 1262), (240, 1210, 120, 120), 4), "Round action button in agent details"),
    "size.avatar":        ("15-profile-sheet-bar-charts", "bbox", ((330, 380), (280, 320, 250, 250), 3), "Profile avatar"),
    "size.continue":      ("dark/18-context-sheet-mode-options", "extent", ("row", 1123, 300, 520, (300, 1060), 8), "'Continue' capsule width through its centre"),
    "size.continue.h":    ("dark/18-context-sheet-mode-options", "extent", ("col", 405, 1060, 1190, (300, 1060), 8), "'Continue' capsule height through its centre"),
    "size.menu.w":        ("dark/11-agent-menu-pulldown", "extent", ("row", 600, 200, 790, (230, 600), 12), "Pull-down menu width (the scan stops inside the screen)"),
    "size.popup.w":       ("dark/05-group-by-popup-menu", "extent", ("row", 600, 200, 790, (230, 600), 12), "Pop-up menu width (the scan stops inside the screen)"),
    "size.grabber":       ("07-changes-sheet-disclosure-empty-diff", "bbox", ((400, 185), (320, 170, 170, 30), 6), "Sheet grabber"),
    "size.bar":           ("15-profile-sheet-bar-charts", "bbox", ((235, 1200), (220, 1100, 40, 220), 12), "One bar of the Tokens chart"),
    "size.heatDot":       ("light/20-profile-bottom-streak-heatmap-support", "bbox", ((435, 684), (410, 660, 50, 50), 30), "Busiest heatmap dot"),
    "rows.single":        ("02-inbox-tiles-projects-workspaces", "find", ("col", 400, 990, 1300, None, 0), "Row edges down the Projects list"),
    "rows.double":        ("dark/03-all-agents-grouped-status-dots", "find", ("col", 78, 740, 1150, (66, 162, 235), 30), "Unread-dot pixels down the three Needs Attention rows"),
    # ---------------------------------------------------------------- radii
    "radius.tile":        ("02-inbox-tiles-projects-workspaces", "diag", (200, 470, 150, 470), "Inbox tile"),
    "radius.card":        ("06-agent-thread-changes-card-diffstat", "diag", (400, 845, 70, 845), "Changes card"),
    "radius.banner":      ("18-context-sheet-mode-options", "diag", (600, 1030, 80, 1030), "Photo-access card"),
    "radius.sheet":       ("light/04-customize-sheet-switches-popups", "diag", (600, 320, 30, 320, 20), "Full-height sheet, top corner, against the grey strip above it"),
    "radius.sheetHalf":   ("09-model-sheet-search-field", "diag", (600, 990, 60, 1110), "Half-height sheet, top corner"),
    "radius.composerOpen": ("dark/08-composer-expanded-typed-model-send", "diag", (550, 1330, 60, 1450), "Expanded composer panel"),
    "radius.menu":        ("dark/11-agent-menu-pulldown", "diag", (650, 270, 300, 270), "Pull-down menu"),
    "radius.popup":       ("dark/05-group-by-popup-menu", "diag", (650, 520, 290, 520), "Pop-up menu"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.largeTitle":    ("dark/02-inbox-tiles-projects-workspaces", "cap", (54, 305, 66, 365), "'I' of 'Inbox'"),
    "type.navTitle":      ("dark/15-profile-sheet-bar-charts", "cap", (354, 225, 373, 270), "'P' of the sheet title 'Profile'"),
    "type.sheetTitle":    ("dark/09-model-sheet-search-field", "cap", (360, 915, 388, 960), "'M' of the sheet title 'Model'"),
    "type.rowTitle":      ("dark/04-customize-sheet-switches-popups", "cap", (121, 636, 140, 680), "'R' of the row title 'Repo'"),
    "type.body":          ("dark/06-agent-thread-changes-card-diffstat", "cap", (55, 645, 64, 690), "'I' of 'Items' in an agent reply"),
    "type.sectionHeader": ("dark/02-inbox-tiles-projects-workspaces", "cap", (55, 932, 74, 970), "'P' of 'Projects'"),
    "type.subtitle":      ("dark/03-all-agents-grouped-status-dots", "cap", (164, 548, 191, 584), "'M' of the row subtitle 'Merged'"),
    "type.composer":      ("dark/01-repo-agents-list-composer", "cap", (149, 1596, 169, 1642), "'P' of the composer placeholder"),
    "type.menuItem":      ("dark/11-agent-menu-pulldown", "cap", (392, 296, 413, 338), "'R' of 'Rename'"),
    "type.tileLabel":     ("dark/02-inbox-tiles-projects-workspaces", "cap", (444, 812, 453, 852), "'I' of 'In Review'"),
    "type.profileName":   ("dark/15-profile-sheet-bar-charts", "cap", (56, 600, 97, 645), "'W' of the profile name"),
    "type.statValue":     ("dark/15-profile-sheet-bar-charts", "cap", (139, 915, 173, 962), "'M' of '947M'"),
    "type.statLabel":     ("dark/15-profile-sheet-bar-charts", "cap", (56, 870, 78, 905), "'T' of 'Tokens'"),
    "type.chartAxis":     ("dark/15-profile-sheet-bar-charts", "cap", (211, 1316, 225, 1344), "'1' of '1 Oct' (monospace axis label)"),
    "type.emptyTitle":    ("dark/14-search-no-matches-empty", "cap", (322, 1085, 344, 1118), "'N' of 'No matches'"),
    "type.emptyBody":     ("dark/14-search-no-matches-empty", "cap", (89, 1133, 111, 1168), "'N' of 'Nothing matched'"),
    "type.detailTitle":   ("dark/12-agent-details-sheet-icon-buttons", "cap", (194, 1033, 227, 1078), "'M' of the agent title in its details sheet"),
    "type.chip":          ("dark/13-search-sheet-focused-chips-rows", "cap", (77, 455, 98, 490), "'A' of the chip 'All'"),
    "type.code":          ("dark/06-agent-thread-changes-card-diffstat", "cap", (116, 390, 131, 422), "'L' of inline code 'GL11'"),
    "lines.body":         ("dark/06-agent-thread-changes-card-diffstat", "lines", (57, 648, 740, 775), "Three lines of an agent reply"),
    "lines.empty":        ("dark/14-search-no-matches-empty", "lines", (90, 1135, 725, 1210), "Two lines of empty-state body"),
    "lines.detailTitle":  ("dark/12-agent-details-sheet-icon-buttons", "lines", (100, 1035, 710, 1185), "Three lines of the agent title in its details sheet"),
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


def op_diag(rows, cx, cyc, cxr, cy, tol=None):
    """tol: a fixed tolerance, for a corner whose side edge meets something other than its top."""
    f = rows[cy][cxr]
    x = cxr
    while x > 0 and d(rows[cy][x - 1], f) <= 3:
        x -= 1
    if x < 5:
        raise ValueError(f"diag: no edge with background beyond it left of ({cxr}, {cy})")
    bg = rows[cy][x - 5]
    tol = tol or max(2, d(bg, f) // 2)
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
        if isinstance(entry, dict):   # one box per theme
            note = entry["note"]
            plan = [(theme, *entry[theme]) for theme in ("dark", "light") if theme in entry]
        else:
            cap, op, args, note = entry
            themes = [cap.split("/")[0]] if "/" in cap else ["dark", "light"]
            plan = [(theme, cap, op, args) for theme in themes]
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
