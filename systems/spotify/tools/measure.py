#!/usr/bin/env python3
"""Read Spotify's values out of the full-colour iPhone Mirroring captures (native kit).

    python3 tools/measure.py ~/.design-systems/spotify/raw-shots

Copied from systems/grokbot through tools/kit/native/. Adapted here: NAME, THEMES, the reading
table R, whose boxes are capture pixels on Spotify's screens, and one op, diagr (diag mirrored for
a top-right corner, because Spotify's tiles and cards hold artwork at their top-left).

RAW holds dark/ sRGB captures only: Spotify for iOS has no light theme. The captures are 812 x 1780
px, the 390 x 844 pt screen at 2 px per pt, offset 16, 76 inside the PNG, as written by
tools/capture/native/shot.sh. Writes raw/readings.json (every reading with its file, box, method,
value and evidence label) and raw/<slug>-measured.md (the same as tables). tools/build_tokens.py
reads only raw/readings.json.

Each reading is one of:
  fill    the dominant colour of a box and its share of the box            Sampled when share >= 90%
  text    the anti-aliased pixel furthest from the fill (a glyph colour)    Sampled (text)
  bbox    the bounding box of pixels close to the colour at a point,
          inside a window: a control's width and height in pt             Sampled
  extent  first and last pixel along a line that differs from a
          background point: the size of a glass control                    Sampled
  find    positions along a line whose colour is close to a reference      Sampled
  diag    corner radius from the inset along the corner's diagonal        Derived (about +-2 pt)
  diagr   the same for a top-right corner                                  Derived (about +-2 pt)
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

NAME = "Spotify"   # PRODUCT (adapt): the product name in the generated tables
SLUG = PKG.name    # the package folder
SCALE = 2          # px per pt
CAP_EM = 0.72      # cap height assumed for font sizes (the family is not known)
THEMES = ("dark",)  # Spotify for iOS has no light theme

# id: (capture, op, args, note). Every capture is read in dark, the only theme.
# PRODUCT (adapt): one entry per reading, boxes measured on Spotify's captures.
R = {
    # ---------------------------------------------------------------- surfaces
    "bg.page":            ("02-home", "fill", (450, 1195, 200, 10), "Home background, between sections"),
    "bg.drawer":          ("19-profile-drawer", "fill", (560, 940, 100, 30), "Profile drawer background"),
    "surface.tile":       ("02-home", "fill", (350, 290, 30, 50), "Home shortcut tile, right of its title"),
    "surface.card":       ("02-home", "fill", (400, 1030, 100, 20), "Promo card (Upcoming release)"),
    "surface.settingsTile": ("20-settings", "fill", (220, 300, 40, 10), "Settings quick tile (Data Saver mode)"),
    "surface.drawerCard": ("19-profile-drawer", "fill", (500, 230, 100, 15), "Account card in the profile drawer"),
    "surface.notice":     ("19-profile-drawer", "fill", (600, 1300, 20, 20), "Push-notification card in the drawer"),
    "surface.glass":      ("20-settings", "fill", (55, 205, 12, 12), "Round glass back button, centre"),
    "surface.chip":       ("10-library", "fill", (55, 300, 6, 20), "Library filter chip (glass), left of its label"),
    "surface.field":      ("05-search", "fill", (300, 300, 200, 10), "Search field, resting"),
    "surface.fieldFocused": ("07-search-focused-recents", "fill", (560, 205, 40, 15), "Focused search field (glass), right of the placeholder"),
    "surface.sheet":      ("24-artist-context-sheet", "fill", (450, 1300, 100, 20), "Context sheet (glass) over the artist page"),
    "surface.sheetSort":  ("12-sort-sheet", "fill", (500, 1180, 80, 20), "Sort sheet (glass) over Your Library"),
    "surface.shareSheet": ("14-share-sheet", "fill", (400, 1680, 200, 20), "Share sheet (glass), bottom"),
    "surface.shareTarget": ("14-share-sheet", "fill", (70, 1250, 10, 10), "Round share target (Search), left of its icon"),
    "surface.segmented":  ("18-share-song-segmented", "fill", (500, 1000, 8, 15), "Segmented control track, right of 'Lyrics'"),
    "surface.miniPlayer": ("02-home", "fill", (300, 1460, 10, 10), "Mini player, tinted from the playing track's artwork"),
    "scrim.ref":          ("10-library", "fill", (300, 600, 20, 20), "Your Library between rows, undimmed"),
    "scrim.sort":         ("12-sort-sheet", "fill", (300, 600, 20, 20), "The same spot under the sort sheet's scrim"),
    "scrim.shareRef":     ("10-library", "fill", (550, 180, 20, 20), "Your Library header, undimmed"),
    "scrim.share":        ("14-share-sheet", "fill", (550, 180, 20, 20), "The same spot under the share sheet's scrim"),
    "scrim.contextRef":   ("23-artist-tabs-following", "fill", (600, 785, 20, 10), "Artist page below the header, undimmed"),
    "scrim.context":      ("24-artist-context-sheet", "fill", (600, 785, 20, 10), "The same spot under the context sheet's scrim"),
    "border.divider":     ("21-settings-playback-switches-slider", "fill", (300, 927, 300, 1), "Section divider in Playback (one pixel row)"),
    "border.sheetDivider": ("24-artist-context-sheet", "fill", (300, 958, 300, 1), "Divider under a context sheet's header"),
    "border.drawerDivider": ("19-profile-drawer", "fill", (300, 344, 300, 1), "Divider inside the drawer's account card"),
    "border.outline":     ("23-artist-tabs-following", "text", (158, 875, 12, 30), "Following pill outline (1 pt, anti-aliased)"),
    "border.grabber":     ("12-sort-sheet", "fill", (380, 1118, 40, 2), "Sheet grabber"),
    # ---------------------------------------------------------------- text
    "text.primary":       ("10-library", "text", (200, 495, 270, 40), "Library row title"),
    "text.secondary":     ("10-library", "text", (264, 540, 190, 30), "Library row subtitle"),
    "text.searchSubtitle": ("07-search-focused-recents", "text", (168, 418, 260, 35), "Recent search subtitle"),
    "text.settingsSubtitle": ("20-settings", "text", (112, 525, 430, 35), "Settings row subtitle"),
    "text.eyebrow":       ("02-home", "text", (376, 905, 40, 30), "Promo card eyebrow ('EP')"),
    "text.chevron":       ("20-settings", "text", (745, 490, 25, 45), "Settings row chevron"),
    "text.listeners":     ("23-artist-tabs-following", "text", (48, 795, 250, 35), "Monthly listeners line"),
    "text.tertiary":      ("10-library", "text", (200, 1340, 140, 30), "DJ row subtitle ('Tap to start')"),
    "text.tabActive":     ("02-home", "text", (80, 1625, 70, 35), "Tab bar label, current tab"),
    "text.tabInactive":   ("02-home", "text", (270, 1625, 80, 35), "Tab bar label, other tabs"),
    "text.pageTabInactive": ("23-artist-tabs-following", "text", (185, 965, 90, 45), "Artist page tab, not selected ('Video')"),
    "text.sheetHeader":   ("12-sort-sheet", "text", (78, 1155, 90, 30), "Sort sheet header ('Sort by'), on glass"),
    "text.cancel":        ("12-sort-sheet", "text", (355, 1620, 100, 40), "Sort sheet Cancel, on glass"),
    "text.placeholder":   ("05-search", "text", (145, 320, 440, 40, "dark"), "Search field placeholder, on white"),
    "text.placeholderFocused": ("07-search-focused-recents", "text", (80, 200, 430, 40), "Focused search field placeholder"),
    "text.accent":        ("20-settings", "text", (70, 365, 175, 35), "Green label on an active settings tile"),
    "text.accentOnSheet": ("12-sort-sheet", "text", (78, 1235, 115, 40), "Selected sort option ('Recents'), on glass"),
    "text.checkOnSheet":  ("12-sort-sheet", "text", (690, 1230, 45, 40), "Tick beside the selected sort option"),
    "text.onAccent":      ("11-library-chip-selected", "text", (160, 300, 100, 30, "dark"), "Label on the selected green chip"),
    "text.onInverse":     ("02-home", "text", (550, 1095, 110, 40, "dark"), "'Pre-save' label on the white pill"),
    "text.onSegmented":   ("18-share-song-segmented", "text", (310, 1000, 80, 45, "dark"), "'Song' on the selected segment"),
    "text.onFamily":      ("19-profile-drawer", "text", (588, 490, 80, 35, "dark"), "'Family' on the plan badge"),
    "text.onBeta":        ("24-artist-context-sheet", "text", (405, 1655, 45, 35, "dark"), "'Beta' on its green tag"),
    "text.onPlay":        ("23-artist-tabs-following", "text", (690, 870, 50, 45, "dark"), "Play glyph on the green button"),
    "text.miniTitle":     ("02-home", "text", (140, 1455, 100, 35), "Mini player track title"),
    "text.miniArtist":    ("02-home", "text", (140, 1495, 200, 35), "Mini player artist line"),
    # ---------------------------------------------------------------- accent and controls
    "accent.green":       ("11-library-chip-selected", "fill", (140, 300, 12, 30), "Selected filter chip (Playlists)"),
    "accent.chipHome":    ("02-home", "fill", (146, 200, 8, 40), "Selected home chip (All)"),
    "accent.play":        ("23-artist-tabs-following", "fill", (715, 850, 10, 10), "Play button"),
    "accent.like":        ("02-home", "fill", (613, 1488, 5, 10), "Saved (liked) tick in the mini player"),
    "accent.pin":         ("10-library", "fill", (210, 552, 3, 3), "Pin icon in a library row"),
    "accent.caret":       ("07-search-focused-recents", "fill", (73, 205, 2, 30), "Text caret, two pixel columns"),
    "accent.tabIndicator": ("23-artist-tabs-following", "fill", (60, 1017, 60, 2), "Underline under the selected artist tab"),
    "accent.slider":      ("21-settings-playback-switches-slider", "fill", (140, 865, 60, 1), "Slider, filled part"),
    "accent.dot":         ("19-profile-drawer", "fill", (676, 790, 4, 4), "Unread dot (Your Updates)"),
    "badge.family":       ("19-profile-drawer", "fill", (575, 485, 6, 35), "Plan badge ('Family')"),
    "badge.beta":         ("24-artist-context-sheet", "fill", (399, 1660, 5, 20), "'Beta' tag"),
    "button.inverse":     ("02-home", "fill", (525, 1095, 30, 10), "'Pre-save' pill"),
    "button.notice":      ("19-profile-drawer", "fill", (440, 1320, 10, 10), "'Turn on' pill"),
    "segmented.selected": ("18-share-song-segmented", "fill", (298, 1000, 10, 30), "Selected segment ('Song')"),
    "switch.on":          ("21-settings-playback-switches-slider", "fill", (655, 460, 15, 15), "Switch on, track"),
    "switch.thumb":       ("21-settings-playback-switches-slider", "fill", (720, 465, 20, 6), "Switch on, thumb"),
    "switch.off":         ("22-settings-switch-off", "fill", (735, 1330, 20, 10), "Switch off, track (Mono audio)"),
    "switch.thumbOff":    ("22-settings-switch-off", "fill", (680, 1333, 15, 4), "Switch off, thumb (shaded)"),
    "slider.track":       ("21-settings-playback-switches-slider", "fill", (500, 865, 100, 1), "Slider, empty part"),
    "slider.thumb":       ("21-settings-playback-switches-slider", "fill", (224, 860, 8, 10), "Slider thumb"),
    # ---------------------------------------------------------------- browse category palette (Search)
    **{f"category.{k}": ("06-search-grid", "fill", box, f"Browse tile '{label}'")
       for k, label, box in [("music", "Music", (100, 480, 100, 40)), ("podcasts", "Podcasts", (470, 480, 100, 40)),
                             ("liveEvents", "Live Events", (100, 720, 100, 40)), ("fitness", "Fitness", (470, 720, 100, 40)),
                             ("madeForYou", "Made For You", (100, 960, 100, 40)), ("upcoming", "Upcoming releases", (470, 1010, 100, 40)),
                             ("newReleases", "New Releases", (100, 1200, 100, 40)), ("playlisting", "The Art of Playlisting", (470, 1250, 100, 40))]},
    # ---------------------------------------------------------------- sizes
    "size.chip":          ("11-library-chip-selected", "bbox", ((140, 300), (115, 270, 200, 90), 14), "Selected filter chip (Playlists)"),
    "size.chipHome":      ("02-home", "bbox", ((150, 200), (125, 175, 110, 90), 14), "Selected home chip (All)"),
    "size.chipGlass.w":   ("10-library", "extent", ("row", 300, 30, 216, (30, 300), 8), "Glass filter chip width (Playlists)"),
    "size.chipGlass.h":   ("10-library", "extent", ("col", 150, 265, 365, (150, 265), 8), "Glass filter chip height"),
    "size.shortcut.w":    ("02-home", "extent", ("row", 340, 30, 405, (30, 340), 8), "Home shortcut tile width"),
    "size.shortcut.h":    ("02-home", "extent", ("col", 380, 255, 375, (380, 255), 8), "Home shortcut tile height"),
    "size.category":      ("06-search-grid", "bbox", ((100, 480), (30, 380, 390, 260), 4), "Browse category tile (Music)"),
    "size.card.w":        ("02-home", "extent", ("row", 1050, 30, 790, (30, 1050), 8), "Promo card width"),
    "size.card.h":        ("02-home", "extent", ("col", 700, 860, 1190, (700, 860), 8), "Promo card height"),
    "size.pill":          ("02-home", "bbox", ((530, 1100), (500, 1070, 250, 90), 8), "'Pre-save' pill"),
    "size.miniPlayer":    ("02-home", "bbox", ((300, 1460), (20, 1420, 780, 140), 8), "Mini player, without its progress line"),
    "size.miniPlayer.h":  ("02-home", "extent", ("col", 400, 1425, 1560, (400, 1560), 8), "Mini player height with its progress line"),
    "size.miniArt":       ("02-home", "extent", ("row", 1490, 40, 140, (40, 1490), 30), "Mini player artwork"),
    "size.like":          ("02-home", "bbox", ((614, 1497), (590, 1460, 80, 70), 14), "Saved tick (a filled circle)"),
    "size.searchField":   ("05-search", "bbox", ((300, 300), (30, 270, 760, 140), 6), "Search field, resting"),
    "size.fieldFocused.w": ("07-search-focused-recents", "extent", ("row", 205, 30, 662, (30, 205), 6), "Focused search field width"),
    "size.fieldFocused.h": ("07-search-focused-recents", "extent", ("col", 560, 170, 265, (560, 170), 6), "Focused search field height"),
    "size.cancel.w":      ("07-search-focused-recents", "extent", ("row", 205, 662, 790, (662, 205), 6), "Cancel button width (glass)"),
    "size.cancel.h":      ("07-search-focused-recents", "extent", ("col", 760, 170, 265, (760, 170), 6), "Cancel button height (glass)"),
    "size.artLibrary":    ("10-library", "extent", ("col", 60, 450, 610, (60, 450), 12), "Library row artwork, first row"),
    "size.artLibrary2":   ("10-library", "extent", ("col", 60, 610, 770, (60, 610), 12), "Library row artwork, second row"),
    "size.artSearch":     ("09-search-results-rows", "extent", ("col", 60, 270, 400, (60, 270), 12), "Search result artwork, first row"),
    "size.artSearch2":    ("09-search-results-rows", "extent", ("col", 60, 400, 525, (60, 400), 12), "Search result artwork, second row"),
    "size.navButton.w":   ("20-settings", "extent", ("row", 214, 30, 150, (30, 214), 12), "Round glass back button, width"),
    "size.navButton.h":   ("20-settings", "extent", ("col", 92, 150, 275, (92, 150), 12), "Round glass back button, height"),
    "size.settingsTile":  ("20-settings", "bbox", ((60, 305), (30, 280, 255, 170), 3), "Settings quick tile (the window stops before the second tile)"),
    "size.switch":        ("21-settings-playback-switches-slider", "bbox", ((655, 460), (620, 420, 170, 100), 14), "Switch track"),
    "size.switchThumb":   ("21-settings-playback-switches-slider", "bbox", ((720, 465), (680, 430, 100, 80), 30), "Switch thumb"),
    "size.sliderTrack":   ("21-settings-playback-switches-slider", "extent", ("col", 500, 850, 880, (500, 850), 20), "Slider track thickness"),
    "size.sliderThumb":   ("21-settings-playback-switches-slider", "bbox", ((228, 865), (200, 835, 60, 60), 30), "Slider thumb"),
    "size.following.w":   ("23-artist-tabs-following", "extent", ("row", 892, 150, 360, (150, 892), 20), "Following pill width"),
    "size.following.h":   ("23-artist-tabs-following", "extent", ("col", 180, 840, 940, (180, 840), 20), "Following pill height"),
    "size.play":          ("23-artist-tabs-following", "bbox", ((715, 850), (650, 830, 130, 130), 14), "Play button"),
    "size.tabIndicator.w": ("23-artist-tabs-following", "extent", ("row", 1017, 40, 145, (40, 1017), 20), "Selected tab underline, width"),
    "size.tabIndicator.h": ("23-artist-tabs-following", "extent", ("col", 90, 1005, 1025, (90, 1005), 20), "Selected tab underline, thickness"),
    "size.segmented.w":   ("18-share-song-segmented", "extent", ("row", 1020, 280, 530, (280, 1020), 12), "Segmented control width"),
    "size.segmented.h":   ("18-share-song-segmented", "extent", ("col", 470, 970, 1070, (470, 970), 12), "Segmented control height"),
    "size.segmentedSelected": ("18-share-song-segmented", "bbox", ((300, 1020), (285, 975, 140, 90), 10), "Selected segment"),
    "size.shareTarget":   ("18-share-song-segmented", "bbox", ((60, 1260), (40, 1205, 130, 130), 6), "Round share target"),
    "size.grabber.w":     ("12-sort-sheet", "extent", ("row", 1118, 330, 480, (330, 1118), 30), "Sheet grabber width"),
    "size.grabber.h":     ("12-sort-sheet", "extent", ("col", 400, 1105, 1130, (400, 1108), 30), "Sheet grabber height"),
    "size.noticeButton":  ("19-profile-drawer", "bbox", ((440, 1320), (400, 1300, 220, 100), 8), "'Turn on' pill"),
    "size.family":        ("19-profile-drawer", "bbox", ((575, 490), (555, 470, 150, 75), 14), "Plan badge"),
    "size.dot":           ("19-profile-drawer", "bbox", ((678, 792), (660, 775, 40, 40), 40), "Unread dot"),
    "size.beta":          ("24-artist-context-sheet", "bbox", ((400, 1660), (390, 1640, 80, 60), 14), "'Beta' tag"),
    "size.avatarHeader":  ("10-library", "extent", ("row", 218, 30, 125, (30, 218), 12), "Account avatar in a page header"),
    "size.avatarDrawer":  ("19-profile-drawer", "extent", ("row", 280, 40, 160, (40, 280), 12), "Account avatar in the drawer"),
    "size.drawerEdge":    ("19-profile-drawer", "extent", ("row", 960, 20, 800, (300, 960), 6), "Where the drawer ends and the page behind it shows"),
    # ---------------------------------------------------------------- radii
    "radius.category":    ("06-search-grid", "diag", (200, 420, 100, 550), "Browse category tile"),
    "radius.field":       ("05-search", "diag", (300, 300, 60, 338), "Search field"),
    "radius.miniPlayer":  ("02-home", "diag", (300, 1460, 40, 1475), "Mini player"),
    "radius.settingsTile": ("20-settings", "diag", (220, 305, 50, 380), "Settings quick tile"),
    "radius.drawerCard":  ("19-profile-drawer", "diag", (500, 230, 40, 280), "Account card in the drawer"),
    "radius.notice":      ("19-profile-drawer", "diag", (300, 1295, 40, 1350), "Notification card in the drawer"),
    "radius.sheet":       ("24-artist-context-sheet", "diag", (300, 850, 50, 1000), "Context sheet, top corner"),
    "radius.tile":        ("02-home", "diagr", (380, 300, 390, 330), "Home shortcut tile, top-right corner"),
    "radius.card":        ("02-home", "diagr", (700, 900, 755, 1000), "Promo card, top-right corner"),
    # ---------------------------------------------------------------- type (cap heights)
    "type.display":       ("23-artist-tabs-following", "cap", (45, 600, 71, 690), "'I' of the artist name over the header photo"),
    "type.pageTitle":     ("10-library", "cap", (125, 185, 182, 255), "'Y' of 'Your Library'"),
    "type.sectionTitle":  ("02-home", "cap", (45, 1220, 76, 1275), "'I' of a home section title"),
    "type.sectionTitle2": ("07-search-focused-recents", "cap", (45, 290, 82, 345), "'R' of 'Recent searches'"),
    "type.drawerSection": ("19-profile-drawer", "cap", (45, 1215, 83, 1260), "'M' of 'Messages' in the drawer"),
    "type.navTitle":      ("21-settings-playback-switches-slider", "cap", (335, 190, 360, 240), "'P' of the nav title 'Playback'"),
    "type.rowTitle":      ("10-library", "cap", (195, 490, 219, 535), "'T' of a library row title"),
    "type.settingsRow":   ("20-settings", "cap", (108, 470, 140, 515), "'A' of a settings row ('Account')"),
    "type.settingsRow3":  ("20-settings", "cap", (108, 705, 134, 760), "'P' of the third settings row ('Privacy and social')"),
    "type.searchPlaceholder": ("05-search", "cap", (140, 320, 176, 358), "'W' of the search placeholder"),
    "type.drawerRow":     ("19-profile-drawer", "cap", (115, 485, 150, 525), "'Y' of a drawer row ('Your Premium')"),
    "type.category":      ("06-search-grid", "cap", (60, 415, 92, 455), "'M' of a browse tile title"),
    "type.tab":           ("23-artist-tabs-following", "cap", (45, 965, 76, 1000), "'M' of the selected artist tab"),
    "type.segmented":     ("18-share-song-segmented", "cap", (425, 1005, 446, 1040), "'L' of 'Lyrics' in the segmented control"),
    "type.sheetItem":     ("24-artist-context-sheet", "cap", (128, 1115, 155, 1158), "'R' of a context sheet item ('Report')"),
    "type.sortItem":      ("12-sort-sheet", "cap", (74, 1305, 97, 1345), "'R' of a sort option"),
    "type.subtitle":      ("10-library", "cap", (260, 535, 280, 575), "'P' of a library row subtitle"),
    "type.chip":          ("10-library", "cap", (75, 295, 96, 335), "'P' of a chip label"),
    "type.tileTitle":     ("02-home", "cap", (155, 300, 181, 340), "'L' of a home shortcut tile title"),
    "type.button":        ("02-home", "cap", (548, 1095, 570, 1135), "'P' of 'Pre-save'"),
    "type.buttonOutline": ("23-artist-tabs-following", "cap", (192, 872, 216, 912), "'F' of 'Following'"),
    "type.eyebrow":       ("02-home", "cap", (372, 900, 392, 935), "'E' of the promo card eyebrow"),
    "type.cardTitle":     ("02-home", "cap", (372, 935, 396, 975), "'A' of the promo card title"),
    "type.miniPlayer":    ("02-home", "cap", (142, 1490, 166, 1525), "'M' of the mini player artist line"),
    "type.badgeFamily":   ("19-profile-drawer", "cap", (584, 490, 607, 525), "'F' of the plan badge"),
    "type.sheetHeader":   ("12-sort-sheet", "cap", (74, 1150, 93, 1185), "'S' of 'Sort by'"),
    "type.settingsTile":  ("20-settings", "cap", (578, 365, 596, 395), "'P' of a settings tile label"),
    "type.badge":         ("24-artist-context-sheet", "cap", (403, 1658, 421, 1688), "'B' of the 'Beta' tag"),
    "type.tabLabel":      ("02-home", "cap", (80, 1630, 99, 1660), "'H' of a tab bar label"),
    "lines.settingsSubtitle": ("21-settings-playback-switches-slider", "lines", (48, 460, 600, 530), "Two-line setting description"),
    "lines.tileTitle":    ("02-home", "lines", (160, 395, 330, 470), "Two-line shortcut tile title"),
    "lines.category":     ("06-search-grid", "lines", (439, 900, 600, 990), "Two-line browse tile title"),
    "lines.notice":       ("19-profile-drawer", "lines", (64, 1315, 380, 1385), "Two-line notification text"),
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


def op_diagr(rows, cx, cyc, cxl, cy):
    """diag for a top-right corner: (cx, cyc) is inside under the top edge, (cxl, cy) inside left of the right edge."""
    f = rows[cy][cxl]
    x = cxl
    while d(rows[cy][x + 1], f) <= 3:
        x += 1
    bg = rows[cy][x + 5]
    tol = max(2, d(bg, f) // 2)
    while d(rows[cy][x + 1], f) <= tol:
        x += 1
    x0, y = x, cyc
    while d(rows[y - 1][cx], f) <= tol:
        y -= 1
    t = 0
    while d(rows[y + t][x0 - t], f) > tol:
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
    absent = [t for t in THEMES if not (raw / t).is_dir()]
    if absent:   # dark only: a light/ folder is neither needed nor read
        raise SystemExit(f"{raw}: no {', '.join(absent)}/ captures; nothing written")
    pending, out = {}, {}
    for rid, (cap, op, args, note) in R.items():
        themes = [cap.split("/")[0]] if "/" in cap else list(THEMES)
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
    if missing:   # a reading with no value means its capture is absent
        raise SystemExit(f"no capture for {len(missing)} readings ({', '.join(missing[:5])}...); nothing written")
    write(readings)
    print(f"{sum(len(v) for v in readings.values())} readings of {len(readings)} ids")
