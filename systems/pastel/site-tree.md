# Pastel public site tree

Mapped from https://usepastel.com/ on 2026-11-20 in headless Chromium before any package screenshots. The homepage returned HTTP 200. The tree below is what a signed-out visitor can open. Login, signup, dashboard, and any control that asks for an email, a password, a name, or SSO were recorded and not entered. No form was submitted. No email, phone, or location is written here.

Pastel paints three public shells. They are not a theme switch.

| Shell | Where | What opens it |
|---|---|---|
| Marketing (Webflow) | `/`, `/features`, `/plans`, `/agents`, `/faq`, `/terms`, `/privacy`, `/markup-alternative` | Header links on the homepage |
| Blog (Webflow, own nav) | `/blog`, `/reviews`, `/sitemap`, most tool and SEO pages, `blog.usepastel.com` (redirects to `web.usepastel.com/blog`) | Header Blog, footer Our blog |
| App marketing (Tailwind) | `/customers`, `/teams`, `/about`, `/how-it-works`, `/website-revisions`, `/trackduck-alternative`, `/customers/<slug>` | Footer Customers, For teams, Our story. `/case-studies` redirects here |

A fourth surface, the annotation canvas, is behind login. `/home` redirects to `/login`.

## Homepage controls

Desktop header (visible links, no hamburger):

| Control | Opens |
|---|---|
| Announcement bar "See how it works" | `/agents` |
| Logo | `/` |
| Features | `/features` |
| Case Studies | `/case-studies`, which redirects to `/customers` |
| Blog | `https://blog.usepastel.com/` which redirects to `https://web.usepastel.com/blog` |
| Pricing | `/plans` |
| Login | `/login` (email, password, and SSO). Stop. |
| Sign up | `/signup` (name, email, password). Stop. |
| Start a free trial, Get started now | `/signup`. Stop. |
| Watch demo, Play demo | `/#demo-video` (YouTube embed `VIZXLI2LMlI` already on the page). Not played. |
| On Purpose Projects quote link | `https://onpurposeprojects.com/` (external). Not followed. |
| Open Intercom Messenger | Third-party chat launcher. Not opened. |

Phone (390) adds `.nav-menu-button`. It opens the same header links in a menu: Features, Case Studies, Blog, Pricing, Login, Sign up.

Footer, same on the marketing pages:

| Control | Opens |
|---|---|
| Pricing | `/plans` |
| Product features | `/features` |
| For teams | `/teams` |
| Customers | `/customers` |
| Help center | `http://help.usepastel.com/en/` |
| Our story | `/about` |
| Status | `https://status.usepastel.com/` |
| Terms of use | `/terms` |
| Privacy Policy | `/privacy` |
| Sitemap | `/sitemap` |
| Our blog | `/blog` |
| Web annotation tool | `/website-annotation-tool` |
| PDF annotation tool | `/pdf-annotation-tool` |
| Email annotation tool | `/email` |
| Broken link checker | `/broken-link-checker` |
| Hourly rate calculator | `/hourly-rate-calculator` |
| Responsive website test | `/responsive-website-test` |
| Box shadow generator | `/box-shadow-generator` |
| Compare pixels | `/compare-pixels` |

The HTML sitemap has a mailto link. That address is not copied into this package.

## Marketing pages

| Page | URL | Interaction |
|---|---|---|
| Home | `/` | File-type carousel (Splide, 5 slides: live Webflow, wireframes, Shopify, branding, moodboard). No submit. |
| Features | `/features` | Same header and footer. |
| Agents | `/agents` | Same header. CTAs go to `/signup`. Stop. |
| Pricing | `/plans` | Monthly / Annual toggle (`.toggle-text.monthly`, `.toggle-text.annual`, `.toggle-switch`). Local UI only. Plan CTAs go to `/signup`. Stop. |
| FAQ | `/faq` | `.faq-accordion-question` expands the answer in place. No form. |
| Markup alternative | `/markup-alternative` | Same marketing shell. `marketing.usepastel.com/markup-alternative` is the same page on another host. |
| Terms | `/terms` | Long legal page. |
| Privacy | `/privacy` | Long legal page. |

## Blog shell

Desktop nav is a row of links. Phone uses `.menu-mob.w-nav-button` (aria-label `menu`).

| Control | Opens |
|---|---|
| home | `/` |
| Features | `/features` |
| Pricing | `/plans` |
| Customers | `/customers` |
| Reviews | `/reviews` |
| Blog | `/blog` |
| Log in | `/login`. Stop. |
| Sign Up | `/signup`. Stop. |
| A post card | `/blog/<slug>` |
| A tag | `/blog-tag/<tag>` |
| menu (phone) | The same nav links, overlaid |

Declared CSS custom properties on this shell: `--black`, `--midnight-blue`, `--royal-blue`, `--light-slate-grey`, `--alice-blue`, `--white`, `--medium-slate-blue`, `--ghost-white`, and six more.

## App-marketing shell

