# Factory component measurements

Computed styles read from factory.com, docs.factory.com and auth.factory.ai on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the `data-theme="light"` marketing pages with their scoped dark sections (the [data-dark-hero] heroes, the dark footer), the docs pages measured light and then re-measured after the docs theme selector switched them to `data-theme="dark"` (states named `dark`), and the dark auth.factory.ai sign-in card reached through the app.factory.ai redirect — with any overlay hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Scoped dark surfaces

#### dark-hero

Dark scoped section. A [data-container-variant="inverted"] panel painting the dark token layer inside the light page — /enterprise's "Built for large enterprises" section.

Page: enterprise. Selector: `[data-container-variant=inverted]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 677.56 |
| Padding | 48px 32px |
| Gap | 64px 24px |
| Border | none |
| Radius | 10px |
| Background | #1f1d1c |
| Background image | linear-gradient(#ffffff @ 0.6, #ffffff @ 0.6), url(…) |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | p.text-foreground.text-pretty: Geist 12px/12px 400, #eeeeee, ls -0.24px |
| Transition | none |
| Icon | 24 x 24, colour #a49d9a |
| Painted layers | section.relative.grid 1280.0x677.6 bg #1f1d1c image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.6), url(…) r 10px; div.size-2.transform-gpu 8.0x8.0 bg #5c5855 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest |

Crops: `dark-hero-default.png`.

#### dark-h1

Dark section headline. The inverted section's heading, light ink on the near-black field.

Page: enterprise. Selector: `[data-container-variant=inverted] h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 311.45 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 32px/35.2px 400 |
| Letter spacing | normal |
| Colour | #eeeeee |
| Transition | none |
| How | at rest |

Crops: `dark-h1-default.png`.

#### dark-eyebrow

Dark section eyebrow. The small uppercase eyebrow label inside the inverted section.

Page: enterprise. Selector: `[data-container-variant=inverted] eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 102.41 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 12px/12px 400 |
| Letter spacing | -0.24px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `dark-eyebrow-default.png`.

#### dark-cta

Dark feature label. A feature row label inside the inverted section ("SSO + SAML") — the section carries no CTA.

Page: enterprise. Selector: `[data-container-variant=inverted] feature label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 203.55 x 16.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 14px/16.8px 400 |
| Letter spacing | normal |
| Colour | #eeeeee |
| Transition | none |
| How | at rest |

Crops: `dark-cta-default.png`.

### Enterprise / product pages

#### ent-h2

Section heading (enterprise). An /enterprise section heading.

Page: enterprise. Selector: `enterprise h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 149.78 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 144px/144px 400 |
| Letter spacing | -5.12px |
| Colour | #5c5855 |
| Transition | all 0.7s cubic-bezier(0.4, 0, 0.2, 1) |
| Opacity | 0.15 |
| How | at rest |

Crops: `ent-h2-default.png`.

#### ent-card

Enterprise feature card. An enterprise capability card on the light field.

Page: enterprise. Selector: `enterprise feature card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 198.19 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | h2.font-normal.ds-heading-2: Geist 36px/39.6px 400, #ebebeb, ls -1.12px |
| Transition | none |
| Icon | 40 x 40, colour #ebebeb |
| Painted layers | a.group.relative 154.4x31.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 152.4x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p |
| Ancestor paint | 1 up div.bg-light-base-primary.light:bg-base-100 bg #1f1d1c |
| How | at rest |

Crops: `ent-card-default.png`.

### Pricing

#### price-h1

Pricing headline. The "Pricing Plans" masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1296 x 39.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 36px/39.6px 400 |
| Letter spacing | -1.12px |
| Colour | #020202 |
| Text node | span.char-reveal: Geist 36px/39.6px 400, #020202, ls -1.12px |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### tier-tab

Plan-tier tab. A plan-tier switcher button (PRO/PLUS/MAX, role=radio). PRO is the page's own default, so another tier was selected first and the resting states read PRO unselected; the selected state was measured after clicking PRO — a local UI toggle.

Page: pricing. Selector: `plan tier PRO`. States: default, hover, focus-visible, pressed, selected.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 116 x 22 | = | = | = | = |
| Padding | 0px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 2px | = | = | = | = |
| Background | transparent | #d6d3d2 | = | #d6d3d2 @ 0.455 | #101010 @ 0.996 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = | = |
| Font | Geist 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #020202 | = | = | = | = |
| Text node | p.text-pretty.ds-label-1-mono: Geist Mono 16px/24px 400, #4d4947, ls -0.28px | = | = | = | p.text-pretty.ds-label-1-mono: Geist Mono 16px/24px 400, #f9f9f9, ls -0.28px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Ancestor paint | 1 up div.border-base-800.bg-dark-base-secondary bg #ebebeb | = | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover | own toggle, pressed once; a local UI state, never submitted |
| Painted layers | - | button.flex.h-full 116.0x22.0 bg #d6d3d2 r 2px | button.flex.h-full 116.0x22.0 r 2px outline 1px solid #101010 offset 2px | button.flex.h-full 116.0x22.0 bg #d6d3d2 @ 0.455 r 2px | button.flex.h-full 116.0x22.0 bg #101010 @ 0.996 r 2px |

Crops: `tier-tab-default.png`, `tier-tab-hover.png`, `tier-tab-focus-visible.png`, `tier-tab-pressed.png`, `tier-tab-selected.png`.

#### plan-card

Plan card. A pricing plan card (name, price, feature list).

