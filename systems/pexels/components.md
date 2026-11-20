# Components

Values are computed styles from the signed-out site, 2026-11-19. Crops are from the 1440×900 home screenshot (PNG 2880×1800).

## Button

Join is the primary control: 48px tall, 12px radius, padding 1px 20px, background #191919, text #ffffff, Canva Sans 17px, tracking -0.5px. The stylesheet names that colour `Button_color-shadow`.

![Join](components/crops/button-primary-default.png)

Load More is the white button: background #ffffff, border 1px #ededed, same height and radius. Free download and the Log in submit use alien #54ca84 with white text. Google sign-up is a white button with label rgb(101, 111, 107).

Declared, not forced live: shadow hover and focus-visible move the fill to #393939. Alien focus-visible moves it to #32ac64. A disabled shadow button uses #cdcdcd.

## Search

The home search container is #f7f7f7, 12px radius, 72px tall, padding 12px. The input inside is 17px, transparent, placeholder "Search for free photos".

![Search](components/crops/search-default.png)

## Tabs

Home is a black pill, 30px radius, 48px tall, white 17px label. Inactive tabs are transparent with #393939 text.

![Home tab](components/crops/tab-selected.png)

## Text field

Join and login inputs are 48px, radius 10px, padding 4px 16px, white fill, text #393939, 15px on join and 17px on login. Placeholders: First name, Last name, Email, Password, and name@email.com.

## Card

Photo cards use 12px radius. The first home card measured 259×425.

## Link

Nav labels (Explore, License) are 17px #191919 with no underline. Footer column links match. Legal links on the join form are 14px #747474.

## Logo

The wordmark is an inline SVG, 85×38, viewBox 0 0 512 227.

![Wordmark](components/crops/logo-default.png)

## Gaps

Checkbox, radio, switch, select, textarea, tooltip, toast, dialog, table, avatar, and badge were not on the pages that stayed open long enough to measure as their own controls. The cookie banner has a checkbox list that was not opened. Hover, pressed, disabled, loading, and error were read from stylesheet rules, not from a live forced state. No form was submitted, so no validation error was shown.
