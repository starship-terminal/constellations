# Components

Public marketing on weave.figma.com and the signed-out sign-in card on app.weavy.ai/signin. Values are computed styles. Crops were not cut: the preview browser did not produce screenshot frames, and the sign-in page was not opened in a second browser.

## Button

Start Now (`.huge_nav-button.is-real`) is the marketing primary. At 1440 it is 40px Figma Sans, lemon `#f7ff9e`, black text, height 90px, only the bottom-left corner rounded 8px. Authored hover is rich black `#252525` with `#f4f4f4` text. That hover was not held.

Contact Sales (`.button-primary`) is lemon-100 `#f7ffa8`, richer black `#212126` text, 24px, radius 8.064px, 172 by 47. Hover computed richer black with `#f0ffff` text.

Plan CTA (`.button`) is rich black `#252525`, white text, 14.4px, padding 10.8px 21.6px, radius 4px, height 42px. Hover computed lemon `#f7ff9e` with richer black text.

The slider Try button is lemon, rich black text, 18.72px, padding 9.36px 18px, radius 0 10.08px 0 0. Authored hover swaps to rich black and lemon text.

## Link

Nav links are 12px uppercase, letter-spacing 0.15px, padding 6px 10px, radius 4px, white on a transparent fill. Hover computed white fill and rich black text. The current page computed white fill and richer black text.

Footer links (`.text-link-xsmall`) are 12px / 14.04px, white, padding 1.08px 5.04px, radius 2.16px.

Sign-in legal links are 12px, rgb(44, 44, 44), underlined.

## Text field

Not present on the signed-out surfaces. Sign-in has no email field.

## Tabs

Pricing audience tabs are 14.4px, padding 8px 16px, radius 4px. Selected is richer black `#212126` with white text. Unselected is transparent with richer black text.

## Switch

The billing control is a 32 by 16 pill, radius 144px, fill `#f1fa8c`, 0.5px border rgba(0, 0, 0, 0.2). The knob is 12 by 8, white, radius 144px. The Save 30% badge is lemon, 13px DM Sans, radius 2px. Monthly is rgba(0, 0, 0, 0.5). Annual, the active label, is rgba(0, 0, 0, 0.9).

## Card

Plan cards are `#f5f5f6`, 1px `#e6e6e6`, radius 13px, padding 21px, about 317px wide. The name is 24px weight 500. The price is 48px weight 700, letter-spacing -1.296px.

The sign-in card is white, radius 13px, padding 84px 48px, 444px wide. Its shadow matches the app elevation-100 token: `0 1px 3px #00000026, 0 0 0.5px #0000004d`.

## Accordion

FAQ rows have a 1px border at rgba(255, 255, 255, 0.15). The question is 14px white, padding 24px 0. The open answer is 14px / 17.5px, `#d0d0d2`. The icon rotates 45 degrees when open.

## Table

The comparison table uses 14px text, `#1a1a1a`, line-height 22px, cell padding 8px 12px 8px 8px. Header weight is 700.

## SSO button

Log in with Figma, Google, and Microsoft are 344 by 48, radius 8px, 1px `#e6e6e6`, white fill, 18px weight 700, label rgba(0, 0, 0, 0.3), padding 1px 16px 1px 70px. Hover computed `#f5f5f5`. They were not clicked.

## Gaps

Icon button, text area, select, checkbox, radio, menu, tooltip, dialog, toast, list row, avatar, and badge were not on the signed-out pages. Focus-visible did not match from a scripted focus. Pressed and disabled were not shown. Loading was not shown.
