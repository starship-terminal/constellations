#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from systems/grokbot. Adapt NAME, INVENTORY and GAPS (PRODUCT (adapt)).

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

NAME = "GitHub Mobile"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Neutral button", "button", "Full-width or paired grey buttons: Add Favorites, Get started, Star with its fork and watch icon buttons.",
     [("height", "size.button"), ("corner", "radius.button"), ("fill", "color.button.neutral.bg"), ("label", "color.button.neutral.text"),
      ("label type", "typography.headline"), ("icon button", "size.iconButton")],
     [("default", "button-neutral"), ("Star with icon buttons", "button-repo-actions")],
     "The app's main button is grey, not green or blue. Star was not tapped, so no pressed or starred state is captured."),
    ("Accent and purple buttons", "button", "Compact buttons inside a card: Configure (blue text on a tinted fill), and Copilot's filled purple button beside a purple Dismiss text button.",
     [("height", "size.buttonCompact"), ("corner", "radius.button"), ("accent fill", "color.button.accent.bg"), ("accent label", "color.button.accent.text"),
      ("purple fill", "color.button.done.bg"), ("purple label", "color.button.done.text"), ("text button", "color.done.fg")],
     [("Configure", "button-accent"), ("Dismiss and Email me", "button-done")],
     "Purple belongs to Copilot and to merged or done states; blue to links and the Configure call to action."),
    ("Floating button", "button", "New Session floats bottom right above the tab bar on Home and Copilot, with a round compose button beside it on Copilot.",
     [("height", "size.fab"), ("corner", "radius.capsule"), ("fill", "color.button.fab.bg"), ("label", "color.button.fab.text")],
     [("Home", "fab-new-session"), ("Copilot", "fab-copilot")],
     "Grey glass in dark, the theme's ink (near-black) in light."),
    ("Icon button", "icon button", "Round glass back, close and more buttons; paired glass capsules hold two icons (+ and search, + and more).",
     [("size", "size.navButton"), ("fill", "color.surface.glass"), ("glyph", "color.text.primary")],
     [("back", "icon-button-back")], "Each is iOS 26 glass; the fill token is its centre reading over an empty page."),
    ("Link", "link", "Blue text links and text buttons (View All, Configure, hunk headers).",
     [("colour", "color.text.link"), ("fill behind accent text", "color.accent.subtle")],
     [("Configure", "button-accent")], ""),
    ("Search field", "text field", "Glass capsule at the top of search with a magnifier, a clear button once typed, and a round close button beside it.",
     [("height", "size.searchField"), ("corner", "radius.capsule"), ("fill", "color.surface.glass"), ("placeholder", "color.text.placeholder"),
      ("text", "color.text.primary"), ("caret", "color.focus.caret")],
     [("focused, empty", "search-field-focused"), ("typed", "search-field-typed")],
     "Focus shows only the blue caret. Search qualifiers (org, user, repo, path) sit in a glass bar where the tab bar was."),
    ("Filter chips", "select or picker", "Glass capsules under a list's title (Inbox, Focused, Unread, Repository; Open, Label, Author). A chevron marks the ones that open a menu.",
     [("height", "size.chip"), ("corner", "radius.capsule"), ("fill", "color.surface.glass"), ("label", "color.text.secondary"), ("type", "typography.caption")],
     [("Inbox", "chip-filter-inbox"), ("Issues", "chip-filter-issues"), ("search qualifiers", "chip-qualifiers")], ""),
    ("Menu", "menu or action sheet", "iOS 26 glass pull-down from a nav button (Share via, Report, Add to favorites) and a pop-up from a chip with a tick on the current choice.",
     [("fill", "color.surface.menu"), ("item type", "typography.body")],
     [("pull-down", "menu-pulldown"), ("pop-up, Open chosen", "menu-popup")], "Captured in dark only."),
    ("Sheet", "sheet", "Inbox Filters opens as a sheet with a round confirm button; the chosen filter turns blue with a count and a tick.",
     [("fill", "color.bg.page"), ("rows", "color.surface.card"), ("selected", "color.text.link")],
     [("Inbox chosen", "sheet-filters")], "Captured in dark only."),
    ("Switch", "checkbox or toggle / switch", "iOS 26 switch with a pill thumb, in grouped rows.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("on", "color.switch.on"), ("off", "color.switch.off"), ("thumb", "color.switch.thumb")],
     [("on and off", "switch-on-off")], "On is the accent blue in both themes."),
    ("Choice list", "radio or segmented control", "Appearance: one row per choice in a grouped card, with a filled blue tick on the chosen one.",
     [("card", "color.surface.card"), ("tick", "color.accent.fg"), ("row", "size.rowSettings")],
     [("Automatic chosen", "select-appearance")], ""),
    ("Tab bar", "tabs", "A floating glass capsule with four tabs (Home, Inbox, Explore, Copilot); the selected tab sits in a darker or greyer pill and turns blue.",
     [("height", "size.tabBar.height"), ("width", "size.tabBar.width"), ("fill", "color.surface.glass"), ("selected pill", "color.surface.tabSelected"),
      ("label", "color.text.tab"), ("selected label", "color.text.tabSelected"), ("type", "typography.tab")],
     [("Home", "tab-bar-home"), ("Inbox", "tab-bar-inbox")], "Content scrolls under it."),
    ("Navigation bar", "navigation bar", "Floating glass controls over the content: a round back button, a centred title (with the repository under an issue or PR title) and a glass capsule of actions.",
     [("button", "size.navButton"), ("title type", "typography.headline"), ("fill", "color.surface.glass")],
     [("repository", "nav-bar-repo")], "No bar background."),
    ("Grouped card", "card", "Rows in a rounded card with hairline dividers inset to the text; rows lead with a coloured icon tile.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("padding", "space.cardPadding"), ("divider", "color.border.divider"),
      ("row", "size.row"), ("tile", "size.tile"), ("tile corner", "radius.tile"), ("title", "typography.rowTitle")],
     [("My Work", "card-grouped"), ("Settings, with values", "card-settings"), ("repository rows", "list-row-tiles")], ""),
    ("Content cards", "card", "The Copilot promo card, the Explore activity card with a rendered Markdown excerpt, and the profile status card.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("status fill", "color.surface.muted"), ("status corner", "radius.status")],
     [("promo", "card-promo"), ("activity", "card-activity"), ("profile status", "card-status")], ""),
    ("Banner", "toast or banner", "A yellow strip under the nav bar for an archived repository, and a dismissable notification prompt at the top of Inbox.",
     [("archived fill", "color.attention.subtle"), ("archived text", "color.attention.fg"), ("prompt", "color.bg.list"), ("separator", "color.border.section")],
     [("archived", "banner-archived"), ("notification prompt", "banner-notification")], "No toast appeared in any capture."),
    ("List row", "list row", "Full-bleed rows on the list background: Inbox notifications, issues, pull requests, repository results, search scopes.",
     [("title", "typography.callout"), ("meta", "color.text.secondary"), ("unread dot", "color.accent.fg"), ("count", "color.accent.subtle"),
      ("open icon", "color.success.fg"), ("divider", "color.border.divider")],
     [("Inbox, unread", "list-row-inbox"), ("issue with labels", "list-row-issue"), ("pull request", "list-row-pr"),
      ("repository result", "list-row-repo-result"), ("search scope", "list-row-search-scope")], ""),
    ("State badge", "badge", "Capsules for an issue or PR's state: Open (green), Draft (grey), Merged (purple), all with white labels and an icon; Locked (muted).",
     [("height", "size.badge"), ("corner", "radius.capsule"), ("open", "color.success.emphasis"), ("draft", "color.neutral.emphasis"),
      ("merged", "color.done.emphasis"), ("locked", "color.surface.muted"), ("label", "color.text.onEmphasis"), ("type", "typography.caption")],
     [("Open and Locked", "badge-open-locked"), ("Draft, Locked, branches", "badge-draft-branch"), ("Merged, branches", "badge-merged-branch")], ""),
    ("Small badges", "badge", "The New badge before a settings row, unread counts in Inbox, and agent-session status chips (Completed, Failed).",
     [("new", "size.newBadge"), ("fill", "color.accent.subtle"), ("label", "color.text.link"), ("status chip", "size.statusChip"), ("status fill", "color.surface.muted")],
     [("New", "badge-new"), ("count", "badge-count"), ("Completed", "chip-status-completed"), ("Failed", "chip-status-failed")], ""),
    ("Branch pill", "badge", "A monospace branch name in a tinted, slightly rounded box; two pills with an arrow show base and head.",
     [("height", "size.branch"), ("corner", "radius.branch"), ("fill", "color.accent.subtle"), ("text", "color.text.link"), ("type", "typography.code")],
     [("with Merged", "badge-merged-branch")], ""),
    ("Issue label", "badge", "Repository labels as capsules in the label's own colour.",
     [("height", "size.label"), ("corner", "radius.capsule")],
     [("two labels", "label-issue")], "Colours come from each repository's label settings, so none is a token."),
    ("Avatar", "avatar", "Round photos: the account at the top of Home, comment authors with a role label, the profile header.",
     [("header", "size.avatar.header"), ("comment", "size.avatar.comment"), ("profile", "size.avatar.profile"), ("role label", "typography.footnote")],
     [("Home", "avatar-header"), ("comment author", "avatar-comment"), ("profile", "avatar-profile")], ""),
    ("Diff", "table", "Files Changed: a gutter of line numbers and full-width tinted lines, a blue hunk header, monospace code with syntax colours.",
     [("line", "color.surface.code"), ("gutter", "color.surface.gutter"), ("added", "color.diff.addition"), ("added gutter", "color.diff.additionGutter"),
      ("deleted", "color.diff.deletion"), ("deleted gutter", "color.diff.deletionGutter"), ("hunk", "color.diff.hunk"), ("type", "typography.code")],
     [("lines", "diff-lines"), ("diffstat row", "diffstat")], ""),
    ("Code preview", "card", "A code block in a card with a file path bar, line numbers and syntax colours (Code Options).",
     [("fill", "color.surface.card"), ("keyword", "color.syntax.keyword"), ("entity", "color.syntax.entity"), ("constant", "color.syntax.constant")],
     [("preview", "code-preview")], ""),
    ("Comment", "card", "Author avatar, name, age and role label, then the body; no bubble or card around it.",
     [("body", "typography.body"), ("meta", "color.text.secondary")],
     [("issue comment", "comment")], ""),
    ("Empty state", "pattern", "A centred title, sometimes with a grey line under it; on Home, an empty card with a neutral button.",
     [("title", "typography.title"), ("body", "color.text.secondary")],
     [("no repositories", "empty-state-list"), ("search", "empty-state-search"), ("Favorites", "empty-state-favorites")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Loading", "Not captured. 09-repo-results-loading-spinner is pixel-identical to 10-repo-results-list: the results had loaded before the capture."),
    ("Comment composer and text area", "Not captured: opening it on a real issue risks posting."),
    ("Dialog or alert", "Not captured: none appeared."),
    ("Toast", "Not seen in any capture."),
    ("Error state", "Not captured; no request failed."),
    ("Pressed and selected states of Star, Watch, Fork", "Not captured: nothing was starred, watched or forked."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light-theme menus, sheet, search focus, issue and lists", "Light was captured for 12 of the 23 screens (01, 03, 05, 06, 08, 11, 17, 18, 20, 21, 22, 23)."),
    ("Danger fill", "No red badge, button or banner appeared."),
]


def main():
    out = [f"# {NAME} components", "",
           "Generated by `tools/build_components_md.py` from its inventory, [tokens.json](tokens.json) and [components/crops/](components/crops). "
           "Values are token paths (in the `light` and `dark` sets for colours, `core` for the rest); take them from tokens.json. "
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
