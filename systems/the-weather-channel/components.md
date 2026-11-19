# Components

Public signed-out weather.com, measured 19 November 2026. Crops were not cut. The screenshots in [screenshots/](screenshots/) show each control in place.

## Button

The rail Sign in is a filled control: background `#252422`, text `#ffffff`, weight 600, height 56px, padding `0 12px`, radius 16px. On the phone header the same fill is 48px tall with radius 24px. See details uses `#0d142a`, white text, padding `12px 16px`, radius 8px, height 40px.

The login submit, empty, is disabled: background `rgb(84, 83, 81)`, text `rgb(205, 205, 205)`, radius 8px, height 41px, padding `10px 16px`, size 14px, weight 500. Hover and pressed were not held. Loading was not shown.

## Icon button

Hourly carousel controls are 44 by 44px, white, 1px border `oklab(0 0 0 / 0.08)`, fully rounded. The settings close control is 32 by 32px, background `#f2f2f2`, fully rounded. Nav icons are 24px SVGs with viewBox `0 0 24 24`.

## Link

Improve location precision is `#3a61cc`, 14px, weight 500. Footer links are `#252422`, 14px, no underline. Privacy-page links on trust.weather.com use a system sans stack, not Inter, and underline in the body copy.

## Text field

The open location search is white, height 48px, radius 24px, border `2px solid #3a61cc`, padding `4px 40px 4px 38px`, size 14px, placeholder "Search for a location". No query was submitted.

The login email and password fields are white, height 60px, radius 5px, border `2px solid transparent`, padding `18px 40px 0 7px`, size 16px. Labels are `rgb(111, 117, 133)`. The header search on the login page is `#f2f2f2`, radius 8px, height 48px, placeholder "Search City or Postcode".

## Text area

Not present on the public pages that were opened.

## Select

Not present as a native select. Units are radios in the More dialog. Language is a button labelled "Singapore · English". The open language list was not captured.

## Checkbox

Not present on the forecast page.

## Radio

Unit choices in the More dialog are `role="radio"`. The selected °F radio is `#252422` with white text, weight 600, size 12px, height 26px, padding `4px 10px`, fully rounded, `aria-checked="true"`. Idle radios are transparent with colour `rgb(84, 83, 81)` and weight 500.

## Switch

Not present on the public pages.

## Tabs

Today, Hourly, 10-Day, and Monthly sit in a pill row. Selected Today is `#f2f2f2` with text `#3a61cc`, weight 700, size 14px, height 48px, padding `0 16px`, radius 24px. Idle tabs are transparent with text `#252422` and the same size and weight.

## Menu

More opens a `role="dialog"` panel, 340px wide, white, shadow `rgba(0, 0, 0, 0.08) 8px 0px 30px 0px`. It holds unit radios and the language button. A dropdown menu with `role="menu"` was not found.

## Tooltip

Not captured. No tooltip was opened.

## Dialog

The More panel is the dialog that was opened. A cookie banner did not appear on weather.com. weathercompany.com showed a consent dialog and was not used as the source of these tokens.

## Toast

Custom properties for toast spacing exist (`--toast-icon-margin-end` and related names). No toast was on screen, so no toast colours were measured.

## Card

The condition hero is a section with background `#0e1d25`, radius 16px, padding 24px. On the 1169px live viewport it measured 661 by 242px. Temperature is 120px, weight 800, white, line-height 104px, letter-spacing -4.8px. Condition text is 18px, weight 700, white.

Hourly cells are 64 by 240px links, radius 12px. Time is 12px weight 700. Temperature is 20px weight 500.

Daily rows are 56px tall, radius 16px.

## List row

Daily forecast rows are the list. A settings list beyond the unit radios was not opened.

## Table

Not present on the forecast page.

## Avatar

Not present while signed out.

## Badge

Not present as a named badge. Precipitation percentages sit in the hourly strip in `#3f95b2` (`rgb(63, 149, 178)`). Sunrise is `#cb4a14`.

## Gaps

- Dark theme: the public page had `color-scheme: normal` and no theme switch. No dark tokens.
- Hover: hovering Radar in headless Chromium returned `rgba(242, 242, 242, 0.016)`, which is not a readable hover fill. Pressed was not held.
- Focus: focusing the Sign in link set `outline` to a 50% gray `oklab` colour, offset 1px, and no box-shadow. A branded focus ring was not measured on that control. The open search field uses a 2px `#3a61cc` border.
- Loading, error, empty, and validation states were not reached. The login form was not submitted.
- Signed-in forecast, saved locations, and alerts were not entered.
- weathercompany.com (IBM Plex Sans, `#001141` page, `#0f62fe` buttons) is a separate marketing system and is not in these tokens.
- trust.weather.com privacy page uses a system sans stack and a 60px heading. Those values are recorded here as a gap against the Inter forecast system, not copied into tokens.
