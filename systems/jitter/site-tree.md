# Jitter site tree

Mapped 2026-11-21 from the public homepage at https://jitter.video/ before screenshots. Signed out. `body.animate`. One light theme (`color-scheme: normal`, `theme-color` `#FFFFFF`). No dark-theme control.

No cookie dialog was on the page. The Intercom launcher was hidden, not clicked. No password, email, or code was typed. No form was submitted. Google and SSO were not clicked.

jitter.video is the product. help.jitter.video, trust.jitter.video, Discord, YouTube, and social links leave the marketing site.

## Shell (desktop, 1440)

The header is a fixed bar. Product and Customers are links with `aria-haspopup="true"`. Hover opens a menu on the same page. A click on the label itself goes to that label's page.

| Control | Opens |
|---|---|
| Logo (`a[aria-label="Jitter Logo : Back to homepage"]`) | page https://jitter.video/ |
| Product (`a[href="/product/"][aria-haspopup="true"]`) | menu on the same page. The label's own href is https://jitter.video/product/ |
| Customers (`a[href="/customers/"][aria-haspopup="true"]`) | menu on the same page. The label's own href is https://jitter.video/customers/ |
| Templates | page https://jitter.video/templates/ |
| Pricing | page https://jitter.video/pricing/ |
| Log in | page https://jitter.video/login/. Login wall. Branch stopped. |
| Sign up | page https://jitter.video/join/. Signup wall. Branch stopped. |
| Open menu (`button[aria-label="Open menu"]`) | hidden at 1440. Visible at 390. |

### Product menu (hover, same page)

| Control | Opens |
|---|---|
| Import from Figma | page https://jitter.video/product/#figma-plugin |
| A brand-new way to design and animate | page https://jitter.video/product/#design |
| Unlock collaboration | page https://jitter.video/product/#collaborate |
| Export to 4K, GIF, Lottie | page https://jitter.video/product/#export |
| Template collection: Counters | page https://jitter.video/changelog/2026-11-17-counter-templates |
| Brand Kits (beta) | page https://jitter.video/changelog/2026-11-10-animated-brand-kits |
| Jitter Partners | page https://jitter.video/changelog/2026-11-03-jitter-affiliate-program |
| See what's new | page https://jitter.video/changelog/ |

### Customers menu (hover, same page)

| Control | Opens |
|---|---|
| How Perplexity brings their brand to life with Jitter | page https://jitter.video/customers/perplexity/ |
| How 27b uses Jitter to scale motion without slowing down | page https://jitter.video/customers/27b/ |
| How Deliveroo adds delight to their product with Jitter | page https://jitter.video/customers/deliveroo/ |
| Creative teams | page https://jitter.video/customers/#creative |
| Agencies | page https://jitter.video/customers/#agencies |
| Studios | page https://jitter.video/customers/#studios |
| See all customers | page https://jitter.video/customers/#customers |

## Home https://jitter.video/

| Control | Opens |
|---|---|
| Superagents pill ("Learn more") | page https://jitter.video/changelog/2026-07-09-ai-agents/ |
| Try Jitter for free | page https://jitter.video/join/. Signup wall. Not entered past the empty card. |
| Template tiles (The Track: Poster, and the rest of the strip) | public file pages `/file/?id=…`. Photographed one public example. Not edited. |
| Explore all the features / Explore all features | page https://jitter.video/product/ |

## Footer (every page)

Product: Product `/product/`, Import from Figma `/product/#figma-plugin`, Design `/product/#design`, Animate `/product/#animate`, Collaborate `/product/#collaborate`, Export `/product/#export`.

Templates: Templates `/templates/`, Community `/community/`, Devices `/templates/devices/`, Text animations `/templates/text/`, Logos `/templates/logos/`, Animated icons `/templates/icons/`, Charts `/templates/charts/`, Animated websites `/templates/websites/`, Buttons `/templates/buttons/`.

Resources: Pricing `/pricing/`, Changelog `/changelog/`, Figma animations `/figma-animation/`, Lottie animations `/lottie-animations/`, After Effects alternative `/after-effects-alternative/`, Jitter vs Figma Motion `/jitter-vs-figma-motion/`, Jitter vs After Effects `/jitter-vs-after-effects/`, Jitter for agencies `/jitter-for-agencies/`.

Company: Customers `/customers/`, Terms & conditions `/terms/`, Privacy policy `/privacy/`, AI Manifesto `/ai-manifesto/`, Contact sales `/contact-sales/`. Support is an in-page control (`href="/"`) that opens the Intercom launcher. It was not clicked.

Get started for free goes to `/join/`. Signup wall. Not submitted.

Leaves the site, not opened as product surfaces: Join our Discord, Documentation (https://help.jitter.video/), Tutorials (YouTube), Hire an expert, Trust Center (https://trust.jitter.video/), Careers (Notion), and the social icons.

## Phone (390)

The header keeps the logo, Log in, and Open menu. Product, Customers, Templates, and Pricing leave the bar.

| Control | Opens |
|---|---|
| Open menu (`button[aria-label="Open menu"]`) | drawer on the same page. Close menu (`button[aria-label="Close menu"]`) returns to the same page. |
| Product, Customers, Templates, Pricing | the same pages as desktop. No flyout inside the drawer. |
| Contact sales | page https://jitter.video/contact-sales/ |
| Log in | page https://jitter.video/login/. Login wall. |
| Sign up | page https://jitter.video/join/. Signup wall. |

## Login walls (recorded, not entered)

| Control or URL | What loaded |
|---|---|
| Log in, `/login/` | Page "Log in · Jitter". Continue with Google, Continue with SSO, Continue with email, an empty work-email field. Branch stopped. Google and SSO were not clicked. Email was not typed. |
| Sign up, Try Jitter for free, Get started for free, `/join/` | Page "Sign up · Jitter". The same three continue buttons and an empty email field. Not submitted. |
| `/file/?id=…` | Public template file. Photographed when it stayed signed out. Not edited. |
