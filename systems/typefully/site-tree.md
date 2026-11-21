# Typefully public site tree

Mapped 2026-11-21 from https://typefully.com/ in headless Playwright (desktop 1440x900) before screenshots. The homepage returned HTTP 200 with the title "Typefully: Best social media tool for creators & businesses". Same-origin links, the sitemap (231 URLs), and clicks on controls were walked. SSO buttons were not clicked. No form was submitted. No password, code, or email was typed.

The product app (Write, Plan, Analyze, drafts, queue, calendar, settings) is behind sign-in. Signed-out visitors get a marketing site plus login and signup dialogs.

## Homepage `/`

`/` is a full-viewport marketing page drawn inside a dialog (`role="dialog"`, fixed overlay, z-index 1000) over a non-interactive product-shell illustration. `documentElement.scrollHeight` stays 900. The shell's buttons (Write, Plan, Analyze, Drafts, Queue, Posted, Draft filters, Schedule, Publish, platform icons) have `pointer-events: none` on every ancestor. Clicks do not navigate, open a menu, or change the painted text. They are illustration, not routes.

The dialog has no Close control. Escape and a backdrop click leave it open.

| Control | Opens |
|---|---|
| Log in (header, y 62) | Second dialog on `/`: "Welcome back. Log in to your Typefully account." Buttons: Google, X/Twitter, LinkedIn, Email, "Sign up instead", Close. URL stays `/`. |
| Sign up (header) | Second dialog: "Get started. Sign up for Typefully." Same four provider buttons, "Log in instead", Close. URL stays `/`. |
| Google, X/Twitter, LinkedIn (hero and repeated lower CTAs) | Not clicked. Known SSO. Branch stops. |
| Email (same groups) | Reveals an email input (placeholder "your@email.com") and a hidden Cloudflare Turnstile field inside the login or signup dialog. Not submitted. |
| Footer and in-page links | Same destinations as the marketing footer below, once the long dialog is scrolled. The first probe's link list came from this dialog's DOM, not from a separate header. |

Repeated Email / Google / X / LinkedIn groups sit further down the marketing dialog (about y 2257, 3216, 6244, 7947, 9492). They open the same auth dialogs. "Add to queue Tomorrow at 5pm" and "View integrations" are inside the dialog content. View integrations points at https://zapier.com/apps/typefully/integrations (off-site).

## Marketing header

Present on pricing, blog, changelog, jobs, tools, glossary, platform pages, and the other marketing routes. Not a separate nav on `/` (that page is the modal).

| Control | Opens |
|---|---|
| Typefully (logo) | `/?typ_source=<page>&typ_content=header-logo` (the homepage modal) |
| Pricing | `/pricing` |
| Blog | `/blog` |
| Changelog | `/changelog` |
| Jobs | `/jobs` |
| Help | https://support.typefully.com (Intercom help center; HTTP 200, title "Home \| Typefully Help Center") |
| Try Typefully now | `/?typ_source=<page>&typ_content=header-cta` (homepage modal, login/signup wall) |

Phone 390x844 on `/pricing`: the logo and "Try Typefully now" only. Pricing, Blog, Changelog, Jobs, and Help are not in the top bar. There is no menu button in the first 100px. Those links remain in the footer.

## Marketing footer

Same groups on the marketing pages. External hosts are recorded and not walked as Typefully UI.