Page: pricing. Selector: `pricing plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 416 x 408.81 |
| Padding | 24px 0px |
| Gap | 0px normal |
| Border | 1px solid #b8b3b0 |
| Radius | 4px |
| Background | #f9f9f9 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | h2.font-normal.ds-subheading-3: Geist 24px/24px 400, #4d4947 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #020202 |
| Painted layers | div.text-card-foreground.flex-col 416.0x408.8 bg #f9f9f9 border T:1px solid #b8b3b0 / R:1px solid #b8b3b0 / B:1px solid #b8b3b0 / L:1px solid #b8b3b0 r 4px; div.border-base-700.mb-8 366.0x1.0 border T:1px dotted #a49d9a; a.group.relative 366.0x31.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 364.0x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. A plan card's action; measured never followed.

Page: pricing. Selector: `plan card CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.89 x 25 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #a49d9a | = | = | = |
| Radius | 3px | = | = | = |
| Background | #f9f9f9 | #101010 | #101010 | #101010 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #020202, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #f9f9f9, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #f9f9f9, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #f9f9f9, ls -0.24px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 113.9x25.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 113.9x25.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 113.9x25.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 113.9x25.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-item

FAQ accordion item. A question row in the pricing FAQ accordion; the opened state was measured after clicking the question toggle, and the revealed answer region is measured beside the button (the opened crop shows the answer).

Page: pricing. Selector: `faq item`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 1368 x 67.2 | = | = | = | = |
| Padding | 24px 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | 2px | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = | = |
| Font | Geist 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #5c5855 | #ef6f2e | = | #ef6f2e | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 16px/19.2px 400, #020202, ls -0.32px | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.group/trigger.text-base-500 1368.0x67.2 r 2px outline 1px solid #101010 offset 2px | = | = |
| Panel | - | = | = | = | div.overflow-hidden, 1368 x 50, Geist 16px/24px 400, "You do. You retain 100% ownership and can use it however you like, including com" |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`, `faq-item-opened.png`.

### Contact form

#### contact-h1

Contact headline. "Bring Autonomy to your Engineering Organization" — the /contact masthead beside the form.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 92.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 44px/46.2px 400 |
| Letter spacing | -1.76px |
| Colour | #020202 |
| Text node | span.char-reveal: Geist 44px/46.2px 400, #020202, ls -1.76px |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### field-firstname

First name field. The HubSpot First Name text input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[name*=firstname]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 287 x 36 | = | = |
| Padding | 8px 16px | = | = |
| Border | 1px solid #a49d9a | 1px solid #ef6f2e | 1px solid #ef6f2e |
| Radius | 3px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist 12px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #020202 | = | = |
| Transition | border-color 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #b8b3b0, opacity 1 | = | = |
| Painted layers | input.hsfc-TextInput 287.0x36.0 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px | input.hsfc-TextInput 287.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px | input.hsfc-TextInput 287.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px |
| How | at rest | clicked into the field | typed "Ada", then deleted; nothing sent |

Crops: `field-firstname-default.png`, `field-firstname-focused.png`, `field-firstname-filled.png`.

#### field-email

Email field. The Work Email input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 287 x 36 | = | = |
| Padding | 8px 16px | = | 8px 40px 8px 16px |
| Border | 1px solid #a49d9a | 1px solid #ef6f2e | 1px solid #ef6f2e |
| Radius | 3px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist 12px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #020202 | = | = |
| Transition | border-color 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #b8b3b0, opacity 1 | = | = |
| Painted layers | input.hsfc-TextInput 287.0x36.0 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px | input.hsfc-TextInput 287.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px | input.hsfc-TextInput 287.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `field-email-default.png`, `field-email-focused.png`, `field-email-filled.png`.

#### field-select

Topic select. The "Select one..." dropdown field (a HubSpot select rendered as a read-only input); the opened state was measured after clicking it — a local UI toggle, no option chosen — and the revealed options list is measured beside the field (the opened crop shows the list).

Page: contact. Selector: `contact select`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 606 x 36 | = | = | = | = |
| Padding | 8px 36px 8px 16px | = | = | = | = |
| Border | 1px solid #a49d9a | 1px solid #ef6f2e | 1px solid #ef6f2e | 1px solid #ef6f2e | 1px solid #ef6f2e |
| Radius | 3px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Geist 12px/18px 400 | = | = | = | = |
| Letter spacing | -0.24px | = | = | = | = |
| Colour | #101010 | = | = | = | = |
| Transition | border-color 0.2s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Placeholder | #b8b3b0, opacity 1 | = | = | = | = |
| Painted layers | input.hsfc-TextInput.hsfc-TextInput--button 606.0x36.0 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px | input.hsfc-TextInput.hsfc-TextInput--button 606.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px | input.hsfc-TextInput.hsfc-TextInput--button 606.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px | input.hsfc-TextInput.hsfc-TextInput--button 606.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px | input.hsfc-TextInput.hsfc-TextInput--button 606.0x36.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Panel | - | = | = | = | ul.hsfc-DropdownOptions__List, 596 x 140, Geist 12px/18px 400, "LINKEDIN X EVENT PODCAST GOOGLE BILLBOARD REFERRAL/WORD OF MOUTH AN EXISTING CUS" |

Crops: `field-select-default.png`, `field-select-hover.png`, `field-select-focus-visible.png`, `field-select-pressed.png`, `field-select-opened.png`.

#### field-msg

Message textarea. The "how can we help" textarea; focused and typed into then cleared — never submitted.

Page: contact. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 606 x 72 | = | = |
| Padding | 8px 16px | = | = |
| Border | 1px solid #a49d9a | 1px solid #ef6f2e | 1px solid #ef6f2e |
| Radius | 3px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist 12px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #020202 | = | = |
| Transition | border-color 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #b8b3b0, opacity 1 | = | = |
| Painted layers | textarea.hsfc-TextareaInput 606.0x72.0 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px | textarea.hsfc-TextareaInput 606.0x72.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px | textarea.hsfc-TextareaInput 606.0x72.0 border T:1px solid #ef6f2e / R:1px solid #ef6f2e / B:1px solid #ef6f2e / L:1px solid #ef6f2e r 3px |
| How | at rest | clicked into the field | typed "A short question about Droid.", then deleted; nothing sent |

Crops: `field-msg-default.png`, `field-msg-focused.png`, `field-msg-filled.png`.

#### send-btn

Submit button. The form's SUBMIT button; its states were measured but the button was never clicked — nothing was submitted.

Page: contact. Selector: `contact SUBMIT`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.33 x 31 | = | = | = |
| Padding | 0px 38px 0px 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #8a8380 | 1px solid #ffffff |
| Radius | 3px | = | = | = |
| Background | transparent | = | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist Mono 14px/14px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #f9f9f9 | = | #101010 | #ffffff |
| Transition | color, border-color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hsfc-Button 100.3x31.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3px | = | button.hsfc-Button 100.3x31.0 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px | button.hsfc-Button 100.3x31.0 bg #000000 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3px |
| Ancestor paint | 1 up div.hsfc-NavigationRow__Buttons bg #a49d9a | = | 1 up div.hsfc-NavigationRow__Buttons bg #a49d9a outline 1px solid #101010 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `send-btn-default.png`, `send-btn-hover.png`, `send-btn-focus-visible.png`, `send-btn-pressed.png`.

### Docs (docs.factory.com)

#### docs-header

Docs header. The docs top bar: wordmark, Documentation/API Reference/Changelog tabs, GitHub + Discord icons, SIGN IN, DOWNLOAD, the three-way theme selector.

Page: docs. Selector: `docs header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 73 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #b8b3b0; L: none |
| Radius | 0px |
| Background | #f9f9f9 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | a.flex.h-[72px]: Geist 12px/12px 400, #020202 |
| Transition | none |
| Icon | 0 x 0, colour #3d3a39 |
| Painted layers | header.bg-dark-base-primary.border-base-800 1440.0x73.0 bg #f9f9f9 border B:1px solid #b8b3b0; a.flex.h-[72px] 111.0x72.0 border B:2px solid #ef6f2e; a.flex.h-[72px] 105.0x72.0 border B:2px solid #000000 @ 0; a.flex.h-[72px] 87.0x72.0 border B:2px solid #000000 @ 0; button.border-base-700.text-base-400 131.4x36.0 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 4px; kbd.border-base-700.text-base-500 24.4x18.0 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 4px |
| Ancestor paint | 1 up div.bg-dark-base-primary.min-h-screen bg #f9f9f9 |
| How | at rest |

