# Macaw component measurements

Computed styles read from macawhq.com on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### navbar

Top bar. 80px Webflow nav on the cream page. Frosted fill rgba(255,253,249,0.3), 32px inline padding. Holds Product, Writing examples, Resources, Pricing, affiliate, Log in and Start for free.

Page: home. Selector: `.navbar_component`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px 32px |
| Border | none |
| Radius | 0px |
| Background | #fffdf9 @ 0.3 |
| Box shadow | none |
| Backdrop filter | blur(26px) |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1d2939 |
| Text node | a.navbar_link.w-nav-link: Inter 16px/24px 600, #1d2939 |
| Transition | none |
| Icon | 0 x 0, colour #1d2939 |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar_component.w-nav 1440.0x80.0 bg #fffdf9 @ 0.3; nav.navbar_dropdown-list.w-dropdown-list 0.0x0.0 bg #dddddd shadow #000000 @ 0.08 0px 12px 16px -4px, #101828 @ 0.03 0px 4px 6px -2px; a.button-secondary-gray.w-inline-block 81.3x46.0 bg #ffffff border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px; a.button.is-button-xsmall 158.5x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 1 up body.body bg #fffdf9 |
| How | at rest |

Crops: `navbar-default.png`.

#### nav-link

Nav link. 16/600 Inter, ink rgb(29,41,57). A link, so hover and keyboard focus are real. Pressed is forced :active and the link is not followed.

Page: home. Selector: `.navbar_link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.27 x 48 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1d2939 | #f66658 | = | #f66658 |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.navbar_link.w-nav-link 86.3x48.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### button-primary

Primary button. Coral fill rgb(246,102,88), white 14.8/600 label, 8px radius, 46px tall, 10px 18px padding, a 1px soft shadow. The href is the sign-up wall and was not followed.

Page: home. Selector: `a.button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 158.55 x 46 | = | = | = |
| Padding | 10px 18px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | 1px solid #f66658 | 1px solid #de4f30 | = | 1px solid #de4f30 |
| Radius | 8px | = | = | = |
| Background | #f66658 | #de4f30 | = | #de4f30 |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px | = | #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14.8px/22.2px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.text-block: Inter 14.8px/19.24px 600, #ffffff, ls -0.2px | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.is-button-xsmall 158.5x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | a.button.is-button-xsmall 158.5x46.0 bg #de4f30 border T:1px solid #de4f30 / R:1px solid #de4f30 / B:1px solid #de4f30 / L:1px solid #de4f30 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | a.button.is-button-xsmall 158.5x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px outline 1px auto #005fcc offset 1px | a.button.is-button-xsmall 158.5x46.0 bg #de4f30 border T:1px solid #de4f30 / R:1px solid #de4f30 / B:1px solid #de4f30 / L:1px solid #de4f30 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `button-primary-default.png`, `button-primary-hover.png`, `button-primary-focus-visible.png`, `button-primary-pressed.png`.

#### button-secondary

Secondary button. White fill, ink rgb(52,64,84), 8px radius, 46px tall. The href is the sign-in wall and was not followed. Playwright calls the link hidden; the box is on screen.

Page: home. Selector: `a.button-secondary-gray`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.3 x 46 | = | = | = |
| Padding | 10px 18px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | 1px solid #d0d5dd | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f2f4f7 | = | #f2f4f7 |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px | = | #101828 @ 0.05 0px 1px 2px 0px, #f2f4f7 0px 0px 0px 4px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14.8px/22.2px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #344054 | #1d2939 | = | #1d2939 |
| Text node | div: Inter 14.8px/22.2px 600, #344054 | div: Inter 14.8px/22.2px 600, #1d2939 | = | div: Inter 14.8px/22.2px 600, #1d2939 |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-secondary-gray.w-inline-block 81.3x46.0 bg #ffffff border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | a.button-secondary-gray.w-inline-block 81.3x46.0 bg #f2f4f7 border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | a.button-secondary-gray.w-inline-block 81.3x46.0 bg #ffffff border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #f2f4f7 0px 0px 0px 4px outline 1px auto #005fcc offset 1px | a.button-secondary-gray.w-inline-block 81.3x46.0 bg #f2f4f7 border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `button-secondary-default.png`, `button-secondary-hover.png`, `button-secondary-focus-visible.png`, `button-secondary-pressed.png`.

#### button-google

Google sign-in link. Same quiet white button as Log in. The href starts a Google strategy on the app host and was not followed.

