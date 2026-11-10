# 1password.com capture plan

Web batch 1, app 2 (webapps-manifest.json, issue c-wenlong/designs#437). Public
marketing site only — the 1Password web vault needs an account + secret key +
master password (not Google OAuth, no credentials held) and `start.1password.com`
redirects headless Chromium to `/unsupported`, so app internals are a declared
gap.

## Surfaces

- `/` home: nav banner + white header (Business/Personal/Partners/Resources
  flyouts, Sign in, Get started free), dark 88px-light hero, CTAs, logo cloud,
  product sections, footer
- `/pricing`: plan cards/tabs (Individual/Business toggle), comparison table
- `/product/enterprise-password-manager`: product tour page, feature sections
- `/downloads/mac`: download hero, platform chips, download CTA
- `/developer-security`, `/personal-ai-agent-integrations`, `/contact-sales`:
  secondary marketing surfaces if cheap
- `start.1password.com/unsupported`: the browser gate page (the real sign-in
  card is unreachable headless — feature detection, not a popup)

## States

- nav flyout (hover a `group/nav-item` button — Business menu is the rich one)
- promo banner strip (top of header, `header-navigation__nav-banner-link`)
- pricing billing toggle (monthly/annual if present)
- mobile 390x844: home, hamburger menu, hero

## Components to measure

Shell: banner, header, nav-link, nav-menu-button, flyout panel, cta buttons
(primary/outline), signin link, footer. Home: hero, hero-cta, logo cloud, card,
section heading. Pricing: billing toggle, plan card, plan-cta, compare table.
Product: feature heading, media card, stat. Download: platform chip, download
button. Mobile: m-header, m-hamburger, m-menu.

## Popup surface

None observed on load (no consent modal in the probe). Keep the generic
closePromo sweep for cookie banners; 1password's nav banner is chrome, not a
modal — do NOT kill it.

## Notes

- Tailwind classes; :root has only 4 vars — the theme tokens live in the
  Tailwind v4 `@layer theme`/utility scale; vars.mjs reads the CSSOM sheets.
- Fonts: Agile Sans Variable + Agile Mono Variable (proprietary, woff2 from
  1password.com assets) — style guide falls back to system faces.
- signin link: start.1password.com/signin -> /unsupported headless; capture
  the unsupported page as the "account" surface.
