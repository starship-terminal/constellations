# District site tree

Walked signed out on 2026-11-21 with Playwright, starting at `https://www.district.in/`. Desktop viewport 1440×900. Phone viewport 390×844. No form was submitted. No password, code, or phone number was typed. No app download was followed. No SSO button was clicked.

Login is an in-page dialog, not a URL. `https://www.district.in/login` returns a not-found page. The dialog asks for a mobile number and an OTP. That branch stopped there. Account, checkout, payment, order, and booking pages were not opened.

Shots live in [screenshots/](screenshots). Names are `{page}-light-{state}.png`. Phone shots use a `mobile-` prefix.

## Shell (every marketing page)

| Control | Opens |
|---|---|
| Logo, `aria-label` District Home | `/` |
| Location button (pin) | In-page dialog "Select Location": city search field, Use Current Location, Popular Cities, A–Z city list. Shot: [home-light-location.png](screenshots/home-light-location.png). City was not changed. |
| Search scope button "All" (on `/` it reads All; on `/events/` it reads Events) | Listbox "Select tab": All, Events. Shot: [home-light-search-scope.png](screenshots/home-light-search-scope.png). |
| Search control, `aria-label` Open search, `aria-controls` search-results-panel | Listbox of trending results and "View all results". Typing shows matches. Enter was not pressed and no result was opened. Shot: [home-light-search.png](screenshots/home-light-search.png). |
| Login | In-page dialog "Log in or sign up": country code, mobile field, SMS, WhatsApp, Continue (disabled until a number). Branch stopped. Shot: [home-light-login-wall.png](screenshots/home-light-login-wall.png). The phone field is painted over. |
| For you | `/` |
| Events | `/events/` |
| Phone header | Same controls, stacked. No separate menu button. Profile icon is the Login control. |

Footer, present on the home shell and most section pages:

| Control | Opens |
|---|---|
| Contact Us | `/contact` |
| Corporate Announcements | `/corporate-announcements` |
| List your events | `/events/list-your-event` |
| List your restaurant | `https://www.zomato.com/partner-with-us/new/` (left the site; not captured) |
| Zomato, Blinkit, Feeding India, Hyperpure | External. Not captured. |
| District MCP | `https://studio.district.in/mcp` (other host; not captured) |
| Eternal SBI Credit Card | External. Not captured. |
| Facebook, Instagram, X, YouTube | External. Not clicked. |
| Scan to Download / app badges | `https://link.district.in/DSTRKT/appicons`. Not followed. |
| Terms & Conditions | `/policies/terms-of-service` |
| Privacy Policy | `/policies/privacy` |

There is no theme toggle on the public site. Stylesheets declare `html[data-theme=dark]`. That theme was not painted.

## Pages

### `/` For you