| Group | Control | Opens |
|---|---|---|
| Legal | Privacy | https://support.typefully.com/en/articles/8718444-privacy-policy |
| Legal | Terms | https://support.typefully.com/en/articles/8718440-terms-of-service |
| Legal | Contact us | A mailto link. Not opened. The address is not recorded. |
| Company | Work with us | `/jobs` |
| Product | AI | `/ai` |
| Product | Pricing | `/pricing` |
| Product | Changelog | `/changelog` |
| Product | Affiliate program | https://support.typefully.com/en/articles/8718317 |
| Product | Schedule X posts | `/x-twitter` |
| Product | Schedule LinkedIn posts | `/linkedin` |
| Product | Schedule Threads posts | `/schedule-threads-posts` |
| Product | API docs | `/docs/api` |
| Product | AI Agents | `/ai-agents` |
| Product | Zapier | https://support.typefully.com/en/articles/8718280-automate-typefully-with-zapier |
| Product | MCP | https://support.typefully.com/en/articles/13128440-typefully-mcp-server |
| Help | Help pages | https://support.typefully.com/ |
| Help | Brand assets | https://typefully.notion.site/Brand-Assets-68774421815c49368c0967578f1616ae (off-site Notion) |
| Help | Twitter | https://x.com/typefully (off-site; not clicked as SSO) |
| Help | Blog | `/blog` |
| Help | Announcements | `/announcements` |
| Help | Keyboard Shortcuts | `/shortcuts` |
| Compare | Typefully vs Buffer | `/blog/buffer-review-alternative` |
| Compare | Typefully vs Hypefury | `/blog/hypefury-review-alternative` |
| Compare | Typefully vs TweetHunter | `/blog/tweet-hunter-review-alternative` |
| Compare | Typefully vs Ordinal | `/blog/typefully-vs-ordinal-review-alternative` |
| Use | Schedule social posts | `/social-media-scheduling` |
| Use | Get a social blog | `/profile` |
| Use | Automate with Zapier | https://zapier.com/apps/typefully/integrations |
| Use | Boost engagement | https://support.typefully.com/en/articles/8718239 |
| Use | Minimal Theme for X | `/minimal-twitter` |
| Tools | Fake Tweet Generator | `/tools/fake-tweet-generator` |
| Tools | Twitter Character Counter | `/tools/twitter-character-counter` |
| Tools | LinkedIn Video Downloader | `/tools/linkedin-video-downloader` |
| Tools | Social Media Glossary | `/social-media-glossary` |
| Tools | All tools | `/tools` |
| AI tools | Free AI Writer | `/tools/ai/ai-writer` |
| AI tools | AI Story Generator | `/tools/ai/ai-story-generator` |
| AI tools | AI Text Generator | `/tools/ai/ai-text-generator` |
| AI tools | ChatGPT Alternative | `/tools/ai/chat-gpt-alternative` |
| AI tools | AI Paragraph Generator | `/tools/ai/ai-paragraph-generator` |
| AI tools | AI Content Generator | `/tools/ai/ai-content-generator` |
| AI tools | All AI Tools | `/tools/ai` |

## Marketing pages (sitemap and live probes)

Each row is a public page that loaded (HTTP 200) unless noted. "Try Typefully now", "Get started", and "Create profile" all land on the homepage auth wall.

