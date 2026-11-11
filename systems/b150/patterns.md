# B150 patterns

How the measured components combine on each captured surface of b150.ai, signed out. Every value is measured from computed styles — the site is Tailwind v4 and declares no design-token custom properties.

## Chrome

- **Header** (`header`, 1440 x 65): dark bar holding the wordmark (`logo`), six nav links in `.label` — VIBEATHON, EVENTS, JOBS, MARKETPLACE, TALENT, FREE RESOURCES (`nav-item`, Fragment Mono 10px uppercase, cream #fffdf6, hover fades opacity) — then `login-link` (LOGIN, points at app.b150.ai) and `signup-btn` (SIGN UP: white pill, #ffffff fill, #1f1915 text, 40px tall, infinite radius).
- **Footer** (`footer`, 1440 x ~1064): the near-black #000 surface. `footer-link` rows repeat the mono-label treatment at 10px; section columns carry the page links.
- **Mobile chrome** (`m-header`, 390 x 65): wordmark plus `m-menu-button` (40 x 40). Pressing it opens the menu (`m-menu-open`, crop shows the open layer); `m-nav-link` rows are 358 x 29 inside it.

## Home

- **Hero** (`hero`, 740 x ~336): the "Don't wait for the future. Build it." display heading — Geist Variable ~120px measured — over the dark ground, with `hero-cta` JOIN THE BETA (cream #fffdf6 pill, #1f1915 text, 41px tall, infinite radius; hover shifts to #e6e3dd).
- **Sections** (`home-section`, 1440 x ~969): below the hero, full-width dark sections stack feature copy and imagery; the same mono labels mark eyebrows and CTAs.

## Vibeathon

- `vibe-title` (~1220 x 440 display block), `vibe-card` (the first card/section container, 1440 x ~921), `vibe-cta` (a small text call-to-action). The page is a long-scroll event surface: title, stacked sections, repeated CTA.

## Talent

- `talent-title` (740 x ~335 display heading), `talent-card` (512 x 700 — a profile/talent card on the warm-cream ground), `talent-cta` (41px pill). Cards sit on the cream inner surface; hover is a subtle tone/opacity shift.

## Free resources

- `res-title` (1220 x ~264) over `res-card` rows (412 x ~596): resource cards on the cream ground.

## About

- `about-title` (1220 x ~264) and `about-body` (the founder-letter copy block, 800 x 540). Editorial layout: display title, long-form body.

## Contact

- `contact-title` (300 x ~112) above a compact form: `contact-input` (300 x 56, 12px text, 8px radius), `contact-email` (same shape), `contact-button` (SEND MESSAGE, 112 x 40). Focused states were measured; the form was never submitted.

## Overlays and gates

- No consent wall or promo modal blocked any captured route; `home-light-arrival` records the page as it arrives.
- **Auth gate**: LOGIN and SIGN UP link to app.b150.ai and /auth/signup, which return HTTP 429 to non-browser clients — a documented boundary. The links are measured chrome, never followed.
