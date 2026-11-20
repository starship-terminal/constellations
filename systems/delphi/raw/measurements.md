# Delphi component measurements

Computed styles read from www.delphi.co on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — home, /discover/<topic>, public /search/<question> results, public /<expert> profiles and /<expert>/chat, and the Sign-In/onboarding dialogs, and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and navigation

#### mkt-header

Site header. The fixed top bar: Delphi wordmark, Sign In and the Create Your Delphi pill.

Page: home. Selector: `header.fixed`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px 20px 0px 12px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | a.group/button.inline-flex: Delphi Inter 14px/20px 500, #63635e |
| Transition | translate, opacity, visibility 0.3s cubic-bezier(0.3, 0.9, 0.25, 1) |
| Icon | 84.5 x 26, colour #82827c |
| ::before | 1440px x 0px, fixed, bg #ffffff, radius 0px |
| Painted layers | header::before.fixed.inset-x-0 1440pxx0px bg #ffffff; div.absolute.inset-x-0 1440.0x88.0 image linear-gradient(#ffffff 0%, #ffffff @ 0.9888 6.25%, #ffffff @ 0.957 12.5%, #ffffff @ 0.907; a.group/button.inline-flex 96.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px; a.group/button.inline-flex 180.0x36.0 bg oklch(0.67 0.22 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Delphi mark at the left of the header.

Page: home. Selector: `header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 91.5 x 40 |
| Padding | 0px 0px 0px 7px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #82827c |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 84.5 x 26, colour #82827c |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-topic

Topic link. A topic link in the header/category strip ("Career & Work"); measured, never followed.

Page: home. Selector: `topic link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79 x 40 | = | = | 77.42 x 39.2 |
| Padding | 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #8d8d86 @ 0.1 | #8d8d86 @ 0.15 | = | #8d8d86 @ 0.15 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #fd5400 @ 0.5 offset 1px | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63635e | #21201c | = | #21201c |
| Transition | all 0.2s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.shrink-0.cursor-pointer 79.0x40.0 bg #8d8d86 @ 0.1 r 3.35544e+07px | a.shrink-0.cursor-pointer 79.0x40.0 bg #8d8d86 @ 0.15 r 3.35544e+07px | a.shrink-0.cursor-pointer 79.0x40.0 bg #8d8d86 @ 0.1 r 3.35544e+07px outline 1px auto #fd5400 @ 0.5 offset 1px | a.shrink-0.cursor-pointer 77.4x39.2 bg #8d8d86 @ 0.15 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-topic-default.png`, `nav-topic-hover.png`, `nav-topic-focus-visible.png`, `nav-topic-pressed.png`.

#### signin-btn

Sign In. The header Sign-In action; it opens the auth dialog (measured below), never followed past it.

Page: home. Selector: `header Sign In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96 x 36 | = | = | 94.08 x 35.28 |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | = |
| Radius | 26px | = | = | = |
| Background | transparent | #8d8d86 @ 0.1 | = | #8d8d86 @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63635e | #21201c | = | #21201c |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.6 x 13.6, colour #63635e, fill #000000 | 13.6 x 13.6, colour #21201c, fill #000000 | = | 13.33 x 13.33, colour #21201c, fill #000000 |
| Painted layers | a.group/button.inline-flex 96.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 96.0x36.0 bg #8d8d86 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 96.0x36.0 border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 94.1x35.3 bg #8d8d86 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-btn-default.png`, `signin-btn-hover.png`, `signin-btn-focus-visible.png`, `signin-btn-pressed.png`.

#### create-cta

Create CTA. The "Create Your Delphi" primary pill in the header; measured, never followed (it starts onboarding).

