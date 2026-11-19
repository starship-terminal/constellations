# Patterns

Public marketing pages, signed out, 2026-11-19. Screenshots are in [screenshots/](screenshots/). `preview_snapshot` could not produce frames, so these PNGs come from a later headless Playwright pass on the same public URLs.

## Home

Dutch home and English home share one stack. A white header holds BOOK ROOM at the left and MENU at the right. A promo sign sits over the hero. Below that, a white manifesto, a grey slider band (`light.background.band`), a grey rooms call to action, a four-up venue block, a white split, a grey map, and a black footer.

[screenshots/home-light-default.png](screenshots/home-light-default.png) is the English home at innerWidth 1440. [screenshots/home-light-phone.png](screenshots/home-light-phone.png) is the same URL at innerWidth 390. At 390 the MENU label is hidden and the hamburger remains.

## Rooms

`/en/hotel/` puts STANDARD ROOMS and SPECIAL ROOMS as square tabs over a grey band of white cards. Each card has a 1px grey border and a BOOK ROOM outline button. The booking picker was not opened.

[screenshots/hotel-light-default.png](screenshots/hotel-light-default.png)

## Venue

`/en/canvas/` swaps the display face to Pressura. The top control says "book a table" instead of BOOK ROOM. The page still uses the white page, grey bands, 3px black buttons, and the black footer.

[screenshots/canvas-light-default.png](screenshots/canvas-light-default.png)

## Blog

`/en/blog/` is a grey field of white cards. Category links sit above the cards as uppercase text. There is no search field.

[screenshots/blog-light-default.png](screenshots/blog-light-default.png)

## Prose

General information is a 700px column of Century Old Style titles and Apercu paragraphs on white. At 390 the column is 340px and the title drops from 50px to 30px.

[screenshots/info-light-default.png](screenshots/info-light-default.png)

## Newsletter

The page title and the line "No spam. No regrets." are on the Volkshotel page. The form itself is a Sendinblue iframe. It was not filled.

[screenshots/newsletter-light-default.png](screenshots/newsletter-light-default.png)

## Footer

Every measured page ends in a black footer with white Century Old Style column titles, 14px contact copy, and 16px rule links. Social marks are 30px.