Crops: `docs-header-default.png`.

#### docs-theme-btn

Theme selector button. One segment of the docs light/dark/system theme selector; a local UI toggle.

Page: docs. Selector: `.theme-selector-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 14, colour #020202 | = | = | = |
| Ancestor paint | 1 up div.border-base-800.bg-dark-base-secondary bg #ebebeb | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.theme-selector-button.relative 24.0x24.0 r 3px outline 1px solid #101010 offset 2px | = |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-sidebar

Docs sidebar. The left navigation column of the docs.

Page: docs. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 311 x 72 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | a.flex.h-[72px]: Geist 12px/12px 400, #020202 |
| Transition | none |
| Painted layers | a.flex.h-[72px] 111.0x72.0 border B:2px solid #ef6f2e; a.flex.h-[72px] 105.0x72.0 border B:2px solid #000000 @ 0; a.flex.h-[72px] 87.0x72.0 border B:2px solid #000000 @ 0 |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-nav-link

Docs nav link. A sidebar navigation link; measured, never followed.

Page: docs. Selector: `docs sidebar a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 203 x 32 | = | = | = |
| Padding | 6px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #d6d3d2 @ 0.6 | = | #d6d3d2 @ 0.6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = |
| Font | Geist 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4d4947 | #020202 | = | #020202 |
| Text node | span.min-w-0.break-normal: Geist 14px/20px 400, #4d4947 | span.min-w-0.break-normal: Geist 14px/20px 400, #020202 | = | span.min-w-0.break-normal: Geist 14px/20px 400, #020202 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.relative.flex 203.0x32.0 bg #d6d3d2 @ 0.6 r 4px | a.relative.flex 203.0x32.0 r 4px outline 1px solid #101010 offset 2px | a.relative.flex 203.0x32.0 bg #d6d3d2 @ 0.6 r 4px |

Crops: `docs-nav-link-default.png`, `docs-nav-link-hover.png`, `docs-nav-link-focus-visible.png`, `docs-nav-link-pressed.png`.

#### docs-h1

Docs headline. "Welcome to Factory" — the docs landing masthead.

Page: docs. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 824 x 46.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 44px/46.2px 400 |
| Letter spacing | -1.76px |
| Colour | #020202 |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-cta

Docs CTA. The "CREATE AN ACCOUNT" action; measured, never followed.

Page: docs. Selector: `docs CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185.25 x 31 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Border | 1px solid #a49d9a | = | = | = |
| Radius | 3px | = | = | = |
| Background | #f9f9f9 | #101010 | #101010 | #101010 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #020202, ls -0.28px | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #020202 | 16 x 16, colour #f9f9f9 | 16 x 16, colour #f9f9f9 | 16 x 16, colour #f9f9f9 |
| Painted layers | a.group.relative 185.3x31.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 183.3x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 185.3x31.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 183.3x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 185.3x31.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 183.3x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 185.3x31.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 183.3x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-cta-default.png`, `docs-cta-hover.png`, `docs-cta-focus-visible.png`, `docs-cta-pressed.png`.

#### docs-code

Code block. A docs code block (rehype-pretty-code / shiki themed).

