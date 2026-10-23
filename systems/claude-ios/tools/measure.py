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

NAME = "Claude for iOS"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# id: (capture, op, args, note). Captures without a theme prefix are read in both themes when the
# file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            ("01-new-chat-greeting-composer", "fill", (300, 400, 200, 200), "New chat and chat thread background"),
    "bg.thread":          ("07-chat-thread-user-bubble-response-actions", "fill", (600, 1000, 150, 8), "Chat thread background, right of the response"),
    "bg.list":            ("14-time-focus-selects-day-toggles", "fill", (300, 1200, 300, 100), "Pushed list and settings pages (Time & focus body)"),
    "bg.listChats":       ("dark/11-chats-list-search-new-chat", "fill", (300, 1100, 100, 40), "Chats list background"),
    "bg.listProjects":    ("dark/18-projects-list-new-project-pill", "fill", (300, 1000, 300, 200), "Projects list background"),
    "bg.sidebar":         ("06-sidebar-nav-pinned-recents", "fill", (400, 870, 200, 20), "Sidebar background"),
    "bg.sheet":           ("03-model-picker-sheet", "fill", (200, 990, 400, 20), "Bottom sheet background (Select model)"),
    "bg.sheetSettings":   ("13-settings-sheet-grouped", "fill", (300, 315, 300, 20), "Settings sheet background, under its nav bar"),
    "scrim.ref":          ("01-new-chat-greeting-composer", "fill", (300, 400, 200, 100), "New chat behind a sheet, undimmed"),
    "scrim.sheet":        ("03-model-picker-sheet", "fill", (300, 400, 200, 100), "New chat under the sheet scrim"),
    "scrim.context":      ("dark/09-message-longpress-menu", "fill", (300, 1100, 10, 30), "Thread under the long-press scrim"),
    "surface.card":       ("13-settings-sheet-grouped", "fill", (560, 640, 150, 20), "Grouped card in Settings (Give the gift of Claude)"),
    "surface.cardSheet":  ("03-model-picker-sheet", "fill", (400, 1040, 200, 15), "Grouped card in a bottom sheet (model list)"),
    "surface.userBubble": ("07-chat-thread-user-bubble-response-actions", "fill", (300, 296, 400, 12), "The owner's message bubble, above its text"),
    "surface.composer":   ("07-chat-thread-user-bubble-response-actions", "fill", (500, 1515, 200, 15), "Composer (glass; centre reading above the placeholder)"),
    "surface.control":    ("07-chat-thread-user-bubble-response-actions", "fill", (170, 1620, 20, 10), "Model pill inside the composer"),
    "surface.navGlass":   ("01-new-chat-greeting-composer", "fill", (60, 200, 8, 8), "Round glass sidebar button, beside its icon"),
    "surface.menu":       ("08-chat-menu-destructive", "fill", (600, 280, 100, 8), "Pull-down menu (glass; picks up colour from what is behind)"),
    "surface.selected":   ("dark/23-sidebar-selected-row", "fill", (450, 500, 150, 10), "Selected sidebar row (Code)"),
    "surface.badge":      ("15-capabilities-switches-on-disabled", "fill", (476, 535, 8, 25), "Beta badge fill, left of its label"),
    "surface.badgeRecommended": ("dark/04-effort-sheet-badges", "fill", (240, 1172, 6, 10), "Recommended badge fill"),
    "surface.badgeUsage": ("dark/04-effort-sheet-badges", "fill", (182, 1470, 6, 8), "'5.5x or more usage' badge fill (amber)"),
    "surface.field":      ("14-time-focus-selects-day-toggles", "fill", (60, 655, 10, 20), "Pop-up select field (Break reminders)"),
    "surface.searchField": ("dark/12-chats-search-typed-results", "fill", (300, 1640, 200, 10), "Search field, typed"),
    "surface.dayToggle":  ("14-time-focus-selects-day-toggles", "fill", (60, 975, 10, 25), "Day toggle circle, off (Quiet hours)"),
    "surface.emptyIcon":  ("dark/19-archived-empty-state-accent-icon", "fill", (370, 870, 15, 10), "Circle behind an empty-state icon"),
    "border.divider":     ("13-settings-sheet-grouped", "fill", (300, 939, 300, 1), "Divider between settings rows (one pixel row)"),
    "border.field":       ("14-time-focus-selects-day-toggles", "fill", (50, 640, 1, 30), "Pop-up select rim, left edge"),
    "border.listCard":    ("dark/20-artifacts-list-cards", "fill", (48, 380, 1, 60), "Artifact card rim, left edge (the card is only a rim on the page)"),
    "border.grabber":     ("03-model-picker-sheet", "fill", (370, 876, 60, 4), "Sheet grabber"),
    # ---------------------------------------------------------------- text
    "text.primary":       ("13-settings-sheet-grouped", "text", (168, 870, 110, 40), "Settings row label ('Profile')"),
    "text.response":      ("07-chat-thread-user-bubble-response-actions", "text", (48, 640, 560, 40), "Serif response text ('Done. Both now use ...')"),
    "text.onUserBubble":  ("07-chat-thread-user-bubble-response-actions", "text", (170, 320, 520, 40), "Text in the owner's bubble"),
    "text.greeting":      ("01-new-chat-greeting-composer", "text", (136, 905, 540, 55), "Serif greeting on a new chat"),
    "text.wordmark":      ("06-sidebar-nav-pinned-recents", "text", (48, 195, 155, 45), "'Claude' wordmark at the top of the sidebar"),
    "text.secondary":     ("13-settings-sheet-grouped", "text", (185, 425, 450, 35), "Account line under the account name"),
    "text.sidebarSection": ("06-sidebar-nav-pinned-recents", "text", (64, 915, 100, 32), "Sidebar section header ('Pinned')"),
    "text.tertiary":      ("03-model-picker-sheet", "text", (100, 1105, 340, 35), "Sheet row subtitle ('For your toughest challenges')"),
    "text.sectionHeader": ("13-settings-sheet-grouped", "text", (88, 780, 120, 35), "Settings section header ('Account')"),
    "text.rowValue":      ("13-settings-sheet-grouped", "text", (530, 975, 140, 40), "Settings row value ('Max plan')"),
    "text.toolStep":      ("07-chat-thread-user-bubble-response-actions", "text", (110, 548, 580, 38), "Tool-step summary row ('Checking whether ...')"),
    "text.actionIcon":    ("07-chat-thread-user-bubble-response-actions", "text", (48, 1300, 360, 45), "Response action icons (copy, share, play, thumbs, retry)"),
    "text.placeholder":   ("07-chat-thread-user-bubble-response-actions", "text", (75, 1535, 480, 40), "Composer placeholder ('Reply to Claude or hold to talk')"),
    "text.footnote":      ("07-chat-thread-user-bubble-response-actions", "text", (48, 1400, 440, 30), "Disclaimer under a response"),
    "text.chevron":       ("13-settings-sheet-grouped", "text", (690, 875, 25, 35), "Disclosure chevron on a settings row"),
    "text.listSubtitle":  ("dark/11-chats-list-search-new-chat", "text", (140, 360, 200, 35), "Chats list row subtitle ('last week')"),
    "text.disabled":      ("15-capabilities-switches-on-disabled", "text", (150, 382, 145, 40), "Title of a locked setting ('Artifacts')"),
    "text.disabledSubtitle": ("15-capabilities-switches-on-disabled", "text", (150, 432, 345, 30), "Subtitle of a locked setting"),
    "text.subtitle":      ("15-capabilities-switches-on-disabled", "text", (150, 585, 310, 30), "Setting subtitle ('Allow Claude to generate ...')"),
    "text.link":          ("13-settings-sheet-grouped", "text", (185, 525, 200, 40), "'Add account' action text"),
    "text.selectedDark":  ("dark/24-settings-app-appearance-cards", "text", (575, 1725, 95, 30), "Label of the chosen Appearance tile ('System')"),
    "text.selectedLight": ("light/24-settings-app-appearance-cards", "text", (155, 1725, 65, 30), "Label of the chosen Appearance tile ('Light')"),
    "text.tileLabel":     ("dark/24-settings-app-appearance-cards", "text", (375, 1725, 60, 30), "Label of an unchosen Appearance tile ('Dark')"),
    "text.destructive":   ("08-chat-menu-destructive", "text", (390, 632, 100, 42), "'Delete' menu item"),
    "text.menuItem":      ("08-chat-menu-destructive", "text", (390, 215, 95, 40), "'Unpin' menu item"),
    "text.badge":         ("15-capabilities-switches-on-disabled", "text", (488, 538, 62, 30), "'Beta' badge label"),
    "text.badgeRecommended": ("dark/04-effort-sheet-badges", "text", (250, 1160, 160, 32), "'Recommended' badge label"),
    "text.badgeUsage":    ("dark/04-effort-sheet-badges", "text", (190, 1455, 195, 35), "'5.5x or more usage' badge label"),
    "text.onPrimary":     ("07-chat-thread-user-bubble-response-actions", "text", (660, 1630, 60, 40, "inverse"), "'Talk' label on the inverse pill"),
    "text.onAccent":      ("02-composer-typed-send-enabled", "text", (712, 1625, 30, 40, "light"), "Arrow on the orange send button"),
    "text.emptyTitle":    ("dark/19-archived-empty-state-accent-icon", "text", (240, 985, 335, 45), "Empty-state line ('No archived projects')"),
    "text.pillSecondary": ("dark/21-code-empty-sessions-secondary-pill", "text", (140, 425, 170, 45), "'Add device' label on a glass pill"),
    # ---------------------------------------------------------------- accent and controls
    "accent.brand":       ("01-new-chat-greeting-composer", "fill", (400, 835, 6, 6), "The spark above the greeting, centre"),
    "accent.send":        ("02-composer-typed-send-enabled", "fill", (698, 1625, 12, 30), "Send button, left of the arrow"),
    "accent.archive":     ("dark/19-archived-empty-state-accent-icon", "fill", (688, 205, 12, 20), "Archive filter button, on (glass tinted orange)"),
    "accent.blue":        ("15-capabilities-switches-on-disabled", "fill", (612, 540, 20, 15), "Switch on (Inline visualizations)"),
    "accent.check":       ("03-model-picker-sheet", "text", (675, 1215, 40, 40), "Tick on the chosen model"),
    "button.primary":     ("07-chat-thread-user-bubble-response-actions", "fill", (600, 1620, 15, 10), "Talk pill (the inverse primary pill)"),
    "button.primarySidebar": ("06-sidebar-nav-pinned-recents", "fill", (380, 1625, 20, 10), "New chat pill over the sidebar (glass)"),
    "button.control":     ("07-chat-thread-user-bubble-response-actions", "fill", (80, 1625, 10, 10), "+ button inside the composer"),
    "focus.caret":        ("02-composer-typed-send-enabled", "fill", (134, 1530, 1, 40), "Text caret after typed text, one pixel column"),
    "switch.on":          ("15-capabilities-switches-on-disabled", "fill", (612, 540, 20, 15), "Switch on"),
    "switch.onDisabled":  ("15-capabilities-switches-on-disabled", "fill", (612, 392, 15, 15), "Switch on, locked (Artifacts)"),
    "switch.off":         ("17-usage-progress-meters-switch-off", "fill", (700, 1545, 20, 15), "Switch off (Usage credits)"),
    "switch.thumb":       ("15-capabilities-switches-on-disabled", "fill", (680, 550, 20, 10), "Switch thumb"),
    "switch.thumbDisabled": ("15-capabilities-switches-on-disabled", "fill", (660, 395, 40, 10), "Switch thumb, locked"),
    "progress.fill":      ("17-usage-progress-meters-switch-off", "fill", (100, 755, 60, 4), "Usage meter fill (All models)"),
    "progress.track":     ("17-usage-progress-meters-switch-off", "fill", (400, 955, 200, 4), "Usage meter track (Fable only, 0%)"),
    # ---------------------------------------------------------------- sizes
    "size.navButton.w":   ("dark/01-new-chat-greeting-composer", "extent", ("row", 213, 20, 200, (25, 213), 12), "Round glass sidebar button, width"),
    "size.navButton.h":   ("dark/01-new-chat-greeting-composer", "extent", ("col", 92, 150, 280, (92, 150), 12), "Round glass sidebar button, height"),
    "size.composer.h":    ("dark/07-chat-thread-user-bubble-response-actions", "extent", ("col", 450, 1480, 1720, (450, 1480), 12), "Composer height, thread"),
    "size.composer.w":    ("dark/07-chat-thread-user-bubble-response-actions", "extent", ("row", 1580, 30, 790, (35, 1450), 12), "Composer width, thread"),
    "size.composerNew.w": ("dark/01-new-chat-greeting-composer", "extent", ("row", 1580, 20, 800, (25, 1450), 12), "Composer width, new chat"),
    "size.composerButton": ("dark/07-chat-thread-user-bubble-response-actions", "extent", ("row", 1645, 50, 150, (52, 1645), 6), "+ button inside the composer"),
    "size.talk":          ("dark/07-chat-thread-user-bubble-response-actions", "bbox", ((600, 1620), (570, 1590, 200, 110), 12), "Talk pill"),
    "size.send":          ("dark/02-composer-typed-send-enabled", "bbox", ((700, 1660), (670, 1590, 120, 110), 40), "Send button"),
    "size.userBubble":    ("dark/07-chat-thread-user-bubble-response-actions", "bbox", ((300, 296), (100, 270, 700, 230), 3), "The owner's bubble, three lines"),
    "size.cardAccount":   ("dark/13-settings-sheet-grouped", "bbox", ((600, 560), (30, 330, 760, 290), 3), "Account card in Settings"),
    "size.cardOneRow":    ("dark/13-settings-sheet-grouped", "bbox", ((560, 640), (30, 600, 760, 150), 3), "One-row card (Give the gift of Claude)"),
    "size.cardSheet":     ("dark/03-model-picker-sheet", "bbox", ((400, 1040), (40, 1010, 730, 590), 3), "Model list card in a sheet"),
    "size.cardSheetOneRow": ("dark/03-model-picker-sheet", "bbox", ((400, 1640), (40, 1590, 730, 140), 3), "One-row card in a sheet (Effort)"),
    "size.switch":        ("15-capabilities-switches-on-disabled", "bbox", ((612, 540), (580, 500, 180, 90), 12), "Switch track"),
    "size.switchThumb":   ("dark/15-capabilities-switches-on-disabled", "bbox", ((680, 550), (620, 510, 140, 80), 8), "Switch thumb"),
    "size.selectedRow":   ("dark/23-sidebar-selected-row", "bbox", ((450, 500), (20, 470, 640, 120), 4), "Selected sidebar row"),
    "size.pillPrimary":   ("dark/11-chats-list-search-new-chat", "bbox", ((700, 1520), (480, 1480, 300, 110), 8), "New chat pill"),
    "size.buttonFull":    ("dark/22-gift-sheet-illustration-primary", "bbox", ((200, 1630), (30, 1580, 750, 130), 8), "Full-width Share button"),
    "size.pillSecondary": ("dark/21-code-empty-sessions-secondary-pill", "bbox", ((80, 446), (50, 390, 320, 110), 4), "Add device pill (glass)"),
    "size.select":        ("14-time-focus-selects-day-toggles", "bbox", ((60, 655), (40, 610, 260, 100), 3), "Pop-up select field"),
    "size.dayToggle":     ("dark/14-time-focus-selects-day-toggles", "bbox", ((60, 988), (40, 945, 90, 90), 6), "Day toggle circle"),
    "size.progress":      ("17-usage-progress-meters-switch-off", "bbox", ((400, 955), (70, 935, 670, 40), 8), "Usage meter track"),
    "size.grabber":       ("03-model-picker-sheet", "bbox", ((400, 878), (330, 866, 150, 25), 8), "Sheet grabber"),
    "size.emptyIcon":     ("dark/19-archived-empty-state-accent-icon", "bbox", ((370, 870), (340, 830, 130, 130), 4), "Empty-state icon circle"),
    "size.badge":         ("dark/04-effort-sheet-badges", "bbox", ((240, 1172), (220, 1145, 220, 60), 3), "Recommended badge"),
    "size.badgeUsage":    ("dark/04-effort-sheet-badges", "bbox", ((182, 1470), (160, 1440, 260, 70), 6), "Usage badge"),
    "size.searchField.h": ("dark/12-chats-search-typed-results", "extent", ("col", 300, 1590, 1720, (300, 1590), 12), "Search field height"),
    "rows.settings":      ("dark/13-settings-sheet-grouped", "find", ("col", 600, 830, 1570, (53, 53, 53), 2), "Divider rows down the Account card"),
    "rows.sheet":         ("dark/03-model-picker-sheet", "find", ("col", 650, 1020, 1590, (53, 53, 53), 4), "Divider rows down the model list card"),
    "rows.sidebar":       ("dark/06-sidebar-nav-pinned-recents", "lines", (136, 310, 400, 860), "Sidebar nav labels: pitch of the rows"),
    "rows.chats":         ("dark/11-chats-list-search-new-chat", "lines", (70, 300, 106, 1450), "Chats list icons: pitch of the two-line rows"),
    # ---------------------------------------------------------------- radii
    "radius.userBubble":  ("07-chat-thread-user-bubble-response-actions", "diag", (450, 300, 160, 400), "The owner's bubble"),
    "radius.card":        ("13-settings-sheet-grouped", "diag", (400, 360, 70, 470), "Settings account card"),
    "radius.cardSheet":   ("03-model-picker-sheet", "diag", (400, 1040, 80, 1250), "Model list card in a sheet"),
    "radius.sheet":       ("03-model-picker-sheet", "diag", (250, 950, 50, 1000), "Bottom sheet top corner"),
    "radius.composer":    ("dark/07-chat-thread-user-bubble-response-actions", "diag", (400, 1510, 60, 1600), "Composer"),
    "radius.selectedRow": ("dark/23-sidebar-selected-row", "diag", (400, 495, 55, 530), "Selected sidebar row"),
    "radius.menu":        ("dark/08-chat-menu-destructive", "diag", (600, 190, 280, 300), "Pull-down menu (glass edge)"),
    "radius.select":      ("light/14-time-focus-selects-day-toggles", "diag", (160, 630, 60, 680), "Pop-up select field (light, where its rim reads)"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.display":       ("dark/22-gift-sheet-illustration-primary", "cap", (120, 830, 160, 890), "'G' of the promo sheet title (serif)"),
    "type.wordmark":      ("dark/06-sidebar-nav-pinned-recents", "cap", (48, 190, 78, 240), "'C' of the sidebar wordmark (serif)"),
    "type.greeting":      ("dark/01-new-chat-greeting-composer", "cap", (136, 900, 160, 960), "'I' of the new-chat greeting (serif)"),
    "type.response":      ("dark/07-chat-thread-user-bubble-response-actions", "cap", (48, 630, 75, 690), "'D' of a response (serif)"),
    "type.bubble":        ("dark/07-chat-thread-user-bubble-response-actions", "cap", (596, 315, 625, 365), "'H' in the owner's bubble"),
    "type.row":           ("dark/13-settings-sheet-grouped", "cap", (168, 865, 195, 915), "'P' of a settings row"),
    "type.sidebarItem":   ("dark/06-sidebar-nav-pinned-recents", "cap", (136, 310, 160, 355), "'C' of a sidebar item ('Chats')"),
    "type.listTitle":     ("dark/18-projects-list-new-project-pill", "cap", (145, 310, 165, 350), "'H' of a project row title"),
    "type.menuItem":      ("dark/08-chat-menu-destructive", "cap", (392, 212, 415, 252), "'U' of a menu item"),
    "type.composer":      ("dark/01-new-chat-greeting-composer", "cap", (62, 1530, 85, 1580), "'C' of the composer placeholder"),
    "type.navTitle":      ("dark/11-chats-list-search-new-chat", "cap", (360, 190, 385, 240), "'C' of a nav title ('Chats')"),
    "type.sheetTitle":    ("dark/03-model-picker-sheet", "cap", (305, 915, 330, 960), "'S' of a sheet title"),
    "type.emptyTitle":    ("dark/19-archived-empty-state-accent-icon", "cap", (240, 985, 262, 1025), "'N' of an empty-state line"),
    "type.pageHeading":   ("dark/14-time-focus-selects-day-toggles", "cap", (50, 350, 75, 385), "'T' of a page heading ('Time and focus')"),
    "type.listSubtitle":  ("dark/11-chats-list-search-new-chat", "cap", (145, 1065, 165, 1105), "'2' of a list row subtitle"),
    "type.sectionHeader": ("dark/13-settings-sheet-grouped", "cap", (88, 780, 112, 820), "'A' of a section header"),
    "type.toolStep":      ("dark/07-chat-thread-user-bubble-response-actions", "cap", (112, 545, 135, 590), "'C' of a tool-step row"),
    "type.pill":          ("dark/11-chats-list-search-new-chat", "cap", (582, 1515, 605, 1555), "'N' of the New chat pill"),
    "type.emptyBody":     ("dark/21-code-empty-sessions-secondary-pill", "cap", (105, 835, 128, 870), "'A' of an empty-state explanation"),
    "type.cardTitle":     ("dark/20-artifacts-list-cards", "cap", (347, 330, 372, 370), "'H' of an artifact card title"),
    "type.tileLabel":     ("dark/24-settings-app-appearance-cards", "cap", (157, 1725, 175, 1760), "'L' of an Appearance tile label"),
    "type.subtitle":      ("dark/15-capabilities-switches-on-disabled", "cap", (152, 580, 176, 620), "'A' of a setting subtitle"),
    "type.footnote":      ("dark/07-chat-thread-user-bubble-response-actions", "cap", (48, 1395, 64, 1430), "'C' of the disclaimer"),
    "type.talk":          ("dark/07-chat-thread-user-bubble-response-actions", "cap", (668, 1625, 686, 1665), "'T' of the Talk label"),
    "type.sheetSubtitle": ("dark/03-model-picker-sheet", "cap", (100, 1105, 118, 1140), "'F' of a sheet row subtitle"),
    "type.cardMeta":      ("dark/20-artifacts-list-cards", "cap", (347, 435, 372, 475), "'E' of an artifact card's date"),
    "type.badge":         ("dark/04-effort-sheet-badges", "cap", (250, 1160, 265, 1195), "'R' of a badge label"),
    "lines.response":     ("dark/07-chat-thread-user-bubble-response-actions", "lines", (48, 640, 760, 950), "Lines of the first response paragraph (serif)"),
    "lines.bubble":       ("dark/07-chat-thread-user-bubble-response-actions", "lines", (170, 318, 740, 460), "Lines in the owner's three-line bubble"),
    "lines.subtitle":     ("dark/15-capabilities-switches-on-disabled", "lines", (150, 585, 580, 725), "Four-line setting subtitle"),
    "lines.helper":       ("dark/04-effort-sheet-badges", "lines", (100, 1540, 700, 1605), "Two-line helper text under a sheet card"),
    "lines.promo":        ("dark/22-gift-sheet-illustration-primary", "lines", (85, 930, 730, 1060), "Promo sheet body, three lines"),
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
