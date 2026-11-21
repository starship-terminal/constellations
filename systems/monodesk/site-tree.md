# MonoDesk public site tree

Mapped on 2026-11-21 from the live public site in headless Chromium before any
package screenshot. Start: `https://www.monodesk.com/` (HTTP 200, title
"MonoDesk: All-in-One Workspace for Freelance Creatives"). Official index:
`https://www.monodesk.com/llms.txt` and `https://www.monodesk.com/sitemap-pages.xml`
(105 URLs). Playground index: `https://www.monodesk.com/playground/sitemap.xml`.

Login walls, recorded and not entered:

| Control | URL | What the page asks | Stop |
|---|---|---|---|
| Header and footer "Log in" | `https://app.monodesk.com/login` | Email and password, or Google | Yes. Do not type. |
| Pricing "Get started", "Create account" | `https://app.monodesk.com/create` | Account creation | Yes. Do not fill. |
| `https://www.monodesk.com/signin` | 404 | Nothing | Dead URL, not a form |
| Footer "support@…" mailto | `mailto:` | Mail client | Not followed. Address is not written into the package |

External, not followed: `https://envato.com/`, `https://www.envato.com/privacy/`,
`https://x.com/_MonoDesk`, `https://www.instagram.com/_monodesk`,
`https://www.youtube.com/@MonoDeskHQ`.

One painted theme on the marketing shell: dark page (`rgb(33, 33, 33)`), light
type (`rgb(231, 231, 231)`), font Geist. Help's body background reads
`rgb(28, 100, 245)` (brand blue). No `data-theme` switch. Tokens live on
`:root` in `/_astro/HeroHeader4.*.css` (`--brand-*`, `--spacing-*`, `--radius-*`).

## Header (desktop 1440)

| Control | Opens |
|---|---|
| Logo | `/` |
| "by" / Envato mark | `https://envato.com/` (external; stop) |
| Creative Pros (`a.header-nav-link`) | Hover or click opens `.header-nav-dropdown-menu.mega-menu`. Parent link goes to `/for-creative-pros`. Items: Graphic Designers, Website Creators, Video Creators, Solo Freelancers, Small Teams. |
| Features (`a.header-nav-link`) | Hover or click opens the same mega-menu class. Parent link goes to `/features`. Groups: Today, Co-Worker, Win work (Leads, Research, Meetings, Proposals), Deliver (Projects, Planner, Time Tracking, Teams), Get paid (Invoices), Relationships (Clients, Client portals, Client updates), Integrations (Zapier, MCP). |
| Pricing | `/pricing` |
| About | `/about-us` |
| More (`a.header-nav-link`, `href="#"`) | Hover or click opens a small dropdown, not a page. Items: Help `/help`, Blog `/blog`, Playground `/playground`. Compare `/alternatives` is in the footer, not in this dropdown. |
| Log in | Login wall |
| Get started free | `/pricing#pricing` (public pricing anchor, not the app) |

## Header (phone 390)

| Control | Opens |
|---|---|
| Toggle menu (`button.hamburger-btn`, aria-label "Toggle menu") | Opens `nav.mobile-nav.is-open`, a fixed full-viewport sheet. The list scrolls inside `.mobile-nav-content` (overflow auto). Close is the X in the header. |
| Watch the video (`button.hv4-watch-btn`) | Same video dialog as "Watch how it works" |
| Dismiss (`button.desktop-link__dismiss`) | Closes the "open on desktop" prompt. Local hide only. |
| Email me the link (`button.desktop-link__button`) | A field that would send a link. Not filled, not submitted. Recorded as a boundary. |

Mobile menu links (after Toggle menu, then More): logo, Envato, Get started
free (`/pricing#pricing`), Creative Pros and its five role pages, Features and
the feature pages below, Pricing, About, More (expands Help, Blog, Playground),
Log in (wall), socials (external).

## Home interactions (stay on `/`)

| Control | Opens |
|---|---|
| Play from start / Pause video | Hero video playback. No navigation. |
| Watch how it works (`button.video-modal-trigger`) | Video dialog. Close: "Close video" (`button.video-modal-close`) or Escape. |
| Pillar "Business development — Win the work" (expanded by default) | In-page panel. Links: Lead pipeline `/features/leads`, Client researcher `/features/research`, Meeting assistant `/features/meetings`, Proposal generator `/features/proposals`. |
| Pillar "Project management — Run the work" | In-page panel. Links: `/features/projects` ("Import where you're at"), Time tracking `/features/time`, Team collaboration `/features/teams`. |
| Pillar "Client management — Wow the client" | In-page panel. Links: Client directory `/features/clients`, Client portal `/features/client-portal`, Invoicing `/features/invoices`. |
| Show quote 1 / 2 / 3 (`button.sp-dot`) | Testimonial carousel. Stays on `/`. |
| FAQ buttons (`.faq-question`) | Accordion answers on the same page: "What is MonoDesk?", "Who is MonoDesk built for?", "How is MonoDesk different…?", "How do I provide feedback…?". |
| Play video / 0:39 | Embedded "Intelligently Connected Workspace" video. Playback only. |

## Home links to other public pages

| Control | Page |
|---|---|
| See proposals | `/features/proposals` |
| Teams / Freelancers | `/for-creative-pros/small-teams`, `/for-creative-pros/freelancers` |
| Explore | `/features` |
| See how | `/features/agent` |
| Today | `/features/today` |
| Graphic Designers card | `/for-creative-pros/graphic-designers` |
| Website Creators card | `/for-creative-pros/website-creators` |
| Video Creators card | `/for-creative-pros/video-creators` |
| Footer Blog, Help, Compare, Terms | `/blog`, `/help`, `/alternatives`, `/terms` |
| Footer Privacy Policy | Envato privacy (external; stop) |
| Footer socials | External; stop |

