# Lemonade public site tree

Mapped from https://www.lemonade.com/ on 2026-11-21, signed out. The request returned a live marketing site. The title was "Lemonade: An Insurance Company Built for the 21st Century". This is the insurance company, not Lemon Squeezy.

There is no theme switch. `color-scheme` on the root was `normal`. The `theme-color` meta tag was `#ffffff`.

No email was typed. No password was typed. No quote answer was typed. No form was submitted. No identity provider was clicked. The quote chat was opened and not answered. Checkout and bind-a-policy were not opened.

Headless Playwright received a Cloudflare "Just a moment..." page (HTTP 403, `cf-mitigated: challenge`). The captures below came from a real Chrome window that had already passed that check, driven over its debugging port at CSS 1440 by 900 and 390 by 844.

## Header at 1440

The wordmark sits in the center. Six product links sit on the left. My Account sits on the right. After the first scroll, Check our prices appears as a pink button on the right. There is no desktop flyout on the product names. Each name is a link.

A button labelled "Open the menu" is in the DOM at desktop width. Its box was 0 by 0, so it was not clicked there.

| Control | Opens | Stop? |
|---|---|---|
| Renters | `/renters` | |
| Homeowners | `/homeowners` | |
| Car | `/car` | |
| Pet | `/pet` | |
| Life | `/life` | |
| Giveback | `/giveback` | |
| Lemonade Insurance (wordmark) | `/?f=1` | |
| My Account | `/login` | Stop. Empty email field. Log in was not pressed |
| Check our prices | `/onboarding/start`, which redirects to `https://chat.lemonade.com/initial/flow` | Stop. The chat started. Yes and No were not pressed |
| Skip to main content | In-page skip link | |

## Phone drawer at 390

The product names collapse. "Open the menu" is a 30 by 30 button at the top left. Clicking it opens a dark drawer over the homepage. The drawer is 280 CSS px wide. Closing it is the X at the top right. The rows were not followed.

| Item | Opens |
|---|---|
| Renters | `/renters` |
| Homeowners | `/homeowners` |
| Car | `/car` |
| Pet | `/pet` |
| Life | `/life` |
| Giveback | `/giveback` |
| My Account | `/login` |
| Lemonade Facebook | `https://www.facebook.com/Lemonade/` |
| Lemonade Instagram | `https://instagram.com/lemonade_inc` |
| Lemonade X | `https://x.com/lemonade_inc` |

## Footer

The footer is a dark band of link columns. Products, resources, features, and company are disclosure buttons in the markup. On this visit they were already expanded in the footer text, not a dialog.

| Column | Opens |
|---|---|
| Products | The five product pages, plus their hubs and a few explained articles |
| Resources | `/blog/`, `/faq`, `/availability`, `/insuropedia/`, `/sitemap` |
| Features | `/claims`, `/agentic`, `/api`, `/policy-two` |
| Company | `/insurance-agents`, `/vets`, `https://makers.lemonade.com/`, `/partners-program`, `https://investor.lemonade.com/`, `/transparency`, `/reviews` |
| Legal | `/terms-of-service`, `/telematics-terms-and-conditions`, `/legal-stuff`, `/privacy-policy`, `/accessibility` |
| App stores | Apple and Google Play one-link URLs. Not opened |
| Select your language | A menu of country and language rows. United States, Germany, Netherlands, France, United Kingdom. No row was chosen |

Social icons in the footer point at Facebook, X, Instagram, LinkedIn, YouTube, and TikTok. Those sites were not opened.

The footer also prints a public phone number and a public office address. That region was not committed as a screenshot.

## Pages photographed

| Page | URL | Notes |
|---|---|---|
| Home | `https://www.lemonade.com/` | Desktop viewport, price cards, CTA hover, phone viewport, phone drawer |
| Renters | `/renters` | Desktop sheet and phone viewport |
| Homeowners | `/homeowners` | Desktop sheet |
| Car | `/car` | Desktop sheet |
| Pet | `/pet` | Desktop sheet |
| Life | `/life` | Desktop sheet |
| Giveback | `/giveback` | Desktop sheet |
| FAQ | `/faq` | Desktop sheet. Help is public here |
| Claims | `/claims` | Desktop sheet. How claims work, not a filed claim |
| Quote start | `/onboarding/start` | Redirects to the chat. Photographed while it was still typing. Stopped |
| Login | `/login` | Empty email field. Log in disabled-looking until an address is entered. Nothing typed |

`/signup` and `/register` returned 404. There is no separate public signup page. Account creation was not hunted past those two URLs.

## Stops

| Control | Why it stopped |
|---|---|
| My Account / Log in | Email wall. Field left empty. Button not pressed |
| Check our prices / quote chat | Quote answers would have been typed. Yes and No were not pressed |
| Language menu | Opened, then not chosen. The screenshot was discarded because the footer behind it shows a public phone number and a street address |
| Cookie banner | Hidden with CSS. Accept, reject, and Manage Cookies were not clicked |
| App store, investor site, social | Leave the marketing site |
