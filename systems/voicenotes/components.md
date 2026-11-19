# Voicenotes components

Measured on the public site on 19 November 2026, viewport 1169 by 731. No crops: the preview browser did not produce screenshot frames.

## Button

Nav primary, "Start for free": background `#0D0D0D`, text `#FFFFFF`, Inter Medium 14px / 20px, padding 12px 20px, radius 9999px, height 36px.

Hero primary, "Book a demo": same fill, Inter SemiBold 15px / 20px, padding 12px 24px, height 46px.

Hero secondary: transparent fill, 1px solid `#0D0D0D`, same type and padding as the hero primary.

Pricing quiet, "Get started" and "Talk to sales": background `#E6E5E0`, text `#0D0D0D`, 1px border `rgba(34, 34, 34, 0.08)`, radius 9999px, height 44px, Inter Medium 16px.

Pricing primary: `#0D0D0D` fill, white text, height 44px.

Hover on login provider buttons is declared as `rgba(13, 13, 13, 0.03)` in `.tw-grey-bordered-btn:hover`. Pressed, disabled and loading were not on the page.

## Link

Nav links are Inter Medium 16px / 21px, `#0D0D0D`, padding 6px 12px, pill radius.

Blog post links compute to `#0088FF` with an underline.

"Sign up" in the login modal is `rgba(0, 0, 0, 0.5)`, underlined, Inter Medium 14px.

## Text field

Login email and password fields: height 48px, width 306px, radius 16px, padding 0 16px, background `rgba(13, 13, 13, 0.05)`, 2px transparent border, Inter Regular 14px, colour `#0D0D0D`. Placeholder "Email Address" and "Password".

Focus, from `.tw-input-common-v2:focus`: border colour `#0D0D0D`. Hover, from the same rule: background `rgba(13, 13, 13, 0.1)`. Error and disabled were not shown. Nothing was typed or submitted.

## Card

Login card: white, 450px wide, radius 16px, padding 40px 24px.

Pricing plan card: white, 234px wide at this viewport, radius 4px, border `1px solid rgba(34, 34, 34, 0.08)`, padding 16px 16px 28px.

Home feature cards also use 16px and 24px radii. A demo card shadow was truncated in the reading and is not tokenised.

## Tabs

Pricing Monthly / Annual is a pill track, background `#F2F1ED`, radius 9999px, padding 2px, height 42px. Selected label is `#0D0D0D`. Idle label is `rgba(13, 13, 13, 0.6)`. Both are Inter Regular 16px / 24px.

## Badge

"2 months free": background `#E6F9EB`, text `#006119`, border `1px solid rgba(46, 204, 86, 0.08)`, radius 48px, padding 4px 8px, Inter Regular 12px.

## Accordion

Pricing FAQ questions are buttons, Inter Regular 16px, `#0D0D0D`, padding 16px 0, height 56px. Opened, the answer wrapper is `display: grid` with `grid-template-rows: 68px`. Answer text is 16px / 24px, `#000000`.

## Icon button

The login close control is 32 by 32, radius 9999px. Its icon SVG was not extracted.

## Gaps

Text area, select, checkbox, radio, switch, menu, tooltip, toast, list row, table, avatar: not present on the public pages that were opened.

Dialog exists as the login modal. Toast, empty, loading and error states were not shown.

Dark theme classes exist in the stylesheet (`.dark`, `dark:bg-darkTheme2` `#272829`) and were not applied on the live public pages.

Phone width (390) was not measured. The only viewport read was 1169 by 731 at devicePixelRatio 2.
