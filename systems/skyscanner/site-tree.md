# Skyscanner public site tree

Mapped on 2026-11-22 from the public homepage, https://www.skyscanner.com/, signed out, in the T3 preview browser. The root redirected to https://www.skyscanner.com.sg/?previousCultureSource=COOKIE&redirectedFrom=www.skyscanner.com. The page title was "Compare Cheap Flights & Book Air Tickets to Everywhere | Skyscanner". The visible heading was "Millions of cheap flights. One simple search." Locale on the painted page: English (UK), Singapore, SGD.

The first load of https://www.skyscanner.com/ also redirected through a `session_handoff` query. That frame was discarded. The homepage shot is the later load, which has no session token.

A second navigation of the same homepage, and every later navigation of www.skyscanner.com.sg, www.skyscanner.net and help.skyscanner.net, returned the PerimeterX wall at `/sttc/px/captcha-v2/index.html` ("Are you a person or a robot?", Press & Hold). The captcha was not solved. curl of the same hosts returned the same 307. The walk below is what the first public homepage and one public about page actually painted, plus the links those pages exposed. Pages that only exist as a captcha redirect are listed as not opened.

No email, password, phone, code, or address was typed. No form was submitted. No identity provider was clicked. Search was not run. No flight, stay, or car was booked. `login-extracted` stays not-started.

## How a control opens something

| Control | Gesture | Opens |
|---|---|---|
| Header logo | link | https://www.skyscanner.com.sg/ |
| Flights, Stays, Cars | tab, also a link | /flights, /hotels, /carhire |
| Help | link | https://help.skyscanner.net/hc/en-gb |
| English (UK), Singapore, $ SGD | button | culture panel. Not opened |
| Saved (heart) | link | /profile/saved |
| Log in | button | a dialog, not a navigation. Not opened on this pass |
| Search | button | flight search. Not clicked |
| Search with AI, Explore everywhere | link or button | not opened |
| Footer columns | disclosure buttons | Explore, Company, Partners, Trips, International Sites. Read from the homepage DOM. Not clicked open |
| Cookie card | none on the homepage | The about page painted "We value your privacy". Not accepted |

## Header

Read on the homepage. Desktop, 1440 by 900 CSS pixels, device pixel ratio 2. Header background `#05203c`. The clean frame was not committed. catalog.json still declares `screenshots/` missing, and this pass left catalog.json alone.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Skyscanner | link | / | home |
| Help | link | https://help.skyscanner.net/hc/en-gb | not opened. Later navigations hit the captcha |
| English (UK), Singapore, $ SGD | button | culture panel | not opened |
| Saved flights, hotels and cars | link | /profile/saved | not opened. Account wall |
| Log in | button | dialog on the current page | not opened. The homepage paints the empty button. Stop |
| Flights | tab and link | /flights | not opened |
| Stays | tab and link | /hotels | not opened |
| Cars | tab and link | /carhire | not opened |

The search row sits under the tabs: trip type (Return), Bags, From, To, Depart, Return, travellers and cabin class, Search. From was prefilled "Singapore (Any)". To, dates, and travellers were empty. Nothing was typed. Search was not clicked. Add nearby airports, Direct flights, and Add a place to stay are checkboxes. Swap origin and destination was not clicked.

Under the hero, four cards: Search with AI (`/search-with-ai?rf=home-nc`, not opened), Stays (`/hotels`), Cars (`/carhire`), Explore everywhere (`#`, not opened). A promo links onward to a hotel stay ("Find your room"). Not opened. That path is a search, not a marketing page.

## Footer

Read from the homepage DOM. The first viewport of the homepage shot does not include the footer. Column labels are disclosure buttons: Explore, Company, Partners, Trips, International Sites. A culture button reads "Singapore · English (UK) · $ SGD". No email field was in the footer. No subscribe form was present.

Legal row, on every public page:

| Label | Destination | This pass |
|---|---|---|
| Get our app | https://skyscanner.app.link/4c8KEJ2HaIb | not followed |
| Help | https://help.skyscanner.net/hc/en-gb | not opened |
| Privacy Settings | /privacy-settings | not opened |
| Log in | /profile | not opened. Account wall |
| Cookie policy | /media/cookie-policy | not opened |
| Privacy policy | /media/privacy-policy | not opened |
| Terms of service | /terms-of-service | not opened |
| Company Details | /company-details | not opened |

Company column:

| Label | Destination | This pass |
|---|---|---|
| About us | /about-us | opened on www.skyscanner.net, then the host started returning the captcha |
| Why Skyscanner? | /about-us/why-skyscanner | not opened |
| Media | /media | not opened |
| Our people | /about-us/our-people | not opened |
| Accessibility | /about-us/accessibility | not opened |
| Sustainability | /about-us/sustainability | not opened |
| Jobs | https://www.skyscanner.net/jobs | not opened |
| Travel features & news | /news | not opened |
| Security | /security | not opened |
| How Skyscanner Works | /media/how-skyscanner-works | not opened |

Partners column, all on www.partners.skyscanner.net. Not opened.

| Label | Destination |
|---|---|
| Work with us | / |
| Advertise with us | /advertising/advertise-with-skyscanner |
| Travel Insight | /insights/travel-insight |
| Affiliates | /affiliates/affiliate-products |
| Travel APIs | /affiliates/travel-apis |

Explore also links the product indexes and a long list of destination, airport, airline, and car-hire pages (Singapore, Bangkok, Tokyo, Kuala Lumpur, Seoul, and the rest of the Singapore-market list). Trips repeats destination rows for flights, hotels, and car hire. Those are search and listing pages. They were not opened. Opening one and searching would start booking.

International Sites lists other Skyscanner markets: AU, CN (tianxun.com), HK, IN, ID, JP, MY, MX, NZ, RU, SG, TW, TH, GB (skyscanner.net), PH, KR, US (skyscanner.com), VN. Not switched.

The about page on www.skyscanner.net paints a second nav under the header: About us, Our people, Sustainability, Accessibility, Why Skyscanner?, Media. Its footer also links Privacy, Trust & Safety at /media/privacy-trust-and-safety-centre. That page was not opened.

## Pages opened

| URL | Title | Shot |
|---|---|---|
| https://www.skyscanner.com.sg/ | Compare Cheap Flights & Book Air Tickets to Everywhere \| Skyscanner | painted, not committed |
| https://www.skyscanner.net/about-us | We're the travel company who puts you first | painted, not committed |

The about shot includes the cookie card ("We value your privacy", Accept all, Manage settings, Accept essential only). Nothing on that card was clicked.

## Walls and stops

| Wall | What happened |
|---|---|
| Log in | The header button was visible and empty. It was not clicked. An earlier package note says this button opens a modal. This pass did not open it |
| /profile and /profile/saved | Linked from the footer and the heart. Not opened |
| Signup | No separate signup control was on the homepage. Log in is the account wall |
| Search and booking | Search was not clicked. No destination was typed. No date was picked. Checkout was not started |
| Subscribe | No email field was on the homepage footer |
| Captcha | `/sttc/px/captcha-v2/index.html`, "Are you a person or a robot?". Not solved. Those frames were discarded |
| Identity providers | None were clicked. None were visible on the pages that painted |

Phone width was not photographed. The homepage was measured at 1440 by 900. A 390 pass was not run before the captcha closed the host.
