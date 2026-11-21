# Craft public site tree

Mapped on 2026-11-21 from the homepage at https://www.craft.do/ before any screenshot of this pass. The page title is "Craft — Productivity App for Notes, Tasks, and Docs". It is a live marketing site, not a parked or captcha wall.

The T3 preview tab loaded the homepage and answered DOM reads. Preview screenshots failed twice because the browser was not producing frames. Menu contents below were read after opening the controls. Query strings on Log in are omitted here. They are not committed.

Opened means the control was used and the destination was loaded or photographed. Linked means the href was read and the page was not opened from that control. External stores, social profiles, support, Slack, and the docs host were not followed from the homepage. Log in leaves www.craft.do for docs.craft.do. That wall is recorded in [login-review.json](login-review.json). Nothing was typed. No identity provider was clicked. No form was submitted.

## Header, desktop

The logo links to `/`. Product and Community are buttons. Imagine, Pricing, Learn, and Download are links. Log in and Try Craft Free sit in the same bar.

| Control | Opens |
|---|---|
| Craft Logo | `/` |
| Product | menu on the same URL. See below. |
| Imagine | `/imagine` |
| Community | menu on the same URL. See below. |
| Pricing | `/pricing` |
| Learn | `/learn` |
| Download | `/download` |
| Log in | `https://docs.craft.do/` (login wall, query stripped) |
| Try Craft Free | `/download` |

Product, opened from the header. URL stays `/`.

| Control | Opens |
|---|---|
| Plan | `/plan` |
| Write | `/write` |
| Organize | `/organize` |
| Customize | `/customize` |
| What's New | `/whats-new` |
| Imagine | `/imagine` |
| Help and Support | `https://support.craft.do` (linked, not followed) |
| Blog | `/blog` |
| Try Craft Free | `/download` |

Community, opened from the header. URL stays `/`.

| Control | Opens |
|---|---|
| Reddit Community | `https://www.reddit.com/r/CraftDocs` (linked, not followed) |
| Slack | `https://craft.do/community` (linked, not followed) |
| X / Twitter | `https://x.com/craftdocsapp` (linked, not followed) |

## Header, phone (390)

A promo link reads "Black Friday → Up to 40% off" and goes to `/pricing`. The logo goes to `/`. Try Craft Free in the bar goes to the App Store listing, not `/download`. The Menu button (`aria-label` Menu) opens a drawer on the same URL. Product is expanded in that drawer.

| Control | Opens |
|---|---|
| Plan | `/plan` |
| Write | `/write` |
| Organize | `/organize` |
| Customize | `/customize` |
| What's New | `/whats-new` |
| Imagine | `/imagine` |
| Help and Support | `https://support.craft.do` (linked, not followed) |
| Blog | `/blog` |
| Pricing | `/pricing` |
| Learn | `/learn` |
| Download | App Store listing (linked, not followed) |
| Community | collapsed accordion in the same drawer |
| Reddit Community | `https://www.reddit.com/r/CraftDocs` (linked, not followed) |
| Slack | `https://craft.do/community` (linked, not followed) |
| X / Twitter | `https://x.com/craftdocsapp` (linked, not followed) |
| Download for iOS | App Store listing (linked, not followed) |
| Log in | `https://docs.craft.do/` (login wall, query stripped) |
| Try Craft Free | `/get-craft` |

Community in the drawer was left collapsed. Its three links were already visible under the accordion.

## Homepage body

URL stays `/` unless noted. Hero heading: "Your space for notes, tasks, and big ideas". Feature chips on the page (Docs, Tasks, Calendar, Whiteboards, Daily Notes) are section labels, not separate routes.