Shot: [home-light-default.png](screenshots/home-light-default.png), [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

| Control | Opens |
|---|---|
| Artist cards (horizontal list, next-arrow button) | `/events/{slug}/artist` |
| Event poster cards | `/events/{slug}-buy-tickets` |

### `/events/`

Shot: [events-light-default.png](screenshots/events-light-default.png), [mobile-events-light-default.png](screenshots/mobile-events-light-default.png).

| Control | Opens |
|---|---|
| Filters | Dialog "Filter by": Sort By (Genre, Popularity, Price low/high, Date, Distance), Clear filters, Apply Filters. Apply was not pressed. Shot: [events-light-filters.png](screenshots/events-light-filters.png). |
| Today, Tomorrow, Under 10 km, Music, Music Festivals | In-page chips. URL stayed `/events/`. |
| Artist and event cards | Same patterns as home. |

### `/events/comedy`

Category listing named in `llms.txt`. Same filter chrome, with Comedy and Standups chips, plus Book tickets on each card. Book tickets was not pressed (it continues toward checkout). Shots: [events-comedy-light-default.png](screenshots/events-comedy-light-default.png), [mobile-events-comedy-light-default.png](screenshots/mobile-events-comedy-light-default.png).

### `/events/{slug}/artist`

Example: `/events/sonu-nigam/artist`. Biography plus show cards linking to buy-tickets URLs. Shots: [artist-light-default.png](screenshots/artist-light-default.png), [mobile-artist-light-default.png](screenshots/mobile-artist-light-default.png).

### `/events/{slug}-buy-tickets`

Example: `/events/unifyd-music-festival-buy-tickets`. Public event detail.

| Control | Opens |
|---|---|
| Venue button | In-page venue detail. Not a new URL in the probe. |
| Play video | Video. Not started. |
| View image, Next | Gallery. Shot: [event-light-gallery.png](screenshots/event-light-gallery.png). |
| View more | Expands about copy. |
| Book tickets, Continue Booking | Booking flow. Not pressed. Checkout is disallowed by robots.txt. |
| Close modal, Okay, Okay got it | Dismiss hidden modals already in the DOM. |

Shots: [event-light-default.png](screenshots/event-light-default.png), [mobile-event-light-default.png](screenshots/mobile-event-light-default.png).

### `/movies/`

Movie cards link to `/movies/{slug}-movie-tickets-{id}`. SEO blocks link to city cinema and city ticket pages (`/movies/cinemas-in-delhi-ncr`, `/movies/mumbai-movie-tickets`, and the same pattern for other cities). Those city indexes were not each photographed; they share the movies listing template. Shots: [movies-light-default.png](screenshots/movies-light-default.png), [mobile-movies-light-default.png](screenshots/mobile-movies-light-default.png).

### `/movies/{slug}-movie-tickets-{id}`

Example: Ramayana. Go back, Watch Trailer, Book Tickets (not pressed), FAQ buttons that expand in place (shot: [movie-light-faq.png](screenshots/movie-light-faq.png)), horizontal scroll buttons. Shots: [movie-light-default.png](screenshots/movie-light-default.png), [mobile-movie-light-default.png](screenshots/mobile-movie-light-default.png).

### `/dining/`

Restaurant cards link to `/dining/{city}/{slug}`. Filters button plus chips: Open now, Open early, Open late, Serves alcohol, Outdoor seating, Cafés, Fine dining. MENU and photo-gallery buttons sit on each card. Filters dialog was not re-opened here; the Events filters dialog is the captured filter pattern. Shots: [dining-light-default.png](screenshots/dining-light-default.png), [mobile-dining-light-default.png](screenshots/mobile-dining-light-default.png).

### `/dining/{city}/{slug}`

Example restaurant page. See all photos, overflow menu, Directions, Share, Call. Call is a `tel:` link and was not activated. Directions and Share were not opened. Shots: [restaurant-light-default.png](screenshots/restaurant-light-default.png), [mobile-restaurant-light-default.png](screenshots/mobile-restaurant-light-default.png).

### `/play/`

Public URL loads the shell and an empty main. No venue cards in this signed-out session. Shots: [play-light-default.png](screenshots/play-light-default.png), [mobile-play-light-default.png](screenshots/mobile-play-light-default.png).

### `/activities/`

Venue cards link to `/venue/{slug}` with Book tickets (not pressed). City links (`/activities/{city}-activity-tickets`) and category links (`/activities/water-parks-near-me`, monuments, game zones, theme parks, kids play) share this listing template and were not each photographed. Shots: [activities-light-default.png](screenshots/activities-light-default.png), [mobile-activities-light-default.png](screenshots/mobile-activities-light-default.png).

### `/venue/{slug}`

Example: `/venue/metcalfe-hall`. Public venue page. Shots: [venue-light-default.png](screenshots/venue-light-default.png), [mobile-venue-light-default.png](screenshots/mobile-venue-light-default.png).

### `/stores/`

Marketing hero and an in-page search field ("What are you looking for today?"). The field was not submitted. No store cards in this session. Shots: [stores-light-default.png](screenshots/stores-light-default.png), [mobile-stores-light-default.png](screenshots/mobile-stores-light-default.png).

### `/contact`

Help page. Category radios (Dining, Movies, Events, Other), name, email, mobile, and message fields. Send message was not pressed. Nothing was typed. Phone, email, and street address in "Other ways to reach us" are painted over in the desktop shot. Shots: [contact-light-default.png](screenshots/contact-light-default.png), [mobile-contact-light-default.png](screenshots/mobile-contact-light-default.png).

### `/corporate-announcements`

List of announcement rows. Each "Read more" opens a PDF on `b.zmtcdn.com`. PDFs were not downloaded. Shots: [corporate-light-default.png](screenshots/corporate-light-default.png), [mobile-corporate-light-default.png](screenshots/mobile-corporate-light-default.png).

### `/events/list-your-event`

Partner landing. Login button (same dialog; not re-opened). App download link not followed. Shots: [list-event-light-default.png](screenshots/list-event-light-default.png), [mobile-list-event-light-default.png](screenshots/mobile-list-event-light-default.png).

### `/policies/`

Docusaurus policies home.

| Control | Opens |
|---|---|
| Toggle navigation bar | Sidebar. |
| Movies, Dining, Events, Gift Cards, Pass, District Play, Stores | Expand a nav group. Shot: [policies-light-nav-open.png](screenshots/policies-light-nav-open.png). |
| Terms of Service | `/policies/terms-of-service` |
| Privacy Policy | `/policies/privacy` |
| In-page service links | `/policies/dining/district-pay`, `/policies/movies/booking-terms`, `/policies/events/booking-terms`, `/policies/stores/payment-terms`, `/policies/play/booking-terms` |

Shots: [policies-light-default.png](screenshots/policies-light-default.png), [mobile-policies-light-default.png](screenshots/mobile-policies-light-default.png).

### `/policies/terms-of-service` and `/policies/privacy`

Long policy pages. Sidebar groups expand. In-page anchors jump within the page. Scroll-to-top button. Shots: [terms-light-default.png](screenshots/terms-light-default.png), [privacy-light-default.png](screenshots/privacy-light-default.png), and the matching `mobile-` shots.

### `/login`

Not found. Status 404. Body: the site's missing-page message. Shot: [login-url-light-missing.png](screenshots/login-url-light-missing.png). Phone width was the same 404 and was not kept as a second missing-page shot.

## Not opened

| URL | Why |
|---|---|
| `/profile`, `/users`, `/checkout`, `/payments`, `/bookings`, `/order` | robots.txt disallows them. Login wall stops the account branch. |
| Book tickets, Continue Booking, Call, Directions, Share | Booking, phone, or external handoff. |
| App store badges | Download. |
| External footer links | Other sites. |
| Sitemap city/event/movie URLs | Same templates as the pages above. `sitemap.xml` indexes events, movies, play, and activities sitemaps. |

## Interactions not on this site

No theme toggle. No account menu while signed out. No toast was triggered, because no action was submitted. No separate phone drawer: the header stacks instead.
