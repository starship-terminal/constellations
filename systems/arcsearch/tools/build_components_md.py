#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from the native kit (tools/kit/native, from systems/grokbot); NAME, INVENTORY and GAPS are Arc Search's.

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


KNOWN = set(paths(TOK["core"])) | set(paths(TOK["dark"]))

NAME = "Arc Search"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Search field", "text field", "The launcher's glass capsule: a placeholder, a microphone and the Browse for Me glasses when empty, a clear button when typed.",
     [("height", "size.searchField"), ("corner", "radius.capsule"), ("fill", "color.glass.searchField"), ("placeholder", "color.text.placeholder"),
      ("text", "color.text.primary"), ("caret", "color.focus.caret"), ("type", "typography.search")],
     [("focused, empty", "search-field-empty"), ("typed", "search-field-typed")],
     "Focus shows only the accent caret: no ring, no border. The field and its sheet are glass, so both take the page's colour."),
    ("Launcher rows", "list row", "Pinned and favourite sites under the search field: favicon, name and a pin glyph, no dividers.",
     [("row", "size.rowLauncher"), ("label", "color.text.primary"), ("type", "typography.row"), ("pin", "color.text.tertiary"), ("sheet", "color.glass.launcher")],
     [("pinned", "launcher-rows-pinned")], ""),
    ("Suggestion rows", "list row", "Typed suggestions: a magnifier, the suggestion with the typed part dimmed and the completion in full ink, and a Browse for Me button.",
     [("row", "size.rowLauncher"), ("typed part", "color.text.secondary"), ("completion", "color.text.primary")],
     [("typed", "suggestion-rows")], "The typed part reads grey only after the first suggestion; the first row shows the query itself."),
    ("Browse for Me button", "button", "A small glass rounded rectangle at the end of a suggestion: Arc's AI search action.",
     [("height", "size.pill"), ("corner", "radius.pill"), ("fill", "color.glass.pill"), ("label type", "typography.pill"), ("label", "color.text.primary")],
     [("default", "button-browse-for-me")], "Not pressed: running it is an action, so its result page is not captured."),
    ("Capsule buttons", "button", "Two equal grey capsules at the top of Settings (Downloads, Archive), each with an outline icon.",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.surface.group"), ("label", "color.text.primary"), ("label type", "typography.button"), ("gap", "space.buttonGap")],
     [("pair", "button-pair")], "The same grey as the groups below them: on the Settings sheet one neutral fills every control."),
    ("Nav bar buttons", "icon button", "Glass capsules and circles in a sheet's nav bar: Done, Edit, a back chevron, a round close button.",
     [("height", "size.navButtonHeight"), ("Done fill", "color.glass.navButton"), ("Edit fill", "color.surface.control"), ("close", "size.closeButton"), ("close fill", "color.surface.close"), ("title type", "typography.navTitle")],
     [("Settings with Done", "nav-bar-sheet"), ("pushed page with back", "nav-bar-back"), ("scrolled, content blurred under it", "nav-bar-scrolled-blur"), ("Archive with Edit and confirm", "archive-header")],
     "Content scrolling under the bar blurs out behind it (06); there is no hairline."),
    ("Confirm button", "button", "A round accent button with a white tick at the Archive's top right: the one filled accent control in the app.",
     [("size", "size.confirmButton"), ("fill", "color.accent.default"), ("tick", "color.text.onAccent")],
     [("Archive", "archive-header")], "Lighter and softer in dark (a periwinkle), a saturated blue in light."),
    ("Grouped list", "list row", "Inset cards of rows on the Settings sheet, each row a coloured icon tile, a label, then a value, a chevron or a switch.",
     [("card", "color.surface.group"), ("corner", "radius.group"), ("row", "size.row"), ("tile", "size.tile"), ("tile corner", "radius.tile"), ("separator", "color.border.separator"),
      ("label", "typography.body"), ("value", "color.text.secondary"), ("chevron", "color.text.tertiary"), ("gap between groups", "space.groupGap"), ("margin", "space.screenMargin")],
     [("three rows", "list-group"), ("with values and chevrons", "list-row-value"), ("with a subtitle", "list-row-subtitle")],
     "Separators are inset to start at the label, never under the tile."),
    ("Icon tiles", "icon", "Filled squares behind white glyphs, one colour per kind of setting.",
     [("blue", "color.tile.blue"), ("green", "color.tile.green"), ("yellow", "color.tile.yellow"), ("purple", "color.tile.purple"), ("red", "color.tile.red"), ("size", "size.tile")],
     [("in a group", "list-group")], "The glyphs are Arc's artwork and are not kept here."),
    ("Switch", "checkbox or toggle / switch", "The iOS 26 switch: a green track with a white capsule thumb.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("on track", "color.switch.onTrack"), ("thumb fill", "color.switch.thumb")],
     [("on", "switch-on"), ("a group of them under helper text", "switch-group-helper")],
     "Every switch in Arc's settings is on, and none was changed, so the off state is not captured."),
    ("Choice list", "radio or segmented control", "One choice per row with an accent tick at the right (Default Search Engine), then an accent text action.",
     [("tick", "color.accent.check"), ("action", "color.accent.link"), ("row", "size.row")],
     [("Google chosen", "choice-list-check")], ""),
    ("Pop-up menu", "menu or action sheet", "A glass menu over the row that opened it, with a tick on the current choice (Archive Inactive Tabs).",
     [("fill", "color.glass.popup"), ("item type", "typography.body"), ("item text", "color.text.primary")],
     [("open", "popup-menu")], "Dismissed without a change."),
    ("Context menu", "menu or action sheet", "Long-pressing a favourite lifts its row and opens a glass menu above it with a red Remove Favorite.",
     [("destructive item", "color.destructive.text"), ("item type", "typography.body")],
     [("open", "context-menu-destructive")], "The menu's header (a hostname) is masked in the screenshots."),
    ("Edit menu", "menu or action sheet", "Edit in the Archive turns into a glass capsule holding a red Clear All with a trash glyph.",
     [("destructive item", "color.destructive.textOnControl"), ("fill", "color.surface.control")],
     [("open", "edit-menu-destructive")], "Clear All was not tapped, so its confirmation is not captured."),
    ("Sheet", "sheet", "Settings opens as a sheet over the dimmed browser; App Icon opens as a second sheet over Settings with a round close button.",
     [("sheet", "color.bg.sheet"), ("corner", "radius.sheet"), ("page behind", "color.bg.dimmed"), ("second sheet", "color.surface.sheet"), ("close", "size.closeButton"),
      ("title type", "typography.sectionHeader")],
     [("App Icon", "sheet-app-icon")], ""),
    ("Bottom toolbar", "navigation bar", "Glass along the bottom of a page: the tab stack at the left, a + capsule in the middle, a round chevron that opens the page menu at the right.",
     [("fill", "color.glass.toolbar"), ("+ fill", "color.glass.plus"), ("+ height", "size.plus"), ("+ width", "size.plusWidth"), ("corner", "radius.capsule")],
     [("on a page", "toolbar-bottom")], "No address bar on the page itself: the URL lives in the page menu."),
    ("Page menu", "menu or action sheet", "A glass sheet opened from the toolbar: an address bar with back, forward, copy link and reload, four square action buttons, a list panel with a disclosure and a stepper, Site Settings, and a notice.",
     [("sheet", "color.glass.menu"), ("address bar", "size.addressBar"), ("address fill", "color.glass.address"), ("square button", "size.tileButton"), ("square corner", "radius.tileButton"),
      ("square fill", "color.glass.tileButton"), ("square label", "typography.tileLabel"), ("panel", "color.glass.panel"), ("panel corner", "radius.panel"), ("row", "size.rowMenu"),
      ("row type", "typography.row"), ("text on glass", "color.text.onGlass")],
     [("expanded", "page-menu"), ("collapsed", "page-menu-collapsed"), ("address bar", "address-bar"), ("square buttons", "menu-tile-buttons"), ("list with stepper", "menu-list-stepper")],
     "Display Options collapses into one row with a chevron (13)."),
    ("Stepper", "slider or stepper", "Minus and plus in a small glass capsule at the end of the Page Zoom row.",
     [("fill", "color.glass.panel"), ("glyphs", "color.text.onGlass")],
     [("Page Zoom", "stepper-page-zoom")], "Not changed, so no value or pressed state is captured."),
    ("Notice", "banner or alert", "A glass panel at the bottom of the page menu reporting the ads and trackers Arc removed, with a second line that offers to restore the page.",
     [("fill", "color.glass.notice"), ("text", "color.text.onGlass"), ("second line", "color.text.onGlassSecondary"), ("type", "typography.notice"), ("second line type", "typography.caption")],
     [("page menu", "notice")], ""),
    ("Find bar", "search", "Replaces the toolbar: a round close button, a glass find field with the query and a match count, and previous and next chevrons in one capsule.",
     [("field", "size.findField"), ("close", "size.iconButton"), ("fill", "color.glass.findField"), ("count", "color.text.findCount")],
     [("focused, empty", "find-bar-focused"), ("one match of two", "find-bar-match"), ("no match", "find-bar-no-results")],
     "No match shows a 0 and nothing else; the page's match highlight is WebKit's."),
    ("Space sheet", "sheet", "Long-pressing the tab button opens the space: its name over a full-height gradient in the space's colour, and its tabs.",
     [("top", "color.space.top"), ("bottom", "color.space.bottom"), ("name", "color.space.title"), ("name type", "typography.spaceTitle")],
     [("Main", "space-sheet")], "Each space has its own colour; these are Main's, plum to green."),
    ("Tab switcher", "pattern", "Open tabs as overlapping cards with a site chip over each, above the toolbar.",
     [("toolbar", "color.glass.toolbar")],
     [("cards", "tab-switcher")], "The cards show the sites' pages; only their frame and order belong to Arc."),
    ("History list", "list row", "The Archive: day headers over white (light) or grey (dark) cards of rows, each a favicon, a title and a URL.",
     [("page", "color.bg.page"), ("card", "color.surface.card"), ("corner", "radius.group"), ("row", "size.rowHistory"), ("title type", "typography.row"),
      ("URL", "color.text.url"), ("URL type", "typography.caption"), ("header", "color.text.section"), ("header type", "typography.sectionHeader")],
     [("first day", "archive-list")], "Two rows in the later days are masked in the screenshots (a hostname, two searches)."),
    ("Archive search", "search", "A glass search field floating at the bottom of the Archive; focused, it gains a round close button and filters the list in place.",
     [("height", "size.searchBar"), ("fill", "color.glass.searchBar"), ("close", "size.iconButton")],
     [("resting", "archive-search-bar"), ("focused, empty", "archive-search-field-focused"), ("typed", "archive-search-field-typed"), ("one result", "archive-search-result")],
     "No results leave the page blank (23): no message, no illustration."),
]

