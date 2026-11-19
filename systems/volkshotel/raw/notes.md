# Readings

Date: 2026-11-19. Browser: T3 preview, tab opened with reuseExistingTab false. Start URL: https://www.volkshotel.nl/

`preview_snapshot` returned "The browser is not producing screenshot frames" on the home page and again on the English home. Measurements already read were kept. Screenshots were taken afterwards with headless Playwright on the same public URLs, which loaded without a Cloudflare challenge.

Cookiebot was on the first paint. "Use necessary cookies only" was clicked. Allow all was not clicked. No booking was started. No card, phone, or newsletter address was entered. The newsletter page embeds a Sendinblue form in an iframe. That iframe was not filled.

## Viewports

| Request | Measured innerWidth | innerHeight | devicePixelRatio | visualViewport scale |
|---|---|---|---|---|
| 1440 by 900, after a first 1440 request that reported 1280 by 800 | 1440 | 900 | 2 | 1 |
| 390 by 844, after a first 390 request that reported 1280 by 800 | 390 | 844 | 2 | 1 |

html class at 1440: `macos desktop landscape js webgl audio chrome mac chrome-152`. At 390 the class includes `portrait` and still includes `desktop`.

## Pages measured

| URL | Title |
|---|---|
| https://www.volkshotel.nl/ | Volkshotel Amsterdam Oost \| Hotel / Bar / Restaurant |
| https://www.volkshotel.nl/en/ | Volkshotel Amsterdam \| Hotel / Bar / Restaurant |
| https://www.volkshotel.nl/en/hotel/ | Hotel \| Volkshotel Amsterdam |
| https://www.volkshotel.nl/en/canvas/ | Canvas restaurant & bar dancing \| Volkshotel Amsterdam |
| https://www.volkshotel.nl/en/blog/ | Volkshotel \| Blog |
| https://www.volkshotel.nl/en/newsletter/ | Volkshotel \| Newsletter |
| https://www.volkshotel.nl/en/general-information-house-rules/ | Volkshotel \| General Information & House Rules |
| https://www.volkshotel.nl/en/directions/ | Volkshotel \| Directions |

Stylesheet: `https://www.volkshotel.nl/content/themes/volkshotel/public/stylesheets/main.css` (query 163 on the Dutch home, 164 on later pages). 2263 rules. Zero custom properties. Three `@font-face` rules: Apercu-Regular, Apercu-Bold (weight 700), CenturyOldstyleBT-Bold (weight 700).

## Colours computed

| Role | Computed |
|---|---|
| Page, header, module-manifest | rgb(255, 255, 255). body itself was transparent. |
| Slider, rooms, map, content block | rgb(241, 241, 241) |
| Card | rgb(255, 255, 255), 1px border rgb(213, 213, 213) |
| Footer | rgb(0, 0, 0) background, rgb(255, 255, 255) text |
| Text | rgb(0, 0, 0) |
| Muted card copy | rgb(113, 113, 113) |
| Nav button | rgba(255, 255, 255, 0.97) |
| Button at rest | white fill, 3px solid rgb(0, 0, 0), black text |
| Button hover | rgb(0, 0, 0) fill, rgb(255, 255, 255) text. Matched on BOOK ROOM and SEE OUR ROOMS. |
| Selected room tab | rgb(0, 0, 0) fill, white text, 3px black border, padding 13px 40px 9px |
| Hidden date-picker day | rgb(229, 229, 229). The picker was not opened. |

`body.single #main` declares rgb(243, 243, 243). A single post was not opened, so that value is stylesheet-only.

`.flowing-text a:not(.button):visited` declares rgb(93, 114, 177). An unvisited prose link colour was not sampled.

## Type computed at 1440

| Element | Family | Size | Line height | Tracking |
|---|---|---|---|---|
| body | Apercu-Regular | 13px | 13px | 0.5px |
| h1 Volkshotel | CenturyOldstyleBT-Bold | 39px | 42px | normal (rule says 0px) |
| h2 Canvas | CenturyOldstyleBT-Bold | 29px | 30px | normal |
| GET A ROOM paragraph | Apercu-Regular | 21px | 25px | 0.5px |
| Card paragraph | Apercu-Regular | 14px | 19px | 0.5px |
| Button | Apercu-Bold | 18px | 18px | 0.5px, uppercase |
| Bottom nav KAMERS | Apercu-Bold | 18px | 53px | 0.5px, uppercase |
| Footer paragraph | Apercu-Regular | 14px | 22px | 0.5px |
| Footer General Info | Apercu-Regular | 16px | 22px | 0.5px |
| General info h1 | CenturyOldstyleBT-Bold | 50px | 60px | normal |
| Flowing text | Apercu-Regular | 18px | 27px | 0.5px |
| Newsletter h1 | CenturyOldstyleBT-Bold | 39px | 42px | normal |
| Newsletter lede | Apercu-Regular | 26px | 42px | 0.5px |
| Blog card h2 | CenturyOldstyleBT-Bold | 25px | 28.75px | normal |
| Canvas h1 | Pressura-Medium | 39px | 42px | not re-read |
| Canvas button | Pressura-Bold | 18px | 18px | not re-read |

Pressura is not in the home `@font-face` list. It was computed only on `/en/canvas/`. A second read there gave Pressura-Bold, Georgia, serif, letter-spacing 0.5px, text-transform lowercase on "book a table".

The Canvas hero is a video (`Canvas_1080.mp4`), not a CSS background. One frame sampled from the video element at its centre was rgb(109, 79, 254). That is a frame colour, not a token. The header element behind the video computed rgb(255, 255, 255). A Zenchef iframe (`bookings.zenchef.com`, about 224 by 900) paints "Reserve a table". That widget was not entered.

At 390, home h1 is 32px / 34px, GET A ROOM h1 is 22px / 24px, general-info h1 is 30px / 35px, flowing text computed 20px. MENU text is `display: none`. BOOK ROOM stays 18px.

## Geometry

Buttons and cards computed border-radius 0px. No product control computed a box-shadow. The 3px black border is the outline. Cards are 458px wide on the hotel page at 1440. Prose column is 700px. At 390 the home column is 340px.

Button transition is 0.1s ease on background and color. Menu label transition is transform 0.3s ease-out. Hero video and the nav spinner use opacity 0.2s ease-out. main.css has no `prefers-reduced-motion` rule and no `prefers-color-scheme` rule. `focus()` on a footer link and on SEE OUR ROOMS computed `outline: none` and `box-shadow: none`.

## Menu

`#main-nav-overlay` computed `display: none`. A synthetic click on `.menu-button` did not open it. The stylesheet says the overlay is `position: fixed`, background rgba(255, 255, 255, 0.97), and its links are 40px with padding 8px 0px 12px. Those link sizes were not computed on a painted open menu.

## Not entered

Booking (`?book_room`, Mews, the date picker). Gift card. Newsletter iframe. Jobs on jobs.volkshotel.nl. Payment, phone, account.
