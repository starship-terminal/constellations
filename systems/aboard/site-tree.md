# Aboard public site tree

Mapped on 2026-11-21 from [https://aboard.com/](https://aboard.com/) with Playwright (headless Chromium, 1440×900, then 390×844 for the menu). The homepage returned 200 and the title "AI Transformation Consulting & Custom Software | Aboard". No sign-in link and no account form exist on aboard.com. WordPress sitemaps (`/sitemap.xml`, `/sitemap_index.xml`, `/wp-sitemap.xml`) return 200 and zero `<loc>` entries, so the tree below is the link graph walked from the homepage, not a sitemap.

Nothing in this map was submitted. CookieYes Accept, Customize, and Save My Preferences were not clicked. Newsletter, event, and contact fields were not filled.

## Shell (every public page)

| Control | Opens |
|---|---|
| Wordmark "Aboard — home" | [https://aboard.com/](https://aboard.com/) |
| Skip to content | same page `#main` |
| How We Work | [https://aboard.com/how-we-work/](https://aboard.com/how-we-work/) |
| Case Studies | [https://aboard.com/case-studies/](https://aboard.com/case-studies/) |
| Foundry | [https://aboard.com/foundry/](https://aboard.com/foundry/) |
| Perspectives (desktop nav) | [https://aboard.com/perspectives/](https://aboard.com/perspectives/) |
| Get in Touch | same page `#contact` (contact iframe, not a new route) |
| Footer Perspectives column: Newsletter, Podcast, Events, Media, Whitepaper | the feed and whitepaper pages below |
| Footer About column: About Us, FAQ, Careers, Security | the pages below |
| Footer socials | external: LinkedIn (New York), LinkedIn (Lebanon), YouTube, Instagram, Facebook, X. Recorded, not followed |
| Hover Perspectives | menu: Newsletter, Podcast, Events, Media, Whitepaper. Each is a page, listed under Feeds and Whitepaper |
| Hover About | menu: About (`/about/`), FAQ, Careers |

Desktop nav shows How We Work, Case Studies, Foundry, Perspectives, About, and Get in Touch. Hovering Perspectives opens a menu: Newsletter, Podcast, Events, Media, Whitepaper. Hovering About opens a menu: About, FAQ, Careers. The other nav links have no menu. The same children are in the footer and in the phone menu. The first hover pass missed these menus because it hovered every header link, including ones that are only visible inside a closed menu.

## Phone menu (390)

The trigger is `.rd-nav-toggle` (`aria-label` "Open menu", `aria-expanded` false until opened). It is not visible at 1440. Opening it sets `aria-expanded` true and shows the same destinations as the footer column, plus Get in Touch (`#contact`). Escape closes it. No login item appears.

## Overlays

| Control | Opens | Stop |
|---|---|---|
| CookieYes banner (fixed bottom, role region) | text plus Customize and Accept All | banner is visible on first load. Not answered |
| Customize (`aria-haspopup="dialog"`) | `#ckyPreferenceCenter` (CookieYes preferences dialog: Necessary, Functional, Analytics, Performance, Advertisement, Uncategorized accordions, Save My Preferences, Accept All, Close) | dialog is in the DOM on load, hidden until Customize. Not opened, not saved |
| Accept All | would POST consent | not clicked |

## Home

| Control | Opens |
|---|---|
| Carousel ticks "Show case study N of 6" | in-page slide (tick 3 sets `is-on` on the third tick). Not a navigation |
| Pause case studies | toggles the control to "Play case studies". Local only |
| Previous / Next case study | previous and next slide. Local only |
| Feed chips All, Newsletter, Podcast, Events, In Media | filter the home feed in place. URL stays [https://aboard.com/](https://aboard.com/) |
| A feed row | the article, episode, event, or media item that row names |
| View all case studies | [https://aboard.com/case-studies/](https://aboard.com/case-studies/) |
| Get in Touch | `#contact`. The section heading is "We Can Help". The form is the same-origin iframe `https://aboard.com/contact-form/?iframe=contactForm` |

The hero carousel is a marketing animation (insurance-demo frames), not a product app.

## Marketing pages

| Page | Extra controls |
|---|---|
| [https://aboard.com/how-we-work/](https://aboard.com/how-we-work/) | shell only, plus `#contact` |
| [https://aboard.com/about/](https://aboard.com/about/) | shell only, plus `#contact` |
| [https://aboard.com/careers/](https://aboard.com/careers/) | "See open positions" scrolls to `#open-positions` on the same page. Job rows leave aboard.com for `jobs.polymer.co`. Recorded, not followed. No application form on this host |
| [https://aboard.com/security/](https://aboard.com/security/) | shell only. `/.well-known/security.txt` is linked from the security copy |
| [https://aboard.com/faq/](https://aboard.com/faq/) | category anchors `#faq-company`, `#faq-ai-services`, `#faq-software-delivery`, `#faq-in-practice`, `#faq-working-with-us`, `#faq-investment`, `#faq-knowledge-community`, `#faq-more`. Each question is a `.faq-q` button (`aria-expanded` false) that opens its answer panel on the same page |

## Case studies

Index: [https://aboard.com/case-studies/](https://aboard.com/case-studies/). Each card opens one study. Studies found from the homepage and the index:

- [https://aboard.com/case-studies/sagesure-policy-logic-central/](https://aboard.com/case-studies/sagesure-policy-logic-central/)
- [https://aboard.com/case-studies/make-an-impact-partner-health-analytics-platform/](https://aboard.com/case-studies/make-an-impact-partner-health-analytics-platform/)
- [https://aboard.com/case-studies/etwal-elite-travel-planning-platform/](https://aboard.com/case-studies/etwal-elite-travel-planning-platform/)
- [https://aboard.com/case-studies/laphams-quarterly/](https://aboard.com/case-studies/laphams-quarterly/)
- [https://aboard.com/case-studies/probable-futures-environmental-data-mapping-tool/](https://aboard.com/case-studies/probable-futures-environmental-data-mapping-tool/)
- [https://aboard.com/case-studies/city-of-boston-scheduling-app/](https://aboard.com/case-studies/city-of-boston-scheduling-app/)
- [https://aboard.com/case-studies/newyorkbio-life-science-hub/](https://aboard.com/case-studies/newyorkbio-life-science-hub/)
- [https://aboard.com/case-studies/ansatz-machine-learning-product-generator/](https://aboard.com/case-studies/ansatz-machine-learning-product-generator/)
- [https://aboard.com/case-studies/outsell-b2b-data-platform/](https://aboard.com/case-studies/outsell-b2b-data-platform/)
- [https://aboard.com/case-studies/horizon-signals-remote-traffic-signal-controls/](https://aboard.com/case-studies/horizon-signals-remote-traffic-signal-controls/)
- [https://aboard.com/case-studies/evo-internal-hr-time-expenses-platform/](https://aboard.com/case-studies/evo-internal-hr-time-expenses-platform/)

A study page repeats the shell and `#contact`. Share and next/previous controls, where present, are in-page or external social links. No login wall.

## Foundry

[https://aboard.com/foundry/](https://aboard.com/foundry/) holds product-screenshot carousels. "Open image N of M" changes the visible frame. "Show more" expands a gallery on the same page. "Try Aboard Sign today" leaves the marketing host for `http://sign.aboard.com/`. That branch stops there (see Auth wall).

## Feeds

| Page | Extra controls |
|---|---|
| [https://aboard.com/perspectives/](https://aboard.com/perspectives/) | chips All, Newsletter, Podcast, Events, In Media filter the list in place. "Load more" goes to `?pg=2#perspectives-next` (page 3 and 4 exist the same way). A row opens an article |
| [https://aboard.com/newsletter/](https://aboard.com/newsletter/) | two email forms (`#nl-hero-form`, `#nl-band-form`) POST to `/wp-json/aboard/v1/newsletter-signups`. Not filled, not submitted. Pagination `/newsletter/page/N/` (2, 3, and 17 seen) |
| [https://aboard.com/podcast/](https://aboard.com/podcast/) | "Play episode" and row play buttons (`.rd-pd-play`, `.rd-pd-art`) open the in-page player. The player has Play and Close player. RSS leaves for `https://feeds.captivate.fm/aboard/`. Pagination `/podcast/page/N/` (2, 3, and 15 seen). An episode title opens `/podcast/<slug>/` |
| [https://aboard.com/events/](https://aboard.com/events/) | year anchors `#events-2026` and `#events-2025`. An event row opens `#event-<id>` on the same page. "Watch the event" leaves for YouTube. `#evSignup` POSTs to `/wp-json/aboard/v1/event-signups`. Not filled, not submitted |
| [https://aboard.com/media/](https://aboard.com/media/) | "Show more" expands the list on the same page (URL stays `/media/`). A row leaves for the publisher (NYT, TechRadar, and others). Not followed |

Article pages (newsletter posts and perspectives essays) share one template: title, body, share links, related rows, and `#contact`. Examples reached from the homepage: `/welcome-to-the-age-of-receipts/`, `/lets-have-a-mouse-party/`, `/meet-aboard-sign/`, `/the-great-firmware-flowering/`, `/the-web-is-more-than-enough/`, `/introducing-tinylittleoffice-com/`. Further essays, `/tag/<slug>/` archives, and `/author/<slug>/` archives use the same template. One essay and one archive are captured as representatives. The rest are the same shell.

## Whitepaper

[https://aboard.com/resources/how-to-utilize-ai-agents-to-actually-deliver-results/](https://aboard.com/resources/how-to-utilize-ai-agents-to-actually-deliver-results/) is a long article page (footer "Whitepaper"). Same shell and `#contact`. No download gate and no email wall on the page itself.

## Contact iframe

`https://aboard.com/contact-form/?iframe=contactForm` is the `src` of the iframe inside `#contact`. A direct visit to that URL redirects to the newsletter (`https://aboard.com/?iframe=contactForm`), so it is not its own page. The form is captured as the `#contact` section. Fields are not filled and the form is not submitted.

## Auth wall (branch stopped)

| URL | Where it is linked | What happened |
|---|---|---|
| [http://sign.aboard.com/](http://sign.aboard.com/) | Foundry "Try Aboard Sign today"; Meet Aboard Sign article "Aboard Sign" | not opened. Branch stopped |
| [https://sign.aboard.com/log/](https://sign.aboard.com/log/) | Meet Aboard Sign article, "an anonymized public log" | not opened. Branch stopped |

No Google or Apple button, password field, or signup form was found on aboard.com.

## Not a page

External social, press, job-board, and YouTube links are recorded above and not followed. `jobs.polymer.co` is the careers handoff. CookieYes "CookieYes" credit links to cookieyes.com.
