# Site tree

Captured 2026-11-21 with headless Playwright, signed out. `https://clay.earth/` returns 301 to `https://me.sh/`. The product on that host calls itself Mesh. The catalog name stays Clay.

A control that opens a sign-in or sign-up wall is recorded and that branch stops. Identity-provider buttons were not clicked. Download installer URLs were not followed.

## Redirects

| Request | Result |
|---|---|
| `https://clay.earth/` | 301 to `https://me.sh/` |
| `https://clay.earth/pricing` | 200 at `https://me.sh/pricing` |
| `https://clay.earth/login` | 404 at `https://me.sh/login` |
| `https://me.sh/login` | 404, marketing chrome, heading "Not Found" |
| `https://app.me.sh/` | 200 at `https://app.me.sh/login` (sign-in wall) |
| `https://me.sh/press/kit` | Notion "unsupported browser" page. Stopped |
| `https://me.sh/terms` | 403 at `library.me.sh` ("Confirm you are human"). Stopped |
| `https://me.sh/security-and-privacy` | 403 at `library.me.sh`. Stopped |
| `https://me.sh/new` | 403 at `library.me.sh/whats-new/`. Stopped |

## Shared chrome

Present on marketing pages at desktop 1440. Home paints dark. Pricing, integrations, stories, about, contact, careers, start, nexus, teams, notion, x, vision pro, next, and acknowledgements paint light, with the same links.

| Control | Opens |
|---|---|
| Logo | `https://me.sh/` |
| Releases (`#Releases_Button`) | In-page menu `#Releases_Panel`. Does not navigate |
| Resources (`#Resources_Button`) | In-page menu `#Resources_Panel` |
| Company (`#Company_Button`) | In-page menu `#Company_Panel` |
| Pricing | `https://me.sh/pricing` |
| Sign in | `https://app.me.sh/login?signin` (sign-in wall). Branch stops |
| Get started | `https://app.me.sh/login` (same wall). Branch stops |

### Releases menu

| Item | Opens |
|---|---|
| Integrations | `https://me.sh/integrations` |
| Nexus | `https://me.sh/nexus` |
| Teams | `https://me.sh/teams` |
| 100M | `https://me.sh/serendipity` |
| Introducing Mesh for Notion | `https://me.sh/notion` |

### Resources menu

| Item | Opens |
|---|---|
| Stories | `https://me.sh/stories` |
| Our apps | `https://me.sh/start` |
| Library | `https://library.me.sh/` (external docs). Not walked past the link |
| Tutorials | `https://www.youtube.com/@getmeshapp/playlists` (external). Not walked |

### Company menu

| Item | Opens |
|---|---|
| About Mesh | `https://me.sh/about` |
| Our origins | `https://me.sh/story` |
| Careers | `https://me.sh/careers` |

### Footer

Same links on the marketing pages that render the footer.

| Item | Opens |
|---|---|
| Integrations | `https://me.sh/integrations` |
| Notion | `https://me.sh/notion` |
| X | `https://me.sh/x` |
| Vision Pro | `https://me.sh/apple-vision-pro` |
| 100 million | `https://me.sh/serendipity` |
| Nexus AI | `https://me.sh/nexus` |
| What's new | `https://library.me.sh/whats-new` (403 in this browser). Stopped |
| Stories | `https://me.sh/stories` |
| Our apps | `https://me.sh/start` |
| Library | `https://library.me.sh/` |
| Tutorials | YouTube playlists (external) |
| About Mesh | `https://me.sh/about` |
| Our origins | `https://me.sh/story` |
| Press kit | `https://me.sh/press/kit` (Notion unsupported-browser). Stopped |
| Contact | `https://me.sh/contact` |
| Pricing | `https://me.sh/pricing` |
| Terms | `https://library.me.sh/knowledge-base/terms-of-use` (also `https://me.sh/terms`, 403). Stopped |
| Privacy | `https://library.me.sh/knowledge-base/security-and-privacy`. Stopped |
| LinkedIn, YouTube, Dribbble, X icons | External profiles. Not walked |
| Automattic mark | `https://automattic.com/`. Not walked |

### Phone (390)

The desktop nav is hidden. Header is the logo (`/`) and a `div.y0DxmG_toggle` (hamburger, not a button). The toggle opens the same Releases, Resources, and Company groups plus Pricing and "Get started for free" (`https://app.me.sh/login`). Screenshot: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Home (`https://me.sh/`)

| Control | Opens |
|---|---|
| Get Mesh free | `https://app.me.sh/login`. Wall. Stopped |
| Birthdays, Events, News, Social changes, Posts, Reconnect, Reminders, Sharing, Upcoming | In-page filter on the product demo. Birthdays adds class `_9nEsHa_activeFilterButton`. No navigation |
| View all integrations | `https://me.sh/integrations` |
| See Mesh for Teams | `https://me.sh/teams` |
| Testimonial dots (`Show <name> testimonial`) | In-page. A click did not open a dialog |
| Footer and chrome | As above |

## Pricing (`https://me.sh/pricing`)

