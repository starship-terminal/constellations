# FeedHive public site tree

Walked on 2026-11-21 from [https://www.feedhive.com/](https://www.feedhive.com/) in Playwright at 1440×900 and 390×844. Signed out. No form was submitted. No email or password was typed. Google and other SSO buttons were not clicked.

The marketing site is one Next.js app. Header and footer repeat on every public page. Desktop header menus are dropdowns (`href="#"`, `aria-expanded`). Phone header is a drawer opened by the button labelled Open menu.

Search is not present. No header, footer, or in-page control on the pages opened was a search field.

## Auth wall

These links leave the public site. The walk recorded the URL and stopped. Nothing was typed.

| Control | Where | Opens |
|---|---|---|
| Login | Desktop header, phone drawer | `https://app.feedhive.io/signin`, which redirects to `https://app.feedhive.com/signin` |
| Sign Up | Desktop header, phone header, phone drawer | `https://app.feedhive.com/signup` |
| Get started for free | Home hero | `https://app.feedhive.com/signup` |
| Get started | Feature and social pages | `https://app.feedhive.com/signup` |
| Get started. It's FREE | Some feature pages | `https://app.feedhive.com/signup` |
| Get API key | API feature page | `https://app.feedhive.com/signup` |
| Get FeedHive | Integration pages | `https://app.feedhive.com/signup` |
| Try FeedHive | Some page headers | `https://app.feedhive.com/signup` |
| Schedule it with FeedHive | LinkedIn text formatter | `https://app.feedhive.com/signup` |
| Plan card buttons | Pricing | Same signup host. Not clicked. The label sits on a signup link. |

`https://www.feedhive.com/login` returns 404, title "FeedHive - Social Media Automation", body "404 This page could not be found." Screenshot: [login-404-light-default.png](screenshots/login-404-light-default.png).

The wall that painted is [signin-wall-light-default.png](screenshots/signin-wall-light-default.png) and [mobile-signin-wall-light-default.png](screenshots/mobile-signin-wall-light-default.png). Fields and the stop are in [login-review.json](login-review.json).

## Cookie control

No cookie banner covered the page. The footer has a button labelled Cookie preferences. A click from the footer did not open a dialog in this session (the page stayed on the home view). The button was not used to accept cookies. Screenshots of the footer control are the home shots; a separate dialog shot was not kept because none painted.

## Desktop header (1440×900)

Present on every public page. Height 80px. Screenshot: [home-light-default.png](screenshots/home-light-default.png).

| Control | Opens |
|---|---|
| Logo | `/` |
| Product | Dropdown. Screenshot: [home-light-menu-product.png](screenshots/home-light-menu-product.png) |
| Agents & Automation | Dropdown. Screenshot: [home-light-menu-agents.png](screenshots/home-light-menu-agents.png) |
| Socials | Dropdown. Screenshot: [home-light-menu-socials.png](screenshots/home-light-menu-socials.png) |
| Learn | Dropdown. Screenshot: [home-light-menu-learn.png](screenshots/home-light-menu-learn.png) |
| Pricing | `/pricing` |
| Login | Auth wall. Stop. |
| Sign Up | Auth wall. Stop. |

Announcement strip above the header: "Limited launch bonus: Double your AI credits for 3 months when you start today" links to `/pricing`.

### Product menu

| Item | Opens |
|---|---|
| Scheduling | `/features/scheduling` |
| AI Tools | `/features/ai` |
| Workflow Builder | `/features/workflow-builder` |
| Social Inbox | `/features/social-inbox` |
| Collaboration | `/features/collaboration` |
| Analytics | `/features/analytics` |
| MCP Server | `/features/mcp-server` |
| FeedHive API | `/features/feedhive-api` |
| FeedHive CLI | `/features/feedhive-cli` |

### Agents & Automation menu

| Item | Opens |
|---|---|
| Claude Code | `/features/claude-code` |
| OpenClaw | `/features/openclaw-skills` |
| Hermes Agent | `/features/hermes` |
| ChatGPT | `/features/chatgpt` |
| Manus | `/features/manus` |
| Claude | `/features/claude` |
| Grok Bot | `/features/grok-bot` |
| Muse | `/features/muse` |
| Dots | `/features/dots` |
| Zapier | `/features/zapier` |
| Make | `/features/make` |
| n8n | `/features/n8n` |

### Socials menu

| Item | Opens |
|---|---|
| Facebook | `/socials/facebook` |
| Instagram | `/socials/instagram` |
| YouTube | `/socials/youtube` |
| TikTok | `/socials/tiktok` |
| LinkedIn | `/socials/linkedin` |
| Pinterest | `/socials/pinterest` |
| Google Business | `/socials/google-business` |
| Threads | `/socials/threads` |
| Twitter/X | `/socials/twitter-x` |
| Discord | `/socials/discord` |

### Learn menu

| Item | Opens |
|---|---|
| API Docs | `https://docs.feedhive.com/rest-api/introduction` (external docs, not walked) |
| Automation | `https://docs.feedhive.com/workflows/introduction` |
| Integrations | `https://docs.feedhive.com/automation-integrations/zapier` |
| Blog | `/blog` |
| Free tools | `/tools` |

## Phone header (390×844)

Closed: logo, Sign Up, Open menu. Screenshot: [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

Open menu button opens a drawer. Screenshot: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

| Control | Opens |
|---|---|
| Close menu | Closes the drawer |
| Login | Auth wall. Stop. |
| Sign Up | Auth wall. Stop. |
| Product | Expands the same Product links as desktop. Screenshot: [mobile-home-light-menu-product.png](screenshots/mobile-home-light-menu-product.png) |
| Agents & Automation | Expands the agent links. Screenshot: [mobile-home-light-menu-agents.png](screenshots/mobile-home-light-menu-agents.png) |
| Socials | Expands the social links. Screenshot: [mobile-home-light-menu-socials.png](screenshots/mobile-home-light-menu-socials.png) |
| Learn | Expands the learn links. Screenshot: [mobile-home-light-menu-learn.png](screenshots/mobile-home-light-menu-learn.png) |
| Pricing | `/pricing` |

## Footer

Same on every public page. Brand kit is `href="#"` and did not open a dialog when clicked.

| Column | Control | Opens |
|---|---|---|
| Product | Scheduling | `/features/scheduling` |
| Product | Automation | `/features/workflow-builder` |
| Product | FeedHive AI | `/features/ai` |
| Product | Social Inbox | `/features/social-inbox` |
| Product | Collaboration | `/features/collaboration` |
| Product | Compare | `/comparison` |
| Product | Alternatives | `/alternatives` |
| Resources | Help center | `https://docs.feedhive.com` |
| Resources | API | `https://docs.feedhive.com/rest-api/introduction` |
| Resources | Blog | `/blog` |
| Resources | Pricing | `/pricing` |
| Resources | Brand kit | `#` (no dialog painted) |
| Resources | Privacy | `/privacy` |
| Resources | Terms | `/terms` |
| Resources | LinkDrip | `https://www.linkdrip.com` |
| Resources | Aidbase | `https://www.aidbase.ai` |
| Resources | Image Creator | `https://image-creator.feedhive.com` |
| Platforms | Instagram scheduler | `/socials/instagram` |
| Platforms | LinkedIn scheduler | `/socials/linkedin` |
| Platforms | TikTok scheduler | `/socials/tiktok` |
| Platforms | X (Twitter) scheduler | `/socials/twitter-x` |
| Platforms | Facebook scheduler | `/socials/facebook` |
| Platforms | YouTube Shorts scheduler | `/socials/youtube` |
| Platforms | All platforms | `/socials` |
| Agents | Claude, ChatGPT, Claude Code, OpenClaw, MCP server, API | Matching `/features/...` pages |
| Agents | All integrations | `/integrations` |
| Compare | FeedHive vs Buffer, Hootsuite, Sprout Social, Later, Metricool, Publer | `/comparison/<slug>` |
| Compare | All comparisons | `/comparison` |
| Alternatives | Buffer, Hootsuite, Sprout Social, Later, Metricool, Publer alternatives | `/alternatives/<slug>` |
| Alternatives | All alternatives | `/alternatives` |
| Free tools | Username generator | `/tools/username-generator` |
| Free tools | Instagram font generator | `/tools/instagram-font-generator` |
| Free tools | LinkedIn text formatter | `/tools/linkedin-text-formatter` |
| Free tools | YouTube channel name generator | `/tools/youtube-channel-name-generator` |
| Free tools | Bio generator | `/tools/bio-generator` |
| Free tools | AI Slop Detector | `/tools/ai-slop-detector` |
| Free tools | All free tools | `/tools` |
| Social | Facebook, Threads, Instagram, LinkedIn, YouTube | External profile URLs. Not walked. |
| Legal | Cookie preferences | Footer button. No dialog painted. |
| Legal | Privacy, Terms | `/privacy`, `/terms` |

## Pages opened

Each returned 200 except `/login` (404). Desktop and phone screenshots exist for the rows marked below. Template pages (the other feature, social, and comparison URLs) share the same header, footer, and a signup CTA. They were opened and photographed during the walk. The package keeps a representative set in [screenshots/](screenshots/).

| Path | In-page controls | Package shot |
|---|---|---|
| `/` | Hero CTA to signup. Composer, AI Assistant, Automation, Post Conditions are tabs on the marketing demo, not the app. | home, mobile-home |
| `/pricing` | Monthly and Yearly toggle. Yearly starts selected. Plan cards link onward to signup. | pricing, mobile-pricing |
| `/blog` | Post cards. No search field. | blog, mobile-blog |
| `/tools` | Cards to each free tool. | tools, mobile-tools |
| `/tools/username-generator` | Platform buttons (TikTok, Instagram, YouTube), tone buttons, textarea, keyword input, Generate usernames. Not submitted. | tools-username |
| `/tools/instagram-font-generator` | Style buttons and a textarea. Not submitted. | walk only |
| `/tools/linkedin-text-formatter` | Style buttons, textarea, Clear, Copy text, Schedule it with FeedHive (signup wall). Not submitted. | walk only |
| `/tools/youtube-channel-name-generator` | Same shape as the username tool. Not submitted. | walk only |
| `/tools/bio-generator` | Platform and tone buttons, textarea. Not submitted. | walk only |
| `/tools/ai-slop-detector` | Textarea, Clear, Check for slop. Not submitted. | walk only |
| `/integrations` | Links to feature pages and docs. | integrations |
| `/comparison` | Links to each comparison page. | comparison |
| `/comparison/buffer` and five siblings | Comparison tables and a signup CTA. | walk only |
| `/alternatives` | Links to each alternatives page. | alternatives |
| `/alternatives/buffer` | Alternatives article and a signup CTA. | walk only |
| `/privacy`, `/terms` | Legal text. Footer links only. | privacy |
| `/features/*` listed in the menus | Feature article, docs links, signup CTA. | walk only |
| `/socials` and `/socials/*` | Platform article and a signup CTA. | walk only |
| `/login` | 404. | login-404 |

Docs, social profiles, LinkDrip, Aidbase, Image Creator, ChatGPT, Claude, Zapier, and Make links leave www.feedhive.com. They were recorded and not walked.

## Not captured

The signed-in app behind `app.feedhive.com` was not captured. Signup, recovery (`/recovery`), onboarding, and any page after Sign in were not opened past the wall.
