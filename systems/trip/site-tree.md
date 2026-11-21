# Trip.com site tree

Mapped from the public homepage before screenshots, on 2026-11-21, in headed Chrome (Playwright `channel: 'chrome'`, headless). `https://www.trip.com/` returns 200 and geo-redirects to `https://sg.trip.com/?locale=en-sg`. Headless Chromium is sent to `https://verify.trip.com/static/tripVerify.html` (an icon-order captcha). That captcha was not solved.

Nothing was submitted. No password, code, or profile field was typed. Login and signup branches stop at the URL.

## Shell

The desktop shell is a top bar plus a left rail. The left rail is open on first paint (`aria-expanded="true"` on the Menu button).

| Control | Opens |
|---|---|
| Menu (hamburger, `aria-label="Menu"`) | Collapses or expands the left rail. Same page. |
| Trip.com logo | `https://sg.trip.com/?locale=en-SG&curr=SGD` (home) |
| Header search ("Destination, attraction, hotel, etc") | Focuses the field. Does not navigate. Search was not submitted. |
| App | Page: `/pages/appdownload` |
| List your property | Page: `/list-your-property` |
| SGD (Language/Currency) | Dialog: language and currency picker (`mc-lhd-modal`). Not submitted. |
| Customer support | Page: `/pages/support/` |
| Find bookings | Auth wall: `/passport/ordersearch/`. Stopped. |
| Sign in/register | Dialog on the homepage: "Sign in/register", membership rewards, "Continue with" social buttons. Google and Apple were not clicked. The known probe `https://www.trip.com/account/signin` is a sign-in page; Continue with Google was not used. |
| Suggested Languages (load-time dialog, `.online-language-match`) | A language suggestion over the header. Hidden for captures, never clicked. |
| TripGenie bubble | Chat launcher. Not opened into a conversation. |
| Service Chat | Support chat launcher. Not opened into a conversation. |

## Left rail

Each item is a link. Sale and campaign links under the fold are seasonal and were not treated as the design system.

| Control | Opens |
|---|---|
| Hotels | `/hotels/` |
| Flights | `/flights/` |
| Attractions & Tours | `/things-to-do/` |
| Flight + Hotel | `/packages/` |
| Trains | `/trains/` |
| Cars | `/carhire/` |
| Cruises | `/cruises` |
| Gift Cards | `/giftcard` |
| Travel Insurance | `/insurance` |
| Private Tours | `/package-tours/private-tours` |
| Group Tours | `/package-tours/group-tours` |
| Trip.Planner | `/webapp/tripmap/tripplanner` |
| Travel Inspiration | Home anchor / inspiration module on the homepage (same document as home in this sweep) |
| Map | `/webapp/tripmap/travel` |
| Deals | `/sale/deals/` |
| Trip.com Rewards | `/customer/loyalty/` |
| AI Lab | `/ailab` |

## Search card

The card (`.search-box-instance-con`, tabs `.mc-srh-box__tab-name`) sits on the homepage and repeats on product landings. Tabs navigate. Search was not submitted.

| Control | Opens |
|---|---|
| Hotels & Homes | Stays on home. Fields: Where to?, dates, rooms and guests, Search. |
| Flights | `/flights/`. Fields: Leaving from, Going to, dates. |
| Trains | `/trains/` |
| Cars | `/carhire/` |
| Attractions & Tours | `/things-to-do/` |
| Flight + Hotel | `/packages/` |
| Where to? | Destination field. Typed nothing. Not submitted. |
| Date range | Date control on the hotel card. Not submitted. |
| 1 room, 2 adults, 0 children | Guest stepper (`role=button`). Not submitted. |
| Search | Would run a search. Not clicked. |
| Sign in or register (under the card) | Same sign-in dialog as the header button. Stopped. |

## Homepage modules

| Control | Opens |
|---|---|
| Sign in & claim all | Sign-in dialog. Stopped. |
| Claim all | Sign-in dialog. Stopped. Coupon codes were not claimed. |
| Promo and sale tiles | Seasonal `/sale/w/...` campaign pages. Not part of the component set. |
| Footer: Service Guarantee | `/pages/customer-service/` |
| Footer: More service info | `/pages/service/` |
| Footer: About Trip.com | `/pages/about-us/` |
| Footer: News | `https://www.trip.com/newsroom/` |
| Footer: Careers | `https://careers.trip.com/` (separate host) |
| Footer: Terms & Conditions | `/contents/service-guideline/terms.html` |
| Footer: Privacy Policy | `/contents/service-guideline/privacy-policy.html` |
| Footer: Accessibility Statement | `/contents/eaa-accessibility-statement.html` |
| Footer: AI generated personalized content | `/pages/personalization-settings` (settings; not filled) |
| Footer: About Trip.com Group | `https://group.trip.com/` |
| Footer: Investor Relations | `https://investors.trip.com/` |
| Footer: Partners | `https://www.trip.com/partners/index` |
| Footer: All hotels | `/hotels/all-cities/` |
| Footer: Become a Supplier | `/m/vbooking/home` |
| Footer: Security | `https://src.trip.com/` |

## Auth walls (stopped)

| URL | What it is |
|---|---|
| `https://www.trip.com/account/signin` | Sign-in page. Continue with Google was not clicked. Known probe: that path returns to the public homepage when Google is continued; no account surface was reached, and this capture did not click Google. |
| `https://sg.trip.com/passport/ordersearch/` | Find bookings. Auth wall. |
| Sign in/register dialog, Claim all, Sign in & claim all | Account dialog on the public page. Not submitted. |

## Theme and width

No dark-theme toggle on the public shell. One painted theme (light). Captures are desktop 1440×900 and phone 390×844.
