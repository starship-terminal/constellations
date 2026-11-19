# Components

Public signed-out surfaces on skyscanner.com.sg, 19 November 2026. Crops are missing because the preview browser returned no screenshot frames.

## Button

Search is a featured button: background `#0062e3`, white label, weight 700, 16px, radius 12px. Desktop height 72px, padding 12px 16px, width 84px. Phone height 48px, full width of the form (358px at 390).

Log in is canvas `#eff3f8`, ink `#161616`, height 36px, radius 8px, padding 6px 16px, weight 700.

Accept all is primary `#05203c`, white, height 40px, radius 8px. Accept essential only and the login-provider buttons are secondary `#e0e4e9`, height 40px (providers 48px large). Continue is featured, height 48px, radius 8px.

The stepper is an icon button, 36px square, radius 8px, padding 6px 10px, secondary fill. The decrease control that cannot go lower uses `rgba(0, 0, 0, 0.2)` for its label.

Hover, pressed and loading were not captured. Pressed fills exist as tokens (`#154679` primary, `#024daf` featured, `#c1c7cf` secondary) and were not painted.

## Icon button

Swap origin and destination is 40px, radius 50%, 3px solid `#05203c`, white fill, transform 400ms ease.

Close modal is 32px, radius 100%, white fill.

## Link

Help in the hero is white, no underline. Modal legal links are `#626971`, 12px, line-height 16px. Help Centre links are `#0a6cff`, no underline.

## Text field

The origin field is a white 72px row, padding 0 16px, radius 12px on the start side. The input is 16px, black, placeholder "Country, city or airport". The placeholder line is `#626971`. Focus paints a 2px white ring on the field. Phone fields are 48px, radius 12px on the top corners, 358px wide at 390.

The field was not filled. No validation error was shown.

## Text area

Not present on these pages.

## Select

Cabin class sits in the travellers popover as a list, not a native select. The popover is white, radius 12px, shadow `rgba(37, 32, 31, 0.25) 0px 4px 14px 0px`, 392 by 360. Option styles were not isolated.

## Checkbox

20px square, radius 4px, 3px solid `#626971` on white. The checked "Add a place to stay" box is `#0062e3` fill and border. Disabled and indeterminate were not painted. Token `--bpk-private-checkbox-bg-default-checked` is `#0062e3`.

## Radio

Not painted. Cabin class did not expose a visible radio input.

## Switch

A switch input exists for "Include nearby airports" with height 0. The track was not painted. Gap.

## Tabs

Flights, Stays and Cars. Selected Flights is `#0062e3`, white, height 36px, radius 18px, padding 0 16px, inset ring of the same blue. Idle Stays has an inset ring `rgba(255, 255, 255, 0.2)`. Group gap 8px.

## Menu

The travellers popover and the origin autosuggest are the menus that opened. Autosuggest option rows were not painted in the measured box. Culture and currency menus were not opened.

## Tooltip

Not present.

## Dialog

The cookie banner is `#f1f2f8`, shadow `rgba(37, 32, 31, 0.25) 0px 4px 14px 0px`, height 372 at 1169. It was dismissed with "Accept essential only".

A login modal opened over the search form. White, radius 12px, shadow `rgba(37, 32, 31, 0.25) 0px 12px 50px 0px`. Title is hero-6: 40px, weight 900, line-height 40px. It was closed. No email was entered.

## Toast

Not present.

## Card

Homepage nav card is `#05203c`, radius 12px, height 72px, shadow `rgba(37, 32, 31, 0.3) 0px 1px 3px 0px`. It transitions background-color 200ms ease and box-shadow 200ms ease-in-out.

The graphic promo card is `#eff3f8`, radius 12px, height 460 at desktop. Its headline is 48px, weight 900, line-height 48px, letter-spacing -1.92px. At 390 the same headline is 32px, weight 700.

## List row

Accordion questions are 55px rows, 16px, weight 400, ink. Expanded content was not opened.

## Table

Not present.

## Avatar

Not present.

## Badge

Not painted. Badge tokens exist (`--bpk-private-badge-*`) and were not on a visible badge.

## Gaps

- No screenshots or crops. The preview browser returned "The browser is not producing screenshot frames".
- Button hover, pressed, loading and disabled painted states.
- Switch track.
- Radio, text area, tooltip, toast, table, avatar, badge.
- Autosuggest option rows and culture menu.
- Dark theme. Declared sheets include a dark canvas. The painted page resolved light tokens, and no theme switch was found.
- Reduced motion was read from 18 stylesheet rules, not from a live emulation pass.