Page: home. Selector: `a[href*="strategy=google"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 227.39 x 46 | = |
| Padding | 10px 18px | = |
| Gap | normal 8px | = |
| Border | 1px solid #d0d5dd | = |
| Radius | 8px | = |
| Background | #ffffff | #f2f4f7 |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 14.8px/22.2px 600 | = |
| Letter spacing | normal | = |
| Colour | #344054 | #1d2939 |
| Text node | div: Inter 14.8px/22.2px 600, #344054 | div: Inter 14.8px/22.2px 600, #1d2939 |
| Transition | all 0.3s ease | = |
| Cursor | pointer | = |
| Painted layers | a.button-secondary-gray._2 227.4x46.0 bg #ffffff border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | a.button-secondary-gray._2 227.4x46.0 bg #f2f4f7 border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover |

Crops: `button-google-default.png`, `button-google-hover.png`.

#### resources-toggle

Resources menu toggle. Webflow dropdown toggle. Hover opens the menu. The menu items point at # and were not followed.

Page: home. Selector: `.navbar_dropdown-toggle`. States: .

Not found on the page at capture time.

#### resources-menu

Resources menu. Blog and Documentation rows. Both hrefs are #. The desktop toggle is display:none, so this menu was not opened by hover. The page shot is a forced open.

Page: home. Selector: `.navbar_menu-dropdown`. States: .

Not found on the page at capture time.

#### footer-link

Footer link. Footer legal link, ink rgb(51,51,51).

Page: home. Selector: `footer a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 41.25 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | Inter 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #667085 | #f66658 | = |
| Transition | all 0.3s ease | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.footer08_legal-link 41.3x21.0 outline 1px auto #005fcc offset 1px |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`.

### Home

#### display

Display heading. Home h1, Inter 53.6/700, ink rgb(16,24,40).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 630 x 128.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 53.6px/64.32px 700 |
| Letter spacing | -1.608px |
| Colour | #101828 |
| Transition | none |
| How | at rest |

Crops: `display-default.png`.

#### body-copy

Page. Cream page rgb(255,253,249), body ink rgb(71,84,103), Inter 16/400.

