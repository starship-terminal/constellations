# Foodnoms patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome

A 64px white header pairs the rounded app icon and the Aquawax Bold wordmark with 15px Medium nav links (News, Foodnoms+, Help) on `light.muted` — hovering lifts them to `light.accent-hover`. The action is the 40px "Get the App" App-Store pill: `light.accent` on `radius.button` (20px), white 16px DemiBold, which lifts to `light.accent-hover` on hover. The same pill recipe — 40px/20px/16px DemiBold — is the site's only button shape: it reappears as the hero download CTA (reversed to `light.surface.card` fill with `light.accent-text` ink), the help search submit, the newsletter subscribe and the "Get Foodnoms" closer.

## Hero and goal-pill marquee

The hero is a 56px/61.6px Aquawax Bold ticker that cycles benefit words (Log Food, Count Calories, Track Macros…) through the nutrient hue set (`light.hue.*`), over an 18px Medium sub on `light.muted`. Beneath it a marquee of 40px goal pills — neutral or accent-tinted text on `light.surface.card` with a star glyph — scrolls on a slow Framer animation; the whole site animates freely and ignores prefers-reduced-motion (raw/motion.json: 125 moving records, none removed).

## Feature cards and values

Feature cards sit on `light.surface.card` (#f2f2f2) at 18.8px radius (`radius.card`) with a per-card title hue — blue, teal, green, pink… — in 28px Bold over 16px Medium body on `light.body`. The values trio drops the card shell: its wrapper is transparent and square, and the shield/cloud/eye-off glyphs are 40px mask glyphs painted in the nutrient hues themselves — `light.hue.steel`, `light.hue.teal`, `light.hue.indigo` — beside 22px Bold titles on `light.ink`. The "As Featured By" strip and the review marquee repeat the card shell at smaller scale.

## Pricing (/plus)

Headline, a "Find pricing info for your region in the app" tag chip and two download CTAs, then the Free vs Foodnoms+ comparison — a Framer Row/Header/Paragraph/Divider/Symbol component (measured `pricing-table`, `pricing-row`, `pricing-check`), not a `<table>`: 17px Bold headers, 16px feature cells, check/cross mask glyphs, 12px-rounded rows on alternating card fill. No prices render publicly; the tag names the gap.

## Help center

A 44px h1 over the Search trigger (a 40px capsule that opens Framer's own search modal — opened, typed, cleared, never submitted) and stacked topic accordions. A section's own header toggles Closed → Open; the open state is the accordion-head + item list measured in the Open states entries. The Contact Us block ends the page with a mailto pill.

## Article pages

/family-plan, /vs/myfitnesspal, help and news articles share one longform recipe: a tag chip / date line, the 44px Bold h1, then Medium prose at 16-18px with inline links on `light.accent-text` orange, h2/h3 subheads, figure images, and — on family-plan and vs-mfp — a static FAQ block of bordered question rows (`fp-faq`, `mfp-faq`).

## Newsletter and press

/news' "Become a Foodnoms Insider" block puts the email field and Subscribe pill in one 40px capsule bar: the field is `light.surface.card` with an inset `light.surface.ring` shadow, 16px Medium; focus keeps `outline: none` and adds a measured 2px inset accent-tint shadow (`0 0 0 2px` #f98158-class) inside the ring. /press is an app-details block (icon, name, tagline, platform lines) plus press-kit asset links — measured, never downloaded.

## Legal and the open interstitial

/terms and /privacy are one tall Legal Item body under the h1 (~18k and ~12k px). /open/settings/* are static "Open in Foodnoms" deep-link interstitials — what an app link lands on in a browser, measured at rest.

## Dark theme

The site repaints under its own `prefers-color-scheme: dark` media rule: canvas goes black, card fill becomes #1a1a1a (`dark.surface.card`), the .2/.4 text greys climb to .8/.6, while the accent pills, white text and the accent-orange footer panel stay unchanged — a hue-anchored rather than accent-anchored dark map. There is no on-site toggle; theme follows the OS, captured via emulated dark scheme.

## Mobile (390 wide)

The chrome collapses to wordmark + hamburger ("Open navigation menu"; its overlay is the mobile-home-light-drawer screenshot). The mobile pass does record metric drift beyond layout: the hero ticker drops to 36px/39.6px, feature-card titles to 22px/26.4px and review quotes to 16px/22.4px (from 56px/61.6px, 28px/33.6px and 18px/25.2px), while cards stack and the footer columns reflow on the same tokens.

## Footer

An accent-orange panel (`light.accent`, the same `#ff5406` as the pills) at `radius.card` (18.8px), identical in both themes: white 17px Bold column heads, white 15px links that lift to `light.accent-hover` on hover, the Explore / Comparisons / Company / Social groups, a mailto and the legal row.
