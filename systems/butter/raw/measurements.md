# Component measurements

Computed styles read from butter.video on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's two painted surfaces — the light marketing pages and the dark /explore app shell — with the iubenda consent banner hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The marketing header: wordmark, the Co-Create/Product dropdown, plain links, Login and the Try-for-free pill.

Page: home. Selector: `header.index-style__HeaderContainer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | a.index-style__SkipToContent-sc-d968d94e-2.gWhVeu: DieGrotesk 18px/27px 400, #fafafa |
| Transition | none |
| Icon | 107 x 23, colour #1e1e1e |
| Painted layers | a.index-style__SkipToContent-sc-d968d94e-2.gWhVeu 137.0x47.0 bg #1e1e1e r 8px; div::before.index-style__HeaderLeftInner-sc-d968d94e-5.ckqdyg 708.312pxx64px bg #ededed r 16px; div.index-style__HeaderDropdown-sc-d968d94e-11.kVgSbW 694.1x382.7 bg #ededed; hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 bg #0f0f0f @ 0.15; hr.index-style__Hr-sc-a31f9adc-0.gTNDyN 0.0x1.0 bg #0f0f0f @ 0.15; hr.index-style__Hr-sc-a31f9adc-0.fphVdi 0.0x1.0 bg #0f0f0f @ 0.15 |
| How | at rest |

Crops: none.

#### logo

Logo. The wordmark anchor (an unclassed <a> wrapping the Butter svg).

Page: home. Selector: `header a:has(svg)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 107 x 23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Transition | none |
| Cursor | pointer |
| Icon | 107 x 23, colour #1e1e1e |
| How | at rest |

Crops: none.

#### nav-link

Nav link. A plain header link (Pricing/Blog).

Page: home. Selector: `header nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49.58 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.line: DieGrotesk 16px/20px 400, #1e1e1e, ls 0.7px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 49.6x20.0 shadow #3c3c3c 0px 0px 0px 1px | = |

Crops: none.

#### nav-cta

Nav CTA. The Try-for-free header action; links to /explore, measured never followed.

Page: home. Selector: `header a Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110.5 x 39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 16px/21px 400 | = | = | = |
| Letter spacing | 0.7px | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.index-style__ButtonText-sc-482eeec2-3: DieGrotesk 16px/21px 400, #ebebeb, ls 0.7px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.index-style__ButtonContent-sc-482eeec2-1.kszsnD 110.5x39.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px; span::before.index-style__ButtonContent-sc-482eeec2-1.kszsnD 108.5pxx37px bg #4dc5e5 r 10px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.kszsnD 108.5pxx37px bg #1e1e1e r 10px | = | a 110.5x39.0 shadow #3c3c3c 0px 0px 0px 1px; span.index-style__ButtonContent-sc-482eeec2-1.kszsnD 110.5x39.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px outline 3px solid #4dc5e5 offset 3px; span::before.index-style__ButtonContent-sc-482eeec2-1.kszsnD 108.5pxx37px bg #4dc5e5 r 10px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.kszsnD 108.5pxx37px bg #1e1e1e r 10px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### nav-trigger

Nav trigger. The Co-Create button that opens the header dropdown; toggled, never followed.