Page: docs. Selector: `docs pre`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 824 x 515 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #3d3a39 |
| Text node | div.flex-1.text-center: Geist 11px/16.5px 400, #7a6f68 |
| Transition | none |
| Icon | 14 x 14, colour #3d3a39 |
| Painted layers | div.relative.w-full 824.0x515.0 bg #f3f1ee border T:1px solid #dcd6d0 / R:1px solid #dcd6d0 / B:1px solid #dcd6d0 / L:1px solid #dcd6d0 r 20px; div.absolute.inset-0 822.0x513.0 bg #fbfaf8; div.flex.h-9 822.0x36.0 bg #ecebe8 border B:1px solid #dcd6d0; span.block.h-3 12.0x12.0 bg #ff5f57 r 3.35544e+07px; span.block.h-3 12.0x12.0 bg #febc2e r 3.35544e+07px; span.block.h-3 12.0x12.0 bg #28c840 r 3.35544e+07px |
| How | at rest |

Crops: `docs-code-default.png`.

#### docs-card

Docs link card. A docs path card (QUICKSTART GUIDE / "Ship Code Faster"); measured, never followed.

Page: docs. Selector: `docs path card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 200 x 27.25 | = |
| Padding | 4px 0px 4px 12px | = |
| Border | T: none; R: none; B: none; L: 1px solid #b8b3b0 | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist 14px/19.25px 400 | = |
| Letter spacing | normal | = |
| Colour | #4d4947 | #020202 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.line-clamp-2.border-l 200.0x27.3 border L:1px solid #b8b3b0 | = |
| How | at rest | mouse hover |

Crops: `docs-card-default.png`, `docs-card-hover.png`.

#### docs-h1-dk

Docs headline (dark). The docs masthead re-measured after the theme selector switched the page to dark.

Page: docs. Selector: `docs h1, dark theme`. States: dark.

| Property | dark |
|---|---|
| Size (w x h) | 824 x 46.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 44px/46.2px 400 |
| Letter spacing | -1.76px |
| Colour | #eeeeee |
| Transition | none |
| How | docs theme selector switched to Dark (data-theme now "dark") |

Crops: `docs-h1-dk-dark.png`.

#### docs-sidebar-dk

Docs sidebar (dark). The sidebar re-measured in dark.

Page: docs. Selector: `docs sidebar, dark theme`. States: dark.

| Property | dark |
|---|---|
| Size (w x h) | 311 x 72 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #eeeeee |
| Text node | a.flex.h-[72px]: Geist 12px/12px 400, #eeeeee |
| Transition | none |
| Painted layers | a.flex.h-[72px] 111.0x72.0 border B:2px solid #ef6f2e; a.flex.h-[72px] 105.0x72.0 border B:2px solid #000000 @ 0; a.flex.h-[72px] 87.0x72.0 border B:2px solid #000000 @ 0 |
| How | still dark from the previous toggle |

Crops: `docs-sidebar-dk-dark.png`.

#### docs-code-dk

Code block (dark). The code block re-measured in dark (the --shiki-dark palette).

Page: docs. Selector: `docs pre, dark theme`. States: dark.

| Property | dark |
|---|---|
| Size (w x h) | 824 x 515 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #b8b3b0 |
| Text node | div.flex-1.text-center: Geist 11px/16.5px 400, #807670 |
| Transition | none |
| Icon | 14 x 14, colour #b8b3b0 |
| Painted layers | div.relative.w-full 824.0x515.0 bg #060606 border T:1px solid #1e1c1b / R:1px solid #1e1c1b / B:1px solid #1e1c1b / L:1px solid #1e1c1b r 20px; div.absolute.inset-0 822.0x513.0 bg #0d0c0b; div.flex.h-9 822.0x36.0 bg #131211 border B:1px solid #1e1c1b; span.block.h-3 12.0x12.0 bg #ff5f57 r 3.35544e+07px; span.block.h-3 12.0x12.0 bg #febc2e r 3.35544e+07px; span.block.h-3 12.0x12.0 bg #28c840 r 3.35544e+07px |
| How | still dark |

Crops: `docs-code-dk-dark.png`.

#### docs-nav-link-dk

Docs nav link (dark). A sidebar link re-measured in dark; measured, never followed.

Page: docs. Selector: `docs sidebar a, dark theme`. States: dark, hover.

| Property | dark | hover |
|---|---|---|
| Size (w x h) | 203 x 32 | = |
| Padding | 6px 8px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #1f1d1c @ 0.0195021 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #a49d9a | #a6a09d |
| Text node | span.min-w-0.break-normal: Geist 14px/20px 400, #a49d9a | span.min-w-0.break-normal: Geist 14px/20px 400, #a6a09d |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | a.relative.flex 203.0x32.0 bg #1f1d1c @ 0.0195021 r 4px |

Crops: `docs-nav-link-dk-dark.png`, `docs-nav-link-dk-hover.png`.

### Sign-in card (auth.factory.ai)

#### signin-panel

Sign-in panel. The dark auth.factory.ai sign-in card: "Sign in", email field, Continue-with-email and Google actions.

Page: signin. Selector: `signin form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 248.52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #eeeeee |
| Text node | label.rt-Text.rt-r-size-2: Geist 13px/18px 500, #b5ada7 |
| Transition | none |
| Icon | 15 x 15, colour #f5f2ef |
| ::before | 378px x 246.516px, absolute, bg #000000 @ 0, radius 0px |
| ::after | 378px x 246.516px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.rt-TextFieldRoot.rt-r-size-3 380.0x36.0 bg #0c0b0a r 2px shadow #463f3c 0px 0px 0px 1px inset; button.rt-reset.rt-BaseButton 380.0x36.0 bg #fdfcfb border T:1px solid #fdfcfb / R:1px solid #fdfcfb / B:1px solid #fdfcfb / L:1px solid #fdfcfb r 2px; div::before.rt-Text.rt-r-size-1 169.469pxx1px bg #26211f; div::after.rt-Text.rt-r-size-1 169.469pxx1px bg #26211f; a.rt-reset.rt-BaseButton 380.0x36.0 border T:1px solid #6b615c / R:1px solid #6b615c / B:1px solid #6b615c / L:1px solid #6b615c r 2px |
| How | at rest |