## Features hub `/features`

Same header and footer. Feature cards link to the feature pages in the sitemap
group below. Log in is the wall. No form.

## Feature pages (same shell)

Each is a public marketing page. Header Log in is the wall. No account form.

- `/features/agent` Co-Worker
- `/features/client-portal`
- `/features/client-updates`
- `/features/clients`
- `/features/discover` (redirect/notice that Discover moved)
- `/features/invoices`
- `/features/leads`
- `/features/mcp`
- `/features/meetings`
- `/features/planner`
- `/features/projects`
- `/features/proposals`
- `/features/research`
- `/features/teams`
- `/features/time`
- `/features/today`
- `/features/zapier`

## Audiences

- `/for-creative-pros` hub
- `/for-creative-pros/freelancers`
- `/for-creative-pros/graphic-designers`
- `/for-creative-pros/small-teams`
- `/for-creative-pros/video-creators`
- `/for-creative-pros/website-creators`

## Pricing `/pricing`

| Control | Opens |
|---|---|
| See full feature set (`button.ptable-toggle`, aria-expanded) | Expands the comparison table on the same page |
| FAQ `.faq-question` | Accordion on the same page (free during beta, seats, storage, data) |
| Get started / Create account | `https://app.monodesk.com/create` (wall; stop) |
| Log in | wall |
| See how MonoDesk compares | `/alternatives` |
| terms of service | `/terms` |

## About, campaign, legal

- `/about-us` team and mission. Same shell. Log in is the wall.
- `/admin-sorted` campaign page. "Get started free" goes to `https://app.monodesk.com/create` (wall). Log in is the wall.
- `/terms` terms of service. Same shell.

## Compare

- `/alternatives` hub, cards to the comparison pages
- `/alternatives/asana`, `/basecamp`, `/bonsai`, `/clickup`, `/dubsado`, `/honeybook`, `/manyrequests`, `/moxie`, `/notion`, `/todoist`, `/trello`

## Blog

- `/blog` index of posts
- Posts: `/blog/client-portal`, `/blog/clients-and-projects`, `/blog/how-the-ai-agent-works`, `/blog/how-to-organise-creative-projects`, `/blog/kickoff-email-template`, `/blog/meet-your-co-worker`, `/blog/monodesk-is-in-beta`, `/blog/scope-creep`, `/blog/teams-collaboration-without-the-noise`, `/blog/the-planner`

## Help

| Control | Opens |
|---|---|
| Search help articles (`input[type=search]`) | In-page filter. Typed text is not submitted. |
| Category cards | The category indexes below |
| Article links | Article pages. Markdown twins exist at the same path plus `.md` (not a separate UI). |

Category indexes: `/help/getting-started`, `/help/planner-today`, `/help/projects-tasks`, `/help/clients`, `/help/client-portal`, `/help/discover-leads`, `/help/co-worker`, `/help/proposals-invoices`, `/help/time-tracking`, `/help/teams-account`, `/help/integrations`, `/help/videos`.

Articles (public, no login): the rest of the `help` group in
`sitemap-pages.xml` (53 help URLs including the hub and categories). Examples:
`/help/getting-started/what-is-monodesk`, `/help/clients/client-profiles`,
`/help/time-tracking/track-your-time`.

## Playground `/playground`

Separate layout (`PlaygroundLayout` CSS, Tailwind variables, "Geist Variable").
Nav button "Playground" (`button.pg-nav-btn`, aria-expanded) opens the
playground menu on the same origin. Cards link to tools. Some tools ask for an
image, a name, a location, or a quote. Those fields are not filled and no
generator is submitted.

Index cards:

| Card | Page |
|---|---|
| 24x24 | `/playground/24x24` |
| Aesthetic deconstructor | `/playground/aesthetic-deconstructor` |
| AI video studio | `/playground/ai-video-studio` |
| Captions | `/playground/captions` |
| Cast | `/playground/cast` |
| Focal guessr | `/playground/focal-guessr` |
| Invoice generator | `/playground/invoice-generator` |
| Level up | `/playground/level-up` |
| Magic 8 | `/playground/magic8` |
| Palette guessr | `/playground/palette-guessr` |
| Prompt library | `/playground/prompt-library` |
| Quote generator | `/playground/quote-generator` |
| Thumbnail maker | `/playground/thumbnail-maker` |
| What to charge | `/playground/what-to-charge` |

Also in the playground sitemap, not all linked as cards from the index:
`/playground/24x24/library`, `/requests`, `/studio`, `/vote`;
`/playground/given-name`, `/playground/namesake`; invoice and quote
trade variants (`cleaning-invoice`, `electrician-invoice`,
`free-invoice-generator`, `freelance-invoice-maker`,
`graphic-design-invoice`, `invoice-template`, `logo-brand-invoice`,
`photography-invoice`, `plumber-invoice`, `website-design-invoice`, and the
matching `quote-generator/*` pages); `what-to-charge` craft pages
(`3d-modeling`, `app-dev`, `audio-production`, `copywriting`,
`freelance-rate-calculator`, and the rest of that sitemap group).

What-to-charge asks for a location. That field is not filled. Invoice and
quote generators ask for client details. Those fields are not filled.

## Not a public page

`https://app.monodesk.com/` returned HTTP 200 to a header probe and is the
signed-in app. It is not opened. Refero lists `/create` and
`/welcome-dashboard` on that host; both are behind the account wall.
