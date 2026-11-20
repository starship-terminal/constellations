# Prime Video public site tree

Mapped from the signed-out homepage at https://www.primevideo.com/ on 2026-11-21, before screenshots. The homepage redirects to `/offers/nonprimehomepage`. The browser that loaded it was headless Chromium (Playwright), desktop 1440x900, locale en-US. The storefront that came back prices the trial in the page's own currency. No account was created and no form was submitted.

A control that opens Amazon Sign-In is a wall. That branch stops at the URL. Password was not submitted. Nothing was typed into an email or mobile field.

## Homepage

https://www.primevideo.com/ redirects to https://www.primevideo.com/offers/nonprimehomepage

| Control | Opens |
|---|---|
| prime video wordmark | `/storefront`, which redirects back to `/offers/nonprimehomepage` |
| Home | `/storefront`, same redirect |
| Movies | `/movie` (public browse) |
| TV shows | `/tv` (public browse) |
| Sports | `/sports` (public browse) |
| Search button (aria-label "Search Prime Video") | In-page search panel with a search field (`#pv-search-nav`, placeholder "Search"). Enter submits a search. Not submitted. |
| EN | Language menu, in page. Items are language names (Bahasa Indonesia, Bahasa Melayu, Dansk, Deutsch, English, and further languages through 한국어). Selecting one would change the storefront language. Not selected. |
| Categories (grid icon) | `/categories` |
| Profile, Settings, and Account | Account menu, in page |
| Join Prime (header) | `/signup`, which redirects to Amazon Sign-In. Wall. |
| Prime Member? Sign in | `/gp/video/signup` (offer=pm), which redirects to Amazon Sign-In. Wall. |
| Start your 30-day free trial | `/gp/video/signup` (offer=ft), which redirects to Amazon Sign-In. Wall. |
| Sign up now (NBA promo, below the fold) | `/gp/video/signup`, which redirects to Amazon Sign-In. Wall. |
| Start your 30-day free trial (repeated lower on the page) | `/gp/video/signup`, wall |
| Terms and Privacy Notice | `/help?nodeId=202064890` (also linked as `/ww-av-legal-home`, which lands on the same help node) |
| Send us feedback | `/contactus`, which redirects to Amazon Sign-In. Wall. |
| Help | `/help` |

## Account menu

Opened from Profile, Settings, and Account. Stays on the current page.

| Item | Opens |
|---|---|
| Sign In | `/auth-redirect?signin=1`, which redirects to Amazon Sign-In. Wall. |
| Help | `/help` |
| Watch Anywhere | `/splash/watchAnywhere` |
| Join Prime | `/signup`, wall |

## Language menu

Opened from EN. A list of language buttons. No navigation until one is chosen. None was chosen.

## Search

The search button opens a panel. The field is a search input. Typing a query was not done in the capture (the task forbids typing an email or a mobile number; a title query is not that, but the field was left empty so no search request was sent). Pressing Enter would submit. Not submitted.

## Movies, TV shows, Sports

Each is a public browse page with poster cards and "See more" links.

| Control | Opens |
|---|---|
| Poster card | `/detail/<title-id>` (public title page) |
| See more | A browse or collection URL on the same host when the card row has one. `/browse` itself redirects to the signed-out homepage. |
| Header controls | Same as the homepage |

## Categories

https://www.primevideo.com/categories

| Control | Opens |
|---|---|
| Action and adventure | `/genre/action` |
| Romance | `/genre/romance` |
| Horror | `/genre/horror` |
| Mystery and thrillers | `/genre/suspense` |
| Comedy | `/genre/comedy` |
| Drama | `/genre/drama` |
| Kids | `/kids` |
| Fantasy | `/genre/fantasy` |
| Documentary | `/genre/documentary` |
| Science fiction | `/genre/science-fiction` |
| Anime | `/genre/anime` |
| Historical | `/genre/historical` |
| New releases | `/collection/newandupcoming` |
| Korean content | `/collection/ktime` |
| Best of India | `/collection/best_of_india` |
| Made in South East Asia | `/collection/madeinsea` |
| Obsession is in Session | `/collection/ya_women_sea` |
| The Harry Potter Collection | `/collection/sea_hp26` |
| Footer Terms and Privacy Notice | `/ww-av-legal-home` then `/help?nodeId=202064890` |
| Footer Send us feedback | `/contactus`, wall |
| Footer Help | `/help` |

Genre and collection pages repeat the same pattern: filter chips (All, Movies, TV shows), poster rows, See more, and title links to `/detail/<id>`.

## Title page

Example reached from Movies: `/detail/0GOXEUMNGKVV4AQ0HEBYT02TD5` (public).

| Control | Opens |
|---|---|
| Watch trailer | Full-screen player (`#dv-web-player`). On this capture the player showed "Video Unavailable" and an OK button. OK closes it. |
| Add to Watchlist | Amazon Sign-In. Wall. Not clicked in the capture after the trailer overlay blocked it; the control is a submit button and the same class of account action as Like. |
| Like | Amazon Sign-In. Wall. Clicked once to confirm the destination, then the branch stopped. Password was not submitted. |
| Not for me | Same account-action class as Like. Not clicked, so the destination is not captured. |
| Share | In-page dialog: Email, Facebook, X, Whatsapp, Copy link. Email would leave the page into a mail composer. Not clicked. |
| 30-day free trial / Join Prime | `/signup`, wall |
| Genre links under the synopsis (Comedy, Fantasy, and others) | `/genre/<slug>` |
| Related | Selected tab, related titles |
| Details | Second tab on the same page |
| More like this / related posters | Other `/detail/<id>` pages |

## Help

https://www.primevideo.com/help

| Control | Opens |
|---|---|
| Account Details | `/settings`, Amazon Sign-In. Wall. |
| Register a Device | `/ontv/code`, Amazon Sign-In. Wall. |
| Parental Controls | `/settings/parental-controls`, Amazon Sign-In. Wall. |
| Watch History | `/settings/watch-history`, wall (same account gate as the other settings links) |
| Prime Video Profiles | `/profiles`, Amazon Sign-In. Wall. |
| Help article titles | `/help?nodeId=<id>` on the same host. One article was opened in the capture. |
| Contact Us | `/contactus`, wall |
| Terms and Privacy Notice | `/ww-av-legal-home` |

https://www.primevideo.com/privacyprefs/primevideo returned the public error page "That shouldn't have happened." It is not a settings form.

## Watch anywhere

https://www.primevideo.com/splash/watchAnywhere is a public marketing page. Device-store buttons on it leave primevideo.com. They were not followed.

## Phone width

At 390x844 the same homepage loads. The header collapses: the wordmark, a menu control, search, and Join Prime stay in the bar. The menu opens the same destinations as the desktop header (Home, Movies, TV shows, Sports, Categories, account). Captured as its own state. No extra public route appeared.

## Walls (stop)

Every one of these ended at https://www.amazon.sg/ap/signin (title "Amazon Sign-In"), with an email-or-mobile field and a password field. Password was not submitted. No email or mobile number was typed.

- Join Prime, Sign in, Start your 30-day free trial, Sign up now
- Profile menu Sign In (`/auth-redirect`)
- Send us feedback and Contact Us (`/contactus`)
- Like on a title page
- `/settings`, `/settings/parental-controls`, `/profiles`, `/ontv/code`

Signed-in storefront, playback of a full title, watchlist, profiles, and purchases are behind that wall.