Page: home. Selector: `button.CoCreateTrigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.13 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.line: DieGrotesk 16px/20px 400, #1e1e1e, ls 0.7px | = | = | = |
| Transition | opacity 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.4 | = | 0.4 |
| Painted layers | - | = | button.index-style__CoCreateTrigger-sc-adb0d9eb-0.kOPflO 73.1x20.0 shadow #3c3c3c 0px 0px 0px 1px | = |

Crops: none.

#### nav-dropdown

Nav dropdown. The Product dropdown panel, opened by hovering its own trigger.

Page: home. Selector: `nav.HeaderDropdownMain`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 666.71 x 149.45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | span.line: DieGrotesk 16px/20px 400, #1e1e1e, ls 0.7px |
| Transition | none |
| Painted layers | hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 bg #0f0f0f @ 0.15; hr.index-style__Hr-sc-a31f9adc-0.gTNDyN 0.0x1.0 bg #0f0f0f @ 0.15; hr.index-style__Hr-sc-a31f9adc-0.fphVdi 0.0x1.0 bg #0f0f0f @ 0.15; hr.index-style__Hr-sc-a31f9adc-0.gkleBz 0.0x1.0 bg #0f0f0f @ 0.15 |
| Ancestor paint | 1 up div.index-style__HeaderDropdown-sc-d968d94e-11.kVgSbW bg #ededed |
| How | at rest |

Crops: none.

#### menu-link

Menu link. A link inside the opened header dropdown.

Page: home. Selector: `dropdown link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 666.71 x 28.42 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | #3c3c3c 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.line: DieGrotesk 16px/20px 400, #1e1e1e, ls 0.7px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 bg #0f0f0f @ 0.15 | = | a 666.7x28.4 shadow #3c3c3c 0px 0px 0px 1px; hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 bg #0f0f0f @ 0.15 | a 666.7x28.4 shadow #3c3c3c 0px 0px 0px 1px; hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 bg #0f0f0f @ 0.15 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Home

#### hero-title

Hero headline. The 108px display headline (TextStyles__Heading1Styled).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1081.77 x 106.69 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 107.568px/106.708px 400 |
| Letter spacing | 0.344219px |
| Colour | #0f0f0f |
| Text node | span.word.word1: DieGrotesk 107.568px/106.708px 400, #0f0f0f, ls 0.344219px |
| Transition | none |
| How | at rest |

Crops: none.

#### hero-cta

Hero CTA. The hero Get-Started action; measured never followed.

Page: home. Selector: `hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 144.95 x 50 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 16px/21px 400 | = | = | = |
| Letter spacing | 0.7px | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span.index-style__ButtonText-sc-482eeec2-3: DieGrotesk 16px/21px 400, #ebebeb, ls 0.7px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 145.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px bg #4dc5e5 r 16px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px bg #1e1e1e r 16px | = | a 145.0x50.0 shadow #3c3c3c 0px 0px 0px 1px; span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 145.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px outline 3px solid #4dc5e5 offset 3px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px bg #4dc5e5 r 16px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px bg #1e1e1e r 16px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### hero-sub

Hero copy. The lede under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 467.67 x 108.16 |
| Padding | 0px |
| Gap | 30px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.line: DieGrotesk 24.4842px/28.1568px 400, #0f0f0f, ls 0.734526px |
| Transition | none |
| Painted layers | span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 145.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px bg #4dc5e5 r 16px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px bg #1e1e1e r 16px |
| How | at rest |

Crops: none.

#### cursor-badge

Cursor badge. The custom-cursor pill ("Add butter") that follows the pointer. Captured in its hidden state (opacity 0, scale .6): it only paints while a real pointer follows the page, which synthetic movement does not wake — the reported box is the shrunken pill, not its visible size.

Page: home. Selector: `span.CursorButter`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 62.54 x 25.82 |
| Padding | 10px 13px |
| Border | none |
| Radius | 12px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | p.TextStyles__TextBodySmallStyled-sc-358d108c-6.HqwlT: DieGrotesk 16px/21px 400, #fafafa, ls 0.7px |
| Transition | opacity, transform 0.2s, 0.2s ease, ease delay 0s, 0s |
| Transform | matrix(0.6, 0, 0, 0.6, 0, 0) |
| Opacity | 0 |
| Painted layers | span.index-style__CursorButter-sc-804e36a2-2.eXVnrj 62.5x25.8 bg #0f0f0f r 12px |
| How | element at rest: the badge does not paint for synthetic pointer movement, so the sampled state is its hidden one (opacity 0, scale .6) |

Crops: none.

#### section-h2

Section heading. A 60px section heading (TextStyles__Heading2Styled).

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1077.59 x 185.86 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 60.4px/58.588px 400 |
| Letter spacing | 0.3624px |
| Colour | #0f0f0f |
| Text node | span.word.word1: DieGrotesk 60.4px/58.588px 400, #000000 @ 0, ls 0.3624px |
| Transition | none |
| How | at rest |

Crops: none.

### Pricing

#### pricing-h1

Pricing title. The "Unlimit your creativity." display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 949.34 x 106.69 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 107.568px/106.708px 400 |
| Letter spacing | 0.344219px |
| Colour | #0f0f0f |
| Text node | span.word.word1: DieGrotesk 107.568px/106.708px 400, #0f0f0f, ls 0.344219px |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### billing-toggle

Billing toggle. A Monthly/Annually billing-period button; toggled, never checked out.

Page: pricing. Selector: `button.PricingToggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.89 x 54 | = | = | = |
| Padding | 15px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span.line: DieGrotesk 20.7474px/24px 400, #fafafa, ls 0.684663px | = | = | = |
| Transition | color, opacity 0.5s, 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99), cubic-bezier(0.2, 0.715, 0.205, 0.99) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.index-style__PricingToggle-sc-51b11a00-2.cEBaxH 118.9x54.0 shadow #3c3c3c 0px 0px 0px 1px | = |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-focus-visible.png`, `billing-toggle-pressed.png`.