Header links: Features `/features`, How it works `/#how-it-works`, Pricing `/plans`, Reviews `/reviews`, Customers `/customers`, Blog `https://usepastel.com/blog`, Log in `/login` (stop), Sign up free `/signup` (stop).

A footer email field (`name=email`, placeholder "Enter your email address") sits far down the page. It was not typed into and not submitted. A `close` button exists in the DOM at 0x0 and was not clicked.

| Page | Notes |
|---|---|
| `/customers` | Index. Each "Read more" opens `/customers/<slug>`. |
| `/customers/calendly`, `/customers/fountain-digital`, `/customers/lemonly`, `/customers/north-designs`, `/customers/bentobox`, `/customers/freshysites`, `/customers/studio-almond`, `/customers/guru-hotel`, `/customers/revamp`, `/customers/pbj`, `/customers/ada`, `/customers/the-couch-digital-studio`, `/customers/crisp-digital` | Story pages. `/case-studies/<slug>` redirects to the matching customer page. |
| `/teams`, `/about`, `/how-it-works` | Same shell. CTAs go to `/signup`. Stop. |
| `/website-revisions`, `/trackduck-alternative` | Same shell, no email field on the first screen. |

## Tools (blog shell, plus a form that was not submitted)

| Page | Control | What it would do | Captured as |
|---|---|---|---|
| `/broken-link-checker` | URL field, "Check for broken links" | Submits a URL | Field and button visible. Not typed, not submitted. |
| `/responsive-website-test` | URL field, "Preview website" | Loads a third-party site in a preview | Not typed, not submitted. |
| `/hourly-rate-calculator` | Currency inputs, NEXT | Multi-step calculator | Resting step one only. Not filled. |
| `/box-shadow-generator` | Preset shadows, Share, Post | Share and Post leave the page (social). Not clicked. |
| `/compare-pixels` | File input, website URL field | Upload and fetch. Not used. |
| `/on` | "Enter a website URL" | Demo loader. Not typed. |
| `/on-any-website` | "Go to usepastel.com", "Get started" | Home, or `/signup`. Stop on the latter. |

Share and Post buttons on the tool pages were not clicked.

## SEO and feature landing pages (blog shell)

`/website-annotation-tool`, `/pdf-annotation-tool`, `/email`, `/design-reviews`, `/website-qa-testing`, `/client-project-approval`, `/copy-changes`, `/adobe-xd` (previous/next slide controls), `/marker-illustrations`, `/bugherd-alternative`.

`/adobe-xd` has previous slide, next slide, and "Show slide 1 of 1". Those are local carousel controls.

## Blog index, tags, and posts

`/blog` lists posts. Sitemap tags: `/blog-tag/best-practices`, `/blog-tag/building-pastel`, `/blog-tag/design-development`, `/blog-tag/entrepreneurship`, `/blog-tag/interviews`, `/blog-tag/product-features`, `/blog-tag/resources`.

The XML sitemap lists 42 `/blog/<slug>` posts (approvals, website-feedback, introducing-revisions, and the rest). One post (`/blog/approvals`) and one tag (`/blog-tag/product-features`) were opened to confirm the template. The other posts use that same template. They are listed in the sitemap, not each captured as a unique screen.

## Help center

`https://help.usepastel.com/en/` (Intercom help). Search field `name=q` was not typed into.

| Collection | Opens |
|---|---|
| Using Pastel | `/en/collections/1169706-using-pastel` |
| Account Settings, Plans & Privacy | `/en/collections/1169715-account-settings-plans-privacy` (account articles; not entered past the collection index if it asks for a login) |
| Integrations | `/en/collections/1169728-integrations` |
| Pastel for AI Agents | `/en/collections/19717381-pastel-for-ai-agents` |
| Frequently Asked Questions | `/en/collections/1959818-frequently-asked-questions` |

## Status

`https://status.usepastel.com/` (Instatus). Public. "Get updates" expands subscribe links: Email, Slack, Microsoft Teams, Google Chat, Webhook, RSS, Atom. Those subscribe pages ask for a contact and were not opened. "Report an issue" is a mailto. Uptime graph buttons ("Read uptime graph for ...") expand a graph in place. A dark-mode control is in the DOM. The first probe did not find a visible "Dark mode" button to click, so a live dark theme was not confirmed.

## Walls (recorded, then stopped)

| URL | What it asks for |
|---|---|
| `https://usepastel.com/login` | Email and password. SSO buttons are on the page. Not clicked. |
| `https://usepastel.com/signup` | Name, email, password. Not filled. |
| `https://usepastel.com/home` | Redirects to `/login`. |
| Any "Start a free trial", "Get started", "Sign up free", "Log in" | The wall above. |

The annotation canvas, projects, comments, billing, and team settings are behind that wall. They are not in this package.

## External, not captured as Pastel UI

Facebook, X, and LinkedIn icons in the blog footer. YouTube demo embed (present, not played). Intercom launcher (present, not opened). `onpurposeprojects.com`.
