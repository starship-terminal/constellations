# Wiza public site tree

Mapped on 2026-11-21 from the live public site, signed out. Official domain confirmed as `https://wiza.co/` (wordmark "wiza", hero "Find verified emails and phone numbers in seconds"). Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. `login-extracted` stays `not-started`.

The marketing site is Webflow and paints one light theme. There is no theme control. `color-scheme` on the root was `normal`. The blog is a separate WordPress surface. Login and signup are a separate app at `/auth/`.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Header "Log in" | `https://wiza.co/auth/login` | Empty email field, placeholder "e.g: john@toyota.com". Log in. "Log in via Google". Not typed. Google not clicked. Log in not clicked. |
| Header "Sign up", hero "Get started for free", 404 "Get started for free" | `https://wiza.co/auth/signup` | "Get started for free." Empty work-email field, same placeholder. Sign up. "Sign up via Google". Not typed. Google not clicked. Sign up not clicked. |
| Signup "Log in" | The login wall | Not followed from the signup card. |
| Login "Get started" | The signup wall | Not followed from the login card. |
| Login "Reset it here" | A password reset form | Not clicked. |
| "Get a demo", Resources "Book a meeting", footer "Get a demo" | `https://wiza.co/book-demo` | A HubSpot form (work email, first name, last name, use case). Photographed in the browser, then discarded. Not typed. Not submitted. |
| Footer "Do not sell or share my personal information" | `https://wiza.co/optout-contact-info` | An opt-out form with name, email, and phone fields, plus a captcha. Not typed. Captcha not solved. Submit not clicked. Shot discarded. |

Headless Chromium received a Cloudflare "Just a moment..." page on `/auth/signup` and on `/directory`. Those shots were discarded. The empty signup wall in this package is the T3 preview browser at `https://wiza.co/auth/signup`, field empty, scaled from a 2x frame to 1440 by 900.

## Homepage header (`https://wiza.co/`)

Desktop, left to right: logo to `/`, Solutions (hover menu), Resources (hover menu), Enterprise (`/enterprise`), Pricing (`/pricing`). Right side: Log in, Sign up. The bar is a white pill.

| Control | Opens |
|---|---|
| Solutions | A white panel. Left: Sales (`/sales`), Recruiting (`/recruiting`), Marketing (`/marketing`), AI Research (`/ai-research`), API (`/wiza-api`), Wiza MCP (`/mcp`). Right, "How it works": Watch video (`/watch-demo`). |
| Resources | A white panel. Support Line: Knowledge base (`https://help.wiza.co/`), Support (href `#`, no dialog opened on click). Learn and Grow: Customers (`/customers`), Blog (`/blog`), Watch our demo (`/watch-demo`), Book a meeting (`/book-demo`). |
| Enterprise | `https://wiza.co/enterprise` |
| Pricing | `https://wiza.co/pricing` |
| Log in | Login wall. |
| Sign up | Signup wall. |
| Hero play control | A Webflow lightbox. The open state did not show a finished video frame, so that shot was discarded. The video was not played. |

Phone (390): logo, Log in, and a menu button. The menu is a full-screen drawer: Solutions, Resources, Enterprise, Pricing, then Get a demo and Get started for free. The drawer was photographed. No row was followed.

## Footer

On the homepage, after the page. White fill, muted links. Columns:

- Brand line: "The future of prospecting © 2026 Wiza" and "Wiza is a sales prospecting and engagement platform."
- Email: `mailto:hello@wiza.co`. Not opened.
- Solutions: Wiza Prospect (`/`), Wiza Enterprise, AI Research, API, Wiza MCP, Integrations (`/integrations`), Pricing, Get a demo.
- Resources: Customers, Blog, Knowledge base (`help.wiza.co`), Support (`#`), Trust center (`https://trust.wiza.co/`), Status (`https://status.wiza.co/`), Free email finder (`/find-email-free`), Free email verifier (`/verify-email-free`), Company directory (`/directory`).
- Company: Feature requests (`feedback.wiza.co`), Changelog (`feedback.wiza.co`), Careers (`apply.workable.com`), Become an affiliate (Typeform), Terms of service (`/tos`), Privacy policy (`/privacy`), Privacy center (`/privacy/center`), Vulnerability disclosure (`/vdp`), Do not sell or share my personal information (`/optout-contact-info`).
- Social: LinkedIn, YouTube, Instagram, X. Not opened.
- Credit: Site by Yes Chef Studio. Not followed.

Trust center, Status, Knowledge base, Careers, Feature requests, Changelog, and the affiliate form are other hosts. They were not captured as product pages.

## Pages opened

| Page | What it is |
|---|---|
| `https://wiza.co/` | Marketing home. Lavender hero. Product demo artwork. |
| `https://wiza.co/pricing` | Individual plans. Free, Starter, Email, Email + Phone. Annual is the default. Monthly was opened. Checkout was not entered. |
| `https://wiza.co/enterprise` | Enterprise product page. |
| `https://wiza.co/sales` | Sales solution. |
| `https://wiza.co/recruiting` | Recruiting solution. |
| `https://wiza.co/marketing` | Marketing solution. |
| `https://wiza.co/ai-research` | AI Research. |
| `https://wiza.co/wiza-api` | API product page. |
| `https://wiza.co/mcp` | Wiza MCP. |
| `https://wiza.co/customers` | Customer stories. |
| `https://wiza.co/integrations` | Integrations index. |
| `https://wiza.co/blog/` | Blog index. Separate header (Login, Create account). Search field not typed. |
| `https://wiza.co/privacy` | Privacy policy. |
| `https://wiza.co/tos` | Terms of service. |
| `https://wiza.co/privacy/center` | Privacy center. |
| `https://wiza.co/vdp` | Vulnerability disclosure. |
| `https://wiza.co/watch-demo` | Product demo page. Video not played. |
| `https://wiza.co/find-email-free` | Free email finder landing. The finder itself is a signup wall. Not submitted. |
| `https://wiza.co/verify-email-free` | Free email verifier landing. Not submitted. |
| `https://wiza.co/this-page-does-not-exist-capture-2026` | 404. "This page could not be found." Return home and Get started for free. |
| `https://wiza.co/auth/login` | Login wall. Empty. |
| `https://wiza.co/auth/signup` | Signup wall. Empty. Preview browser. |
| `https://wiza.co/directory` | Cloudflare check in headless Chromium. Discarded. |
| `https://wiza.co/book-demo` | Demo form. Discarded. |
| `https://wiza.co/optout-contact-info` | Opt-out form and captcha. Discarded. |

## Phone

390 by 844, devicePixelRatio 2. Homepage, the homepage menu drawer, and pricing. Pricing stacks the plan cards.