#### plan-card

Plan card. A pricing plan card (the Pro tier); the grey 32px-radius fill is a sibling Background layer, reported under Child layers.

Page: pricing. Selector: `div.PricingCardInner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.2 x 1132.59 |
| Padding | 25px 25px 40px 25px |
| Gap | 25px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.line: ABCDiatype 13.4947px/24px 400, #0f0f0f, ls 0.485811px |
| Transition | none |
| Icon | 13 x 9, colour #0f0f0f |
| Painted layers | div.index-style__PricingCardHighlightTooltip-sc-9eabdcbf-6.jPGyaI 123.0x35.5 bg #ededed r 12px; div.index-style__PricingCardName-sc-9eabdcbf-7.dLZuhC 258.2x64.0 bg #fafafa r 16px; span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 258.2x70.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px bg #4dc5e5 r 16px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px bg #1e1e1e r 16px; li::before.index-style__ListItem-sc-a04fc86c-4.iA-DFA-d 16pxx13px image url(data:…) r 0% |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan card's price figure ($18 annually / $25 monthly).

Page: pricing. Selector: `div.PricingAmount`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 258.2 x 58.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.word.word1: DieGrotesk 60.4px/58.588px 400, #0f0f0f, ls 0.3624px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan Choose-Pro action; measured never followed.

Page: pricing. Selector: `a.PricingCTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 258.2 x 70 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span.index-style__ButtonText-sc-482eeec2-3: DieGrotesk 16px/21px 400, #ebebeb, ls 0.7px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 258.2x70.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px bg #4dc5e5 r 16px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px bg #1e1e1e r 16px | = | a 258.2x70.0 shadow #3c3c3c 0px 0px 0px 1px; span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 258.2x70.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px outline 3px solid #4dc5e5 offset 3px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px bg #4dc5e5 r 16px shadow #4dc5e5 0px 0px 4px 0px, #4dc5e5 1px 1px 2px 0px, #63ad45 1px 2px 2px 0px, #e9d352 1px 4px 6px 0px, #4dc5e5 1px 6px 10px 0px; span::after.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px bg #1e1e1e r 16px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-item

FAQ item. A Frequently-Asked accordion question (button.AccordionTrigger); toggled open would reveal the answer, never clicked.

Page: pricing. Selector: `button.AccordionTrigger`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 641.41 x 75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 21.06px/31.59px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.line: DieGrotesk 24.4842px/28.1568px 400, #0f0f0f, ls 0.734526px |
| Transition | none |
| Icon | 14 x 8, colour #5a5a5a |
| How | at rest |

Crops: `faq-item-default.png`.

#### feature-row

Feature row. A feature-comparison accordion row (Free stock photos, Reseller rights, ...).