Page: home. Selector: `body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 9106.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fffdf9 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #475467 |
| Text node | a.navbar_link.w-nav-link: Inter 16px/24px 600, #1d2939 |
| Transition | none |
| Icon | 0 x 0, colour #1d2939 |
| Painted layers | body.body 1440.0x9106.6 bg #fffdf9; div.tingle-modal 0.0x0.0 image linear-gradient(#000000 @ 0.5 0%, #101828 @ 0.7 100%); div.tingle-modal-box 0.0x0.0 bg #ffffff r 12px; div.div-block-57 0.0x0.0 bg #ffffff border T:1px solid #eaecf0 / R:1px solid #eaecf0 / B:1px solid #eaecf0 / L:1px solid #eaecf0 r 12px; aside.div-block-50 0.0x0.0 bg #ffffff border B:1px solid #eaecf0 r 12px 12px 0px 0px; aside.aside 0.0x0.0 image linear-gradient(#000000 @ 0, #000000 @ 0.08 56%, #000000 @ 0.18) r 0px 0px 12px 12px |
| How | at rest |

Crops: none.

### Pricing

#### pricing-heading

Pricing heading. Inter 53.6/700, ink rgb(29,41,57).

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 64.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 53.6px/64.32px 700 |
| Letter spacing | -1.608px |
| Colour | #1d2939 |
| Transition | none |
| How | at rest |

Crops: `pricing-heading-default.png`.

#### plan-starter

Starter plan card. Lavender fill rgb(246,226,255), 12px radius, 40px 0 16px padding. Yearly price at rest.

Page: pricing. Selector: `.pricing07_top-row-content.purple`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 272.45 x 310.78 |
| Padding | 40px 0px 16px 0px |
| Border | 1px solid #f6e2ff |
| Radius | 12px |
| Background | #f6e2ff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #475467 |
| Text node | div: Inter 16px/24px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #475467 |
| Painted layers | div.pricing07_top-row-content.purple 272.5x310.8 bg #f6e2ff border T:1px solid #f6e2ff / R:1px solid #f6e2ff / B:1px solid #f6e2ff / L:1px solid #f6e2ff r 12px; div.div-block-41.purple 152.3x36.0 bg #bd3df6 r 100px; a.button.is-button-xxsmall 222.5x37.8 bg #222020 border T:1px solid #222020 / R:1px solid #222020 / B:1px solid #222020 / L:1px solid #222020 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 1 up div.w-layout-grid.pricing07_top-row bg #fffdf9 |
| How | at rest |

Crops: `plan-starter-default.png`.

#### plan-pro

Pro plan card. Peach fill rgb(255,232,226), 12px radius.

Page: pricing. Selector: `.pricing07_top-row-content.orange`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 272.44 x 310.78 |
| Padding | 40px 0px 16px 0px |
| Border | 1px solid #000000 |
| Radius | 12px |
| Background | #ffe8e2 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #475467 |
| Text node | div: Inter 16px/24px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #475467 |
| Painted layers | div.pricing07_top-row-content.orange 272.4x310.8 bg #ffe8e2 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 12px; div.div-block-41.orange 125.8x36.0 bg #f66658 r 100px; a.button.is-button-xxsmall 222.4x37.8 bg #222020 border T:1px solid #222020 / R:1px solid #222020 / B:1px solid #222020 / L:1px solid #222020 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px; div.div-block-63 81.7x17.5 bg #222020 r 70px |
| Ancestor paint | 1 up div.w-layout-grid.pricing07_top-row bg #fffdf9 |
| How | at rest |

Crops: `plan-pro-default.png`.

#### plan-scale

Scale plan card. Blue fill rgb(227,238,255), 12px radius.

Page: pricing. Selector: `.pricing07_top-row-content.blue`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 272.45 x 310.78 |
| Padding | 40px 0px 16px 0px |
| Border | none |
| Radius | 12px |
| Background | #e3eeff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #475467 |
| Text node | div: Inter 16px/24px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #475467 |
| Painted layers | div.pricing07_top-row-content.blue 272.5x310.8 bg #e3eeff r 12px; div.div-block-41.blue 142.3x36.0 bg #3c83ed r 100px; a.button.is-button-xxsmall 224.5x37.8 bg #222020 border T:1px solid #222020 / R:1px solid #222020 / B:1px solid #222020 / L:1px solid #222020 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 1 up div.w-layout-grid.pricing07_top-row bg #fffdf9 |
| How | at rest |

Crops: `plan-scale-default.png`.

#### billing-yearly

Yearly billing toggle. Selected at rest. A div, so it takes no keyboard focus. Not switched during this reading.

Page: pricing. Selector: `.pricing-toggle-button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 166.11 x 42 | = |
| Padding | 9px 14px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 600 | = |
| Letter spacing | normal | = |
| Colour | #344054 | #de4f30 |
| Text node | div: Inter 16px/24px 600, #344054 | div: Inter 16px/24px 600, #de4f30 |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.text-block-13 77.1x24.0 bg #ecfdf3 border T:1px solid #abefc6 / R:1px solid #abefc6 / B:1px solid #abefc6 / L:1px solid #abefc6 r 100px | = |
| Ancestor paint | 1 up div.div-block-90 bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `billing-yearly-default.png`, `billing-yearly-hover.png`.

#### billing-monthly

Monthly billing toggle. Clicked to reveal the monthly price state, then left. No checkout was opened.

Page: pricing. Selector: `.pricing-toggle-button`. States: default, selected.

| Property | default | selected |
|---|---|---|
| Size (w x h) | 91.5 x 42 | = |
| Padding | 9px 14px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 600 | = |
| Letter spacing | normal | = |
| Colour | #344054 | = |
| Text node | div: Inter 16px/24px 600, #344054 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Ancestor paint | 1 up div.div-block-90 bg #ffffff | = |
| How | at rest | clicked the Monthly label; no checkout |

Crops: `billing-monthly-default.png`, `billing-monthly-selected.png`.

#### plan-cta

Plan call to action. Get started links to sign-up. Not followed.

Page: pricing. Selector: `a`. States: .

Not found on the page at capture time.

#### faq-question

FAQ question. First pricing FAQ row. Expanded by a click that only opens the answer.

Page: pricing. Selector: `.faq01_question`. States: default, hover, expanded.

