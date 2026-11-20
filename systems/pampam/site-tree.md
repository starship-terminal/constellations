# PamPam public site tree

Mapped on 2026-11-21 from https://www.pampam.city/ in headless Chromium before screenshots. Same-origin links were crawled from the homepage, the header menus, the footer, and the sitemap at `/sitemap.xml` (315 locs). A control that opens a Google sign-in wall stops that branch. No form was submitted. No Google or Apple control was clicked.

The product is PamPam, an AI map maker. The public surface is a marketing site, a template gallery, a few published community maps, and a print-guide wizard. Making or copying a map requires Google sign-in. There is no public dark-theme control.

## Shell

Desktop header (1440), on every marketing page:

| Control | Opens |
|---|---|
| PAM wordmark (`a[href="/"]`) | Home `/` |
| Pricing | Page `/pricing` |
| Solutions (button, `aria-expanded`) | Menu, stays on the page. Links: Travelers `/travel-map`, Tourism `/tourism-maps`, Startup Maps `/startup-maps`, Real Estate `/real-estate-maps`, Nonprofits `/maps-for-nonprofits` |
| Products (button, `aria-expanded`) | Menu, stays on the page. Links: Custom Maps `/custom-maps`, Travel Maps `/travel-map`, Map Animations `/map-animation`, AI Maps `/ai-map-maker`, Printable Maps `/printable-maps`, Event Maps `/event-maps` |
| Inspiration | Page `/explore-q3lldmKbBaAR63C6nT4c` (title Explore). The sitemap also lists `/inspiration-q3lldmKbBaAR63C6nT4c` |
| Sign in with Google (header) | Page `/login`. Google Identity iframe only. Stop |

Phone (390): the header collapses to the PAM wordmark and a Sign in with Google button. That button is the same `/login` wall. No burger drawer was found. Pricing, Solutions, Products and Inspiration are not in the phone header; the footer still lists them after scroll.

## Home `/`

| Control | Opens |
|---|---|
| Hero prompt ("Make map", rotating placeholders) | Dialog: "Welcome to PamPam / Login to create and share maps" with Login with Google and a close control. URL stays `/`. Stop. Do not click Google |
| Interactive Map, Map animation, Printable map | Segmented control under the hero. Changes the demo on the page. Not a navigation |
| Press logos | External articles (Fast Company, Business Insider, Forbes, Dense Discovery). Off-site |
| Explore PamPam's map maker | Page `/map-maker` |
| Startup Maps, Travel Maps, Directory Maps, Event Maps cards | `/startup-maps`, `/travel-map`, `/business-directory-maps`, `/event-maps` |
| Template cards | `/templates/startup-ecosystem-map`, `/templates/event-map`, `/templates/business-directory`, `/templates/people-directory`, `/templates/resource-map`, `/templates/city-guide` |
| Audience cards | `/travel-map`, `/tourism-maps`, `/maps-for-nonprofits`, `/real-estate-maps` |
| FAQ rows ("How do I make my own custom map?" and four more) | Accordion on the page. No navigation |
| Try it for free | `/login`. Stop |
| Explore our map maker | `/map-maker` |
| Make travel maps | `/travel-map` |

## Footer (marketing pages)

Tools: `/map-maker`, `/ai-map-maker`, `/travel-map`, `/templates`, `/custom-map-templates`, `/map-animation`, `/printable-maps`, `/notion-maps`, `/vicinity-map-maker`, `/event-maps`, `/travel-recap`.

Use cases: `/community-maps`, `/tourism-maps`, `/real-estate-maps`, `/maps-for-media`, `/maps-for-nonprofits`, `/startup-maps`, `/wedding-maps`, `/store-locator`.

Company: `/about`, `/pricing`, `/releases`, `/features`, `/blog`, `/on-a-walk`, `/gift-shop`. Help & Docs, Terms & Privacy, Feature requests, Ambassador, Affiliate, Instagram and YouTube are off-site (Intercom, Notion, Canny, Instagram, YouTube).

## Marketing pages (same shell, FAQ accordions where present)

