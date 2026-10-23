#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from systems/grokbot through tools/kit/native/. NAME, INVENTORY and GAPS (PRODUCT (adapt)) are
Spotify's.

    python3 tools/build_components_md.py

Every value in an entry is a token path; the builder refuses a path tokens.json lacks and a crop
that is not on disk, so the page cannot drift from the package. Standard library only, deterministic.
"""
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CROPS = PKG / "components" / "crops"


def paths(node, pre=()):
    if isinstance(node, dict) and "$value" in node:
        yield ".".join(pre)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from paths(v, pre + (k,))


KNOWN = set(paths(TOK["core"])) | set(paths(TOK["dark"]))  # dark is the only theme

NAME = "Spotify"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Tab bar", "navigation bar", "Four tabs at the bottom (Home, Search, Your Library, Create): an outline icon over a small label. The current tab's icon fills and its label turns white.",
     [("label type", "typography.tabLabel"), ("current", "color.text.tabActive"), ("other", "color.text.tabInactive"), ("background", "color.bg.page")],
     [("Home current", "tab-bar-home")],
     "With Data Saver on, a 'Data Saver mode' line sits under the tabs."),
    ("Mini player", "card", "A rounded bar floating above the tab bar on every tab: artwork, title and artist, a devices button, the saved tick and play or pause, with a thin progress line along its bottom edge.",
     [("height", "size.miniPlayer"), ("corner", "radius.md"), ("artwork", "size.miniArtwork"), ("fill", "color.surface.miniPlayer"),
      ("title", "color.text.primary"), ("artist", "color.text.onMiniPlayer"), ("type", "typography.subtitle"), ("saved tick", "color.status.success"), ("tick size", "size.savedIcon")],
     [("default", "mini-player-default")],
     "The fill comes from the playing track's artwork, so it changes per track; the token is one album's reading. It sits 8 pt in from each edge."),
    ("Filter chips", "tabs or segmented control", "A row of capsules under the page header that filters the page (All, Music, Podcasts on Home; Playlists, Podcasts, Albums, Artists on Your Library). Choosing one adds a close (x) chip and sub-filters.",
     [("height", "size.chip"), ("corner", "radius.capsule"), ("fill", "color.chip.bg"), ("label", "color.chip.text"), ("selected fill", "color.chip.selectedBg"),
      ("selected label", "color.chip.selectedText"), ("label type", "typography.subtitle"), ("gap", "space.sm")],
     [("Home, All selected", "chip-home-all-selected"), ("Home, Music selected", "chip-home-music-selected"), ("Library, none selected", "chip-library-default"), ("Library, Playlists selected", "chip-library-selected")],
     "Unselected chips are iOS 26 glass. On Home, Music took the coral of the New Music Friday page it opened instead of green."),
    ("Shortcut tiles", "card", "Home opens with a two-column grid of eight recent items: square artwork at the left, a bold title, on a dark tile.",
     [("height", "size.shortcutTile"), ("corner", "radius.sm"), ("fill", "color.surface.tile"), ("title", "color.text.primary"), ("title type", "typography.label"), ("gap", "space.sm")],
     [("grid", "tile-shortcut-grid")],
     "A tile with an unread or live item shows three green dots at the right (DJ)."),
    ("Promo card", "card", "A full-width card for a release, with the artist's avatar and a heading above it: artwork at the left, eyebrow, title and artist, and a white Pre-save pill.",
     [("height", "size.promoCard"), ("corner", "radius.md"), ("fill", "color.surface.card"), ("eyebrow", "color.text.secondary"), ("title type", "typography.label")],
     [("Upcoming release", "card-promo")], ""),
    ("Artwork cards", "card", "Horizontally scrolling rows of square or round artwork with one or two lines of text under it (playlists, artists, Recents).",
     [("title", "color.text.primary"), ("subtitle", "color.text.secondary"), ("title type", "typography.label"), ("subtitle type", "typography.subtitle"), ("section title", "typography.sectionTitle")],
     [("playlist row", "card-row"), ("Recents", "card-recents")],
     "Artists are circles; playlists, albums and podcasts are squares. 'Show all' sits at the right of a section title in secondary text."),
    ("Browse category tile", "card", "Search's 'Browse all' grid: two columns of flat-colour tiles with a bold title at the top left and tilted artwork in the bottom right corner.",
     [("height", "size.categoryTile"), ("corner", "radius.sm"), ("title type", "typography.bodyBold"), ("colours", "color.category.music"), ("gap", "space.lg")],
     [("grid", "tile-category-grid")],
     "Each category keeps its own colour (core.color.category); the artwork is clipped by the tile."),
    ("Search field", "text field", "At rest, a white field with a magnifier and a dark placeholder. Tapped, it becomes a glass capsule with a green caret and a Cancel button beside it; typed text gets a clear (x) button.",
     [("height", "size.searchField"), ("corner", "radius.field"), ("fill", "color.surface.field"), ("placeholder", "color.text.placeholder"),
      ("focused height", "size.searchFieldFocused"), ("focused fill", "color.surface.fieldFocused"), ("focused placeholder", "color.text.placeholderFocused"), ("caret", "color.focus.caret"), ("type", "typography.body")],
     [("default", "search-field-default"), ("focused", "search-field-focused"), ("typed", "search-field-typed")],
     "Focus changes the whole field from white to glass; the caret is the only focus colour."),
    ("List row", "list row", "Artwork, a title and a subtitle line, with trailing actions: + (add), x (remove from recents), a green saved tick, or nothing. Subtitles can lead with green pin and download icons.",
     [("artwork", "size.rowArtwork"), ("row", "size.row"), ("library artwork", "size.libraryArtwork"), ("library row", "size.libraryRow"),
      ("title", "typography.body"), ("subtitle", "typography.subtitle"), ("subtitle colour", "color.text.secondary"), ("artwork gap", "space.md")],
     [("library", "list-row-library"), ("recent search", "list-row-recent-search"), ("search result", "list-row-search-result"), ("suggestion", "list-row-suggestion")],
     "Artists are round, everything else square. Verified artists get a small green badge after the name."),
    ("Page header", "navigation bar", "Tab pages start with the account avatar (a blue dot when there is news), a bold page title and icon buttons at the right.",
     [("avatar", "size.avatar.header"), ("title type", "typography.pageTitle"), ("dot", "color.accent.dot")],
     [("Your Library", "header-library")], "Tapping the avatar opens the profile drawer."),
    ("Navigation bar", "navigation bar", "Pushed pages (Settings, Playback) have a round glass back button, a centred bold title and an optional round glass action.",
     [("button", "size.navButton"), ("button fill", "color.surface.glass"), ("title type", "typography.navTitle")],
     [("Settings", "nav-bar-settings"), ("back button", "icon-button-back")], ""),
    ("Sort control", "select or picker", "A sort row above a list ('Recents' with up-down arrows, a grid toggle at the right) opens the sort sheet.",
     [("label type", "typography.subtitle"), ("label", "color.text.primary")],
     [("Recents", "sort-control")], ""),
    ("Sheet", "sheet", "Glass sheets rise from the bottom, inset 8 pt from the sides, with a grabber. Sort, context (track and artist) and share sheets all use them.",
     [("corner", "radius.sheet"), ("fill", "color.surface.sheet"), ("sort fill", "color.surface.sheetSort"), ("grabber", "color.border.grabber"), ("grabber size", "size.grabber.width"),
      ("header divider", "color.border.sheet"), ("item type", "typography.sheetItem"), ("header type", "typography.sheetHeader"), ("selected item", "color.text.accentOnSheet"),
      ("sort backdrop", "color.bg.scrim"), ("context backdrop", "color.bg.scrimContext")],
     [("sort", "sheet-sort"), ("artist context", "sheet-context-artist"), ("track context", "sheet-context-track")],
     "Context sheets open with the item's artwork and name, then a divider, then rows of line icon plus label. The selected sort option is green with a green tick; Cancel sits at the bottom."),
    ("Share sheet", "sheet", "A preview card of the shared item, colour swatches for the card, then round targets for search, groups, contacts and apps.",
     [("fill", "color.surface.shareSheet"), ("target", "size.shareTarget"), ("target fill", "color.surface.shareTarget"), ("label type", "typography.subtitle"), ("backdrop", "color.bg.scrimStrong")],
     [("playlist", "sheet-share-playlist"), ("targets", "share-targets")],
     "It opened on its own whenever a playlist or Now Playing was captured (see the README)."),
    ("Segmented control", "radio or segmented control", "Two segments in a glass capsule; the chosen one is a white pill with dark bold text (Song or Lyrics, when sharing a song).",
     [("height", "size.segmented"), ("corner", "radius.capsule"), ("track", "color.segmented.track"), ("selected", "color.segmented.selectedBg"), ("selected label", "color.segmented.selectedText"), ("label", "color.segmented.text"), ("label type", "typography.body"), ("selected label type", "typography.bodyBold")],
     [("Song selected", "segmented-song-selected")], ""),
    ("Tabs", "tabs", "Text tabs on an artist page (Music, Video, Events, Merch): the selected one is white and bold with a green underline as wide as the label.",
     [("selected", "color.tab.selected"), ("unselected", "color.tab.unselected"), ("underline", "color.tab.indicator"), ("underline height", "size.tabIndicator"), ("type", "typography.bodyBold")],
     [("Music selected", "tabs-artist")], ""),
    ("Buttons", "button", "Three kinds: the round green play button, white pills (Pre-save, Turn on) and an outlined pill (Following). Icon-only actions (shuffle, more) have no container.",
     [("play size", "size.playButton"), ("play fill", "color.button.primary.bg"), ("play glyph", "color.button.primary.glyph"), ("pill height", "size.pill"),
      ("white pill", "color.button.inverse.bg"), ("white pill label", "color.button.inverse.text"), ("outline", "color.button.outline.border"), ("outline width", "border.width.outline"), ("label type", "typography.label")],
     [("play", "button-play"), ("Pre-save", "button-pre-save"), ("Following", "button-following"), ("artist actions", "artist-actions")],
     "Green fills only the play button; every other button is white, outlined or a bare icon."),
    ("Icon button", "icon button", "Round glass buttons on pushed pages (back, search), bare line icons in page headers (search, +) and on rows (+, x, more), and 56 pt circles in the share sheet.",
     [("glass size", "size.navButton"), ("glass fill", "color.surface.glass"), ("share target", "size.shareTarget"), ("share target fill", "color.surface.shareTarget"), ("glyph", "color.text.primary"), ("row glyph", "color.text.secondary")],
     [("glass back", "icon-button-back"), ("header icons", "header-library"), ("share targets", "share-targets")],
     "Header and row icons have no container; only pushed pages and the share sheet put an icon in a circle."),
    ("Switch", "checkbox or toggle / switch", "The stock iOS 26 switch with a pill thumb, in the system green.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("on", "color.switch.on"), ("off", "color.switch.off"), ("thumb on", "color.switch.thumb"), ("thumb off", "color.switch.thumbOff")],
     [("on", "switch-on"), ("off", "switch-off")],
     "The one green that is not Spotify's: the switch keeps the system tint."),
    ("Slider", "slider", "A thin track with a white round thumb and end labels (0 sec, 12 sec); the filled part is Spotify green.",
     [("track", "size.slider.track"), ("thumb", "size.slider.thumb"), ("fill", "color.slider.fill"), ("empty", "color.slider.track"), ("thumb colour", "color.slider.thumb")],
     [("Crossfade", "slider-crossfade")], ""),
    ("Settings rows and tiles", "list row", "Settings opens with three quick tiles (icon, label, state; the active one green), then rows of line icon, title, subtitle and chevron. Playback's rows are title, description and a switch, grouped under bold section titles.",
     [("tile height", "size.settingsTile"), ("tile fill", "color.surface.panel"), ("tile corner", "radius.md"), ("tile label", "typography.caption"), ("active label", "color.text.accent"),
      ("row", "size.settingsRow"), ("title", "typography.body"), ("subtitle", "typography.subtitle"), ("chevron", "color.text.secondary"), ("section divider", "color.border.divider")],
     [("quick tiles", "tile-settings-quick"), ("rows", "list-row-settings")], ""),
    ("Profile drawer", "menu or action sheet", "The avatar opens a drawer from the left: an account card, a menu of icon rows, friends' activity, and Messages with a notification prompt.",
     [("fill", "color.bg.elevated"), ("width", "size.drawerWidth"), ("account card", "color.surface.tile"), ("card corner", "radius.md"), ("avatar", "size.avatar.drawer"),
      ("row type", "typography.body"), ("notice", "color.surface.notice"), ("notice button", "color.button.inverse.bg")],
     [("account", "drawer-account"), ("menu", "drawer-menu"), ("friends", "drawer-friends"), ("notification prompt", "drawer-notice")], ""),
    ("Banner", "toast or banner", "A card in the drawer asking to turn on push notifications: two lines of text, a white 'Turn on' pill with a bell, and a close (x).",
     [("fill", "color.surface.notice"), ("corner", "radius.md"), ("text type", "typography.subtitle"), ("button", "color.button.inverse.bg"), ("button label", "color.button.inverse.text"), ("button height", "size.pill")],
     [("notification prompt", "drawer-notice")], "No toast appeared in any capture."),
    ("Avatar", "avatar", "Round photos for the account, artists and friends; a letter on a colour when there is no photo; a + circle to invite.",
     [("header", "size.avatar.header"), ("drawer", "size.avatar.drawer"), ("corner", "radius.capsule")],
     [("friends row", "drawer-friends")], ""),
    ("Badge", "badge", "A plan badge (Family, lavender), a green 'Beta' tag, a blue unread dot, and a green verified seal.",
     [("plan fill", "color.badge.plan"), ("beta fill", "color.badge.beta"), ("text", "color.text.onBadge"), ("plan height", "size.badge"), ("dot", "color.accent.dot"), ("dot size", "size.dot"), ("plan type", "typography.label"), ("Beta type", "typography.tag")],
     [("plan", "badge-plan"), ("Beta", "badge-beta"), ("unread dot", "badge-unread-dot"), ("verified", "badge-verified")], ""),
    ("Artist header", "pattern", "A full-bleed photo under the status bar with the artist's name in very large bold type at its bottom and a 'Verified by Spotify' line.",
     [("name type", "typography.display"), ("name", "color.text.primary")],
     [("header", "artist-header")], "The photo is the artist's; the back button floats over it in glass."),
]

# PRODUCT (adapt)
GAPS = [
    ("Now Playing", "Not captured. Capturing it opened Spotify's share sheet at once, every time; only a low-resolution layout reference exists outside the repo."),
    ("Playlist and album page", "Not captured, for the same reason (15-share-sheet-playlist-auto shows the sheet that opened)."),
    ("Queue", "Not captured: the DJ session showed no queue button, and Now Playing could not be captured."),
    ("Long-press menu", "Not captured: 13-library-longpress-sheet shows the share sheet again, so it was left out of screenshots/."),
    ("Loading state", "Not captured: 01-home-loading shows Home already loaded (only the mini player's icons differ from 02-home), so it was left out."),
    ("Dialog or alert", "Not captured: no dialog was reachable without acting (log out, delete)."),
    ("Destructive confirmation", "Not captured: Log out was not tapped."),
    ("Empty state", "Not captured: search matched even a random string (09-search-results-rows)."),
    ("Toast", "Not seen in any capture."),
    ("Error and danger colours", "No error, warning or destructive state appeared."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light theme", "Not applicable: Spotify for iOS has no light theme."),
]


def main():
    out = [f"# {NAME} components", "",
           "Generated by `tools/build_components_md.py` from its inventory, [tokens.json](tokens.json) and [components/crops/](components/crops). "
           "Values are token paths (in the `dark` set for colours, the only theme, and `core` for the rest); take them from tokens.json. "
           "Crops are cut from the 256-colour screenshots by `tools/crops.py`, so they show layout and state, never exact colour.", ""]
    for name, item, what, props, states, notes in INVENTORY:
        for _, path in props:
            if path not in KNOWN:
                raise SystemExit(f"{name}: unknown token {path}")
        out += [f"## {name}", "", f"Checklist item: {item}. {what}", "", "| Property | Token |", "|---|---|"]
        out += [f"| {p} | `{path}` |" for p, path in props]
        out.append("")
        cells = []
        for state, stem in states:
            for suffix, theme in (("", "dark"), ("-light", "light")):
                f = CROPS / f"{stem}{suffix}.png"
                if f.exists():
                    cells.append(f"[{state} ({theme})](components/crops/{f.name})")
                elif not suffix:
                    raise SystemExit(f"{name}: no crop {f.name}")
        out += ["Crops: " + ", ".join(cells) + ".", ""]
        if notes:
            out += [notes, ""]
    out += ["## Gaps", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in GAPS] + [""]
    (PKG / "components.md").write_text("\n".join(out))
    print("components.md:", len(INVENTORY), "components")


if __name__ == "__main__":
    main()
