# Appwrite public site tree

Mapped from https://appwrite.io/ on 2026-11-21 in headless Chromium (Playwright) before screenshots. Desktop viewport 1440×900. The marketing document pins `html.dark`. No cookie banner mounted. Nothing was submitted. Sign-in, sign-up, recovery, and OAuth controls were recorded and not used.

External hosts (GitHub, YouTube, Discord, X, LinkedIn, Instagram, store.appwrite.io, arena.appwrite.io, status) are leaves. They were not opened.

## Home header

| Control | Opens |
|---|---|
| Logo | `/` |
| Products (button, `aria-haspopup="dialog"`) | Dialog: product links below |
| Solutions (button, `aria-haspopup="dialog"`) | Dialog: solution links below |
| Pricing | `/pricing` |
| Docs | `/docs` |
| Customers | `/blog/categories/customer-stories` |
| Blog | `/blog` |
| Changelog | `/changelog` |
| GitHub star count | `https://github.com/appwrite/appwrite` (external, not opened) |
| Sign in | `/sign-in` (login wall) |
| Sign up | `/sign-up` (signup wall) |
| Skip to content | `/#main-content` |
| Breaking announcement | `/init` |

### Products dialog

| Control | Opens |
|---|---|
| Auth | `/products/auth` |
| Databases | `/products/databases` |
| PostgreSQL | `/products/postgres` |
| Storage | `/products/storage` |
| Functions | `/products/functions` |
| Messaging | `/products/messaging` |
| Realtime | `/products/realtime` |
| Sites | `/products/sites` |
| Domains | `/domains` |
| Firewall | `/products/firewall` |

### Solutions dialog

| Control | Opens |
|---|---|
| Startups | `/startups` |
| Agencies | `/agencies` |
| Innovation teams | `/innovation-teams` |
| Enterprise | `/enterprise` |

## Phone header (390×844)

| Control | Opens |
|---|---|
| Open website navigation | Left drawer (300×844): Products, Solutions, Pricing, Docs, Customers, Blog, Changelog, GitHub, Close |
| Drawer links | Same destinations as the desktop header |
| QUICK STARTS, PRODUCTS, LEARN, SOLUTIONS, ABOUT, ONE AGAINST ALL | In-page accordions on the home document, not a route |

## Home body (representative)

| Control | Opens |
|---|---|
| Start project, Start building | `/sign-up` (signup wall) |
| View docs | `/docs` |
| View pricing plans | `/pricing` |
| Framework marks (React, Next.js, Vue, and the rest) | `/docs/quick-starts/<framework>` |
| Agent marks (Cursor, Claude Code, Codex, Grok Build, and the rest) | `/docs/tooling/ai/agents/<agent>` |
| Product cards | Matching `/products/*` page |
| Compare links | `/alternative-to/<product>` |
| Read customer story | `/blog/post/customer-stories-*` or `/blog/post/customer-story-*` |
| View full benchmark | `https://arena.appwrite.io/` (external) |

## Footer (shared marketing chrome)

| Control | Opens |
|---|---|
| Product, docs, company, legal columns | The same public routes listed under Pages |
| YouTube (button, `aria-haspopup="dialog"`) | Dialog: youtube.com/@appwrite, @LearnPostgres, @LearnAuth (external, not opened) |
| Discord | `/discord` then `discord.com/invite/appwrite` (external redirect) |
| X, LinkedIn, Instagram, daily.dev, Threads | External profiles (not opened) |
| Status | `https://appwrite.online/` (external) |
| Store | `https://store.appwrite.io/` (external) |
| Terms, Privacy, Cookies | `/terms`, `/privacy`, `/cookies` |

## Pages captured as their own surfaces

Marketing and docs pages that the home, header, menus, or footer reach. Each was opened at desktop 1440×900 and phone 390×844.

