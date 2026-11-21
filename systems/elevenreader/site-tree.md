# ElevenReader public site tree

Mapped 2026-11-21 from the signed-out public site, starting at https://elevenreader.io/. Cookie dialog was hidden after it was photographed, and not accepted. No email was typed. No password was typed. No form was submitted. Google and Apple were not clicked. Branches that open a login or signup wall stop at that URL.

Desktop captures are 1440 by 900 CSS pixels. Phone captures are 390 by 844 CSS pixels at 2x (780 by 1688 PNG).

## Shell

Marketing pages share one header, one promo band, and one footer. `/explore` adds a search field and filter chips. The reader app lives at `/reader/*` and stops at sign-in or sign-up.

### Promo band

| Control | Opens |
|---|---|
| Get this offer | https://elevenreader.io/reader/account/subscribe (redirects to `/reader/sign-up`, signup wall, stop) |

### Header (desktop)

| Control | Opens |
|---|---|
| Logo | https://elevenreader.io/ |
| Explore | https://elevenreader.io/explore |
| Discover | Mega-menu. Screenshot: [home-desktop-menu-discover.png](screenshots/home-desktop-menu-discover.png) |
| Features | Dropdown. Screenshot: [home-desktop-menu-features.png](screenshots/home-desktop-menu-features.png) |
| Upload & Listen | https://elevenreader.io/text-reader-app |
| Sign in | https://elevenreader.io/reader/sign-in (login wall, stop) |
| Start listening free | https://elevenreader.io/reader/sign-up (signup wall, stop) |

Discover menu items:

| Control | Opens |
|---|---|
| Explore all audiobooks | https://elevenreader.io/explore |
| Romance | https://elevenreader.io/genres/romance-audiobooks |
| Mystery & Thriller | https://elevenreader.io/genres/mystery-and-thriller-audiobooks |
| Science Fiction | https://elevenreader.io/genres/science-fiction-audiobooks |
| Technology | https://elevenreader.io/genres/technology-audiobooks |
| Action & Adventure | https://elevenreader.io/genres/action-and-adventure-audiobooks |
| Horror | https://elevenreader.io/genres/horror-audiobooks |
| Fan Fiction | https://elevenreader.io/genres/fan-fiction-audiobooks |
| Fantasy | https://elevenreader.io/genres/fantasy-audiobooks |
| New Releases We Can't Put Down | https://elevenreader.io/collections/new-releases-we-can-t-put-down-audiobooks/new_releases |
| On Everyone's Shelf | https://elevenreader.io/collections/on-everyone-s-shelf-audiobooks/on_everyones_shelf |
| Essential HarperCollins | https://elevenreader.io/collections/essential-harpercollins-audiobooks/essential_harpercollins |
| New York Times & Booker Prize Bestsellers | https://elevenreader.io/collections/new-york-times-booker-prize-bestsellers-audiobooks/critically_acclaimed |
| Best of Vinci Books | https://elevenreader.io/collections/best-of-vinci-books/best_of_vinci |
| Explore all collections | https://elevenreader.io/collections |
| Free Audiobooks | https://elevenreader.io/free-audiobooks |

Features menu items:

| Control | Opens |
|---|---|
| iOS App | https://elevenreader.io/download-mobile-app?placement=nav&platform=ios |
| Android App | https://elevenreader.io/download-mobile-app?placement=nav&platform=android |
| Chrome Extension | https://elevenreader.io/text-to-speech-chrome-extension |
| Iconic Voices | https://elevenreader.io/iconic-voices |
| Pricing | https://elevenreader.io/pricing |
| Free for Students | https://elevenreader.io/students |

There is no site-language switch in the header. Language is a filter on `/explore`.

### Header (phone)

| Control | Opens |
|---|---|
| Logo | https://elevenreader.io/ |
| Start listening | https://elevenreader.io/reader/sign-up (signup wall, stop) |
| Open menu (`button[aria-label="Open menu"]`) | Full-screen drawer. Screenshot: [home-phone-menu.png](screenshots/home-phone-menu.png) |

Drawer items: Explore, Discover, Features, Upload & Listen, Sign in (login wall), Start listening free (signup wall), Close.

| Drawer control | Opens |
|---|---|
| Discover | Nested list: the same genre and collection links as the desktop mega-menu. DOM text confirmed. The nested screenshot was clipped by the drawer animation and is not kept. |
| Features | Nested list: iOS App, Android App, Chrome Extension, Iconic Voices, Pricing, Free for Students. |

### Footer

Columns are `<details>` summaries: Get Started, Use Cases, Compare, Browse, Resources, Socials, Terms, Company. On desktop they render open. Screenshot: [home-desktop-footer.png](screenshots/home-desktop-footer.png).