Crops: `signin-panel-default.png`.

#### signin-field

Email field (sign-in). The e-mail input on the sign-in card; focused and typed into then cleared — never submitted.

Page: signin. Selector: `input[name=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 378 x 34 | = | = |
| Padding | 0px 10px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #f5f2ef | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #807973, opacity 1 | = | = |
| Ancestor paint | 1 up div.rt-TextFieldRoot.rt-r-size-3 bg #0c0b0a shadow #463f3c 0px 0px 0px 1px inset | 1 up div.rt-TextFieldRoot.rt-r-size-3 bg #0c0b0a shadow #b5ada7 0px 0px 0px 1px inset, #b5ada7 0px 0px 0px 1px outline 2px solid #6255ae | 1 up div.rt-TextFieldRoot.rt-r-size-3 bg #0c0b0a shadow #b5ada7 0px 0px 0px 1px inset, #b5ada7 0px 0px 0px 1px outline 2px solid #6255ae |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-field-default.png`, `signin-field-focused.png`, `signin-field-filled.png`.

#### signin-submit

Continue with email. The email submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: signin. Selector: `signin Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #fdfcfb | = | = | = |
| Radius | 2px | = | = | = |
| Background | #fdfcfb | #e4dfdb | = | #e4dfdb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #b5ada7 offset 2px | = |
| Font | Geist 14px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17120f | = | = | = |
| Text node | span: Geist 14px/24px 500, #17120f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.rt-reset.rt-BaseButton 380.0x36.0 bg #fdfcfb border T:1px solid #fdfcfb / R:1px solid #fdfcfb / B:1px solid #fdfcfb / L:1px solid #fdfcfb r 2px | button.rt-reset.rt-BaseButton 380.0x36.0 bg #e4dfdb border T:1px solid #fdfcfb / R:1px solid #fdfcfb / B:1px solid #fdfcfb / L:1px solid #fdfcfb r 2px | button.rt-reset.rt-BaseButton 380.0x36.0 bg #fdfcfb border T:1px solid #fdfcfb / R:1px solid #fdfcfb / B:1px solid #fdfcfb / L:1px solid #fdfcfb r 2px outline 2px solid #b5ada7 offset 2px | button.rt-reset.rt-BaseButton 380.0x36.0 bg #e4dfdb border T:1px solid #fdfcfb / R:1px solid #fdfcfb / B:1px solid #fdfcfb / L:1px solid #fdfcfb r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-focus-visible.png`, `signin-submit-pressed.png`.

#### signin-google

Continue with Google. The Google OAuth action; measured, never followed.

Page: signin. Selector: `signin Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 36 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #6b615c | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | #1d1a18 | = | #1d1a18 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #b5ada7 offset 2px | = |
| Font | Geist 14px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f5f2ef | = | = | = |
| Text node | span.rt-Text.rt-r-size-2: Geist 16px/24px 500, #f5f2ef | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 15, colour #f5f2ef | = | = | = |
| Painted layers | a.rt-reset.rt-BaseButton 380.0x36.0 border T:1px solid #6b615c / R:1px solid #6b615c / B:1px solid #6b615c / L:1px solid #6b615c r 2px | a.rt-reset.rt-BaseButton 380.0x36.0 bg #1d1a18 border T:1px solid #6b615c / R:1px solid #6b615c / B:1px solid #6b615c / L:1px solid #6b615c r 2px | a.rt-reset.rt-BaseButton 380.0x36.0 border T:1px solid #6b615c / R:1px solid #6b615c / B:1px solid #6b615c / L:1px solid #6b615c r 2px outline 2px solid #b5ada7 offset 2px | a.rt-reset.rt-BaseButton 380.0x36.0 bg #1d1a18 border T:1px solid #6b615c / R:1px solid #6b615c / B:1px solid #6b615c / L:1px solid #6b615c r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-google-default.png`, `signin-google-hover.png`, `signin-google-focus-visible.png`, `signin-google-pressed.png`.

#### signin-signup

Sign up link. The "Sign up" link under the card; measured, never followed.

Page: signin. Selector: `signin Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6255ae offset 2px | = |
| Font | Geist 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f5f2ef | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.rt-Text.BrandedLink 48.0x18.0 outline 2px solid #6255ae offset 2px | = |

Crops: `signin-signup-default.png`, `signin-signup-hover.png`, `signin-signup-focus-visible.png`, `signin-signup-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header: the mark, the locale globe and the "Open menu" button — there is no header CTA pill at 390 wide.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | p.text-pretty.ds-paragraph-1: Geist 16px/19.2px 400, #4d4947 |
| Transition | none |
| Icon | 0 x 0, colour #020202 |
| Painted layers | a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a.group.relative 0.0x0.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px |
| Ancestor paint | 1 up body.__variable_8eaea4.__variable_8c25df bg #f9f9f9 |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-cta

Mobile drawer CTA. The "DOWNLOAD" row inside the opened nav overlay at 390 wide; measured never followed.

Page: mobile. Selector: `mobile nav overlay DOWNLOAD`. States: default, hover, focus-visible, pressed.

Earlier readings kept — a 2026-11-13 re-run did not re-measure this component (retained from the 2026-11-13 run).
| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 31 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #8a8380 | 1px solid #8a8380 |
| Radius | 3px | = | = | = |
| Background | #101010 | = | #f9f9f9 | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | 1px solid #101010 offset 4px |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px | = | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #101010, ls -0.28px | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #101010, ls -0.28px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 358.0x31.0 bg #101010 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3px; div.group-hover:running.group-focus-visible:running 356.0x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | = | a.group.relative 358.0x31.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 356.0x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | a.group.relative 358.0x31.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 356.0x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-menu-btn

