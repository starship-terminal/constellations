# Understory public site tree

Mapped from the live homepage on 2026-11-21 with headless Playwright, before screenshots. Official marketing host is `https://understory.io/` (Webflow, title "Understory - Powering Experience Makers"). Confirmed against `https://understory.io/sitemap.xml` (483 locs; 78 English). Language copies under `/da`, `/sv`, `/no`, `/it`, `/es` are the same tree and were not walked page by page.

Nothing was submitted. No email, password, code, or survey field was typed. Login and signup URLs were recorded and that branch stopped.

## Header (desktop, marketing pages)

The bar is a Webflow navbar. Three items are hover dropdowns (`.w-dropdown`). They also link to an overview page. Pricing is a direct link. The right cluster is Login, Book a demo, and Try for free.

| Control | Opens |
|---|---|
| Logo | `https://understory.io/?r=0` (home) |
| Booking system (hover) | Dropdown menu, listed below. The label itself links to `/all-in-one-solution` |
| Marketing (hover) | Dropdown menu. The label itself links to `/overview` |
| Made for (hover) | Dropdown menu. No overview link on the toggle |
| Pricing | `/pricing` |
| Login | `https://backoffice.understory.io/login?language=en` (auth wall; stop) |
| Book a demo | `/book-a-demo` (HubSpot meeting embed; do not submit) |
| Try for free | `https://preview.understory.io/` (preview generator; do not type a URL or submit) |

A fourth dropdown, Resources, is in the DOM with class `resources-nav hide`. It is not in the visible desktop bar. Its links also appear in the mobile menu.

### Booking system menu

| Item | Opens |
|---|---|
| View all | `/all-in-one-solution` |
| Ticketing | `/ticketing` |
| Booking management | `/booking-management` |
| Take bookings | `/take-bookings` |
| Event scheduling | `/event-scheduling-operations` |
| Gift cards | `/gift-cards` |
| Guest Communication | `/guest-communication` |
| Reporting & Analytics | `/reporting-business-insights` |
| Integrations | `/integrations` |
| Payments | `/payments` |
| Resource management | `/resource-management` |

### Marketing menu

| Item | Opens |
|---|---|
| View all | `/overview` |
| Google Ads | `/google-ads` |
| Meta Ads | `/meta-ads` |
| Websites | `/websites` |
| Reviews | `/reviews` |
| Marketplaces | `/marketplaces` |

### Made for menu

| Item | Opens |
|---|---|
| Cooking & Drinking | `/cooking-drinking` |
| Camps | `/camps` |
| Creative Workshops | `/creative-workshops` |
| Festivals | `/festivals` |
| Tastings | `/tastings` |
| Tours | `/tours` |
| Active Experiences | `/active-experiences` |
| Boat Tours | `/boat-tours` |

### Resources (hidden desktop dropdown; visible in the phone menu)

| Item | Opens |
|---|---|
| About Us | `/about-new` |
| Support | `/support` |
| Watch Demo | `/watch-understory-in-action` |
| Get a better booking solution in 30 seconds | `https://preview.understory.io/` (preview wall; stop before typing) |
| Knowledge | `/blog` |

## Phone (390)

The same navbar collapses. A menu button opens `.w-nav-overlay` / `.w-nav-menu` with Booking system, Marketing, Made for, Resources, Pricing, Login, Book a demo, and Try for free. Nested dropdowns expand inside that drawer. Login and Try for free are the same walls as desktop.

## Homepage interactions

| Control | What it does |
|---|---|
| Promo "Learn more" | `/meta-ads` |
| Tabs "Less admin", "More bookings", "Better booking experience" | In-page Webflow tabs (`#w-tabs-0-data-w-pane-0` through `-2`). Each pane has a "See how it works" link (`/booking-management`, `/meta-ads`, `/take-bookings`) |
| Experience tiles (Food & Drink Classes, Creative Workshops, Tastings, Active Experiences, Boat Tours, Festivals, Tours, Camps) | The matching Made for page |
| FAQ questions (What exactly does Understory do?, How much does it cost?, and six more) | Accordion / dropdown on the same page. Opens a panel; does not navigate |
| Website field "Enter your website" + submit | Form on `/`. Not submitted |
| Footer email "Enter your email" + submit | Newsletter. Not submitted. Present on most marketing pages |
| Footer language "Change language" | Dropdown: English `/?r=0`, Danish `/da`, Swedish `/sv`, Norwegian `/no`, Italian `/it`, Spanish `/es` |

## Pricing

