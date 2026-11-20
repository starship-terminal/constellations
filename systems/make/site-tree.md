# Make public site tree

Mapped from https://www.make.com/ in headless Chromium on 2026-11-21, before screenshots. Desktop viewport requested 1440×900. The header lives in a shadow root (`code-island` / `.header`). OneTrust's cookie banner mounts on every page; it was hidden with CSS and its scripts were aborted at request time. No consent button was clicked. No form was submitted.

Theme: one light theme. `color-scheme` is `normal`. No `data-theme`, no dark class, no theme toggle.

## Shell

| Control | Opens |
|---|---|
| Announcement bar "Read now" | https://www.make.com/blog/waves26-the-glass-box-for-the-agentic-era (new tab) |
| Announcement bar close | Dismisses the bar on this page only |
| Logo "make" | https://www.make.com/ |
| Skip to main content | `#main-content` |
| Product (nav-dd-toggle) | Mega menu, see below |
| Solutions | Mega menu |
| Resources | Mega menu |
| Partners | Mega menu |
| Pricing | https://www.make.com/pricing |
| Enterprise | https://www.make.com/enterprise |
| Talk to sales | https://www.make.com/talk-to-sales |
| Sign in | https://www.make.com/login (auth wall; branch stops) |
| Get started free | https://www.make.com/register (signup wall; branch stops) |
| Phone "Open menu" | Same destinations in a drawer (integrations and templates pages expose the button) |

## Product menu

| Item | URL |
|---|---|
| Platform overview | https://www.make.com/product |
| What's new in Make | https://www.make.com/whats-new |
| Make Waves '26 | https://waves.make.com/ (subdomain; not captured as a page) |
| AI automation | https://www.make.com/ai-automation |
| Integrations | https://www.make.com/integrations |
| Build by prompting (Maia) | https://www.make.com/maia |
| AI agents | https://www.make.com/ai-agents |
| Make MCP server | https://www.make.com/mcp |
| MakeOS | https://www.make.com/makeos |
| Observability (Grid) | https://www.make.com/grid |
| Enterprise | https://www.make.com/enterprise |
| Security | https://www.make.com/security |

## Solutions menu

| Item | URL |
|---|---|
| Marketing | https://www.make.com/solutions/automate-marketing |
| IT & Engineering | https://www.make.com/solutions/automate-it |
| Customer service | https://www.make.com/solutions/automate-customer-experience |
| Sales | https://www.make.com/solutions/automate-sales |
| Operations | https://www.make.com/solutions/automate-operations |
| Finance & invoicing | https://www.make.com/solutions/automate-finance |
| HR & recruiting | https://www.make.com/solutions/automate-hr |
| Productivity | https://www.make.com/solutions/automate-productivity |
| Salesforce, HubSpot, Slack, Perplexity, OpenAI chips | matching `/integrations/<slug>` pages |
| Show all integrations | https://www.make.com/integrations |

## Resources menu

| Item | URL |
|---|---|
| Integrations | https://www.make.com/integrations |
| Templates | https://www.make.com/templates |
| Library of Agents | https://www.make.com/ai-agents-library |
| Make Skills for AI | https://skills.make.com/ (subdomain; not captured) |
| Blog | https://www.make.com/blog |
| How-to guides | https://www.make.com/how-to-guides |
| Success stories | https://www.make.com/success-stories |
| Make Academy | https://academy.make.com/ (subdomain; not captured) |
| Webinars | https://www.make.com/webinars |
| Make Community | https://community.make.com/ (subdomain; not captured) |
| Help center | https://help.make.com/ (subdomain; not captured) |
| Developer Hub | https://developers.make.com/ (subdomain; not captured) |
| Compare n8n | https://www.make.com/compare/make-vs-n8n |
| Compare Zapier | https://www.make.com/compare/make-vs-zapier |
| Compare Workato | https://www.make.com/blog/make-vs-workato |

## Partners menu

| Item | URL |
|---|---|
| Hire an expert | https://www.make.com/partners-directory |
| Become a partner | https://www.make.com/partners |

## Footer (same on marketing pages)

Product links already in the Product menu, plus https://www.make.com/agentic-automation, https://status.make.com/, https://www.make.com/platform-ideas, https://www.make.com/integrations/category/ai.

Company: https://www.make.com/about, /careers, /contact-us, /press, /privacy-notice, /terms-and-conditions, /disclaimer, /bounty, /cookie-notice. `/en/cookie-notice` redirects to `/cookie-notice`.

Ethics & compliance leaves the site for https://www.celonis.com/legal/trust-center/ethics-compliance. Social links leave for Facebook, Instagram, X, LinkedIn, YouTube.

## On-page interactions (public, not submitted)

| Page | Control | Result |
|---|---|---|
| Home, product, feature, solution, pricing pages | FAQ / accordion buttons (`aria-expanded`) | Opens that answer in place |
| Maia, AI agents, MCP, MakeOS, Grid | Feature tabs | Switches the panel |
| Integrations, templates, agents library | Search field | Filters the public list; not submitted as a form |
| Integrations, templates | Category checkboxes, Open filters | Filter panel |
| Pricing | Plan cards, billing toggle if present, FAQ | In-page. "Get started" on a plan goes to `/register` and stops |
| Blog index | Article cards | One article captured: Waves '26 post. Table of contents expands |
| Blog post | Table of contents | Expands the outline |
| Careers | Search field, "View open positions" | Search filters the list. Job applications are not opened |
| Partners directory | Partner search | Filters the public directory |
| Talk to sales, contact | Lead forms | Visible. Not filled, not submitted |
| Cookie banner | Select Cookies Settings, Understood, Allow All, Reject All | Not clicked. Banner hidden |

## Auth walls (branch stops)

| Control | URL | What it asks |
|---|---|---|
| Sign in | https://www.make.com/login | Email, password, Continue with Google, Continue with SSO, other options |
| Get started free / Try it free / Sign up | https://www.make.com/register | Google, Apple, GitHub, Facebook, work email, name, password, captcha |
| Forgot password | https://www.make.com/en/lost-password | Not opened |
| Can't sign in | https://www.make.com/en/login-issue | Not opened |
| SSO | https://www.make.com/en/login/organization-sign-in | Not opened |
| Google / Apple / GitHub / Facebook | `/en/login/google` and siblings | Not opened |

The product app (scenario editor, org, grid) is the marketing demo on the home page, not a signed-in surface. That demo is labelled as a public demo.