| Path | What it is | Local interactions |
|---|---|---|
| `/` | Marketing home | Mobile nav drawer |
| `/pricing` | Plans and FAQ | FAQ accordion (one item opens; first item starts open) |
| `/docs` | Docs home | Search button opens a search dialog. Query typed and cleared, never submitted |
| `/docs/quick-starts/react` | One quick start (docs chrome) | Sidebar links stay inside docs |
| `/blog` | Blog index | Category chips are links, not a form |
| `/blog/categories/tutorials` | One category filter | Same chrome as the index |
| `/changelog` | Changelog index | Entry links |
| `/changelog/entry/2026-11-19` | One changelog entry | Article page |
| `/integrations` | Integration catalog | Search field (typed and cleared, not submitted). Category chip "All categories" is a local filter |
| `/integrations/ai-openai` | One integration detail | Marketing article |
| `/company` | Company | Careers hash `/company#careers` stays on the page |
| `/assets` | Brand assets | Download links are files, not pages |
| `/enterprise` | Enterprise marketing | FAQ accordion. Contact us goes to the login wall |
| `/startups` | Startups program | CTAs to sign-up (wall) |
| `/agencies` | Agencies | Same marketing chrome |
| `/innovation-teams` | Innovation teams | Same marketing chrome |
| `/community` | Community | External contributor links not opened |
| `/education` | Education program | Join goes to `/education/join` |
| `/partners` | Partner form page | Fields present. Not filled. Not submitted |
| `/affiliates` | Affiliates marketing | Account dashboard is behind sign-in |
| `/threads` | Public community threads index | Search field typed and cleared, not submitted |
| `/threads/1566144282123833344` | One public thread | Read only |
| `/init` | Init week campaign | Thin page, no nav chrome |
| `/domains` | Domain search marketing | Search field present. Not submitted |
| `/products/auth` | Product page | Tabs or feature switches if present, local only |
| `/products/databases` | Product page | Same |
| `/products/postgres` | Product page | Same |
| `/products/storage` | Product page | Same |
| `/products/functions` | Product page | Same |
| `/products/messaging` | Product page | Same |
| `/products/realtime` | Product page | Same |
| `/products/sites` | Product page | Same |
| `/products/firewall` | Product page | Same |
| `/alternative-to/firebase` | One comparison page | Same marketing chrome as the other ten comparisons |
| `/terms` | Terms | Long legal page |
| `/privacy` | Privacy | Long legal page |
| `/cookies` | Cookies | Long legal page |
| `/sign-in` | Login wall | Recorded. Not typed. OAuth and passkey not clicked |
| `/sign-up` | Signup wall | Recorded. Not typed. OAuth not clicked |
| `/recovery` | Password recovery | Email field present. Not typed. Not submitted |
| `/education/join` | Education join | "Sign up with GitHub" is an OAuth wall. Not clicked |

## Walls (recorded, branch stopped)

| Control | URL | Stopped because |
|---|---|---|
| Sign in, Login, Contact us on enterprise (`/contact-us` redirects here) | `https://appwrite.io/sign-in` or `https://appwrite.io/sign-in?redirect=%2Fsales` | Email and password, or GitHub, GitLab, Bitbucket, Google, or a passkey |
| Sign up, Start project | `https://appwrite.io/sign-up` | Name, email, password, or GitHub, GitLab, Bitbucket, Google |
| Forgot password | `https://appwrite.io/recovery` | Asks for an email and a submit. Not filled |
| Affiliates dashboard | `https://appwrite.io/sign-in?redirect=%2Faccount%2Faffiliates` | Login wall |
| Sales | `https://appwrite.io/sign-in?redirect=%2Fsales` | Login wall |
| Education join | `https://appwrite.io/education/join` | GitHub signup only |
| Discord | `https://discord.com/invite/appwrite` | External invite |
| GitHub star, source, roadmap | `github.com/appwrite` | External. Not clicked |

## Same chrome, not a separate capture

These are reachable and use the same marketing or docs chrome as a page above. They are listed so the tree is complete. They are not separate screenshot families.

- Other comparisons: `/alternative-to/amplify`, `auth0`, `clerk`, `cloudinary`, `convex`, `neon`, `netlify`, `planetscale`, `supabase`, `vercel`.
- Other blog categories: announcements, architectures, customer-stories, open-source, products, security, ai, startups.
- Blog pagination `/blog/2` through `/blog/37`, author pages, and individual posts.
- Other changelog entries and other integration detail pages (the catalog has one card per integration).
- Docs sidebar: products, APIs, quick starts, tutorials, tooling. One docs home and one quick start stand in for that chrome.
- Asset file downloads (`/assets.zip`, logo SVGs). Files, not pages.

## Not present on the public surface

No public theme switch. No cookie dialog. No toast. No destructive confirmation. No signed-in dashboard, empty project, or onboarding. Partners has a form and it was not submitted, so there is no validation or success state.
