#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from the native kit (tools/kit/native, from systems/grokbot); NAME, INVENTORY and GAPS are YouTube's.

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

NAME = "YouTube"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Filled button", "button", "The primary call to action: a capsule in the theme's ink (Install, Shop now, Learn more on ads; '1 month free' on the Premium interstitial).",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.button.filled.bg"), ("label", "color.button.filled.text"), ("label type", "typography.label"),
      ("large fill", "color.button.large.bg"), ("large label", "color.button.large.text"), ("large height", "size.buttonLarge")],
     [("ad pair", "button-ad-pair"), ("Premium interstitial", "button-large-upsell")],
     "White in dark, near-black in light; never red or blue. The interstitial's large button is the exception: dark grey with a white label, over its own light gradient."),
    ("Tonal button", "button", "The secondary action beside a filled one (Watch on an ad).",
     [("height", "size.button"), ("fill", "color.button.tonal.bg"), ("label", "color.button.tonal.text")],
     [("ad pair", "button-ad-pair")],
     "In dark its fill takes the ad's tint (navy under one ad, plum under another); in light it reads a neutral grey."),
    ("Pill buttons", "button", "Smaller capsules on the You tab: View channel filled with the ink, Get Premium outlined.",
     [("height", "size.pill"), ("filled", "color.button.pill.bg"), ("filled label", "color.button.pill.text"), ("outlined fill", "color.button.outlined.bg"),
      ("outline", "color.button.outlined.border"), ("outline width", "border.width.outline")],
     [("View channel and Get Premium", "button-pill-pair")], ""),
    ("Subscribe pill", "button", "White capsule beside the channel on a Short.",
     [("height", "size.subscribe"), ("fill", "color.button.subscribe.bg"), ("label type", "typography.meta")],
     [("on a Short", "button-subscribe-short")], "Subscribe was not tapped, so its subscribed state is not captured."),
    ("Icon button", "icon button", "Outline icons with no container: the header's Cast/Inbox, Notifications and Search, the overflow dots, the Shorts action rail.",
     [("colour", "color.text.primary"), ("touch target", "size.touchTarget")],
     [("home header", "header-home"), ("Shorts action rail", "shorts-action-rail")],
     "On a Short the rail's icons carry their count or label under them (70k, 591, Save, Share, Remix)."),
    ("Link", "link", "Blue text, no underline ('All' at the end of the subscriptions row; Safety Centre in My Ad Centre).",
     [("colour", "color.text.link"), ("on the dark sheet", "color.text.linkOnSheet")],
     [("subscriptions row", "avatar-subscriptions")], ""),
    ("Search field", "text field", "Grey capsule in the header with a back chevron before it and a microphone (empty) or a clear x (typed) after it.",
     [("height", "size.searchField"), ("corner", "radius.capsule"), ("fill", "color.surface.secondary"), ("placeholder", "color.text.placeholder"),
      ("text", "color.text.primary"), ("caret", "color.focus.caret")],
     [("focused, empty", "search-field-empty"), ("typed", "search-field-typed")],
     "Focus shows only the caret: no ring, no border."),
    ("Comment field", "text field", "Capsule inside the comments teaser with the owner's avatar before it.",
     [("height", "size.commentField"), ("fill", "color.surface.field"), ("placeholder", "color.text.secondary")],
     [("in the teaser", "card-comments")], ""),
    ("Filter chips", "tabs", "A horizontally scrolling row of rounded-rectangle chips that filters the feed (All, Today, Videos, Shorts, Live) and the library (Recent, Playlists).",
     [("height", "size.chip"), ("corner", "radius.chip"), ("fill", "color.surface.secondary"), ("selected fill", "color.surface.inverse"),
      ("selected label", "color.text.inverse"), ("label type", "typography.label"), ("gap", "space.sm")],
     [("All selected", "chip-row-all-selected"), ("Videos selected", "chip-row-videos-selected"), ("library", "chip-library")],
     "Selection inverts the chip. Recent carries a chevron because it opens the sort sheet."),
    ("Switch", "checkbox or toggle / switch", "A Material-style switch, not the iOS one: a thin track with a round thumb that overhangs it.",
     [("track width", "size.switch.width"), ("thumb", "size.switch.thumb"), ("on track", "color.switch.onTrack"), ("on thumb", "color.switch.onThumb"),
      ("off track", "color.switch.offTrack"), ("off thumb", "color.switch.offThumb")],
     [("off and on", "switch-on-off")], "On is the accent blue thumb on a pale-blue track in both themes."),
    ("Choice list", "radio or segmented control", "One choice per row with a tick at the right (Appearance) or the left (library sort).",
     [("tick", "color.icon.check"), ("row type", "typography.body")],
     [("Appearance", "choice-list-check")], ""),
    ("Tab bar", "navigation bar", "Five items over a translucent bar with a hairline on top: Home, Shorts, a round Create (+), Subscriptions, and the owner's avatar as You.",
     [("height", "size.tabBar"), ("fill", "color.surface.tabBar"), ("hairline", "color.border.tabBar"), ("label", "color.text.tab"), ("label type", "typography.tab"),
      ("Create", "size.createButton"), ("Create fill", "color.surface.createButton"), ("new-content dot", "color.brand.red")],
     [("You tab", "tab-bar")], "The selected tab fills its outline icon; there is no colour change."),
    ("Header and nav bar", "navigation bar", "Home has the logo at the left and icon buttons at the right. A pushed page has a back chevron and a bold title; Settings has a close x.",
     [("title type", "typography.navTitle"), ("icons", "color.text.primary"), ("background", "color.bg.page")],
     [("home", "header-home"), ("pushed page", "nav-bar-pushed")],
     "In light the pushed pages' titles read nearly white on white (light/10, light/11), so the light title colour is not captured."),
    ("Overflow menu", "menu or action sheet", "A floating card of icon-and-label rows that opens from a video's dots.",
     [("width", "size.menuWidth"), ("corner", "radius.menu"), ("fill", "color.surface.menu"), ("item type", "typography.body"), ("item text", "color.text.primary")],
     [("video overflow", "menu-overflow")],
     "In dark it sits over the feed undimmed; in light it opens near the top right with a soft shadow."),
    ("Bottom sheet", "sheet", "A sheet inset from the screen edges with a grabber, over a 50% scrim.",
     [("fill", "color.bg.sheet"), ("corner", "radius.sheet"), ("grabber", "color.icon.grabber"), ("scrim", "color.bg.scrim"), ("tick", "color.icon.check")],
     [("library sort", "sheet-sort"), ("My Ad Centre", "sheet-ad-centre")],
     "My Ad Centre keeps a dark body in the light theme too: only its header row turns white."),
    ("Accordion", "list row", "Outlined rows with an icon, a label and a chevron (About this advertiser, Why you're seeing this ad), then an outlined Send feedback capsule.",
     [("row", "size.accordion"), ("gap", "space.accordionGap"), ("outline", "color.border.accordion"), ("sheet", "color.surface.adSheet")],
     [("closed", "accordion-ad-centre")], "Only the closed state was captured."),
    ("Video card", "card", "A full-width 16:9 thumbnail with a duration badge, then the channel avatar, a two-line title, a meta line and an overflow button.",
     [("title", "typography.videoTitle"), ("title colour", "color.text.primary"), ("meta", "typography.meta"), ("meta colour", "color.text.secondary"),
      ("avatar", "size.avatarChannel"), ("margin", "space.screenMargin")],
     [("feed card", "card-video")],
     "Feed thumbnails run edge to edge with no radius. The thumbnail is the creator's artwork; only its frame belongs to the style."),
    ("Ad card", "card", "An ad in the feed: artwork, then an advertiser avatar, a headline, a description, 'Sponsored' and two buttons, on a tinted block.",
     [("block", "color.surface.ad"), ("headline", "typography.videoTitle"), ("buttons", "size.button")],
     [("home feed", "card-ad")], "The block's colour follows the ad in dark; treat it as a reading."),
    ("Shelf", "card", "A titled horizontal or two-column group: the Shorts shelf (portrait cards) and History (small rounded thumbnails with a red progress bar).",
     [("title", "typography.sectionTitle"), ("thumbnail corner", "radius.thumbnail"), ("progress", "color.brand.red"), ("gap", "space.xl")],
     [("Shorts", "shelf-shorts"), ("History", "shelf-history")], ""),
    ("Comments teaser", "card", "A rounded card under the watch page's actions with the comment count, a page dot and the comment field.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("height", "size.commentsCard")],
     [("watch page", "card-comments")], ""),
    ("List rows", "list row", "Settings rows (outline icon, label), General rows (label, helper text, value or switch), search rows (history clock or magnifier, query, thumbnail, fill-in arrow).",
     [("settings row", "size.row"), ("search row", "size.rowSearch"), ("label", "typography.body"), ("helper", "color.text.secondary"), ("section header", "typography.sectionTitle")],
     [("settings", "list-row-settings"), ("search history", "list-row-search-history"), ("suggestion with a second line", "list-row-suggestion")],
     "No dividers: rows are separated by space alone."),
    ("Avatar", "avatar", "Circles everywhere: channel avatars by titles, larger ones in the subscriptions row with a blue new-content dot, the owner's at 72 pt on the You tab.",
     [("channel", "size.avatarChannel"), ("subscriptions", "size.avatarSubscription"), ("profile", "size.avatarProfile"), ("new-content dot", "color.accent.default")],
     [("subscriptions row", "avatar-subscriptions"), ("profile", "avatar-profile")], "The pictures are channels' and the owner's own; only the circle and sizes are the style."),
    ("Badge", "badge", "The duration over a thumbnail: white text on a translucent black capsule.",
     [("fill", "color.overlay.duration"), ("type", "typography.meta"), ("corner", "radius.capsule")],
     [("duration", "badge-duration")], ""),
    ("Mini player", "pattern", "Closing the watch page shrinks the video to a floating card above the tab bar, with play and close over it.",
     [("controls", "color.text.primary")],
     [("floating", "mini-player")], ""),
    ("Watch page actions", "pattern", "Under the player: the title, the channel handle with likes, views and age, then a row of the channel avatar, a notification pill and outline action icons.",
     [("title", "typography.videoTitle"), ("meta", "color.text.secondary")],
     [("actions", "watch-actions")], "The block takes an ambient tint from the video in dark."),
]

