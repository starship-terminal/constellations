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
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(HERE / "capture" / "native"))
import sample  # noqa: E402

NAME = "Telegram"  # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
SRGB = "/System/Library/ColorSync/Profiles/sRGB Profile.icc"
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)

# Captures whose .png was masked after capture (the owner's phone number, a hostname in a thumbnail).
# Their readings come from the unmasked Display P3 original, <name>.raw.png, converted to sRGB with
# the same sips call capture/native/shot.sh makes, so they read the pixels the .png held before masking.
FROM_RAW = {"09-settings-root-profile", "22-attachment-sheet-tab-bar"}

# Three screens have a different name per theme: the light chat list also shows stories, the archive
# row and a search field, so its rows sit lower; the light pass captured Auto-Night Mode for the
# checklist; and Appearance's Night Mode switch is disabled in dark and plain off in light.
CHATS = {"dark": "dark/02-chat-list-folders-tabbar", "light": "light/02-chat-list-stories-archive-folders-tabbar"}
LIST = {"dark": "dark/12-checklist-with-sticker-header", "light": "light/12-checklist-auto-night-mode"}
LOOK = {"dark": "dark/25-appearance-theme-cards-disabled-switch", "light": "light/25-appearance-theme-cards-switch-off"}

# id: (capture, op, args, note), or a list of them, one per theme. Captures without a theme prefix
# are read in both themes when the file exists in both; "dark/..." or "light/..." reads one theme only.
# PRODUCT (adapt): one entry per reading, boxes measured on this product's captures.
R = {
    # ---------------------------------------------------------------- backgrounds and surfaces
    "bg.chats":           [(CHATS["dark"], "fill", (300, 1200, 200, 200), "Chat list background below the rows"),
                           (CHATS["light"], "fill", (300, 1450, 200, 100), "Chat list background below the rows")],
    "bg.pinned":          [(CHATS["dark"], "fill", (300, 790, 300, 30), "Pinned chats band behind the top rows"),
                           (CHATS["light"], "fill", (300, 1250, 300, 30), "Pinned chats band behind the top rows")],
    "bg.grouped":         ("10-settings-notifications-switches-on-off", "fill", (100, 1110, 600, 30), "Grouped settings page, between cards"),
    "bg.groupedAlt":      ("13-chat-folders-add-pill-buttons", "fill", (100, 1490, 600, 30), "Chat Folders page, between cards (a lighter page in dark)"),
    "bg.sheet":           ("dark/22-attachment-sheet-tab-bar", "fill", (500, 690, 200, 20), "Attachment sheet, beside its title"),
    "surface.card":       ("11-settings-privacy-grouped-values", "fill", (430, 610, 150, 30), "Grouped card (Privacy and Security)"),
    "surface.cardAlt":    ("13-chat-folders-add-pill-buttons", "fill", (300, 960, 300, 30), "Grouped card on the Chat Folders page"),
    "surface.search":     ("16-contacts-list-search", "fill", (100, 310, 150, 60), "Search field (Contacts)"),
    "surface.chipBar":    [(CHATS["dark"], "fill", (600, 320, 20, 10), "Folder chip bar (glass), between two chips"),
                           (CHATS["light"], "fill", (600, 620, 20, 10), "Folder chip bar (glass), between two chips")],
    "surface.chipSelected": [(CHATS["dark"], "fill", (58, 325, 30, 25), "Selected folder chip ('All')"),
                             (CHATS["light"], "fill", (58, 625, 30, 25), "Selected folder chip ('All')")],
    "surface.glassButton": ("10-settings-notifications-switches-on-off", "fill", (60, 210, 20, 15), "Round glass back button, above its chevron"),
    "surface.tabBar":     [(CHATS["dark"], "fill", (240, 1700, 60, 12), "Tab bar (glass), between two tabs"),
                           (CHATS["light"], "fill", (240, 1700, 60, 12), "Tab bar (glass), between two tabs")],
    "surface.tabSelected": [(CHATS["dark"], "fill", (430, 1610, 40, 10), "Selected tab's pill (Chats)"),
                            (CHATS["light"], "fill", (430, 1610, 40, 10), "Selected tab's pill (Chats)")],
    "surface.segmented":  ("14-calls-segmented-all", "fill", (512, 205, 20, 50), "Segmented control track (All / Missed), right end"),
    "surface.segmentedSelected": ("14-calls-segmented-all", "fill", (282, 205, 25, 50), "Selected segment ('All'), left of its label"),
    "surface.menu":       ("05-message-context-menu-reactions", "fill", (620, 1000, 120, 60), "Context menu (glass over the blurred chat)"),
    "surface.menuSort":   ("dark/17-contacts-sort-menu", "fill", (380, 300, 80, 4), "Pull-down menu (Contacts > Sort), between its items"),
    "surface.reactions":  ("05-message-context-menu-reactions", "fill", (640, 255, 20, 20), "Reaction bar above the message"),
    "surface.bubbleIn":   [(LOOK[t], "fill", (390, 525, 120, 15), "Incoming bubble in the theme preview (Appearance)") for t in LOOK],
    "surface.bubbleOut":  ("03-chat-topics-pinned-link-preview", "fill", (690, 715, 25, 40), "Outgoing bubble, top"),
    "surface.bubbleOutEnd": ("03-chat-topics-pinned-link-preview", "fill", (650, 1400, 40, 12), "Outgoing bubble, bottom"),
    "surface.quote":      ("03-chat-topics-pinned-link-preview", "fill", (640, 895, 100, 15), "Link preview card inside an outgoing bubble"),
    "surface.service":    ("03-chat-topics-pinned-link-preview", "fill", (440, 690, 60, 8), "Service message pill ('... was created'), under its text"),
    "surface.composer":   ("03-chat-topics-pinned-link-preview", "fill", (450, 1650, 100, 20), "Composer field (glass over the wallpaper)"),
    # ---------------------------------------------------------------- borders
    "border.divider":     ("11-settings-privacy-grouped-values", "fill", (500, 442, 200, 1), "Divider between grouped rows (one pixel row)"),
    "border.dividerList": [(CHATS["dark"], "fill", (300, 535, 300, 1), "Divider between chat rows (one pixel row)"),
                           (CHATS["light"], "fill", (300, 987, 300, 1), "Divider between chat rows (one pixel row)")],
    # ---------------------------------------------------------------- text
    "text.primary":       ("11-settings-privacy-grouped-values", "text", (165, 365, 230, 45), "Row title ('Blocked Users')"),
    "text.secondary":     ("10-settings-notifications-switches-on-off", "text", (165, 470, 200, 35), "Row subtitle ('173 exceptions')"),
    "text.value":         ("11-settings-privacy-grouped-values", "text", (640, 1210, 75, 40), "Row value ('My Contacts')"),
    "text.sectionHeader": ("10-settings-notifications-switches-on-off", "text", (78, 352, 320, 30), "Section header ('MESSAGE NOTIFICATIONS')"),
    "text.footnote":      ("11-settings-privacy-grouped-values", "text", (78, 975, 600, 60), "Footnote under a card"),
    "text.chatTitle":     [(CHATS["dark"], "text", (275, 700, 120, 45), "Chat row title (a contact's name)"),
                           (CHATS["light"], "text", (275, 1155, 120, 45), "Chat row title (a contact's name)")],
    "text.chatPreview":   [(CHATS["dark"], "text", (188, 745, 180, 35), "Chat row preview line"),
                           (CHATS["light"], "text", (188, 1200, 180, 35), "Chat row preview line")],
    "text.chatTime":      [(CHATS["dark"], "text", (690, 705, 75, 35), "Chat row time ('14:53')"),
                           (CHATS["light"], "text", (725, 1160, 45, 35), "Chat row time ('Fri')")],
    "text.readMark":      [(CHATS["dark"], "text", (650, 555, 30, 30), "Read tick beside a chat row time"),
                           (CHATS["light"], "text", (650, 1010, 30, 30), "Read tick beside a chat row time")],
    "text.navTitle":      ("10-settings-notifications-switches-on-off", "text", (300, 210, 210, 45), "Navigation title ('Notifications')"),
    "text.link":          ("09-settings-root-profile", "text", (170, 660, 320, 45), "Accent action row ('Change Profile Photo')"),
    "text.online":        ("16-contacts-list-search", "text", (145, 575, 90, 30), "Presence line ('online')"),
    "text.username":      ("dark/18-search-typed-global-results", "text", (145, 410, 120, 35), "Username in search results ('@...')"),
    "text.placeholder":   ("16-contacts-list-search", "text", (375, 320, 130, 45), "Search field placeholder"),
    "text.danger":        ("24-devices-primary-button-destructive-row", "text", (165, 1105, 420, 45), "Destructive row ('Terminate all other sessions')"),
    "text.dangerMenu":    ("05-message-context-menu-reactions", "text", (450, 1495, 100, 40), "Destructive menu item ('Delete')"),
    "text.missed":        ("15-calls-segmented-missed-red", "text", (188, 305, 150, 40), "Missed call name (red)"),
    "text.onAccent":      ("24-devices-primary-button-destructive-row", "text", (345, 730, 180, 50, "light"), "Label on the accent button ('Add Device')"),
    "text.disabled":      (LOOK["dark"], "text", (78, 1350, 180, 45), "Disabled row label ('Night Mode')"),
    "text.disabledAction": ("dark/20-chat-list-edit-mode-disabled-actions", "text", (75, 1660, 150, 45), "Disabled bottom action ('Read All')"),
    "text.onBubbleOut":   ("03-chat-topics-pinned-link-preview", "text", (140, 945, 600, 30), "Text in an outgoing bubble"),
    "text.bubbleMeta":    ("03-chat-topics-pinned-link-preview", "text", (660, 1378, 55, 25), "Time inside an outgoing bubble ('23:08')"),
    "text.bubbleLink":    ("03-chat-topics-pinned-link-preview", "text", (125, 722, 330, 40), "Link in an outgoing bubble"),
    "text.quoteTitle":    ("03-chat-topics-pinned-link-preview", "text", (143, 778, 170, 30), "Site name on a link preview ('docusaurus.io')"),
    "text.service":       ("03-chat-topics-pinned-link-preview", "text", (310, 655, 230, 35, "light"), "Service message text"),
    "text.tab":           [(CHATS["dark"], "text", (285, 1670, 60, 30), "Unselected tab label ('Calls')"),
                           (CHATS["light"], "text", (285, 1670, 60, 30), "Unselected tab label ('Calls')")],
    "text.tabSelected":   [(CHATS["dark"], "text", (450, 1670, 80, 30), "Selected tab label ('Chats')"),
                           (CHATS["light"], "text", (450, 1670, 80, 30), "Selected tab label ('Chats')")],
    # ---------------------------------------------------------------- accent and controls
    "accent.button":      ("24-devices-primary-button-destructive-row", "fill", (560, 730, 150, 50), "Accent button ('Add Device')"),
    "accent.compose":     [(CHATS[t], "fill", (738, 225, 15, 20), "Compose button (round, accent glass), right of its glyph") for t in CHATS],
    "accent.send":        ("04-composer-typed-send-button", "fill", (662, 1650, 12, 14), "Send button in the composer"),
    "accent.pill":        ("13-chat-folders-add-pill-buttons", "fill", (630, 1645, 20, 20), "Small accent pill ('ADD')"),
    "accent.check":       [(LIST["dark"], "text", (712, 715, 25, 25), "Checkmark on the chosen row"),
                           (LIST["light"], "text", (95, 482, 25, 25), "Checkmark on the chosen row")],
    "accent.caret":       ("04-composer-typed-send-button", "fill", (238, 1648, 1, 38), "Text caret in the composer, one pixel column"),
    "switch.on":          ("10-settings-notifications-switches-on-off", "fill", (620, 1232, 25, 14), "Switch on (In-App Sounds)"),
    "switch.off":         ("10-settings-notifications-switches-on-off", "fill", (695, 1340, 25, 12), "Switch off track (In-App Vibrate)"),
    "switch.thumb":       ("10-settings-notifications-switches-on-off", "fill", (630, 1340, 40, 12), "Switch thumb"),
    "switch.offDisabled": (LOOK["dark"], "fill", (700, 1365, 25, 10), "Switch off and disabled (Night Mode)"),
    "switch.thumbDisabled": (LOOK["dark"], "fill", (630, 1365, 30, 10), "Thumb of the disabled switch"),
    "badge.count":        [(CHATS["dark"], "fill", (729, 326, 7, 6), "Count badge on a folder chip ('19'), muted"),
                           (CHATS["light"], "fill", (700, 772, 12, 12), "Count badge on the archive row ('109'), muted")],
    "icon.secondary":     [(CHATS["dark"], "text", (725, 460, 40, 40), "Pin glyph on a pinned chat row"),
                           (CHATS["light"], "text", (725, 915, 40, 40), "Pin glyph on a pinned chat row")],
    # ---------------------------------------------------------------- core palettes (dark captures)
    "tile.blue":          ("dark/10-settings-notifications-switches-on-off", "fill", (80, 468, 10, 3), "Settings icon tile (a gradient), blue (Private Chats)"),
    "tile.green":         ("dark/10-settings-notifications-switches-on-off", "fill", (80, 612, 10, 3), "Settings icon tile (a gradient), green (Group Chats)"),
    "tile.orange":        ("dark/10-settings-notifications-switches-on-off", "fill", (80, 757, 10, 3), "Settings icon tile (a gradient), orange (Channels)"),
    "tile.violet":        ("dark/10-settings-notifications-switches-on-off", "fill", (80, 880, 10, 3), "Settings icon tile (a gradient), violet (Stories)"),
    "tile.pink":          ("dark/10-settings-notifications-switches-on-off", "fill", (80, 1005, 10, 3), "Settings icon tile (a gradient), pink (Reactions)"),
    "tile.red":           ("dark/11-settings-privacy-grouped-values", "fill", (80, 390, 10, 3), "Settings icon tile (a gradient), red (Blocked Users)"),
    "tile.purple":        ("dark/11-settings-privacy-grouped-values", "fill", (80, 910, 10, 3), "Settings icon tile (a gradient), purple (Auto-Delete Messages)"),
    "tile.grey":          ("dark/09-settings-root-profile", "fill", (85, 1555, 10, 3), "Settings icon tile (a gradient), grey (Privacy and Security)"),
    "avatar.red":         ("dark/18-search-typed-global-results", "fill", (52, 697, 10, 3), "Initials avatar, red ('N'), left of the letter"),
    "avatar.purple":      ("dark/18-search-typed-global-results", "fill", (52, 797, 10, 3), "Initials avatar, purple ('S'), left of the letter"),
    "avatar.blue":        ("dark/21-new-message-sheet-index", "fill", (52, 987, 10, 3), "Initials avatar, blue ('A'), left of the letter"),
    "avatar.green":       ("dark/14-calls-segmented-all", "fill", (92, 613, 10, 3), "Initials avatar, green ('M'), left of the letter"),
    "avatar.orange":      ("dark/23-folder-chip-selected-os", "fill", (58, 765, 10, 3), "Initials avatar, orange-red ('A'), left of the letter"),
    # ---------------------------------------------------------------- sizes
    "rows.grouped":       [("dark/11-settings-privacy-grouped-values", "find", ("col", 560, 330, 970, (43, 43, 45), 3), "Dividers down a card of one-line rows"),
                           ("light/11-settings-privacy-grouped-values", "find", ("col", 560, 330, 970, (228, 228, 228), 3), "Dividers down a card of one-line rows")],
    "rows.groupedTwoLine": [("dark/10-settings-notifications-switches-on-off", "find", ("col", 560, 390, 1080, (46, 46, 48), 3), "Dividers down a card of two-line rows"),
                            ("light/10-settings-notifications-switches-on-off", "find", ("col", 560, 390, 1080, (224, 224, 224), 3), "Dividers down a card of two-line rows")],
    "rows.chats":         [(CHATS["dark"], "find", ("col", 300, 520, 850, (46, 46, 48), 3), "Dividers down the chat list (text pixels of the same grey included)"),
                           (CHATS["light"], "find", ("col", 300, 830, 1300, (220, 220, 220), 3), "Dividers down the chat list (text pixels of the same grey included)")],
    "rows.calls":         ("dark/14-calls-segmented-all", "find", ("col", 560, 540, 1000, (26, 26, 26), 2), "Dividers down the calls list"),
    "rows.contacts":      ("dark/16-contacts-list-search", "find", ("col", 600, 500, 960, (26, 26, 26), 3), "Dividers down the contacts list"),
    "size.navButton.w":   ("10-settings-notifications-switches-on-off", "extent", ("row", 233, 30, 200, (32, 233), 8), "Round glass back button, width"),
    "size.navButton.h":   ("10-settings-notifications-switches-on-off", "extent", ("col", 90, 160, 320, (90, 165), 8), "Round glass back button, height"),
    "size.search.h":      ("16-contacts-list-search", "extent", ("col", 150, 270, 420, (150, 285), 3), "Search field height"),
    "size.chipBar.h":     ("dark/02-chat-list-folders-tabbar", "extent", ("col", 400, 285, 395, (400, 290), 8), "Folder chip bar height"),
    "size.chipSelected":  ("dark/02-chat-list-folders-tabbar", "bbox", ((70, 338), (49, 302, 110, 72), 6), "Selected folder chip ('All')"),
    "size.tabBar.h":      ("dark/02-chat-list-folders-tabbar", "extent", ("col", 150, 1570, 1760, (150, 1580), 8), "Tab bar height"),
    "size.tabBar.w":      ("dark/02-chat-list-folders-tabbar", "extent", ("row", 1660, 20, 790, (30, 1660), 8), "Tab bar width"),
    "size.tabSelected.w": ("dark/02-chat-list-folders-tabbar", "extent", ("row", 1660, 380, 600, (390, 1660), 12), "Selected tab pill width"),
    "size.tabSelected.h": ("dark/02-chat-list-folders-tabbar", "extent", ("col", 487, 1600, 1719, (487, 1602), 12), "Selected tab pill height"),
    "size.segmented":     ("dark/14-calls-segmented-all", "extent", ("row", 233, 255, 560, (258, 233), 8), "Segmented control width"),
    "size.segmented.h":   ("dark/14-calls-segmented-all", "extent", ("col", 520, 175, 290, (520, 180), 8), "Segmented control height"),
    "size.button":        ("24-devices-primary-button-destructive-row", "bbox", ((600, 755), (30, 690, 760, 140), 24), "Full-width accent button"),
    "size.pill":          ("13-chat-folders-add-pill-buttons", "bbox", ((630, 1655), (590, 1610, 190, 100), 24), "Small accent pill ('ADD')"),
    "size.switch":        ("dark/10-settings-notifications-switches-on-off", "bbox", ((620, 1240), (590, 1200, 170, 90), 12), "Switch track (on)"),
    "size.switchThumb":   ("dark/10-settings-notifications-switches-on-off", "bbox", ((640, 1345), (600, 1320, 140, 50), 10), "Switch thumb (off)"),
    "size.iconTile":      ("dark/10-settings-notifications-switches-on-off", "extent", ("col", 90, 420, 520, (90, 425), 10), "Settings icon tile"),
    "size.avatarChat":    ("dark/02-chat-list-folders-tabbar", "extent", ("col", 100, 690, 838, (100, 695), 10), "Chat list avatar"),
    "size.avatarList":    ("dark/14-calls-segmented-all", "extent", ("row", 615, 60, 200, (65, 615), 12), "Calls list avatar"),
    "size.avatarContact": ("dark/16-contacts-list-search", "extent", ("col", 100, 625, 740, (100, 630), 12), "Contacts list avatar"),
    "size.send":          ("dark/04-composer-typed-send-button", "bbox", ((668, 1650), (630, 1600, 140, 140), 40), "Send button in the composer"),
    # ---------------------------------------------------------------- radii
    "radius.card":        ("11-settings-privacy-grouped-values", "diag", (400, 360, 60, 700), "Grouped card"),
    "radius.cardAlt":     ("13-chat-folders-add-pill-buttons", "diag", (400, 720, 60, 980), "Grouped card on the Chat Folders page"),
    "radius.search":      ("16-contacts-list-search", "diag", (300, 320, 120, 342), "Search field (capsule)"),
    "radius.button":      ("24-devices-primary-button-destructive-row", "diag", (300, 730, 80, 757), "Accent button (capsule)"),
    "radius.tabBar":      ("dark/02-chat-list-folders-tabbar", "diag", (300, 1612, 75, 1662), "Tab bar (capsule)"),
    "radius.bubble":      ("03-chat-topics-pinned-link-preview", "diag", (600, 718, 112, 900), "Outgoing bubble, top-left corner"),
    "radius.iconTile":    ("dark/10-settings-notifications-switches-on-off", "diag", (105, 448, 82, 470), "Settings icon tile"),
    "radius.menu":        ("05-message-context-menu-reactions", "diag", (600, 980, 345, 1065), "Context menu (glass)"),
    "radius.sheet":       ("dark/22-attachment-sheet-tab-bar", "diag", (400, 650, 40, 700), "Attachment sheet, top-left corner"),
    # ---------------------------------------------------------------- type (cap heights, dark)
    "type.navTitle":      ("dark/10-settings-notifications-switches-on-off", "cap", (303, 205, 332, 260), "'N' of a navigation title"),
    "type.rowTitle":      ("dark/11-settings-privacy-grouped-values", "cap", (165, 365, 186, 415), "'B' of a row title"),
    "type.rowSubtitle":   ("dark/10-settings-notifications-switches-on-off", "cap", (165, 1005, 192, 1045), "'M' of a row subtitle ('Messages, Stories')"),
    "type.sectionHeader": ("dark/10-settings-notifications-switches-on-off", "cap", (78, 350, 98, 385), "'M' of a section header"),
    "type.footnote":      ("dark/11-settings-privacy-grouped-values", "cap", (78, 972, 98, 1005), "'A' of a footnote"),
    "type.chatTitle":     ("dark/02-chat-list-folders-tabbar", "cap", (275, 700, 300, 745), "'H' of a chat row title"),
    "type.chatPreview":   ("dark/02-chat-list-folders-tabbar", "cap", (188, 595, 210, 635), "'Y' of a chat row preview"),
    "type.button":        ("dark/24-devices-primary-button-destructive-row", "cap", (345, 730, 372, 780), "'A' of 'Add Device'"),
    "type.tab":           ("dark/02-chat-list-folders-tabbar", "cap", (288, 1668, 304, 1700), "'C' of a tab label"),
    "type.chip":          ("dark/02-chat-list-folders-tabbar", "cap", (88, 318, 112, 360), "'A' of a folder chip"),
    "type.bubble":        (LOOK["dark"], "cap", (86, 520, 112, 565), "'D' of bubble text (Appearance preview)"),
    "type.quote":         ("dark/03-chat-topics-pinned-link-preview", "cap", (143, 878, 167, 915), "'A' of a link preview's description"),
    "type.bubbleMeta":    ("dark/03-chat-topics-pinned-link-preview", "cap", (664, 1378, 677, 1403), "'2' of a bubble time"),
    "type.segmented":     ("dark/14-calls-segmented-all", "cap", (300, 210, 325, 255), "'A' of a segment label"),
    "type.menuItem":      ("dark/05-message-context-menu-reactions", "cap", (450, 990, 474, 1040), "'R' of a menu item"),
    "type.profileName":   ("dark/09-settings-root-profile", "cap", (342, 440, 362, 495), "'k' of the profile name (ascender height)"),
    "lines.footnote":     ("dark/11-settings-privacy-grouped-values", "lines", (78, 970, 700, 1040), "Two-line footnote"),
    "lines.quote":        ("dark/03-chat-topics-pinned-link-preview", "lines", (140, 880, 740, 1015), "Lines of a link preview's description"),
    "lines.chatPreview":  ("dark/02-chat-list-folders-tabbar", "lines", (230, 440, 700, 515), "Two-line chat row preview"),
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


def load(raw, theme, name):
    """The capture's rows. A masked capture is read from its unmasked original (FROM_RAW)."""
    png = raw / theme / f"{name}.png"
    if name not in FROM_RAW:
        return sample.read_png(png)[2]
    original = raw / theme / f"{name}.raw.png"
    if not original.exists():
        raise SystemExit(f"{original}: the unmasked original of a masked capture is missing; nothing written")
    with tempfile.TemporaryDirectory() as tmp:
        out = pathlib.Path(tmp) / f"{name}.png"
        subprocess.run(["sips", "--matchTo", SRGB, str(original), "--out", str(out)],
                       check=True, capture_output=True)
        return sample.read_png(out)[2]


def run(raw):
    raw = pathlib.Path(raw).expanduser()
    if not (raw / "dark").is_dir():
        raise SystemExit(f"{raw}: no dark/ captures; nothing written")
    pending, out = {}, {}
    for rid, entries in R.items():
        for cap, op, args, note in entries if isinstance(entries, list) else [entries]:
            themes = [cap.split("/")[0]] if "/" in cap else ["dark", "light"]
            name = cap.split("/")[-1]
            for theme in themes:
                if not (raw / theme / f"{name}.png").exists():
                    continue
                pending.setdefault(f"{theme}/{name}", []).append((rid, op, args, note))
    # One decoded capture at a time: a decoded capture is several hundred MB as Python tuples, so
    # the readings are grouped by capture and each image is released before the next is read.
    for key in sorted(pending):
        theme, name = key.split("/")
        rows = load(raw, theme, name)
        for rid, op, args, note in pending[key]:
            if op == "fill":
                res = op_fill(rows, *args)
            elif op == "text":
                res = op_text(rows, *args, dark=(theme == "dark"))
            else:
                res = globals()["op_" + op](rows, *args)
            res.update({"capture": f"screenshots/{theme}/{name}.png", "op": op,
                        "args": json.loads(json.dumps(args)), "note": note})
            if name in FROM_RAW:
                res["readFrom"] = f"{name}.raw.png, converted to sRGB (the .png is masked)"
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
