# Pitch public site tree

Mapped from https://pitch.com/ on 2026-11-21, signed out, in headless Chromium at 1440×900. The painted theme stays light when `prefers-color-scheme` is dark. Log in and Sign up both open the same empty wall on auth.pitch.com. Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. A control that opens that wall is recorded and that branch stops.

`login-extracted` stays `not-started`.

## Shell

The marketing pages share one Framer nav. Desktop items are links that also open a hover menu. Pricing is a link with no menu. The phone width (390) replaces the centre links with a round menu button.

| Control | Opens | Stop? |
|---|---|---|
| Logo | `/` | |
| Product | Hover menu, and `/product` on click | |
| Use Cases | Hover menu, and `/customer-stories` on click | |
| Templates | Hover menu, and `/templates` on click | |
| Resources | Hover menu, and `/blog` on click | |
| Pricing | `/pricing` | |
| Log in | auth.pitch.com login wall | yes, login wall |
| Sign up | same wall, signup copy | yes, signup wall |
| Banner "See what's new" | `/blog/an-mcp-for-decks-worth-sending` | public post |
| Banner close | Hides the promo strip | local |

## Product menu

Hover on Product. Escape or moving away closes it. [screenshots/nav-product-menu.png](screenshots/nav-product-menu.png)

| Item | Opens |
|---|---|
| Product overview | `/product` |
| What's new | `/whats-new` |
| Pitch MCP & API | `/mcp` |
| Integrations | `/integrations` |
| Download | `/download` |
| Status | `https://status.pitch.com/` (external status page) |

## Use Cases menu

[screenshots/nav-use-cases-menu.png](screenshots/nav-use-cases-menu.png)

| Item | Opens |
|---|---|
| Customer stories | `/customer-stories` |
| Software companies | `/solutions/software-companies` |
| Sports & media | `/solutions/sports-and-media` |
| Creative agencies | `/solutions/creative-agencies` |
| Leading brands | `/solutions/leading-brands` |
| Freelance designers | `/solutions/freelance-designers` |

## Templates menu

[screenshots/nav-templates-menu.png](screenshots/nav-templates-menu.png)

| Item | Opens |
|---|---|
| Presentation templates | `/templates` |
| Pitch decks | `/templates/collections/Pitch-deck` |
| Business | `/templates/collections/Business` |
| Sales | `/templates/collections/Sales` |
| Startups | `/templates/collections/Startups` |
| Professional | `/templates/collections/Professional` |
| Agency | `/templates/collections/Agency` |
| Portfolio | `/templates/collections/Portfolio` |
| Brand | `/templates/collections/Brand` |
| Creative | `/templates/collections/Creative` |
| Modern | `/templates/collections/Modern` |
| Project plan | `/templates/collections/Project-plan` |
| Proposal | `/templates/collections/Proposal` |
| Research | `/templates/collections/Research` |
| Strategy | `/templates/collections/Strategy` |
| Marketing | `/templates/collections/Marketing` |

## Resources menu

[screenshots/nav-resources-menu.png](screenshots/nav-resources-menu.png)

| Item | Opens |
|---|---|
| Blog | `/blog` |
| Customer stories | `/customer-stories` |
| Agentic workflows | `/workflows` |
| Presentation gallery | `/templates` |
| Help center | `https://help.pitch.com/en/` |

## Home interactions that stay on `/`

| Control | Opens | Stop? |
|---|---|---|
| More features | Popover: "Unlock more features. Attach files, pick a template, and apply your brand by signing up." No link inside it. | do not sign up from here |
| Prompts | Cycles the prompt placeholder. It does not open a menu. | do not type a prompt, do not press Generate |
| Generate | Would start a deck | not clicked |
| Sign up for free, Start creating | Signup wall | yes |
| Get a demo | `/demo` | public page, not submitted |
| See customer stories | `/customer-stories` | |
| Explore workflows | `/workflows` | |
| Browse templates | `/templates` | |

## Pricing

