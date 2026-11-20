# Page layouts

Read by [tools/capture/layout.mjs](../tools/capture/layout.mjs) on the public
pages at 1440, 1920, 1024 and 390 wide; the full readings are in
[layout.json](layout.json). One theme throughout (`body.theme-light`).

## The shared shell

Every marketing page carries `header.shared-header`, position fixed, full
width: on the home page it is 108 tall (the 34 px "Introducing Fin 4" promo
banner over the 74 px nav bar); on the other marketing pages it measures 66
tall (the promo banner is not mounted there — the home reading includes it).
The nav row inside is 40 tall, starting 12 px from the left edge at 1440.
`main` is the full viewport width; sections centre their content in a column
that measures about 1164 px of the 1440 canvas (the largest `max-width`
in page flow; wider sections bleed full width). The footer is a 578 px tall
link grid on the page ground (`--body-bg` = `--color-cream`).

At 390 wide the header keeps the wordmark and swaps the nav for the menu
button (`aria-label="Open navigation menu"`), which opens a full-height
`div[role=dialog].shared-header-portal` sheet on the off-white ground.

## Per page

| Page | URL | doc height @1440 | h1 size @1440 | h1 @1920 / @1024 / @390 |
|---|---|---|---|---|
| home | `/` | 9691 | 64/64 | 80 · 48/45.6 · 40/38 |
| pricing | `/pricing` | 7162 | 48/48 | 54 · 40 · 30 |
| helpdesk | `/helpdesk` | 8181 | 64/51.2 | 100/90 · 56 · 48 |
| inbox | `/helpdesk/inbox` | 14642 | 64/64 | — |
| copilot | `/helpdesk/copilot` | 9238 | 64/51.2 | — |
| customers | `/customers` | 4727 | 64/64 | — |
| integrations | `/integrations` | 9203 | 48/48 | — |
| security | `/security` | 7107 | 64/64 | — |
| view-demos | `/view-demos` | 1458 | 80/80 | — |
| contact-sales | `/contact-sales` | 900 (one screen) | 40/40 | 40 · 40 · 40/38 |
| why-choose | `/why-choose-intercom` | 11796 | 68/68 | — |
| enterprise | `/enterprise` | 10862 | 64/64 | — |
| blog | `/blog` | 4067 | 48/48 | 54 · 40 · 30 |
| help | `/help/en/` | 2740 | 60/67.2 in **IvoryLLSub-Light** 500 | 60 · 51.2/57.3 · 40/44.8 |
| changes | `/changes/en` | 11276 | 33/40.9 system-ui | — |

Every h1 is in the `Saans` stack except the help center (IvoryLLSub-Light,
the `.intercom-legacy` serif) and the changelog (system-ui — the older
`header__lite` surface). Heading sizes step down across the declared
`--text-heading-*-{mobile,tablet,small-desktop,desktop}` breakpoints.

## Other surfaces

- `/help/en/` (the help center) centres an 830 px column under a 60 px
  header of its own — a separate shell from the marketing pages, white
  ground, the docs nav down the left of article pages.
- `/changes/en` (the changelog) has a 147 px `header__lite` header on the
  `#f3f5f7` ground, then a 900 px feed of `div.paper.newsfeed__newsitem`
  cards (white, 4 px radius).
- `view-demos` is a single screen: three fixed elements (the header plus
  demo UI chrome) and two grid areas in a 1458 px document.
- `contact-sales` is a single screen at every desktop width (the form's
  first step centred), growing to 1097 px at 390.

## Fixed elements

One fixed element on most pages: the shared header. The helpdesk adds a
second fixed strip at 1440+ (a product sub-nav); view-demos carries three.
The changelog has none (its header scrolls with the page).
