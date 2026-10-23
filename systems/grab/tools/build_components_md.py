#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from the native kit (systems/grokbot). NAME, INVENTORY and GAPS are Grab's; one theme, light.

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


KNOWN = set(paths(TOK["core"])) | set(paths(TOK["light"]))

NAME = "Grab"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Primary button", "button", "Full-width capsule at the bottom of a sheet or page (Yes, Book Standard, Choose this pickup, Let's go).",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.button.primary.bg"), ("label", "color.button.primary.text"),
      ("label type", "typography.button"), ("disabled fill", "color.button.disabled.bg"), ("disabled label", "color.button.disabled.text")],
     [("default", "button-primary-default"), ("with a leading icon button", "button-primary-book"), ("disabled", "button-primary-disabled")],
     "Grab green with a white label. Disabled turns it light grey with a grey label, no green left. Book Standard sits beside a round mint schedule button."),
    ("Secondary button", "button", "Full-width capsule under a primary button (Later).",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.button.secondary.bg"), ("label", "color.button.secondary.text")],
     [("default", "button-secondary-default")], "Pale mint fill, dark teal label, no border."),
    ("Compact button", "button", "Small capsule inside a card (Buy on a voucher).",
     [("height", "size.buttonCompact"), ("corner", "radius.capsule"), ("fill", "color.button.compact.bg"), ("label", "color.button.compact.text")],
     [("default", "button-compact-buy")], "A darker forest green than the full-width button."),
    ("Floating action button", "icon button", "Round button floating over a list, bottom right (new chat).",
     [("size", "size.fab"), ("fill", "color.nav.fab")], [("default", "fab-new-chat")], ""),
    ("Text field", "text field", "Outlined field with a coloured dot before it (pickup and destination).",
     [("height", "size.field"), ("corner", "radius.field"), ("border", "color.border.field"), ("focused border", "color.focus.ring"),
      ("focus halo", "color.focus.glow"), ("caret", "color.focus.caret"), ("placeholder", "color.text.placeholder")],
     [("focused, empty", "text-field-focused"), ("focused, typed", "text-field-typed")],
     "Focus is a darker green border with a soft green halo outside it; the unfocused field above keeps its grey border. A clear button replaces the camera and + icons once text is typed."),
    ("Search field", "text field", "A field on a coloured header (white) or on the page (grey).",
     [("height", "size.field"), ("corner", "radius.field"), ("on a header", "color.surface.card"), ("on the page", "color.surface.field"),
      ("placeholder", "color.text.placeholder"), ("caret", "color.focus.caret")],
     [("on the home header", "search-field-home"), ("focused, on the page", "search-field-focused")],
     "The focused grey field shows only the green caret; it gains no border."),
    ("Checkbox", "checkbox", "Rounded square at the end of a row (dietary preferences) or before a disclaimer.",
     [("size", "size.checkbox"), ("border", "color.border.control"), ("border width", "border.width.control"), ("row height", "size.row")],
     [("unchecked", "checkbox-unchecked")], "Only the unchecked state was captured; checking a box would have changed the account's food filters."),
    ("Filter chip", "chip", "Capsules in a horizontal row that filter a list (All, Transport, Food; Delivery, Pickup, Dine Out).",
     [("height", "size.chip"), ("corner", "radius.capsule"), ("selected fill", "color.chip.selected.bg"), ("selected label", "color.chip.selected.text"),
      ("default fill", "color.chip.default.bg"), ("default label", "color.chip.default.text"), ("label type", "typography.chip"), ("gap", "space.sm")],
     [("search filters", "chip-filter-selected"), ("service switch", "chip-service-selected")],
     "Selected is dark teal with a white label; the rest are pale mint with a teal label. Service chips carry a leading icon."),
    ("Outlined chip", "chip", "Capsules with a grey outline and a white fill on Moments (Location, Services, Health).",
     [("height", "size.chip"), ("border", "color.border.chip"), ("badge", "color.badge.new")], [("default, with a New badge", "chip-outlined-new-badge")], ""),
    ("Recent-search pill", "chip", "Grey capsules with a history or trending icon under Recent & popular.",
     [("fill", "color.surface.pill"), ("corner", "radius.capsule")], [("default", "pill-recent-search")], ""),
    ("Tabs", "tabs", "Text tabs with an underline under the active one (Following, For you, Top posts; Deals, Reviews, Photos, About).",
     [("active label", "color.tab.active"), ("inactive label", "color.tab.inactive"), ("indicator", "color.tab.indicator"), ("label type", "typography.chip")],
     [("Moments", "tabs-underline"), ("merchant page", "tabs-merchant")], ""),
    ("Pill tabs", "tabs", "Text tabs whose active one sits in a pale mint capsule (Recent, Suggested, Saved).",
     [("active fill", "color.brand.mint"), ("active label", "color.tab.active"), ("inactive label", "color.text.secondary")],
     [("Recent active", "tabs-recent-suggested-saved")], ""),
    ("Segmented control", "tabs", "Two options in a grey capsule track, the active one on a white capsule (Now, Later).",
     [("track", "color.surface.field"), ("thumb", "color.surface.card"), ("corner", "radius.capsule")],
     [("Now selected", "segmented-now-later")], ""),
    ("Tab bar", "app shell", "Five items with the scan button raised in the middle (Home, Moments, scan, Activity, Messages); GrabFood has its own four-item bar.",
     [("height", "size.tabBar"), ("active", "color.nav.active"), ("inactive", "color.nav.inactive"), ("scan button", "color.nav.scan"),
      ("scan size", "size.scanButton"), ("label type", "typography.caption")],
     [("Home", "tab-bar-home"), ("GrabFood", "tab-bar-food")], "The tab bar hides as Home scrolls."),
    ("Header", "app shell", "A coloured band behind the status bar with a search field (Home deep green, GrabFood blue).",
     [("Home top", "color.bg.header"), ("Home bottom", "color.bg.headerEnd"), ("GrabFood", "color.service.food"), ("banner type", "typography.display")],
     [("Home", "header-home"), ("GrabFood", "header-food"), ("compact, scrolled (account)", "header-compact-account")],
     "Each service owns a header colour; Home's is a gradient."),
    ("Card", "card", "White cards with a grey outline or a soft shadow (shortcut, account, voucher, payment), and tinted promo cards.",
     [("fill", "color.surface.card"), ("border", "color.border.card"), ("corner", "radius.card"), ("shortcut height", "size.card.height")],
     [("shortcut", "card-shortcut"), ("promo", "card-promo"), ("account", "card-account"), ("payment methods", "card-payment"),
      ("voucher", "card-voucher"), ("offer grid", "card-offer-grid")],
     "The payment card's last digits and the Ride to card's destination are masked in the crops."),
    ("List row", "list row", "Rows with a leading icon or image, a title, a meta line and a trailing value or chevron.",
     [("row height", "size.row"), ("title", "color.text.primary"), ("meta", "color.text.secondary"), ("divider", "color.border.divider"),
      ("status (bad)", "color.text.danger"), ("status (good)", "color.text.success"), ("link", "color.text.link"), ("New marker", "color.text.danger")],
     [("activity, with status labels", "list-row-activity-status"), ("settings, with New", "list-row-settings-new"), ("merchant", "list-row-merchant"),
      ("place suggestion", "list-row-place-suggestion"), ("ride option, selected", "list-row-ride-option-selected")],
     "Trip titles that start with the owner's home address are masked in the activity crop. A selected ride option gets a green outline."),
    ("Tooltip", "tooltip", "Dark green bubble with an arrow pointing at its control and a close button.",
     [("fill", "color.surface.tooltip"), ("text", "color.text.onTooltip"), ("corner", "radius.tooltip")], [("shown", "tooltip-save-posts")], ""),
    ("Coach mark", "tooltip", "White card over a scrim, pointing at a control, with a Next button.",
     [("fill", "color.surface.sheet"), ("scrim", "color.bg.scrim"), ("button", "color.button.primary.bg")], [("shown", "coachmark-export")], ""),
    ("Bottom sheet", "dialog", "Sheet over a scrim with an illustration, a two-line title, body and two buttons; or a coloured flash-deals sheet with a countdown.",
     [("fill", "color.surface.sheet"), ("corner", "radius.sheet"), ("scrim", "color.bg.scrim"), ("lighter scrim", "color.bg.scrimLight"),
      ("title type", "typography.sheetTitle"), ("flash header", "color.service.flash"), ("timer box", "color.service.timer")],
     [("permission pre-prompt", "sheet-preprompt"), ("flash deals", "sheet-flash-deals"), ("pickup, over the map", "sheet-pickup-over-map")],
     "The map behind the pickup sheet is masked: it was centred on the owner's home."),
    ("Banner", "pattern", "An orange bar above the tab bar with a countdown (25% off flash deals).",
     [("fill", "color.badge.discount"), ("timer box", "color.service.timer")], [("default", "banner-flash-deals")], ""),
    ("Empty state", "pattern", "A 3D illustration, a display title, one grey line and a green text action; or a short hint under search results.",
     [("title type", "typography.sheetTitle"), ("body", "color.text.secondary"), ("action", "color.text.linkBrand")],
     [("cart", "empty-state-cart"), ("no more results", "empty-state-search")], ""),
    ("Interstitial", "pattern", "A full-screen promo on cream with a large orange-brown headline and a primary button.",
     [("background", "color.service.cream"), ("button", "color.button.primary.bg")], [("open", "interstitial-pickup-promo")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Dark theme", "Not applicable: Grab has no dark UI. It stays light with the phone in dark mode."),
    ("Switch", "Not captured: the account page would not scroll down to Settings."),
    ("Dialog or alert", "Not captured: none appeared."),
    ("Toast", "Not captured: the toast after answering Later had gone before the capture (12-messages-toast-fab shows the page after it)."),
    ("Loading", "Not captured: screens loaded before a capture could run."),
    ("Checked checkbox and other states that change the account", "Not captured: checking a dietary preference or booking would have changed the account."),
    ("Error and validation", "Not captured: no form showed an error."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Masked regions", "Addresses, postcodes, the map round the owner's home and card digits are painted over in screenshots and crops (tools/masks.json); values were read before masking."),
]


def main():
    out = [f"# {NAME} components", "",
           "Generated by `tools/build_components_md.py` from its inventory, [tokens.json](tokens.json) and [components/crops/](components/crops). "
           "Values are token paths (in the `light` set for colours, `core` for the rest; Grab has no dark set); take them from tokens.json. "
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
            f = CROPS / f"{stem}.png"   # light only: no theme suffix
            if not f.exists():
                raise SystemExit(f"{name}: no crop {f.name}")
            cells.append(f"[{state}](components/crops/{f.name})")
        out += ["Crops: " + ", ".join(cells) + ".", ""]
        if notes:
            out += [notes, ""]
    out += ["## Gaps", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in GAPS] + [""]
    (PKG / "components.md").write_text("\n".join(out))
    print("components.md:", len(INVENTORY), "components")


if __name__ == "__main__":
    main()
