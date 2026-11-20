# Fernand patterns

How the measured components combine into the real pages. Values are the measured ones in [components.md](components.md) and [raw/measurements.md](raw/measurements.md); tokens in [tokens.json](tokens.json). The screenshots under [screenshots/](screenshots) show each pattern in place.

## Site chrome

Every marketing page carries a fixed `header` (~72px tall, white over a 1px `--border` hairline, `z-index: 999`): the Fernand wordmark left, `About us` / `Pricing` / `Log in` nav links, then `Book a demo` (a `role="button"` anchor wired to a Cal.com scheduler — measured, never activated) and the near-black `Start for free` button. Header controls use the ~6px `--radius-control`, 8px vertical / 12px horizontal padding rhythm. At 390px the demo action drops out (`m--hide`), leaving logo + `Start for free`; there is no hamburger on the marketing site. The docs site swaps the marketing nav for collection links, a `menu__toggle` (mobile only), the search field, the `Go to Fernand` link and `a.switch__dark`, the real dark-mode link.

## The hero

Left-aligned masthead pattern on `home-light-default`: a dated changelog eyebrow pill (`a.hero__eyebrow` — date + label inside a white pill), the 38px/400 masthead "The free customer support platform for SaaS teams", a muted lede, then a pair of actions: the near-black `#1a2035` 8px-radius primary CTA and the Cal.com demo action, with `button.hero-demo__btn` ("Watch a 2 minute demo") mounting `.demo-modal__dialog` (a 1280×720 YouTube-nocookie embed over a backdrop) as a local overlay. Beside the copy sits `button.ai-setup__toggle` — an `aria-haspopup="menu"` "Install with AI" menu whose items copy a setup prompt for each agent (Claude, Cursor, Codex deep links); the toggle flips `aria-expanded` and paints a floating menu of agent items.

## Section anatomy

Marketing sections repeat one grammar: a centered white `.section__tag` eyebrow pill (40px radius, layered hairline shadows), a mid-size section heading, muted standfirst, then the section's own grid — `channels__card` carousel tiles (300px, `#f7fafc`, 10px radius, arrow buttons), `feat3__card` product-mock tiles, the `trusted__card` dark testimonial strip, the `int-logo` integration grid, and the `footer-cta` closing block ("Start free. Email included."). Buttons are consistent: near-black fill, white ink, 8px radius, `font-weight: 500`.

## The widget playground

The "Live chat and AI, embedded in your product" section is an in-page product demo: `button.wpg-color` brand-colour swatches retint a drawn widget mock, `.wpg-tab` tabs switch its panes, `.wpg-article` rows stand in for knowledge-base articles, and on/off switches flip its features. The same widget is *really* embedded on the site: `.fernand__launcher` is a fixed 48px dark bubble at the page corner that opens the `.fernand__backdrop` chat panel — captured open, never typed into.

## Pricing and comparison

`/pricing/` pairs a `pricing__col--free` card (blue radial-gradient decoration, blue-tinted ring, "FREE" eyebrow) with a paid card ($29 per active human per month) — white surfaces, 16px radius, layered shadow/border; plan features render as `pricing__line` rows and the FAQ is plain `dl.faq` dt/dd pairs. `/alternative/intercom` uses a real `table.alt-table` for the Intercom-vs-Fernand matrix plus `.alt-faq__item` disclosures behind `button.alt-faq__summary`.

## Signed-out app forms

`app.getfernand.com/auth/login` and `/create` are the only reachable app surfaces: a light card on the SPA's own palette (fields on white, the primary submit on the dark fill, small account links beside) and the `/create` intro panel ("Bonjour, I'm Fernand…") beside work-email, product-name and terms-checkbox fields with a `Continue` button. Both were measured and typed into then cleared; neither submit was ever pressed.

## Docs surfaces

`help.getfernand.com` reuses the palette with its own resolutions: a header of collection links and `menu__toggle`, a `#search-field` ("Start typing to search an article, collection…" with a ⌘K hint) that opens a `search__popover` results list as a local filter, `a.card` collection cards (emoji glyph, title, article count) and `wrapper__articles` rows. `a.switch__dark` sets `body.dark-mode` (persisted in localStorage) — the docs stylesheet also declares a `@media (prefers-color-scheme: dark)` partial remap — and the whole surface remaps: page #161618, ink #f7f8f8, borders to a white-at-10% hairline.

## Mobile

At 390px the marketing header keeps logo + `Start for free`, the masthead drops to 26px (from 38px), cards stack to one column and the carousel scrolls. The docs site's `menu__toggle` appears and opens the collection nav as an overlay.

## Motion and focus

Controls carry a measured ~150–300ms transition on colour/background/border/shadow (see the motion table in [components.md](components.md)); keyboard focus paints the browser/UAG or a themed outline where styled — the per-component focus rows in [components.md](components.md) record which rings paint where. `prefers-reduced-motion` behaviour was probed on the header CTA and is recorded in `raw/components-computed.json` `_meta.reducedMotion`.
