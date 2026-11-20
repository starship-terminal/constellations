# Components

Values are token names. Each one was read from the live signed-out site on 2026-11-19. There are no crops: the preview browser did not produce screenshot frames, and headless Playwright was stopped by Cloudflare. See [raw/readings.md](raw/readings.md).

## Button

Add to Cart on the photo page. Fill `{dark.color.action.fill}`, text `{dark.color.text.on-accent}`, radius `{core.radius.pill}`, height `{core.spacing.button}`, padding 8px 16px, type `{core.typography.button}`.

View Pricing, Like, Save, Share, Comp and the 404 pills. Fill `{dark.color.bg.raised}`, text `{dark.color.text.strong}`, same radius and height, 2px border in the same colour.

Accept All on the cookie dialog. Fill `{dark.color.action.fill}`, radius `{core.radius.cookie}`, letter-spacing 2px, uppercase, padding 8.4px 23.8px. Manage Cookies is `{dark.color.bg.input}` with a 2px `{dark.color.text.on-accent}` border.

Hover and pressed fills for `.btn-success` (`#28d080`) are stylesheet rules. They were not forced on the live control.

## Link

Nav link. `{core.typography.nav}`, colour `{dark.color.text.strong}` on dark pages. Footer link. `{core.typography.label}`, colour `{dark.color.action.outline}`. 404 text link on the light page. `{light.color.text.link}`.

## Text field

Hero and nav search. Fill `{dark.color.bg.input}`, text `{dark.color.text.on-input}`, radius `{core.radius.md}`. Hero height 48px. Nav search on the results page was 36px tall. Placeholder "Search all" and "Search keywords and hex colors".

Login email and password, and the business form fields. Fill white, 1px border `{dark.color.border.input}`, radius `{core.radius.sm}`, height 48px. The business textarea is 90px. None were filled. The business form includes a phone field, so it was not submitted.

Focus on the nav search, after `focus()` and before `blur()`, showed `outline: none` and `box-shadow: none`. The stylesheet still declares a Bootstrap ring `{dark.color.focus.ring}` on `.form-control:focus`. That ring was not the live search focus.

## Select

The hero "All types" control is a button, not a native select. Fill white, text `{dark.color.text.on-input}`, radius 8px, height 48px, weight 500. It was not opened. Search sort is text in the results masthead ("Sort by: Curated"), not a measured native select.

## Checkbox, radio, switch

Not present on the pages that were read. The cookie preferences dialog has toggles (`--cc-toggle-on-bg` `#0ae47c`). Manage Cookies was not opened, so those toggles were not computed.

## Tabs

Search type chips (Photo, Video, Illustration). Fill `{dark.color.bg.raised}`, 1px border in the same colour, text white, 14px / 500, padding 0 15px, height 41px. Outer corners radius 5px, inner corners 1px. A selected style was not found in the computed chip (`aria-selected` was absent). About has TEAM and CONTACT US as `.btn-transparent-dark` pills, colour `{light.color.text.muted}`.

## Menu

Desktop nav is a 60px bar. On the hero it is a black scrim at 25% opacity. On inner pages it is `{dark.color.bg.nav}`. Items: Insights & Trends, Pricing, For Business, For Artists, Log In, cart. At 390px the labelled links collapse (width 0) and a hamburger (`aria-label` "Main Navigation") is in the DOM. The menu was not opened.

## Tooltip

Not seen.

## Dialog

Cookie dialog, before Accept All. Primary and secondary buttons measured above. `--cc-bg` is `#f0f0f0`, `--cc-text` is `#131313`, `--cc-modal-border-radius` is `.5rem`, overlay `--cc-overlay-bg` is `#000000a6`. The dialog element itself was not given a separate computed box after the buttons were read.

Share on the photo page was not opened. Cart was not opened.

## Toast

Not seen.

## Card

Collection card radius `{core.radius.lg}`, text `{dark.color.action.outline}`. Resource card radius 16px. Home features panel padding 32px, 1px border `{dark.color.border.features}`, radius 16px. License size rows are buttons, radius 8px, height 48px. Rest fill `{dark.color.bg.surface}`. Active fill `{dark.color.bg.selected}`, text white.

## List row

Pricing price row. Label `{core.typography.lead}` in `{dark.color.action.outline}`, meta `{core.typography.label}` in `{dark.color.text.subtle}`, price `{core.typography.lead}` weight 600 in white. Footer links are 36px rows, padding 10px 0.

## Table

The pricing page is a stepped list, not an HTML table. Step badge is a 32px circle, 1px border and text `{dark.color.status.info}`, weight 700. Connector fill is the same blue.

## Avatar

Artist pill on the photo page. Image 36 by 36, radius 50%. Pill fill `{dark.color.bg.surface}`, radius 30px, height 40px.

## Badge

Pricing step number, above. `.site-nav__count` in the stylesheet is 11px / 500 on `{dark.color.action.fill}` with radius 8px. It was not in the measured nav.

## Gaps

- No component crop. Screenshot capture failed. See the coverage table in [README.md](README.md).
- Hover, pressed, disabled and loading were not forced on live controls. Hover colours in the tokens are stylesheet rules and are labelled that way.
- Checkbox, radio, switch, tooltip, toast, select menu and the open hamburger were not on screen.
- Error state of a form was not produced. Nothing was submitted.
- Focus ring in the stylesheet did not match the live search focus.