| Path | What it is |
|---|---|
| `/pricing` | Free, Explorer, Business, Advanced. "Try it for free" goes to `/login`. Stop. No other plan button was a form |
| `/map-maker` | Product page |
| `/custom-maps` | Product page. `/embed-map` redirects here |
| `/ai-map-maker` | Product page |
| `/ai-trip-planner` | Product page |
| `/spreadsheet-map` | Product page (sitemap; not in the footer) |
| `/map-animation` | Product page. Has empty inputs; not filled |
| `/printable-maps` | Product page |
| `/travel-map` | Product page |
| `/travel-recap` | Travel recap maker. Place fields and "Make travel recap video". Not filled, not submitted |
| `/vicinity-map-maker` | Product page |
| `/notion-maps` | Product page |
| `/event-maps` | Product page |
| `/store-locator` | Product page |
| `/tourism-maps` | Product page |
| `/wedding-maps` | Product page |
| `/real-estate-maps` | Product page |
| `/maps-for-media` | Product page |
| `/maps-for-nonprofits` | Product page |
| `/maps-for-designers` | Product page (sitemap only) |
| `/startup-maps` | Product page |
| `/community-maps` | Product page |
| `/business-directory-maps` | Product page (homepage card; not in the sitemap sample of unique tools) |
| `/guidebook` | Product page (sitemap) |
| `/about` | Team page. Published names stay; no contact fields filled |
| `/features` | Feature list |
| `/releases` | What's new |
| `/blog` | Index of 12 posts linked on the page |
| `/blog/<slug>` | Article. Same shell. Example: `/blog/how-to-make-a-travel-recap` |
| `/on-a-walk` | Series page |
| `/gift-shop` | Hat and tote. "Shop hat" / "Shop tote" did not expose a checkout form in the first paint |
| `/event-map-america250` | Campaign page |
| `/world-cup-2026-maps` | Campaign page |

## Templates and galleries

| Path | What it is |
|---|---|
| `/templates` | Template index, grouped (Featured, Events, and more) |
| `/templates/<slug>` | One template landing (29 in the sitemap, plus more linked from pages). FAQ accordion. Copy/start controls that need an account go to `/login`. Stop |
| `/custom-map-templates` | Continent, country and city index |
| `/custom-map-templates/<place>` | One place page (242 in the sitemap). Same marketing shell |
| `/<name>-<id>` city templates | Example `/london-map-template-xxdJtKcbzJ0VggodT0nH`. "Copy Map" is an account action. A place row opens `/<map>/<placeId>` |
| `/explore-q3lldmKbBaAR63C6nT4c` | Explore gallery. Search field "Search map" (typed into, not submitted). Sections: Featured, Collaborative, Collections, Food Guides, City guides, More maps. A card opens a published map |

## Published maps (public, no account)

| Path | What it is |
|---|---|
| `/p/<id>` | Redirects to a slug form, for example `/p/LbRKFLtehcIbADWIDXjM` to `/startup-hubs-map-LbRKFLtehcIbADWIDXjM` |
| `/<slug>-<id>` | Published map. Search field, Filter control, place list, zoom +/−, "Make your map" (account). A place row opens that map's place URL |
| `/<map>/<placeId>` | Place detail on a template or published map |

Filter on the published map and Explore did not open a separate page in the first click probe. Search was not submitted.

## Print wizard (public, not submitted)

`/printshop/destination-visitor-guide/create` and `/printshop/travel-guide/create`. Steps on the first screen: Pick a neighborhood, Add amenities, Add businesses, Make it yours, Pick your paper, Download. The neighborhood field was not filled. "Next" was not clicked, so later steps are not captured as reached states.

## Auth wall (stop)

| URL | What it shows |
|---|---|
| `/login` | "Welcome to PamPam". One control: Sign in with Google (Google Identity iframe). Terms and Privacy are Notion pages. No email field, no Apple button, no password field |
| Header "Sign in with Google" | Same `/login` |
| Hero prompt, "Try it for free", and copy-map actions | Same wall, sometimes as a dialog on the current URL |

Signed-in map editor, account settings, billing, onboarding and newsletter signup are not reachable without that wall.

## Off-site (not captured)

Intercom help, Notion terms and privacy, Canny feature requests, Notion ambassador and affiliate pages, Instagram, YouTube, press articles, Tally "submit your map".
