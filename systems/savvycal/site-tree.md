# SavvyCal public site tree

Mapped from https://savvycal.com/ on 2026-11-21 in headless Chromium before screenshots. The homepage loaded (HTTP 200, title "Scheduling Software Everyone Will Love · SavvyCal"). The published sitemap at https://savvycal.com/sitemap.xml lists 119 URLs. Link harvest from the homepage and a crawl of the first 80 same-host pages confirmed the control map below.

Official product: SavvyCal scheduling software, domain savvycal.com. No theme switch on the marketing pages. Body class is `bg-brand-oatmeal`. Login and signup CSS includes unused `dark:` variants; those pages do not expose a theme control.

## Shell

Desktop header (1440): logo "SavvyCal home" opens `/`. Text links Features (`/features`), Pricing (`/pricing`), What's New (`https://feedback.savvycal.com/updates`, other host, recorded, not crawled). Log in opens `/login` (wall). Sign up opens `/signup` (wall). No desktop dropdown, dialog, or hamburger.

Phone header (390): the same logo. A button labelled "Open main menu" (`aria-expanded=false`) opens an in-page menu. That menu holds the same destinations as the desktop header plus the footer groups. Closing it returns to the page. No other phone dialog.

Footer (every marketing page), groups and the control that opens each destination:

| Group | Control | Opens |
|---|---|---|
| Product | Features | `/features` |
| Product | Pricing | `/pricing` |
| Product | Integrations | `/integrations-directory` |
| Product | Google Calendar | `/google-calendar-scheduling-tool` |
| Product | Outlook | `/outlook-scheduling-tool` |
| Product | iCloud | `/icloud` |
| Product | All your calendars | `/calendar-scheduler` |
| Product | Chrome extension | `/chrome-extension` |
| Product | AI assistants | `/ai` |
| Product | Availability | `/features/availability` |
| Product | Teams | `/for-teams` |
| Product | Round robin | `/features/round-robin-scheduling` |
| Product | Meeting polls | `/meeting-polls` |
| Product | Workflows | `/features/workflows` |
| Product | Payments | `/stripe` |
| Product | Branding and embeds | `/features/branding` |
| Product | Delegated access | `/features/delegation` |
| Solutions | Sales | `/solutions/sales` |
| Solutions | Marketing | `/solutions/marketing` |
| Solutions | Recruiting | `/solutions/recruiting` |
| Solutions | Customer success | `/solutions/customer-success` |
| Solutions | Education | `/solutions/education` |
| Solutions | Consulting | `/solutions/consulting` |
| Solutions | Podcasting | `/solutions/podcasting` |
| Compare | Calendly vs SavvyCal | `/calendly-vs-savvycal` |
| Compare | Cal.com alternative | `/cal-alternative` |
| Compare | Acuity alternative | `/acuity-alternative` |
| Compare | Doodle alternative | `/doodle-alternative` |
| Compare | Microsoft Bookings alternative | `/microsoft-bookings-alternative` |
| Compare | HubSpot Scheduling alternative | `/hubspot-scheduling-alternative` |
| Compare | Chili Piper alternative | `/chili-piper-alternative` |
| Compare | YouCanBook.me alternative | `/youcanbookme-alternative` |
| Compare | TidyCal alternative | `/tidycal-alternative` |
| Compare | Outlook scheduling tools | `/outlook-scheduling-tools-compared` |
| Compare | Round robin tools | `/round-robin-scheduling-tools-compared` |
| Compare | iCloud scheduling tools | `/icloud-scheduling-tools-compared` |
| Compare | Acuity alternatives | `/acuity-scheduling-alternatives` |
| Compare | Calendly alternatives | `/calendly-alternatives` |
| Learn | Articles | `/articles` |
| Learn | Scheduling link etiquette | `/scheduling-link-etiquette` |
| Learn | Help docs | `https://docs.savvycal.com/` (other host) |
| Learn | Developers | `https://docs.savvycal.com/developers` (other host) |
| Company | About us | `/company` |
| Company | Security | `/security` |
| Company | Status | `https://savvycal.instatus.com/` (other host) |
| Legal | Privacy | `/privacy` |
| Legal | Terms | `/terms` |
| Legal | Cookies | `/cookie-policy` |
| Legal | DPA | `/dpa` |
| Product badge | SavvyCal Appointments | `https://savvycal.app/` (other host) |

"Drop us a line" is a mailto link in the footer. Recorded. Not opened. The address is not stored in this package.

## Homepage `/`

Hero "The fresh way to find a time to meet."

| Control | Opens |
|---|---|
| Try SavvyCal risk-free | `/signup` wall. Stop. |
| See plans & pricing | `/pricing` |
| feel confident sending a SavvyCal link | `/scheduling-link-etiquette` |
| See a live booking page | `/demo` (public booking calendar, not a login) |
| Calendar overlay card | `/features/calendar-overlay` |
| Custom domains card | `https://docs.savvycal.com/custom-domains` (other host) |
| More ways to protect your time | `/features/availability` |
| Learn about paid bookings | `/stripe` |
| Learn about workflows | `/features/workflows` |
| SavvyCal for teams | `/for-teams` |
| Round robin card | `/features/round-robin-scheduling` |
| Collective card | `https://docs.savvycal.com/collective-scheduling-links` (other host) |
| Group card | `https://docs.savvycal.com/group-scheduling-mode` (other host) |
| Connect your assistant | `/ai` |
| Integration logos (unnamed anchors) | `/integrations-directory`, `/outlook-scheduling-tool#microsoft-teams` |
| Get started free | `/signup` wall. Stop. |
| FAQ summaries (details, closed) | In-page disclosure, not a new URL. Five items: free trial, company billing, ways to save, calendars and video tools, cancel. |

