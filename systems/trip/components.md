# Components

Values are token names where a token exists. Sizes are computed styles from the live page. There are no crops: the preview browser returned no screenshot frames, and a fresh headless session was stopped by Trip's verification wall.

## Button

Search on the home card, class `tripui-online-btn-large tripui-online-btn-solid-primary`.

| State | What was read |
|---|---|
| Default | Background `light.color.bg-brand` (`#2c61fe`), text `#fff`, font 700 16px/24px Trip Geom, height 48px, padding 0 16px, radius `core.radius.s` (4px), no shadow. At innerWidth 1440 a different Search control in the header measured 38px tall and weight 500 |
| Hover | Stylesheet `.tripui-online-btn-solid-primary:hover:not(:disabled)` sets background `rgb(41, 83, 214)` (`light.component.button-primary-hover-background`). Not confirmed with a pointer |
| Header Sign in hover | `.mc-lhd-login-btn:hover` sets background `rgb(44, 89, 229)` |
| Disabled | Continue with email on `/account/signin` is `disabled`, background `rgb(206, 210, 217)`, text `#fff`, height 56px, radius 4px, font 700 18px/24px. The token `--compButtonDisabledFilledBackgroundColor` is `#b9bec7` and was not what painted |
| Secondary | `--compButtonSecondary*` is transparent fill, brand border, brand text. Not seen as a painted control on these pages. Support's Search Bookings is a white wireframe button, 36px, radius 4px, border `rgba(255,255,255,0.6)` |
| Pressed, loading | Not captured |

Token sizes: large height `--compButtonLHeight` 56px, font 18px, weight 700, radius 4px. Medium height 38px, font 16px, weight 500. Small height 34px, font 14px, weight 400.

## Text field

| Control | What was read |
|---|---|
| Destination, home and hotels | Input font 700 16px Trip Geom, colour `light.color.text-primary`, placeholder "Where to?", transparent background, no own border. The row around it is white, radius 8px, border 1px `rgb(218, 223, 230)` (`light.component.search-field-border`) |
| Dates and guests | Same 700 16px. Shown as "Thu, Nov 19 - Fri, Nov 20" and "1 room, 2 adults, 0 children". Not opened |
| Email, `/account/signin` | Height 56px, padding 16px 12px 16px 8px, radius 4px, border 1px `#d4d7de` at rest, border `light.color.bg-brand` when focused, font 700 16px/22px, placeholder "Please enter an email address". Not filled |
| Header search | 14px, padding 8px 34px 8px 8px, radius 4px, height 32px |
| Error, disabled | Tokens only: `--compTextinputErrorColor` `#d02c2a`, disabled background `#f6f7fa`, disabled text `#b9bec7` |

## Tabs

Home search product tabs, class `mc-srh-box__tab-item`. Six items: Hotels & Homes (active), Flights, Trains, Cars, Attractions & Tours, Flight + Hotel.

Active label: 500 14px/21px, colour `light.color.text-brand`. Rest label: 500 14px/21px, colour `light.color.text-primary`. Tab hit area about 96 by 69 px. Hover rule sets the label to brand blue. `--compTabsItemFontSize` is 30px and does not match this paint. Indicator height token is 4px, radius 2px; the indicator element was not measured on its own.

## Card

| Card | What was read |
|---|---|
| Search | `.mc-srh-box.experiment-e`, white, radius 16px (`core.radius.16`), shadow `light.shadow.search-card` (`rgba(7, 20, 60, 0.16) 0px 0px 4px` plus `rgba(7, 20, 60, 0.12) 0px 8px 32px`). Width 1096px at innerWidth 1440, height 260px |
| Coupon | `.online-mkm-coupon-content-card`, radius 8px, shadow `0px 4px 16px rgba(18, 24, 38, 0.08)`, about 278 by 154 px |
| Hotel | `.hotel-recommend-card-default` on `/hotels/`, white, radius 8px, border 1px `#d4d7de` on the outer card, shadow `0px 2px 6px rgba(0, 0, 0, 0.08)`, about 264 by 371 px |
| Sign-in | Left panel white, radius `8px 0 0 8px`, padding 64px 16px 40px, width 474px. Right aside `#f6f7fa`, radius `0 8px 8px 0`, width 384px, height 650px |

## Link

Header "Find bookings" is 500 14px/22px, colour `#121826`. "Sign in or register" under the search card is 14px/21px, colour brand blue. Support FAQ chips are links: background `#f5f7fa`, padding 12px 16px, radius 4px, font 400 14px/18px.

## Dialog, checkbox, radio, switch, badge, toast

Declared as `--comp*` tokens in [tokens.json](tokens.json) `light.component`. Not painted on the pages that were read, except a suggested-language dialog that stayed closed. No values were read from an open dialog.

## Gaps

- No screenshots and no crops. Preview snapshot failed with "The browser is not producing screenshot frames". Headless Chromium against www.trip.com was redirected to verify.trip.com. Those frames were not kept.
- Search was not submitted. No results, filters, sort, map, or empty results.
- The email field was focused and not filled. Continue with email, Google, Apple, and Facebook were not pressed. No account was created. No phone, card, or code was entered.
- No booking, payment, or checkout page was opened.
- Checkbox, radio, switch, tooltip, toast, menu, select, and open dialog were not on the pages read.
- Pressed and loading states were not captured. Hover colours are stylesheet rules.
- Motion was not probed under `prefers-reduced-motion`.
- Phone width (390) was not captured.
- Dark theme was not present.
- Icons were not extracted. The icon font `fi` and inline marks stay in the product.