`/pricing` is public. Pay yearly and Pay monthly are a segmented pill on the same page. The seat slider stays on the page. Info buttons open tooltips (Member limit was opened). Plan buttons that say Get started or Choose Plus go to the signup wall and were not followed. [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) [screenshots/pricing-light-tooltip.png](screenshots/pricing-light-tooltip.png)

## Templates

`/templates` is a public gallery, not the signed-in editor. Search is a field plus a Search button. A query was not submitted. Collection chips go to `/templates/collections/<name>`. One collection, Pitch deck, was photographed. Generate presentation on a card was not clicked. [screenshots/templates-light-default.png](screenshots/templates-light-default.png)

## Footer

The footer is on the marketing pages. Groups are the labels as painted. One sample of each group was opened or confirmed public. The rest are mapped.

| Group | Items |
|---|---|
| Product | Product overview `/product`, What's new `/whats-new`, Pricing `/pricing`, Integrations `/integrations`, MCP & API `/mcp`, Agentic workflows `/workflows`, Customer stories `/customer-stories`, Presentation maker `/use-cases/presentation-maker`, AI Presentation maker `/use-cases/ai-presentation-maker`, Video presentation maker `/use-cases/video-presentation-maker`, Pitch vs PowerPoint `/pitch-vs-powerpoint`, Pitch vs Keynote `/pitch-vs-keynote`, Pitch vs Google Slides `/pitch-vs-google-slides`, Pitch vs Figma Slides `/pitch-vs-figma-slides`, Pitch vs Canva `/pitch-vs-canva`, Help center `https://help.pitch.com/en/`, Download `/download`, Status `https://status.pitch.com/` |
| Templates | Collection links under `/templates/collections/` (Pitch decks, Marketing, Startups, Design, Sales, Business, UX, Proposal, Report, Simple, Creative, Professional, Modern, Project plan, Project proposal, Portfolio, Brand, Product, Agency) |
| Legal | Terms of Use `/terms-of-use`, Privacy Policy `/privacy-policy`, Legal Notice `/legal-notice`, DPA `/dpa`, DMCA Policy `/dmca-policy`, ERDF Support `/erdf`, GDPR `/gdpr`, Security `/security`, Cookie Settings `/#cookie-settings` |
| Company | About `/about`, Blog `/blog`, Press room `/press`, Brand studio `/brand`, Careers `/jobs`, Affiliates `/affiliates` |
| Social | LinkedIn, TikTok, Instagram, YouTube, X (external) |
| Footer Log in / Sign up | Same auth wall. The footer markup builds an Auth0 URL with a state query. That URL was not opened and was not stored. |

## Auth walls

Photographed empty. Continue with Google, Continue with Apple, Single sign-on (SSO), and Continue with email and password were not clicked. The email field was left empty. The captcha checkbox was not clicked.

| Control | Opens | What it shows |
|---|---|---|
| Log in (nav) | auth.pitch.com `/login` | "We'll sign you in or create an account if you don't have one yet." Work email, Continue with email, Google, Apple, SSO. [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Sign up (nav) | Same wall | Same card, with a "Verify you are human" checkbox still empty. [screenshots/signup-light-default.png](screenshots/signup-light-default.png) |

The address bar on that wall carries an OAuth `state` query. Screenshots of the wall do not show the address bar. The capture sidecars store `https://auth.pitch.com/login#/` and drop the query. A direct open of `https://auth.pitch.com/login` with no client parameter is the public error page, not the wall.

## Empty and error

`/error.html` is a public error state: "Something went wrong, please try again." and Back to Home. [screenshots/error-light-default.png](screenshots/error-light-default.png)

## Phone

At 390px the nav collapses to the wordmark and a round menu button. Home and pricing were photographed at that width. The menu lists Product, Use Cases, Templates, Resources, Pricing, Log in and Sign up. Product inside the menu expands the same Product items. Log in and Sign up were not followed from the phone menu. [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png) [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) [screenshots/mobile-pricing-light-default.png](screenshots/mobile-pricing-light-default.png)

## Not entered

The signed-in deck at app.pitch.com, Google, Apple, SSO, the email-and-password step, captcha, checkout, demo request submit, and any URL that carries OAuth or session state. `login-extracted` stays `not-started`.
