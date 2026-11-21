# Wynde site tree

Mapped 2026-11-21 from the public marketing site at https://wynde.io/. Desktop viewport measured 1440 by 900 CSS pixels at devicePixelRatio 1. Phone shots used a 390 by 844 CSS viewport at devicePixelRatio 2, with a desktop user agent, so the phone chrome is the narrow layout, not a device-class page. One light theme (`color-scheme: normal`). `prefers-color-scheme: dark` left the page white. No theme control.

No cookie dialog appeared. No form was submitted. No email, password, code, phone, or address was typed. Identity providers were not clicked. The signed-in app was not entered.

The site is one marketing page plus two legal pages. Features and Pricing are in-page anchors, not separate routes. There is no product catalog, no drawer beyond the phone menu, and no dialog.

## Shell (desktop, 1440)

The header is sticky. The wordmark is a text logo, left. Nav links sit right.

| Control | Opens |
|---|---|
| Wordmark | https://wynde.io/ |
| Features | same page, `#features` |
| Pricing | same page, `#pricing` |
| Watch demo | https://app.arcade.software/share/rr8wqodaSjSohYuDoMDf (external product tour). Not followed |
| Log in | https://app.wynde.io/, which redirects to https://app.wynde.io/login. Login wall. Branch stopped |
| Get started for free | the same login wall. There is no separate signup page |

## Home https://wynde.io/

A long page. Sections, in order, from the DOM:

| Section | What it is | Control |
|---|---|---|
| Hero | "Take the guesswork out" on a blue-grey wash, plus a product illustration | Get started for free (login wall), Book a demo |
| Logo marquee | customer logos, auto-scrolling | none |
| Methods | "Create your perfect research study in minutes" and a method list | none |
| Builder | illustrated study builder | none |
| Audience | green band, respondent pricing comparison | none |
| Reports | navy band, report features | none |
| Quotes | two customer quotes and a G2 score | G2 link https://g2.com/products/pathway-pathway/reviews. Not followed |
| Trust | GDPR, SSO, security copy | none |
| Pricing | `#pricing`. Three cards and an Annual discount switch | Contact sales has no href. The switch was not toggled |
| Close | "Great decisions start with your users" | Get started for free (login wall) |
| Footer | copyright, social, legal | see Footer |

| Control | Opens |
|---|---|
| Book a demo | https://meetings-eu1.hubspot.com/sergey-timofeev/wynde-demo. External scheduler. Not followed. Not submitted |
| Annual discount | painted switch on the same page. Left at rest. Not toggled |
| Contact sales | a pill with no href. Not clicked |
| Open Intercom Messenger | third-party chat launcher. Not opened |

## Footer

| Control | Opens |
|---|---|
| LinkedIn icon | https://www.linkedin.com/company/wynde/. Not followed |
| X icon | https://x.com/wynde_uxr. Not followed |
| Terms of Service | page https://wynde.io/terms-of-service |
| Privacy Policy | page https://wynde.io/privacy-policy |

## Legal pages

| Page | What it shows |
|---|---|
| https://wynde.io/terms-of-service | "Terms of Service", last updated 16 Feb 2024. Long Inter text. No form, no nav |
| https://wynde.io/privacy-policy | "Privacy Policy", last updated 16 Feb 2024. Same layout. No form |

## Phone (390)

The desktop nav hides. The header is the wordmark and a 32 px menu button.

| Control | Opens |
|---|---|
| Menu button | a white panel on the same page, 390 by 271, fixed. Close (x) returns to the same page |
| Features, in the panel | `#features` |
| Pricing, in the panel | `#pricing` |
| Watch demo, in the panel | the Arcade tour. Not followed |
| Log in, in the panel | login wall. Not followed from this width |
| Get started for free, in the panel | login wall. Not followed from this width |

## Missing route

https://wynde.io/this-page-does-not-exist-wynde-9f3a returns HTTP 404. The page is Framer's empty state: "Page not found", "This page doesn't exist or has moved.", and Back to home. Title "Page Not Found | Framer". It is not a Wynde layout.

## Login wall (recorded, not entered)

Log in and Get started for free both open the same wall. There is no separate signup route.

| URL | What loaded |
|---|---|
| https://app.wynde.io/ | redirects to https://app.wynde.io/login. Heading "Sign in to Wynde". Empty email field ("Enter your email here"), Continue, Sign in with Google. Footer: Contact us (`mailto:hi@wynde.io`), Terms of Service, Privacy Policy. Branch stopped. Nothing typed. Continue not clicked. Google not clicked |
| https://app.wynde.io/signup | "Failed to load data" and Try again. Not a signup form. Try again was not clicked |
| https://app.wynde.io/sign-up, /register, /join | the same "Failed to load data" page |

No theme switch exists on the public site or on the login wall.
