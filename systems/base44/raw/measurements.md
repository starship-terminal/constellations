# Component measurements

Computed styles read from base44.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the light theme every captured route paints (the bundle also declares a shadcn .dark block it never paints here; no consent overlay mounts on these routes), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The fixed bar: logo, the nav (Product, Use Cases, Solutions, Resources menus; Pricing, Enterprise, Superagents links), the language globe and the dark Start building pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 86 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.br-nav-label: Dazzed 16px/24px 500, #1e1e24 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 111 x 26, colour #0f0f0f |
| Painted layers | span::after.br-nav-label 62.4531pxx1px bg #1e1e24; span::after.br-nav-label 83.3906pxx1px bg #1e1e24; span::after.br-nav-label 73.3594pxx1px bg #1e1e24; span::after.br-nav-label 83.75pxx1px bg #1e1e24; span::after.br-nav-label 54.6562pxx1px bg #1e1e24; span::after.br-nav-label 80.9219pxx1px bg #1e1e24 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `header a[aria-label=Base44]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 111 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Transition | color, background-color, border-color, opacity 0.16s, 0.16s, 0.16s, 0.16s ease, ease, ease, ease delay 0s, 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 111 x 26, colour #0f0f0f |
| How | at rest |

Crops: `logo-default.png`.

#### nav-menu-button

Nav menu button. A top-level nav item that opens a mega menu (Product; Use Cases, Solutions and Resources are the same control).

Page: home. Selector: `header button:has-text("Product")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.45 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Dazzed 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Text node | span.br-nav-label: Dazzed 16px/24px 500, #1e1e24 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 4, colour #1e1e24 | = | = | = |
| Painted layers | span::after.br-nav-label 62.4531pxx1px bg #1e1e24 | = | button.font-medium.text-[16px] 81.5x24.0 r 6px outline 2px solid #1e1e24 offset 4px; span::after.br-nav-label 62.4531pxx1px bg #1e1e24 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-menu-button-default.png`, `nav-menu-button-hover.png`, `nav-menu-button-focus-visible.png`, `nav-menu-button-pressed.png`.

#### nav-product-open

Product menu, open. The nav button after its own press opens the full-width product panel; the crop holds the opened panel.

Page: home. Selector: `header button:has-text("Product")`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 81.45 x 24 |
| Padding | 0px |
| Gap | 9px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dazzed 16px/24px 500 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Text node | span.br-nav-label: Dazzed 16px/24px 500, #1e1e24 |
| Transition | none |
| Cursor | pointer |
| Icon | 10 x 4, colour #1e1e24 |
| Painted layers | span::after.br-nav-label 62.4531pxx1px bg #1e1e24 |
| How | menu held open by opts.open |

Crops: `nav-product-open-opened.png`.

#### nav-link

Nav link.

Page: home. Selector: `header a:has-text("Pricing")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54.66 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Dazzed 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Text node | span.br-nav-label: Dazzed 16px/24px 500, #1e1e24 | = | = | = |
| Transition | color, background-color, border-color, opacity 0.16s, 0.16s, 0.16s, 0.16s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::after.br-nav-label 54.6562pxx1px bg #1e1e24 | = | a.font-medium.text-[16px] 54.7x24.0 r 6px outline 2px solid #1e1e24 offset 4px; span::after.br-nav-label 54.6562pxx1px bg #1e1e24 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-superagents

Superagents link. The highlighted nav item, dotted either side and painted blue.

Page: home. Selector: `header a:has-text("Superagents")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.45 x 24 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Dazzed 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3950e6 | = | = | = |
| Text node | span.br-nav-sa-label: Dazzed 16px/24px 600, #3950e6 | = | = | = |
| Transition | color, background-color, border-color, opacity 0.16s, 0.16s, 0.16s, 0.16s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.size-[4px].shrink-0 4.0x4.0 bg #3950e6; span::after.br-nav-sa-label 101.453pxx1px bg #3950e6; span.size-[4px].shrink-0 4.0x4.0 bg #3950e6 | = | a.br-nav-sa.inline-flex 145.5x24.0 r 2px outline 2px solid #1e1e24 offset 4px; span.size-[4px].shrink-0 4.0x4.0 bg #3950e6; span::after.br-nav-sa-label 101.453pxx1px bg #3950e6; span.size-[4px].shrink-0 4.0x4.0 bg #3950e6 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-superagents-default.png`, `nav-superagents-hover.png`, `nav-superagents-focus-visible.png`, `nav-superagents-pressed.png`.