Page: pricing. Selector: `div.PricingAccordionItem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1636.44 x 72 |
| Padding | 25px 0px |
| Border | T: 1px solid #0f0f0f @ 0.15; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.line: DieGrotesk 16px/21px 400, #0f0f0f, ls 0.7px |
| Transition | none |
| Cursor | grab |
| Painted layers | div.index-style__PricingAccordionItem-sc-9d1d7ebc-4.linyFJ 1636.4x72.0 border T:1px solid #0f0f0f @ 0.15 |
| How | at rest |

Crops: `feature-row-default.png`.

### App shell (dark)

#### d-sidebar

App sidebar. The dark app-shell rail: wordmark, Home/Explore/Templates/Blocks nav, Log-in/Sign-up at the foot.

Page: explore. Selector: `aside.sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 283 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | dieGroteskA 16px/24px 400 |
| Letter spacing | 0.200102px |
| Colour | #f5f5f5 |
| Text node | span.MuiTypography-root.MuiTypography-cap: dieGroteskA 12px/16px 400, #a1a1aa, ls 0.8px |
| Transition | none |
| Icon | 110 x 24, colour #f5f5f5 |
| Painted layers | div.MuiStack-root.css-14i17xy-root 283.0x900.0 bg #0a0909; div.MuiStack-root.css-NavItem-content-ref 245.0x39.0 bg #252525 r 12px; a.MuiButtonBase-root.css-1e0gtz4-button 251.0x38.0 bg #1d1d1d r 10px; a.MuiButtonBase-root.css-gqu8g2-button 251.0x38.0 bg #f5f5f5 r 10px |
| How | at rest |

Crops: `d-sidebar-default.png`.

#### d-nav-link

Sidebar link. A nav link inside the dark sidebar.

Page: explore. Selector: `sidebar a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 245 x 39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | dieGroteskA 16px/24px 400 | = | = | = |
| Letter spacing | 0.200102px | = | = | = |
| Colour | #f5f5f5 | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-default: dieGroteskA 14px/20px 400, #f5f5f5, ls 0.8px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 21 x 21, colour #f5f5f5 | = | = | = |
| Painted layers | div.MuiStack-root.css-NavItem-content-ref 245.0x39.0 bg #252525 r 12px | = | div.MuiStack-root.css-NavItem-content-ref 245.0x39.0 bg #252525 r 12px shadow #f5f5f5 0px 0px 0px 0.5px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-nav-link-default.png`, `d-nav-link-hover.png`, `d-nav-link-focus-visible.png`, `d-nav-link-pressed.png`.

#### d-login

Sidebar login. The sidebar Log-in button (dark fill); measured never followed.

Page: explore. Selector: `sidebar Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 251 x 38 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #1d1d1d | #252525 | = | #252525 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | dieGroteskA 16px/24px 400 | = | = | = |
| Letter spacing | 0.200102px | = | = | = |
| Colour | #f5f5f5 | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-ui: dieGroteskA 13px/18px 400, #f5f5f5, ls 0.8px | = | = | = |
| Transition | opacity, background-color, border-color 0.16s, 0.16s, 0.16s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.MuiButtonBase-root.css-1e0gtz4-button 251.0x38.0 bg #1d1d1d r 10px | a.MuiButtonBase-root.css-1e0gtz4-button 251.0x38.0 bg #252525 r 10px | a.MuiButtonBase-root.Mui-focusVisible 251.0x38.0 bg #1d1d1d r 10px | a.MuiButtonBase-root.css-1e0gtz4-button 251.0x38.0 bg #252525 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `d-login-default.png`, `d-login-hover.png`, `d-login-focus-visible.png`, `d-login-pressed.png`.

#### d-signup

Sidebar signup. The sidebar Sign-up button (white pill); measured never followed.

Page: explore. Selector: `sidebar Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 251 x 38 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #f5f5f5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | dieGroteskA 16px/24px 400 | = | = | = |
| Letter spacing | 0.200102px | = | = | = |
| Colour | #0a0909 | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-ui: dieGroteskA 13px/18px 400, #0a0909, ls 0.8px | = | = | = |
| Transition | opacity, background-color, border-color 0.16s, 0.16s, 0.16s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.MuiButtonBase-root.css-gqu8g2-button 251.0x38.0 bg #f5f5f5 r 10px | = | a.MuiButtonBase-root.Mui-focusVisible 251.0x38.0 bg #f5f5f5 r 10px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `d-signup-default.png`, `d-signup-hover.png`, `d-signup-focus-visible.png`, `d-signup-pressed.png`.