# PRODUCT (adapt)
GAPS = [
    ("Browse for Me results", "Not captured: running it is an action; the glasses toggle was left alone."),
    ("Voice search", "Not captured: the microphone would raise a permission prompt."),
    ("Dialog or alert", "Not captured: only Clear Browsing Data and Clear All lead to one, and neither was tapped."),
    ("Switch off", "Not captured: every switch in Arc's settings is on, and none was changed."),
    ("Toast or snackbar", "Not captured: no action that raises one was taken (look, don't act)."),
    ("Downloads", "Not captured: the button opens the system Files app, not Arc."),
    ("Pressed, disabled and error states", "Not captured: stills made with clicks, and no control was disabled."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Empty states", "No message exists to capture: a find with no match shows 0, and an Archive search with no results is a blank page."),
    ("Status colours", "Only the destructive red appeared; no success, warning or info colour."),
    ("Tabs, tooltip, table, date picker", "Not present in the screens captured."),
]

def main():
    out = [f"# {NAME} components", "",
           "Generated by `tools/build_components_md.py` from its inventory, [tokens.json](tokens.json) and [components/crops/](components/crops). "
           "Values are token paths (in the `light` and `dark` sets for colours, `core` for the rest); take them from tokens.json. "
           "Crops are cut from the 256-colour screenshots by `tools/crops.py`, so they show layout and state, never exact colour. "
           "Pages shown inside the browser (YouTube, Google, other sites) are those sites' content, kept for layout only.", ""]
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