| Control | Opens |
|---|---|
| Black Friday banner | `/pricing` |
| Try Craft Free, hero | `/download` |
| Learn more, writing | `/write` |
| Learn more, Imagine | `/imagine` |
| Claude | `/imagine/guide/mcp/claude` |
| ChatGPT | `/imagine/guide/mcp/chatgpt` |
| Claude Code | `/imagine/guide/mcp/claude-code` |
| Windsurf | `/imagine/guide/mcp/windsurf` |
| Cursor | `/imagine/guide/mcp/cursor` |
| Visual Studio Code | `/imagine/guide/mcp/vscode` |
| Raycast | `/imagine/guide/mcp/raycast` |
| Other MCP Clients | `/imagine/guide/mcp` |
| Lovable | `/imagine/guide/api/lovable` |
| Replit | `/imagine/guide/api/replit` |
| Apple Shortcuts | `/imagine/guide/api/shortcuts` |
| Bolt | `/imagine/guide/api/bolt` |
| v0 | `/imagine/guide/api/v0` |
| Codex CLI | `/imagine/guide/api/codex_cli` |
| Other Tools | `/imagine/guide/api` |
| Blog Publisher | `/imagine/personal-blog` |
| Reading Tracker | `/imagine/reading-log` |
| Plant Dashboard | `/imagine/plant-dashboard` |
| Dream Journal | `/imagine/dream-journal` |
| Explore community templates | `/imagine#community` |
| Learn more, planning | `/plan` |
| Learn more, customize | `/customize` |
| Reddit card | `https://www.reddit.com/r/CraftDocs` (linked, not followed) |
| Slack card | `https://craft.do/community` (linked, not followed) |
| X card | `https://x.com/craftdocsapp` (linked, not followed) |
| YouTube card | `https://www.youtube.com/@CraftDocs` (linked, not followed) |
| Get Started | `/download` |
| Upgrade to Plus | `https://docs.craft.do/` with a checkout query (login or checkout wall, not followed) |
| Learn more about group discounts | `/pricing` |
| Continue on web | `https://docs.craft.do/` (login wall, not followed from this control) |
| Download on the App Store | App Store listing (linked, not followed) |

Accordion buttons on the page (MCP Connections, API Integrations, Start Building, Community, Calendar, Tasks, Journal, Reminders) expand in place. They do not navigate. Two of them were already expanded on load. None of those toggles submit a form.

## Footer

| Control | Opens |
|---|---|
| Product Releases | `/whats-new` |
| Write | `/write` |
| Plan | `/plan` |
| Organize | `/organize` |
| Customize | `/customize` |
| Imagine With Craft | `/imagine` |
| Pricing | `/pricing` |
| Education Plan | `/education` |
| Slack | `https://craft.do/community` (linked, not followed) |
| Reddit Community | `https://www.reddit.com/r/CraftDocs` (linked, not followed) |
| X / Twitter | `https://x.com/craftdocsapp` (linked, not followed) |
| Learn | `/learn` |
| Use Cases | `/for` |
| Compare Craft | `/compare` |
| Getting Started Guide | `/getting-started` |
| Template Gallery | `/templates` |
| Help Center | `https://support.craft.do/` (linked, not followed) |
| Contact Support | `mailto:feedback@craft.do` (not sent) |
| About us | `/about` |
| Blog | `/blog` |
| Careers | `/careers` |
| Affiliate Program | `/affiliates` |
| Media | `/media` |
| Terms | `/terms` |
| Privacy Policy | `/privacy` |
| Security | `/security` |
| ESG | `/esg` |
| Responsible Disclosure | `/security/responsible-disclosure` |
| Craft for iPhone, iPad, Vision Pro | App Store listings (linked, not followed) |
| Craft for Mac | a `.dmg` download (not followed) |
| Windows x64, Windows ARM64 | installer downloads (not followed) |
| Craft for Android | Play Store listing (linked, not followed) |
| Instagram, YouTube, X, LinkedIn | social profiles (linked, not followed) |
| English | locale dialog on the same URL. See below. |

English opens a dialog. None of the locales were followed.

| Control | Opens |
|---|---|
| Deutsch | `/de` |
| English | `/` |
| Italiano | `/it` |
| Français | `/fr` |
| Español | `/es` |
| Tiếng Việt | `/vi` |
| 简体中文 | `/zh-CN` |
| 繁體中文 | `/zh-TW` |
| 한국어 | `/ko` |
| 日本語 | `/ja` |
| Polski | `/pl` |
| Português (Brasil) | `/pt-BR` |

## Login and signup walls

Log in, Continue on web, and Upgrade to Plus leave the marketing host. They were not used as a signed-in path. The empty docs wall was opened separately and photographed. No email, password, or code was typed. Google, Apple, and every other identity provider were not clicked.