# PRODUCT (adapt)
GAPS = [
    ("Player controls and scrubber", "Not captured. 17-player-controls-overlay-scrubber shows the same paused watch page as 16; the controls had already faded."),
    ("Dialog or alert", "Not captured: none appeared."),
    ("Toast or snackbar", "Not captured: no action that raises one was taken (look, don't act)."),
    ("Search results and no-results", "Not captured: submitting a search would add to the owner's history."),
    ("Create (+) sheet", "Not captured: it may raise camera or photo permission prompts."),
    ("Notifications list", "Not captured: opening it marks notifications as seen."),
    ("Pressed, disabled and error states", "Not captured: stills made with clicks, and no control was disabled."),
    ("Subscribed, liked and downloaded states", "Not captured: no like, subscribe or download was made."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light-theme Shorts, watch page, mini player and Premium interstitial", "Light covers 13 of the 18 screens."),
    ("Status colours", "No success, warning or error colour appeared."),
    ("Tooltip, table", "Not present in the screens captured."),
]

def main():
    out = [f"# {NAME} components", "",
           "Generated by `tools/build_components_md.py` from its inventory, [tokens.json](tokens.json) and [components/crops/](components/crops). "
           "Values are token paths (in the `light` and `dark` sets for colours, `core` for the rest); take them from tokens.json. "
           "Crops are cut from the 256-colour screenshots by `tools/crops.py`, so they show layout and state, never exact colour. "
           "Thumbnails, Shorts and ads in them are other creators' and advertisers' artwork, kept for layout only.", ""]
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