| Control | Opens |
|---|---|
| Sign Up Free Online | `/reader/sign-up` (signup wall, stop) |
| Free for Students | `/students` |
| Get the iOS App | `/download-mobile-app?placement=footer&platform=ios` |
| Get the Android App | `/download-mobile-app?placement=footer&platform=android` |
| Get the Chrome Extension | Chrome Web Store (off-site, not crawled) |
| Pricing | `/pricing` |
| Iconic Voices | `/iconic-voices` |
| Read Aloud PDF | `/read-aloud-pdf` |
| ADHD PDF Reader | `/read-aloud-pdf/adhd-reader` |
| Dyslexia PDF Reader | `/read-aloud-pdf/dyslexia-pdf-reader` |
| Kindle Read Aloud | `/kindle-read-aloud` |
| AI Voice Reader App | `/ai-voice-reader-app` |
| Text Reader App | `/text-reader-app` |
| Text to Speech Browser Extension | `/text-to-speech-chrome-extension` |
| Text to Speech (TTS) Reader | `/text-to-speech-reader` |
| ElevenReader vs. Speechify | `/speechify-alternative` |
| ElevenReader vs. NaturalReader | `/naturalreader-alternative` |
| ElevenReader vs. Audible | `/audible-alternative` |
| ElevenReader vs. Readwise | `/readwise-alternative` |
| ElevenReader vs. Voice Dream Reader | `/voice-dream-reader-alternative` |
| All comparisons | `/compare` |
| Explore Audiobooks | `/explore` |
| Free Audiobooks | `/free-audiobooks` |
| Audiobooks by Genre | `/genres` |
| Audiobooks by Tag | `/tags` |
| Audiobook Collections | `/collections` |
| ElevenReader Blog | `/blog` |
| Help Using The App | https://elevenlabs.io/docs (off-site) |
| Help Publishing Your Books | https://elevenlabs.io/docs (off-site) |
| Report Copyright/IP Issue | https://help.elevenlabs.io (off-site form, not submitted) |
| Flag Inappropriate Content | https://help.elevenlabs.io (off-site form, not submitted) |
| System Status | https://statuspage.incident.io/elevenreader (off-site) |
| X, YouTube, Discord, Instagram, TikTok | Off-site socials, not crawled |
| ElevenReader Terms | `/elevenreader-terms` |
| Publishing Terms of Service | `/publishing-terms-of-service` |
| Publishing Content Guidelines | `/content-guidelines` |
| Publishing Payment Terms | `/publishing-payment-terms` |
| Cookie Settings | Cookiebot dialog. Not accepted. Screenshot: [home-desktop-cookie-settings.png](screenshots/home-desktop-cookie-settings.png) |
| About, Safety, Contact Partnerships | https://elevenlabs.io (off-site) |
| Careers | https://jobs.ashbyhq.com/elevenlabs (off-site) |

Cookie dialog buttons, recorded and not clicked: Reject all, a customize control, Accept all cookies. The dialog was hidden in the DOM for later shots (`display: none` on `#CybotCookiebotDialog`). Hiding is not an accept and not a reject.

## Pages loaded

The crawl loaded 70 public URLs (HTTP 200) and stopped with 1,764 same-site URLs still queued. Those leftovers are more audiobook, author, genre, collection, and blog URLs of the same patterns, not a different product surface.

| Page | URL | Desktop | Phone |
|---|---|---|---|
| Home | https://elevenreader.io/ | [home-desktop-default.png](screenshots/home-desktop-default.png) | [home-phone-default.png](screenshots/home-phone-default.png) |
| Pricing | https://elevenreader.io/pricing | [pricing-desktop-default.png](screenshots/pricing-desktop-default.png) | [pricing-phone-default.png](screenshots/pricing-phone-default.png) |
| Explore | https://elevenreader.io/explore | [explore-desktop-default.png](screenshots/explore-desktop-default.png) | [explore-phone-default.png](screenshots/explore-phone-default.png) |
| Genres index | https://elevenreader.io/genres | [genres-desktop-default.png](screenshots/genres-desktop-default.png) | [genres-phone-default.png](screenshots/genres-phone-default.png) |
| Text reader | https://elevenreader.io/text-reader-app | prior package [screenshots](screenshots) | [text-reader-phone-default.png](screenshots/text-reader-phone-default.png) |
| Sign-in wall | https://elevenreader.io/reader/sign-in | [signin-desktop-wall.png](screenshots/signin-desktop-wall.png) | [signin-phone-wall.png](screenshots/signin-phone-wall.png) |
| Sign-up wall | https://elevenreader.io/reader/sign-up | [signup-desktop-wall.png](screenshots/signup-desktop-wall.png) | [signup-phone-wall.png](screenshots/signup-phone-wall.png) |

Also loaded and inventoried, screenshots not all kept this pass: `/students`, `/iconic-voices`, `/read-aloud-pdf`, `/read-aloud-pdf/adhd-reader`, `/read-aloud-pdf/dyslexia-pdf-reader`, `/kindle-read-aloud`, `/ai-voice-reader-app`, `/text-to-speech-chrome-extension`, `/text-to-speech-reader`, five comparison pages, `/compare`, `/free-audiobooks`, `/tags`, `/collections`, `/blog`, four legal pages, one collection, several audiobook and author pages, and the app-store handoff at `/download-mobile-app`.

## Homepage controls

