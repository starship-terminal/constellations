# Onefinestay site tree

Mapped from the public homepage at `https://www.onefinestay.com/` on 2026-11-21, before screenshots. Headless Chromium, signed out. The cookie banner was not accepted. Controls that open a login or signup wall were recorded and that branch stopped. No form was submitted. No email, phone, or location was typed.

The homepage is a Next.js storefront (Tailwind utility classes, `font-akkurat` and `tiempos`). OneTrust mounts `#onetrust-consent-sdk` on every page. Same-context navigation after the homepage often returns a 403 "Performing security verification" interstitial. A fresh browser context per route loads the public pages (HTTP 200).

## Global chrome (desktop 1440)

| Control | Opens |
|---|---|
| Skip to main content | `#main` on the current page |
| Destinations (`a[aria-label="Destinations"]`, no href) | Mega menu. Country rows link to `/search/<slug>/<id>`. See Destinations menu. |
| List Your Home | Page `/list-your-home` |
| Inspiration (`a[aria-label="Inspiration"]`, no href) | Mega menu. See Inspiration menu. |
| Logo (`a[aria-label="onefinestay homepage"]`) | `/` |
| Heart (`a[aria-label="View your favorites"]`) | `/wishlist` (public empty state; Login button is a wall) |
| Account (`button[aria-label="Login or Sign up menu"]`) | Dropdown. Create Login goes to `/signup`. Log in and the password field are the login wall. Forgot password goes to `/forgot-password`. "Are you a travel advisor?" is a further control inside the wall. Stop. |
| Inquire Now | Page `/enquire` (enquiry form; not submitted) |
| Current currency: USD (footer) | Currency list: USD, GBP, EUR, CAD, AUD. Display preference, not a form submit. |
| Cookies Settings | OneTrust preference center (checkboxes, Allow All, Confirm My Choices). Not opened for capture: accepting or confirming would record consent. Banner left visible, not accepted. |
| Accept All Cookies | Consent accept. Not clicked. |
| Continue without Accepting | Consent continue. Not clicked. |

Phone (390): header shows Open menu, logo, and a contact icon to `/enquire`. Open menu reveals Destinations, List Your Home, Inspiration, My favorites (`/wishlist`), Log in (wall), Find a stay (search). Close menu dismisses it.

## Homepage interactions

