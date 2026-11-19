# Components

Public marketing chrome on navan.com, plus the signed-out identifier page at login.navan.com. Values are computed styles from 19 November 2026. Crops were not saved: the preview browser returned "The browser is not producing screenshot frames", so this file has no images.

## Button

Primary "Get started" is a 44px pill. Background and 2px border are `rgb(99, 7, 248)`, label is white Inter 400 at 14/20, padding `10px 28px`, radius `9999px`. Transition is 150ms on colour, background and border, `cubic-bezier(0.4, 0, 0.2, 1)`. Outline offset is 4px.

"Request a demo" uses the same geometry with background and border `rgb(21, 0, 44)`.

"Reject All Cookies" is a 40px pill, white face, 1px `rgb(21, 0, 44)` border, padding `0px 20px`.

"Accept All Cookies" matches the primary colour at 40px height, padding `0px 20px`, border width 0.

Hover, pressed, disabled and loading were not captured. The stylesheet declares a 150ms colour transition, which is the only hover evidence.

## Link

"Log In" in the wide nav is Inter 700, 14/20, `rgb(21, 0, 44)`, no underline. A second Log In node, hidden at this width, computes to `rgb(99, 7, 248)`. Footer "Privacy" is 13px, weight 300, white, no underline.

## Text field

The marketing pages measured here have no painted text field. The identifier page has one email input: 490 by 52, radius 10px, padding `20px 16px 6px`, 1px border and a 1px ring both `rgb(161, 75, 227)`, font `nvn-regular` at 16px. It was left empty.

## Text area, select, checkbox, radio, switch

Not present on the public pages that were opened. The homepage checkboxes are CSS menu toggles (`display` none or 18 by 34) and are not form controls.

## Tabs

Pricing has a mobile-only plan switch (Navan Business / Navan Enterprise) that is `display: none` at 1440. Not measured in a visible state.

## Menu

The Platform menu was already open on the homepage. Items are 14/19 Inter 400, ink `rgb(21, 0, 44)`, with a 200ms transform (`xl:hover:scale-[1.025]`). The menu panel's own background was not isolated from the page.

## Tooltip

Not present.

## Dialog

The cookie sheet is a fixed bottom section, white, top radius 12px, shadow `rgba(0, 0, 0, 0.16) 0px -8px 24px`, padding `40px 64px`. Title is Sanomat 600 at 16/16, ink `rgb(21, 0, 44)`. Body is Inter 300 at 14/20. It was dismissed with "Reject All Cookies". No other dialog was opened.

## Toast

Not present.

## Card

Flip cards on the homepage are 310 by 458, white, radius 14px. Plan cards are 509 by 776, white, radius 20px, 1px border `rgb(99, 7, 248)`, padding `30px 42px 17px`. The plan name is Inter 300 at 21px in `rgb(99, 7, 248)`. "Free" and "Let's talk" are Inter 700 at 30px, ink `rgb(21, 0, 44)`. Feature rows are Inter 300 at 15px, `rgb(90, 90, 114)`.

## List row

Plan features are list rows inside the card. Row chrome beyond the text colour above was not separated.

## Table

Not present on the pages opened.

## Avatar

Not present. Review marks ("4.7 out of 5") are text, not avatars.

## Badge

Not present as a separate component. The announcement bar is a 50px strip with `linear-gradient(117deg, rgb(124, 81, 250), rgb(27, 0, 95), rgb(124, 81, 250))` and white 17px text. The declared token `--global-announcement-bar-height` is 55px; the painted bar was 50px.

## Gaps

- No screenshots or crops. The preview browser did not produce frames.
- No dark theme. The marketing site has no theme switch on these pages.
- Hover, focus-visible, pressed, disabled and loading were not forced.
- Signed-in app, booking, expense entry, cards and company SSO were not entered.
- The email field on the identifier page was not filled, so the visible error style was not measured. Hidden error nodes exist ("Please enter an email address", "Email is not valid.") at 13.92px, `rgb(30, 33, 42)`, `display: none`.
- Icon SVGs were not exported. The site uses an `icon` webfont.
