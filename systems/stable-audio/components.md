# Components

Public controls on stableaudio.com, measured 2026-11-21 in headless Chromium at 1440x900. Values are token names where [tokens.json](tokens.json) has them. Crops were not cut; the states are in [screenshots/](screenshots/).

| Component | Present | States seen | Where |
|---|---|---|---|
| Button | yes | default, hover (fill flips to white) | Start free, Sign in, Make my mix, pricing plan buttons. [home-dark-default.png](screenshots/home-dark-default.png) |
| Icon button | yes | default | Help (`aria-label="Help"`), Open menu, play bowl. [home-dark-help.png](screenshots/home-dark-help.png) |
| Link | yes | default, hover (8% white wash) | Nav Pricing, Plugin, API. [home-dark-default.png](screenshots/home-dark-default.png) |
| Text field | not present | | No public field except the newsletter input, which was not focused or filled |
| Text area | not present | | |
| Select | not present | | Presets is a menu, not a select |
| Checkbox | not present | | |
| Radio | not present | | |
| Switch | not present | | |
| Tabs | yes | selected | Plugin Mac / Windows. [plugin-dark-windows.png](screenshots/plugin-dark-windows.png) |
| Menu | yes | open | Presets menu, phone nav. [home-dark-presets.png](screenshots/home-dark-presets.png), [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png) |
| Tooltip | not captured | | Help mode mounts `?` marks. Their tooltip text was not read |
| Dialog | yes | open | Signup dialog from Make my mix. Not submitted. [home-dark-signup-dialog.png](screenshots/home-dark-signup-dialog.png) |
| Toast | not present | | |
| Card | yes | default | Pricing plan cards, 4px radius, `#0b0b0b`. [pricing-dark-default.png](screenshots/pricing-dark-default.png) |
| List row | yes | default | Presets menu rows, FAQ summaries. [home-dark-faq-open.png](screenshots/home-dark-faq-open.png) |
| Table | not present | | |
| Avatar | not present | | |
| Badge | not present | | |

## Shared values

Buttons are square (`--sx-r-control: 0`). The homepage primary button on the harvest load was `#9d4edd` with black text, 36px tall, 13px / 600. A later screenshot painted the same button blue. Pricing paints the featured plan button `#aba185` (`--sx-primary` on `.sx-scope.sx-platform`). Sign in is a ghost: transparent, `#e8e8e8` text, `rgba(255, 255, 255, 0.22)` border. Hover on these buttons fills them white and turns the label black.

The signup dialog is the exception to the square rule: 440x238, background `#141414`, radius 6px.

The Presets menu is 281x486, background `rgba(31, 31, 31, 0.8)`, square, with a stacked shadow recorded in [raw/components-computed.json](raw/components-computed.json).

## Gaps

Signed-in workspace, sampler, labs, generate, checkout and account settings were not opened. Text fields, selects, checkboxes, radios, switches, toasts, tables, avatars and badges do not appear on the public pages. Focus-visible was requested in the harvest and the outline width stayed 0 on the buttons read. Disabled, loading and error states were not shown.
