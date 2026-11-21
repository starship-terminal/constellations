# Dopper site tree

Mapped on 2026-11-21 from [https://dopper.com/](https://dopper.com/), which redirects to `https://www.dopper.com/`. Signed out. Cookiebot was hidden, never accepted. No form was submitted. No password was typed.

Two hosts share one chrome bar (`dopper-navigation`):

- `www.dopper.com` is the marketing site (Next.js on Vercel, Storyblok). English lives under `/en/`. The sitemap index also lists `/nl/`, `/de/` and `/fr/` (112 English URLs). Those locales were not walked page by page. The EN control opens them.
- `shop.dopper.com` is the Magento store (`Dopper/dopper_b2c`). The cart icon always goes to the basket.

Account sign-in is not in the public nav. `https://dopper.com/account/login` is a not-found page (probe: no form). The shop login form exists only at a Magento URL that the public nav does not link. That URL is a login wall. The branch stopped there. Checkout past an empty basket was not opened. No filled-cart checkout was reached, and none was invented.

## Global chrome

The bar is a `dopper-navigation` custom element (shadow root), 110px, fixed.

| Control | Opens |
|---|---|
| Bottle | In-page panel. Links below. Chevron flips when open. |
| Travel Mug | In-page panel. Same shape as Bottle. |
| Tap | In-page panel. |
| Mission | In-page panel. |
| Get Involved | In-page panel. |
| Wordmark | `https://www.dopper.com/` (relative `/` from the marketing host; from the shop it still points at the marketing home in the shadow link list as `/`) |
| Impact report | `https://www.dopper.com/en/mission/impact-report-2025` |
| Find a Store | `https://www.dopper.com/en/about/store-locator` |
| For Businesses | In-page panel. |
| EN | Language menu: English (`/en/`), Nederlands (`/nl/`), Deutsch (`/de/`), Français (`/fr/`). Take me there on the locale overlay goes to the matching locale home. |
| Cart icon | `https://shop.dopper.com/checkout/cart/` (empty basket when nothing is added). Not a drawer. |
| Menu toggle (390) | Blue full-screen drawer with the same six items, plus Impact report and Find a Store as pills. Close returns to the page. |

Footer (`dopper-footer`), both hosts:

| Control | Opens |
|---|---|
| Instagram | `https://www.instagram.com/dopper_official/` (external) |
| Facebook | `https://facebook.com/DopperBottle/` (external) |
| LinkedIn | `https://www.linkedin.com/company/dopper/` (external) |
| TikTok | `https://www.tiktok.com/@dopper_official/` (external) |
| Newsletter submit | Not used. Field left empty. |
| FAQs | `https://help.dopper.com/` (external help centre) |
| Care Manual | `https://dopper.com/en/products/bottle-care` |
| Delivery & Shipping | `https://help.dopper.com/en/what-is-the-delivery-time` (external) |
| Returns & Warranty | `https://dopper.com/en/legal/returns-warranty` |
| Find a Store | `https://www.dopper.com/about/store-locator` |
| All Products | `https://shop.dopper.com/` |
| Personalise a Bottle | `https://dopper.com/en/products/personalise-a-bottle` |
| Personalise a Travel Mug | `https://www.dopper.com/en/products/personalise` |
| Accessories | `https://shop.dopper.com/accessories` |
| Spare Parts | `https://shop.dopper.com/spare-parts` |
| Mission | `https://dopper.com/en/mission/story` |
| Annual Reports | `https://www.dopper.com/en/mission/impact-report-2025` |
| Blog | `https://dopper.com/en/blog/` |
| Contact | `https://dopper.com/en/about/contact` |
| Dopper Team | `https://dopper.com/en/about/team` |
| Vacancies | `https://jobs.dopper.com/` (external) |
| Accessibility | `https://www.dopper.com/en/about/accessibility` |
| Order Customised Bottles | `https://dopper.com/en/products/custom` |
| Order Customised Travel Mugs | `https://www.dopper.com/en/products/travel-mug-b2b` |
| Get the Dopper Water Tap | `https://dopper.com/en/products/tap` |
| Sell Dopper products | `https://order.dopper.com` (external retail-partner order site; not walked) |
| Terms & conditions | `https://dopper.com/en/legal/terms-conditions/` |
| Privacy Policy | `https://dopper.com/en/legal/privacy-policy` |
| Cookies | `https://dopper.com/en/legal/cookie-policy` |

External certification marks in the footer (B Corp, Cradle to Cradle, 1% for the Planet, Climate-ID, Thuiswinkel) leave the site. Not walked.

## Bottle panel

| Control | Opens |
|---|---|
| All products | `https://shop.dopper.com/` |
| Buy a Bottle | `https://shop.dopper.com/bottles` |
| Buy a Flip Straw bottle | `https://shop.dopper.com/bottles?bottle_collection=5587` |
| Personalise a Bottle | `https://www.dopper.com/en/products/personalise-a-bottle` |
| Buy Accessories | `https://shop.dopper.com/accessories` |
| Buy Spare Parts | `https://shop.dopper.com/spare-parts` |
| Care for Your Bottle | `https://help.dopper.com/en/how-do-i-clean-and-care-for-my-dopper-bottle` (external) |
| Give your bottle a second life | `https://www.dopper.com/en/products/second-life` |
| Customised bottles | `https://www.dopper.com/en/products/custom` |
| Get started (promo card) | `https://www.dopper.com/products/custom` |

## Travel Mug panel

| Control | Opens |
|---|---|
| All products | `https://shop.dopper.com/` |
| Buy a Travel Mug | `https://shop.dopper.com/travel-mug` |
| Personalise a Travel Mug | `https://www.dopper.com/en/products/personalise-a-bottle` |
| Buy Accessories | `https://shop.dopper.com/accessories` |
| Buy Spare Parts | `https://shop.dopper.com/spare-parts` |
| Customised Travel Mugs | `https://www.dopper.com/en/products/travel-mug-b2b` |

## Tap panel

| Control | Opens |
|---|---|
| Find a Tap Near You | `https://www.dopper.com/en/products/tap-map` |
| Get the Dopper Water Tap | `https://www.dopper.com/en/products/tap` |
| Bring tap water to your event | `https://www.dopper.com/en/get-involved/tap-water-at-events` |

## Mission panel

| Control | Opens |
|---|---|
| Story: Why We Exist | `https://www.dopper.com/en/mission/story` |
| Sustainability | `https://www.dopper.com/en/mission/sustainability` |
| Impact: Our Progress and Annual Reports | `https://www.dopper.com/en/mission/impact-report-2025` |
| Nepal | `https://www.dopper.com/en/mission/nepal` |
| Blog | `https://www.dopper.com/en/blog/` |

## Get Involved panel

| Control | Opens |
|---|---|
| Sign the pledge | `https://www.dopper.com/en/get-involved/pledge/` |
| Teach Sustainability in Schools | `https://www.dopper.com/en/get-involved/schools` |
| Bring tap water to your event | `https://www.dopper.com/en/get-involved/tap-water-at-events` |

## For Businesses panel

| Control | Opens |
|---|---|
| Customised bottles | `https://www.dopper.com/en/products/custom` |
| Customised Travel Mugs | `https://www.dopper.com/en/products/travel-mug-b2b` |
| Dopper Tap | `https://www.dopper.com/en/products/tap` |
| Login as a retail partner | `https://order.dopper.com` (external; not walked; treated as a partner login, not opened past the link) |
| Become a retailer | `https://www.dopper.com/en/about/become-a-dopper-retailer` |

## Home (`https://www.dopper.com/`)

| Control | Opens |
|---|---|
| Shop our collection | `https://shop.dopper.com/` |
| Watch now | `https://www.dopper.com/en/campaigns/gifting-2026-1` |
| Pause video | Pauses the hero film. In-page. |
| Scroll to next section | Scrolls the page. |
| Collection cards (Travel Mug, Insulated, Steel, Original, Accessories) | In-page slider. Dots: Go to page 0, Go to page 1. |
| Shop Travel Mug | `https://shop.dopper.com/travel-mug` |
| Learn more about the Travel Mug | `https://www.dopper.com/en/products/travel-mug` |
| Learn more about Insulated | `https://www.dopper.com/en/products/insulated` |
| Shop now (bottles) | `https://shop.dopper.com/bottles` |
| Customise a product | `https://www.dopper.com/en/products/personalise` |
| Annual Impact Report 2025 / Discover the report / Read our 2025 Impact Report | `https://www.dopper.com/en/mission/impact-report-2025` |
| Read our mission | `https://www.dopper.com/en/mission/story` |
| Learn about packaged water | `https://www.dopper.com/en/blog/just-refill` |
| Discover corporate gifts | `https://www.dopper.com/products/custom` |
| Product tiles (Insulated, Steel, Original) | Shop product URLs for that line. |
| Learn more cards (Travel Mug, Bottle, Tap, Map, Community) | Matching product, tap, tap-map and pledge pages. |

## Marketing pages walked

Photographed at 1440 and 390 unless noted. Interactions are the ones on the page, not a second copy of the global chrome.

| Page | URL | Controls beyond chrome |
|---|---|---|
| Home | `https://www.dopper.com/` and `https://www.dopper.com/en` | See home table. |
| Story | `https://www.dopper.com/en/mission/story` | In-page story sections. |
| Sustainability | `https://www.dopper.com/en/mission/sustainability` | In-page sections. |
| Impact 2025 | `https://www.dopper.com/en/mission/impact-report-2025` | Report sections. |
| Nepal | `https://www.dopper.com/en/mission/nepal` | In-page sections. |
| Impact calculator | `https://www.dopper.com/en/mission/calculate-your-impact` | Calculator UI. Not submitted. |
| Blog index | `https://www.dopper.com/en/blog` | Each card opens one post. |
| Blog post | `https://www.dopper.com/en/blog/just-refill` | Related posts. |
| Insulated | `https://www.dopper.com/en/products/insulated` | Shop now into the shop collection. |
| Original | `https://www.dopper.com/en/products/original` | Shop now. |
| Steel | `https://www.dopper.com/en/products/steel` | Shop now. |
| Travel Mug | `https://www.dopper.com/en/products/travel-mug` | Shop now to `shop.dopper.com/travel-mug`. |
| Personalise | `https://www.dopper.com/en/products/personalise` and `/en/products/personalise-a-bottle` | Hands off to the shop personalise flow. Not filled. |
| Second life | `https://www.dopper.com/en/products/second-life` | In-page. |
| Bottle care | `https://dopper.com/en/products/bottle-care` | Care copy. |
| Tap | `https://www.dopper.com/en/products/tap` | Brochure link to `/en/products/tap-form`. Form not filled. |
| Tap map | `https://www.dopper.com/en/products/tap-map` | Map. Search not typed. |
| Custom bottles | `https://www.dopper.com/en/products/custom` | Business enquiry. Form not filled. |
| Custom mugs | `https://www.dopper.com/en/products/travel-mug-b2b` | Same. |
| Pledge | `https://www.dopper.com/en/get-involved/pledge` | Get started goes to `/en/get-involved/pledge/form`. Form not filled. |
| Schools | `https://www.dopper.com/en/get-involved/schools` | In-page. |
| Events | `https://www.dopper.com/en/get-involved/tap-water-at-events` | In-page. |
| Campaign | `https://www.dopper.com/en/campaigns/gifting-2026-1` | In-page. Watch target from the home hero. |
| Contact | `https://www.dopper.com/en/about/contact` | Contact form. Not filled. |
| Team | `https://www.dopper.com/en/about/team` | Staff grid. |
| Store locator | `https://www.dopper.com/en/about/store-locator` | Store search. Not typed. |
| Accessibility | `https://www.dopper.com/en/about/accessibility` | Statement. |
| Newsletter | `https://www.dopper.com/en/about/newsletter` | Form. Not filled. |
| Become a retailer | `https://www.dopper.com/en/about/become-a-dopper-retailer` | Form. Not filled. |
| Terms | `https://www.dopper.com/en/legal/terms-conditions` | Links to business, general, retail, water-tap and wave terms. |
| Privacy | `https://www.dopper.com/en/legal/privacy-policy` | Statement. |
| Cookies | `https://www.dopper.com/en/legal/cookie-policy` | Statement. Cookiebot "change your consent" was not clicked. |
| Returns | `https://www.dopper.com/en/legal/returns-warranty` | Policy. |
| Not found | `https://www.dopper.com/account/login` redirects to `/not-found-page` | No login form. |

English sitemap pages not opened one by one (same templates as the pages above): older impact reports (`/en/mission/reports-2022`, `2023`, `2024`), donations, the rest of the blog index (38 posts), pledge subpages (`form`, `form-individuals`, `form-organisations`, `form-thanks`, toolkits, wave-makers, schools, sports), get-involved extras (byob-challenge, festivals-and-events, join-the-wave, sports), other campaigns (back-to-routine-2026, gifting-2025, micro-dopper, summer-2026, world-refill-day), product extras (accessories, born-from-blue, flip-straw, summer-essentials, worthy), `/en/sign-up`, `/en/partners/travel-mug-wrist-cord`, and `/en/test-pages/*` (internal tests, not linked from the nav). `/en/error-page` is the error template.

## Shop (`https://shop.dopper.com/`)

Second nav, under the shared bar. No search field. No account link in the header.

| Control | Opens |
|---|---|
| All products | `https://shop.dopper.com/` |
| Mugs | `https://shop.dopper.com/travel-mug` |
| Bottles | `https://shop.dopper.com/bottles` |
| Accessories | `https://shop.dopper.com/accessories` |
| Spare parts | `https://shop.dopper.com/spare-parts` |
| E-Gift Card | `https://shop.dopper.com/gift-card` |
| Last chance | `https://shop.dopper.com/last-chance` |
| Cart icon | `https://shop.dopper.com/checkout/cart/` |

Submenus are in the DOM and stay closed on hover in this capture (`display: none`):

| Parent | Items |
|---|---|
| Mugs | Travel Mug `/travel-mug/mug`, Wrist Cord `/travel-mug/wristcord` |
| Bottles | Dopper Original `/bottles/original`, Dopper Insulated `/bottles/insulated`, Dopper Steel `/bottles/steel` |
| Spare parts | Bottle cap `/spare-parts/cap`, Bottle cup `/spare-parts/cup`, Bottle body `/spare-parts/bottle`, Mug cap `/spare-parts/mug-cap`, Mug ring `/spare-parts/mug-rings`, Mug body `/spare-parts/mug-body`, Accessories `/spare-parts/accessories` |

### Shop pages walked

| Page | URL | Controls |
|---|---|---|
| Shop home | `https://shop.dopper.com/` | Shop now, Personalise your bottle, product tiles into PDPs. |
| Bottles | `https://shop.dopper.com/bottles` | Filters opens a sheet: Collection (Original, Insulated, Steel, Flip Straw), Size (350 ml through 1.1 L), Colour swatches. Sort By: Position, Product Name, Price. Direction toggle. Product tiles open a PDP. |
| Flip Straw filter | `https://shop.dopper.com/bottles?bottle_collection=5587` | Same grid, collection pre-filtered. |
| Mugs | `https://shop.dopper.com/travel-mug` | Colour chips (beige, black, blue, green, pink) and size tiles (300 ml, 400 ml) into PDPs. Wrist cord category. |
| Accessories | `https://shop.dopper.com/accessories` | Product tiles. |
| Spare parts | `https://shop.dopper.com/spare-parts` | Category tiles into cap, cup, bottle, mug parts. Each part is its own PDP. |
| Gift card | `https://shop.dopper.com/gift-card` | Amount picker. Not added to the basket. |
| Last chance | `https://shop.dopper.com/last-chance` | Product tiles. |
| PDP example | `https://shop.dopper.com/dopper-original-pacific-blue` | Breadcrumb, price, Add to cart. Add to cart was not used, so the basket stayed empty. Gallery skip links. |
| Empty basket | `https://shop.dopper.com/checkout/cart/` | Continue shopping, Customer Service, Back to shop. No checkout button while empty. Branch stopped: a checkout URL was not followed. |

Product PDPs are one template. The crawl saw dozens (Original colours, Steel sizes, Insulated sizes, Travel Mug 300/400, collaborations, spare-part SKUs). They are not separate page types. Colour and size live on the collection filters and on each PDP, not on a picker dialog.

## Walls

| URL | What it is |
|---|---|
| `https://dopper.com/account/login` and `https://www.dopper.com/account/login` | 200, redirected to `/not-found-page`. No password field. Probe is no-form. |
| `https://shop.dopper.com/customer/account/login/` | 200, title Customer Login. Email and password fields, Sign in, Create an Account. Not linked from the public header or footer. Recorded and stopped. Nothing typed. |
| `https://shop.dopper.com/customer/account/` | Redirects to the login URL above. Stopped. |
| `https://shop.dopper.com/checkout/` | Disallowed in robots. Not opened. The empty basket has no checkout control. |
| `https://order.dopper.com` | Retail-partner login, linked as "Login as a retail partner" and "Sell Dopper products". Not opened. |

No public walk reached a checkout wall, because the basket was left empty and checkout was not started. The only login wall found is the Magento customer login URL above.
