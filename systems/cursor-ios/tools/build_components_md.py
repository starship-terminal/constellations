#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from systems/grokbot. Adapt NAME, INVENTORY and GAPS (PRODUCT (adapt)). A state cropped from
the light capture only is listed as light, with dark not captured.

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

NAME = "Cursor for iOS"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Navigation bar", "navigation bar", "Floating glass circles over the page: back (or the account avatar on Inbox) at the left, search and filter or a folder-plus at the right. In a thread the title sits between them in plain text, truncated.",
     [("button", "size.navButton"), ("fill", "color.surface.glass"), ("glyph", "color.text.emphasis"), ("title type", "typography.body")],
     [("list", "nav-bar-list"), ("thread", "nav-bar-thread")],
     "No bar background: content scrolls under the circles, and the status bar area blurs it."),
    ("Icon button", "icon button", "Round buttons: glass nav circles, and flat grey circles for actions in the agent details sheet (Rename, Unpin, Share).",
     [("nav size", "size.navButton"), ("action size", "size.iconButton"), ("action fill", "color.surface.iconButton"), ("glyph", "color.text.emphasis")],
     [("back", "icon-button-back"), ("details actions", "icon-button-details")], ""),
    ("Large title", "navigation bar", "A large left-aligned page title under the nav circles (Inbox, All Agents, a repo name).",
     [("type", "typography.largeTitle"), ("colour", "color.text.primary"), ("margin", "space.screenMargin")],
     [("Inbox", "large-title-inbox")], ""),
    ("Inbox tile", "card", "Two-by-two grid of rounded tiles on Inbox: a coloured outline icon, then a label and a grey count (All Agents, Needs Attention, Working, In Review).",
     [("width", "size.tile.width"), ("height", "size.tile.height"), ("corner", "radius.tile"), ("fill", "color.surface.card"), ("rim", "color.border.tile"),
      ("gap", "space.md"), ("label type", "typography.subheadline"), ("count", "color.text.tertiary"), ("All Agents icon", "color.icon.allAgents"),
      ("Needs Attention icon", "color.icon.attention"), ("Working icon", "color.icon.working"), ("In Review icon", "color.icon.review")],
     [("Inbox", "tile-inbox")],
     "Each tile's icon has its own colour; nothing else on the tile is coloured."),
    ("List row", "list row", "Single-line rows with an outline icon, a title and a chevron, divided by hairlines inset to the title (Projects, Workspaces, Add Workspace, Customize, Context, Support).",
     [("height", "size.row"), ("title", "color.text.primary"), ("icon", "color.text.tertiary"), ("chevron", "color.text.tertiary"), ("action row", "color.text.muted"),
      ("divider", "color.border.divider"), ("project icon", "color.icon.projectTeal"), ("type", "typography.body")],
     [("projects", "list-row-project"), ("repos", "list-row-repo"), ("mode options", "list-row-mode"), ("support and sign out", "list-row-support")],
     "Repo rows dim the owner prefix ('c-wenlong/') to tertiary and keep the repo name primary. 'New Project' is a muted action row with a + icon. Outbound rows (Help, Contact Sales) end in a north-east arrow; Sign out is not red."),
    ("Agent row", "list row", "Two-line rows for agents: a status dot, the title, then a line with the branch state, a diffstat and the repo.",
     [("height", "size.rowTwoLine"), ("unread dot", "color.status.unread"), ("read dot", "color.status.read"), ("merged icon", "color.status.merged"),
      ("draft icon", "color.status.draft"), ("status line", "color.text.secondary"), ("repo", "color.text.tertiary"), ("added", "color.diff.add"), ("type", "typography.subheadline")],
     [("merged, read", "list-row-agent-merged"), ("draft, unread", "list-row-agent-unread")],
     "Groups (Pinned, Needs Attention, Open PR, Read) start with a secondary header and a down chevron that collapses them."),
    ("Info row", "list row", "Label and value rows in the agent details sheet: label primary at the left, value secondary at the right, or a two-line repo and branch.",
     [("label", "color.text.primary"), ("value", "color.text.secondary"), ("divider", "color.border.divider")],
     [("agent details", "list-row-info")], ""),
    ("Pull-request row", "list row", "Rows in the Pull Requests sheet: a branch icon in the state colour, the PR title with its number in secondary, and a diffstat line.",
     [("merged", "color.status.merged"), ("closed", "color.status.closed"), ("added", "color.diff.add"), ("deleted", "color.diff.delete")],
     [("merged and closed", "list-row-pr")], ""),
    ("Composer", "text field", "A glass capsule pinned to the bottom of every list and thread: a round + button, the placeholder, a round microphone. Once text is typed it grows into a panel with a grabber, the model picker, the microphone and a round send button.",
     [("height", "size.composer"), ("panel height", "size.composerPanel"), ("corner", "radius.capsule"), ("panel corner", "radius.composerPanel"), ("fill", "color.surface.glass"),
      ("panel fill", "color.surface.composerPanel"), ("buttons", "color.surface.glassButton"), ("button size", "size.composerButton"), ("placeholder", "color.text.placeholder"),
      ("send", "color.button.send.bg"), ("send glyph", "color.button.send.glyph"), ("send size", "size.sendButton"), ("caret", "color.focus.caret"), ("type", "typography.body")],
     [("default", "composer-default"), ("typed", "composer-typed")],
     "The placeholder changes with the screen ('Plan, ask, build...' on lists, 'Follow up...' in a thread). Send is the theme's inverse, not the accent."),
    ("Search field", "text field", "Glass capsule search field at the top of a sheet, with a magnifier. Typed, it gains a clear button inside and (in the Model sheet) a separate round cancel button.",
     [("height", "size.searchField"), ("corner", "radius.capsule"), ("fill", "color.surface.glassField"), ("icon", "color.text.emphasis"), ("placeholder", "color.text.placeholder"),
      ("clear", "color.button.clear.bg"), ("caret", "color.focus.caret")],
     [("default", "search-field-default"), ("focused", "search-field-focused"), ("typed", "search-field-typed")],
     "Focus shows only the blue caret: no ring, no fill change."),
    ("Filter chips", "radio or segmented control", "A scrolling row of text chips under the search field; the selected chip gets a grey capsule, the rest are plain text.",
     [("height", "size.chip"), ("selected fill", "color.surface.secondary"), ("selected label", "color.text.primary"), ("label", "color.text.muted"), ("type", "typography.subheadline")],
     [("All selected", "chips-filter")], ""),
    ("Segmented control", "radio or segmented control", "All / Merged / Closed at the top of the Pull Requests sheet, drawn like the filter chips.",
     [("height", "size.segment"), ("selected fill", "color.surface.segment"), ("selected label", "color.text.primary"), ("label", "color.text.muted")],
     [("All selected", "segmented-pr")],
     "Light only: the Pull Requests sheet was not captured in dark, so `color.surface.segment` in dark is Not captured."),
    ("Switch", "checkbox or toggle / switch", "iOS 26 switch with a pill thumb, in the accent blue when on.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("on", "color.switch.on"), ("off", "color.switch.off"), ("thumb colour", "color.switch.thumb")],
     [("on and off", "switch-on-off")], ""),
    ("Pop-up select", "select or picker", "A row value with up-down chevrons opens a glass pop-up over the sheet with a tick on the current choice (Group by).",
     [("value", "color.text.secondary"), ("menu fill", "color.surface.popup"), ("menu corner", "radius.menu"), ("item type", "typography.body")],
     [("closed", "select-row"), ("open", "select-open")], ""),
    ("Menu", "menu or action sheet", "Glass pull-down from a thread's more button: icon and label rows in groups split by hairlines, a chevron on the item with a submenu (Copy).",
     [("width", "size.menuWidth"), ("corner", "radius.menu"), ("fill", "color.surface.menu"), ("divider", "color.border.menu"), ("item", "color.text.emphasis"), ("type", "typography.body")],
     [("agent menu", "menu-agent")],
     "Archive, the one destructive item, is drawn like the others: no red."),
    ("Sheet", "sheet", "Full-height sheets (Customize, Search, Profile, Add Workspace) and half-height ones (Model, Context, Pull Requests, agent details): a grabber, a round close button at the top left, a centred title.",
     [("fill", "color.bg.sheet"), ("corner", "radius.sheet"), ("behind", "color.bg.scrim"), ("grabber", "color.surface.grabber"), ("grabber width", "size.grabber.width"), ("title", "typography.title"), ("title colour", "color.text.emphasis")],
     [("full height", "sheet-customize"), ("half height", "sheet-model")],
     "A full-height sheet leaves a grey strip at the top over the dimmed page; a half sheet is inset from the screen edges."),
    ("Disclosure row", "list row", "File rows in the Changes sheet: a chevron, a file icon, the name, its path in secondary (clipped), the diffstat and a more button. Expanded, the chevron turns down and the diff appears in an inset band.",
     [("row fill", "color.surface.card"), ("sheet fill", "color.bg.sheetGrouped"), ("expanded band", "color.surface.inset"), ("path", "color.text.secondary"), ("added", "color.diff.add"), ("deleted", "color.diff.delete")],
     [("collapsed", "disclosure-collapsed"), ("expanded, empty diff", "disclosure-expanded"), ("files header", "sheet-header-files")],
     "Light shows a '5 Files / Expand All' header above the rows; the dark capture does not (light only)."),
    ("Changes card", "card", "A rounded card at the end of an agent's reply listing changed files with their diffstats; a '7 PRs' glass capsule floats above the composer.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("header count", "color.text.secondary"), ("file name", "color.text.primary"), ("file icon", "color.text.tertiary"),
      ("added", "color.diff.add"), ("deleted", "color.diff.delete"), ("PRs capsule", "color.surface.glass")],
     [("in a thread", "card-changes"), ("diffstat", "diffstat"), ("PRs capsule", "capsule-prs")], ""),
    ("Agent reply", "card", "Replies are plain text on the page, no bubble: numbered lists with secondary numbers, semibold runs, inline code on a grey chip.",
     [("text", "color.text.primary"), ("type", "typography.body"), ("list number", "color.text.secondary"), ("code fill", "color.surface.code"), ("code text", "color.text.code"), ("code type", "typography.code")],
     [("reply", "reply-text")], ""),
    ("Banner", "toast or banner", "A grey card in the Context sheet asking for photo access, with a centred line and a Continue capsule.",
     [("fill", "color.surface.secondary"), ("corner", "radius.banner"), ("text", "color.text.muted"), ("button", "color.surface.continue"), ("button height", "size.capsuleButton")],
     [("photo access", "banner-photos")], "No toast appeared in any capture."),
    ("Avatar", "avatar", "The account is an initial on a grey circle: small in the Inbox nav button, large on the profile.",
     [("fill", "color.surface.avatar"), ("profile size", "size.avatar"), ("nav size", "size.navButton")],
     [("profile", "avatar-profile"), ("nav", "avatar-nav")], ""),
    ("Agent title", "pattern", "The agent's full title, centred and medium, at the top of its details sheet over three round action buttons.",
     [("type", "typography.detailTitle"), ("colour", "color.text.primary")],
     [("details sheet", "detail-title")], ""),
    ("Bar chart", "pattern", "Daily bars in the chart orange with rounded tops, dashed weekly gridlines, a monospace axis on the right and dates below; a stat label and big number above.",
     [("bar", "color.chart.bar"), ("bar width", "size.chartBar"), ("grid", "color.border.chartGrid"), ("axis type", "typography.caption"), ("stat", "typography.statValue"), ("stat label", "color.text.secondary")],
     [("tokens", "chart-tokens"), ("agents", "chart-agents"), ("streak stats", "stats-streak")], ""),
    ("Activity heatmap", "pattern", "A year of days as dots in five steps from grey to the chart orange, with month initials under it.",
     [("empty", "color.surface.secondary"), ("level 1", "color.orange.100"), ("level 2", "color.orange.200"), ("level 3", "color.orange.300"), ("level 4", "color.orange.400"), ("dot", "size.heatDot")],
     [("profile", "heatmap-activity")],
     "Light only: the profile bottom was captured in light, so the dark heatmap is Not captured."),
    ("Empty state", "pattern", "Centred secondary text: a title and a sentence in search, one line in the Model sheet.",
     [("text", "color.text.secondary"), ("type", "typography.subheadline")],
     [("no search matches", "empty-state-search"), ("no model matches", "empty-state-model")], ""),
    ("Version footer", "pattern", "The app version centred at the bottom of the profile in upper-case monospace.",
     [("type", "typography.caption"), ("colour", "color.text.secondary")],
     [("profile", "footer-version")], "Light only."),
]