#### nav-locale

Language button. The globe icon left of the CTA.

Page: home. Selector: `header button[aria-label*="language"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.hidden.min-[1431px]:block 24.0x24.0 r 6px outline 2px solid #1e1e24 offset 4px | = |

Crops: `nav-locale-default.png`, `nav-locale-hover.png`, `nav-locale-focus-visible.png`, `nav-locale-pressed.png`.

#### nav-cta

Start building button. The dark pill on the right of the nav, repeated through the site. Measured, never followed.

Page: home. Selector: `header a:has-text("Start building")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129.17 x 38 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #312f2f | #433f3f | = | #433f3f |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/20.8px 600 | = | = | = |
| Letter spacing | -0.36px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.relative.leading-none: Geist 16px/16px 600, #ffffff, ls -0.36px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 129.2x38.0 bg #312f2f r 8px | a.group.relative 129.2x38.0 bg #433f3f r 8px | a.group.relative 129.2x38.0 bg #312f2f r 8px outline 2px solid #1e1e24 offset 4px | a.group.relative 129.2x38.0 bg #433f3f r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "Every builder needs a base" in the site's display face (Dazzed).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1135.47 x 98.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dazzed 93.744px/98.4312px 600 |
| Letter spacing | -3.74976px |
| Colour | #1e1e24 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subcopy.