Mobile menu button. The "Open menu" button that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.

Page: mobile. Selector: `mobile header menu button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = | = |
| Padding | 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | 2px | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = | = |
| Font | Geist 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | oklch(0.551 0.027 264.364) | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour oklch(0.551 0.027 264.364) | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.relative.-m-1 32.0x32.0 r 2px outline 1px solid #101010 offset 2px | = | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The nav overlay opened by the menu button; its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 80px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #f9f9f9 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | p.text-pretty.ds-paragraph-1: Geist 16px/19.2px 400, #4d4947 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #020202 |
| Painted layers | nav.bg-background.absolute 390.0x844.0 bg #f9f9f9; button.group.focus-visible:outline-light-base-primary 358.0x37.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #000000 @ 0 offset 0px; button.group.focus-visible:outline-light-base-primary 358.0x37.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #000000 @ 0 offset 0px; button.group.focus-visible:outline-light-base-primary 358.0x37.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #000000 @ 0 offset 0px; a.group.relative 358.0x31.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 356.0x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 318.22 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 32px/32px 500 |
| Letter spacing | -1.28px |
| Colour | #020202 |
| Text node | span: Geist 32px/32px 500, #020202, ls -1.28px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Ancestor paint | 1 up section.bg-background.relative bg #f9f9f9 |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "GET STARTED" pill at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero GET STARTED`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.92 x 31 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #8a8380 | = |
| Radius | 3px | = | = | = |
| Background | #101010 | = | #f9f9f9 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px | = | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #101010, ls -0.28px | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 114.9x31.0 bg #101010 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3px; div.group-hover:running.group-focus-visible:running 112.9x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | = | a.group.relative 114.9x31.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 112.9x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

### Site chrome

#### mkt-header

Site header. The fixed 72px top bar with the backdrop-blur mask: Factory wordmark, Product/Enterprise/Company mega-menu buttons, Pricing/News/Docs links, locale globe, SIGN IN, CONTACT SALES and DOWNLOAD.

Page: home. Selector: `header[data-site-header]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | span.text-pretty.ds-label-2: Geist 12px/12px 400, #020202 |
| Transition | none |
| Icon | 128 x 19, colour #020202 |
| Painted layers | a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a::after.text-pretty.ds-label-2 0pxx1px bg #020202; a.group.relative 113.9x25.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px |
| Ancestor paint | 1 up body.__variable_8eaea4.__variable_8c25df bg #f9f9f9 |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Factory mark-and-wordmark in the header, linking home.

Page: home. Selector: `header a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128 x 19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Transition | none |
| Cursor | pointer |
| Icon | 128 x 19, colour #020202 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-menu-btn

Mega-menu trigger. The "Product" header button — opens the mega-menu panel on hover (aria-expanded). The opened state was measured after a real pointer hover.

Page: home. Selector: `header button Product`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 61 x 60 | = | = | = | = |
| Padding | 24px 0px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | 2px | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = | = |
| Font | Geist 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #020202 | = | = | = | = |
| Text node | span.text-pretty.ds-label-2: Geist 12px/12px 400, #020202 | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 12 x 12, colour #020202 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.text-light-base-primary.hover:text-light-base-primary 61.0x60.0 r 2px outline 1px solid #101010 offset 2px | = | = |

Crops: `nav-menu-btn-default.png`, `nav-menu-btn-hover.png`, `nav-menu-btn-focus-visible.png`, `nav-menu-btn-pressed.png`, `nav-menu-btn-opened.png`.

#### nav-panel

Mega-menu panel. The mega-menu panel opened under the header by hovering "Product"; its links were never followed.

Page: home. Selector: `.megamenu-viewport`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 363 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | p.text-pretty.ds-label-2-mono: Geist Mono 12px/12px 400, #5c5855, ls -0.24px |
| Transition | transform, opacity 0.42s, 0.22s cubic-bezier(0.22, 1, 0.36, 1), ease-out delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.border-base-800.bg-surface-raised 570.0x363.2 bg #ffffff border T:1px solid #b8b3b0 / R:1px solid #b8b3b0 / B:1px solid #b8b3b0 / L:1px solid #b8b3b0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div.flex.flex-col 149.0x329.2 border R:1px solid #b8b3b0; div.flex.flex-col 186.0x329.2 border R:1px solid #b8b3b0 |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Mega-menu item. A link inside the opened mega-menu panel; measured, never followed.