| Control | Opens |
|---|---|
| Dates | Dialog: Calendar / Flexible tabs, month grid, Previous month, Next month, flexibility chips (Exact dates, ±1 day, ±2 days, ±3 days, ±7 days). Selecting a day is a local picker state, not a submit. |
| Guests | Guest-count buttons 1–12 and Search. Search would navigate to results. Not submitted as a booking. |
| Search (in the menus) | Search field "Where to next?". Not filled. |
| Previous slide / Next slide | Carousel step on the home carousels (featured homes, Just In, London's finest). |
| Home card | `/home-listing/<slug>` (one listing captured as the template) |
| Discover | `/destination/<path>` |
| Show homes | `/search/<slug>/<id>` |
| Explore Here | `/black-friday-weekend` |
| Discover more | Expands a home-page section (button, no navigation) |
| Footer phone link | `tel:` link. Not activated. The number is not written into this package. |
| Footer socials | External: Trustpilot, X, Pinterest, Instagram, Facebook. Not followed. |
| Google privacy / terms (map widget) | `policies.google.com`. Not followed. |
| Cookiepedia / OneTrust product links | External consent docs. Not followed. |

## Destinations menu

Each row is a search results page.

| Label | Path |
|---|---|
| United Kingdom | `/search/united-kingdom/496` |
| London | `/search/london/500` |
| Italy | `/search/italy/985` |
| Amalfi Coast | `/search/amalfi-coast/1001` |
| Florence | `/search/florence/1081` |
| Lake Como | `/search/lake-como/1038` |
| Rome | `/search/rome/1019` |
| Tuscany | `/search/tuscany/1075` |
| France | `/search/france/566` |
| Cannes | `/search/cannes/673` |
| Provence | `/search/provence/873` |
| Saint-Tropez | `/search/saint-tropez/905` |
| South of France | `/search/south-of-france/644` |
| USA | `/search/usa/1444` |
| Aspen | `/search/aspen/1468` |
| Breckenridge | `/search/breckenridge/1470` |
| Colorado | `/search/colorado/1466` |
| Hawaii | `/search/hawaii/1290` |
| Los Angeles | `/search/los-angeles/1566` |
| Park City | `/search/park-city/1516` |
| Steamboat | `/search/steamboat/2230` |
| Telluride | `/search/telluride/1477` |
| Vail & Beaver Creek | `/search/vail-and-beaver-creek/1478` |
| Caribbean | `/search/caribbean/130` |
| Anguilla | `/search/anguilla/132` |
| Barbados | `/search/barbados/176` |
| Cayman Islands | `/search/cayman-islands/212` |
| Dominican Republic | `/search/dominican-republic/217` |
| Jamaica | `/search/jamaica/240` |
| St Barts | `/search/st-barts/302` |
| St John | `/search/st-john/297` |
| St Martin | `/search/st-martin/357` |
| Turks and Caicos | `/search/turks-and-caicos/416` |
| US Virgin Islands | `/search/us-virgin-islands/1805` |
| Mexico | `/search/mexico/1349` |
| Cabo San Lucas | `/search/cabo-san-lucas/1353` |
| Puerto Vallarta | `/search/puerto-vallarta/1392` |
| Punta Mita | `/search/punta-mita/1395` |
| Riviera Maya | `/search/riviera-maya/1425` |
| Central America | `/search/central-america/441` |
| Costa Rica | `/search/costa-rica/446` |

Search results share one template. London (`/search/london/500`) is the captured instance. Its controls: location chip (Clear location), Filters (Garden, Air-conditioning, Washer, Children welcome, King size bed, Guests, Bedrooms, Bathrooms, More filters, Close), Sort by: Recommended, pagination (1, 2, 3, Next page), Add to favorites, View Map (Google map chrome: keyboard shortcuts, fullscreen, camera, zoom). Map "Map Data" is a Google link. Not followed.

## Inspiration menu

| Group | Label | Path |
|---|---|---|
| Collections | European Escapes | `/lp/europe-edit` |
| Collections | Beach Villas | `/villa-collection` |
| Collections | Design-led | `/lp/design-led-vacation-rentals` |
| Collections | Seasonal Promotions | `/lp/seasonal-promotions` |
| Collections | Ski & Snow | `/chalet-collection` |
| Collections | City Breaks | `/home-collection` |
| Collections | Wellness Retreats | `/lp/wellness-vacation-rentals` |
| Collections | Extended Stays | `/monthly-rentals` (also `/lp/monthly-rentals` from the homepage body) |
| Trending now | London | `/destination/london` |
| Trending now | Rocky Mountains | `/destination/the-rockies` |
| Trending now | Paris | `/destination/paris` |
| Trending now | Los Angeles | `/destination/los-angeles` |
| Trending now | Rome | `/destination/italy/rome` |
| Trending now | Turks & Caicos | `/destination/caribbean/turks-and-caicos` |
| Trending now | South of France | `/destination/france/luxury-villas-south-of-france` |
| Trending now | Cabo San Lucas | `/destination/mexico/cabo-san-lucas` |
| Journal | Journal | `/journal` |
| Journal | Stories | `/journal/stories` |
| Journal | Guides | `/journal/guides` |
| Journal | Trending | `/journal/trending` |

`/journal` is a different app shell (search field, currency, a newsletter email field, a login/signup overlay baked into the document). The newsletter field was not filled. Journal search was not submitted.

## Listing page

`/home-listing/cadogan-street-iv-cad126` is the captured listing template. Other `/home-listing/*` cards on the homepage are the same template.

| Control | Opens |
|---|---|
| View all photos | Photo gallery |
| Previous slide / Next slide | Gallery step |
| Add to wishlist | Local favorite, or the login wall if the site requires an account. Not treated as a submit. |
| Ask a question | Enquiry fragment. Email field present. Not filled. Not submitted. |
| Check Availability | Date picker (Select date, month grid). Not submitted. |
| Dedicated concierge, Meet & Greet, housekeeping, 24/7 support | In-page service notes |
| Scroll left / Scroll right | Room strip |
| Newsletter email on the listing | Not filled. Not submitted. |

## Footer and editorial pages

| Control | Path |
|---|---|
| Vacation Home Listings | `/home-listing` |
| Collection category pages | `/c/ski-lodge-cabin-rentals`, `/c/pet-friendly-vacation-homes`, `/c/luxury-vacation-apartment-rentals`, `/c/luxury-chalet-rentals`, `/c/beachfront-vacation-rentals`, `/c/luxury-vacation-rentals-london-uk`, `/c/vacation-rentals-with-swimming-pool`, `/c/family-vacation-rentals`, `/c/luxury-vacation-villa-rentals`, `/c/vacation-rentals-with-hot-tubs`, `/c/ski-in-ski-out-rentals` |
| Home Collection | `/home-collection` |
| Chalet collection | `/chalet-collection` |
| Villa Collection | `/villa-collection` |
| Destination guides (footer) | `/destination/london`, `/destination/los-angeles`, `/destination/italy/rome`, `/destination/italy/tuscany/florence`, `/destination/the-rockies/aspen`, `/destination/the-rockies/park-city`, `/destination/the-rockies/breckenridge`, `/destination/the-rockies/steamboat`, `/destination/the-rockies/vail-beavercreek`, `/destination/france/french-riviera/saint-tropez`, `/destination/france/french-riviera/cannes`, `/destination/caribbean`, `/destination/caribbean/turks-and-caicos`, `/destination/caribbean/st-john`, `/destination/caribbean/st-barts`, `/destination/caribbean/st-martin`, `/destination/caribbean/jamaica`, `/destination/caribbean/barbados`, `/destination/caribbean/dominican-republic`, `/destination/italy/tuscany`, `/destination/italy/amalfi-coast`, `/destination/italy/lake-como`, `/destination/mexico`, `/destination/mexico/punta-mita`, `/destination/mexico/cabo-san-lucas`, `/destination/mexico/riviera-maya`, `/destination/france/luxury-villas-south-of-france`, `/destination/the-rockies` |
| Additional services | `/onefinestay-services` |
| Reviews | `/reviews` |
| All Accor Live Limitless | `/lp/all-accor-live-limitless-onefinestay-benefits` |
| Jobs | `/jobs` |
| Press room | `/press-room` |
| Travel agency partners | `/travel-advisors` |
| Affiliate programme | `/lp/affiliate-programme` |
| List your home | `/list-your-home` (Submit your home, FAQ accordions, video controls, testimonials) |
| Journal | `/journal` |
| About onefinestay | `/about` |
| Team | `/team` |
| Housekeeping and guest safety | `/lp/housekeeping-guest-safety-commitment` |
| Cancellation policies | `/cancellation-policies` |
| Terms of use | `/terms-of-use` |
| Terms and conditions | `/terms-conditions` |
| Privacy policy | `/privacy-policy` |
| Website accessibility | `/website-accessibility` |
| Contact us | `/contact-us` |
| London monthly rentals | `/lp/london-monthly-rentals` |
| Journal articles (homepage) | `/journal/trending/new-homes`, `/journal/guides/architectural-stays`, `/journal/stories/inside-rancho-cuatras-patas`, `/journal/stories/meet-matthew-williamson`, `/journal/trending/10-design-led-homes`, `/journal/guides/guide-book-belgravia`, `/journal/trending/spotlight-on-hereford-square`, `/journal/trending/when-to-book` |
| Brochure | External `cloud.3dissue.net` flipbook. Not followed. |
| Press citation | External `cntraveller.com`. Not followed. |

Destination pages share one guide template (search chip, carousels, neighbourhood chips, FAQ accordions, a newsletter email field). London is the captured instance. Collection, category, legal, and landing pages share the marketing shell. One of each family is captured. The rest are the same template.

## Walls (recorded, branch stopped)

| URL | What it asks for |
|---|---|
| `https://www.onefinestay.com/login` | Email address and password. Show password, Log in, Forgot password, travel-advisor prompt. |
| `https://www.onefinestay.com/signup` | Name, email, password, country, phone. Not filled. |
| `https://www.onefinestay.com/forgot-password` | Account recovery. Not filled. |
| Account menu on any page | Same login wall, inline. |
| Wishlist Login button | Same wall. |
| Enquire, listing "Ask a question", newsletter fields | Email, phone, name, postal code. Not filled. Not submitted. |

No Google, Facebook, or Apple button was present on the login page that loaded. None was clicked.

## Not a page

Carousel steps, FAQ accordions, filter chips, sort, currency, the date picker, and the guest stepper are interactions on the pages above. They do not add a new URL.
