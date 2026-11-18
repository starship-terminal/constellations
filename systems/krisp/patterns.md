# Krisp patterns

Public marketing patterns from krisp.ai on 2026-11-18, plus the signed-in free-account app on app.krisp.ai the same day.

## Header

A 73px white bar. Wordmark at the left, product menus (AI Meeting Assistant, Call Center AI, Developers), Customers, Pricing, then Sign in as text, Book a demo as an ink pill, Get Krisp as an indigo pill. See [home-light-default](screenshots/home-light-default.png).

Hovering a product name opens a white mega-menu with a featured card and two columns of links. The page behind it blurs. See [home-light-nav-menu](screenshots/home-light-nav-menu.png).

On a 390px width the menus collapse to a `.burger` at the right of the wordmark. See [mobile-home-light-default](screenshots/mobile-home-light-default.png) and [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Hero

Left column: a "New" pill, a 52px Plus Jakarta Sans headline with "Voice AI" in a blue-to-indigo treatment and the rest in ink, a two-line lede, and a Get Krisp pill. Right column: a product illustration (a meeting UI), which is marketing art, not the app. See [home-light-default](screenshots/home-light-default.png).

## Pricing

Audience tabs (Meeting AI, Call Center AI, Developers) sit above the title. A Monthly / Annually pill switches the prices; Annually shows a Save 50% badge. Four cards in a row: Free Trial, Core, Advanced (indigo border, Most popular badge, ink CTA), Enterprise (Talk to Sales). See [pricing-light-default](screenshots/pricing-light-default.png) and [pricing-light-monthly](screenshots/pricing-light-monthly.png).

## FAQ

A centred question list. Opening a row reveals the answer under the question and swaps the control to a close mark. See [home-light-faq-open](screenshots/home-light-faq-open.png).

## Footer

Link columns for products, company and legal, including Cookie settings. Cookie settings was not clicked.

## App shell

A left sidebar: product switcher (Meeting Assistant), Invite teammates, Search, Noise Cancellation, Accent Conversion, Note Taker with My Notes / Shared with me / Action Items, Create folder, then settings/download/bell and the account chip. The notes canvas is a welcome banner plus an empty-state card. Upgrade sits top-right and was not pressed. Light: [app-notes-light-default](screenshots/app-notes-light-default.png). Dark: [app-notes-dark-default](screenshots/app-notes-dark-default.png). Phone: hamburger plus Upgrade. [mobile-app-notes-light-default](screenshots/mobile-app-notes-light-default.png).

## Settings

A nested vertical list (Account, Workspace, Meeting Assistant, App Behavior) and a content column of fields, switches, radios and outline buttons. Delete my account is a red fill. [app-settings-account-light-default](screenshots/app-settings-account-light-default.png). Appearance is Light / Dark / System; System was left as found. [app-settings-app-light-default](screenshots/app-settings-app-light-default.png).

## Billing (free)

Free plan at US $0 /per month, a Core upsell banner, seat management, no payment method. Upgrade was not pressed. [app-billing-light-default](screenshots/app-billing-light-default.png).

## Onboarding gates

`/setup` asks to download the desktop app. [app-setup-light-default](screenshots/app-setup-light-default.png). Phone `/setup` says continue on desktop. [mobile-app-setup-light-default](screenshots/mobile-app-setup-light-default.png). Connect calendar offers Google and Outlook and a Skip; neither calendar was connected. [app-connect-calendar-light-default](screenshots/app-connect-calendar-light-default.png). Action Items opens a Core paywall dialog. [app-action-items-light-default](screenshots/app-action-items-light-default.png).

## What is not a pattern here

- Recordings and `/meetings`: they redirect to `/setup` on this free account.
- Calendar OAuth, Upgrade checkout, desktop download, Delete account, Enable 2FA.
- Forms and validation on https://krisp.ai/contact-sales/. Not submitted.
- Help centre at https://help.krisp.ai/hc/en-us.

## Marketing shell

The public shell is the header, the hero, a content band and the footer. It is the same on home, pricing, product, customers, about, security, blog and careers. See [home-light-full](screenshots/home-light-full.png).
