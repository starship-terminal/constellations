# Gladia patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (dark)

Every www.gladia.io page carries the same floating glass navbar — a 1200 x 72 rounded bar (`--nav-bar-height` 70px) painting rgba(0, 0, 0, 0.65) over the black `--bg-primary` field, ringed by a 1px #1f1f1f hairline at 20px radius. Inside it: the Gladia wordmark (mkt-logo), the Product/Solutions/Developers/Resources/Company mega-menu triggers (`nav-menu-btn`, 15px Suisse Intl at rgba(255, 255, 255, 0.68) ink that lifts to white on hover), the Pricing link, the "Request a demo" ghost pill (`nav-demo`, 146 x 32, `core.color.neutral.800` fill under a `core.color.alpha.white12` hairline, 40px radius) and the white signup pill (`nav-cta`, 81 x 32, white fill on black ink — the header's inverse accent). Both pills spring-scale 1.02 on hover over `cubic-bezier(0.34, 1.56, 0.64, 1)` (`--ease-spring`).

The triggers open a full-width mega-menu by hover intent (keyboard focus + Enter is the fallback; Escape closes). The Product panel (`mega-panel`, 1080 x 361.66, black at 23px radius) pairs a 360px overview card — a white-on-black gradient wash with a 1px rgba(255,255,255,0.1) border and an inset top highlight — against a grid of product links (`mega-item`) eyebrowed in Geist Mono 11px at rgba(148, 122, 252, 0.95) purple. The other four panels were captured as the `home-dark-menu-*` screenshots.

## Home and product pages

The home hero is a display masthead in Suisse Intl ~80/94.8 (`hero-h1`) on the black field, topped by a white announcement pill (`hero-badge`, `.announce-pill`, 338 x 38 — a "Live" marker beside an animated counter). Section headings step down to 48/57.6 (`section-h2`). Product pages (`/product/speech-to-text-api` and its real-time/async children, `/product/audio-intelligence`, the `/use-cases/*` family) repeat the same grammar: dark field, display h1, feature grids, code blocks in Geist Mono, and CTA pills — measured as `prod-h1`, `prod-cta`, `prod-code`.

## Pricing

/pricing leads with an Async/Real-time segmented toggle (`price-mode-async`/`price-mode-rt`, aria-pressed, a local UI toggle that re-prices the grid; focus draws the 2px `light.border.focus` #1a9eff ring). Plan cards (`plan-card`, 428px columns in the 880px `.pricing-grid--plans`) carry per-plan CTAs (`plan-cta`, 346 x 40), and a usage calculator pairs an hours text field (44px, `component.field.height`) with a 20px range track and 13px feature checkboxes — the hours field was typed into then cleared, the range and checkboxes measured at rest and keyboard-focused, never dragged or toggled. FAQ rows (`faq-acc`, 720px) accordion open.

## Demo request

/demo-request is a single-column form under an 860px h1: 462 x 44 text fields (`demo-email`, `demo-name`), a 462 x 44 company-size select, and the 462 x 48 submit pill (`demo-submit`). Fields were focused and typed into then cleared; Submit was measured in every state, never pressed — what a submission returns is unverified.

## The docs site (Mintlify, light + dark)

docs.gladia.io is a different stack — Mintlify — with its own token layer and a real light/dark preference. Its chrome: 240px sidebar nav links (`docs-nav-link`), a search trigger, code blocks (`docs-code`), content tabs (`docs-tab`) and the "Change theme preference" button (`docs-theme-btn`, 20px). The preference was measured but never held; the docs' dark surface is captured as the `docs-*-theme-dark` screenshots — a genuinely painted dark theme, kept out of the marketing token sets.

## The auth shell

app.gladia.io / and /signup are the product auth shell — a different stack again that shares none of the marketing `--*` layer. Each page splits a 720 x 900 form panel from a marketing panel: "Continue with" SSO buttons and a sign-in/sign-up submit at 360 x 44 (`login-sso`, `signup-sso`, `login-submit`, `signup-submit`), with the shell's own purple focus ring #7e65e1. The email/password fields were typed into then cleared; every button was measured, never pressed — the forms were never submitted.

## Library and blog (the light surfaces)

/library is the one marketing page that mounts `body.light-mode`, re-pointing the 19 semantic roles to light values — the `light` token set (`light.bg.primary` #ffffff, `light.text.primary` #000000, `light.border.primary` #e5e5e5). /blog is a separate legacy Webflow build on its own stylesheets; both were captured at index level. `.section--white` re-points 5 roles for white sections embedded inside dark pages.

## Mobile (390px)

The phone surface keeps the same bar: a top bar (`m-topbar`, the 358 x 56 `nav.navbar`) with the mark and a 36 x 36 "Open menu" button (`m-menu-btn`) that toggles a full-height 390 x 844 overlay (`m-drawer`, `div#mobileNav.mobile-nav`: a dimming backdrop plus a 358 x 744 dark sheet of nav links at 20px radius) — measured opened and closed. The hero drops to a smaller masthead (`m-hero-h1`, 342 x 144).

## Motion and focus

Marketing controls transition fast — 0.16–0.32s `cubic-bezier(0, 0, 0.2, 1)` on colour, background and transform, with the spring easing reserved for the pill hover scale; page-level elements run longer 0.8–1.25s entrance fades. The motion probe saw heavy ambient animation (1926 moving elements across 6 pages) that fully subsides under `prefers-reduced-motion` — every moving element stops, and the only reduced-mode transitions left are negligible ≤1ms resets. Focus is an outline ring: 2px `light.bg.brand` purple on nav triggers, 2px `light.border.focus` #1a9eff on the pricing toggle, the auth shell's #7e65e1, and plain 1px auto rings elsewhere — measured as `focus-visible` states.

## Theme architecture

The marketing `:root` is dark by default — the `dark` token set is what every www.gladia.io page paints, and an emulated `prefers-color-scheme` pass resolved `:root` identically (no theme control exists). `body.light-mode` is the light scope /library mounts (the `light` set); `.section--white` re-points a smaller subset. The docs' Mintlify dark preference and the app shell's own dark surface are captured as screenshots and component measurements, not token values.
