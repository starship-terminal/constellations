# Anam public site tree

Mapped 2026-11-21 from `https://anam.ai/` with Playwright (headless Chromium, 1440x900), before screenshots. The crawl followed in-page links from the home page and stopped at 60 visited pages with more still queued. Paths below include those visits plus links those pages exposed. Auth, signup, Google, GitHub and SSO were recorded and not opened. No form was submitted. No field was filled.

Two marketing headers exist. The Framer home (`/`) shows logo, Developers, Pricing, Sign in. Next.js pages (`/pricing`, `/tools`, `/cara-4-1`, `/get-demo`) show logo, a Developers button, Pricing, a Resources button, Sign in. Docs (`/docs/...`) are Mintlify.

## Auth walls (recorded, not entered)

| Control | URL | Why the branch stopped |
|---|---|---|
| Sign in (Framer and Next nav) | `https://lab.anam.ai/login` | Email and password, or Google, GitHub, or SSO. Known probe. Not typed. Not clicked. |
| Sign up, Start building, Get started, Start for free, plan CTAs | `https://lab.anam.ai/register` and `?plan=` variants | Account creation. |
| Docs Sign In | `https://lab.anam.ai/` | Lab app. |
| Get an API key, Pick an avatar, Anam Lab, Create a persona | `https://lab.anam.ai/api-keys`, `/build`, `/` | Signed-in product. |
| Docs "Single sign-on" nav link | `/docs/security/single-sign-on` | Public doc page about SSO. The page itself is public. The SSO login control is not used. |

GitHub links (`github.com/anam-org/...`) are external source repos, not the product. They were not opened. Newsletter (`https://mail.anam.ai/subscribe`) is a form. It was not filled and not submitted.

## Framer home header (`/`)

| Control | Opens |
|---|---|
| Logo (`aria-label` home) | `/` |
| Developers | `/api` |
| Pricing | `/pricing` |
| Resources | Link. Hover and a Developers-button click on `/` on 2026-11-21 opened no dropdown (`home-light-nav-submenu.png` matches the resting header). The Next.js header on `/pricing` is the one with the dropdown. |
| Sign in | `https://lab.anam.ai/login` (wall) |

At 390 the home header shows a hamburger (`div[data-framer-name=Icon]`, no accessible name) beside Sign in. A real click opens the same Company / Start building / Resources list as the pricing menu. `/pricing` at 390 uses an X close on that menu. A synthetic DOM click does not open it.

In-page controls on `/`, not submissions:

| Control | Interaction |
|---|---|
| Select card 1-5 | Local carousel. Swaps the visible persona card. |
| unmute call, call, unmute | Live avatar call (microphone and a server session). Not pressed. |
| Copy code | Copies a snippet. Local. |
| Cookie settings / Manage cookies | Cookie settings dialog (Strictly necessary always on, Analytics switch, Advertising switch). Opened, not toggled, not saved, not accepted or rejected. |
| Reject all / Accept all | Consent submission. Not pressed. |

## Next.js header (`/pricing`, `/tools`, `/cara-4-1`)

| Control | Opens |
|---|---|
| Logo | `/` |
| Developers button (`aria-expanded`) | Dropdown. Same panel as Resources (see below). |
| Pricing | `/pricing` |
| Resources button | Same dropdown. |
| Sign in | `https://lab.anam.ai/login` (wall) |
| Open menu (present on `/pricing` as `aria-expanded=false`) | Mobile nav. Captured at 390. |

Developers and Resources both open one dropdown. Columns read on `/pricing` on 2026-11-21:

