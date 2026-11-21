# ROVR public site tree

Mapped from [https://www.rovr.live/](https://www.rovr.live/) on 2026-11-21 in headless Chromium, signed out, before screenshots were taken for the package. The product is ROVR (Radio Reinvented). The page paints one dark theme (`color-scheme: dark`, black page, yellow accent). No theme switch was found.

A control that opens a login or signup wall is recorded and that branch stops. No password was typed. No form was submitted. Google and Apple were not clicked. The contact control is a `mailto:` link; it was not opened.

## Shell

The same header and footer sit on every public page.

| Control | Opens |
|---|---|
| ROVR wordmark | [https://www.rovr.live/](https://www.rovr.live/) |
| RADIO | [https://www.rovr.live/](https://www.rovr.live/) |
| MOODS | [https://www.rovr.live/moods](https://www.rovr.live/moods) |
| SCHEDULE | [https://www.rovr.live/schedule](https://www.rovr.live/schedule) |
| CURATORS | [https://www.rovr.live/curators](https://www.rovr.live/curators) |
| ARCHIVE | [https://www.rovr.live/archive](https://www.rovr.live/archive) |
| SHOP | [https://shop.rovr.live/](https://shop.rovr.live/) (external shop; not captured) |
| MENU (`aria-label="open drawer menu"`) | Yellow navigation drawer, dialog, stays on the current page |
| Instagram | [https://instagram.com/rovr_live](https://instagram.com/rovr_live) (external) |
| App Store | Apple App Store listing (external) |
| Google Play | Google Play listing (external) |
| Alexa badge (`Open Alexa modal`) | Dialog: ENABLE ALEXA FOR ROVR, with an ENABLE link to Amazon |
| About Us | [https://www.rovr.live/about](https://www.rovr.live/about) |
| Rate Us | Google Play listing (external) |
| Privacy Policy | [https://www.rovr.live/privacy](https://www.rovr.live/privacy) |
| Terms & Conditions | [https://www.rovr.live/terms](https://www.rovr.live/terms) |
| Contact | `mailto:` (not opened; address not recorded) |
| Copyright line | UK Companies House company page (external) |

On a 390 px width the header links collapse. An `open menu` button opens the same yellow drawer. SIGN UP / SIGN IN in that drawer is a link to `/login`.

## Home (`/`)

Live radio player. The show title, curator and art change with the clock. At mapping time the show was Morning Strut.

| Control | Opens |
|---|---|
| Show quick menu | Expands two icon buttons beside the title: Share current show, Save show |
| Share current show | No dialog. A status toast: "Couldn't copy the link" (clipboard blocked in headless) |
| Save show | Dialog: "Sign in to save your favorite shows", with SIGN UP, SIGN IN, Continue with Google, Continue with Apple. Wall. Branch stops |
| Listen to music | Toggles the live player (play / pause). Stays on `/` |
| Time readout | A button. Click did not open a page or dialog |
| Curator name | `/curators/<slug>` (example: `/curators/andre-navarro`) |
| Like track | Disabled while the track metadata is the placeholder Title / Artist / Label. When enabled, expected to hit the same sign-in wall as MY TRACKS. Not followed |
| Share current track | Disabled in the same placeholder state. Not followed |
| Learn more about ROVR | `/about` |
| View the full schedule | `/schedule` |
| Explore our curators | `/curators` |
| Browse all radio shows | `/archive` |

## MENU drawer

Opened from MENU. Close control is `close drawer` (X). Version string `V0.1.103` sits at the bottom of the drawer. A SEARCH field in the drawer is a link to `/search`.

| Control | Opens |
|---|---|
| SIGN UP / SIGN IN | [https://www.rovr.live/login](https://www.rovr.live/login). Wall (email and password, Google, Apple). Branch stops |
| MY TRACKS | Dialog on the current page: "Sign in to see your liked tracks". Wall. Branch stops |
| MY SAVED SHOWS | Dialog: "Sign in to see you favorite shows". Wall. Branch stops |
| COMMUNITY RADIO (button) | Dialog with an application form (name, email, social links, mix link, website). Form fields were not filled. Not submitted |
| COMMUNITY RADIO (link) | `/#community-radio` |
| CURATOR MESSAGES | Dialog: "Sign in to chat with your favorite curators". Wall. Branch stops |
| RADIO, MOODS, SCHEDULE, CURATORS, ARCHIVE, SHOP | Same destinations as the header |
| SEARCH | [https://www.rovr.live/search](https://www.rovr.live/search) |
| CONTACT | `mailto:` (not opened) |

## Moods (`/moods`)

Three full-height stations: THINK, FEEL, MOVE. Each card is a button with a Listen to music control. Clicking play stays on the page and switches the station. No further route.

## Schedule (`/schedule`)

A week strip (SAT 21 through FRI 27 at mapping time) and a list of show rows. Day labels are not buttons; the strip did not expose a clickable day control. Each row links the curator name to `/curators/<slug>`. Share show copies (or fails to copy) and does not navigate. Listen to music on a row starts that show's audio and stays on the page.

## Curators (`/curators`)

A grid of curator cards. Each card links to `/curators/<slug>`. Search by name is a text field. Typing filters the grid in place (the capture types a public name and does not submit a form). Search button sits beside the field.

## Curator (`/curators/<slug>`)

One public curator page is in the capture (`/curators/andre-navarro`). The sitemap lists many more curator URLs; they share this template. Go back returns to the list. View Archive links to `/archive?query=<name>`. Each episode row's View tracklist opens `/show/<id>`. Share show is the same copy action as on the schedule.

## Archive (`/archive`)

Show cards. Search by Curator or by Show filters in place. Shows / Saved are tabs. Saved opens a sign-in dialog ("Sign in to save your favorite tracks and shows"). Wall. Branch stops. Save show on a card opens the same wall. Go to show opens `/show/<id>`. Share show is the copy action. A collapsed filter button is present; opening it did not reveal a separate panel beyond the drawer already on the page.

## Show (`/show/<id>`)

Reached from Archive's Go to show and from a curator episode's View tracklist. Two public examples were opened. TRACKLIST toggles the track list on the same page. Go back returns. Message (`Open curator message form`) is the curator-message wall. Like track and Share show behave as on the player. Listen to music plays the archived show on the page.

## Search (`/search`)

Reached from the drawer SEARCH link. The field updates the query (`/search?q=`) as you type. Results list artist pages and tracks inside the drawer. Clear resets the field. Artist and track rows were not followed into an account. No form was submitted.

## About, privacy, terms

| URL | What it is |
|---|---|
| `/about` | Marketing manifesto. No further in-site controls beyond the shell |
| `/privacy` | Privacy notice. Long document. In-page anchors only |
| `/terms` | Terms and conditions. Long document. In-page anchors only |

Static sitemap (`/sitemaps/sitemap-static`) lists only `/`, `/about`, `/schedule`, `/curators`, `/archive`, `/privacy`, `/terms`. Dynamic sitemaps list curator, artist and article URLs. Article and artist templates were not walked; one curator template and one show template stand in for those families.

## Auth walls (recorded, not entered)

| URL or control | What it shows | Action |
|---|---|---|
| `/sign-in` | WELCOME BACK, email, password, Reset my password, SIGN IN, Google, Apple | Stopped. Password was not submitted |
| `/login` | RADIO REINVENTED, SIGN UP / SIGN IN tabs, email, password, Google, Apple | Stopped |
| `/sign-up` | RADIO REINVENTED, email, password, SIGN UP, Google, Apple | Stopped. No account created |
| `/forgot-password` | Linked from Reset my password on `/sign-in` | Not opened. Auth branch |
| Drawer SIGN UP / SIGN IN | Navigates to `/login` | Stopped |
| MY TRACKS, MY SAVED SHOWS, CURATOR MESSAGES, Save show, Saved, Message | Sign-in dialog on the current page | Stopped. Google and Apple not clicked |

## Not in the public tree

Shop (`shop.rovr.live`), Instagram, the app stores, Amazon Alexa enablement, and Companies House are external. The signed-in library (liked tracks, saved shows, curator chat) was not reached. Community Radio's application form was opened and not filled.
