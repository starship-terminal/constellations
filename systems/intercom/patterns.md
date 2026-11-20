# Intercom patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

Three surfaces share the one brand system. **www.intercom.com** (the marketing site — Next.js + Tailwind v4, `body.theme-light`) carries the main design layer: `--color-*` ramps, the `--text-*` type scale, the `--button-*` state matrix and the `.theme-light` nav roles on `:root`, plus the `.brand-i2y4` campaign palette. **intercom.com/help/en/** (the help center) is a separate white-ground shell that still carries the shared styles. **intercom.com/changes/en** (the changelog) is the older `header__lite` surface running the `.intercom-legacy` palette and the MediumLL/IvoryLL/DmMono faces.

## The marketing shell

Every marketing page hangs off the fixed **shared header** (`header.shared-header`, `promo-banner` + `header`, 108 tall on home where the banner mounts, 66 elsewhere): the Fin 4 promo row on `rgb(225, 226, 229)`, then the white nav bar — the **wordmark** (`logo`), the Product/Customers/Resources **mega-menu triggers** (`nav-item`, 40 tall, radius 6, chalk `--color-nav-background-highlight` fill on hover), the Pricing **link** (`nav-link`), then Log in, Contact sales, View demo links and the black **"Start free trial" CTA** (`nav-cta`, the `--button-primary-*` matrix: #111 resting, helpdesk #0007cb on hover, the same blue at 85% pressed). The Product trigger opens the **mega-menu**. The page screenshot is `home-light-nav-menu`. The component reading is a gap: the saved measurement hit a hidden switch-card, not the open panel.

## The home grammar

The home page sets the pattern the product pages repeat: a Saans **hero title** (`hero-title`, text-heading-2 — 64/64 at 1440, stepping to 80 at 1920, 48 at 1024, 40 at 390), a pair of actions — the black **primary CTA** (`hero-cta`) beside a bordered **secondary link** (`hero-secondary`, 1px off-black ring, radius 4) — then full-bleed sections on the cream ground (`--body-bg` = `--color-cream`): the **eyebrow label** (`eyebrow`, SaansMono 12/12, +0.6px tracking, uppercase), the **section titles** (`section-title`, text-heading-3), and **feature cards** (`feature-card`, radius 14 on a black/6 ring) in a centred ~1164 px column. The **footer** (`footer`, `footer-link`, `locale-select`) is a 578 px link grid ending in the legal row.

## Pricing

`/pricing` leads with the billing segmented control (**billing-toggle** — the selected "Billed annually" half fills with `--color-canvas`), the helpdesk-blue **promo badge** (`promo-badge`, `--color-helpdesk` text on its 15% tint, 2px radius) and the **plan columns** (`plan-card` — the @container cells themselves paint nothing; the plan name, "Includes Fin AI Agent" list and the CTA sit inside them). The **FAQ accordion** (`faq-item`) is a 20px question row that expands its answer on its own press — captured `pricing-light-faq`.

## The contact-sales form

`/contact-sales` is a one-screen first step: the **form** (`form`) holds **labels** (`input-label`, 14px), the Business Email **text field** (`input`, off-white `--color-off-white` fill, black/20 ring, 2px radius, 40 tall), the company-size **select** (`select`, same field chrome) whose own press opens the **listbox** (page screenshot `contact-sales-light-select-open`, no option chosen; the component reading is a gap because the saved measurement was a 0x0 listbox), the opt-in **checkbox row** (`checkbox`, never ticked) and the full-width **Next** button (`next-button`) — measured with forced pseudo states only, never pressed, so the form was never advanced. The one `filled` reading typed `name@example.com` and deleted it on the spot; nothing was sent.

## The help center and changelog

`/help/en/` is the docs shell: its own 60 px white header (**help-header**, **help-search** — focused once, nothing typed), the IvoryLLSub-Light **hero** ("Great service changes everything.", 60/67 at 1440), **article cards** (`help-card`) and the **docs nav** (`help-nav`). `/changes/en` is the release feed on `#f3f5f7`: a 147 px `header__lite` header, then a 900 px column of `div.paper.newsfeed__newsitem` **entry cards** (`changes-entry`, white, 4px radius) in the legacy MediumLL-era styling.

## Mobile (390 wide)

The header collapses to the wordmark plus the **menu button** (`m-menu-button`, `aria-label="Open navigation menu"`, a 40px icon button); its press opens the full-height **menu sheet**. The page screenshot is `mobile-home-light-menu`. The component reading is a gap: the saved measurement was a demo form, not the navigation sheet. The hero steps down through the declared `--text-heading-*-mobile` sizes (`m-hero`).

## Motion and focus

The site's default is `--default-transition-duration` 150 ms on `--default-transition-timing-function` (`cubic-bezier(.4, 0, .2, 1)`); the declared `--ease-*` set is the full Penner library. Measured on components: buttons and nav rows repaint inside that 150 ms window, menu panels take longer transforms. The reduced-motion probe ([raw/motion.json](raw/motion.json)) records a **partial** reduced-motion story — most pages keep transitions under `prefers-reduced-motion`; only some are removed. The declared focus token is `--color-focus-outline` (`--color-blue` #000ce1). The captured keyboard rings are black (`#101010`) on the desktop controls and orange (`#e59700`) on the mobile menu button.

## The boundary beyond the signed-out surface

This package documents the public product, not the account. **app.intercom.com** (the real product behind Log in), **/signup** trial onboarding, the checkout, and the later steps of the contact-sales form were never entered: Log in and Start free trial were measured, never followed; Next was measured, never pressed; the marketing checkbox was never ticked; nothing was searched, chosen, uploaded or sent.