Page: home. Selector: `header Create Your Delphi`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 36 | = | = | 176.4 x 35.28 |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | = |
| Radius | 26px | = | = | = |
| Background | oklch(0.67 0.22 42) | oklch(0.6 0.21 42) | = | oklch(0.6 0.21 42) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.6 x 13.6, colour #ffffff, fill #000000 | = | = | 13.33 x 13.33, colour #ffffff, fill #000000 |
| Painted layers | a.group/button.inline-flex 180.0x36.0 bg oklch(0.67 0.22 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 180.0x36.0 bg oklch(0.6 0.21 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 180.0x36.0 bg oklch(0.67 0.22 42) border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 176.4x35.3 bg oklch(0.6 0.21 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `create-cta-default.png`, `create-cta-hover.png`, `create-cta-focus-visible.png`, `create-cta-pressed.png`.

### Home

#### hero-h1

Hero headline. "Find people who’ve been there" — the Pythia serif display heading.

Page: home. Selector: `h1.font-heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 597.25 x 51 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Pythia 50px/51px 500 |
| Letter spacing | -1.75px |
| Colour | #21201c |
| Transition | none |
| ::before | 821.25px x 115px, absolute, bg #000000 @ 0 radial-gradient(#fcf8f3 30%, #fcf8f3 @ 0.92 48%, #000000 @ 0 74%), radius 50% |
| Painted layers | h1::before.font-heading 821.25pxx115px image radial-gradient(#fcf8f3 30%, #fcf8f3 @ 0.92 48%, #000000 @ 0 74%) r 50% |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-search

Ask field. The "Describe your situation" hero textarea — the product’s front door; focused and typed into then cleared, never submitted.

Page: home. Selector: `textarea[aria-label=Search Delphi]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 624 x 52 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = |
| Font | Delphi Inter 18px/26px 400 | = | = |
| Letter spacing | -0.18px | = | = |
| Colour | #21201c | = | = |
| Transition | color, background-color, border-color, box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #63635e, opacity 1 | = | = |
| Painted layers | textarea.min-w-0.placeholder:text-fg-mid 624.0x52.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | clicked into the field | typed "how do i find a co-founder", then deleted; nothing sent |

Crops: `hero-search-default.png`, `hero-search-focused.png`, `hero-search-filled.png`.

#### mic-btn

Voice button. The "Say your situation" mic button beside the ask field; measured, never pressed (it would start recording).

Page: home. Selector: `Say your situation`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | #e9e8e6 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.992 0px 0px 0px 1.98098px, #fd5400 @ 0.990492 0px 0px 0px 3.96197px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63635e | = | = | #21201c |
| Transition | opacity, transform, background-color, color, box-shadow 0.4s, 0.4s, 0.4s, 0.4s, 0.4s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17 x 17, colour #63635e, fill #000000 | = | = | 17 x 17, colour #21201c, fill #000000 |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.inline-flex.shrink-0 32.0x32.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.992 0px 0px 0px 1.98098px, #fd5400 @ 0.990492 0px 0px 0px 3.96197px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.shrink-0 32.0x32.0 bg #e9e8e6 r 3.35544e+07px |

Crops: `mic-btn-default.png`, `mic-btn-hover.png`, `mic-btn-focus-visible.png`, `mic-btn-pressed.png`.

#### topic-card

Topic card. A shuffled topic card ("Ask ex-Googlers about scaling under pressure"); measured, never pressed.

Page: home. Selector: `button.deck-card.topic-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 346.66 x 280 | = | = | = |
| Padding | 20px | = | = | = |
| Gap | 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #f7f3f0 | = | = | = |
| Background image | radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 72%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #21201c offset 4px | = |
| Font | Delphi Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #23211f | = | = | = |
| Text node | span.topic-ask.font-heading: Delphi Pythia 22px/25.3px 600, #23211f, ls -0.55px | = | = | = |
| Transition | translate, box-shadow 0.26s, 0.26s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #23211f | = | = | = |
| Painted layers | button.deck-card.topic-card 346.7x280.0 bg #f7f3f0 image radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 r 24px; span::before.deck-glow 429.844pxx347.188px image radial-gradient(150% 120% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.32), #000000 @ ; span.brand-tag.topic-tag 100.9x24.0 bg #000000 @ 0.06 r 6px | = | button.deck-card.topic-card 346.7x280.0 bg #f7f3f0 image radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 r 24px outline 2px solid #21201c offset 4px; span::before.deck-glow 429.844pxx347.188px image radial-gradient(150% 120% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.32), #000000 @ ; span.brand-tag.topic-tag 100.9x24.0 bg #000000 @ 0.06 r 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topic-card-default.png`, `topic-card-hover.png`, `topic-card-focus-visible.png`, `topic-card-pressed.png`.

#### persp-card

Expert card. An expert portrait card on the home rail (name, claim, the Read-perspective flip).

Page: home. Selector: `div.perspective-flip-front`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 272 x 360 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | span: Delphi Pythia 24px/25.2px 500, #ffffff, ls -0.6px |
| Transition | none |
| Cursor | grab |
| Icon | 20.02 x 20.02, colour #ffffff |
| Painted layers | div.perspective-flip-front 272.2x360.3 bg #f7f3f0 r 28px shadow oklch(0.67 0.22 42) 0px 0px 0px 2px, color(srgb 0.990616 0.33041 -0.139183 / 0.85) 0px 12px 28px -8px; span.portrait-well.relative 272.2x360.3 bg #f7f3f0; span.perspective-scrim 272.2x198.2 image linear-gradient(#000000 @ 0, #000000 @ 0.35 50%, #000000 @ 0.8); button.group/button.inline-flex 272.2x360.3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 28px; a.group/badge.inline-flex 232.2x45.8 bg #ffffff @ 0.18 r 12px shadow #ffffff @ 0.22 0px 0px 0px 1px inset; div.perspective-flip-back 271.8x359.7 bg #3c4534 r 28px shadow oklch(0.67 0.22 42) 0px 0px 0px 2px, color(srgb 0.990616 0.33041 -0.139183 / 0.85) 0px 12px 28px -8px |
| How | at rest |

Crops: none.

#### persp-flip

Perspective flip. The "Read <name>’s perspective" card toggle — a local flip, never a navigation.

Page: home. Selector: `button[aria-label*=perspective]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 272.23 x 360.3 | = | = | 266.78 x 353.09 |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | = |
| Radius | 28px | 133.769px 133.769px 28px 28px | 127.551px 127.551px 28px 28px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid oklch(0.67 0.22 42) offset -5px | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63635e | #21201c | = | #21201c |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group/button.inline-flex 272.2x360.3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 28px | button.group/button.inline-flex 272.2x360.3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 133.769px 133.769px 28px 28px | button.group/button.inline-flex 272.2x360.3 border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 127.551px 127.551px 28px 28px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px outline 2px solid oklch(0.67 0.22 42) offset -5px | button.group/button.inline-flex 266.8x353.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 28px |
| Ancestor paint | 1 up div.perspective-flip-front bg #f7f3f0 shadow oklch(0.67 0.22 42) 0px 0px 0px 2px, color(srgb 0.990616 0.33041 -0.139183 / 0.85) 0px 12px 28px -8px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `persp-flip-default.png`, `persp-flip-hover.png`, `persp-flip-focus-visible.png`, `persp-flip-pressed.png`.

#### persp-quote

Perspective quote. A quoted perspective on a card ("Nir on why we reach for our phones...").

Page: home. Selector: `blockquote.font-heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 227.81 x 171.29 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Pythia 18px/21.96px 500 |
| Letter spacing | -0.27px |
| Colour | #f0eae4 |
| Text node | span.perspective-flip-on: Delphi Inter 13px/15.86px 500, #f0eae4, ls -0.27px |
| Transition | none |
| Cursor | grab |
| Ancestor paint | 1 up div.perspective-flip-back bg #3c4534 shadow oklch(0.67 0.22 42) 0px 0px 0px 2px, color(srgb 0.990616 0.33041 -0.139183 / 0.85) 0px 12px 28px -8px |
| How | at rest |

Crops: `persp-quote-default.png`.

#### section-h2

Section heading. A home section heading ("Ask people who’ve lived it").

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 228 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 20px/28px 500 |
| Letter spacing | -0.5px |
| Colour | #21201c |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Footer

#### site-footer

Site footer. The sitemap footer (Discover / About Delphi / Blog / Premium...).

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 242.88 |
| Padding | 0px 40px 24px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | a.text-fg-mid.hover:text-fg-high: Delphi Inter 14px/20px 400, #63635e |
| Transition | none |
| Icon | 78 x 24, colour #21201c |
| Painted layers | div.shrink-0.data-horizontal:h-px 1072.0x1.0 bg #8d8d86 @ 0.12 |
| Ancestor paint | 1 up div.advice-landing.advice-landing-surface bg #f9f9f8 |
| How | at rest |

Crops: `site-footer-default.png`.

### Auth and onboarding dialogs

#### signin-dialog

Sign-in dialog. The auth dialog opened by the header Sign In (Continue with Google / Continue with Email); its buttons were measured, never pressed.

Page: home. Selector: `[role=dialog]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448 x 360 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 26px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #21201c @ 0.05 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Outline | none |
| Font | Delphi Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | h2.cn-font-heading.text-balance: Delphi Inter 24px/32px 500, #21201c, ls -0.6px |
| Transition | all 0.1s ease |
| Icon | 13.6 x 13.6, colour #63635e, fill #000000 |
| Painted layers | div.fixed.top-1/2 448.0x360.0 bg #ffffff r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #21201c @ 0.05 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.pointer-events-none.absolute 0.0x0.0 bg #dad9d6 r 3.35544e+07px; button.group/button.inline-flex 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px; button.group/button.inline-flex 400.0x40.0 bg #21201c border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px; div.data-horizontal:h-px.data-horizontal:w-full 169.7x1.0 bg #8d8d86 @ 0.12; div.data-horizontal:h-px.data-horizontal:w-full 169.7x1.0 bg #8d8d86 @ 0.12 |
| How | at rest |

Crops: `signin-dialog-default.png`.

#### dialog-google

Google SSO button. "Continue with Google" inside the auth dialog; measured, never pressed.

Page: home. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 40 | = | = | 392 x 39.2 |
| Padding | 0px 16px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | 1px solid oklch(0.67 0.22 42) |
| Radius | 26px | = | = | = |
| Background | #21201c | #63635e | #63635e | #63635e |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.6 x 13.6, colour #ffffff, fill #000000 | = | = | 13.33 x 13.33, colour #ffffff, fill #000000 |
| Painted layers | button.group/button.inline-flex 400.0x40.0 bg #21201c border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | button.group/button.inline-flex 400.0x40.0 bg #63635e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | button.group/button.inline-flex 400.0x40.0 bg #63635e border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 392.0x39.2 bg #63635e border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dialog-google-default.png`, `dialog-google-hover.png`, `dialog-google-focus-visible.png`, `dialog-google-pressed.png`.

#### dialog-email

Email button. "Continue with Email" inside the auth dialog; measured, never pressed.

Page: home. Selector: `Continue with Email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 40 | = | = | 392 x 39.2 |
| Padding | 0px 16px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | 1px solid oklch(0.67 0.22 42) |
| Radius | 26px | = | = | = |
| Background | #8d8d86 @ 0.1 | #8d8d86 @ 0.15 | #8d8d86 @ 0.15 | #8d8d86 @ 0.15 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #21201c | = | = | = |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.6 x 13.6, colour #21201c, fill #000000 | = | = | 13.33 x 13.33, colour #21201c, fill #000000 |
| Painted layers | button.group/button.inline-flex 400.0x40.0 bg #8d8d86 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | button.group/button.inline-flex 400.0x40.0 bg #8d8d86 @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | button.group/button.inline-flex 400.0x40.0 bg #8d8d86 @ 0.15 border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 392.0x39.2 bg #8d8d86 @ 0.15 border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dialog-email-default.png`, `dialog-email-hover.png`, `dialog-email-focus-visible.png`, `dialog-email-pressed.png`.

### Discover galleries

#### disc-h1

Gallery headline. "Productivity advice from people who’ve been there" — the topic gallery heading.

Page: discover. Selector: `h1.font-heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 102 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Pythia 50px/51px 500 |
| Letter spacing | -1.75px |
| Colour | #21201c |
| Transition | none |
| ::before | 924px x 166px, absolute, bg #000000 @ 0 radial-gradient(#fcf8f3 30%, #fcf8f3 @ 0.92 48%, #000000 @ 0 74%), radius 50% |
| Painted layers | h1::before.font-heading 924pxx166px image radial-gradient(#fcf8f3 30%, #fcf8f3 @ 0.92 48%, #000000 @ 0 74%) r 50% |
| How | at rest |

Crops: `disc-h1-default.png`.

#### disc-cats

Topic chip strip. The category chip strip under the gallery heading (Career & Work / Money & Business / ...).

Page: discover. Selector: `.hl-topic-ripples`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1072 x 320.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | span.hl-topic-name: Delphi Inter 13px/13px 400, #63635e |
| Transition | none |
| Icon | 1440 x 520, colour #21201c @ 0.07, fill #000000 |
| Painted layers | span.hl-ripples-paper 1440.0x788.6 image linear-gradient(#fcf8f3 62%, #f9f9f8); span.hl-ripples-warmth 1440.0x544.6 image radial-gradient(520px 300px at 50% 300px, color(srgb 0.990616 0.33041 -0.139183 / 0.04), #; span.breath-fallback.absolute 1440.0x570.6 image radial-gradient(80% 52% at 46% 40%, #ff9e66 @ 0.56 0%, #000000 @ 0 70%), radial-gradient(7; span.hl-topic-pill 136.0x32.0 bg #f2eee9 r 999px; span.hl-topic-pill 158.0x32.0 bg #f2eee9 r 999px; span.hl-topic-pill 155.0x32.0 bg #f2eee9 r 999px |
| How | at rest |

Crops: `disc-cats-default.png`.

#### disc-cat

Topic chip. A category chip in the gallery strip; measured, never followed.

Page: discover. Selector: `topic chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79 x 40 | = | = | 77.43 x 39.2 |
| Padding | 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #8d8d86 @ 0.1 | #8d8d86 @ 0.15 | = | #8d8d86 @ 0.149813 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #fd5400 @ 0.5 offset 1px | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63635e | #21201c | = | #21201c |
| Transition | all 0.2s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.shrink-0.cursor-pointer 79.0x40.0 bg #8d8d86 @ 0.1 r 3.35544e+07px | a.shrink-0.cursor-pointer 79.0x40.0 bg #8d8d86 @ 0.15 r 3.35544e+07px | a.shrink-0.cursor-pointer 79.0x40.0 bg #8d8d86 @ 0.1 r 3.35544e+07px outline 1px auto #fd5400 @ 0.5 offset 1px | a.shrink-0.cursor-pointer 77.4x39.2 bg #8d8d86 @ 0.149813 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `disc-cat-default.png`, `disc-cat-hover.png`, `disc-cat-focus-visible.png`, `disc-cat-pressed.png`.

#### disc-quote

Gallery quote. A quoted expert perspective in the gallery.

Page: discover. Selector: `blockquote`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 227.81 x 149.36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Pythia 18px/21.96px 500 |
| Letter spacing | -0.27px |
| Colour | #f0eae4 |
| Text node | span.perspective-flip-on: Delphi Inter 13px/15.86px 500, #f0eae4, ls -0.27px |
| Transition | none |
| Cursor | grab |
| Ancestor paint | 1 up div.perspective-flip-back bg #343d34 |
| How | at rest |

Crops: `disc-quote-default.png`.

#### disc-card

Expert tile. An expert portrait tile in the gallery grid.

Page: discover. Selector: `portrait card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 528 x 192 |
| Padding | 24px 24px 18px 24px |
| Gap | 12px |
| Border | 1px solid #21201c @ 0.09 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | h3: Delphi Inter 23px/29.9px 500, #63635e, ls -0.46px |
| Transition | box-shadow, transform, background-color, border-color 0.26s, 0.26s, 0.18s, 0.26s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.165, 0.84, 0.44, 1), ease delay 0s, 0s, 0s, 0s |
| Painted layers | div.group/card.flex 528.0x192.0 bg #ffffff border T:1px solid #21201c @ 0.09 / R:1px solid #21201c @ 0.09 / B:1px solid #21201c @ 0.09 / L:1px solid #21201c @ 0.09 r 24px; a.group/button.inline-flex 526.0x190.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px; span::before.q-glow 526pxx190px image radial-gradient(150% 120% at 50% 118%, color(srgb 0.990616 0.33041 -0.139183 / 0.14), #000; span.brand-tag.question-tag 108.9x24.0 bg #21201c @ 0.06 r 6px; span.portrait-well.relative 28.9x36.7 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50% 50% 16% 16% / 40% 40% 12% 12% shadow #21201c @ 0.08 0px 0px 0px 1px; span.portrait-well.relative 28.9x36.7 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50% 50% 16% 16% / 40% 40% 12% 12% shadow #21201c @ 0.08 0px 0px 0px 1px |
| How | at rest |

Crops: `disc-card-default.png`.

#### disc-ask

Ask card. A gallery "Ask <group> about <topic>" card; measured, never pressed.

Page: discover. Selector: `button.deck-card.topic-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 346.66 x 280 | = | = | = |
| Padding | 20px | = | = | = |
| Gap | 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #f7f3f0 | = | = | = |
| Background image | radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 72%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #21201c offset 4px | = |
| Font | Delphi Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #23211f | = | = | = |
| Text node | span.topic-ask.font-heading: Delphi Pythia 22px/25.3px 600, #23211f, ls -0.55px | = | = | = |
| Transition | translate, box-shadow 0.26s, 0.26s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #23211f | = | = | = |
| Painted layers | button.deck-card.topic-card 346.7x280.0 bg #f7f3f0 image radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 r 24px; span::before.deck-glow 429.844pxx347.188px image radial-gradient(150% 120% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.32), #000000 @ ; span.brand-tag.topic-tag 108.9x24.0 bg #000000 @ 0.06 r 6px | = | button.deck-card.topic-card 346.7x280.0 bg #f7f3f0 image radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 r 24px outline 2px solid #21201c offset 4px; span::before.deck-glow 429.844pxx347.188px image radial-gradient(150% 120% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.32), #000000 @ ; span.brand-tag.topic-tag 108.9x24.0 bg #000000 @ 0.06 r 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `disc-ask-default.png`, `disc-ask-hover.png`, `disc-ask-focus-visible.png`, `disc-ask-pressed.png`.

### Search results

#### srch-top

Top perspectives. The "Top perspectives" results heading over the quoted answers.

Page: search. Selector: `Top perspectives`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 150 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 18px/28px 500 |
| Letter spacing | normal |
| Colour | #63635e |
| Transition | none |
| How | at rest |

Crops: `srch-top-default.png`.

#### srch-personalize

Personalize link. The "Personalize your results" action; measured, never followed.

Page: search. Selector: `Personalize your results`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #fd5400 @ 0.5 offset 1px | = |
| Font | Delphi Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63635e | #f48734 | = | #f48734 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.6 x 13.6, colour #63635e, fill #000000 | 13.6 x 13.6, colour #f48734, fill #000000 | = | 13.6 x 13.6, colour #f48734, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.inline-flex.items-center 180.0x20.0 outline 1px auto #fd5400 @ 0.5 offset 1px | = |

Crops: `srch-personalize-default.png`, `srch-personalize-hover.png`, `srch-personalize-focus-visible.png`, `srch-personalize-pressed.png`.

#### srch-quote

Result quote. A quoted expert answer in the results.

Page: search. Selector: `blockquote`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 630 x 82 |
| Padding | 14px 16px 20px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | span.mr-0.5.text-fg-low: Delphi Inter 16px/24px 400, #82827c |
| Transition | none |
| Icon | 20 x 20, colour #63635e |
| ::before | 630px x 82px, absolute, bg #f1f1f0 radial-gradient(42% 120% at 50% calc(160%), oklch(0.67 0.22 42 / 0.16) 0%, #000000 @ 0 100%), radius 14px |
| ::after | 40px x 44px, absolute, bg #f1f1f0, radius 0px |
| Painted layers | blockquote::before.perspective-bubble.relative 630pxx82px bg #f1f1f0 image radial-gradient(42% 120% at 50% calc(160%), oklch(0.67 0.22 42 / 0.16) 0%, #000000 @ 0 100 r 14px; blockquote::after.perspective-bubble.relative 40pxx44px bg #f1f1f0 |
| How | at rest |

Crops: `srch-quote-default.png`.

#### srch-expert-card

Result expert card. An expert result card (portrait, name, role, badges, quoted answer, Save/Expand).

Page: search. Selector: `result card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 318 |
| Padding | 18px 0px 20px 0px |
| Gap | 24px |
| Border | 1px solid #8d8d86 @ 0.2 |
| Radius | 26px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | span.-my-1.py-1: Delphi Pythia 24px/28px 600, #21201c, ls -0.6px |
| Transition | box-shadow, --quote-glow 0.2s, 1.8s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.3, 0, 0, 1) delay 0s, 0s |
| Icon | 24 x 24, colour #21201c |
| Painted layers | div.group/card.flex 672.0x318.0 bg #ffffff border T:1px solid #8d8d86 @ 0.2 / R:1px solid #8d8d86 @ 0.2 / B:1px solid #8d8d86 @ 0.2 / L:1px solid #8d8d86 @ 0.2 r 26px; span.avatar-squircle.group/avatar 56.0x56.0 bg #ffffff border T:1px solid #8d8d86 @ 0.12 / R:1px solid #8d8d86 @ 0.12 / B:1px solid #8d8d86 @ 0.12 / L:1px solid #8d8d86 @ 0.12 r 28%; span.brand-tag.brand-tag-compact 228.0x20.0 bg #21201c @ 0.06 r 6px; span.brand-tag.brand-tag-compact 335.4x20.0 bg #21201c @ 0.06 r 6px; span.brand-tag.brand-tag-compact 213.0x20.0 bg #21201c @ 0.06 r 6px; span.relative.flex 12.0x12.0 bg #ffffff r 3.36px |
| How | at rest |

Crops: `srch-expert-card-default.png`.

#### srch-badge

Credential badge. A credential badge on a result card ("VP OF GLOBAL COMMUNITY AT TORC").

Page: search. Selector: `span.brand-tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 228 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 6px |
| Background | #21201c @ 0.06 |
| Box shadow | none |
| Outline | none |
| Font | Delphi Pythia 10px/10px 600 |
| Letter spacing | 0.8px |
| Colour | #63635e |
| Text node | span.brand-tag-label: Delphi Pythia 10px/20px 600, #63635e, ls 0.8px |
| Transition | none |
| Painted layers | span.brand-tag.brand-tag-compact 228.0x20.0 bg #21201c @ 0.06 r 6px |
| How | at rest |

Crops: `srch-badge-default.png`.

#### srch-field

Query field. The large query textarea at the top of results, pre-filled with the asked question; focused, never submitted.

Page: search. Selector: `results textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 664 x 72 | = |
| Padding | 16px 48px 8px 20px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Delphi Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #21201c | = |
| Transition | color, background-color, border-color, box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = |
| Cursor | text | = |
| Placeholder | #63635e, opacity 1 | = |
| Painted layers | textarea.min-w-0.resize-none 664.0x72.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | clicked into the field |

Crops: `srch-field-default.png`, `srch-field-focused.png`.

#### srch-save

Save button. The card’s "Save" action; measured, never pressed.

Page: search. Selector: `Save`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 36 | = | = | 79.38 x 35.28 |
| Padding | 0px 12px 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | = |
| Radius | 26px | = | = | = |
| Background | transparent | #8d8d86 @ 0.1 | = | #8d8d86 @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63635e | #21201c | = | #21201c |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.6 x 13.6, colour #63635e, fill #000000 | 13.6 x 13.6, colour #21201c, fill #000000 | = | 13.33 x 13.33, colour #21201c, fill #000000 |
| Painted layers | a.group/button.inline-flex 81.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 81.0x36.0 bg #8d8d86 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 81.0x36.0 border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 79.4x35.3 bg #8d8d86 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `srch-save-default.png`, `srch-save-hover.png`, `srch-save-focus-visible.png`, `srch-save-pressed.png`.

#### srch-expand

Expand button. The orange "Expand" card action; measured, never followed.

Page: search. Selector: `Expand`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97 x 36 | = | = | 95.06 x 35.28 |
| Padding | 0px 10px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | = |
| Radius | 26px | = | = | = |
| Background | oklch(0.67 0.22 42) | oklch(0.6 0.21 42) | = | oklch(0.6 0.21 42) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.6 x 13.6, colour #ffffff, fill #000000 | = | = | 13.33 x 13.33, colour #ffffff, fill #000000 |
| Painted layers | a.group/button.inline-flex 97.0x36.0 bg oklch(0.67 0.22 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 97.0x36.0 bg oklch(0.6 0.21 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 97.0x36.0 bg oklch(0.67 0.22 42) border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 95.1x35.3 bg oklch(0.6 0.21 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 3 up div.group/card.flex bg #ffffff shadow #ffffff 0px 2px 2px 0px inset, #000000 @ 0.03 0px 10.213px 10.213px -5.107px, #000000 @ 0.03 0px 5.107px 5.107px -2.553px, #000000 @ 0.03 0px 2.553px 2.553px -2px, #000000 @ 0.03 0px 0.638px 0.638px -0.319px | = | = |

Crops: `srch-expand-default.png`, `srch-expand-hover.png`, `srch-expand-focus-visible.png`, `srch-expand-pressed.png`.

### Expert profile

#### exp-name

Expert name. The expert’s display name heading on their public profile.

Page: expert. Selector: `expert h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 418.19 x 41.47 |
| Padding | 0px 23.8px 4.08px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Pythia 34px/37.4px 600 |
| Letter spacing | -0.85px |
| Colour | #21201c |
| Transition | none |
| Icon | 17 x 17, colour #21201c |
| How | at rest |

Crops: `exp-name-default.png`.

#### exp-portrait

Expert portrait. The expert’s portrait photo in the profile header.

Page: expert. Selector: `profile img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 110 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | -0.24px |
| Colour | #000000 @ 0 |
| Transition | none |
| Ancestor paint | 1 up span.avatar-squircle.group/avatar bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 32.25px 32.25px 0px, #000000 @ 0.1 0px 17.2px 17.2px -8.6px, #000000 @ 0.03 0px 8.6px 8.6px -4.3px, #000000 @ 0.05 0px 4.3px 4.3px -2.15px, #000000 @ 0.05 0px 1.075px 1.075px -0.538px, #ffffff @ 0.5 0px 2px 4px 0px inset, #ffffff @ 0.4 0px -2px 4px 0px inset |
| How | at rest |

Crops: `exp-portrait-default.png`.

#### share-btn

Share button. The "Share" profile action; measured, never pressed.

Page: expert. Selector: `Share`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.81 x 40 | = | = | 76.26 x 39.2 |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | = |
| Radius | 26px | = | = | = |
| Background | #21201c @ 0.1 | = | = | #21201c @ 0.15 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Backdrop filter | blur(4px) | = | = | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 16px/24px 450 | = | = | = |
| Letter spacing | -0.24px | = | = | = |
| Colour | #63635e | = | = | #21201c |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group/button.inline-flex 77.8x40.0 bg #21201c @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | = | button.group/button.inline-flex 77.8x40.0 bg #21201c @ 0.1 border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 76.3x39.2 bg #21201c @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `share-btn-default.png`, `share-btn-focus-visible.png`, `share-btn-pressed.png`.

#### exp-about

About text. The expert’s About copy on the profile.

Page: expert. Selector: `about text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | -0.08px |
| Colour | #82827c |
| Transition | none |
| How | at rest |

Crops: `exp-about-default.png`.

#### exp-section

Profile section. A profile section heading ("Experiences").

Page: expert. Selector: `profile h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 22.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 18px/22.5px 500 |
| Letter spacing | -0.24px |
| Colour | #161615 |
| Transition | none |
| How | at rest |

Crops: `exp-section-default.png`.

#### exp-exp-item

Experience item. A listed experience on the profile.

Page: expert. Selector: `experience item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655 x 77.5 |
| Padding | 14px 12px 0px 6px |
| Border | none |
| Radius | 20px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | -0.24px |
| Colour | #21201c |
| Text node | span.min-w-0.truncate: Delphi Inter 14px/20px 400, #6b6b67, ls -0.24px |
| Transition | none |
| Painted layers | div.mt-3.5.h-px 637.0x1.0 bg #1c1814 @ 0.06 |
| How | at rest |

Crops: none.

### Chat surface

#### chat-name

Chat expert name. The expert’s name in the chat header.

Page: chat. Selector: `chat header name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 163 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | span.truncate.text-sm: Delphi Inter 14px/20px 500, #21201c |
| Transition | none |
| Icon | 13.6 x 13.6, colour #63635e, fill #000000 |
| Painted layers | span.avatar-squircle.group/avatar 48.0x48.0 bg #ffffff border T:1px solid #8d8d86 @ 0.12 / R:1px solid #8d8d86 @ 0.12 / B:1px solid #8d8d86 @ 0.12 / L:1px solid #8d8d86 @ 0.12 r 28% shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 32.25px 32.25px 0px, #000000 @ 0.1 0px 17.2px 17.2px -8.6px, #000000 @ 0.03 0px 8.6px 8.6px -4.3px, #000000 @ 0.05 0px 4.3px 4.3px -2.15px, #000000 @ 0.05 0px 1.075px 1.075px -0.538px, #ffffff @ 0.5 0px 2px 4px 0px inset, #ffffff @ 0.4 0px -2px 4px 0px inset; span.avatar-squircle.pointer-events-none 46.0x46.0 r 28% shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.5 0px 2px 4px 0px inset, #ffffff @ 0.4 0px -2px 4px 0px inset; div.mx-auto.flex 163.0x34.0 bg #ffffff border T:1px solid #8d8d86 @ 0.12 / R:1px solid #8d8d86 @ 0.12 / B:1px solid #8d8d86 @ 0.12 / L:1px solid #8d8d86 @ 0.12 r 3.35544e+07px shadow #000000 @ 0.1 0px 2px 12px -2px, #000000 @ 0.08 0px 4px 20px -4px |
| Ancestor paint | 1 up main.relative.flex bg #ffffff |
| How | at rest |

Crops: none.

#### chat-greeting

Greeting bubble. The clone’s opening message ("Hi there. What problem you trying to solve?").

Page: chat. Selector: `greeting bubble`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 287 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #63635e |
| Transition | none |
| How | at rest |

Crops: `chat-greeting-default.png`.

#### suggested-label

Suggested label. The "Suggested" label over the starter questions.

Page: chat. Selector: `Suggested`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 752 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | button.group/button.inline-flex: Delphi Inter 12px/16px 500, #82827c |
| Transition | none |
| Icon | 8.5 x 8.5, colour #82827c, fill #000000 |
| Painted layers | button.group/button.inline-flex 88.0x26.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.group/button.inline-flex 20.0x20.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `suggested-label-default.png`.

#### suggested-chip

Suggested question. A suggested starter question chip; measured, never pressed — pressing it would send the question.

Page: chat. Selector: `suggested chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 245.33 x 83.75 | = | = | 240.42 x 82.07 |
| Padding | 12px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid oklch(0.67 0.22 42) | = |
| Radius | 18px | = | = | = |
| Background | #8d8d86 @ 0.1 | #8d8d86 @ 0.15 | = | #8d8d86 @ 0.15 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/19.25px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #21201c | = | = | = |
| Transition | color, background-color, border-color, box-shadow, transform, opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group/button.inline-flex 245.3x83.8 bg #8d8d86 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px | button.group/button.inline-flex 245.3x83.8 bg #8d8d86 @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px | button.group/button.inline-flex 245.3x83.8 bg #8d8d86 @ 0.1 border T:1px solid oklch(0.67 0.22 42) / R:1px solid oklch(0.67 0.22 42) / B:1px solid oklch(0.67 0.22 42) / L:1px solid oklch(0.67 0.22 42) r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fd5400 @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 240.4x82.1 bg #8d8d86 @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `suggested-chip-default.png`, `suggested-chip-hover.png`, `suggested-chip-focus-visible.png`, `suggested-chip-pressed.png`.

#### chat-input

Message field. The "Send a message..." composer; focused and typed into then cleared, never submitted.

Page: chat. Selector: `chat textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 592 x 52 | = | = |
| Padding | 12px 4px 12px 12px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #21201c 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = |
| Font | Delphi Inter 18px/28px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #21201c | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #82827c, opacity 1 | = | = |
| Painted layers | textarea.text-fg-high.placeholder:text-fg-low 592.0x52.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #21201c 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | clicked into the field | typed "what should i learn next", then deleted; nothing sent |

Crops: `chat-input-default.png`, `chat-input-focused.png`, `chat-input-filled.png`.

#### chat-send

Send button. The composer submit button — it only renders once text is in the field; its states were measured but it was never pressed, and the text was cleared.

Page: chat. Selector: `send button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | 45.6 x 45.6 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | oklch(0.67 0.22 42) | = | = | = |
| Box shadow | #000000 @ 0.05 0px 24.348px 24.348px 0px, #ef05f0 @ 0 0px 12.986px 12.986px -6.493px, #000000 @ 0.05 0px 6.493px 6.493px -3.246px, #000000 @ 0.05 0px 3.246px 3.246px -1.623px, #ef5f00 @ 0.05 0px 0.812px 0.812px -0.406px, #000000 @ 0.04 0px 0px 0px 0.812px, #ffffff @ 0.2 0px -1.623px 1.623px 0px inset, #ffffff @ 0.2 0px 1.623px 1.623px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | Delphi Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity, transform, background-color, color, box-shadow 0.4s, 0.4s, 0.4s, 0.4s, 0.4s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17 x 17, colour #ffffff, fill #000000 | = | = | 16.15 x 16.15, colour #ffffff, fill #000000 |
| Painted layers | button.inline-flex.shrink-0 48.0x48.0 bg oklch(0.67 0.22 42) r 3.35544e+07px shadow #000000 @ 0.05 0px 24.348px 24.348px 0px, #ef05f0 @ 0 0px 12.986px 12.986px -6.493px, #000000 @ 0.05 0px 6.493px 6.493px -3.246px, #000000 @ 0.05 0px 3.246px 3.246px -1.623px, #ef5f00 @ 0.05 0px 0.812px 0.812px -0.406px, #000000 @ 0.04 0px 0px 0px 0.812px, #ffffff @ 0.2 0px -1.623px 1.623px 0px inset, #ffffff @ 0.2 0px 1.623px 1.623px 0px inset | = | = | button.inline-flex.shrink-0 45.6x45.6 bg oklch(0.67 0.22 42) r 3.35544e+07px shadow #000000 @ 0.05 0px 24.348px 24.348px 0px, #ef05f0 @ 0 0px 12.986px 12.986px -6.493px, #000000 @ 0.05 0px 6.493px 6.493px -3.246px, #000000 @ 0.05 0px 3.246px 3.246px -1.623px, #ef5f00 @ 0.05 0px 0.812px 0.812px -0.406px, #000000 @ 0.04 0px 0px 0px 0.812px, #ffffff @ 0.2 0px -1.623px 1.623px 0px inset, #ffffff @ 0.2 0px 1.623px 1.623px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `chat-send-default.png`, `chat-send-hover.png`, `chat-send-focus-visible.png`, `chat-send-pressed.png`.

#### scroll-bottom

Scroll-to-bottom. The "Scroll to bottom" helper pill; measured, never pressed.

Page: chat. Selector: `Scroll to bottom`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30.4 x 30.4 | = | - | 31.36 x 31.36 |
| Padding | 0px | = | - | = |
| Border | 1px solid #8d8d86 @ 0.12 | = | - | 1px solid #8d8d86 |
| Radius | 3.35544e+07px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | - | = |
| Outline | none | = | - | = |
| Font | Delphi Inter 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #63635e | = | - | #21201c |
| Transition | translate, scale, opacity 0.4s cubic-bezier(0.7, 0, 0.84, 0) | = | - | = |
| Opacity | 0 | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12.92 x 12.92, colour #63635e, fill #000000 | = | - | 13.33 x 13.33, colour #21201c, fill #000000 |
| Painted layers | button.group/button.inline-flex 30.4x30.4 bg #ffffff border T:1px solid #8d8d86 @ 0.12 / R:1px solid #8d8d86 @ 0.12 / B:1px solid #8d8d86 @ 0.12 / L:1px solid #8d8d86 @ 0.12 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | - | button.group/button.inline-flex 31.4x31.4 bg #ffffff border T:1px solid #8d8d86 / R:1px solid #8d8d86 / B:1px solid #8d8d86 / L:1px solid #8d8d86 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `scroll-bottom-default.png`, `scroll-bottom-hover.png`, `scroll-bottom-pressed.png`.

#### chat-terms

Terms line. The "By using this service, you..." terms line under the composer.

Page: chat. Selector: `chat terms`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 429.25 x 16 |
| Padding | 0px 0px 0px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 12px/16px 400 |
| Letter spacing | -0.3px |
| Colour | #63635e |
| Transition | none |
| Painted layers | a.border-b.border-sand-9/40 97.2x16.0 border B:1px solid #8d8d86 @ 0.4; a.border-b.border-sand-9/40 77.8x16.0 border B:1px solid #8d8d86 @ 0.4 |
| How | at rest |

Crops: `chat-terms-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone top bar: wordmark, Sign In, Create pill.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px 20px 0px 12px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | a.group/button.inline-flex: Delphi Inter 14px/20px 500, #ffffff |
| Transition | translate, opacity, visibility 0.3s cubic-bezier(0.3, 0.9, 0.25, 1) |
| Icon | 84.5 x 26, colour #82827c |
| ::before | 390px x 0px, fixed, bg #ffffff, radius 0px |
| Painted layers | header::before.fixed.inset-x-0 390pxx0px bg #ffffff; div.absolute.inset-x-0 390.0x88.0 image linear-gradient(#ffffff 0%, #ffffff @ 0.9888 6.25%, #ffffff @ 0.957 12.5%, #ffffff @ 0.907; a.group/button.inline-flex 102.0x36.0 bg oklch(0.67 0.22 42) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-signin

Mobile Sign In. The Sign-In action on the phone header; measured, never followed.

Page: mobile. Selector: `mobile Sign In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42 x 17.88 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #fd5400 @ 0.5 offset 1px | = |
| Font | Delphi Inter 13px/17.875px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #82827c | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-fg-low.text-[13px] 42.0x17.9 outline 1px auto #fd5400 @ 0.5 offset 1px | = |

Crops: `m-signin-default.png`, `m-signin-hover.png`, `m-signin-focus-visible.png`, `m-signin-pressed.png`.

#### m-h1

Mobile headline. The phone hero heading.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 65.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Pythia 32px/32.64px 500 |
| Letter spacing | -1.12px |
| Colour | #21201c |
| Transition | none |
| ::before | 390px x 121.25px, absolute, bg #000000 @ 0 radial-gradient(#fcf8f3 30%, #fcf8f3 @ 0.92 48%, #000000 @ 0 74%), radius 50% |
| Painted layers | h1::before.font-heading 390pxx121.25px image radial-gradient(#fcf8f3 30%, #fcf8f3 @ 0.92 48%, #000000 @ 0 74%) r 50% |
| How | at rest |

Crops: `m-h1-default.png`.

#### m-search

Mobile ask field. The ask textarea on the phone hero; focused and typed then cleared, never submitted.

Page: mobile. Selector: `mobile textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 342 x 52 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = |
| Font | Delphi Inter 18px/26px 400 | = | = |
| Letter spacing | -0.18px | = | = |
| Colour | #21201c | = | = |
| Transition | color, background-color, border-color, box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #63635e, opacity 1 | = | = |
| Painted layers | textarea.min-w-0.placeholder:text-fg-mid 342.0x52.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | clicked into the field | typed "how do i sleep better", then deleted; nothing sent |

Crops: `m-search-default.png`, `m-search-focused.png`, `m-search-filled.png`.

#### m-topic-card

Mobile topic card. A topic card on the phone rail; measured, never pressed.

Page: mobile. Selector: `mobile topic card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 150 | = | = | = |
| Padding | 16px 18px | = | = | = |
| Gap | 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | #f7f3f0 | = | = | = |
| Background image | radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 72%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #21201c offset 4px | = |
| Font | Delphi Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #23211f | = | = | = |
| Text node | span.topic-ask.font-heading: Delphi Pythia 20px/23px 600, #23211f, ls -0.5px | = | = | = |
| Transition | translate, box-shadow 0.26s, 0.26s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #23211f | = | = | = |
| Painted layers | button.deck-card.topic-card 350.0x150.0 bg #f7f3f0 image radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 r 20px; span::before.deck-glow 434pxx186px image radial-gradient(150% 120% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.32), #000000 @ ; span.brand-tag.topic-tag 100.9x24.0 bg #000000 @ 0.06 r 6px | = | button.deck-card.topic-card 350.0x150.0 bg #f7f3f0 image radial-gradient(140% 85% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.27), #000000 @ 0 r 20px outline 2px solid #21201c offset 4px; span::before.deck-glow 434pxx186px image radial-gradient(150% 120% at 50% 118%, oklch(0.807277 0.106961 56.5286 / 0.32), #000000 @ ; span.brand-tag.topic-tag 100.9x24.0 bg #000000 @ 0.06 r 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-topic-card-default.png`, `m-topic-card-hover.png`, `m-topic-card-focus-visible.png`, `m-topic-card-pressed.png`.

#### m-footer

Mobile footer. The phone footer.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 372.75 |
| Padding | 0px 20px 24px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Delphi Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #21201c |
| Text node | a.text-fg-mid.hover:text-fg-high: Delphi Inter 14px/20px 400, #63635e |
| Transition | none |
| Icon | 78 x 24, colour #21201c |
| Painted layers | div.shrink-0.data-horizontal:h-px 350.0x1.0 bg #8d8d86 @ 0.12 |
| Ancestor paint | 1 up div.advice-landing.advice-landing-surface bg #f9f9f8 |
| How | at rest |

Crops: `m-footer-default.png`.

## Transitions declared in the readable stylesheets

delphi.co serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- chat: `border-color 0.3s, box-shadow 0.3s, background-color 0.25s, translate 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), scale 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.2s`, `background-color 9999s ease-in-out`, `height 0.18s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.5s ease-out, transform 0.25s cubic-bezier(0.19, 1, 0.22, 1)`, `width 0.5s linear, background-color 0.3s`, `grid-template-rows var(--reveal-duration)var(--reveal-ease),opacity calc(var(--reveal-duration)*.8)var(--reveal-ease)`, `transform 0.3s cubic-bezier(0.25, 1, 0.5, 1)`, `--drop-jewel 0.8s cubic-bezier(0.65, 0, 0.35, 1), --drop-ink 0.8s cubic-bezier(0.65, 0, 0.35, 1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.8s cubic-bezier(.3,0,0,1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.4s cubic-bezier(.3,0,0,1)`, `--person-preview-fade-top 0.22s cubic-bezier(0.22, 1, 0.36, 1), --person-preview-fade-bottom 0.22s cubic-bezier(0.22, 1, 0.36, 1)`

- discover: `border-color 0.3s, box-shadow 0.3s, background-color 0.25s, translate 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), scale 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.2s`, `background-color 9999s ease-in-out`, `height 0.18s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.5s ease-out, transform 0.25s cubic-bezier(0.19, 1, 0.22, 1)`, `width 0.5s linear, background-color 0.3s`, `grid-template-rows var(--reveal-duration)var(--reveal-ease),opacity calc(var(--reveal-duration)*.8)var(--reveal-ease)`, `transform 0.3s cubic-bezier(0.25, 1, 0.5, 1)`, `--drop-jewel 0.8s cubic-bezier(0.65, 0, 0.35, 1), --drop-ink 0.8s cubic-bezier(0.65, 0, 0.35, 1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.8s cubic-bezier(.3,0,0,1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.4s cubic-bezier(.3,0,0,1)`, `--person-preview-fade-top 0.22s cubic-bezier(0.22, 1, 0.36, 1), --person-preview-fade-bottom 0.22s cubic-bezier(0.22, 1, 0.36, 1)`

- expert: `border-color 0.3s, box-shadow 0.3s, background-color 0.25s, translate 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), scale 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.2s`, `background-color 9999s ease-in-out`, `height 0.18s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.5s ease-out, transform 0.25s cubic-bezier(0.19, 1, 0.22, 1)`, `width 0.5s linear, background-color 0.3s`, `grid-template-rows var(--reveal-duration)var(--reveal-ease),opacity calc(var(--reveal-duration)*.8)var(--reveal-ease)`, `transform 0.3s cubic-bezier(0.25, 1, 0.5, 1)`, `--drop-jewel 0.8s cubic-bezier(0.65, 0, 0.35, 1), --drop-ink 0.8s cubic-bezier(0.65, 0, 0.35, 1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.8s cubic-bezier(.3,0,0,1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.4s cubic-bezier(.3,0,0,1)`, `--person-preview-fade-top 0.22s cubic-bezier(0.22, 1, 0.36, 1), --person-preview-fade-bottom 0.22s cubic-bezier(0.22, 1, 0.36, 1)`

- home: `border-color 0.3s, box-shadow 0.3s, background-color 0.25s, translate 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), scale 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.2s`, `background-color 9999s ease-in-out`, `height 0.18s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.5s ease-out, transform 0.25s cubic-bezier(0.19, 1, 0.22, 1)`, `width 0.5s linear, background-color 0.3s`, `grid-template-rows var(--reveal-duration)var(--reveal-ease),opacity calc(var(--reveal-duration)*.8)var(--reveal-ease)`, `transform 0.3s cubic-bezier(0.25, 1, 0.5, 1)`, `--drop-jewel 0.8s cubic-bezier(0.65, 0, 0.35, 1), --drop-ink 0.8s cubic-bezier(0.65, 0, 0.35, 1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.8s cubic-bezier(.3,0,0,1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.4s cubic-bezier(.3,0,0,1)`, `--person-preview-fade-top 0.22s cubic-bezier(0.22, 1, 0.36, 1), --person-preview-fade-bottom 0.22s cubic-bezier(0.22, 1, 0.36, 1)`

- search: `border-color 0.3s, box-shadow 0.3s, background-color 0.25s, translate 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), scale 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.2s`, `background-color 9999s ease-in-out`, `height 0.18s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.5s ease-out, transform 0.25s cubic-bezier(0.19, 1, 0.22, 1)`, `width 0.5s linear, background-color 0.3s`, `grid-template-rows var(--reveal-duration)var(--reveal-ease),opacity calc(var(--reveal-duration)*.8)var(--reveal-ease)`, `transform 0.3s cubic-bezier(0.25, 1, 0.5, 1)`, `--drop-jewel 0.8s cubic-bezier(0.65, 0, 0.35, 1), --drop-ink 0.8s cubic-bezier(0.65, 0, 0.35, 1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.8s cubic-bezier(.3,0,0,1)`, `box-shadow .2s var(--ease-out-quart),--quote-glow 1.4s cubic-bezier(.3,0,0,1)`, `--person-preview-fade-top 0.22s cubic-bezier(0.22, 1, 0.36, 1), --person-preview-fade-bottom 0.22s cubic-bezier(0.22, 1, 0.36, 1)`