# PRODUCT (adapt)
GAPS = [
    ("Light-only components", "The Pull Requests sheet (segmented control, pull-request rows) and the profile bottom (activity heatmap, Support and More rows, version footer) were captured in light only, so their dark crops and the dark `surface.segment` and `status.closed` are Not captured."),
    ("Tab bar", "Not present. Inbox is the root; lists push from it and the composer sits at the bottom."),
    ("Dialog or alert", "Not captured. Only Archive leads to one, and it was not tapped."),
    ("Toast", "Not seen in any capture."),
    ("Loading and a running agent", "Not captured. Working showed 0 agents, and starting one is an action the capture avoided."),
    ("Settings screen", "Not present beyond the profile sheet."),
    ("Error state and warning colour", "No error or warning appeared."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
]


def crop_cells(name, states, crops=CROPS):
    """One link per crop on disk, dark then light. A state cropped from the light capture only is
    marked dark not captured; a state with no crop at all stops the build."""
    cells = []
    for state, stem in states:
        dark, light = crops / f"{stem}.png", crops / f"{stem}-light.png"
        if not dark.exists() and not light.exists():
            raise SystemExit(f"{name}: no crop {dark.name} or {light.name}")
        if dark.exists():
            cells.append(f"[{state} (dark)](components/crops/{dark.name})")
        if light.exists():
            label = "light" if dark.exists() else "light; dark not captured"
            cells.append(f"[{state} ({label})](components/crops/{light.name})")
    return cells


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
        out += ["Crops: " + ", ".join(crop_cells(name, states)) + ".", ""]
        if notes:
            out += [notes, ""]
    out += ["## Gaps", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in GAPS] + [""]
    (PKG / "components.md").write_text("\n".join(out))
    print("components.md:", len(INVENTORY), "components")


if __name__ == "__main__":
    main()
