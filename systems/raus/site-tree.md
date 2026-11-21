# Raus site tree

Mapped on 2026-11-21 from the public site at https://www.raus.life/, signed out, in headless Chromium at 1440 x 900. Cookiebot mounts over the page. Customize reveals a visible Deny control. Clicking Deny sets Cookiebot consent to necessary only (preferences, statistics and marketing false, method explicit). No form was filled. No account sign-in exists on www.raus.life: `/login` returns the styled 404 ("(404) Page not found | Raus", heading "404").

Theme: one light surface. `color-scheme` on the document is `normal`. No `data-theme`, `data-mode`, or dark class. `prefers-color-scheme: dark` was light in the capture browser. Dark is not present.

## Header (every marketing page)

| Control | Opens |
|---|---|
| Logo | `/` |
| Book now! | `/search` |
| Book a Cabin | `/search` |
| Staying with Us | `/staying-with-us` |
| Extras & Experiences | `/extras` |
| Become a Host | `/partner-categories` |
| Gift Cards | `https://shop.raus.life` (external shop, left) |
| Language select (`en` / `de`) | switches locale; `/en` is the English home |
| Phone menu button | opens the nav list: Book a Cabin, Staying with Us, Extras & Experiences, Become a Host, Gift Cards, social links, Help, language |

## Home search bar

The home hero and the search page share one search bar. Each control opens a popover, not a new URL. Search navigates.

| Control | Opens |
|---|---|
| All Regions | Region list: Germany, then Around Berlin, Hamburg, Frankfurt, Düsseldorf, Cologne, Stuttgart, Munich, Bremen, Dortmund, Dresden, Erfurt, Hanover (list continues past the first read) |
| Date | Date range picker |
| 2 Guests | Guest stepper (adults / children) |
| Search | `/search` (with the chosen query when one is set) |
| Book your stay | `/search` |

## Home body and footer

| Control | Opens |
|---|---|
| Start quiz / Cabins near me / Which Cabin Suits You? | `https://finder.raus.life/en` (cabin finder, separate host) |
| Choose your cabin | `/search` |
| Journal cards | one article, for example `/journal/original-feelings` |
| View all articles | `/journal` |
| Sign up for Newsletter | `https://eepurl.com/hDXVCz` (Mailchimp, not filled) |
| FAQs | `/help` |
| Contact | `/#open-chat` (chat widget, not a message sent) |
| Waiting List | `https://form.jotform.com/Stay_Raus/waiting-list` (form, not filled) |
| Packing List | `/what-to-bring` |
| Last Minute Deals | `/lastminute` |
| Travel Companion | `https://companion.raus.life/` |
| Food & Experiences | `/extras` |
| About Us | `/about` |
| Press | `/media` |
| Sustainability | `/sustainable-travelling` |
| Journal | `/journal` |
| Careers | Personio jobs board (external) |
| Team Events | `https://business.raus.life/teams` |
| Retreats (footer) | `https://business.raus.life/retreats` |
| Activations & Productions | `https://business.raus.life/brands-and-agencies` |
| Creator Requests | `https://forms.raus.life/creator` (form, not filled) |
| B2B Gift Cards | `https://business.raus.life/gift-cards` |
| Cabins Close to a Farm | `/raus-cabins-close-to-a-farm` |
| Cabins by the Lake | `/raus-cabins-by-the-lake` |
| Cabins by the Sea | `/raus-cabins-near-the-sea` |
| Cabins in the Forest | `/raus-cabins-in-the-forest` |
| Buy Your Cabin | `/cabin-sales` |
| Trainees & Students | `/raus-student` |
| Imprint / Data Privacy / Terms & Conditions / Accessibility | `/imprint`, `/data-privacy`, `/terms-and-conditions`, `/accessibility` |
| Social icons | Facebook, Instagram, LinkedIn, TikTok, YouTube (external) |

`/teams`, `/brands-and-agencies`, `/creator`, `/gift-cards` and `/collections/gift-cards` on www.raus.life are 404s. The live destinations are the business, shop and forms hosts above.

## Search (`/search`)

| Control | Opens |
|---|---|
| All Regions / Date / Guests | the same popovers as home |
| Search | stays on `/search` with the query |
| Scroll left / Scroll right | amenity chip rail |
| Dogs allowed, Sauna, Hot tub, Lake nearby, Sea nearby, New cabins, Group Stay, Guests' Favourites | toggles a taxonomy filter on `/search` |
| Filters | filter sheet |
| Explore Location (each card) | `/locations/<slug>`, for example `/locations/lodge-am-see` |

Collection landings (`/raus-cabins-by-the-lake` and the farm, sea and forest pages) repeat this card grid.

## Location (`/locations/<slug>`)

| Control | Opens |
|---|---|
| Go back | previous listing |
| Book now | booking dates on the same page (not submitted) |
| Date / Guests | the shared pickers |

One location is captured (Lodge am See). The sitemap lists dozens more of the same template. They are not each captured.

## Help, extras, journal

| Page | Interaction |
|---|---|
| `/help` | FAQ groups. A question expands in place. No form submitted. |
| `/extras` | category links such as `/category-local-food`, `/animal-activities`, `/nature-activities`, `/category-sauna` |
| `/journal` | article cards to `/journal/<slug>` |
| `/partner-categories` | host concept page. Host application forms are not filled. |

## Not on this host

| Host | What it is | Captured |
|---|---|---|
| shop.raus.life | gift shop | no, separate storefront |
| finder.raus.life | cabin quiz | no |
| companion.raus.life | travel companion | no |
| business.raus.life | retreats and B2B | no |
| forms.raus.life, form.jotform.com, eepurl.com | forms and newsletter | not filled |

## Sign-in

No account sign-in on the public site. `/login` is a 404, not a login wall. Newsletter, waiting list, creator request and chat were not filled.
