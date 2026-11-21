# Vevo site tree

Mapped on 2026-11-21 from the public homepage before screenshots, in headless Chromium (Playwright). `https://www.vevo.com/` returns 200 and redirects to `https://www.hq.vevo.com/`. The live site is a Wix marketing site for the music-video network. It has no sign-in control on the homepage.

Widths probed: desktop 1440x900, phone 390x844. Cookie banner is hidden in the capture script (FIELD-NOTES: never click Decline or Accept). No form is submitted.

## Shell

| Control | Opens |
|---|---|
| Logo (header and footer) | `/` (home) |
| About | `/about` |
| Originals | `/originals` |
| People | `/people` |
| For Advertisers | `/for-advertisers` |
| For Artists | `/vevo-for-artists` |
| Newsroom | `/newsroom` |
| Skip to Main Content | jumps to main, no new page |
| Phone hamburger (`#comp-lklqhtjc_r_comp-ldc6q7ym`, top right at 390) | Site navigation drawer: Home, About, Originals, People, For Advertisers, For Artists, Newsroom, plus an unlabeled link to `/home-old` |
| Drawer close | closes the drawer, stays on the page |
| Footer Contact | `/contact` |
| Footer Brand | `https://brand.vevo.com/` (separate host, left as a boundary) |
| Footer Careers | `https://jobs.lever.co/vevo` (Lever, left as a boundary) |
| Footer social (YouTube, Facebook, Instagram, Twitter, LinkedIn) | off-site, not captured |
| Privacy Policy | `/privacy-policy` |
| Terms of Use | `/terms-of-use` |
| Cookie banner Decline / Accept / Close | consent controls. Not clicked. Banner is hidden for screenshots. "Learn more about how we use cookies" goes to `/privacy-policy` |
| Hidden link in the footer markup | `/home-old` (password wall, not a public page) |

Desktop header links are always visible. The hamburger exists only at phone width.

## Home (`/`)

| Control | Opens |
|---|---|
| About Us | `/about` |
| Learn More (artists block) | `/vevo-for-artists` |
| Play video (Ariana Grande live performance) | in-page Wix video lightbox (`video.wixstatic.com`), same URL. Close returns to the page |
| Original Content Offerings | `/originals` |
| Explore (watch block) | `/watch-old`, which redirects to `/originals` |
| Learn More (advertisers block) | `/for-advertisers` |
| Each news card | that press post under `/press/<slug>` |
| View All | `/blog` |

## About (`/about`)

| Control | Opens |
|---|---|
| Play video (Somos Vevo promo) | in-page video lightbox, same URL |
| Start Now (repeated, a platform carousel) | stays on `/about`. The buttons are Wix slideshow controls, not navigation |

## Originals (`/originals`)

Marketing page. Primary links return to the shell (About, For Artists). No extra dialog.

## People (`/people`)

| Control | Opens |
|---|---|
| Join Our Team / careers links | `https://jobs.lever.co/vevo` (boundary) |

## For Advertisers (`/for-advertisers`)

| Control | Opens |
|---|---|
| Play video (GTM sizzle, J Balvin reel) | in-page video lightbox, same URL |
| Mute | toggles the background reel's sound, same page |
| Specs / technical links | `/advertising/specs` |
| Advertising policy link | `/advertisingpolicy` |
| Contact / get in touch | `/for-advertisers-contact` |

## Specs (`/advertising/specs`)

| Control | Opens |
|---|---|
| Video Preroll (`aria-expanded`, `aria-haspopup`) | expands an in-page panel: General Specs, Site Served, VAST Served (same URL anchors), plus an external VAST 3 link |
| Skippable Preroll | same pattern, second accordion, same URL |
| More Video Preroll pages | Wix overflow for the accordion. Click timed out on a covered control. Recorded, not forced |
| betterads.org, IAB VAST, Google 3PAS | off-site, not captured |

## Advertiser contact (`/for-advertisers-contact`)

A form. Fields: Name (required), Agency / Brand, Country (select), Email (required), How can Vevo help? (required textarea), newsletter checkbox, Submit. Not filled. Not submitted. Focus and empty-invalid states only.

## For Artists (`/vevo-for-artists`)

| Control | Opens |
|---|---|
| Play video (Keshi live) | in-page video lightbox |
| Mute | sound toggle, same page |
| Vevo 101 | `/vevo-101` |
| Distribution | `/distribution` |
| Label partners | `/label-partners` (password wall, stop) |
| Artist support | `/contact-artist-support` (form, not submitted) |
| Feedback | `/for-artists-feedback` (survey radios and text areas, not filled, not submitted) |
| Glossary | `/glossary` |
| Distributor names (DashGo, DistroKid, and others) | off-site partner sites, not captured |

## Vevo 101 (`/vevo-101`)

Play video opens the live-channel preview lightbox. Start Now buttons are the same Wix slideshow controls as About. They stay on the page.

## Distribution (`/distribution`)

Play video opens the ad-programming reel lightbox. Mute toggles sound. Partner logos link off-site (Roku, Samsung, and others). Not followed.

## Newsroom (`/newsroom`) and blog (`/blog`)

| Control | Opens |
|---|---|
| A post card | `/press/<slug>` |
| Blog category chips | `/blog/categories/blog` and `/blog/categories/news` |

One press post is captured as the article pattern. The rest of `/press/*` is the same template (share row, recent posts). Not every slug is a separate screen.

## Press post (`/press/<slug>`)

| Control | Opens |
|---|---|
| More actions (`aria-expanded=false`) | share row already on the page: Facebook, X, LinkedIn, copy link, Print. Like post is a Wix reaction. Not clicked (it writes state) |
| Expand image | image lightbox, same URL |
| Recent post links | other `/press/<slug>` pages |

## Contact (`/contact`)

Department blocks with published mailto links (general, artist support, media, advertising, closed captioning). No form on this page. Those addresses are not copied into this package. The contact page is not screenshotted, because the addresses are painted on it.

## Privacy (`/privacy-policy`) and terms (`/terms-of-use`)

Reached, then not kept as screenshots. The terms page paints a published office address, and this package does not store locations. In-page section links stay on the same URL. "More Language pages" is a Wix language menu. The click timed out (covered control). Language copies that the crawl already found, not captured as separate screens:

- `/privacy-policy/es`, `/es-latam`, `/fr-ca`, plus `/br`, `/de`, `/fr`, `/it` linked from the page
- `/terms-of-use/br`, `/de`, `/es`, `/esp`, `/fr`, `/it`

## Walls and dead ends

| URL | What loaded | Branch |
|---|---|---|
| `https://www.vevo.com/login` | HTTP 503, empty document, no form | stopped |
| `https://www.hq.vevo.com/login` | HTTP 404, "Looks like something went wrong on our end." | stopped |
| `/home-old` | password field and a Go button | stopped, not filled |
| `/label-partners` | same password wall | stopped, not filled |
| `/blank` | linked in markup, not a public screen | not captured |

No Google or Apple button appeared. No account, plan, birthday, or onboarding form appeared on a public page.

## Not in this tree

`brand.vevo.com` and `jobs.lever.co` are named in the footer and left as boundaries. YouTube, social, and distributor sites are off-site. There is no theme switch. The site paints one light theme.