| Property | default | hover | expanded |
|---|---|---|---|
| Size (w x h) | 768 x 75 | = | = |
| Padding | 24px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #475467 | = | = |
| Text node | div.text-size-medium.text-weight-medium: Inter 18px/27px 500, #101828 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | div.accordion-icon_component 24.0x24.0 border T:2px solid #98a2b3 / R:2px solid #98a2b3 / B:2px solid #98a2b3 / L:2px solid #98a2b3 r 50%; div.accordion-icon_horizontal-line 12.0x2.0 bg #98a2b3 r 1px; div.accordion-icon_vertical-line 2.0x12.0 bg #98a2b3 r 1px | = | div.accordion-icon_component 24.0x24.0 border T:2px solid #98a2b3 / R:2px solid #98a2b3 / B:2px solid #98a2b3 / L:2px solid #98a2b3 r 50%; div.accordion-icon_horizontal-line 12.0x2.0 bg #98a2b3 r 1px; div.accordion-icon_vertical-line 12.0x2.0 bg #98a2b3 r 1px |
| How | at rest | mouse hover | clicked the question |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-expanded.png`.

#### faq-answer

FAQ answer. The answer under the first question, visible after the row is open or already painted.

Page: pricing. Selector: `.faq01_answer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #475467 |
| Text node | div: Inter 16px/24px 400, #475467 |
| Transition | none |
| How | at rest |

Crops: `faq-answer-default.png`.

#### sales-link

Sales link. Custom-plan link. Not followed.

Page: pricing. Selector: `a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 198.53 x 46 |
| Padding | 10px 18px |
| Gap | normal 8px |
| Border | 1px solid #f66658 |
| Radius | 8px |
| Background | #f66658 |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | Inter 14.8px/22.2px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.text-block: Inter 14.8px/19.24px 600, #ffffff, ls -0.2px |
| Transition | all 0.3s ease |
| Cursor | pointer |
| Painted layers | a.button.is-button-xsmall 198.5x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `sales-link-default.png`.

### Contact form

#### field-label

Field label. Inter 14/400, ink rgb(52,64,84).

Page: contact. Selector: `.field-label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 217 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 500 |
| Letter spacing | normal |
| Colour | #344054 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `field-label-default.png`.

#### text-field

Text field. White field, 8px radius, 44px tall, 8px 14px padding. Autofocus paints a coral ring before any click. Sample text was typed and deleted. The form was not submitted.

Page: contact. Selector: `input.form-input`. States: default, hover, focus-visible, focused, filled.

| Property | default | hover | focus-visible | focused | filled |
|---|---|---|---|---|---|
| Size (w x h) | 217 x 44 | = | = | = | = |
| Padding | 8px 14px | = | = | = | = |
| Border | 1px solid #d0d5dd | = | 1px solid #faa29a | 1px solid #faa29a | 1px solid #faa29a |
| Radius | 8px | = | = | = | = |
| Background | #ffffff | = | = | = | = |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px | = | #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px | #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px | #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px |
| Outline | none | = | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #475467 | = | #101828 | #101828 | #101828 |
| Transition | all 0.3s ease | = | = | = | = |
| Cursor | text | = | = | = | = |
| Placeholder | #667085, opacity 1 | = | = | = | = |
| Painted layers | input.form-input.w-input 217.0x44.0 bg #ffffff border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | = | input.form-input.w-input 217.0x44.0 bg #ffffff border T:1px solid #faa29a / R:1px solid #faa29a / B:1px solid #faa29a / L:1px solid #faa29a r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px | input.form-input.w-input 217.0x44.0 bg #ffffff border T:1px solid #faa29a / R:1px solid #faa29a / B:1px solid #faa29a / L:1px solid #faa29a r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px | input.form-input.w-input 217.0x44.0 bg #ffffff border T:1px solid #faa29a / R:1px solid #faa29a / B:1px solid #faa29a / L:1px solid #faa29a r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | clicked into the field | typed "Sample", then deleted; nothing sent |

Crops: `text-field-default.png`, `text-field-hover.png`, `text-field-focus-visible.png`, `text-field-focused.png`, `text-field-filled.png`.

#### text-area

Text area. 112px tall, 8px radius, 1px rgb(208,213,221) border, 12px 14px padding. Not submitted.

Page: contact. Selector: `textarea.form-input`. States: default, hover, focus-visible, focused.

| Property | default | hover | focus-visible | focused |
|---|---|---|---|---|
| Size (w x h) | 450 x 112 | = | = | = |
| Padding | 12px 14px | = | = | = |
| Border | 1px solid #d0d5dd | = | 1px solid #faa29a | 1px solid #faa29a |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px | = | #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px | #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #475467 | = | #101828 | #101828 |
| Transition | all 0.3s ease | = | = | = |
| Cursor | text | = | = | = |
| Placeholder | #667085, opacity 1 | = | = | = |
| Painted layers | textarea.form-input.text-area 450.0x112.0 bg #ffffff border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | = | textarea.form-input.text-area 450.0x112.0 bg #ffffff border T:1px solid #faa29a / R:1px solid #faa29a / B:1px solid #faa29a / L:1px solid #faa29a r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px | textarea.form-input.text-area 450.0x112.0 bg #ffffff border T:1px solid #faa29a / R:1px solid #faa29a / B:1px solid #faa29a / L:1px solid #faa29a r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | clicked into the field |

