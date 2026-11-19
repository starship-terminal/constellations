# Components

Public signed-out Uber Eats, measured 2026-11-19. No crops: the preview browser produced no screenshot frames. Values are computed styles. Token names point at [tokens.json](tokens.json).

## Button

Primary, home Sign up and Search. Background `rgb(17, 17, 17)` (`light.component.button-primary-background`). Text `rgb(252, 252, 252)` (`light.component.button-primary-text`). UberMoveText 14 px, weight 500, for Sign up (36 px tall, padding 10 px 12 px, radius 500 px). Search is a 48 px circle, padding 14 px, radius 50%, 16 px type.

Secondary, home Log in, Get a ride, Find restaurants. Background `rgb(246, 246, 246)` (`light.background.pill`). Text `rgb(17, 17, 17)`. Same type. Find restaurants is 48 px tall, padding 14 px 16 px, radius 500 px. Transition: `background-color 0.2s ease-out`.

Location Find Food. Background `rgb(17, 17, 17)`, text `rgb(252, 252, 252)`, 56 px tall, padding 12 px 16 px, radius 8 px, 18 px, weight 500.

Hover is declared (`.base-button__style--primary:hover` sets a background from `--tw-compat-backgroundInversePrimary`) and was not measured on a hovered element.

Focus-visible, Log in link: outline `rgb(17, 117, 221) solid 2px`, offset 0. That blue is not `--brandBackgroundPrimary` (`#276ef1`).

Disabled, pressed, loading: not on these pages.

## Icon button

Main navigation menu: 50 by 50, transparent, radius 50%, padding 16 px, 18 px type. Not opened.

Search: see Button.

## Link

Chain names (Subway, Dunkin'): inline, transparent, `rgb(82, 82, 82)`, UberMoveText 16 px, weight 500, line-height 24 px, no underline.

Footer links were present (Get Help, Promotions, Privacy Policy). Their colours were not isolated from the footer, which is white with `rgb(17, 17, 17)` text.

The Uber One promo link is `rgb(252, 252, 252)`, 16 px, weight 500. Its parent fill is a gap.

## Text field

Home address combobox. Placeholder "Enter your address to find local favorites". The input is white, 16 px, `rgb(17, 17, 17)`, computed font Arial (the page family is UberMoveText). The shell is 540 by 48, white, radius 32 px, border `3px solid transparent`.

Location address field. Placeholder "Enter delivery address". Shell 540 by 56, white, radius 8 px, inset shadow `rgb(243, 243, 243) 0px -1px 0px 0px`. Not filled. No error state.

## Tabs

`/near-me` Delivery and Pickup. Transparent, 14 px, weight 500, padding 0 14 px, height 28, radius 500 px. Selected versus idle was not distinguished.

Hidden `input[type=radio][role=tab]` controls the popular section on the home page. The visible tab labels were not measured separately.

## Card

Category copy blocks (Restaurants, Grocery stores, Alcohol, Retail) are transparent stacks. Headings are UberMove 32 / 40 / 700. No card shadow and no card radius on the text column.

Restaurant rows on `/near-me` (Freddie's Sandwiches, La Boulangerie, Sightglass Coffee) are transparent links, about 535 px wide. Image treatment was not isolated.

## List row

City headings on `/location` (Aguada, Aguadilla) are UberMove 24 px, weight 700, `rgb(17, 17, 17)`, no underline.

## Header

64 px tall, padding 0 64 px, transparent. Wordmark link is 90 by 16.

## Gaps

- No crops.
- No hover, pressed, disabled, loading, or error measurements.
- Menu, tooltip, toast, dialog contents, checkbox, radio, switch, text area, select, avatar and badge were not on the public pages, or were not opened.
- The empty dialog node on the home page had no text and was not opened.
- Signed-in app components were not entered.
