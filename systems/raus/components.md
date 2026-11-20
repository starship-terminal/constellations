# Components

Measured on the public marketing site on 2026-11-19, signed out. Values are token names. Readings are in [raw/notes.md](raw/notes.md).

`preview_snapshot` returned "The browser is not producing screenshot frames." Crops were not invented.

## Button

The filled action is `light.component.button-primary.bg` (`#23212c`) with `light.component.button-primary.text` (`#ffffff`), radius `core.radius.control` (20px), height `core.size.button` (48px), horizontal padding `core.spacing.button-x` (20px). Search, Start quiz, View all articles, Learn more and Find a cabin all computed to that.

Book now! is `light.component.button-promo`: orange `#dd5000`, white text, radius 12px, height 32px, padding `0px 10px`.

Cabins near me is an outline button: transparent fill, 1px `light.border.default`, same 20px radius and 48px height.

Book your stay is a 128px circle (`core.radius.circle`) with transparent fill and `light.action.magenta` text. It sits on the yellow search pill.

Hover, pressed, disabled and loading were not painted. Focus on Search and Start quiz, after `focus()`, computed to a 3px white auto outline and no box-shadow.

## Link

Header links at 1440 are `core.typography.nav` (22px, weight 400, letter-spacing -0.22px) in `light.text.primary`. At 390, the open nav uses `core.typography.nav-phone` (30px, weight 300, letter-spacing -0.9px).

The newsletter link is a filled control: `light.surface.promo` background, `light.action.orange` text, radius 20px, height 48px.

Listing cards are anchors. Their own colour computed to the browser default `rgb(0, 0, 238)`. Child text computed to ink. Treat the card text colour as `light.text.primary`, not the anchor's default blue.

## Text field

Not present on the pages measured. Search uses buttons for region, dates and guests. Help had no search input. No email was typed.

## Text area

Not present.

## Select

The language control is a native `select` named `language`. It computed to a transparent background, no border, Neue Haas Unica 14px, padding `0px 16px 0px 6px`. It was not changed.

Region, dates and guests are buttons, not selects. Their open menus were not captured.

## Checkbox

Cookiebot checkboxes were in the consent dialog before Deny was clicked. They were not measured as product controls. No product checkbox was on the later pages.

## Radio, switch

Not present on the pages measured.

## Tabs

Not present. Journal categories are text on cards, not a tab widget.

## Menu

At 390 the header links were collapsed. A 40px button with a 1px ink border and 16px radius opened a nav. The open nav links are listed under Link. The button's icon after the click was the close glyph in [icons/close.svg](icons/close.svg).

## Tooltip

Not present.

## Dialog

Cookiebot was on the first paint. Deny was clicked. The dialog was not measured as a product dialog. Date, guest and filter dialogs were not opened.

## Toast

Not present.

## Card

Journal cards put a white overlay (`light.surface.card`), radius 20px, padding 20px, over the image. The title is `core.typography.journal-title`.

Search listings are 464px wide anchors with a 4px radius. The title is `core.typography.card-title`. Drive-time chips have a 1px ink border, radius 20px, padding `4px 7.2px`. Trait labels are 12px uppercase.

## List row

Help questions sit in a list. A question row computed to padding `12px 0px`, 16px Neue Haas Unica, ink. The section heading above them is 36px, weight 300. The answer paragraph is 18px / 22px, letter-spacing -0.18px.

## Table

Not present.

## Avatar

Not present.

## Badge

Trait labels and the REGION label are uppercase 12px ink text, not a filled badge. The Filters control is a lime pill: `light.action.filters`, radius 16px, padding `0px 10px`, 14px type.

## Gaps

- No screenshots or crops. The preview browser did not produce screenshot frames.
- Hover, pressed, disabled, loading and error were not painted.
- Date, guest, region and filter menus were not opened.
- No booking, card, account, phone or newsletter address was entered.
- Gift cards, the shop, business sites, the cabin finder quiz and careers were not opened.
- Adyen checkout CSS is in the bundle. Those controls were not on screen, so their colours are not tokens.
- Dark theme was not declared.
- Reduced motion was not emulated. The only authored reduce rule found is an Adyen transition reset.