Page: home. Selector: `.megamenu-viewport a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 124 x 32.8 | = |
| Padding | 8px 12px | = |
| Gap | 2px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #ebebeb |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #020202 | = |
| Text node | p.text-pretty.ds-paragraph-2: Geist 14px/16.8px 400, #020202 | = |
| Transition | opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | a.opacity-100.transition-opacity 124.0x32.8 bg #ebebeb r 4px |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-link

Nav link. A header nav link (Pricing); measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 41 x 12 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = |
| Font | Geist 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 1px, absolute, bg #020202, radius 0px | 41px x 1px, absolute, bg #020202, radius 0px | = | 41px x 1px, absolute, bg #020202, radius 0px |
| Painted layers | a::after.text-pretty.ds-label-2 0pxx1px bg #020202 | a::after.text-pretty.ds-label-2 41pxx1px bg #020202 | a.text-pretty.ds-label-2 41.0x12.0 r 2px outline 1px solid #101010 offset 2px; a::after.text-pretty.ds-label-2 0pxx1px bg #020202 | a::after.text-pretty.ds-label-2 41pxx1px bg #020202 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign in link. The "SIGN IN" header link to app.factory.ai; measured, never followed.

Page: home. Selector: `header a SIGN IN`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 55.33 x 12 | = | = | = |
| Padding | 0px 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3d3a39 | #020202 | = | #020202 |
| Text node | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #020202, ls -0.24px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-base-300.hover:text-foreground 55.3x12.0 r 2px outline 1px solid #101010 offset 2px | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Header primary CTA. The dark "DOWNLOAD" pill in the header; links to /product/desktop, measured never followed.

Page: home. Selector: `header a DOWNLOAD`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.09 x 25 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #8a8380 | 1px solid #8a8380 | 1px solid #8a8380 |
| Radius | 3px | = | = | = |
| Background | #101010 | #f9f9f9 | #f9f9f9 | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #f9f9f9, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #101010, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #101010, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #101010, ls -0.24px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 80.1x25.0 bg #101010 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3px; div.group-hover:running.group-focus-visible:running 78.1x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | a.group.relative 80.1x25.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px; div.group-hover:running.group-focus-visible:running 78.1x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | a.group.relative 80.1x25.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 78.1x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | a.group.relative 80.1x25.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px; div.group-hover:running.group-focus-visible:running 78.1x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-cta2

Header secondary CTA. The bordered "CONTACT SALES" pill in the header; links to /contact, measured never followed.

Page: home. Selector: `header a CONTACT SALES`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.89 x 25 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #a49d9a | = | = | = |
| Radius | 3px | = | = | = |
| Background | #f9f9f9 | #101010 | #101010 | #101010 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #020202, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #f9f9f9, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #f9f9f9, ls -0.24px | p.text-foreground.text-pretty: Geist Mono 12px/12px 400, #f9f9f9, ls -0.24px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 113.9x25.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 113.9x25.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 113.9x25.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 113.9x25.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 111.9x23.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta2-default.png`, `nav-cta2-hover.png`, `nav-cta2-focus-visible.png`, `nav-cta2-pressed.png`.

### Home

#### hero-mark

Hero mark. The Factory asterisk mark above the masthead.

Page: home. Selector: `hero mark svg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 87.5 x 84.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 87.5 x 84.88, colour #020202 |
| How | at rest |

Crops: `hero-mark-default.png`.

#### hero-h1

Hero headline. "AI CODING AGENTS FOR THE ENTERPRISE" — the uppercase Geist masthead.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 593.69 x 120.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 60.48px/60.48px 500 |
| Letter spacing | -2.4192px |
| Colour | #020202 |
| Text node | span: Geist 60.48px/60.48px 500, #020202, ls -2.4192px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Ancestor paint | 1 up section.bg-background.relative bg #f9f9f9 |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero subline. "Model agnostic. Deployed anywhere." — the mono tagline under the masthead.

Page: home. Selector: `hero subline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 20.55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Mono 18.6883px/20.5572px 400 |
| Letter spacing | normal |
| Colour | #8a8380 |
| Text node | span: Geist Mono 18.6883px/20.5572px 400, #8a8380 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Ancestor paint | 1 up section.bg-background.relative bg #f9f9f9 |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The dark "DOWNLOAD" pill in the hero; measured never followed.

Page: home. Selector: `hero DOWNLOAD`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109.77 x 31 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #8a8380 | 1px solid #8a8380 | 1px solid #8a8380 |
| Radius | 3px | = | = | = |
| Background | #101010 | #f9f9f9 | #f9f9f9 | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | span.flex.items-center: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px | span.flex.items-center: Geist Mono 14px/14px 400, #101010, ls -0.28px | span.flex.items-center: Geist Mono 14px/14px 400, #101010, ls -0.28px | span.flex.items-center: Geist Mono 14px/14px 400, #101010, ls -0.28px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #f9f9f9 | 10 x 10, colour #101010 | 10 x 10, colour #101010 | 10 x 10, colour #101010 |
| Painted layers | button.group.relative 109.8x31.0 bg #101010 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3px; div.group-hover:running.group-focus-visible:running 107.8x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | button.group.relative 109.8x31.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px; div.group-hover:running.group-focus-visible:running 107.8x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | button.group.relative 109.8x31.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 107.8x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p | button.group.relative 109.8x31.0 bg #f9f9f9 border T:1px solid #8a8380 / R:1px solid #8a8380 / B:1px solid #8a8380 / L:1px solid #8a8380 r 3px; div.group-hover:running.group-focus-visible:running 107.8x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #a49d9a 2px, #a49d9a 3p |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-cta2

Hero secondary CTA. The bordered "BOOK DEMO" pill beside it; measured never followed.

Page: home. Selector: `hero BOOK DEMO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.48 x 31 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Border | 1px solid #a49d9a | = | = | = |
| Radius | 3px | = | = | = |
| Background | #f9f9f9 | #101010 | #101010 | #101010 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020202 | = | = | = |
| Text node | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #020202, ls -0.28px | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px | p.text-foreground.text-pretty: Geist Mono 14px/14px 400, #f9f9f9, ls -0.28px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #020202 | 16 x 16, colour #f9f9f9 | 16 x 16, colour #f9f9f9 | 16 x 16, colour #f9f9f9 |
| Painted layers | a.group.relative 123.5x31.0 bg #f9f9f9 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 121.5x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 123.5x31.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 121.5x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 123.5x31.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px outline 1px solid #101010 offset 4px; div.group-hover:running.group-focus-visible:running 121.5x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p | a.group.relative 123.5x31.0 bg #101010 border T:1px solid #a49d9a / R:1px solid #a49d9a / B:1px solid #a49d9a / L:1px solid #a49d9a r 3px; div.group-hover:running.group-focus-visible:running 121.5x29.0 image repeating-linear-gradient(45deg, #000000 @ 0 0px, #000000 @ 0 2px, #4d4947 2px, #4d4947 3p |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta2-default.png`, `hero-cta2-hover.png`, `hero-cta2-focus-visible.png`, `hero-cta2-pressed.png`.