| Column | Item | Destination |
|---|---|---|
| Company | Team | `/about` |
| Company | Research | `/research` |
| Company | Security | `/ai-governance` |
| Build | Developers | `/api` |
| Build | Documentation | `/docs/javascript-sdk/quickstart` |
| Build | Integrations | `/integrations` |
| Build | Tools | `/tools` |
| Build | Changelog | `/changelog` |
| Learn | Cara-4.1 Express | `/cara-4-1` |
| Learn | Blog | `/blog` |
| Learn | Customer stories | `/case-studies` |
| Learn | Avatar Benchmark | `/tools/latency-benchmark` |
| Learn | Interactive Avatars | `/interactive-avatars` |
| Learn | Glossary | `/resources/glossary` |

Pricing page, not a submission:

| Control | Interaction |
|---|---|
| Monthly / Yearly 2 months free | Local billing toggle (`aria-pressed`). Yearly was pressed on load. |
| Pay yearly, save $… | Same local period switch, per plan card. |
| Get started / Start for free | `lab.anam.ai/register` (wall). |
| Talk to sales | `/get-demo` |

## Docs chrome (`/docs/introduction/overview`)

Top bar:

| Control | Opens |
|---|---|
| Anam home page | `https://anam.ai` |
| Search (`Open search`, ⌘K) | Dialog "Search or ask a question...". Escape closes it. Not typed. |
| Ask Assistant (⌘I) | Assistant panel. Close / Maximize buttons. Not typed. Not sent. |
| Cookbook | `/cookbook` |
| llms.txt | `/docs/llms-full.txt` |
| Support | Slack invite (external). Not joined. |
| Sign In | `https://lab.anam.ai/` (wall) |
| Change theme preference | Menu: System, Light, Dark. Local theme only. |

Secondary nav:

| Control | Destination |
|---|---|
| Overview | `/docs/introduction/overview` |
| Embed | `/docs/embed/overview` |
| JavaScript SDK | `/docs/javascript-sdk/api-key` |
| Python SDK | `/docs/python-sdk/overview` |
| Integrations (button) | Menu of integration docs (sidebar also lists them) |
| API Reference | `/docs/api-reference/overview` |
| Changelog | `/docs/changelog` |

Sidebar groups visible on the overview page (each item is a page, same chrome):

| Group | Pages |
|---|---|
| Getting started | `/docs/introduction/overview`, `/docs/introduction/models` |
| Personas | `/docs/personas/overview`, `/docs/personas/director-notes`, `/docs/personas/meetings` |
| Avatar videos | `/docs/avatar-videos/overview` |
| Security | `/docs/security/privacy`, `/docs/security/network`, `/docs/security/single-sign-on`, `/docs/security/ai-avatar-disclosure` |
| Resources | `/docs/resources/mcp`, `/docs/resources/billing-and-limits`, `/docs/resources/session-performance`, `/docs/resources/session-termination-reasons`, `/docs/resources/faq` |

Docs also expose a Cookie preferences dialog (Decline / Accept). Not pressed. On this pass it sat on top of ⌘K until it was hidden with `display:none` (not a consent click).

Further docs paths linked from crawled pages (same Mintlify chrome, not each given its own screenshot): JavaScript SDK reference and examples, Python SDK, embed widget, LiveKit, Shopify, API reference sessions, personas, meetings, avatar videos, watermark checks. The crawl queue still held more when it stopped at 60 pages.

## Footer (home, scrolled)