Crops: `text-area-default.png`, `text-area-hover.png`, `text-area-focus-visible.png`, `text-area-focused.png`.

#### send-button

Send button. Webflow submit styled as the coral button. Not pressed. Pressed was not forced, so the form cannot fire.

Page: contact. Selector: `input[type=submit].button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 450 x 46 | = | = |
| Padding | 10px 18px | = | = |
| Gap | normal 8px | = | = |
| Border | 1px solid #f66658 | 1px solid #de4f30 | = |
| Radius | 8px | = | = |
| Background | #f66658 | #de4f30 | = |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px | = | #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | Inter 16px/24px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | all 0.3s ease | = | = |
| Cursor | pointer | = | = |
| Placeholder | #ffffff, opacity 1 | = | = |
| Painted layers | input.button.max-width-full 450.0x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | input.button.max-width-full 450.0x46.0 bg #de4f30 border T:1px solid #de4f30 / R:1px solid #de4f30 / B:1px solid #de4f30 / L:1px solid #de4f30 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | input.button.max-width-full 450.0x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px, #ffe1df 0px 0px 0px 4px outline 1px auto #005fcc offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `send-button-default.png`, `send-button-hover.png`, `send-button-focus-visible.png`.

### Free tool

#### tool-heading

Tool heading. Free Blog Title Generator. The generator form itself did not render signed out (no input on the page).

Page: tool. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 630 x 64.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 53.6px/64.32px 700 |
| Letter spacing | -1.608px |
| Colour | #101828 |
| Transition | none |
| How | at rest |

Crops: `tool-heading-default.png`.

#### tool-cta

Tool call to action. Try Macaw free. Not followed.

Page: tool. Selector: `a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 179.06 x 46 | = |
| Padding | 10px 18px | = |
| Gap | normal 8px | = |
| Border | 1px solid #f66658 | 1px solid #de4f30 |
| Radius | 8px | = |
| Background | #f66658 | #de4f30 |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 14.8px/22.2px 600 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | div.text-block: Inter 14.8px/19.24px 600, #ffffff, ls -0.2px | = |
| Transition | all 0.3s ease | = |
| Cursor | pointer | = |
| Painted layers | a.button.is-button-xsmall 179.1x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px | a.button.is-button-xsmall 179.1x46.0 bg #de4f30 border T:1px solid #de4f30 / R:1px solid #de4f30 / B:1px solid #de4f30 / L:1px solid #de4f30 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover |

Crops: `tool-cta-default.png`, `tool-cta-hover.png`.

### Legal

#### legal-heading

Legal heading. Terms and Conditions, Inter 53.6/700.

Page: terms. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540.81 x 64.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 53.6px/64.32px 700 |
| Letter spacing | -1.608px |
| Colour | #101828 |
| Transition | none |
| How | at rest |

Crops: `legal-heading-default.png`.

#### privacy-heading

Privacy heading.

Page: privacy. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 346.17 x 64.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 53.6px/64.32px 700 |
| Letter spacing | -1.608px |
| Colour | #101828 |
| Transition | none |
| How | at rest |

Crops: `privacy-heading-default.png`.

### Mobile (390 wide)

#### m-navbar

Mobile top bar.

Page: home. Selector: `.navbar_component`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | #fffdf9 @ 0.3 |
| Box shadow | none |
| Backdrop filter | blur(26px) |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1d2939 |
| Transition | none |
| Icon | 0 x 0, colour #667085 |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar_component.w-nav 390.0x72.0 bg #fffdf9 @ 0.3; nav.navbar_menu.w-nav-menu 0.0x0.0 bg #ffffff border T:1px solid #f2f4f7; nav.navbar_dropdown-list.w-dropdown-list 0.0x0.0 bg #dddddd shadow #000000 @ 0.08 0px 12px 16px -4px, #101828 @ 0.03 0px 4px 6px -2px; a.button-secondary-gray.w-inline-block 0.0x0.0 bg #ffffff border T:1px solid #d0d5dd / R:1px solid #d0d5dd / B:1px solid #d0d5dd / L:1px solid #d0d5dd r 8px shadow #101828 @ 0.05 0px 1px 2px 0px; a.button.is-button-xsmall 0.0x0.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px; div.menu-icon_line-top 24.0x2.0 bg #344054 r 16px |
| Ancestor paint | 1 up body.body bg #fffdf9 |
| How | at rest |

