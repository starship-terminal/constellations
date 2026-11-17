# Grow with Google patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## The site chrome (light only)

Every page shares the same glue top bar — `header`, a 1440 x 64 white bar: the "Grow with Google" lockup (`header-logo`, 210 x 48, an anchor carrying the Google mark plus the wordmark image), then the nav — `nav-drop-trigger` "Career Certificates" (174.75 x 48), `nav-link` "AI Training" (107.75 x 48), "For Partners" and "Stories & Resources" — all 16px/24 medium in `#3c4043` ink with 12px horizontal padding and a 4px control radius. The dropdown opens `mega-panel`, a full-bleed 1440 x 623 fixed white panel of three link columns (`mega-item`, 272 x 48). Nothing in the header is filled: hover and pressed change nothing measurable; keyboard focus paints the 2px `#1a73e8` box-shadow ring on a `#f8f9fa` wash.

Under it runs the promo — `promo-banner`, a centered line (575.83 x 25) whose copy links in the site's painted accent `#3186ff` and ends in the filled `promo-link` pill ("Enroll now →", 119 x 26, white text on `#3186ff`).

## The home hero

The US home pairs a 616 x 346.5 video teaser (`video-teaser`, 16:9, opening a Glue modal with a YouTube embed — captured open, never played) with the headline column: `hero-h1` at 36px/44 with -0.25px tracking and the `hero-cta` filled pill (142.5 x 50, `#3186ff`, 48px radius). Sections follow with `h2` headings at 28px/36, `body-p` copy at 14px/21 in `#3c4043`, and the full-width announcement `card` (1296 x 285) carrying the white `card-link` (616 x 205, 8px radius) — the card's link text is the *other* blue, declared glue-blue-600 `#1a73e8`.

## The certificates catalog

`/certificates` opens with the `breadcrumb` (12px/20, `#3186ff`), an `eyebrow` (14px/24, 500, uppercase, 0.5px tracking) and `certs-h1` at 48px/56 with -0.5px tracking. The statistics band holds the 700-weight `stat-chip` figures at 48px/57.6 — sibling stats paint one each of the brand hues — with the `learn-more-btn` text anchor (84 x 20). Navigation inside the page is `tab-bar`, the 721 x 48 white pill bar at 120px radius on elevation-1 (`0 1px 2px`/`0 1px 3px 1px` rgba(60,64,67)), its `tab` items (97 x 38) washing `#f8f9fa` on hover and `#f1f3f4` when pressed. The certificate grid below sits on the light-blue band: `cert-card` cells (369.75 x 386) — white, icon, title, rating, blurb, "If you like:" line and a text "Get started on Coursera" CTA.

## The certificate detail page

`/certificates/ux-design/` opens on the dark editorial hero — `cert-hero`, a 1440 x 720 `#18191d` band carrying `cert-h1` in white at 60px/72, the `cert-cta` filled pill (254.5 x 50 — "Get started on Coursera →", an outbound enrolment link measured, never followed) and `badge-card` (377.91 x 68), the "GABE — GOOGLE UX DESIGN GRADUATE" overlay on the photo. The FAQ below is a column of `expansion-panel` rows (1296 x 93 closed, 1296 x 213 opened) separated by `#dadce0` hairlines; the open row's `expansion-content` block is 1296 x 120.

## The AI hub and footer

`/ai` leads with `ai-h1` (60px/72 white on the tinted band) and oversized `ai-card` panels (1069.33 x 702.25) with the filled `ai-link` pill (150 x 50). Every page closes on the `footer` — 1440 x 837 on the `#eff2f7` blue-grey band: `footer-link` columns (107 x 24, 16px medium in `#3c4043`) and the `footer-lang` select (233 x 24) — measured, never changed, because its form posts to services.google.com.

## Motion and focus

The one control transition is glue's 0.2s timing on colour, background and fill — on nav links, tabs, buttons, drawer controls and footer links (the mega-panel runs 0.15s, the jumplinks bar 0.3s). The probe's honest caveat: prefers-reduced-motion is only **partially** honoured — most ambient loops keep running (`raw/motion.json`). Focus is the 2px `#1a73e8` box-shadow ring offset 1px — never an outline; the 5px `outline: auto` in a forced-pressed read is Chrome's artifact.

## Mobile (390px)

The phone header compresses to `m-header` — 64px with the 48 x 48 `m-drawer-btn` hamburger in `#5f6368` that slides the navigation drawer over the page (`m-drawer-link` rows, 134.75 x 48; measured at its off-canvas rest x=-10, y=-999 when closed). The hero headline steps to 24px (`m-hero-h1`) and the CTA keeps the 50px pill (`m-hero-cta`, 142.5 x 50).

## The regional split

grow.google geo-routes by request: a real user agent or an explicit locale is 302'd from `/` to `/intl/<locale>/` — from this host, `/intl/ALL_sg/` (the Singapore/global-English edition). That variant ships a different promo stack and a shorter page (~3268px vs ~6806px); it is captured as the `apac-*` shots only. The canonical surface — everything in tokens.json and components.md — is the US edition a bare headless context receives.

## The boundary past the product

This package documents the marketing site. Enrolment lives on coursera.org, accounts on Google sign-in, the embedded video on YouTube — every one of those links was measured and none followed. The language select was never changed (its form posts to services.google.com). Those are boundaries, named — nothing in this package claims to describe them.
