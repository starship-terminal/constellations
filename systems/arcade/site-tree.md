# Arcade public site tree

Walked signed out on 2026-11-21 from [https://arcade.software](https://arcade.software), which redirects to [https://www.arcade.software/](https://www.arcade.software/) (HTTP 200). Title: Arcade | AI Video Generator for Marketing Teams. Desktop viewport 1440. Phone viewport 390. One light theme. No page-level theme switch. The Finsweet consent banner, when it mounts, is hidden and not accepted or rejected. Intercom is hidden and not opened. Query strings are stripped.

Opened means the control was used and the destination loaded, or the in-page result was photographed. Linked means the href was read and the page was not opened in this pass. A prior capture (2026-11-10) already has screenshots for several marketing routes. This file records this pass.

## Header, desktop

The logo (`a.logo-nav`, accessible name "home") links to `/`.

Product and Resources are anchors with no href. Each opens a dropdown on `/`. Photographed in [home-light-product.png](screenshots/home-light-product.png) and [home-light-resources.png](screenshots/home-light-resources.png).

| Control | Opens |
|---|---|
| Product / Chrome Extension | `https://chromewebstore.google.com/detail/arcade-ai-videos/plbpmcliejllllhnalcbmggjkchokpbg`. Linked. Not opened. Subtitle: Capture your screen and camera with smart zooms and cursor. |
| Product / Agents | `/agents`. Subtitle: Build content with your AI tools. |
| Product / Interactive Demos | `/product/interactive-demo`. Subtitle: Let people experience your product. |
| Product / AI Video | `/`. Subtitle: Make every video your own. |
| Product / Apps | `/apps`. Subtitle: Make videos from your team's tools. |
| Pricing | `/pricing` |
| Resources / Blog | `/blog`. Subtitle: Ideas, guides, and stories. |
| Resources / Showcase | `/ai-video-examples`. Subtitle: See what's possible with Arcade. |
| Resources / Changelog | `/changelog`. Subtitle: New releases and improvements. |
| Resources / Knowledge Base | `https://docs.arcade.software/kb/ai-video`. Linked. Not opened. Subtitle: Look up features and find answers. |
| Enterprise | `/enterprise` |
| Log in | `https://app.arcade.software/auth`. Wall. Branch stopped. |
| Sign up | `https://app.arcade.software/auth`. Same wall. Not followed a second time. |

A second "Open app" link also points at `https://app.arcade.software/auth`. Not followed.

## Header, phone (390)

The bar collapses to the logo and a menu button. Opened in [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Close is the same control (accessible name "Menu Close"). Product and Resources are buttons that expand the same destinations as the desktop dropdowns. Log in and Sign up sit in the drawer and both point at the auth wall. Not followed from the phone.

## Homepage body

URL stays `/` unless noted. Photographed in [home-light-default.png](screenshots/home-light-default.png).

| Control | Result |
|---|---|
| Sign up for free | `https://app.arcade.software/auth`. Wall. Not followed. |
| Open Arcade (plus) | Same auth wall. Not followed. |
| Create video from prompt | Button. No href. Not pressed. A press can start a generation. |
| Launch video, Changelog, Talking head, How-to tutorial, Article to video | Buttons. URL stays `/`. They write a prompt chip. One chip (Launch video) was clicked. Photographed in [home-light-suggestion.png](screenshots/home-light-suggestion.png). Nothing was submitted. |
| Explore examples | `/ai-video-examples` |
| Play cards (MagicPath Team Accounts, Lovable Launch Film, Cursor 2.0 Launch, Kong AI Cost Management Launch, Moonmap: Manage to Profitability, The Self-Driving Company) | `https://cdn.arcade.software/mp4s/<id>.mp4`. Linked. Not opened. |
| Get started | Auth wall. Not followed. |
| Install Extension | Chrome Web Store. Linked. Not opened. |
| Connect Arcade | `/agents` |
| Explore Apps | `/apps` |
| Previous quote, Next quote | Anchors to `/`. URL stays. Next was clicked. Photographed in [home-light-quote-next.png](screenshots/home-light-quote-next.png). |
| Sign up (pre-footer) | Auth wall. Not followed. |
| Talk to sales | `/contact-sales` |

No homepage search. No locale switch. No theme switch.

## Footer

| Control | Opens |
|---|---|
| Logo | `/` |
| AI Videos | `/` |
| Enterprise | `/enterprise` |
| Pricing | `/pricing` |
| Chrome Extension | Chrome Web Store. Linked. |
| Interactive Demos | `/product/interactive-demo` |
| Blog | `/blog` |
| Changelog | `/changelog` |
| Knowledge Base | `https://docs.arcade.software/kb/ai-video`. Linked. |
| Community | Slack invite. Linked. The invite token is not recorded. |
| Careers | `/careers` |
| Brand | `/brand` |
| Security | `/security` |
| Status | `https://arcadehq.statuspage.io/`. Linked. |
| Legal | `/terms-of-service` |
| Privacy Policy | `/privacy` |
| X, LinkedIn, Instagram, TikTok | Off-site social. Linked. Not opened. |
| Ask AI row (ChatGPT, Claude, Perplexity, Gemini, Grok) | Off-site. Linked. Not opened. Not an Arcade identity provider. |
| Copy Wordmark, Copy Logo | Buttons. Not pressed. |
| More brand assets | `/brand` |

## Public pages opened from the tree

Each loaded signed out. Screenshots are named in [login-review.json](login-review.json).

| Path | Result |
|---|---|
| `/pricing` | HTTP 200. FAQ row opened in place. Plan CTAs that point at auth were not followed. |
| `/product/interactive-demo` | HTTP 200. Signup and URL-to-demo actions were not submitted. |
| `/agents` | HTTP 200. |
| `/apps` | HTTP 200. |
| `/enterprise` | HTTP 200. |
| `/ai-video-examples` | HTTP 200. |
| `/blog` | HTTP 200. Post links were linked, not opened. |
| `/changelog` | HTTP 200. |
| `/contact-sales` | HTTP 200. Fields were empty. Placeholders are a sample first name, last name, and work email. Nothing was typed. Submit and the captcha were not used. Photographed in [contact-sales-light-default.png](screenshots/contact-sales-light-default.png). |
| `/careers` | HTTP 200. Application forms not opened. |
| `/brand` | HTTP 200. |
| `/security` | HTTP 200. |
| `/privacy` | HTTP 200. |
| `/terms-of-service` | Linked. Not photographed. The page prints a street address and a contact email. |

## Walls, stopped

`https://app.arcade.software/auth` is the destination of Log in, Sign up, Sign up for free, Open Arcade, Open app, and Get started. Opened once from a direct load. Photographed empty in [login-light-empty.png](screenshots/login-light-empty.png) and [mobile-login-light-empty.png](screenshots/mobile-login-light-empty.png). No email, password, or code was typed. Google, Apple, and any other identity provider were not clicked. No form was submitted. The branch stopped there.
