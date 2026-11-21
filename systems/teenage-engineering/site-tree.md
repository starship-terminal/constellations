# Teenage Engineering site tree

Mapped 2026-11-21 from the public site at https://teenage.engineering/ before screenshots. The official sitemap (`/sitemap.txt`, linked from `robots.txt`) lists 719 URLs. This file records every visible control on the home page and on each section index, what that control opens, and where a branch stops.

No account sign-in was found. `/login` returns the styled 404 page ("page not found"). The capture did not create an account, type a password, submit a form, or complete checkout.

The country select loaded a public store region and was left unchanged. The country name is not recorded here.

## Shell, on every page

The header and footer repeat. At 1440 the primary nav is a row of links. A `menu` button exists in the DOM (phone drawer) and is not a visible desktop control. Search, newsletter and the country select are the only non-link controls in the shell.

| Control | Opens |
|---|---|
| teenage engineering (logo) | page `/` |
| product | page `/products` |
| instruments | page `/products/instruments` |
| audio | page `/products/audio` |
| designs | page `/designs` |
| store | page `/store` |
| checkout | page `/store/checkout` (empty cart; not an auth wall) |
| deals | page `/store/special-offers` |
| newsletter | page `/newsletter` (form; not submitted) |
| instagram | external `https://www.instagram.com/teenageengineering/` |
| now | page `/now` |
| guides | page `/guides` |
| support | external page `https://support.teenage.engineering/hc/en-us` (public help centre) |
| search (button) | in-page search field (`input[name=search]`, placeholder "search"). Typing shows product and store links. Escape closes it. Not a dialog. |
| menu (button) | phone drawer of the same nav links. Not visible as a desktop control at 1440. |
| join our newsletter (button) | page `/newsletter` |
| country or region (`select[name=country]`, 70 countries) | changes the public store region. Not submitted as a profile form. Left at the loaded region. |
| in cart | page `/store/checkout` |
| latest | page `/now` |
| downloads | page `/downloads` |
| contact | page `/contact` |
| retailers | page `/retailers` |
| terms | page `/terms-and-conditions` |
| press | page `/press` |
| returns | page `/store/support/returns` |

`html` carries `data-theme="default"`. Stylesheets declare no dark theme. Theme attributes that do exist (`data-theme-variant`, `data-theme-minimode`) restyle a component, not the page.

## Home `/`

Status 200. Title "teenage engineering".

| Control | Opens |
|---|---|
| Shell controls | see Shell |
| EP/BC–1 | page `/products/bc-1` |
| LIFE IS FANTASTIC! | page `/products/ep-35` |
| Product tiles with empty link text | page `/products/bc-1`, `/products/ep-35` |

## Products `/products`

Status 200. A long index (scroll height about 28131px at 1440). Each tile is a page.

| Control | Opens |
|---|---|
| bc-1, ep-35, apc-2, sinus-transmission-completed, ep-133, ep-136, ep-40, field-system, op-xy, ep-1320, po, tp-7, ob-4, cm-15, tx-6, op-1, field-accessories, choir, field-desk, computer-1, grip-car, orthoremote, od-11, op-z, po/modular, op-1/original, po-80, ep | page `/products/<slug>` |
| riddim-n-ting | page `/store/riddim-n-ting` |

`/products/instruments` and `/products/audio` are category indexes of the same tile pattern.

### Product page (sample: `/products/ep-133`, `/products/op-1`)

| Control | Opens |
|---|---|
| buy / store links | page `/store/<sku>` |
| release notes | page `/guides/ep-133/whats-new` |
| guide | page `/guides/ep-133` |
| app links | page `/apps/update`, `/apps/ep-sample-tool` |
| accessory tiles | page `/store/<sku>` |
| Play Video, Play, Skip, Unmute, Seek, Playback Rate, Chapters, Descriptions, Captions, Audio Track, Fullscreen | in-page video player (video.js). Not a new page. |
| No compatible source (dialog, closed) | dead end in headless: the video element reports no compatible source. The controls still mount. |

Sitemap lists 62 `/products` URLs. The index links the current catalogue. Older slugs remain reachable from the sitemap and are the same page template.

## Store `/store`

Status 200. Index of categories plus product tiles (scroll height about 27655px). Add to cart is a `button[type=submit]` on each tile. The capture did not submit it.

| Control | Opens |
|---|---|
| category links: pocket-operators, field-system, ep, synthesizers, audio, cables, bags-and-cases, apparel, accessories | page `/store/<category>` (sample `/store/pocket-operators` loaded 200, title "pocket operators") |
| product tile (name or image) | page `/store/<sku>` |
| add to cart | would post the item into the cart. Not clicked. Recorded as a control that starts checkout, not an auth wall. |
| sold out, no longer available, not available | dead end: the button is present and does not navigate |
| previous slide, next slide, go to slide N | in-page carousel on a product buy page (`/store/op-1`) |
| explore | page `/products/op-1/original` (from `/store/op-1`) |

Sitemap lists 315 `/store` URLs. Category indexes and product buy pages share one template. Checkout is one page, recorded below.

### Checkout `/store/checkout`

Status 200. Title "checkout". Body: "your cart is empty." plus featured products with add to cart. No login, signup, password, or account field. Not an auth wall. The capture did not add an item or continue to payment.

