# Clearful patterns

How the measured components compose clearful.com's public surfaces — the Webflow marketing site, the Tailwind /library sibling and the app.clearful.com sign-in boundary. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)) unless it names a declared variable from [raw/css-vars.json](raw/css-vars.json).

## The nav bar

A 1440 x 72 white bar (`header`), bottom hairline `#e1e1e1` (`light.border.subtle`, declared `--border-color--border-primary`), 72px side padding. Inside: the wordmark (`logo`), a "Guided Journals" link and "Log In" (`nav-item`/`nav-signin`, 40px tall, 8x20 padding, 16px/600 `#222`, radius 16 — hover paints the `#f7f7f7` wash, never an underline), then the action: "Start a journal — it's free" (`nav-cta`, 225 x 50, the 999px pill, `#1953ff` fill `light.accent` over a 1px same-blue border `light.border.brand`, white 16px/600 text). Hover and pressed share the `#1b1bbc` step (`light.accentHover` — declared only under a deleted variable); focus draws the 1px `#101010` ring (`light.focus`). The pill's href is `#` — measured, never followed.

## The hero

White ground (`light.surface.page`, painted by `body`) under a centred 1024px headline: "Be a more thoughtful, resilient, and happier you with daily journaling" — 72px/700 **Literatatt** (`hero-title`), the display face; **no lede** — the headline stands alone over the action. The "Start journaling for free" CTA (`cta`, 289 x 82, 20px/600) is the same 999px blue pill, but carries a painted halo: a 6px `#adc2ff` ring (`light.ring.cta`, blue-200) proud of the fill. Sections alternate white, `#f7f7f7` secondary (`light.surface.secondary`, feature rows and cards) and one `#d6e0ff` brand-light band (`light.surface.brandLight`, `section-accent`) where headings go navy `#001452` (`light.text.navy`, blue-900).

## Feature cards and tabs

1280 x 720 feature cards (`feature-card`, radius 24 `core.radius.xlarge`, `#f7f7f7` fill, copy column plus app screenshot). The home page's cadence picker is a real `w-tabs` widget (`tab-link` — Weekly/Monthly/Quarterly/Bi-Yearly/Yearly rows switching a demo pane; a local toggle, never a navigation).

## Pricing

Same light skin: a 60px/700 Literatatt "Pricing Plans" h1 (`pricing-title`), the Monthly/Yearly `w-tab-menu` billing tabs (`billing-tab`, 108 x 40, the held period carrying `w--current`), then plan columns (`plan-column`, 347 x 247 tops): 56px/700 Manrope prices ("$0/mo", "$9.99/mo" — `plan-price`) over the 347 x 58 blue "Get started" pill (`plan-cta`, same accent/hover ladder as the nav CTA). Below, a Free/Premium feature table on alternating `#f7f7f7` rows (`feature-row`, 1280 x 56, radius 8 `core.radius.medium`).

## The library surface (Tailwind sibling)

/library is a different build — Tailwind utilities, Mulish (`core.font.family.library`), gray-900 `#111827` ink — on the same light theme: a 60px/800 "Guided Journaling Library" h1 (`library-h1`) over white prompt cards (`prompt-card`, 395 x 160, radius 16 `core.radius.large`, `#e1e1e1` border, a soft drop shadow, black `#000` text — the Tailwind stack's own ink). Hover paints the `#f7f7f7` wash. The cards link into guided-journal detail pages — measured, never followed.

## The sign-in card (Flutter boundary)

app.clearful.com/#/sign-in is a Flutter canvas app on a `#f7f7f7` ground (`core.sampled.app.ground`, pixel-sampled). The card centres a 264 x 176 "Welcome Back" illustration (`signin-image`) over three 400 x 56 buttons (`signin-button`): white "Continue with email" (`core.sampled.app.oauth.email` with `#e1e1e1`-ish edge and `#222` label), near-black `#222` "Continue with Apple" (`core.sampled.app.oauth.ink`), Google-blue `#1a73e8` "Continue with Google" (`core.sampled.app.oauth.google`). All colours are canvas-painted and were sampled off `raw/full/signin-light-default.png`; all rects are real — read through Flutter's `flt-semantics` overlay after mounting the local accessibility switch, at devicePixelRatio 1 (the canvas lays out at half scale under DSF 2). Nothing was signed into or submitted.

## Footer and mobile

The 1440 x 535 `#f7f7f7` footer (`footer`): 16px/400 link columns in `#515151` (`light.text.muted`, declared `--text-color--text-secondary`, hover `#1953ff` `light.text.accent`), social icons (`footer-social`), the App Store badge (`app-badge`, 153 x 80 — links to apps.apple.com, never followed) and the legal subfooter. At 390 px the nav becomes a fixed white bar (`m-header`, 390 x 64), the hero drops to 56px (`m-hero`), and the hamburger's own press opens a 390 x 844 full-height white menu (`m-menu-open`, 18px/600 link rows `m-menu-link` with the `#f7f7f7` hover wash).