| Control | What it does |
|---|---|
| Tabs Sell more, Save time, Get paid faster, Get insights | In-page tabs. Each pane lists feature links into the product pages above |
| Try for free / Book a demo / Login | Same three destinations as the header |
| Newsletter email | Not submitted |

## Blog

| Control | What it does |
|---|---|
| Filter radios (All, Industry Insights, News, Host Story) | Filter the post list on `/blog`. Not a form submit to a server from the capture's point of view; selecting a radio is a client filter and was used as a state |
| A post card | `/blog-posts/<slug>` |
| Newsletter email | Not submitted |

## Support, product, and legal pages

These share the marketing header, footer language dropdown, FAQ accordions where present, and the newsletter field (not submitted).

| Page | Notes |
|---|---|
| `/support` | FAQ accordions. Help articles live on `help.understory.io` |
| `/about-new` | About |
| `/watch-understory-in-action` | Public demo video page |
| `/integrations` | Tool logos and FAQ |
| `/websites` and the other product pages in the menus | Marketing layouts, FAQ accordions |
| `/wall-of-love` | Older header: Product, Watch demo, Pricing, Community, Login, Book a demo, Get started. Newsletter placeholder "Get tips for your experiences". Not submitted |
| `/get-started-with-understory` | Older header. Radio group "Experience business type" is an onboarding/survey form. Recorded, not filled, not submitted |
| `/try-understory-for-free` | Checkbox experience picker and the same pricing tabs. Recorded, not filled, not submitted |
| `/book-a-demo`, `/book-a-demo-meta-ads`, `/book-advertising-demo` | Demo request. HubSpot embed. Not filled, not submitted |
| `/privacy-policy`, `/terms`, `/consent-terms`, `/accounting-terms`, `/websites-terms`, `/understory-pay-terms`, `/reviews-terms`, `/search-ads-terms`, `/sub-processors` | Legal prose |
| `/holdbar-becomes-understory`, `/spring-launch`, `/female-founders-lab` | Campaign pages in the sitemap |
| `/webinar/<slug>` | Dated webinar landing pages in the sitemap |
| `/experience-maker-stories/<slug>` | Story pages |
| `/dev/image-animation`, `/book-a-demo-confirm-test` | Internal or test URLs in the sitemap. Not treated as product UI |

## Other public hosts linked from the marketing site

| Control | Opens | Stop? |
|---|---|---|
| Login / Sign up now | `https://backoffice.understory.io/login` | Yes. Probe: email and password fields, "WELCOME BACK", Sign up now, Forgot password, language "AMERICAN ENGLISH". No Google button. No Apple button. Email not typed. Password not submitted |
| Sign up now (on the login page) | Same host, signup wall | Yes. Not followed into account creation |
| Try for free, Get started, preview card | `https://preview.understory.io/` | Yes as an account or generator branch. The page loaded publicly ("YOUR COMPLETE BOOKING SOLUTION - READY IN SECONDS", URL field, "Show my solution", a demo calendar with Book now / month controls, and a sidebar: Home, Calendar, Experiences, Sales, Booking page, Grow). The URL field was not typed. "Show my solution" and Book now were not clicked, because both continue a booking or profile flow |
| Support articles | `https://help.understory.io/en` | No. Public help center. Search field present; not submitted. Collections: Home, Calendar, Experiences, Location and Resource Management |
| Developer docs | `https://developer.understory.io/` | No. Public docs. Search trigger, light/dark theme button, menu, Get started, API reference, Building with AI, Chat with us |
| Careers | `https://people.understory.io/` | Public careers site with its own cookie dialog (Accept all, Decline all non-necessary, Cookie preferences). Dialog was hidden, not clicked. Career menu, film, cookie-manage modal. Not an Understory product UI; recorded as a linked host, not captured as the product |
| Guest booking widget (example from a marketing embed) | `https://unless-library-neighborhood.understory.io/en/booking/<id>` | Public guest booking flow ("Who & When?"). Not walked further: later steps collect guest details. Recorded as a boundary |

## States captured from this tree

Desktop 1440x900 and phone 390x844, light only (no public theme switch on the marketing site):

- Home default, full page, booking-system menu, marketing menu, FAQ open, homepage tab
- Phone home default, full page, nav drawer
- Pricing default and full page, phone pricing
- Blog default and a filter selected
- One product page (`/ticketing`) and one story vertical (`/tours`)
- Support FAQ open
- Login wall URL recorded, not filled: `https://backoffice.understory.io/login`
- Developer docs theme toggle (public, not an account setting)
- Help center home

Not captured, with the reason in the package README coverage table: signup, preview URL submit, demo forms, newsletter, onboarding radios, guest booking details, signed-in backoffice, dark theme on the marketing site (none found).
