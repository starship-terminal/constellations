# Dock patterns

How the captured components combine on each public surface. Crops and values are in [components.md](components.md); every number's provenance is in [raw/measurements.md](raw/measurements.md).

## The chrome

Every desktop marketing page opens with the same `<dock-site-header>` — a custom element whose shadow root paints a **white 70px bar** (1328px inner container at 1440). Inside: the dock wordmark, a **Product** `<summary.nav-trigger>` (38px, DockWebflowNavigation 14px/20px 500, ink #121722), then plain **Pricing** and **Customers** links, a **Resources** trigger, a spacer, **Log in** text link, a white **Request demo** pill (0.5px inset hairline ring, 100px radius) and the blue **Start for free** pill (#0068f9, 100px radius). At 390px the same bar is 76px with a single `summary.navigation-toggle` menu button.

On home, the header sits on the page's top edge over the deep-blue hero; on interior pages it sits over white with a #dedfe3 bottom hairline.

## The Product mega-menu

Clicking a nav `<summary>` opens `div.menu-viewport` — a **19px-radius painted panel** (258px tall for Product) containing `summary.menu-group-toggle` group headings and `a.menu-link` rows (8px radius, ~#f8f8f9 hover wash). The menu auto-closes; measurement re-opens it per state. Menu groups carry DockWebflowNavigation 500 titles with small square icon blocks.

## The hero

Home's hero is the signature surface: the **#002fa6 deep-blue band** (a painted oklch gradient, `page-placeholder`/`hero-intro` layers) with a **62px/70.4 white display** (DockWebflowHome 600), white subtitle, then two CTAs side by side — the blue **Start for free** pill and a **ghost Request-demo** (transparent, white text, sky #4db5ff-ish inset ring at 40% alpha, white-alpha hover/pressed washes). Below the band, white sections alternate with #f7f7f8 washes, each anchored by a h2 (~40-48px, DockWebflowHome 600).

The mobile hero compresses the same structure: 29.25px/34.375 display, CTAs stacked.

## Pricing

`/pricing` paints Roobert (not the Webflow faces): a **60px/64 h1**, the sub-copy, then **four plan columns** — Free / Standard / Premium / Enterprise — each a column with a price block, feature list and a 40px 100px-pill action (white-outlined for most plans, blue for the popular **Premium** column, which sits on a #f7f7f8 fill with 12px top radii). A sticky `.pr-sticky` summary bar pins beneath the header while scrolling (its CTA clone is excluded from plan-cta measurements). Below: the feature-comparison table and a `details`-based **FAQ** — `summary` rows whose `opened` state flips the disclosure.

## Marketing index pages

`/customers`, `/library`, `/templates` share one pattern: a **page h1** (70px/72px customers, 38px/44px templates), a **filter-pill bar** (`filter-radio` — white pills with hairline, the active one painting #d5ecff blue tint), then a **card grid** of customer-story / resource / template cards (white, hairline ring, ~16px-ish radii) with imagery, a small heading and a link. `/customers` adds a stats band with 700-weight Roobert numbers.

## Product and solutions pages

`/product/dock-ai` and `/solutions/sales` follow the home grammar: white sections, deep-blue islands for emphasis, the same pill CTAs. Product pages carry a left **sidebar nav** (`sidebar-link` rows) through their feature sections.

## The demo page

`/demo` is the biggest type on the site — an ~80.6px/84.3 display (Roobert 600) — above a two-column layout: copy/testimonial left, a **HubSpot form in an iframe** right (`demo-field` inputs, 6px radius, hairline; `demo-submit` button). The form is the only public form; it was measured, never filled or submitted.

## The auth cards

auth.dock.us runs a separate Chakra application. `/login` centres a white card on a light radial field: Roobert 14px controls, the **subdomain field** (`subdomain-field`, 4px radius, `#dedfe3` border, `.dock.us` suffix span) and the **#4058ff Continue** (`continue-btn`, 4px radius, full width). `/sign-up` adds a **deep-blue testimonial pane** (#242d7d→#3542af gradient, white text) beside the card, OAuth provider buttons, an email field, the signup submit and the 1px Turnstile placeholder.

## The footer

A light footer across marketing pages: wordmark, `footer-link` columns (Product / Solutions / Resources / Company), trust badges (SOC 2, GDPR — 12.5px/15), and the legal hairline row. Ink text on white, DockWebflowNavigation.

## Mobile

At 390px: the header collapses to the single `summary.navigation-toggle`; opening it paints `div.navigation-content` — a **386px panel** with `m-nav-item` accordion rows (group summaries + child links). Pages keep their sections at mobile measures; pricing columns stack.
