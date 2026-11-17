# Cofounder patterns

How the measured components compose cofounder.co's public surfaces — the Next.js/Tailwind v4 marketing site and the app.cofounder.co/os login boundary. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)) unless it names a declared variable from [raw/css-vars.json](raw/css-vars.json).

## The header

A 1440 x 91 fixed bar (`header`, `position:fixed`, transparent at the top — the border and shadow stay alpha-0 until scroll), floating over the pixel-art hero on a translucent white gradient with `backdrop-blur` (`light.surface.glass`). Inside: the Cofounder wordmark anchor (`logo`, 126 x 26), six flat nav links (`nav-item`, 15px / `font-weight 410`, `#fbfbf8` = `light.text.nav` on the glass) and the "Run a company" pill (`nav-cta`, 130 x 41, `radius 8px`). The nav CTA is the **light** pill style: painted layers show `#f1f1ee`/`#e7e7e1` fills under `#1a1a1a` 15px/460 text, with the dark-gradient layer present as the border/shadow carrier — the dark pill (`cta-dark`) is a different control. Focus on nav controls draws a `1px #101010` outline offset 1px (`light.focus`).

## The hero

The pixel-art landscape hero carries white gradient text (`hero-title`, 580 x 99, `46px/108%` 400 Neoris — the fill is a `linear-gradient(#fff, rgba(255,255,255,.9))` text clip) over the painted scenery. Two controls: `hero-cta` (128 x 41, `radius 8px`) the light-surface button — `#f5f5f2` fill (hover `#edeeea`), 1px `rgba(32,32,32,.1)` hairline (`light.border.subtle`), the layered inset+drop shadow (`light.shadow.control`), `0.14s ease-out` transition — and `hero-prompt-btn` (179.5 x 41), the glass "Copy Setup Prompt" button: translucent white gradient, `backdrop-filter: blur(24px)`, inset edge lights, white 15px/460 text. It writes the clipboard on press, so it was measured at rest, hover, focus (2px offset-4 ring) and CDP-forced pressed only — never clicked.

## Buttons

One control language: `radius 8px` (`core.radius.control` = declared `--radius-lg`), ~41px height, `15px/460` labels. **Light** (`cta-light`/`hero-cta`/`nav-cta`/`footer-cta`): `#f5f5f2` fill → `#edeeea` hover/pressed, 1px `rgba(32,32,32,.1)` hairline, the five-layer shadow (`0 2px 3px` drop + `#fff@.35` inner rim + `#fff` top inset), `0.14s ease-out`. **Dark** (`cta-dark`, 183.7 x 44; `plan-cta` chip; `logo-pill`): the `#4f4f4f → rgba(32,32,32,.85)` gradient (`light.accent` ≈ `core.color.ctaDark`) under a 1px `#383838` edge (`light.border.cta`) and a five-layer inset+drop shadow, `rgba(255,255,255,.9)` = `light.text.onAccent` text — hover holds the gradient, focus draws `2px ink-80 offset 4px`. The same dark recipe appears as the 20px-radius `logo-pill` (115 x 30 "Case Studies").

## The tools band

A `#1a6fd1` section (`blue-section`, 1425 x 1222, `light.surface.band`) inside the single light theme: white 40px/400 heading, the `aria-pressed` tab row — selected `tool-tab` (234 x 45, white 16px/460 = `light.text.onBand`), unselected `tool-tab-off` at white/40 (oklab white @ .4, hover @ .6) with a white/80 1px focus ring — and the tool picker buttons (`tool-button`, 340 x 47): `radius 10px`, white/60 fill → solid white on hover, `oklab(0 0 0 / .1)` → `/ .2` border, `0.15s cubic-bezier(.4,0,.2,1)`, ink-80 2px/2px focus ring. The tabs swap the diagram; pressing them was safe-local, but the tab toggles were read at their `aria-pressed` state rather than switched.

## Social proof and case studies

The customer logo row uses `logo-tile` cards (170 x 84, `#f3f3f0` = `core.color.tile`, `radius 10px`, inset white rim + `#000@.12` inner shadow + `@.7` outer). Case-study entries are plain anchors (`case-study`, 182 x 96) — no painted card chrome; focus gets the 1px `#101010` ring. A campaign carousel exists further down but its Previous/Next arrows never render a visible box signed out — recorded as missing.

## Pricing

The pricing page opens on a 46px/400 ink-80 headline (`pricing-title`, 1032 x 69 — the h1 is sr-only; the visible headline is the h2). The plans are **whole-card anchors** (`plan-card`, 640 x 594, `aria-label="Get started for Cofounder"`): the inner `.pricing-card` layer paints `#fbfbf8` (`light.surface.raised`), 1px `#dee2de` (`light.border.card`), `radius 16px` (`core.card.radiusPlan` = declared `--radius-2xl`), with the layered inset rim + ambient shadow. Inside: `plan-name` (15px/460 `rgba(38,35,35,.7)` = `light.text.muted`) and, revealed only while the card is hovered, the `plan-cta` chip (89 x 31) — a small `cta-btn-dark` (gradient, `#383838` edge, `12px/460` white-90 "Get started"). No lift transition is recorded on the anchor itself (`transition: 0s`); the chip reveal is the measured hover change. Every card links to app.cofounder.co — measured, never followed.

## The how-to guides

The guide pages render a hidden prerender heading set first in DOM (skipped) then the real column: `howto-title` (620 x 46, `40px/115%` 400 ink-80), `howto-heading` (620 x 33, `24px/140%` 530) and `howto-card-title` (620 x 21, `15px/140%` 530). No landmark wraps the column (the `main`/`section` probe misses — recorded as a gap); the content column's ink ladder is `light.text.primary` throughout.

## The sign-in card (boundary)

app.cofounder.co/os/login is the app's own surface — a different, darker control language measured at rest and never submitted. The page (`signin-card`, the 1430 x 900 `#fcfcf9` shell with the "CofounderOS" 32px title) centres OAuth rows (`signin-button`, 384 x 52): a `linear-gradient(to top, #0f0f0f, #262626)` fill under a 2px `#4f4f4f` border, full-pill radius, `14px/500` white text, three stacked drop shadows — and, recorded honestly, keyboard focus paints **no change** on the OAuth rows (`outline-style: none`; the latent `#4087f2` outlineColor never renders — an honest gap in the app's surface). The `signin-back` icon button (40 x 40, ink-72, hover `rgba(32,32,32,.05)` tint) does draw a focus ring — a `rgba(32,32,32,.1)` 2px shadow ring, not an outline. Nothing was typed, pressed or sent.

## Footer and mobile

The 1425 x 749 footer (`footer`) opens with the "Run an entire company" 40px card and its `footer-cta` light pill, then link columns (`footer-link`, 15px/460 `rgba(38,35,35,.8)` = `light.text.link` — the colour holds on hover while a `radius 4px rgba(231,231,227,.8)` `::before` pill appears behind it), `footer-social` icon buttons (36 x 36 light-surface style — `rgba(38,35,35,.5)` = `light.text.faint` glyphs, hover swaps them to `#e1e8e7` on the `#edeeea` fill) and the legal row.

At 390 px the bar compresses to 78px (`m-header`) with the 41 x 41 glass `m-menu-button`. Its press opens a **full-screen overlay** (`m-menu-open`, 390 x 844 `#f5f5f2`): a `#bfbfbf` (`core.color.feature.neutral`) 24px "How to" label over 40px/400 link rows (`m-menu-link`, `light.text.primary` — focus draws a `1px #e59700` amber ring, the surface's one warm focus), plus social icons and the copyright line at the foot. The hero drops to `m-hero` 34px white gradient text.