No cookie dialog, no theme control, no search field.

## Pricing `/pricing`

| Control | Opens |
|---|---|
| Monthly | In-page billing state. Prices switch. No navigation. |
| Annual (2 months free) | In-page billing state. Default on load. |
| Plan CTAs (Get started / similar) | `/signup` wall. Stop. |
| FAQ summaries | In-page disclosure. Eleven items (free plan, trial, guest account, paid seat, mixed seats, annual savings, discounts, Basic vs Premium, volume pricing, refund, cancel). |

## Features index `/features`

Cards and text links open the feature pages in the sitemap: availability, calendar overlay, branding, delegation, round robin, workflows. Also links out to docs and to `/signup`. No buttons, no FAQ, no dialog.

## Live booking demo `/demo`

Public page titled Demo, heading "Design Sync". A sample scheduling link, not a signed-in app.

| Control | Opens |
|---|---|
| Go to the Previous Month / Next Month | In-page month change. |
| Day numbers | In-page time-slot list for that day. |
| A time slot | In-page confirm step (duration, time). Does not submit a booking. |
| Confirm / continue into a guest form | Recorded as a wall-adjacent form. Not filled. Not submitted. |

No email, password, or OAuth control on the calendar itself.

## Integrations `/integrations-directory`

| Control | Opens |
|---|---|
| Search field ("Search integrations") | Filters the directory in place. Not submitted. |
| Category pills (All, Analytics, Automation, Calendar, Conferencing, CRM, Email, Payments, Podcasting, Productivity, Website) | In-page filter. |
| An integration card | That integration's public detail URL on savvycal.com when the card is a same-host link. External partner docs stay recorded, not crawled. |

## AI `/ai`

| Control | Opens |
|---|---|
| Copy | Copies a prompt to the clipboard. No navigation. |
| Claude / ChatGPT / Other assistants | In-page tab of the same prompt. |
| FAQ summaries | In-page disclosure (nine items). |
| Connect / sign-up links | `/signup` wall. Stop. |

## Article index and articles

`/articles` lists article cards. Each card opens `/articles/<slug>`. The sitemap lists 65 article URLs. An article page is the same marketing shell plus the article body. No form, no dialog. Footer and header behave as on the homepage.

## Other marketing pages (same shell)

Each of these is a long marketing page: header, hero, feature sections, a FAQ of `details`/`summary` (except where noted), footer. CTAs labelled get started, try, or sign up open `/signup` and stop. "Log in" opens `/login` and stops.

Sitemap product and solution pages: `/for-teams`, `/company`, `/brand`, `/meeting-polls`, `/scheduling-link-etiquette`, `/stripe`, `/chrome-extension`, `/open-source`, `/meeting-scheduler`, `/calendar-scheduler`, `/google-calendar-scheduling-tool`, `/outlook-scheduling-tool`, `/icloud`, `/security`, `/ssdlc`, `/time-zone-api`, `/features/availability`, `/features/calendar-overlay`, `/features/branding`, `/features/delegation`, `/features/round-robin-scheduling`, `/features/workflows`, `/solutions/sales`, `/solutions/marketing`, `/solutions/recruiting`, `/solutions/customer-success`, `/solutions/education`, `/solutions/consulting`, `/solutions/podcasting`.

Sitemap comparison pages: `/calendly-vs-savvycal`, `/calendly-alternatives`, `/youcanbookme-alternative`, `/cal-alternative`, `/acuity-alternative`, `/acuity-scheduling-alternatives`, `/doodle-alternative`, `/microsoft-bookings-alternative`, `/chili-piper-alternative`, `/hubspot-scheduling-alternative`, `/tidycal-alternative`, `/round-robin-scheduling-tools-compared`, `/outlook-scheduling-tools-compared`, `/icloud-scheduling-tools-compared`.

Legal: `/cookie-policy`, `/data-processors`, `/dpa`, `/eula`, `/privacy`, `/terms`. No interactive controls beyond the shell.

`/feed.xml` is an RSS document, not a page.

## Walls (recorded, branch stopped)

| URL | What it shows | Not done |
|---|---|---|
| https://savvycal.com/login | Heading "Welcome back". Email field, password field, Sign In. Buttons: Sign in with Google, Sign in with Microsoft, Sign in with Fastmail. Link: Sign up. | Password not typed. Sign In not clicked. Google, Microsoft, Fastmail not clicked. |
| https://savvycal.com/signup | Heading "SavvyCal". Name, email, password fields. hCaptcha iframe present. Buttons: Sign up with Google, Sign up with Microsoft, Sign up with Fastmail, Sign Up. | No field filled. Captcha not solved. OAuth not clicked. Form not submitted. |

Any "Get started", "Try SavvyCal", or plan CTA on a marketing page opens `/signup`. That branch stops.

## Other hosts (recorded from the homepage, not captured as this package)

| Host | How it is reached |
|---|---|
| feedback.savvycal.com | Header "What's New" |
| docs.savvycal.com | Footer Help docs and Developers; homepage custom-domain, collective, and group cards |
| savvycal.instatus.com | Footer Status |
| savvycal.app | Footer "SavvyCal Appointments" |
| chrome.google.com | Chrome extension store link from `/chrome-extension` |

## States to capture

Desktop 1440x900 and phone 390x844, light only (the only painted theme):

- Default and full page: home, features, pricing, demo, integrations, articles, one feature page, one solution page, one comparison page, company, security, legal (privacy), login wall, signup wall.
- Interactions that stay on the page: pricing Monthly toggle, one FAQ open, integrations search focused and one category selected, demo next-month and one day selected, AI assistant tab, phone menu open.
- Login and signup: the wall as it loads. No typed password, no OAuth click, no submit.
