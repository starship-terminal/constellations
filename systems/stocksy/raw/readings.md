# Stocksy readings

Captured 2026-11-19 from the signed-out public site in the T3 preview browser.
`preview_evaluate` read computed styles. `preview_snapshot` failed twice with
"The browser is not producing screenshot frames", so this package has no
screenshots. Headless Playwright against the same URLs returned Cloudflare
"Attention Required" (HTTP 403). Those frames were deleted and are not evidence.

Viewport readings:

| Pass | innerWidth | innerHeight | devicePixelRatio | visualViewport scale |
|---|---|---|---|---|
| Home, first read | 1169 | 731 | 2 | 1 |
| Pricing, search, photo, category, about, business, resources, 404, login | 1440 | 900 | 2 | 1 |
| Home and login after a freeform resize | 390 | 844 | 2 | 1 |

The 1169 pass is the fill viewport before resize. It is not a 1440 capture.
The 1440 and 390 passes are the measured CSS viewports after `preview_resize`.

## Pages read

- https://www.stocksy.com/ home. `body.dark-mode`. Cookie dialog dismissed with Accept All after the first read.
- https://www.stocksy.com/pricing public price table. No checkout button.
- https://www.stocksy.com/search/photo?text=ocean search results. The query was a URL, not a typed submission from an account.
- https://www.stocksy.com/photo/7746947/young-man-lays-in-bed-binge-watching-shows-on-his-laptop asset page. Add to Cart was not pressed.
- https://www.stocksy.com/category/healthcare
- https://www.stocksy.com/service/about/ light page. `body` class `service about`, not `dark-mode`.
- https://www.stocksy.com/business request form. Phone field present. Not submitted.
- https://www.stocksy.com/resources
- https://www.stocksy.com/this-page-does-not-exist-capture 404.
- https://www.stocksy.com/user/login gate only. Not submitted. Turnstile widget present.

## Computed colours

| Role | Value | Where |
|---|---|---|
| Page | rgb(0, 0, 0) | body on dark pages |
| Page, light | rgb(255, 255, 255) | /service/about/ and the 404 body |
| Text on dark | rgb(255, 255, 255) | body, .color-text-strong |
| Text default | rgb(208, 208, 208) | pricing title .color-text-default |
| Muted | rgb(163, 163, 163) | photo h1, filter titles, transparent-dark buttons |
| Soft | rgb(144, 144, 144) | .color-text-soft |
| Subtle | rgb(128, 128, 128) | price meta |
| Accent | rgb(10, 228, 124) | Add to Cart, search submit, Accept All, .btn-success |
| Accent hover | rgb(40, 208, 128) | stylesheet .btn-success:hover only |
| Dark button | rgb(41, 41, 41) | View Pricing, Like, Save, chips |
| Surface | rgb(30, 30, 30) | license button at rest, pullquote, artist pill |
| Selected license | rgb(92, 92, 92) | button.product.active |
| Hero plate | rgb(31, 36, 36) | .site-hero__bg |
| Nav solid | rgb(19, 19, 19) | .site-nav--solid |
| Nav scrim | rgba(0, 0, 0, 0.25) | .site-nav--hero |
| Footer link | rgb(206, 206, 206) | .site-footer__link |
| Step badge | rgb(54, 146, 242) | .pricing-table__badge |
| Input | rgb(255, 255, 255) fill, rgb(206, 206, 206) 1px border, radius 6px, height 48px | login and business |
| Light link | rgb(10, 43, 127) | 404 text links |
| Focus ring | rgba(13, 110, 253, 0.25) 0 0 0 0.25rem | stylesheet .form-control:focus. Live search focus showed outline none and no shadow |

## Type

Poppins on every measured element. Weights seen: 300, 400, 500, 600, 700.
Desktop h1 44px / 300. Home h1 at 390px is 32px / 300 / line-height 40px.
.text07 32px / 40px. .text06 28px / 36px. .text04 20px / 28px. Body 16px / 24px.
Nav 14px / 500 / letter-spacing 0.25px. Footer link 12px / 500 / 0.5px.
Filter title 11px / 600.

## Geometry

Nav height 60px. Hero search control 48px, radius 8px. Pill buttons 40px tall,
radius 200px, padding 8px 16px. Cookie buttons radius 30px, letter-spacing 2px,
uppercase. Collection and resource cards radius 16px. Features panel padding 32px,
border 1px solid rgb(30, 30, 30). Avatar 36px, radius 50%.

## Not entered

Login, signup, cart, checkout, Add to Cart, Follow, Comp, Share, the business
request (it asks for a phone number), newsletter, artist application, and any
payment. Cookie Accept All was clicked so the dialog would not cover later reads.
