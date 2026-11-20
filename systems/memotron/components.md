# Memotron components

Measured on the public marketing site and the signed-out web app on 2026-11-19.
Crops are in [components/crops/](components/crops). Values are computed styles.
A colour written as hex is the rounded sRGB of the computed `rgb()`.

## Inventory

| Checklist | In the product | Evidence |
|---|---|---|
| Button | yes | Go to web app, Download for Mac, Continue with Google, Continue with Apple, Continue offline |
| Icon button | yes | Discord mark in the header, a circle with a 1px fgs2 border |
| Link | yes | Nav links, Terms of Service, Docs |
| Text field | not on these pages | Signup has no email field. Google, Apple, or offline only |
| Text area | not present signed out | |
| Select | not present | Billing period is a segmented control, not a select |
| Checkbox | not present | |
| Radio | not present | |
| Switch | not present | |
| Tabs | partial | Pricing Monthly / Yearly / Lifetime is a segmented control |
| Menu | yes | Resources menu: Features, Tutorials, FAQs, Changelog, Roadmap |
| Tooltip | not captured | none opened on the public pages |
| Dialog | not present signed out | no promo dialog on the marketing site |
| Toast | not present | |
| Card | yes | Feature cards on the home page, plan cards on pricing |
| List row | partial | Plan feature rows |
| Table | not present | Compare is a card layout, not a table, in the first viewport |
| Avatar | not present | |
| Badge | partial | "20% off" sits inside the Yearly segment label |

## Button

Primary filled pill. Go to web app uses `bg-fgs1` text `text-bgs1`, height 33px, radius 9999px, padding 0 12.5px, type body-small.

### Go to web app

- **default.** Go to web app. color #151823 (rgb(21, 24, 35)); backgroundColor #f2f2f2 (rgb(242, 242, 242)); borderRadius 9999px; fontSize 15.0318px; fontWeight 400; padding 0px 12.5265px; height 33.3906px.
- **hover.** . color #151823 (rgb(21, 24, 35)); backgroundColor #c9c9c9 (rgb(201, 201, 201)).


Download for Mac is the same filled pill at body size, height 33px, padding 0 16.6px.

Signup provider buttons (Continue with Google, Continue with Apple) are a quieter fill, computed background `#252837` (between bgs2 and bgs3), text fgs1, height 50px, radius 9999px, padding 16.7px 25px.

Continue offline is a tall card-button: background bgs1, top border brs3, radius 6px on the bottom corners only, padding 12.5px.

## Link

Nav link at rest is text fgs1, transparent, radius 9999px, padding 4px 12.5px, type body-small. Hover turns the text accent primary (`#2c70dd`) and the fill raised (`#252837`, bgs3).

Terms of Service on the signup page is caption size, text secondary, dotted underline.

## Card

Home feature card: background bgs1 (`#151823`), radius 12.6px (rounded-xl), padding 25px 0 0 25px, gap 34px, min height 268px. Title is h4 at 18.9px weight 600. Body is text secondary.

Pricing plan card: border 1px brs3, radius about 12px, icon, title, price, feature list.

## Menu

Resources opens a panel of five tiles (Features, Tutorials, FAQs, Changelog, Roadmap) under the nav. Captured in [screenshots/home-dark-resources-menu.png](screenshots/home-dark-resources-menu.png).

## Segmented control

Pricing billing period: Monthly, Yearly (20% off), Lifetime. The selected segment is a darker pill inside a raised track. Monthly was clicked and recaptured.

## Wordmark

Hexagon mark plus "Memotron" in the h3 utility (21.9px / 32.9px, weight 400) on the marketing header. On signup the same mark sits alone in the left pane.

## Gaps

- No text field, checkbox, radio, switch, dialog, toast, tooltip, table or avatar on the signed-out surfaces.
- Focus-visible was not forced. The pages do not show a custom focus ring in the resting CSS that was read.
- Pressed and disabled were not captured. Nothing was submitted.
- Loading and error states sit behind signup.
- Light theme classes exist (`.cs_tidigit_light_blue` and the other tidigit accents) and are tokenised. The public pages paint dark only. No control on the marketing site or the signup page switches theme.
- The product rail ("21n", "Products") is marketing chrome, not the signed-in app shell.
