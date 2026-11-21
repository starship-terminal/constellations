# Components

Values are computed styles from the signed-out pages in [raw/computed.json](raw/computed.json). There are no crops. `preview_snapshot` did not produce frames.

## Button

Primary, home hero, light. Class `btn btn--x-large btn--primary`. Fill `#121212`, text `#fcfcfc`, radius 8px, padding `0 24px`, height 50px, GT America 17px, tracking -0.238px. The small primary ("Join for free") is the same fill and text, padding `6.75px 10px`, height 32px, 15px type.

The stylesheet rule is `light-dark(rgb(18, 18, 18), rgb(255, 255, 255))` for the fill and `light-dark(rgb(252, 252, 252), rgb(17, 17, 17))` for the text. Hover fill is `#2b2b2b` in light and `#c6c6c6` in dark. Active fill is `#3c3c3c` in light and `#cacaca` in dark. Disabled fill is `#363636` in light with keyword `gray` text, and `#3c3c3c` with `#575757` text in dark. The disabled Continue button on `/login` computed `#3c3c3c` / `#575757` while the page was dark.

Neutral nav links are transparent, text `#2c2a25`, radius 7px, padding `7.5px 10px`, height 33px, border 1.5px solid transparent. Hover colour is `var(--color-brand)`.

Outline ("Get the app") computes white fill, text `#2c2a25`, radius 8px, height 50px. The edge is `currentColor` on `::before` and `::after`, not a normal border.

Icon-only "Show more" is 38px, radius 100%, text `#575757`.

## Link

`a:not(.btn):hover` and `:focus-visible` set colour to `var(--color-brand-default)`, which computes to `#6e36ff`. A body link on the home page ("Log in" in the lede) computed `#2c2a25` at 16px.

## Text field

`/login` while dark: email `#484848` fill, `#f0f0f0` text, radius 7px, padding `6.5px 18px`, height 46px. Password beside it was `#333333`. Placeholder "Enter your email address".

`/register` after `data-theme=light` and focus: fill `#f2f2f2`, text `#222222`, placeholder `#9c9c9c`, height 48px, radius 7px. Label "Email" is 14px / 400 / `#2c2a25`.

The header search input computed a 0×0 box until the search UI is opened. Its open state was not read.

## Tabs and chips

Release page nav item "Overview" is 15px / 400 / `#2c2a25`, height 54px, no fill. `/releases` type chips are radius 8px, padding `0 14px`, height 32px. The active chip is `#2c2a25`. Idle chips are `rgba(55, 53, 47, 0.65)`.

## Card

Home `.bento-item` is `#fafafa`, radius 16px. Browse `.explore-card.card--outline` is transparent with a 1px `#3f3f3f` border and radius 9px. That border stayed dark after the light attribute was set.

## Badge

`.badge--new` is 10.5px / 500, radius 3px. Colour `#9d9d9d` in dark and `#5e5959` after the light attribute. The like activity badge is a 9px circle, fill `#e14d4d`, white ring `0 0 0 2px`.

## Avatar

`.avatar--medium` is a 24px box. Inner radius was not read. No crop.

## List and table

Release artwork inner radius is 4px (186px on the grid, 270px on the release page). Release title is 13px / 400. Track table header computed 14px. Row padding was not read.

Stat labels ("AVG. RATING") are 10px, tracking 0.5px, uppercase, `#9b9b9b`.

## FAQ

Home `details.toggle-section` has a 1px `rgba(0, 0, 0, 0.1)` border, height 58px when closed. The open state was not read.

## Gaps

- No crops. Page screenshots from 2026-11-21 are in [screenshots/](../screenshots/).
- Checkbox, radio, switch, select and textarea were not on the signed-out pages that were read.
- Menu, tooltip, dialog and toast were not opened. `--modal-bg`, `--context-menu-bg` and `--modal-radius` (1.2rem, 12px at the 10px root) are declared only.
- Focus ring was not computed on a control. `:focus-visible` declares outline colour `light-dark(rgb(196, 196, 196), rgb(84, 84, 84))`. `--focus-ring-color` is `#71a2f3`.
- Form error, empty and loading states were not captured. The 404 heading was read.
- Icons were not exported. The page has hundreds of inline SVGs (24px viewBox, wordmark, chevrons).
- Signed-in states (rate, like, queue, lists) were not entered.