#### d-create

Create button. The top-bar Create action (white pill on the dark shell); measured never followed.

Page: explore. Selector: `top Create button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111.38 x 48 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #f5f5f5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/13.3333px 300 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0909 | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-default: dieGroteskA 14px/20px 400, #0a0909, ls 0.8px | = | = | = |
| Transition | opacity, background-color, border-color 0.16s, 0.16s, 0.16s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0a0909 | = | = | = |
| Painted layers | button.MuiButtonBase-root.css-1jbogaq-button 111.4x48.0 bg #f5f5f5 r 10px | = | button.MuiButtonBase-root.Mui-focusVisible 111.4x48.0 bg #f5f5f5 r 10px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `d-create-default.png`, `d-create-hover.png`, `d-create-focus-visible.png`, `d-create-pressed.png`.

#### d-search

Search field. The shell search input, if one paints; never typed into.

Page: explore. Selector: `input`. States: .

Not found on the page at capture time.

#### d-card

Feature card. A large feature/release card on /explore.

Page: explore. Selector: `explore card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 637.03 x 437 | 624.29 x 428.26 | = | 624.29 x 428.26 |
| Padding | 0px | = | = | = |
| Border | 1px solid #212121 | = | = | = |
| Radius | 32px | = | = | = |
| Background | #151515 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = |
| Font | dieGroteskA 16px/24px 400 | = | = | = |
| Letter spacing | 0.200102px | = | = | = |
| Colour | #f5f5f5 | = | = | = |
| Text node | h3.MuiTypography-root.MuiTypography-titles: dieGroteskA 18px/25px 400, #f5f5f5, ls 0.8px | = | = | = |
| Transition | transform 0.16s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.css-zen4d2-card 637.0x437.0 bg #151515 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 32px; div.css-1pocunx-scrim 635.0x435.0 image linear-gradient(#000000 @ 0 0%, #000000 @ 0.42 60%, #000000 @ 0.72 100%) | div.css-zen4d2-card 624.3x428.3 bg #151515 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 32px; div.css-1pocunx-scrim 622.3x426.3 image linear-gradient(#000000 @ 0 0%, #000000 @ 0.42 60%, #000000 @ 0.72 100%) | div.css-zen4d2-card 637.0x437.0 bg #151515 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 32px outline 1px auto #99c8ff offset 0px; div.css-1pocunx-scrim 635.0x435.0 image linear-gradient(#000000 @ 0 0%, #000000 @ 0.42 60%, #000000 @ 0.72 100%) | div.css-zen4d2-card 624.3x428.3 bg #151515 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 32px; div.css-1pocunx-scrim 622.3x426.3 image linear-gradient(#000000 @ 0 0%, #000000 @ 0.42 60%, #000000 @ 0.72 100%) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.98, 0, 0, 0.98, 0, 0) | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `d-card-default.png`, `d-card-hover.png`, `d-card-focus-visible.png`, `d-card-pressed.png`.

#### d-block-card

Block card. A block-preview card in the Featured Blocks row.

