# Huddlekit patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

Two surfaces carry the one system: **huddlekit.com** (the signed-out marketing site — a visual-annotation product for website feedback) and **app.huddlekit.com/login** (the only page the app serves anonymously). Both are Next.js apps on the same Tailwind v4 + shadcn-style semantic layer — the same custom-property names resolve to the same roles — while the marketing site adds its own page-wash and section tokens (`--color-page`, `--color-primary-dark`, `--section-padding`, `--section-gap`, `--card-gap`) and the app adds `--canvas` and `--mode-glow-strength`.

## The marketing chrome (light only)

Every huddlekit.com page shares one frame. An **announcement bar** (`announce-bar`, a centred ink-on-warm strip — "New: hand feedback to your AI agent over MCP") sits above a **header** (`nav-header`): the serif wordmark, the nav links (`nav-link` — Features, Pricing) and the two hover-open menus (`nav-menu-button` → `nav-menu-surface`: Solutions and Resources fly-outs), then a **Sign in** text link (`nav-signin`, to app.huddlekit.com/login — measured, never followed) and the small solid **Get started** CTA (`cta-outline`). The page closes on a **dark footer** (`footer` — the site's biggest `.dark` panel: near-black `--background`, white-alpha borders, a giant outlined wordmark) and a first visit paints the **cookie-consent banner** (`consent-banner`, a rounded card with Decline / Accept — Decline pressed once to dismiss, Accept never pressed); a **cookie settings** control (`cookie-settings`) re-opens it. On the phone the header compresses to a bar (`m-header`) with a "Toggle menu" button (`m-menu-button`) that opens the nav **drawer** (`m-nav-drawer`).

## The landing page

`/` ([full](screenshots/home-light-full.png)) stacks the product story on the warm `--color-page` wash (#f6f3f2) under white `--background` sections: a centred hero (H1 "The visual annotation tool for website feedback", the orange **Get started for free** `cta-primary` on `--primary` #ea580d, a "5-star reviews" star link) over a **dark product-demo card** — a mocked annotation widget on a greyed site (public demo imagery, not the signed-in app). Below, a **feature tablist** (`feature-tab`) swaps the demo panel (captured `home-light-feature-tab`), integration cards (`integration-card`), a wall of **dark testimonial cards** (`testimonial-card-dark` — the second `.dark` panel, behind a "Show more" toggle captured `home-light-testimonials-open`), the client-logo marquee, a **FAQ accordion** (`faq-question`, captured `home-light-faq-open`) and the dark footer.

## Pricing

`/pricing` ([full](screenshots/pricing-light-full.png)) is the standard marketing pattern: a monthly/annual **billing switch** (`billing-switch`, captured `pricing-light-billing-toggle`), three plan slabs (visible in the page shot; the `plan-card` measurement read the "Free forever" label and is marked missing, so no card radius is tokenised), each with its `plan-cta` button, a testimonial strip, a feature-comparison table, **compare-alternatives link cards** (`compare-link-card` → the /compare pages) and another FAQ accordion (`pricing-light-faq-open`), closing on the dark footer CTA.

## The dark panels

huddlekit.com has no theme control — but three components are painted `.dark` surfaces on the light page: the **footer**, the **testimonial card wall** and the **MCP card** on /mcp (`mcp-card-dark`). Inside them the same token names re-point: `--background` → #0e0b0d, `--foreground` → #e3e0df, borders go white-alpha — the identical re-pointed set the app renders under a dark OS preference, so these panels are the marketing site's honest dark evidence, measured at rest.

## Content and utility surfaces

- **Blog** (`/blog` index, `/blog/introducing-huddlekit` article): the prose layer — `breadcrumb`, `prose-h1` (the serif display face), `prose-meta`, `prose-p` body and `prose-link` — on white.
- **Support centre** (`/support`): a search field (`support-search`, focused, never typed into) over category cards (`support-category`); `/support/getting-started` re-casts the blog's prose grammar for the article.
- **Compare** (`/compare` index, `/compare/pastel-alternative`): a TOC rail (`compare-toc`) beside checklist rows (`compare-check-item`).
- **Integrations** (`/integrations` grid cards `integration-grid-card`, `/integrations/linear` detail page).
- **Tools** (`/tools` index of ~30 free utilities, `/tools/color-contrast-checker`): working little apps — `tool-color-input` (with its swatch) and `tool-text-input`, focused, never typed into.
- **Contact** (`/contact`): email rows (`contact-row`) with copy buttons (`contact-copy`, never pressed).
- **Customers / agencies / manifesto / case-study / privacy**: section stacks and prose on the same chrome.

## The app login

`app.huddlekit.com/login` ([light](screenshots/app-login-light-default.png), [dark](screenshots/app-login-dark-default.png)) is a centred **login card** (`app-login-card`, radius-0) on `--canvas`: the wordmark, "Sign in to Huddlekit", the solid orange **Continue with Google** button (`app-google-button` on `--primary`) and the bordered **Continue with email** button (`app-email-button`) — whose own press reveals the **email field** (`app-email-input`, pill radius) with **Continue** (`app-continue-button`) and **back** (`app-back-button`), captured `app-login-light-email-open`. Nothing was typed and nothing was submitted; Google OAuth was never entered. The footer carries the Privacy/Terms line.

## Motion and focus

Transitions are the Tailwind defaults — `--default-transition-duration`/`-timing-function` with `--ease-in`/`--ease-in-out`/`--ease-out`, `--animate-ping`/`-pulse`/`-spin` and the page's own keyframes (the client-logo `clients-stack` marquee, `hero-reveal`, `scattered-scroll`, `enter`). Hover washes settle inside that window (nav links, ghost buttons, cards). Focus is a real keyboard ring on `--ring` (#ff6900 light / #f54900 dark) — verified on buttons, links, fields and the billing switch. The reduced-motion probe (`raw/motion.json`) finds the site **partial at best**: home and /mcp drop a few decorations under `prefers-reduced-motion` while /pricing, /features and the app login **ignore** it, and the infinite animations (clients-stack, ping, scattered-scroll) keep running under reduce — recorded, not tidied.

## Theme architecture

huddlekit.com boots light and offers no theme control: `light` is the only page theme and its `.dark` panels re-point the same names inside component surfaces. app.huddlekit.com paints `html.dark` + `data-theme="dark"` under `prefers-color-scheme` — the only dark-painting path the product has, used for the dark login evidence. Both token themes resolve from one declaration set; `dark` (#0e0b0d ground, #e3e0df ink, the #ea580d primary kept, white-alpha borders) is what the app renders under a dark OS preference.

## The boundary beyond the signed-out surface

This package documents the public product, not the account. Everything on app.huddlekit.com past **/login** — the annotation widget on a real page, the project dashboard, workspaces, settings, billing — redirects an anonymous visitor back and was never entered; Google OAuth and the email form were never submitted. **try./demo./status./docs./help.huddlekit.com** and **app.huddlekit.io** do not resolve. Those are boundaries — no pixel, token or component in this package claims to describe them.