| Control | Destination | Stop |
|---|---|---|
| Start listening free | `/reader/sign-up?source=homepage` | signup wall |
| Upload & listen | `/text-reader-app` |  |
| Explore the library | `/explore` |  |
| Play preview | in-page audio preview |  |
| Previous / Next (coverflow) | in-page carousel |  |
| Voice names (James, Arabella, Sir Michael Caine, and others) | in-page narrator sample |  |
| Play narrator, Previous narrator, Next narrator | in-page voice carousel |  |
| Disable soundscape, Previous soundscape, Next soundscape | in-page soundscape control |  |
| Genre chips (Fantasy, Mystery & Thriller, Business, and others) | in-page filter of the homepage rail |  |
| FAQ questions | in-page accordion. One opened: [home-desktop-faq-open.png](screenshots/home-desktop-faq-open.png) |  |
| Listen Online / Listen now | `/reader/sign-up` | signup wall |

## Explore

Search is a field on `/explore`, not a header control on the homepage. Focus only, empty: [explore-desktop-search-focus.png](screenshots/explore-desktop-search-focus.png). No query was typed.

| Control | Opens |
|---|---|
| Tags | Filter menu. Not selected. |
| Genre | Filter menu of 31 genres. Screenshot: [explore-desktop-genre.png](screenshots/explore-desktop-genre.png). Selecting a genre was not done. |
| Price | Filter menu. Not selected. |
| Rating | Filter menu. Not selected. |
| Narrated by | Filter menu. Not selected. |
| Language | Filter menu: English, Brazilian Portuguese, Dutch, French, German, Italian, Polish, Portuguese, Spanish, plus a "Search language..." field that was not typed in. Screenshot: [explore-desktop-language.png](screenshots/explore-desktop-language.png) |
| Sort by | Menu: Popularity, Relevance, Newest. Screenshot: [explore-desktop-sort.png](screenshots/explore-desktop-sort.png). Not changed. |
| Mature content | In-page toggle. Not changed. |
| Top picks | `/collections/top-picks-audiobooks/explore_v4__top_picks` |
| Book covers | `/audiobooks/<slug>/<id>` public detail pages |

`/genres` lists 31 genre pages under `/genres/<slug>-audiobooks`. One index was photographed. Individual genre pages follow the same catalogue pattern and were not each photographed.

## Pricing

Monthly and Annual are in-page buttons. Annual is the painted default ($8/mo with a Save 25% chip). Monthly was clicked and paints $11/mo: [pricing-desktop-monthly.png](screenshots/pricing-desktop-monthly.png). Nothing was purchased.

| Control | Opens | Stop |
|---|---|---|
| Start listening free (Free plan) | `/reader/sign-up` | signup wall |
| Start 3-day free trial (Ultra) | `/reader/account/subscribe?billing_period=annual` or `monthly` | redirects to `/reader/sign-up`, signup wall |
| Get this offer | `/reader/account/subscribe?plan=ultra&...` | signup wall |

## Login wall

https://elevenreader.io/reader/sign-in asks for email and password, or Google or Apple. The first paint shows Sign in with Google, Sign in with Apple, and Sign in with email. Clicking Sign in with email reveals empty Email and Password fields, Forgot password, and Sign in. Nothing was typed. No code was sent. Google and Apple were not clicked.

Screenshots: [signin-desktop-wall.png](screenshots/signin-desktop-wall.png), [signin-desktop-email-empty.png](screenshots/signin-desktop-email-empty.png), [signin-phone-wall.png](screenshots/signin-phone-wall.png).

Forgot password opens a dialog: "Please enter your email and we'll send you a link to reset your password." The field was left empty. Reset password was not clicked. Screenshot: [signin-desktop-forgot.png](screenshots/signin-desktop-forgot.png).

Create account goes to `/reader/sign-up` and stops there.

## Signup wall

https://elevenreader.io/reader/sign-up shows Sign up with Google, Sign up with Apple, and Sign up with email. Sign up with email was not clicked, so no email field was filled. Terms of Service and Privacy Policy link to elevenlabs.io and were not followed. Screenshot: [signup-desktop-wall.png](screenshots/signup-desktop-wall.png), [signup-phone-wall.png](screenshots/signup-phone-wall.png).

## Stopped branches

- https://elevenreader.io/reader/sign-in
- https://elevenreader.io/reader/sign-up
- https://elevenreader.io/reader/sign-up?source=homepage
- https://elevenreader.io/reader/sign-up?source=explore_no_audiobooks
- https://elevenreader.io/reader/sign-up?source=marketing_no_homepage
- https://elevenreader.io/reader/account/subscribe (redirects to sign-up)
- https://elevenreader.io/reader/account/subscribe?billing_period=annual
- https://elevenreader.io/reader/account/subscribe?plan=ultra&billing_period=monthly&prefilled_promo_code=LISTENMORE30

The signed-in reader (library, player, upload, settings, billing) was not opened. Off-site links (App Store, Play Store, Chrome Web Store, elevenlabs.io, help.elevenlabs.io, socials, careers, status) were recorded and not crawled.