Page: explore. Selector: `block card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 359 x 181 | 351.82 x 177.38 | - | 351.82 x 177.38 |
| Padding | 13px | = | - | = |
| Border | none | = | - | = |
| Radius | 42px | = | - | = |
| Background | #151515 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | dieGroteskA 16px/24px 400 | = | - | = |
| Letter spacing | 0.200102px | = | - | = |
| Colour | #f5f5f5 | = | - | = |
| Text node | p.MuiTypography-root.MuiTypography-default: dieGroteskA 14px/20px 400, #f5f5f5, ls 0.8px | = | - | = |
| Transition | transform, background-color 0.16s, 0.16s ease, ease delay 0s, 0s | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | div.MuiStack-root.css-xfhyob-card 359.0x181.0 bg #151515 r 42px; div.MuiBox-root.css-1pggzu7-tile 155.0x155.0 bg #1d1d1d r 22%; div::after.MuiBox-root.css-1pggzu7-tile 155pxx155px r 22% shadow #ffffff @ 0.55 0px 0px 16px 1px inset | div.MuiStack-root.css-xfhyob-card 351.8x177.4 bg #151515 r 42px; div.MuiBox-root.css-1pggzu7-tile 151.9x151.9 bg #1d1d1d r 22%; div::after.MuiBox-root.css-1pggzu7-tile 155pxx155px r 22% shadow #ffffff @ 0.55 0px 0px 16px 1px inset | - | div.MuiStack-root.css-xfhyob-card 351.8x177.4 bg #151515 r 42px; div.MuiBox-root.css-1pggzu7-tile 151.9x151.9 bg #1d1d1d r 22%; div::after.MuiBox-root.css-1pggzu7-tile 155pxx155px r 22% shadow #ffffff @ 0.55 0px 0px 16px 1px inset |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.98, 0, 0, 0.98, 0, 0) | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `d-block-card-default.png`, `d-block-card-hover.png`, `d-block-card-pressed.png`.

#### d-section

Section heading. An /explore section heading (24px).

Page: explore. Selector: `h2.MuiTypography-sections`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 150 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | dieGroteskA 24px/30px 400 |
| Letter spacing | 0.8px |
| Colour | #f5f5f5 |
| Transition | none |
| How | at rest |

Crops: `d-section-default.png`.

### Footer

#### footer

Footer. The light-grey FooterMain: link columns, social, legal.

Page: home. Selector: `footer.FooterMain`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1126.81 |
| Padding | 160px 0px 60px 0px |
| Border | none |
| Radius | 0px |
| Background | #ededed |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.line: ABCDiatype 13.4947px/24px 400, #0f0f0f @ 0.5, ls 0.485811px |
| Transition | none |
| Painted layers | footer.index-style__FooterMain-sc-144eedcf-0.bdNowa 1440.0x1126.8 bg #ededed |
| How | at rest |

Crops: none.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.73 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span.line: DieGrotesk 20.7474px/24px 400, #1e1e1e, ls 0.684663px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 71.7x24.0 shadow #3c3c3c 0px 0px 0px 1px | = |

Crops: none.

#### social-icon

Social link. A social link in the footer (text links, not glyphs).

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.73 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span.line: DieGrotesk 20.7474px/24px 400, #1e1e1e, ls 0.684663px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 90.7x24.0 shadow #3c3c3c 0px 0px 0px 1px | = |

Crops: none.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 76.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | a.index-style__SkipToContent-sc-d968d94e-2.gWhVeu: DieGrotesk 18px/27px 400, #fafafa |
| Transition | none |
| Icon | 107 x 23, colour #1e1e1e |
| Painted layers | a.index-style__SkipToContent-sc-d968d94e-2.gWhVeu 137.0x47.0 bg #1e1e1e r 8px; div::before.index-style__HeaderLeftInner-sc-d968d94e-5.ckqdyg 290.656pxx64px bg #ededed r 16px; div.index-style__HeaderDropdown-sc-d968d94e-11.kVgSbW 284.8x370.4 bg #ededed; hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 bg #0f0f0f @ 0.15; hr.index-style__Hr-sc-a31f9adc-0.gTNDyN 0.0x1.0 bg #0f0f0f @ 0.15; hr.index-style__Hr-sc-a31f9adc-0.fphVdi 0.0x1.0 bg #0f0f0f @ 0.15 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The menu toggle (button.MenuToggleMain).

Page: mobile. Selector: `button.MenuToggleMain`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 23 x 31 |
| Padding | 10px |
| Border | none |
| Radius | 5px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | span.index-style__MenuToggleClose-sc-548009f3-2.jrYjEI: DieGrotesk 16px/20px 400, #1e1e1e, ls 0.7px |
| Transition | none |
| Cursor | pointer |
| Icon | 3 x 11, colour #1e1e1e |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The whole header menu panel opened by its own toggle (div.index-style__HeaderDropdown).

Page: mobile. Selector: `div.index-style__HeaderDropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 290.66 x 554 |
| Padding | 14px 14px 22px 14px |
| Border | none |
| Radius | 0px |
| Background | #ededed |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | span.line: DieGrotesk 16px/20px 400, #1e1e1e, ls 0.7px |
| Transition | opacity, transform, clip-path 0.8s, 0.5s, 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99), cubic-bezier(0.2, 0.715, 0.205, 0.99), cubic-bezier(0.2, 0.715, 0.205, 0.99) delay 0s, 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 554) |
| Painted layers | div.index-style__HeaderDropdown-sc-d968d94e-11.bfhfPf 290.7x554.0 bg #ededed; div::after.index-style__ButterBlockWrapper-sc-dca6eb83-0.kBcKnP 64pxx64px r 22.4% shadow #ffffff 0px 0px 11.7px 0px inset; hr.index-style__Hr-sc-a31f9adc-0.hyIksl 262.7x1.0 bg #0f0f0f @ 0.15; div::after.index-style__ButterBlockWrapper-sc-dca6eb83-0.kBcKnP 64pxx64px r 22.4% shadow #ffffff 0px 0px 11.7px 0px inset; hr.index-style__Hr-sc-a31f9adc-0.fduGcU 262.7x1.0 bg #0f0f0f @ 0.15; div::after.index-style__ButterBlockWrapper-sc-dca6eb83-0.kBcKnP 64pxx64px r 22.4% shadow #ffffff 0px 0px 11.7px 0px inset |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A link inside the opened header menu.

