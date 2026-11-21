# Components

Values are token names. The number after each name is the resolved value from the signed-out desktop map, product `51.4.4`. Crops are in [components/crops/](components/crops/). The 2026-11-21 pass remeasured the search field (372 by 33, white, radius 18px) and the Login chip (75 by 21, `#4d4d4d`, cream text, radius 24px).

## Button

The login submit (`#submitLogin`) is the primary button. Background `background.action` (`#9d0300`), text `text.on-action` (`#f8f8f8`), Arial 18px weight 300, height 41px, padding 4.5px 18px, radius 36px. The stylesheet class is `.button`: radius `2em`, padding `.25em 1em`, weight 300.

Go Premium is `.premium-button`: background `#d49500`, white text, weight 700, height 20px, padding 3px 12px 3px 30px, radius 24px. The extra left padding holds the icon-font mark.

Hover, pressed, disabled, and loading were not opened. The loading state is a `.75s linear infinite rotate` ring in the stylesheet.

## Icon button

Map tools (zoom, 3D, about, fullscreen) are `iconfont` at 14px, cream `#fff3e1`, padding 4.2px 14px, radius 14px, transparent background. The menu control is a 42px row whose icon disc is `background.action` (`#9d0300`) with three `#f8f8f8` bars, each `0.55em` tall and `border-radius: 0.55em`, transitioning `all .3s ease-in-out`.

## Link

Menu rows are 14px / 14px, cream `#ececec`, padding 5px 10px 5px 0, height 28px, transparent background. An icon-font glyph sits in front of the label. Forgot password is 14px `#fff3e1` with a dotted underline (`.dotted`).

## Text field

Search (`#q`) is a white pill: background `#ffffff`, text `#4d4d4d`, 18px, height 33px, padding 0 32px, radius 18px, shadow `0 0 4px #000`, no border. Placeholder "Search...". A magnifier sits at 8px 8px, 18px. Focused width grew from 372px to 480px. The stylesheet clears the focus outline.

Login fields are 392px by 32px, background `#4d4d4d`, text `#ffffff`, border `1px solid #4d4d4d`, radius 3.6px, 18px, padding 4.5px 7.2px. Labels are 14px / 1.2, cream. Focus, from the stylesheet and not forced live, sets `border-color: var(--color-border)` and `box-shadow: 0 0 4px #000`. Error, not opened, sets `border-color: var(--color-orange-light)`.

## Switch

Model chips and overlay chips are `.switch__item`. Unselected: transparent, cream text. Selected on the bottom bar: background `#d49500`, text `#fff3e1`, radius 12px (model) or 14px (overlay), shadow `0 0 4px #000`, height 21px or 22px. The shared stylesheet rule paints selected chips `var(--color-ui-primary)` (`#9d0300`). The live bottom bar uses the orange override `.switch--uiswitch .switch__item.selected`.

## Menu

`#plugin-menu` is a fixed right pane, stylesheet width `var(--rhpane-width, 400px)`. The content section measured 405px by 731px, background `#3c3c3c`, text `#ececec`. Shortcut box: 8px radius, 1px solid `#4d4d4d`, padding 10px. It slides in with `transform: translate(120%)` when closed. Open state is the class `open`.

## Dialog

Login is `#plugin-login.plugin-popup`, radius 8px, shadow `0 0 4px #000`, background `#3c3c3c`. Title 28px weight 300, colour `#fff3e1`. It fades in over `opacity .5s ease-out`. It asks for email and password and offers Google, Apple, and Facebook. Register uses the same popup and adds username, confirm password, a newsletter checkbox, and a captcha. Nothing was entered.

## Card

The startup article is a 397px by 55px row, class `bg-gray-dark fg-white`, 16px, line-height 1.4, letter-spacing 0.02em, padding `5px 10px 5px 110px`. The close control is 18px, colour `var(--color-yellow)`, opacity transition 0.3s, hover opacity 0.7.

## List row

Search results are 16px white links, about 31px tall, padding 5px 5px 5px 7px. The list itself had a transparent background on this load.

## Table

The place detail table (`.main-table`) is `#f8f8f8` with `#000000` text at 12px, 200px tall, full width. The hour marker is `#d49500`. The footer (`.detail-box-desktop`) is `#9d0300` with white text, 69px tall.

## Badge

`.badge` is weight 600, radius `.3em`, padding `.15em .5em`. A `NEW` badge on the menu computed to 34px by 15px, background `#c42f2f`, white text, class `badge--rounded size-xs bg-error`.

## Gaps

- Text area, radio, toast, avatar: not on the signed-out surfaces that were opened.
- Checkbox, select, tooltip: in the stylesheet, not opened.
- Button hover, pressed, disabled, loading: not opened.
- Form error: not submitted.
- Phone computed styles: a 390px screenshot exists; the values above are from the desktop page.
- Signed-in settings, favourites, alerts: behind a password login. Not entered.
- Canvas map colours: not CSS.
- Icon font glyphs: not extracted. See [icons/](../icons) absence and the catalog `layoutGaps`.