#### install-cmd

Install command. The mono `curl -fsSL https://app.factory.ai/cli | sh` copy box under the CTAs.

Page: home. Selector: `install command box`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 34.5 |
| Padding | 8px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | #ebebeb |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2e2c2b |
| Text node | span.text-orange-500.select-none: Geist Mono 12px/16.5px 400, #5c5855, ls -0.24px |
| Transition | none |
| Icon | 16 x 16, colour #4d4947 |
| Painted layers | div.text-base-200.relative 420.0x34.5 bg #ebebeb; span.mb-0.5.ml-0.5 8.0x16.0 bg #020202; button.group.absolute 32.0x32.0 bg #ebebeb |
| How | at rest |

Crops: `install-cmd-default.png`.

#### copy-btn

Copy button. The "Copy code" control beside the install command; measured, never clicked.

Page: home. Selector: `button Copy code`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | #ebebeb | #a49d9a @ 0.2 | = | #a49d9a @ 0.2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 2px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2e2c2b | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #4d4947 | 16 x 16, colour #2e2c2b | = | 16 x 16, colour #2e2c2b |
| Painted layers | button.group.absolute 32.0x32.0 bg #ebebeb | button.group.absolute 32.0x32.0 bg #a49d9a @ 0.2 | button.group.absolute 32.0x32.0 bg #ebebeb r 2px outline 1px solid #101010 offset 2px | button.group.absolute 32.0x32.0 bg #a49d9a @ 0.2 |
| Ancestor paint | 1 up div.text-base-200.relative bg #ebebeb | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `copy-btn-default.png`, `copy-btn-hover.png`, `copy-btn-focus-visible.png`, `copy-btn-pressed.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 778.63 x 49.27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 44px/49.28px 400 |
| Letter spacing | -1.12px |
| Colour | #020202 |
| Text node | span.char-reveal: Geist 44px/49.28px 400, #1d0f07, ls -1.12px |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Footer

#### footer

Footer. The dark page footer: sitemap columns (Resources/Company/Legal), the mark.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 430 |
| Padding | 0px |
| Gap | normal 24px |
| Border | none |
| Radius | 12px |
| Background | #101010 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #020202 |
| Text node | p.text-foreground.text-pretty: Geist 14px/14px 400, #eeeeee |
| Transition | none |
| Icon | 179.85 x 35.75, colour #020202 |
| Painted layers | footer.relative.grid 1392.0x430.0 bg #101010 r 12px; a::after.text-pretty.ds-label-1 0pxx1px bg #8a8380; a::after.text-pretty.ds-label-1 0pxx1px bg #8a8380; a::after.text-pretty.ds-label-1 0pxx1px bg #8a8380; a::after.text-pretty.ds-label-1 0pxx1px bg #8a8380; a::after.text-pretty.ds-label-1 0pxx1px bg #8a8380 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link on the dark footer; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 35 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #fafafa offset 2px | = |
| Font | Geist 14px/14px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8a8380 | oklch(0.705 0.213 47.604) | = | oklch(0.705 0.213 47.604) |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 1px, absolute, bg #8a8380, radius 0px | 35px x 1px, absolute, bg #ff6a00, radius 0px | = | 35px x 1px, absolute, bg #fb6d00, radius 0px |
| Painted layers | a::after.text-pretty.ds-label-1 0pxx1px bg #8a8380 | a::after.text-pretty.ds-label-1 35pxx1px bg #ff6a00 | a.text-pretty.ds-label-1 35.0x14.0 r 2px outline 1px solid #fafafa offset 2px; a::after.text-pretty.ds-label-1 0pxx1px bg #8a8380 | a::after.text-pretty.ds-label-1 35pxx1px bg #fb6d00 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

## Transitions declared in the readable stylesheets

factory.com serves its CSS same-origin as Next.js bundles, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- contact: `transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.22s ease-out`, `transform 0.13s ease-in, opacity 0.1s ease-in`, `color 0.15s`, `border-color 0.2s`, `background-color 0.15s`, `background-color 0.15s, opacity 0.15s`, `color 0.15s, border-color 0.15s`, `background-color 0.15s, color 0.15s`, `transform 0.2s ease-out, background-color 0.2s linear, box-shadow 0.2s`, `width 0.3s ease-in-out`, `filter 0.1s`, `box-shadow 0.2s`

- docs: `transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.22s ease-out`, `transform 0.13s ease-in, opacity 0.1s ease-in`

- enterprise: `transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.22s ease-out`, `transform 0.13s ease-in, opacity 0.1s ease-in`

- home: `transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.22s ease-out`, `transform 0.13s ease-in, opacity 0.1s ease-in`

- pricing: `transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.22s ease-out`, `transform 0.13s ease-in, opacity 0.1s ease-in`

- signin: `unset`, `inherit`, `box-shadow 0.12s`, `box-shadow 0.12s, background-color 0.12s`, `transform 0.12s`, `background-color 0.1s`, `background-position linear, background-color ease-in-out, box-shadow ease-in-out, filter ease-in-out`, `transform 0.14s cubic-bezier(0.45, 0.05, 0.55, 0.95), box-shadow 0.14s ease-in-out`, `none`, `box-shadow 0.18s`, `inline-size 0.3s cubic-bezier(0.22, 1, 0.36, 1)`, `opacity 0.15s ease-out, transform 0.15s ease-out, visibility 0.15s`

## Reduced motion

- home (`header a` under prefers-reduced-motion): transition `all`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
