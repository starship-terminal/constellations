# Granola public site tree

Mapped 2026-11-21 from https://www.granola.ai/ before screenshots. The seed was the homepage, then the same-site links it exposes, then https://www.granola.ai/sitemap.xml (365 URLs, lastmod 2026-11-21). Auth and download hosts were requested and not entered. No field was typed into. No form was submitted. Google, Apple, and Microsoft were not clicked.

Theme: one painted light theme on the marketing site. `html` carries `data-theme="v2"`. `<meta name="theme-color">` is `#ffffff`. No public theme toggle.

## Global chrome

Desktop header (1440), left to right:

| Control | Opens | Stop |
|---|---|---|
| Logo (`aria-label` "Granola home") | https://www.granola.ai/ | |
| Features | Hover menu, in place. The trigger is a `div`, not a link. Pointer enter on its parent opens it. A click does not navigate | See Features menu |
| Enterprise | https://www.granola.ai/enterprise | |
| Pricing | https://www.granola.ai/pricing | |
| Blog | https://www.granola.ai/blog | |
| Careers | https://www.granola.ai/jobs | |
| Talk to sales | https://www.granola.ai/contact/sales?source=nav | Sales form. Not submitted |
| Download | https://notes.granola.ai/download | Download host. Recorded, not treated as a product page |
| Open menu | Hidden at 1440 (`md:hidden`) | Phone drawer only |

Phone header (390): logo, Download (`https://notes.granola.ai/download`), Open menu. Features, Enterprise, Pricing, Blog, Careers, and Talk to sales are inside the drawer, not the bar.

Cookie banner (iubenda), present on first paint: Manage my preferences, Reject all, Accept all. Not clicked. Hidden in the page for later shots so the banner does not cover the chrome.

## Features menu

Opens in place on pointer enter. Closes when the pointer leaves. Items:

| Label | Opens |
|---|---|
| Notepad | https://www.granola.ai/ |
| Chat | https://www.granola.ai/chat |
| Mobile & Watch | Dialog "Granola for mobile", in place. `aria-haspopup="dialog"` |
| MCP | https://www.granola.ai/mcp |
| Voice typing by Granola | https://www.granola.ai/voice-typing |

## Granola for mobile dialog

Opened from Features > Mobile & Watch, from the footer Mobile control, and from the homepage "Download for mobile" button. Same dialog each time.

| Control | What it is | Stop |
|---|---|---|
| Email field, placeholder "Your work email" | `input type="email"` | Not typed |
| Send link | `button type="submit"` | Not clicked |
| iOS, Android | Tabs inside the dialog | Switched for a shot, no submit |
| Close | Dismisses the dialog | |

On the phone drawer, Mobile & Watch is a link to `https://granola.onelink.me/...` (AppsFlyer), not this dialog. Not opened.

## Homepage interactions

| Control | Result |
|---|---|
| Before the meeting, In the meeting, After the meeting | In-page step list under "Granola helps you before, during and after your meetings." "Before the meeting" is the painted step on load. Clicking the other two did not change the painted step in this session |
| Download for free (hero and later bands) | https://notes.granola.ai/download |
| Download for mobile | Granola for mobile dialog |
| View pricing | https://www.granola.ai/pricing |
| App Store rating link | https://apps.apple.com/us/app/granola-ai-meeting-notes/id6739429409 | External store. Not a product page |

## Phone drawer

Open menu sets `aria-expanded="true"` and the label becomes Close menu. The panel is `#mobile-menu`, fixed under the header. It repeats Features, then the desktop header links, then the footer columns. Close menu dismisses it.

## Footer

Present on marketing pages. Product, Company, Resources.

| Label | URL |
|---|---|
| Notepad | / |
| Chat | /chat |
| Voice typing | /voice-typing |
| MCP | /mcp |
| Mobile | Granola for mobile dialog |
| Pricing | /pricing |
| Enterprise | /enterprise |
| Integrations | /integrations |
| AI notepad vs notetaker | /ai-note-taker |
| AI meeting assistant | /ai-meeting-assistant |
| For sales | /use-cases/sales |
| For product management | /use-cases/product |
| Explore more… | /explore |
| Customers | /customers |
| Careers | /jobs |
| Press | https://grano.la/press |
| Events | /events |
| Startup program | /startups |
| Student program | /students |
| Nonprofit program | /nonprofits |
| Blog | /blog |
| Security | /security |
| Trust Center | https://trust.granola.ai/ |
| Transparency | /transparency |
| Help Center | https://docs.granola.ai/help-center |
| API / Developers | https://docs.granola.ai/introduction |
| Status | https://status.granola.ai/ |
| Affiliates | https://partners.dub.co/granola |
| Contact us | /contact |
| Terms | /policies |
| Privacy | https://go.granola.so/privacy |
| License | /third-party-licenses |
| LinkedIn, X, YouTube | External. Not product pages |

## Auth and download hosts (recorded, branch stopped)

| URL | What it returned | Not clicked |
|---|---|---|
| https://notes.granola.ai/ | HTTP 308 to https://granola.ai/ | |
| https://notes.granola.ai/download | HTTP 500. Next.js error shell (`__next_error__`, `noindex`). Header Download and "Download for free" point here | No retry invented a page |
| https://notes.granola.ai/login | HTTP 500. Same error shell | |
| https://app.granola.ai/ and /login | `ERR_NAME_NOT_RESOLVED` | |
| https://www.granola.ai/download | HTTP 200. Pricing "Get started" points here, not at the notes host | |

No Google, Apple, or Microsoft button was on the marketing homepage. The updates index links to a public post titled "Sign in with Microsoft is here". That is a blog post, not an identity-provider button.

## Marketing pages

Each row is a public page checked 2026-11-21. Shared chrome is the header and footer above.

| Path | What it is |
|---|---|
| / | Home. Features menu, meeting-step buttons, Download for mobile dialog, cookie banner |
| /pricing | Plans. "Get started" goes to /download. "Granola how you wanna" |
| /enterprise | Enterprise. "Talk to sales" goes to /contact/sales |
| /chat | Chat product page |
| /mcp | MCP product page |
| /voice-typing | Voice typing product page |
| /blog | Blog index. Hundreds of posts in the sitemap |
| /jobs | Careers |
| /security | Security and privacy |
| /integrations | Integration index, plus per-app pages in the sitemap |
| /customers | Customer index. Stories at /customers/brex, /docker, /vanta, /zapier |
| /contact | Contact us |
| /contact/sales | Talk to sales form. Not submitted |
| /explore | Role index |
| /updates | Announcements index. Per-entry pages under /updates/ |
| /startups, /students, /nonprofits | Program pages |
| /policies | Terms |
| /ai-note-taker, /ai-meeting-assistant | Comparison pages |
| /use-cases/sales, /use-cases/product | Use-case pages |
| /events | Events |
| /transparency | How notes are disclosed |
| /third-party-licenses | License |

Sitemap also lists /authors and 16 author pages, 16 integration pages, 18 update pages, and about 290 blog posts. Those are the same chrome. They were not each photographed.

## Not on the public homepage

No signed-in nav, settings, or create control. The product app is the notes host, which returned 500 on /download and /login and redirected / to the marketing site.