`robots.txt` disallows `/store/checkout` and `/store/_feeds`. The empty cart page is still public.

## Deals `/store/special-offers`

Status 200. Same tile and add-to-cart pattern as the store index, shorter list.

## Designs `/designs`

Status 200. Editorial collaborations.

| Control | Opens |
|---|---|
| sinus-transmission-completed | page `/products/sinus-transmission-completed` |
| supreme, mind-games, popixel, playdate, mayku-multiplier, frekvens-hacks, frekvens, H, R, I-1, the-holocellulose-OD-11 | page `/designs/<slug>` |
| ob-4 off-white | page `/products/ob-4/off-white` |

Sitemap lists 12 `/designs` URLs. Each design page is the same editorial template.

## Now `/now`

Status 200. A long news index (scroll height about 75213px). Year filters and story anchors.

| Control | Opens |
|---|---|
| in-page anchors (`#sinus-transmission`, `#douglas-carr`, and the other story ids) | in-page |
| year links 2025, 2024, 2023, 2022, 2021 | page `/now/<year>` |
| product, guide, download and app links inside stories | page `/products/…`, `/guides/…`, `/downloads/…`, `/apps/update` |

## Guides `/guides`

Status 200. Index of product manuals.

| Control | Opens |
|---|---|
| each product name | page `/guides/<product>` or `/guides/<product>/<lang>` |
| language variants (en, jp, fr) | page, same guide in another language |
| module guides (oplab, rumble, line) | page `/guides/op-z/modules/<name>` |
| recycle | page `/recycle` |

Sitemap lists 237 `/guides` URLs. A guide chapter is the same manual template. Sample chapters are captured; the rest are the same pattern.

## Downloads `/downloads`

Status 200. Firmware, apps and sound packs.

| Control | Opens |
|---|---|
| product download pages | page `/downloads/<product>` |
| sound packs | page `/downloads/<product>/sound-packs` |
| apps | page `/apps/ep-sample-tool`, `/apps/update`, `/apps/drum-utility` |
| zip and pdf files under `/_img/` | file download. Not opened (binary assets, not a UI state). |
| tp-7 app | page `/redirect/tp-7-app` (redirect; not followed into a store account) |
| orthoplay | page `/products/orthoplay` |

## Press `/press`

Status 200. Press kits.

| Control | Opens |
|---|---|
| each product kit | page `/press/<slug>` |
| logo pdfs under `/_img/*.pdf` | file download. Not opened. |

Sitemap lists 34 `/press` URLs.

## Newsletter `/newsletter`

Status 200. A form: email input (`name=email`), terms checkbox (`name=termsAndConditions`), subscribe button. Privacy policy link opens `/privacy-policy`. The form was not filled and not submitted. The subscribe control is a dead end for this capture.

## Contact `/contact`

Status 200. Links to retailers, press, terms, returns, and `/ems` (events). No contact form fields on the page. No email address or phone was copied into the package.

## Retailers `/retailers`

Status 200. Title area "store locator". "visit our online store" goes to `/store`. Country groups list external retailer sites (273 external links on the loaded page). Those open other companies' shops. The capture did not follow them. No street address was written into the package.

## Legal and utility pages

| URL | Status | What it is |
|---|---|---|
| `/terms-and-conditions` | 200 | legal page |
| `/terms-and-conditions-us`, `/terms-and-conditions-ww`, `/terms-of-service` | in sitemap | regional legal copies, same template |
| `/privacy-policy` | 200 | legal page |
| `/ip-rights-te-products` | in sitemap | legal page |
| `/vdp` | in sitemap | vulnerability disclosure page |
| `/recycle` | 200 | recycling information |
| `/apps` | 200 | app index; links into `/guides` |
| `/holiday-market`, `/25-the-flipped-out-year`, `/pop-report`, `/~sketches` | in sitemap | campaign or archive pages, same shell |
| `/ems` and `/ems/lessons/…` (11 URLs) | linked from contact | education pages |
| `/login` | 404 | styled not-found page. Dead end. Not an auth wall. |
| `/support` on the main host | disallowed in robots | the visible Support control goes to `support.teenage.engineering` instead |

## Support centre `support.teenage.engineering`

Status 200 at `/hc/en-us`. Public Zendesk help centre: categories (product information, payments and safety, shipping and delivery, returns and exchange, warranty and repair, business requests, getting started, troubleshooting, other questions), a search field, and "Submit a request". Submit a request is the support form. The capture did not open it, did not search with personal text, and did not submit anything. Treated as an external public site, not part of the store package screenshots.

## Auth and account

No sign-in, sign-up, account, or password control was found on the home page, store, product pages, or checkout. `/login` is a 404. Branch stop: there is no auth wall to enter. Checkout with an empty cart stays public.

## What was not opened

- Any form submit (newsletter, support request, add to cart, checkout payment).
- External retailer sites and Instagram.
- Binary downloads (`/_img/*.zip`, `*.pdf`).
- The 237 guide chapters and 315 store SKUs beyond the indexes and the samples named above. They share the templates recorded here.
- `robots.txt` disallows `/b2b`, `/support` (main host), `/store/checkout` (visited anyway: public empty cart), `/store/_feeds`.
