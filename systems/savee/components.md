# Components

Public Savee, measured 2026-11-21. Values are computed styles. Screenshots are in [screenshots/](screenshots/). Element crops were not cut on this pass: the full frames are the evidence.

## Button

Join for free on the home nav is a black pill: background `#0a0a0a`, text `#fdfdfd`, 46 px tall, padding 16 px 20 px, 14 px saveeFont at weight 500, letter-spacing -0.14 px. The computed radius is `16777200px` (a full pill). On FAQ the same control flips: background `#fdfdfd`, text `#0e0e0e`.

See plans is the quiet sibling. `--color-accent` is `218,218,218` (`#dadada`) under `theme-light`.

Continue on the empty login wall is the same black pill at 56 px, padding 20 px 40 px, 16 px type, opacity 0.6, and `disabled` while the email field is empty. It was not clicked.

Continue with Google and Continue with Apple are 44 px transparent pills with a `#c4c4c4` 1.25 px ring and `#0a0a0a` text. They were not clicked.

Hover, focus-visible and pressed were not held long enough to record a second computed style. The home nav hover and focus frames are [screenshots/home-light-nav-hover.png](screenshots/home-light-nav-hover.png) and [screenshots/home-light-nav-focus.png](screenshots/home-light-nav-focus.png).

## Icon button

The phone bar uses an unnamed 20 px button to open the drawer. Close is a labelled button. Show another save is a square control inside the home headline. More options and Info sit on the public item page.

## Link

Nav and footer links are saveeFont. Footer link colour on the previous light reading was `#464646`. Off-site store and social links were not opened.

## Text field

Login: `input[name=email]`, type text, placeholder "Email or username", value length 0. 49 px tall, padding 12 px 0, radius 0, colour `#0a0a0a`, 16 px saveeFont. [screenshots/login-light-default.png](screenshots/login-light-default.png).

Contact name field, empty, not submitted: background `#1e1e1e`, colour `#a3a3a3`, radius 14 px, height 46 px, padding 12 px 16 px, weight 500. [screenshots/contact-dark-default.png](screenshots/contact-dark-default.png).

## Text area

Contact message, placeholder "Describe your question or issue. We'll suggest relevant help articles as you type...". Not filled. Not submitted.

## Select, checkbox, radio, switch

Not present on the marketing pages. Pricing Yearly and Monthly are `role=radio` on the same page, not a native select. Marketplace filter has native sort radios and format checkboxes. [screenshots/pricing-light-monthly.png](screenshots/pricing-light-monthly.png). [screenshots/marketplace-default-filter.png](screenshots/marketplace-default-filter.png).

## Tabs

Home and pricing use a review `tablist`. MCP uses client buttons (Claude Code, Cursor, ChatGPT & Codex, Other clients) on the same page. Workshop uses an episode row.

## Menu

The public item More options menu lists Comments, Share, Download, Find original. Those items were not followed. [screenshots/item-dark-menu.png](screenshots/item-dark-menu.png).

The phone drawer lists Features, Teams, Pricing, Join for free, Log in. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Tooltip, dialog, toast

No tooltip was hovered. The home "Get the app" card is a fixed panel, not a dialog. Sonner toast CSS is in the page stylesheet. No toast was triggered. The item menu is the dialog-like surface that was opened.

## Card

Home save tiles, pricing plan cards (Pro, Portfolio, Team, with a Popular badge on Pro), and marketplace product tiles.

## List row

Phone drawer rows and the shortcut list on `/shortcuts/`. The shortcut page is not a `table` element.

## Table, avatar

No data table on the pages opened. Review quotes use a name and a role, not an avatar component that was measured separately. The public item page shows a small face stack (`+40`).

## Badge

Popular on the Pro plan. BETA on `/site/create/`.

## Gaps

- Button hover, focus-visible and pressed colours were not remeasured.
- Signed-in library controls were not entered. `login-extracted` is not-started.
- Checkout, Apply now and Contact us were not submitted.
- Element crops were not cut.
