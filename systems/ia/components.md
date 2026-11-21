# iA Writer components

Public marketing site at https://ia.net/writer, read signed out on 2026-11-21 in headless Chromium at 1440 x 900. Crops are from the live page. Values are computed styles, not guesses. The signed-in writing app is a download, not a web shell, so it is not here.

## Shared

One light page. Page `#f9f9f9`, ink `rgb(26, 26, 26)`, accent `#00c3ff` on the download pill with white ink in iASansNight. Nav links are the same ink as body text and turn blue only when that page is current (Buy on `/writer/pricing`, Download on `/writer/download`). Motion on the measured links and the pill is 0.2s. The header background is transparent.

## Header

Wordmark plus Support, Buy, Download, and a Menu summary. On a 390 viewport the bar keeps the wordmark and Menu only.

| Piece | Crop | Fill | Ink | Size | Radius | Duration |
|---|---|---|---|---|---|---|
| Header bar | [header](components/crops/header-default.png) | `rgba(0, 0, 0, 0)` | `rgb(26, 26, 26)` | 17.1px / 25.0156px | `0px` | 0s |
| Wordmark | [wordmark](components/crops/wordmark-default.png) | `rgba(0, 0, 0, 0)` | `rgb(26, 26, 26)` | 17.1px / auto | `0px` | 0.2s |
| Support link | [nav-link](components/crops/nav-link-default.png) | `rgba(0, 0, 0, 0)` | `rgb(26, 26, 26)` | 17.1px / 24.7812px | `0px` | 0.2s |
| Buy link | [buy-link](components/crops/buy-link-default.png) | `rgba(0, 0, 0, 0)` | `rgb(26, 26, 26)` | 17.1px / 24.7812px | `0px` | 0.2s |
| Download link | [download-link](components/crops/download-link-default.png) | `rgba(0, 0, 0, 0)` | `rgb(26, 26, 26)` | 17.1px / 24.7812px | `0px` | 0.2s |
| Menu summary | [menu-button](components/crops/menu-button-default.png) | `rgba(0, 0, 0, 0)` | `rgb(26, 26, 26)` | 17.1px / 33.3281px | `0px` | 0.2s |
| Download pill | [download-mac](components/crops/download-mac-default.png) | `rgb(0, 195, 255)` | `rgb(255, 255, 255)` | 20px / 52.0156px | `999px` | 0.2s, 0.2s, 0.2s |
| Quote more | [quote-more](components/crops/quote-more-default.png) | `rgba(0, 3, 5, 0.08)` | `rgba(26, 26, 26, 0.66)` | 20px / 22px | `999px` | 0.2s, 0.2s |

Menu panel, opened, is a white card about 291 by 551 px. Crop: [menu-panel-opened.png](components/crops/menu-panel-opened.png).

The download pill grows slightly on hover, focus, and pressed (about 286 by 52 to 292 by 53). Crops: [hover](components/crops/download-mac-hover.png), [focus](components/crops/download-mac-focus-visible.png), [pressed](components/crops/download-mac-pressed.png). The button was not activated, so no file download started.

## Gaps

- No signed-in editor, settings, or account menu. The product is a downloaded app.
- Windows download pill was not on the Mac homepage, so it was not measured.
- The Notebook shipping dialog was measured for size only. Region labels were stripped and the screenshot was not kept.
- Search on `/writer/support` was photographed, not typed into.
- Newsletter fields were left empty and not submitted.
- No checkbox, radio, switch, toast, table, avatar, or badge was a primary control on the captured pages. Pricing uses platform toggles; they are in the pricing screenshot, not cropped.
- Icons were not extracted. They stay inside the screenshots.