| Group | Item | Destination |
|---|---|---|
| Product | Cara-4.1 Express | `/cara-4-1` |
| Product | Interactive Avatars | `/interactive-avatars` |
| Product | Customer stories | `/case-studies` |
| Product | API Platform | `/api` |
| Product | Blog | `/blog` |
| Product | Pricing | `/pricing` |
| Company | About | `/about` |
| Company | Research | `/research` |
| Company | Careers | `/about#careers` |
| Developers | Documentation | `/docs/javascript-sdk/quickstart` |
| Developers | API Reference | `/docs/javascript-sdk/quickstart` (footer href, not `/docs/api-reference`) |
| Developers | Changelog | `/changelog` |
| Developers | Tools | `/tools` |
| Developers | Avatar Benchmark | `/tools/latency-benchmark` |
| Resources | Glossary | `/resources/glossary` |
| Resources | Compare | `/compare` |
| Resources | Guides | `/resources/guides` |
| Resources | Status Page | `https://status.anam.ai/` (external status host) |
| Resources | llms.txt | `/llms.txt` |
| Resources | Trust Center | `https://trust.anam.ai/` (external trust host) |
| Legal | AI Governance | `/ai-governance` |
| Legal | Terms of Service | `/terms-of-service` |
| Legal | DPA | `/data-processing` |
| Legal | Acceptable Use | `/acceptable-use-policy` |
| Legal | Privacy Policy | `/privacy-policy` |
| Social | LinkedIn, YouTube, X, Slack | External. Not opened. |
| Social | Newsletter | `https://mail.anam.ai/subscribe` (form, not filled) |
| CTA | Get started | `https://lab.anam.ai/register` (wall) |

## Page families reached from the home page

Marketing and app pages (public, 200 on the ones visited):

| Path | What it is |
|---|---|
| `/` | Framer home, persona carousel, cookie card |
| `/api` | Developer marketing |
| `/pricing` | Plans, billing toggle |
| `/about` | Team |
| `/research` | Research |
| `/ai-governance` | Governance |
| `/integrations` | Integration index |
| `/tools` | Tool index |
| `/tools/latency-benchmark` | Benchmark |
| `/changelog` | Changelog |
| `/cara-4-1` | Product page |
| `/blog` | Article index |
| `/blog/cara-4-1-express` | Article, plus an email field (not filled) |
| `/case-studies` | Story index |
| `/interactive-avatars` | Product page, "Switch to video with Mia" (local) |
| `/get-demo` | Demo form (name, email, company URL). Photographed. Not filled. Not submitted. |
| `/resources/glossary` | Glossary index |
| `/compare` | Comparison index |
| `/resources/guides` | Guides index |
| `/cookbook` | Cookbook index |
| `/terms-of-service`, `/privacy-policy`, `/data-processing`, `/acceptable-use-policy` | Legal |
| `/llms.txt`, `/pricing.md` | Plain text for agents |

Linked and not each visited (same families, public): `/integrations/*` (agora, cartesia, coreweave, deepgram, elevenlabs, fishaudio, livekit, pipecat, videosdk), `/interactive-avatars/*`, `/tools/*` (playground, interview, tutor, role-play, spelling, quality benchmark, text-to-avatar-video), `/avatar-games/*`, `/case-studies/*`, `/blog/*` and `/blog/categories/*`, `/blog/authors/ben-carr`, `/resources/glossary/*`, `/cookbook/*` and `/cookbook/topic/*`, `/cara4`, `/quickstart`, `/incidents/01KC7A6Q9Q6H1JDZ83TP1EF1Z1`.

External hosts linked from public pages, not captured: `status.anam.ai`, `trust.anam.ai`, `mail.anam.ai`, LinkedIn, YouTube, X, Slack, jobs.ashbyhq.com, Mintlify, Framer, vendor docs. `www.developer.anam.com` appeared as a placeholder URL inside docs copy (`/INSERT?...`), not a real destination.

## Capture set taken from this tree

Desktop 1440x900 and phone 390x844, light, plus docs dark on desktop:

- Surfaces: home, api, pricing, about, research, interactive-avatars, integrations, tools, changelog, cara-4-1, blog, case-studies, get-demo, glossary, compare, guides, cookbook, docs overview, docs API reference.
- States: cookie card, cookie settings dialog (opened, not submitted), persona card select, pricing menu, billing toggle, docs search dialog, docs assistant panel, docs dark theme.
- Phone: home, pricing (menu open), docs overview (menu if a control exists).

Article, glossary term, cookbook recipe, integration detail and API operation pages share the index chrome. They are not each screenshotted. Signed-in lab, live call, checkout, newsletter and every auth button stay out.
