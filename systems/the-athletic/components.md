# Components

Measured on the signed-out Athletic surfaces on 2026-11-19, at a 1169 by 731 viewport. Crops in [components/crops/](components/crops) are reconstructions drawn from those computed boxes. The preview browser returned "The browser is not producing screenshot frames", so none of these is a live pixel crop.

## Button

The trial button is the red action. Background `#b72424`, text `#ffffff`, nyt-franklin 14px weight 700, letter-spacing 0.25px, height 32px, padding 0 16px, radius 2px. Text was "Start a free trial". It links to the subscription marketing page. It was not followed into checkout.

The checkout CTA on the marketing page is a separate control: background `#121212`, text `#ffffff`, 16px weight 600, height 44px, radius 4px, width 335px. Text was "Continue to checkout". It was not pressed.

## Icon button

The hamburger is a 24px hit target labelled "Toggle hamburger menu". The search button is 36 by 60, labelled "Open Search". The dismiss control on the edition banner is 22 by 22. Their icon glyphs were not extracted.

## Link

Nav links are nyt-franklin 14px weight 400, white, letter-spacing 0.25px, padding 0 10px, line-height 40px, on the `#1a1a1a` bar. Footer links are 12px weight 500, `#c4c4c0`.

## Text field

The search field opened from the nav. Placeholder "Search for writers or stories", nyt-franklin 16px, height 32px, width 504px, padding 6px 0 7px, radius 0, no border. The bar behind it is white, 60px tall, over a `rgba(0, 0, 0, 0.65)` scrim. No query was typed. Focus computed to `outline: rgb(0, 0, 0) none 3px` and no box-shadow, so a visible focus ring was not observed.

## Text area

Not present on the public pages that were opened.

## Select

Not present. The edition banner uses two buttons, not a select.

## Checkbox

Not present on the public pages.

## Radio

The subscribe page has two radios, annual (checked) and monthly. The selected label is `#f8f8f8` with a 1px `#267c30` border, radius 3px, padding 14px 10px, 157 by 70. The resting label is white with a 1px `#dfdfdf` border. The radio glyph itself was not measured separately from the label.

## Switch

Not present.

## Tabs

Not present as a tab widget. The league page has a secondary nav, `#2b2b2b`, 40px tall, links at 12px weight 500 in `#dbdbd9`.

## Menu

The hamburger submenu and the league submenus were not opened. Their closed buttons were measured only as hit targets.

## Tooltip

Not observed.

## Dialog

Search opens as a modal: scrim `rgba(0, 0, 0, 0.65)`, white bar. `Modal_fadeIn` runs opacity from 0 to 1. No duration was declared on the sampled animation rule. The login surface is a cross-origin iframe, 552 by 478, and was not entered.

## Toast

Not observed.

## Card

The home headline card title is nyt-franklin 14px weight 500, line-height 18.2px, `#121212`. The 404 suggestion card is white, 227px wide, radius 0, no shadow, on a `#262627` ground.

## List row

The score ribbon row is `#f7f7f4`, 69px tall. Each score block is 140 by 65. Transition on the block link is 0.1s on all properties.

## Table

Not present on the pages opened.

## Avatar

Not present on the signed-out pages. Author photos sit behind the article byline and were not cropped.

## Badge

"BEST VALUE" is 12px weight 500, letter-spacing 0.4px, `#f4f5f2`. The comment count is a pill: white, 1px `#c4c4c0` border, radius 32px, padding 4px 12px 4px 8px, nyt-franklin 12px weight 500, height 32px. Its focus-visible rule is a 2px `#f0f0ee` outline, offset 2px.

## Gaps

- Hover, pressed, disabled and loading were not forced. The preview browser could not take screenshots, so pseudo-states were not captured.
- The login iframe is cross-origin. Its fields, errors and buttons were not read.
- Checkbox, switch, textarea, select, tooltip, toast, table and avatar were not on the public pages.
- Dark theme colours are declared in CSS and were not painted on these pages.
- Icon glyphs other than the wordmark were not extracted.