| Control | Opens |
|---|---|
| Pay monthly / Pay annually | In-page price switch. Annual is selected on load. Monthly shows $20 and $49 copy |
| Personal "Get started" (`#CTA_Personal`) | `https://app.me.sh/login`. Wall. Stopped |
| Pro "Try it free" (`#CTA_Pro`) | `https://app.me.sh/login`. Wall. Stopped |
| Team "Try it free" (`#CTA_Team`) | `https://app.me.sh/login`. Wall. Stopped |
| Enterprise "Contact us" | `mailto:care@me.sh` with an enterprise subject. Not sent |
| Educational / invoice / security mail links | `mailto:care@me.sh`. Not sent |
| Apple subscription help | `https://support.apple.com/en-us/118428`. Not walked |
| Privacy policy link | `https://me.sh/security-and-privacy` (403). Stopped |
| Get Mesh free | `https://app.me.sh/login`. Wall. Stopped |

## Integrations (`https://me.sh/integrations`)

Search field filters the catalog in place. Typing "gmail" left one card. Not submitted.

Category chips (All, Communication, Productivity, Sales, Social) are in-page. All is selected on load.

Each card opens `/integrations/<slug>`. A card page has "All integrations" back to `/integrations`, a Connect control to `https://app.me.sh/login` (wall, stopped), a docs link on `library.me.sh` (not walked past the URL), related cards, and "Request integration" (`mailto:care@me.sh`, not sent).

Slugs linked from the catalog or from card footers:

address-book, adobe-creative-cloud, adobe-xd, airtable, atlassian-confluence, babbel, basecamp, bitly, canva, chatgpt, clickup, contacts, coursera, csv, duolingo, facebook, figma, flickr, gmail, google-calendar, google-workspace, hootsuite, hubspot, imessage, instagram, kajabi, lynda-linkedin-learning, mailchimp, make, microsoft-outlook, microsoft-teams, mixpanel, notion, phone-calls, pinterest, quora, signal, skype, slack, smartsheet, snapchat, spotify, squarespace, surveymonkey, telegram, tiktok, trello, twitter-x, udemy, vimeo, webflow, whatsapp, wix, zapier, zendesk.

Visited as the template: address-book, chatgpt, contacts, csv, facebook, gmail, google-calendar, imessage, instagram, make, microsoft-outlook, notion, phone-calls, twitter-x, whatsapp, zapier, adobe-xd. Each returned 200 with the same chrome. The rest are the same card template, linked, not each opened.

## Stories (`https://me.sh/stories`)

Each card opens `/stories/<slug>`. A story page has share buttons (LinkedIn, email, X). Those were not clicked. Related stories link to other slugs.

Slugs seen: 100m, building-rapport, career-mentor, career-networking, clay-for-real-estate-agents, digital-rolodex, follow-up, grant-and-glueck-study, likable, lindsay-kaplan, mesh, mesh-ai, organize-and-group-contacts, personal-relationship-manager-deepdive, remember-birthdays, soc2-certification, ultimate-networking-tip, will-allen.

Visited: mesh-ai, 100m, mesh, likable, lindsay-kaplan, will-allen, soc2-certification, career-mentor, career-networking, digital-rolodex, personal-relationship-manager-deepdive. Each 200.

## Other marketing pages

| Path | What its own controls open |
|---|---|
| `/nexus` | Get early access to `https://app.me.sh/login` (wall). Product Hunt (external, not walked). Read more to `/stories/mesh-ai` |
| `/teams` | Press logos to external articles (not walked). Get started to `https://app.me.sh/login` (wall) |
| `/start` | macOS download `https://me.sh/api/download/mac` (download starts; not followed). Windows download `https://me.sh/api/download/windows` (same). Web app `https://app.me.sh/` (sign-in wall). App Store, Play Store, Chrome, Safari, Firefox, Edge, Vision Pro store links (external, not walked) |
| `/about` | Origins to `/story`. Team to `/careers`. Advisor cards to `/<handle>`, which redirects to `/profile/<slug>` (public profile, then rate-limited). Stories, product updates (`/new`, 403), X and LinkedIn (external) |
| `/story` | External books and papers. Not walked |
| `/careers` | Shared chrome only in the visible control list. No application form was shown |
| `/contact` | `mailto:care@me.sh` and `mailto:press@me.sh`. Not sent. No form |
| `/notion` | Shared chrome plus page CTAs into the sign-in wall |
| `/x` | Shared chrome. Page about X |
| `/apple-vision-pro` | Store link (external, not walked) |
| `/serendipity` | Shared chrome. Milestone page |
| `/next` | Automattic partnership page. Shared chrome |
| `/acknowledgements` | Shared chrome. Credits page |
| `/atlas` | People search field (not filled, not submitted). Sign in and Get started to the wall. About to `/about` |
| `/directory` | A long list of `/profile/<id>` links. Public profiles. Crawl hit HTTP 429 and stopped. Tag pages under `/directory/tags/<tag>` were linked and not each opened |
| `/login` | 404. Shared chrome. Sign in in the header still goes to the wall |

## Sign-in wall

See [login-review.json](login-review.json). `https://app.me.sh/login` and `https://app.me.sh/login?signin` render the same sign-in form. Create account switches the copy to a sign-up form on the same URL. Neither form was submitted. Apple, Google, and SSO were not clicked.

SSO href, not followed: `https://accounts.me.sh/sign-in`. A direct load of that URL shows an email field and a Continue button. Not filled. Not submitted.

## Not in this tree

Signed-in app screens. They sit behind the wall. Profile pages after the 429. Library docs behind the browser check. The press kit on Notion.
