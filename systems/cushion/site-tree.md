# Cushion public site tree

Mapped from the homepage at https://cushion.so/ on 2026-11-21, signed out, before any screenshot in this refresh. The marketing site is cushion.so. The app is a separate host, app.cushion.so. Booking is cal.com. Status is cushion.openstatus.dev. Follow us leaves the site for x.com.

Nothing was submitted. No identity provider was clicked. No email, password, phone, or code was typed.

Homepage title: "Cushion | Workplace communication for distributed teams". Headline: "Work messaging that keeps your team organised".

No cookie dialog rendered on load. No captcha wall rendered. The site is not parked.

## Desktop nav (1440)

Sticky nav, 72px, no hamburger. Logo, three page links, then Log in and Sign up.

| Control | Opens |
|---|---|
| Logo (`a[aria-label="Cushion"]`, href `/`) | Homepage, https://cushion.so/ |
| Pricing | Page, https://cushion.so/pricing |
| Updates | Page, https://cushion.so/updates |
| Blog | Page, https://cushion.so/blog |
| Log in | Login wall, https://app.cushion.so/login. Stop. |
| Sign up | Signup wall, https://app.cushion.so/sign-up. Stop. |

The nav has no dropdown menu. Pricing, Updates, and Blog are pages, not menus.

## Homepage body

The inbox, channels, and posts on the homepage are a public demo labelled Acme Inc. Their buttons stay on the same page. They do not open the signed-in app.

| Control | Opens |
|---|---|
| Get started (hero and closing band) | Signup wall, https://app.cushion.so/sign-up. Stop. |
| Talk to a human | External booking page, https://cal.com/cushion/30min. Not opened. |
| New post, Inbox, Search, channel rows, direct-message rows, Save draft, Post | Same page. Demo chrome inside the mock. Not a dialog. Not clicked through to the app. |
| Ashley John · Founder, OYNK | External page, https://oynk.co.uk/. Not opened. |
| FAQ: How's this different from Slack, Discord, Teams? | Same page. Accordion, `aria-expanded`. Not a dialog. |
| FAQ: I've been burnt switching apps before. How stable are you? | Same page. Accordion. |
| FAQ: Have you got a mobile app? | Same page. Accordion. |
| FAQ: How much does it cost? | Same page. Accordion. |
| FAQ: Who's behind Cushion? | Same page. Accordion. |
| hey@cushion.so | mailto:hey@cushion.so. Not opened. |

## Theme

A 36px button labelled Toggle theme sits in the page footer, next to the wordmark. It is a public control, not an account setting.

| Control | Opens |
|---|---|
| Toggle theme | Same page. Adds `class="dark"` on `<html>`. Page background goes from rgb(245, 245, 245) to rgb(18, 18, 18). A second click removes the class. Not a menu or dialog. |

## Footer (same on the mapped marketing pages)

| Column | Control | Opens |
|---|---|---|
| Product | Pricing | https://cushion.so/pricing |
| Product | Download | https://cushion.so/download |
| Product | Integrations | https://cushion.so/integrations |
| Product | Blog | https://cushion.so/blog |
| Product | Updates | https://cushion.so/updates |
| Use cases | Async slack alternative | https://cushion.so/slack-alternative |
| Use cases | Discord alternative for teams | https://cushion.so/discord-alternative |
| About | Privacy | https://cushion.so/privacy |
| About | Terms | https://cushion.so/terms |
| About | Contact | https://cushion.so/contact. Public form. Do not submit it. |
| About | Status | External page, https://cushion.openstatus.dev/. Not opened. |
| Brand | Follow us | External page, https://cushion.so/follow redirects to https://x.com/usecushion. Not photographed. |
| Brand | Toggle theme | Same page. Theme class, as above. |

## Phone nav (390)

The band shows the logo and a 32px button with `aria-expanded="false"`. Pricing, Updates, Blog, Log in, and Sign up are not in the bar.

| Control | Opens |
|---|---|
| Logo | Homepage |
| Menu button (unlabelled, top right) | Dialog, `role="dialog"`, `data-state="open"`. Text: Close, Pricing, Updates, Blog, Log in, Sign up. |
| Dialog: Close | Same page. Closes the dialog. |
| Dialog: Pricing | Page, https://cushion.so/pricing |
| Dialog: Updates | Page, https://cushion.so/updates |
| Dialog: Blog | Page, https://cushion.so/blog |
| Dialog: Log in | Login wall, https://app.cushion.so/login. Stop. |
| Dialog: Sign up | Signup wall, https://app.cushion.so/sign-up. Stop. |

## Walls (not entered)

| Control | What is on the other side |
|---|---|
| Log in | https://app.cushion.so/login. Photographed, then stopped. Email field and "Send me a login link" were not used. Continue with Google was not clicked. |
| Sign up / Get started | https://app.cushion.so/sign-up. Photographed, then stopped. Email field and Continue were not used. Continue with Google was not clicked. |

Login offers: Continue with Google, an email field ("Enter your email"), Send me a login link, Terms of Service, Privacy Policy. Signup offers: Log in, Continue with Google, an email field, Continue, Terms of Service, Privacy Policy. No Apple button. No password field. No captcha on either wall.

## Pages linked from the homepage, mapped and not all photographed

| Page | What it adds |
|---|---|
| https://cushion.so/pricing | One plan, $8/mo/user. Get started is a button on this page (it does not navigate in the DOM). "More than 20 members? Contact us" is a link to https://cushion.so/contact. FAQ accordion, nine questions, including ones the homepage does not list. |
| https://cushion.so/updates | Changelog. Contact us link to /contact. |
| https://cushion.so/blog | Category links: All posts, Remote work, Productivity, Tools. Post cards link to /blog/<slug>/. |
| https://cushion.so/download | "Download for Apple Silicon" links to https://cushion.so/download/mac. Not clicked, so no file was saved. |
| https://cushion.so/integrations | Learn more links to /integrations/github/, /integrations/slack/, /integrations/stripe/. |
| https://cushion.so/contact | Form: name, work email, company, message, Submit. Not submitted. |
| https://cushion.so/privacy | Links to https://cushion.so/sub-processors. |
| https://cushion.so/slack-alternative and /discord-alternative | Same nav, hero CTAs, and demo chrome as the homepage. |

## Pages photographed from this tree

Desktop: homepage light, homepage dark, one FAQ open, pricing, updates, blog, one blog post, download, integrations, contact (form empty, not submitted), slack alternative. Phone: homepage, open menu. Walls: login, signup.
