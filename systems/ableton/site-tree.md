# Ableton site tree

Mapped 2026-11-21 from [https://www.ableton.com/en/](https://www.ableton.com/en/) with headless Playwright (desktop 1440×900, then the phone menu at 390×844). Every row is a control that was present on the loaded page. Auth branches were opened once to confirm the wall, then not followed. No form was submitted. Language and country selects were not changed (they POST).

The same shell repeats on every public page: top bar, footer newsletter, language select, country select, cookie banner. Those rows are written once.

## Shell (every public page)

| Control | Opens |
|---|---|
| Logo (grid mark) | Page `/en/` |
| Nav link Live | Page `/en/live/` |
| Nav link Push | Page `/en/push/` |
| Nav link Move | Page `/en/move/` |
| Nav link Note | Page `/en/note/` |
| Nav link Link | Page `/en/link/` |
| Nav link Shop | Page `/en/shop/` |
| Nav link Packs | Page `/en/packs/` |
| Nav link Help | Page `/en/help/` |
| Nav link Try Live 12 for free | Page `/en/trial/` |
| Nav link Log in or register | Auth wall `https://www.ableton.com/en/login/?next=/en/` (email or username, password, passkey, register). Branch stopped. |
| Button More (`aria-controls="more"`, desktop) | Menu panel, not a navigation. Links below. |
| Button Menu (`aria-controls="main-nav-content"`, phone) | Same links as the desktop bar plus the More panel, as a full-screen menu. |
| Cookie banner Close | Local dismiss. Not clicked (would record a consent choice). |
| Cookie banner Accept | Consent POST. Not clicked. |
| Cookie banner More info | Page `/en/privacy/` (privacy policy). |
| Footer Sign up (email field) | Form POST `/en/subscribe-to-newsletter/`. Not submitted. The GET of that path is a public newsletter page. |
| Footer select Language | Form POST `/set-language/`. Not changed. Options: English, Deutsch, Français, 日本語, 简体中文, Español. |
| Footer select country | Form POST `/en/change-country/`. Not changed. |
| YouTube modal (`abl-modal--youtube`, `role="dialog"`) | Hidden until a video control opens it. Close Dialog dismisses it. |

### More panel (desktop) and phone menu

| Control | Opens |
|---|---|
| Blog | Page `/en/blog/` |
| Ableton for the Classroom | Page `/en/classroom/` |
| Ableton for Colleges and Universities | Page `/en/colleges-universities/` |
| Certified Training | Page `/en/certified-training/` (directory of trainers; individual trainer pages not walked) |
| About Ableton | Page `/en/about/` |
| Jobs | Page `/en/jobs/` |
| Apprenticeships | Page `/en/ausbildung/` |
| Ableton Learn | External `https://learn.ableton.com/` |
| Learning Synths | External `https://learningsynths.ableton.com/` |
| Making Music | External `https://makingmusic.ableton.com/` |

### Footer columns

| Control | Opens |
|---|---|
| Register Live, Push or Move | Auth wall `https://www.ableton.com/en/account/add_license/` (redirects to login). Branch stopped. |
| About Ableton | Page `/en/about/` |
| Jobs | Page `/en/jobs/` |
| Facebook, X, YouTube, Instagram, TikTok, Discord icons | External social profiles. Not followed. |
| Offers for students and teachers | Page `/en/shop/education/` |
| Ableton for the Classroom | Page `/en/classroom/` |
| Ableton for Colleges and Universities | Page `/en/colleges-universities/` |
| Find Ableton User Groups | Page `/en/community/user-groups/` (directory; individual groups not walked) |
| Find Certified Training | Page `/en/certified-training/` |
| Become a Certified Trainer | Page `/en/education/certification-program/` |
| Contact Us | Page `/en/contact-us/` |
| Press Resources | Page `/en/press/` |
| Legal Info | Page `/en/legal/` |
| Corporate Information | Page `/en/corporate-information/` |
| Privacy Policy | Page `/en/privacy-policy/` (redirects to `/en/privacy/`) |
| Cookie Settings | Page `/en/cookie-settings/` (settings form with tracking-cookie checkboxes; not changed) |
| Imprint | Page `/en/imprint/` |
| Withdraw from Contract | External `https://help.ableton.com/hc/en-us/requests/new?ticket_form_id=26653726324764` (support form, not submitted) |

## Home `/en/`

| Control | Opens |
|---|---|
| Buy now (promo) | Page `/en/shop/live/` |
| Take a first look | Page `/en/live/` |
| Scroll down | In-page anchor `#`. No new page. |
| Blog teaser images and titles | Individual posts, for example `/en/blog/drum-synth-ned-rush/`, `/en/blog/step-sequencer-seed-to-stage/`, `/en/blog/live-13-is-coming/` |
| Category chips (Tutorials, News, Artists, Downloads, Videos, Loop) | Pages `/en/blog/categories/<name>/` |
| All posts / See all posts | Page `/en/blog/` |
| One Thing video titles | Page `/en/one-thing/` (some links add `?autoplay=`) |
| See all videos | Page `/en/one-thing/` |
| Video play badges | YouTube dialog on the same page |

## Live `/en/live/`

| Control | Opens |
|---|---|
| Previous feature / Next feature | In-page gallery step. Local. |
| Play … video | Video dialog (`abl-video-modal`). Close, previous, next, captions, play/pause stay in the dialog. |
| FAQ questions (`aria-expanded`, collapsed) | In-page disclosure. Local. |
| Back to top | Scroll to top. |
| Compare / edition links in body | Page `/en/live/compare-editions/` and shop links |
| Logout form in the DOM | POST `/en/logout/`. Not submitted. Signed-out session; no effect intended. |

## Push `/en/push/`, Move `/en/move/`, Note `/en/note/`

Product marketing pages. Body links open tech-spec anchors, feature lists (`/en/move/all-new-features/` and the same pattern on Push and Note), shop product pages, and YouTube embeds. Move's "Free practice lessons" leaves the site (Melodics). No auth wall on the marketing pages themselves.

## Link `/en/link/`

| Control | Opens |
|---|---|
| Check out the latest Link-enabled products | Page `/en/link/products/` |
| Play video | YouTube. Dialog or external watch URL. |
| App tiles | External partner product sites. Not followed. |
| Form action `/en/link/` | Present on the page. Not submitted. |

## Shop `/en/shop/`

| Control | Opens |
|---|---|
| Section tabs Overview, Live, Push, Move, Educational offers, Max for Live, Merchandise | In-page sections, and pages `/en/shop/live/`, `/en/shop/push/`, `/en/shop/move/`, `/en/shop/education/`, `/en/shop/merchandise/` |
| Buy now on Live | Page `/en/shop/live/` |
| Learn more (Max for Live) | Page `/en/live/max-for-live/` |
| Browse Packs | Page `/en/packs/` |
| Browse Merchandise | Page `/en/shop/merchandise/` |
| Add to cart forms | POST `/en/cart/add/`. Not submitted. |
| Verify Max serial | POST `/en/shop/verify-max-serial/`. Not submitted. |
| Ask us a question | External help center request form. Not submitted. |

## Shop Live `/en/shop/live/`

Redirects to `/en/shop/live/?tab=buy-now`.

| Control | Opens |
|---|---|
| Buy now / Rent-to-own | In-page tabs `#buy-now`, `#rent-to-own` |
| Log in to see your upgrade prices | Auth wall `https://www.ableton.com/en/login/?next=…/en/shop/live/?tab=buy-now`. Branch stopped. |
| Live 13 is coming | Page `/shop/live-13` |
| See full feature comparison | Page `/en/upgrade-live/` and `/en/live/compare-editions/` |
| Ableton account | Auth wall `https://www.ableton.com/en/account/`. Branch stopped. |
| Add to cart | POST `/en/cart/add/`. Not submitted. Cart page `/cart/` is itself a wall ("Your shopping cart") and was not used. |

## Packs `/en/packs/`

| Control | Opens |
|---|---|
| Filter chips (Sounds, Max for Live, Software Instruments, Bundles, Free, genres) | Same page with a query, for example `/en/packs/#?item_type=max_for_live` |
| Pack title | Pack detail, for example `/en/packs/generators-by-iftah/` |
| Artist name | Page `/en/packs/by/<artist>/` |
| Add to cart | POST `/en/cart/add/`. Not submitted. Download of a pack is an account action and was not followed. |

## Trial `/en/trial/`

Download and edition cards. Following a download was not done (it starts a file transfer and can require an account). Edition comparison links go to Live compare pages.

## Blog `/en/blog/`

| Control | Opens |
|---|---|
| Category row (All posts, Artists, News, Downloads, Tutorials, Videos, Loop, One Thing, Podcasts) | `/en/blog/`, `/en/blog/categories/<name>/`, `/en/one-thing/` |
| Post title | Individual post under `/en/blog/<slug>/` |
| Tag chip | `/en/blog/tags/<group>/<tag>/` |

One representative post (`/en/blog/live-13-is-coming/`) is in the capture set. The rest of the archive was not walked.

## Help `/en/help/`

| Control | Opens |
|---|---|
| Search form | External `https://help.ableton.com/hc/en-us/search`. Not submitted. |
| Go to the Knowledge Base | External `https://help.ableton.com/hc/en-us` |
| Live, Push, Move, Note | Pages `/en/help/live/`, `/en/help/push/`, `/en/help/move/`, `/en/help/note/` |
| FAQ disclosures | In-page. Local. |
| Article titles | External help-center articles. Not walked. |
| Learn Live / Learn Push / Learn Move | Learning sites already listed under More. |

## About, jobs, apprenticeships

| Control | Opens |
|---|---|
| About subnav Jobs | Page `/en/jobs/` |
| About subnav Apprenticeships | Page `/en/ausbildung/` |
| See job openings | Page `/en/jobs/` |
| Job title on `/en/jobs/` | Apply form `/de/jobs/apply/62213/` (profile and application fields). Not filled. Recorded as an application wall. |
| Apprenticeships "here" | Page `http://ableton.com/de/ausbildung` (German locale). Not switched. |

## Education and community

| Control | Opens |
|---|---|
| Classroom: Discover what's possible | Page `/en/classroom/why-teach-live-move/` |
| Classroom: Check your eligibility and apply | Page `/en/classroom/offers/` (application). Not filled. |
| Classroom: See the latest resources | Page `/en/classroom/support/` |
| Colleges newsletter Subscribe | Page `/colleges-universities/newsletter-signup/`. Not filled. |
| Certification program | Page `/en/education/certification-program/` |
| Events page (linked from community content, not the top nav) | Page `/en/events/`. In-page anchors for Ableton, Discord, and community events. Join and Book a slot leave the site (Eventbrite, Discord, Humanitix, Berlin spaces). Not followed. |

## Press, contact, legal

| Control | Opens |
|---|---|
| Contact: Help Center, sales question, technical request, developer request | External help-center forms. Not submitted. |
| Press: Sign up to press mailing list | Page `/en/press/signup` (loaded as the homepage shell; mailing-list fields not filled). |
| Press kit links | Zip downloads on `cdn-resources.ableton.com`. Not downloaded. |
| Press archive titles | Pages under `/en/press/press-archive/<slug>/` |
| Legal list | Pages `/en/gtc/`, `/en/privacy/`, `/en/eula/`, `/en/ableton-cloud-terms-of-service/`, `/en/copyright-and-licensing/`, `/en/legal/trademark-list/`, `/en/legal/patents/`, `/en/legal/branding-trademark-guidelines/`, `/en/safety-and-warranty/`, `/en/dpa`, `/en/imprint/` |

## Auth walls (opened, then stopped)

| URL | What it asks for |
|---|---|
| `https://www.ableton.com/en/login/` | Email or username, password, passkey. Also hosts the register form. |
| `https://www.ableton.com/en/register/` | Same document as login. Register form asks for a password. |
| `https://www.ableton.com/en/login/?next=/en/` | Same wall, with a return path. |
| `https://www.ableton.com/en/account/` | Redirects to login. |
| `https://www.ableton.com/en/account/add_license/` | Redirects to login. |
| `https://www.ableton.com/cart/` | Shopping cart. Not used. |
| `https://www.ableton.com/en/send-password-reset/` | Forgot-password link on the login page. Not opened (account recovery). |

## Not a page

| Control | Why it was left |
|---|---|
| Newsletter, language, country, add to cart, verify serial, logout | Forms. None submitted. |
| Cookie Accept and Close | Consent choice. Banner was hidden for clean shots and shown once as its own state. |
| External help center, Learn, Learning Synths, Making Music, social, partner apps, press zips | Off `www.ableton.com`. Named here, not captured. |
| Trainer directory and user-group directory | Same template repeated hundreds of times. Index pages captured; individuals not walked. |
| Dark theme | Not present. No theme toggle and no dark stylesheet. |