Page: mobile. Selector: `header menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 262.66 x 73 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #3c3c3c 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | DieGrotesk 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.line: DieGrotesk 16px/20px 400, #1e1e1e, ls 0.7px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div::after.index-style__ButterBlockWrapper-sc-dca6eb83-0.kBcKnP 64pxx64px r 22.4% shadow #ffffff 0px 0px 11.7px 0px inset; hr.index-style__Hr-sc-a31f9adc-0.hyIksl 262.7x1.0 bg #0f0f0f @ 0.15 | = | a 262.7x73.0 shadow #3c3c3c 0px 0px 0px 1px; div::after.index-style__ButterBlockWrapper-sc-dca6eb83-0.kBcKnP 64pxx64px r 22.4% shadow #ffffff 0px 0px 11.7px 0px inset; hr.index-style__Hr-sc-a31f9adc-0.hyIksl 262.7x1.0 bg #0f0f0f @ 0.15 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 338.3 x 123.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DieGrotesk 56.7263px/61.8317px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.word.word1: DieGrotesk 56.7263px/61.8317px 400, #0f0f0f |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

butter.video serves its Next.js CSS bundles and styled-components blocks same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- explore: `background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `background-color 160ms`, `opacity 160ms, background-color 160ms, border-color 160ms`, `color 160ms`, `transform 160ms`, `opacity 160ms`, `opacity 0.15s`, `transform 160ms, opacity 160ms`, `width 300ms cubic-bezier(0.22, 1, 0.36, 1)`, `transform 160ms, background-color 160ms`, `background-position 0.4s, background-color 0.4s`, `all`

- home: `opacity 0.2s, transform 0.2s`, `opacity 0.8s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99), padding-left 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.2s`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.3s`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.4s`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.5s`, `opacity 0.3s`, `transform 0.2s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 2s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 0.8s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.2s, transform 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99), clip-path 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99)`

- pricing: `opacity 0.3s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 0.2s, transform 0.2s`, `opacity 0.8s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99), padding-left 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.2s`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.3s`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.4s`, `transform 1s cubic-bezier(0.2, 0.715, 0.205, 0.99) 0.5s`, `opacity 0.3s`, `transform 0.2s cubic-bezier(0.2, 0.715, 0.205, 0.99)`, `opacity 2s cubic-bezier(0.2, 0.715, 0.205, 0.99)`