Crops: `m-navbar-default.png`.

#### m-menu-button

Mobile menu button. Opens the Webflow nav drawer. The drawer shot is in screenshots; this crop is the button at rest.

Page: home. Selector: `.w-nav-button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/36px 400 |
| Letter spacing | normal |
| Colour | #1d2939 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.menu-icon_line-top 24.0x2.0 bg #344054 r 16px; div.menu-icon_line-middle 24.0x2.0 bg #344054 r 16px; div.menu-icon_line-bottom 24.0x2.0 bg #344054 r 16px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-button-primary

Primary button (mobile). Coral Start control in the first phone screen. The href was not followed.

Page: home. Selector: `a.button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 46 |
| Padding | 12px 20px |
| Gap | normal 8px |
| Border | 1px solid #f66658 |
| Radius | 8px |
| Background | #f66658 |
| Box shadow | #101828 @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | Inter 14.8px/22.2px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.text-block: Inter 14.8px/19.24px 600, #ffffff, ls -0.2px |
| Transition | all 0.3s ease |
| Cursor | pointer |
| Painted layers | a.button.is-button-xsmall 358.0x46.0 bg #f66658 border T:1px solid #f66658 / R:1px solid #f66658 / B:1px solid #f66658 / L:1px solid #f66658 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `m-button-primary-default.png`.

#### m-plan

Plan card (mobile).

Page: pricing. Selector: `.pricing07_top-row-content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 522.73 |
| Padding | 40px 19.2px 19.2px 19.2px |
| Border | 1px solid #f6e2ff |
| Radius | 12px |
| Background | #f6e2ff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #475467 |
| Text node | div: Inter 16px/24px 500, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #475467 |
| Painted layers | div.pricing07_top-row-content.purple 358.0x522.7 bg #f6e2ff border T:1px solid #f6e2ff / R:1px solid #f6e2ff / B:1px solid #f6e2ff / L:1px solid #f6e2ff r 12px; div.div-block-41.purple 152.3x36.0 bg #bd3df6 r 100px; a.button.is-button-xxsmall 317.6x37.8 bg #222020 border T:1px solid #222020 / R:1px solid #222020 / B:1px solid #222020 / L:1px solid #222020 r 8px shadow #101828 @ 0.05 0px 1px 2px 0px; div.div-block-26 317.6x73.4 border T:1px solid #000000 @ 0.09 |
| Ancestor paint | 1 up div.w-layout-grid.pricing07_top-row bg #fffdf9 |
| How | at rest |

Crops: `m-plan-default.png`.

## Transitions declared in the readable stylesheets

Macaw's Webflow CSS is on cdn.prod.website-files.com. This list is what the CSSOM could read on each page. The per-state Transition rows above are computed values.

- contact: `transform 167ms cubic-bezier(0.33, 0, 0, 1)`, `transform 250ms cubic-bezier(0.33, 0, 0, 1)`, `transform 134ms cubic-bezier(0.45, 0, 0.2, 1)`, `transform 100ms linear, opacity 80ms linear`, `opacity 80ms linear`

- home: `opacity 0.2s`, `transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), -webkit-transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)`, `bottom 0.3s ease-in-out 0.3s`, `background-color 0.4s`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`, `transform 250ms cubic-bezier(0.33, 0, 0, 1)`, `transform 134ms cubic-bezier(0.45, 0, 0.2, 1)`, `transform 100ms linear, opacity 80ms linear`, `opacity 80ms linear`

- pricing: `cubic-bezier(0.46, 0.1, 0.52, 0.98)`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`, `transform 250ms cubic-bezier(0.33, 0, 0, 1)`, `transform 134ms cubic-bezier(0.45, 0, 0.2, 1)`, `transform 100ms linear, opacity 80ms linear`, `opacity 80ms linear`

- tool: `background-size 0.25s linear, background-position 0.4s linear`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`, `transform 250ms cubic-bezier(0.33, 0, 0, 1)`, `transform 134ms cubic-bezier(0.45, 0, 0.2, 1)`, `transform 100ms linear, opacity 80ms linear`, `opacity 80ms linear`
