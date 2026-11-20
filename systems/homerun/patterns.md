# Homerun patterns

How the measured components compose Homerun's public surfaces — the Webflow marketing site on www.homerun.co, the jobs.homerun.co careers app, and the two sign-in boundaries. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)) unless it names a declared variable from [raw/css-vars.json](raw/css-vars.json).

## The nav bar

A 1440 x 104 white sticky bar (`header`, `position:sticky`, painted `light.surface.page`), GT America ink `#4a3e3e` = `light.text.primary`. Inside: the wordmark (`logo`, 126 x 26), a product dropdown pill (`nav-product-pill`, 221 x 58), plain link rows (`nav-link`, ~74 x 58, `radius 10px`), then two hover-open dropdowns and the actions: the dark "Book a demo" (`nav-demo`, 127 x 72, solid `#2d2323` = `light.darkFill` = `color.brown.500`, `radius 12px`, white label) and the blue "Start free trial" (`nav-trial`, 136 x 72, `#4f75fe` = `light.accent` = `color.blue.500`, same `radius 12px`). Both dropdowns open on hover (Webflow `data-hover`): Resources opens a 436 x 240 panel (`nav-resources-panel`) with 186 x 40 link rows; Log in opens a 234 x 138 panel (`nav-login-panel`) listing the product surfaces. Focus draws a 1px `auto` outline in the ink colour.

## The hero

Left-aligned on the white ground (`page-ground`, painted by the body): a 64px GT Walsheim 900 headline (`hero-title`, `#382d2d` = `light.text.heading` = `color.brown.400`, 576 x 192 at 1440), a 22px GT America subline (`hero-sub`, `#4a3e3e`), then the CTA pair — blue `hero-cta` (234 x 52, `light.accent`, 20px label) beside the dark `hero-demo` (160 x 54, `#382d2d` = `color.brown.400` fill, 1px `#edebe7` = `light.border.demo` = `color.beige.600` hairline). A rating row (`rating-row`, 640 x 50) of stars and review copy sits under them.

## Buttons

One button language across the marketing site: `radius 12px`, GT America labels (16px in the nav, 20px on heroes), two fills — solid blue `light.accent` #4f75fe and solid dark `light.darkFill` #2d2323 (a third, outlined `#382d2d` over the beige hairline, is the hero secondary). Pressed, the blue controls darken to `light.accentPressed` #254cda = `color.blue.600` and the dark ones lift to `light.darkFillHover` #4a3e3e = `color.brown.300`. The careers site runs the same language in its own blue (`light.careers.accent` #466af6, `radius 12px`, 22px labels on `careers-all-jobs`) and the application wizard carries it into the 538 x 80 `apply-next` bar.

## Bands and cards

Sections alternate the white ground with beige tints: testimonial cards (`testimonial-card`, 400 x 354, `#f5f1ec` = `light.surface.band`, `radius 20px`) sit in a tinted band; the feature accordions (`feature-accordion`, 548 x 56 → 548 x 153.7 opened, white card, `radius 10px`) expand a `feature-accordion-body` of body copy. The logo marquee (`marquee-item`, 128 x 96) scrolls customer marks on white. Every page closes on the dark CTA band (`cta-band`, 1260 x 461, `#2d2323` = `light.surface.dark`, **`radius 40px`** — the largest corner on the site) with white text and the blue CTA inside it — a dark band inside the one light theme, not a theme.

## Pricing

`pricing-title` (1120 x 180, 48px GT Walsheim) over three plan cards (`plan-card`, 652 x 442, white, 1px `#e3e1dd` = `light.border.subtle` = `color.beige.700`, **`radius 32px`**). Each card's job-slot count steps on `plan-stepper-plus`/`plan-stepper-minus` icon buttons (26 x 32); plan actions are dark `plan-button`s (150 x 52). The comparison table (`pricing-table`/`pricing-table-row`) kept earlier readings — the lazy-loaded rows were below the fold on the recapture pass. The FAQ is a `faq-item` accordion (678 x 56 → 678 x 227.5 opened, `radius 10px`, 25px questions) with `faq-answer` bodies; `pricing-cta` (130 x 54) is the page's closing action.

## Careers site and the application wizard

jobs.homerun.co is a separate client-rendered app on the same palette: a white `careers-header` (GT-America), a job list of `careers-job-card` rows (white, `radius 8px`, job titles in GT-Walsheim-Ultra-Bold `#131313` = `light.careers.link` = `color.brown.700`; the card's own link colour stays `#22a9e5` on the anchor's chrome), the `careers-all-jobs` blue button and a `careers-filter` control. A job ad opens `job-title`, the blue `job-apply` (130 x 60, `#466af6`), `job-prose` body and `job-share`/`job-back` chrome. The careers `cookie-banner` (white card, `radius 5px`) is hidden on every capture — never answered. The apply link opens the public wizard: an `apply-steps` strip (Your details / Questions / Preview / Submit), `apply-field`/`apply-email` inputs (40px high, `#fafafa` ground on a 1px `#e8e8e8` hairline, Inter), `apply-back` (61 x 40) and the blue `apply-next` (538 x 80). **It was measured at rest only: nothing was typed, uploaded or submitted.**

## The sign-in cards (boundaries)

app.homerun.co/login is the Angular ATS card (`signin-card`), measured at rest: an `h-button` tab row (`signin-tab`, 231 x 64), SSO buttons (`signin-sso`, 382 x 44, transparent on a 1px `rgba(102,87,87,.2)` hairline, `radius 10px`), email and password fields (`signin-email`/`signin-password`, 382 x 44, `#f5f3ef` fill = `color.beige.500` = the app's declared `--ui-input-bg`, `radius 10px` = `--ui-input-border-radius`, 44px = `--ui-input-height`), the blue `signin-button` (382 x 44, `#4f75fe`, pressed → `#254cda`) and a `signin-link`. **No credentials were typed and the form was never submitted.** app.homerun.hr/Account/Logon is the .NET HR card (`hr-card`, 382 x 278) on the Tailwind `public-form__*` stack: the same 44px beige fields (`hr-field`/`hr-password`) and the green `hr-button` (`#00b16b` = `light.app.hrAccent` = `color.secondary.green`, pressed → `#128053`) with `hr-link`.

## Footer and mobile

The 1340 x 622 footer stacks link columns (`footer-link`, `#736b6b` = `light.text.muted` = `color.brown.200`, 20px), `footer-heading` labels, and a newsletter row: `newsletter-field` (217 x 50, `rgba(45,35,35,.1)` tint, **`radius 30px`** pill) plus `newsletter-button` (96 x 50). At 390 px the bar collapses to a 390 x 72 `m-header` with the painted `m-menu-button` hamburger (39 x 40 — a second, hidden `.w-nav-button` copy sits in the DOM at 0x0). Its press opens the `m-menu-open` sheet (358 x 451) with `m-menu-link` rows (324 x 60); the tap layer never reaches the button, so the capture opens it with an in-page click. The hero drops to `m-hero` 322 x 160 GT Walsheim.
