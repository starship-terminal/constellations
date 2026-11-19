# Components

Public signed-out surfaces of mymind, measured on 2026-11-19 from computed styles. No component crop was saved: the preview browser returned "The browser is not producing screenshot frames."

Values are token names. Shared numbers are in [tokens.json](tokens.json).

## Button

The marketing primary is an orange pill. On the home page, "TRY IT OUT" paints `light.component.button-primary.background` (`#ff5924`) with `light.component.button-primary.text` (`#ffffff`), `core.typography.button` (Nunito 15px, tracking 0.8px) and `core.radius.cta` (120px). Padding is `core.spacing.button-y` by `core.spacing.button-x`.

The header "Sign up" item is the same orange with `core.radius.pill` (30px) and `core.typography.ui` (Nunito 16px, weight 500). On pricing, `.button-orange.button-xl` is 50px tall, radius `core.radius.button` (25px), horizontal padding about 27px.

"GET APP" is an orange text link, `#ff5924`, radius 100px, 14px Nunito, tracking 0.4px. Its computed border width was 0, so the outline is not a measured stroke.

Hover, focus-visible, pressed, disabled and loading were not measured. Rest transitions on `.is-content` are `all` over `core.motion.duration.button` (700ms) with `core.motion.easing.ease-out-expo`.

## Link

Header links "What", "Why" and "How" use `core.typography.nav` (Louize 20px) in `light.color.link` (`#1573dd`). The visible label inside the link is Inter 18px at `rgba(74, 84, 101, 0.8)`. "Log in" is Nunito 16px weight 500 in `light.color.muted`.

On the sign-in panel, "Sign up here." is Nunito 15px in `#ff5924`. "Terms of Use" and "Privacy Policy" are Nunito 15px in `#748297`.

## Text field

Not present on the public marketing pages or the signed-out sign-in panel. Sign-in offers Google and Apple buttons, not an email field. Recorded as a gap.

## Text area, select, checkbox, radio, switch

Not present on the captured public pages.

## Tabs

Pricing has a Monthly / Yearly pair of buttons. Both computed to Nunito 20px weight 600, colour `#7e90a7`, tracking -1px, transparent background. The Yearly button carries class `yearly active`. The selected treatment (underline, colour change) was not isolated from the rest state, so the selected colour is a gap.

## Menu

At innerWidth 390 the header nav computes `display: none` and a `.hamburger` shows at 50 by 36px on `#e2e6ee`. The opened menu was not captured.

## Tooltip, toast

Not present on the captured pages.

## Dialog

The sign-in URL also holds an onboarding layer ("SET UP MY MIND", "SOUND") whose button sat at y 731, on the fold of the 731px-tall viewport. It was not opened. Not captured.

## Card

Pricing `.feature-card` is `light.color.surface`, radius `core.radius.card` (22px), shadow `core.shadow.card` (`rgba(61, 65, 84, 0.15) 0px 1px 6px 0px`), about 350px wide. The title is Louize 28px weight 500, tracking -1.4px, colour `#2c3441`, padding 15px 30px 0.

## List row, table, avatar, badge

Review quotes are blockquotes, Inter about 19px, colour `#4a5465`, with no card background. No table, avatar or badge was on the captured pages.

Hero keyword chips (notes, bookmarks, inspiration, articles, images) are transparent pills with a 1px border in the matching text colour, radius `core.radius.bubble` (36px), padding 4px 18px, Nunito 18px.

## Icon button

The home play control is a circle with shadow `rgba(255, 154, 36, 0.1) 0px 8px 16px 2px`. Size was not isolated. Not captured as a component state.

## Gaps

- No screenshots or crops. Preview snapshot failed with "The browser is not producing screenshot frames."
- Dark theme of the signed-in product. Pricing copy mentions night mode. The public site did not paint a dark theme. `prefers-color-scheme: dark` was true in the browser and the sign-in page still painted a light panel.
- Hover, focus-visible, pressed, disabled, loading, error.
- Email field, validation, and any account form. FAQ says Google and Apple are the only sign-in methods.
- Open mobile menu, tooltips, toasts, destructive confirm, empty and loading app states.
- Selected style of the pricing Monthly / Yearly control.
- Reduced-motion pass. Computed motion was read at rest only.
