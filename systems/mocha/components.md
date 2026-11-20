# Mocha components

Measured on docs.getmocha.com and the app.mocha.app 410 page, 2026-11-19. Desktop is 1440×900. Crops are 2×. Token names point at [tokens.json](tokens.json).

## Button

The top-bar "Go to Mocha" control is a transparent anchor over a 36px face. The face is `span.absolute.inset-0` with `bg-primary-dark` in light (`#000000`) and the light primary in dark (`#ffffff`). Radius is 12px (`core.radius.lg`). Label is 14px medium.

![Go to Mocha, light](components/crops/button-primary-light.png)

![Go to Mocha, dark](components/crops/button-primary-dark.png)

Focus on the anchor paints a 1px auto outline in `light.focus` (`#513a06`) or `dark.focus` (`#b4ff6a`). Hover on the face is an opacity change on the span (`group-hover:opacity-[0.9]`), not a new fill.

The 410 page has one control, a white pill. Border `#d7d1ca`, radius 999px, padding 13px 18px, 15px weight 650. Hover moves the border to `#a9a199` and translates the link up 1px. Focus-visible outline is 3px `#ef6a3a`, offset 3px.

![Shutdown link](components/crops/button-shutdown-default.png)

## Link

Sidebar links are 14px. The current page uses a 12px radius, padding 6px 12px 6px 16px, and a 10% tint of the accent. Light tint is `oklab(0.364975 0.0100353 0.0705809 / 0.1)` with text `#513a06`. Dark tint is `oklab(0.921162 -0.129713 0.145731 / 0.1)` with text `#b4ff6a`.

![Current sidebar link, light](components/crops/nav-active-light.png)

![Current sidebar link, dark](components/crops/nav-active-dark.png)

"Support" in the top bar is 14px medium, `#525150` in light and `#a0a09e` in dark, with no fill.

## Text field

The top-bar search is a button, 36px tall, 12px radius, page-coloured fill, 14px label, padding 0 12px 0 14px. A 1px ring sits in the box-shadow, not the border.

![Search, light](components/crops/search-default-light.png)

![Search, dark](components/crops/search-default-dark.png)

Opening it shows a dialog, 640px wide, 20px radius, page fill. The input is transparent, 16px, with 30px of left padding for the icon. Nothing was typed.

![Search dialog, light](components/crops/search-dialog-light.png)

![Search dialog, dark](components/crops/search-dialog-dark.png)

There is no text area, select, checkbox, radio, or switch on the captured pages.

## Accordion

FAQ rows are `details`/`summary`. A closed summary is 52px, padding 14px 20px, 16px, transparent. Open, the summary fill becomes gray-100 (`#f0efee`) in light and gray-800 (`#272725`) in dark. The answer is 16px, gray-700 in light and gray-400 in dark.

![Closed FAQ row](components/crops/accordion-default-light.png)

![Open FAQ row, light](components/crops/accordion-open-light.png)

![Open FAQ row, dark](components/crops/accordion-open-dark.png)

## Menu

The theme button opens a menu with System, Light, and Dark. Items are 14px, 36px tall, 12px radius. The current item uses the accent colour.

![Theme menu, light](components/crops/theme-menu-light.png)

![Theme menu, dark](components/crops/theme-menu-dark.png)

## Callout

The shutdown notice on docs is a 16px-radius card, padding 16px 20px, 1px border. Light fill `#fefce8`, border `#fef08a`. Dark fill is `oklab(0.68064 0.0348215 0.137956 / 0.2)`, border `#713f12`.

![Callout, light](components/crops/callout-default-light.png)

![Callout, dark](components/crops/callout-default-dark.png)

## Heading

Page titles are 36px, weight 600, line-height 40px, letter-spacing -0.025em. Light `#191816` (gray-900). Dark `#e0e0de` (gray-200).

![FAQ heading](components/crops/heading-default-light.png)

The 410 heading is 68px, weight 700, line-height 0.98, letter-spacing -0.055em, colour `#221f1c`. That size is `clamp(42px, 8vw, 68px)` in the page's own stylesheet.

![Shutdown heading](components/crops/heading-shutdown.png)

## Gaps

Text area, select, checkbox, radio, switch, toast, table, avatar, and badge are not on the captured pages. The product app that would have had them returns 410. Disabled and loading states were not on screen. The Go to Mocha hover is an opacity change on a child span; the anchor's computed colour did not change.