| Path | What it is | Controls that open something else |
|---|---|---|
| `/pricing` | Plan cards (Free, Creator, Business) and a feature comparison. No monthly/yearly toggle; copy says annual billing. | "1 social set" opens a menu: "Social Sets. A social set is a collection of social media accounts…" with Learn more. Comparison rows (Publishing, Scheduling, Calendar, Social Sets, Teams, Writing Assistant, API, and the other feature rows) are `aria-expanded` disclosure rows; several expand in place with little extra text. Six "Get started" buttons go to `/` (auth wall). Phone comparison uses Free / Creator / Business tabs. |
| `/ai` | Writing assistant marketing. | Header and footer. Auth CTAs go to `/`. |
| `/ai-agents` | Agents marketing. | Header and footer. |
| `/x-twitter` | Schedule X posts. | Header and footer. |
| `/linkedin` | Schedule LinkedIn posts. | Header and footer. |
| `/schedule-threads-posts` | Schedule Threads posts. | Header and footer. |
| `/bluesky` | Schedule Bluesky posts. In the sitemap, not the footer. | Header and footer. |
| `/content-ideas` | Content ideas marketing. In the sitemap. | Header and footer. |
| `/social-media-analytics` | Analytics marketing. In the sitemap. | Header and footer. |
| `/social-media-scheduling` | Scheduling marketing. | Header and footer. |
| `/profile` | Public Typefully Profiles landing. Featured creator threads (for example `/DanHollick/...`) are published posts. | Log in and Create profile open the homepage auth dialog (Create profile stays on `/profile` with the marketing modal; Log in navigates to `/`). "Follow on Twitter" and "My website" are off-site. Thread titles open `/<handle>/<slug>` public posts. |
| `/minimal-twitter` | Chrome extension marketing for a Minimal Theme. | Install control points at the Chrome Web Store (off-site). |
| `/blog` | Index of 84 posts, no pager. | Each card opens `/blog/<slug>`. Sample post `/blog/x-analytics-ai-agents` has a "Mini Tools" control. |
| `/changelog` | 20 entries per page, then "Older updates". | Entry links `/changelog/<slug>`. Older updates opens `/changelog/page/2` through `/changelog/page/6` (sitemap). |
| `/announcements` | Two posts. | `/announcements/typefully-2-0` and `/announcements/twitter-co-founder-evan-williams-invests-in-typefully`. |
| `/academy` | Discontinued email course. Copy says the growth course subscription has been discontinued and points at the blog. | Header and footer. No course player. |
| `/jobs` | "Work at Typefully." No open-role links in the probe. A reach-out line is present. The address is not recorded. | Header and footer. |
| `/shortcuts` | Keyboard shortcut reference for the signed-in app (Command Bar, sidebars). The page itself is public. | No interactive menu. Documents shortcuts that exist only once signed in. |
| `/tools` | Tool index. | Cards open the tool paths below. |
| `/tools/ai` | AI tool index. | Cards open `/tools/ai/<slug>`. Sitemap also lists `/tools/ai/hook-generator`, which is not in the footer. |
| `/tools/fake-tweet-generator` | Local mock tweet composer. | Fields: Account Name, Handle, tweet textarea, avatar URL, file upload, datetime, verification select. Buttons: Mini Tools, Upload image, Show Advanced Options, Publish with Typefully, Copy image, Download. Not submitted. Publish with Typefully is an auth-wall candidate and was not used to create an account. |
| `/tools/twitter-character-counter` | Public counter. | Local fields. Not submitted. |
| `/tools/linkedin-video-downloader` | Public tool. | Not submitted. |
| `/tools/linkedin-text-formatter` | Public tool. In the tools index, not the footer. | Not submitted. |
| `/tools/linkedin-post-preview` | Public tool. In the tools index. | Not submitted. |
| `/social-media-glossary` | Term index, A–Z jump links (same page), search field. | Search is `type=search`, placeholder "Search for a marketing term ...". Not submitted. About 77 term links open `/social-media-glossary/<slug>` (for example `/social-media-glossary/algorithm`). |
| `/docs/api` | Scalar API reference ("Typefully Public API"). | Open Search opens a search field (placeholder "Search..."). Sidebar groups (Introduction, Users, Social Sets, Drafts, Comments, Engagements, Queue, Media, Tags, Webhooks) expand and collapse. Endpoint rows (GET, POST, PATCH, PUT, DEL) scroll to that operation. An API Client panel is on the page (Token field visible). Token was not filled. No request was sent. |
| `/refunds` | Not a public page. Redirects to `/?next=/refunds` (homepage auth wall). | Stop. |

## Auth wall (every branch that asks to sign in)

Reached from Log in, Sign up, Get started, Try Typefully now, and Create profile.

| Control | Result |
|---|---|
| Google | Not clicked. SSO. |
| X/Twitter | Not clicked. SSO. |
| LinkedIn | Not clicked. SSO. |
| Email | Shows an email field and a Turnstile widget. Not submitted. |
| Sign up instead / Log in instead | Switches the same dialog between signup and login. |
| Close | Dismisses the second dialog. The homepage marketing dialog has no Close. |

Direct URLs `/login`, `/signup`, `/sign-up`, `/app`, and `/mastodon` return the site's "Not found..." page (HTTP 200), not an auth form.

## Stopped branches

| Branch | Why |
|---|---|
| Signed-in app (Write, Plan, Analyze, queue, calendar, settings, team, billing) | Login wall. Shell on `/` is not clickable. |
| Google, X, LinkedIn, Apple SSO | Forbidden. Apple was not offered on the probed dialog. |
| Email submit, newsletter, jobs mailbox, profile create | Forms not submitted. |
| `/refunds` | Redirects to the homepage auth wall. |
| support.typefully.com, Notion brand assets, Zapier, X, Chrome Web Store | Other hosts. Help center home was confirmed up; its article tree was not captured as the product UI. |
| Changelog pages 3–6 and most of the 84 blog posts and 77 glossary terms | Same template as the index item and the first sample. Sitemap lists them. Captures cover the index, one post, one changelog entry, and one glossary term rather than every slug. |

## Theme

No theme toggle was found on the marketing pages. With `prefers-color-scheme: dark`, `/pricing` paints a dark page background (`rgb(17, 20, 24)`) while `color-scheme` stays `normal` and `html` has no `dark` class. Light is the captured default (`colorScheme: light` in the browser context). A forced dark context is recorded as a preference check, not as a second product theme switch.