Page: home. Selector: `first long paragraph under h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 726.77 x 58.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 21.024px/29.2234px 400 |
| Letter spacing | -0.21024px |
| Colour | #1e1e24 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### section-title

Section title.

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 535.05 x 119.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dazzed 57.024px/59.8752px 600 |
| Letter spacing | -2.28096px |
| Colour | #1e1e24 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### prompt-box

Prompt box. The hero's "I want to build…" composer: a white rounded card with the textarea and its button row.

Page: home. Selector: `.sa-prompt-box`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 555 x 150 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Text node | div.sa-prompt-box-placeholder.pointer-events-none: Geist 17px/26px 400, #6d6a67 |
| Transition | none |
| Icon | 14 x 14, colour #1e1e24 |
| Painted layers | div.sa-prompt-box.rounded-[8px] 555.0x150.0 bg #ffffff r 8px; span 45.6x28.0 bg #1e1e24 r 6px; span.sa-prompt-box-mic-tooltip 113.9x28.0 bg #1e1e24 r 6px; button.sa-prompt-box-submit-btn.flex 40.0x40.0 bg #ff773c r 8px; span.sa-prompt-box-icon-tooltip 53.2x28.0 bg #1e1e24 r 6px |
| How | at rest |

Crops: `prompt-box-default.png`.

#### prompt-field

Prompt field. The composer's textarea; sample text was typed and deleted, nothing sent.

Page: home. Selector: `textarea[aria-label="Describe the app you want to build"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 541 x 84 | = | = |
| Padding | 20px 12px 12px 24px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist 17px/26px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | #6d6a67, opacity 1 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `prompt-field-default.png`, `prompt-field-focused.png`, `prompt-field-filled.png`.

#### prompt-attach

Attach button. The "+" button at the composer's left. Measured, never pressed.

Page: home. Selector: `button[aria-label="More options"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f1eeea | = | #f1eeea |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Transition | background-color 0.16s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #1e1e24 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.sa-prompt-box-plus-btn.flex 40.0x40.0 bg #f1eeea r 8px | button.sa-prompt-box-plus-btn.flex 40.0x40.0 r 8px outline 2px solid #1e1e24 offset 4px | button.sa-prompt-box-plus-btn.flex 40.0x40.0 bg #f1eeea r 8px |

Crops: `prompt-attach-default.png`, `prompt-attach-hover.png`, `prompt-attach-focus-visible.png`, `prompt-attach-pressed.png`.

#### prompt-mode

Mode trigger. The "Build" dropdown inside the composer; its menu was not opened.

Page: home. Selector: `button:has-text("Build")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.09 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f1eeea | = | #f1eeea |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Transition | background-color 0.16s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #1e1e24 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.sa-prompt-box-mode-trigger.inline-flex 80.1x40.0 bg #f1eeea r 8px | button.sa-prompt-box-mode-trigger.inline-flex 80.1x40.0 r 8px outline 2px solid #1e1e24 offset 4px | button.sa-prompt-box-mode-trigger.inline-flex 80.1x40.0 bg #f1eeea r 8px |

Crops: `prompt-mode-default.png`, `prompt-mode-hover.png`, `prompt-mode-focus-visible.png`, `prompt-mode-pressed.png`.

#### prompt-mic

Voice button. The microphone button. Measured, never pressed.

Page: home. Selector: `button[aria-label="Voice input"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f1eeea | = | #f1eeea |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Transition | background-color 0.16s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 20, colour #1e1e24 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.sa-prompt-box-mic-btn.flex 40.0x40.0 bg #f1eeea r 8px | button.sa-prompt-box-mic-btn.flex 40.0x40.0 r 8px outline 2px solid #1e1e24 offset 4px | button.sa-prompt-box-mic-btn.flex 40.0x40.0 bg #f1eeea r 8px |

Crops: `prompt-mic-default.png`, `prompt-mic-hover.png`, `prompt-mic-focus-visible.png`, `prompt-mic-pressed.png`.

#### prompt-submit

Send button. The orange send button. Measured in all states except pressed for real — nothing was sent.

Page: home. Selector: `button[aria-label="Send message"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | 38.8 x 38.8 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ff773c | #ff8f5c | = | #ff8f5c |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Transition | background-color, transform 0.16s, 0.1s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #1e1e24 | = | = | 11.64 x 11.64, colour #1e1e24 |
| Painted layers | button.sa-prompt-box-submit-btn.flex 40.0x40.0 bg #ff773c r 8px | button.sa-prompt-box-submit-btn.flex 40.0x40.0 bg #ff8f5c r 8px | button.sa-prompt-box-submit-btn.flex 40.0x40.0 bg #ff773c r 8px outline 2px solid #1e1e24 offset 4px | button.sa-prompt-box-submit-btn.flex 38.8x38.8 bg #ff8f5c r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `prompt-submit-default.png`, `prompt-submit-hover.png`, `prompt-submit-focus-visible.png`, `prompt-submit-pressed.png`.

#### build-tile

Build-type tile. One of the five "What will you build?" tiles under the composer (App; Dashboard, Website, Mobile app and Online store are the same control).

Page: home. Selector: `button.br-build-type-tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120 x 66 | = | = | = |
| Padding | 14px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #f9f7f4 | #e2ded7 | = | #e2ded7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Transition | background-color, color 0.2s, 0.2s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6073f0 | = | = | = |
| Painted layers | button.br-build-type-tile 120.0x66.0 bg #f9f7f4 r 4px | button.br-build-type-tile 120.0x66.0 bg #e2ded7 r 4px | button.br-build-type-tile 120.0x66.0 bg #f9f7f4 r 4px outline 2px solid #1e1e24 offset 4px | button.br-build-type-tile 120.0x66.0 bg #e2ded7 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `build-tile-default.png`, `build-tile-hover.png`, `build-tile-focus-visible.png`, `build-tile-pressed.png`.

#### faq-item

FAQ item. A collapsed row of the FAQ accordion.

Page: home. Selector: `button:has-text("What is Base44?")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 712.47 x 66.97 | = | = | = |
| Padding | 32.976px 0px 0px 0px | = | = | = |
| Gap | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Dazzed 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Text node | span.br-faq-q.br-display: Dazzed 24.0048px/30.006px 600, #1e1e24, ls -0.720144px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #1e1e24 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.w-full 712.5x67.0 r 6px outline 2px solid #1e1e24 offset 4px | = |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`.

#### faq-open

FAQ item, expanded. The same row after its own press; the crop holds the item and its answer.

Page: home. Selector: `button:has-text("What is Base44?")`. States: expanded.

| Property | expanded |
|---|---|
| Size (w x h) | 712.47 x 66.97 |
| Padding | 32.976px 0px 0px 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dazzed 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Text node | span.br-faq-q.br-display: Dazzed 24.0048px/30.006px 600, #1e1e24, ls -0.720144px |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #1e1e24 |
| How | own toggle |

Crops: `faq-open-expanded.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 790 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Text node | p.footer-tagline: Geist 16px/24px 400, #1e1e24 |
| Transition | none |
| Icon | 111 x 26, colour #1e1e24 |
| Painted layers | footer.br-footer 1440.0x790.0 bg #ffffff; span::after.br-footer-underline 67.0156pxx1px bg #1e1e24; span::after.br-footer-underline 121.375pxx1px bg #1e1e24; span::after.br-footer-underline 56.75pxx1px bg #1e1e24; span::after.br-footer-underline 63.9531pxx1px bg #1e1e24; span::after.br-footer-underline 87.0469pxx1px bg #1e1e24 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a.br-footer-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.02 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Text node | span.br-footer-underline: Geist 16px/32px 400, #1e1e24 | = | = | = |
| Transition | color, background-color, border-color, opacity 0.16s, 0.16s, 0.16s, 0.16s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::after.br-footer-underline 67.0156pxx1px bg #1e1e24 | = | a.br-footer-link.footer-link 67.0x21.0 r 6px outline 2px solid #1e1e24 offset 4px; span::after.br-footer-underline 67.0156pxx1px bg #1e1e24 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon. One of the social icon links (X; Discord, LinkedIn and Reddit are the same control).

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 26 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Text node | undefined: Geist 16px/24px 400, #1e1e24 | = | = | = |
| Transition | color, background-color, border-color, opacity 0.16s, 0.16s, 0.16s, 0.16s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 26 x 26, colour #1e1e24 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-[#1e1e24] 26.0x26.0 r 6px outline 2px solid #1e1e24 offset 4px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-legal

Legal link.

Page: home. Selector: `footer a:has-text("Privacy")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.3 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 16px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Text node | span.br-footer-underline: Geist 16px/32px 400, #1e1e24 | = | = | = |
| Transition | color, background-color, border-color, opacity 0.16s, 0.16s, 0.16s, 0.16s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::after.br-footer-underline 101.297pxx1px bg #1e1e24 | = | a.br-footer-link.footer-link 101.3x21.0 r 6px outline 2px solid #1e1e24 offset 4px; span::after.br-footer-underline 101.297pxx1px bg #1e1e24 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1278.86 x 93.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dazzed 87.904px/93.1782px 600 |
| Letter spacing | -2.90083px |
| Colour | #1e1e24 |
| Text node | span: Dazzed 87.904px/93.1782px 600, #1e1e24, ls -2.90083px |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-toggle

Billing toggle. The Yearly/Monthly segment control over the plan cards.

Page: pricing. Selector: `parent of .pricing-toggle-btn`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 283.05 x 56 |
| Padding | 4px |
| Border | none |
| Radius | 12px |
| Background | #ffffff @ 0.6 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Text node | button.pricing-toggle-btn.relative: Geist 20px/28px 500, #1e1e24, ls -0.4px |
| Transition | none |
| Painted layers | div.font-geist.relative 283.0x56.0 bg #ffffff @ 0.6 r 12px; span.pointer-events-none.absolute 170.0x48.0 bg #ff773c r 8px |
| How | at rest |

Crops: `billing-toggle-default.png`.

#### billing-yearly

Yearly segment. The selected segment ("Yearly SAVE 20%"), painted orange.

Page: pricing. Selector: `button:has-text("Yearly")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170 x 48 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 20px/28px 500 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Text node | undefined: Geist 17px/17px 400, #1e1e24, ls -0.4px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.font-geist.relative bg #ffffff @ 0.6 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.pricing-toggle-btn.relative 170.0x48.0 r 8px outline 2px solid #1e1e24 offset 4px | = |

Crops: `billing-yearly-default.png`, `billing-yearly-hover.png`, `billing-yearly-focus-visible.png`, `billing-yearly-pressed.png`.

#### billing-monthly

Monthly segment. The unselected segment; switching it is a local toggle, no purchase.

Page: pricing. Selector: `button:has-text("Monthly")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.05 x 48 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 20px/28px 500 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #1e1e24 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.font-geist.relative bg #ffffff @ 0.6 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.pricing-toggle-btn.relative 105.0x48.0 r 8px outline 2px solid #1e1e24 offset 4px | = |

Crops: `billing-monthly-default.png`, `billing-monthly-hover.png`, `billing-monthly-focus-visible.png`, `billing-monthly-pressed.png`.

#### plan-cta

Plan CTA. The full-width "Start building" button inside a plan card. Measured, never followed.

Page: pricing. Selector: `.br-cta-fluid inside a plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 50 | = | = | = |
| Padding | 0px 26px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 10px | = | = | = |
| Background | #312f2f | #433f3f | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1e1e24 offset 4px | = |
| Font | Geist 18px/18px 500 | = | = | = |
| Letter spacing | -0.72px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.flex.h-[1.05em]: Geist 18px/normal 500, #ffffff, ls -0.72px | = | = | = |
| Transition | background-color, color, border-color 0.2s, 0.2s, 0.2s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.br-cta-fluid.group/cta 380.0x50.0 bg #312f2f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px | a.br-cta-fluid.group/cta 380.0x50.0 bg #433f3f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px | a.br-cta-fluid.group/cta 380.0x50.0 bg #312f2f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px outline 2px solid #1e1e24 offset 4px | = |
| Ancestor paint | 1 up div.pricing-card.relative bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-card

Plan card.

Page: pricing. Selector: `.pricing-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 691.42 |
| Padding | 30px 20px |
| Gap | 21.024px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Text node | h3.pc-name.font-dazzed: Dazzed 36px/39.6px 600, #1e1e24 |
| Transition | none |
| Icon | 14 x 14, colour #1e1e24 |
| Painted layers | div.pricing-card.relative 420.0x691.4 bg #ffffff; div.h-[2px].w-full 380.0x2.0 bg #1e1e24; span 288.0x101.0 bg #1e1e24 r 6px; div.h-[2px].w-full 380.0x2.0 bg #1e1e24; a.br-cta-fluid.group/cta 380.0x50.0 bg #312f2f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px |
| How | at rest |

Crops: `plan-card-default.png`.

#### popular-badge

Popular badge. The blue chip on the Builder plan card.

Page: pricing. Selector: `span:has-text("Popular")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 70.81 x 28 |
| Padding | 7px 10px |
| Border | none |
| Radius | 4px |
| Background | #3b51e5 |
| Box shadow | none |
| Outline | none |
| Font | Geist 14px/14px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | span.font-geist.shrink-0 70.8x28.0 bg #3b51e5 r 4px |
| How | at rest |

Crops: `popular-badge-default.png`.

#### price

Price figure. A plan's price ("$160" on Elite at yearly billing).

Page: pricing. Selector: `text "$NNN"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380.02 x 48 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Text node | span.pc-currency.font-geist: Geist 48px/48px 400, #1e1e24 |
| Transition | none |
| How | at rest |

Crops: `price-default.png`.

### Sign in

#### signin-title

Sign-in title. "Welcome to Base44" on app.base44.com/login.

Page: signin. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dazzed 28px/32px 560 |
| Letter spacing | -0.56px |
| Colour | #0f0e0e |
| Transition | none |
| Ancestor paint | 3 up div.w-full.max-w-md shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `signin-title-default.png`.

#### signin-google

Log in with Google. The OAuth button. Measured, never pressed — no sign-in was attempted.

Page: signin. Selector: `button:has-text("Log in with Google")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #c9c3bc | 1px solid #99928b | 1px solid #99928b | 1px solid #99928b |
| Radius | 6px | = | = | = |
| Background | transparent | #e9e6e0 | = | #ddd8d2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3b51e5 offset -1px | = |
| Font | Wix Madefor Text 14px/18px 460 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0e0e | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 25.2 x 25.2, colour #0f0e0e | = | = | = |
| Painted layers | button.inline-flex.items-center 384.0x36.0 border T:1px solid #c9c3bc / R:1px solid #c9c3bc / B:1px solid #c9c3bc / L:1px solid #c9c3bc r 6px | button.inline-flex.items-center 384.0x36.0 bg #e9e6e0 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px | button.inline-flex.items-center 384.0x36.0 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px outline 2px solid #3b51e5 offset -1px | button.inline-flex.items-center 384.0x36.0 bg #ddd8d2 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px |
| Ancestor paint | 3 up div.w-full.max-w-md shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-google-default.png`, `signin-google-hover.png`, `signin-google-focus-visible.png`, `signin-google-pressed.png`.

#### signin-apple

Log in with Apple. The OAuth button. Measured, never pressed.

Page: signin. Selector: `button:has-text("Log in with Apple")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #c9c3bc | 1px solid #99928b | 1px solid #99928b | 1px solid #99928b |
| Radius | 6px | = | = | = |
| Background | transparent | #e9e6e0 | = | #ddd8d2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3b51e5 offset -1px | = |
| Font | Wix Madefor Text 14px/18px 460 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0e0e | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #0f0e0e | = | = | = |
| Painted layers | button.inline-flex.items-center 384.0x36.0 border T:1px solid #c9c3bc / R:1px solid #c9c3bc / B:1px solid #c9c3bc / L:1px solid #c9c3bc r 6px | button.inline-flex.items-center 384.0x36.0 bg #e9e6e0 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px | button.inline-flex.items-center 384.0x36.0 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px outline 2px solid #3b51e5 offset -1px | button.inline-flex.items-center 384.0x36.0 bg #ddd8d2 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px |
| Ancestor paint | 3 up div.w-full.max-w-md shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-apple-default.png`, `signin-apple-hover.png`, `signin-apple-focus-visible.png`, `signin-apple-pressed.png`.

#### signin-github

Log in with GitHub. The OAuth button. Measured, never pressed.

Page: signin. Selector: `button:has-text("Log in with GitHub")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #c9c3bc | 1px solid #99928b | 1px solid #99928b | 1px solid #99928b |
| Radius | 6px | = | = | = |
| Background | transparent | #e9e6e0 | = | #ddd8d2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3b51e5 offset -1px | = |
| Font | Wix Madefor Text 14px/18px 460 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0e0e | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #0f0e0e | = | = | = |
| Painted layers | button.inline-flex.items-center 384.0x36.0 border T:1px solid #c9c3bc / R:1px solid #c9c3bc / B:1px solid #c9c3bc / L:1px solid #c9c3bc r 6px | button.inline-flex.items-center 384.0x36.0 bg #e9e6e0 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px | button.inline-flex.items-center 384.0x36.0 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px outline 2px solid #3b51e5 offset -1px | button.inline-flex.items-center 384.0x36.0 bg #ddd8d2 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px |
| Ancestor paint | 3 up div.w-full.max-w-md shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-github-default.png`, `signin-github-hover.png`, `signin-github-focus-visible.png`, `signin-github-pressed.png`.

#### signin-field-wrap

Email field shell. The bordered box holding the email input.

Page: signin. Selector: `bordered ancestor of the email input (marked in-page)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 36 |
| Padding | 8px 12px |
| Gap | 6px |
| Border | 1px solid #99928b |
| Radius | 6px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Wix Madefor Text 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0f0e0e |
| Transition | background-color, border-color, box-shadow 0.26s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.group.flex 384.0x36.0 border T:1px solid #99928b / R:1px solid #99928b / B:1px solid #99928b / L:1px solid #99928b r 6px; input.flex-1.min-w-0 358.0x18.0 outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `signin-field-wrap-default.png`.

#### signin-field

Email field. The sign-in email input; sample text was typed and deleted, nothing sent.

Page: signin. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 358 x 18 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Wix Madefor Text 14px/18px 460 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0f0e0e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #99928b, opacity 1 | = | = |
| Painted layers | input.flex-1.min-w-0 358.0x18.0 outline 2px solid #000000 @ 0 offset 2px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |
| Ancestor paint | - | 1 up div.group.flex bg #ffffff @ 0.3 | 1 up div.group.flex bg #ffffff @ 0.3 |

Crops: `signin-field-default.png`, `signin-field-focused.png`, `signin-field-filled.png`.

#### signin-submit

Continue with email button. The email sign-in submit, captured disabled as painted for an empty field (the state was measured, never enabled or pressed).

Page: signin. Selector: `button:has-text("Continue with email")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 36 |
| Padding | 0px 16px |
| Gap | 4px |
| Border | none |
| Radius | 6px |
| Background | #ebebeb |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Wix Madefor Text 14px/18px 460 |
| Letter spacing | normal |
| Colour | #929292 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | button.inline-flex.items-center 384.0x36.0 bg #ebebeb r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 2 up div.w-full.max-w-md shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `signin-submit-default.png`.

#### signin-signup

Sign up link. The register link under the form. Measured, never followed.

Page: signin. Selector: `a:has-text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.2 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b51e5 0px 0px 0px 3px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Wix Madefor Text 14px/18px 460 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0e0e | #3a3939 | #5d5d5d | #3a3939 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 2 up div.w-full.max-w-md shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.inline-flex.items-center 50.2x18.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b51e5 0px 0px 0px 3px outline 2px solid #000000 @ 0 offset 2px | = |

Crops: `signin-signup-default.png`, `signin-signup-hover.png`, `signin-signup-focus-visible.png`, `signin-signup-pressed.png`.

#### signin-legal

Legal link.

Page: signin. Selector: `a:has-text("Terms of Service")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.61 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Wix Madefor Text 12px/16px 460 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5d5d5d | #0f0e0e | = | #0f0e0e |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.cursor-pointer.font-medium 93.6x15.0 outline 1px auto #005fcc offset 1px | = |

Crops: `signin-legal-default.png`, `signin-legal-hover.png`, `signin-legal-focus-visible.png`, `signin-legal-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 54 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.relative.leading-none: Geist 14px/14px 500, #ffffff, ls -0.14px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 94 x 22, colour #0f0f0f |
| Painted layers | span::after.br-nav-label autox1px bg #1e1e24; span::after.br-nav-label autox1px bg #1e1e24; span::after.br-nav-label autox1px bg #1e1e24; span::after.br-nav-label autox1px bg #1e1e24; span::after.br-nav-label autox1px bg #1e1e24; span::after.br-nav-label autox1px bg #1e1e24 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. The hamburger trigger at the right of the mobile bar; its own press opens the full-sheet menu.

Page: home. Selector: `header button[aria-label*="menu"]`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1e1e24 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The trigger after its own toggle; the open sheet shows in the crop.

Page: home. Selector: `header menu trigger`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1e24 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #1e1e24 |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `transform var(--dur-hover) var(--ease-standard)`, `none`, `transform .3s var(--ease-standard)`, `background-color var(--dur-hover, .2s) var(--ease-standard)`, `color var(--dur-hover, .2s) var(--ease-standard)`, `border-color var(--dur-hover, .2s) var(--ease-standard)`, `border-color var(--dur-hover, .2s) var(--ease-standard),color var(--dur-hover, .2s) var(--ease-standard)`, `background-color var(--dur-fast, .15s) var(--ease-standard)`, `transform var(--dur-fast, .15s) var(--ease-standard)`, `background-color var(--dur-hover, .2s) var(--ease-standard),border-color var(--dur-hover, .2s) var(--ease-standard)`, `transform var(--dur-hover, .2s) var(--ease-snap, cubic-bezier(.34, 1.56, .64, 1)),opacity .12s var(--ease-standard)`, `transform var(--dur-hover, .2s) var(--ease-snap, cubic-bezier(.34, 1.56, .64, 1))`

- pricing: `transform var(--dur-hover) var(--ease-standard)`, `none`, `transform .3s var(--ease-standard)`, `background-color var(--dur-hover, .2s) var(--ease-standard)`, `color var(--dur-hover, .2s) var(--ease-standard)`, `border-color var(--dur-hover, .2s) var(--ease-standard)`, `border-color var(--dur-hover, .2s) var(--ease-standard),color var(--dur-hover, .2s) var(--ease-standard)`, `background-color var(--dur-fast, .15s) var(--ease-standard)`, `transform var(--dur-fast, .15s) var(--ease-standard)`, `background-color var(--dur-hover, .2s) var(--ease-standard),border-color var(--dur-hover, .2s) var(--ease-standard)`, `transform var(--dur-hover, .2s) var(--ease-snap, cubic-bezier(.34, 1.56, .64, 1)),opacity .12s var(--ease-standard)`, `transform var(--dur-hover, .2s) var(--ease-snap, cubic-bezier(.34, 1.56, .64, 1))`
