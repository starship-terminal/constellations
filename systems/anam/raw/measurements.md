# Component measurements

Computed styles read from anam.ai on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Panels and dialogs

#### consent-card

Cookie consent card. The .anam-cc-card consent card pinned bottom-right on a fresh profile (Manage cookies / Reject all / Accept all). Photographed and measured in place, then hidden without a click: a consent choice is a submission.

Page: home. Selector: `.anam-cc-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 180 |
| Padding | 20px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.18 0px 12px 32px -8px, #000000 @ 0.06 0px 1px 2px 0px |
| Outline | none |
| Font | Inter 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.anam-cc-body: Inter 15px/21px 400, #000000 @ 0.62, ls -0.15px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | section.anam-cc-card 420.0x180.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 16px shadow #000000 @ 0.18 0px 12px 32px -8px, #000000 @ 0.06 0px 1px 2px 0px; button.anam-cc-btn.anam-cc-btn--text 119.7x38.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; button.anam-cc-btn.anam-cc-btn--choice 102.8x38.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; button.anam-cc-btn.anam-cc-btn--choice 109.1x38.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px |
| How | at rest |

Crops: `consent-card-default.png`.

#### consent-manage

Manage cookies button. The text button in the consent card. Measured and focused, never pressed.

Page: home. Selector: `"Manage cookies" in .anam-cc-card`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 119.69 x 38 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 999px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 offset 2px |
| Font | Inter 15px/15px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | background-color, border-color 0.16s, 0.16s cubic-bezier(0.16, 1, 0.3, 1), ease delay 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.anam-cc-btn.anam-cc-btn--text 119.7x38.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | = | button.anam-cc-btn.anam-cc-btn--text 119.7x38.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px outline 2px solid #000000 offset 2px |
| Ancestor paint | 2 up section.anam-cc-card bg #ffffff shadow #000000 @ 0.18 0px 12px 32px -8px, #000000 @ 0.06 0px 1px 2px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `consent-manage-default.png`, `consent-manage-hover.png`, `consent-manage-focus-visible.png`.

#### consent-accept

Accept all button. The filled choice button in the consent card. Measured and focused, never pressed: accepting is a submission.

Page: home. Selector: `"Accept all" in .anam-cc-card`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 109.11 x 38 | = | = |
| Padding | 0px 18px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 999px | = | = |
| Background | #f5f5f5 | #ebebeb | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 offset 2px |
| Font | Inter 15px/15px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | background-color, border-color 0.16s, 0.16s cubic-bezier(0.16, 1, 0.3, 1), ease delay 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.anam-cc-btn.anam-cc-btn--choice 109.1x38.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | button.anam-cc-btn.anam-cc-btn--choice 109.1x38.0 bg #ebebeb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | button.anam-cc-btn.anam-cc-btn--choice 109.1x38.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px outline 2px solid #000000 offset 2px |
| Ancestor paint | 2 up section.anam-cc-card bg #ffffff shadow #000000 @ 0.18 0px 12px 32px -8px, #000000 @ 0.06 0px 1px 2px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `consent-accept-default.png`, `consent-accept-hover.png`, `consent-accept-focus-visible.png`.

#### docs-search-dialog

Search dialog. The ⌘K search overlay: a field, result list and keyboard hints. Opened by keyboard; nothing was typed.

Page: docs-overview. Selector: `the [role=dialog] search overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 62 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #110d0a @ 0.06 0px 0px 0px 1px, #000000 @ 0.01 0px 57px 34px 0px, #000000 @ 0.02 0px 25px 25px 0px, #000000 @ 0.02 0px 6px 14px 0px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.shrink-0.self-stretch: Inter 14px/20px 500, #77726f, ls -0.1px |
| Transition | transform, scale, opacity 0.25s cubic-bezier(0.22, 1, 0.36, 1) |
| Icon | 16 x 16, colour #77726f, fill #000000 |
| Painted layers | div.origin-center.flex 640.0x62.0 bg #ffffff r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #110d0a @ 0.06 0px 0px 0px 1px, #000000 @ 0.01 0px 57px 34px 0px, #000000 @ 0.02 0px 25px 25px 0px, #000000 @ 0.02 0px 6px 14px 0px; div.relative.h-full 628.0x50.0 bg #ffffff border T:1px solid #e6e1de / R:1px solid #e6e1de / B:1px solid #e6e1de / L:1px solid #e6e1de r 16px; button.shrink-0.self-stretch 143.7x32.0 bg #110d0a @ 0.05 r 10px |
| How | at rest |

Crops: `docs-search-dialog-default.png`.

#### docs-search-input

Search field.

Page: docs-overview. Selector: `the input inside the search dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 460.34 x 36 |
| Padding | 0px 0px 0px 30px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | -0.2px |
| Colour | #110d0a |
| Transition | none |
| Cursor | text |
| Placeholder | #a6a19e, opacity 1 |
| Ancestor paint | 1 up div.relative.h-full bg #ffffff; 3 up div.origin-center.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #110d0a @ 0.06 0px 0px 0px 1px, #000000 @ 0.01 0px 57px 34px 0px, #000000 @ 0.02 0px 25px 25px 0px, #000000 @ 0.02 0px 6px 14px 0px |
| How | at rest |

Crops: none.

#### docs-assistant-panel

Assistant panel. The "Ask Assistant" sheet with a question box and send button. Opened by keyboard; nothing was typed or sent.

Page: docs-overview. Selector: `the assistant sheet`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 368 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #77726f |
| Text node | span.font-medium.text-gray-900: Inter 16px/24px 500, #1e1916 |
| Transition | none |
| Icon | 20 x 20, colour #ff6200, fill #000000 |
| Painted layers | div.flex.flex-col 368.0x900.0 bg #ffffff; div.flex.flex-col 336.0x84.0 bg #ffffff border T:1px solid #e6e1de / R:1px solid #e6e1de / B:1px solid #e6e1de / L:1px solid #e6e1de r 16px; button.chat-assistant-send-button.flex 24.0x24.0 bg #ff6200 @ 0.3 r 9999px |
| Ancestor paint | 1 up div.sticky.shrink-0 bg #ffffff |
| How | at rest |

Crops: `docs-assistant-panel-default.png`.

#### docs-assistant-send

Assistant send button. The send control in the assistant sheet. Measured, never pressed.

Page: docs-overview. Selector: `"Send message" in the assistant panel`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 24 x 24 | = | - |
| Padding | 4px | = | - |
| Border | none | = | - |
| Radius | 9999px | = | - |
| Background | #ff6200 @ 0.3 | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Inter 16px/24px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #77726f | = | - |
| Transition | none | = | - |
| Cursor | default | = | - |
| Icon | 10 x 10, colour #ffffff, fill #000000 | = | - |
| Painted layers | button.chat-assistant-send-button.flex 24.0x24.0 bg #ff6200 @ 0.3 r 9999px | = | - |
| How | at rest | mouse hover | - |
| Error | - | = | keyboard focus could not be moved to the element |

Crops: `docs-assistant-send-default.png`, `docs-assistant-send-hover.png`.

### Shell and navigation

#### nav-bar

Top navigation bar. The floating pill nav on every marketing page: the Anam logo, the section links (Developers, Pricing, Resources, Company), Sign in and the Get started button.

Page: tools. Selector: `the fixed nav container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.anam-nav-link: Inter 14px/16.8px 500, #000000 |
| Transition | none |
| Icon | 60 x 22, colour #000000 |
| ::after | 1440px x 523px, fixed, bg #f4f4f4 @ 0.55, radius 0px |
| Painted layers | header::after.anam-site-nav 1440pxx523px bg #f4f4f4 @ 0.55; div.anam-nav-shell 1440.0x100.0 bg #ffffff; a.anam-signin-pill 96.6x34.0 bg #f5f5f5 r 50px; button.anam-mobile-toggle 0.0x0.0 bg #efefef border T:2px outset #000000 / R:2px outset #000000 / B:2px outset #000000 / L:2px outset #000000 |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-link

Nav link. A section link in the pill nav. Measured, never followed.

Page: tools. Selector: `"Pricing" inside the nav`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.73 x 32.8 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #000000 @ 0.18 offset 2px | = |
| Font | Inter 14px/16.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #000000 @ 0.5 | #000000 @ 0.5 | #000000 @ 0.5 |
| Transition | color 0.2s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.anam-nav-link 78.7x32.8 r 6px outline 1px solid #000000 @ 0.18 offset 2px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign in link. The quiet "Sign in" action (lab.anam.ai/login). Measured, never followed.

Page: tools. Selector: `"Sign in" inside the nav`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 96.58 x 34 | = | = |
| Padding | 16px 24px | = | = |
| Border | none | = | = |
| Radius | 50px | = | = |
| Background | #f5f5f5 | #e8e6e6 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | Inter 15px/15px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | background, transform 0.4s, 0.4s cubic-bezier(0.44, 0, 0.56, 1), cubic-bezier(0.44, 0, 0.56, 1) delay 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.anam-signin-pill 96.6x34.0 bg #f5f5f5 r 50px | a.anam-signin-pill 96.6x34.0 bg #e8e6e6 r 50px | a.anam-signin-pill 96.6x34.0 bg #f5f5f5 r 50px outline 1px auto #005fcc offset 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`.

#### nav-submenu

Nav submenu. The dropdown that opens under a nav section on hover (Developers: Documentation, Tools, Changelog; Company: Team, Research, Security). Shown in its hover-open state.

Page: tools. Selector: `the open ContentSubMenu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 222 x 128.91 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.anam-submenu-eyebrow: Inter 13px/16.9px 500, #000000 @ 0.5 |
| Transition | none |
| How | at rest |

Crops: `nav-submenu-default.png`.

#### footer

Footer. The page footer: product/company/legal link columns, socials and the status line.

Page: tools. Selector: `the footer block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 1154.59 |
| Padding | 64px 0px 40px 0px |
| Border | none |
| Radius | 32px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.anam-footer-group-title: Inter 15px/18px 400, #ffffff @ 0.5 |
| Transition | none |
| Painted layers | footer.anam-footer 1400.0x1154.6 bg #000000 r 32px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A quiet link in the footer columns. Measured, never followed.

Page: tools. Selector: `a legal link inside the footer`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 112.44 x 18 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | Inter 15px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff @ 0.8 | #ffffff | #ffffff |
| Transition | color 0.15s ease | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a 112.4x18.0 outline 1px auto #005fcc offset 1px |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`.

#### nav-sub-link

Submenu link. A row inside the open nav dropdown. Measured, never followed.

Page: pricing. Selector: `a link inside the submenu`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 102.02 x 19 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #ff6200 offset 3px |
| Font | Inter 15px/22.5px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.pricing-module__lP4odW__textLink 102.0x19.0 outline 2px solid #ff6200 offset 3px |

Crops: `nav-sub-link-default.png`, `nav-sub-link-hover.png`, `nav-sub-link-focus-visible.png`.

### Home

#### hero-title

Hero title. "Create interactive avatars for…" — the display line the home page opens with (the last word rotates through personas).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1240 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subline.

Page: home. Selector: `the paragraph under the h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 353.47 x 27.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 13px/15.6px 500, #ff6200 |
| Transition | none |
| Painted layers | a.framer-0niav.framer-v-10tw580 353.5x27.6 bg #ff6200 @ 0.05 r 40px; div 3.0x3.0 bg #ff6200 r 6px; div 3.0x3.0 bg #ff6200 r 6px; div 3.0x3.0 bg #ff6200 r 6px |
| How | at rest |

Crops: none.

#### hero-cta

Hero CTA button. The primary button under the hero copy. Links to lab.anam.ai/register; measured, never followed.

Page: home. Selector: `"Get started"/"Start building" near the hero`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.02 x 34 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #000000 | #000000 @ 0.85 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 15px/18px 500, #ffffff | p.framer-text: Inter 15px/18px 500, #ffffff @ 0.85 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-Ey2WY.framer-v-g1wz6y 128.0x34.0 bg #000000 r 50px | a.framer-Ey2WY.framer-v-g1wz6y 128.0x34.0 bg #000000 @ 0.85 r 50px | a.framer-Ey2WY.framer-v-g1wz6y 128.0x34.0 bg #000000 r 50px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### persona-chip

Persona chip. One of the persona selector cards under the hero demo (Mia medical services, Anne skills training, Richard customer support, Liv sales, Gabriel language tutor). Pressed is forced; a real press only swaps the persona the demo card names.

Page: home. Selector: `a [role=button] persona card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 451 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text: Inter 2px/2.4px 400, #000000 | = | = | = |
| Transition | transform 0.3s cubic-bezier(0.12, 0.23, 0.5, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 160, -225.5) | matrix(1, 0, 0, 1, 1616, -225.5) | matrix(1, 0, 0, 1, 1616, -225.5) | matrix(1, 0, 0, 1, 1616, -225.5) |
| Cursor | pointer | = | = | = |
| Painted layers | div 340.0x403.0 r 32px shadow #000000 @ 0.01 0px 124px 50px 0px, #000000 @ 0.05 0px 70px 42px 0px, #000000 @ 0.09 0px 31px 31px 0px, #000000 @ 0.1 0px 8px 17px 0px; div.framer-FrIXp.framer-v-7a4czi 48.0x48.0 bg #ffffff @ 0.5 r 50px; div::after.framer-FrIXp.framer-v-7a4czi 48pxx48px border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px; div.framer-I1bjZ 24.0x24.0 bg #000000 @ 0.7; div.framer-FrIXp.framer-v-w05bga 156.7x48.0 bg #ffffff @ 0.5 r 50px; div::after.framer-FrIXp.framer-v-w05bga 156.719pxx48px border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px | div 340.0x403.0 r 32px shadow #000000 @ 0.01 0px 124px 50px 0px, #000000 @ 0.05 0px 70px 42px 0px, #000000 @ 0.09 0px 31px 31px 0px, #000000 @ 0.1 0px 8px 17px 0px | div 340.0x451.0 outline 1px auto #005fcc offset 0px; div 340.0x403.0 r 32px shadow #000000 @ 0.01 0px 124px 50px 0px, #000000 @ 0.05 0px 70px 42px 0px, #000000 @ 0.09 0px 31px 31px 0px, #000000 @ 0.1 0px 8px 17px 0px | div 340.0x403.0 r 32px shadow #000000 @ 0.01 0px 124px 50px 0px, #000000 @ 0.05 0px 70px 42px 0px, #000000 @ 0.09 0px 31px 31px 0px, #000000 @ 0.1 0px 8px 17px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `persona-chip-default.png`, `persona-chip-hover.png`, `persona-chip-focus-visible.png`, `persona-chip-pressed.png`.

#### persona-chip-selected

Persona chip, selected. The same chip after a press, in its selected state (the demo card now names that persona).

Page: home. Selector: `a pressed persona card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 340 x 451 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 2px/2.4px 400, #000000 |
| Transition | transform 0.3s cubic-bezier(0.12, 0.23, 0.5, 1) |
| Transform | matrix(1, 0, 0, 1, 2742, -225.5) |
| Cursor | pointer |
| Painted layers | div 408.0x483.6 r 32px shadow #000000 @ 0.01 0px 124px 50px 0px, #000000 @ 0.05 0px 70px 42px 0px, #000000 @ 0.09 0px 31px 31px 0px, #000000 @ 0.1 0px 8px 17px 0px; div.framer-FrIXp.framer-v-7a4czi 57.6x57.6 bg #ffffff @ 0.5 r 50px; div::after.framer-FrIXp.framer-v-7a4czi 48pxx48px border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px; div.framer-I1bjZ 28.8x28.8 bg #000000 @ 0.7; div.framer-FrIXp.framer-v-w05bga 194.2x57.6 bg #ffffff @ 0.5 r 50px; div::after.framer-FrIXp.framer-v-w05bga 161.828pxx48px border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px |
| How | at rest |

Crops: `persona-chip-selected-default.png`.

#### demo-card

Avatar demo card. The "Talk with …" card under the hero: the avatar preview, the persona name and the call controls. The call button starts a live avatar session with microphone access, so it is measured inside the card and never pressed.

Page: home. Selector: `the visible Talk-with card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 408 x 483.6 |
| Padding | 0px |
| Gap | 30px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 15px/18px 500, #000000 @ 0.7, ls -0.3px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div 408.0x483.6 r 32px shadow #000000 @ 0.01 0px 124px 50px 0px, #000000 @ 0.05 0px 70px 42px 0px, #000000 @ 0.09 0px 31px 31px 0px, #000000 @ 0.1 0px 8px 17px 0px; div.framer-FrIXp.framer-v-7a4czi 57.6x57.6 bg #ffffff @ 0.5 r 50px; div::after.framer-FrIXp.framer-v-7a4czi 48pxx48px border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px; div.framer-I1bjZ 28.8x28.8 bg #000000 @ 0.7; div.framer-FrIXp.framer-v-w05bga 194.2x57.6 bg #ffffff @ 0.5 r 50px; div::after.framer-FrIXp.framer-v-w05bga 161.828pxx48px border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px |
| How | at rest |

Crops: `demo-card-default.png`.

#### tab-section

Feature tab section. The scroll-driven tab showcase (TabSection): a tab per feature with a video or metric card beside it.

Page: home. Selector: `[data-framer-name=TabSection]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 765 |
| Padding | 0px 20px 100px 20px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.framer-text: Inter 32px/38.4px 500, #000000, ls -0.64px |
| Transition | none |
| Painted layers | a.framer-Ey2WY.framer-v-g1wz6y 143.8x34.0 bg #000000 r 50px; div 2.0x95.8 bg #000000 @ 0.12 r 30px; div 2.0x6.2 bg #ff6200 r 99px; div 2.0x28.8 bg #000000 @ 0.12 r 30px; div 2.0x28.8 bg #000000 @ 0.12 r 30px; div 620.0x665.0 bg #f5f5f5 r 32px |
| How | at rest |

Crops: `tab-section-default.png`.

#### cta-band

Sticky CTA band. The "Build the future of customer experience. Today." band pinned at the foot of the page, with a Get started button.

Page: home. Selector: `the bottom sticky CTA`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 163.59 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.framer-text: Inter 48px/52.8px 500, #000000, ls -0.96px |
| Transition | none |
| Painted layers | a.framer-Ey2WY.framer-v-g1wz6y 128.0x34.0 bg #000000 r 50px |
| How | at rest |

Crops: `cta-band-default.png`.

#### tab-item

Feature tab. A tab label inside the showcase. Measured, never pressed: the section advances on scroll.

Page: home. Selector: `a tab inside TabSection`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 372 x 28.8 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.framer-text: Inter 24px/28.8px 500, #000000, ls -0.48px | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `tab-item-default.png`, `tab-item-hover.png`, `tab-item-focus-visible.png`.

#### demo-cta

Demo call button. The "Talk with <persona>" call control beside the demo card. Hovered and focused, never pressed: a press opens a session on Anam’s servers and asks for the microphone.

Page: home. Selector: `the "Talk with …" call button under the demo card`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 184.58 x 48 | = | = |
| Padding | 1px 18px | = | = |
| Gap | 8px | = | = |
| Border | 2px solid #ffffff @ 0.12 | = | = |
| Radius | 50px | = | = |
| Background | #ffffff @ 0.5 | #ffffff @ 0.6 | = |
| Box shadow | none | = | = |
| Backdrop filter | blur(24px) | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0.7 | = | = |
| Text node | span: Inter 15px/normal 500, #000000 @ 0.7, ls -0.3px | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #000000 @ 0.7 | = | = |
| Painted layers | button 184.6x48.0 bg #ffffff @ 0.5 border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px | button 184.6x48.0 bg #ffffff @ 0.6 border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px | button 184.6x48.0 bg #ffffff @ 0.5 border T:2px solid #ffffff @ 0.12 / R:2px solid #ffffff @ 0.12 / B:2px solid #ffffff @ 0.12 / L:2px solid #ffffff @ 0.12 r 50px outline 1px auto #005fcc offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `demo-cta-default.png`, `demo-cta-hover.png`, `demo-cta-focus-visible.png`.

### Feature sections

#### feature-card

Feature card. A metrics/feature block from the latency or platform sections (a claim, its value and a diagram or video).

Page: home. Selector: `a [data-framer-name=Feature/Metrics] block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 144 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: IBM Plex Mono 13px/15.6px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `feature-card-default.png`.

#### logo-cloud

Customer logo cloud. The customer logo strip that scrolls on a loop.

Page: home. Selector: `[data-framer-name="Logos Carousel"/Customers]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 82 |
| Padding | 0px 20px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 15px/21px 400, #000000 @ 0.5, ls -0.3px |
| Transition | none |
| How | at rest |

Crops: `logo-cloud-default.png`.

#### api-title

API page title.

Page: api. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 427 x 115.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/38.4px 500 |
| Letter spacing | -0.64px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `api-title-default.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 820 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-toggle

Billing period toggle. The monthly/annual period switch above the plan cards. A local toggle; the capture presses it once on the screenshot pass.

Page: pricing. Selector: `the billing period control`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 92.33 x 40 | = | = |
| Padding | 0px 18px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 50px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #ff6200 offset 3px |
| Font | Inter 15px/22.5px 500 | = | = |
| Letter spacing | -0.3px | = | = |
| Colour | #000000 @ 0.68 | #000000 | = |
| Transition | background-color, color, box-shadow 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up div.pricing-module__lP4odW__toggle bg #f5f5f5 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.pricing-module__lP4odW__toggleOption 92.3x40.0 r 50px outline 2px solid #ff6200 offset 3px |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-focus-visible.png`.

#### plan-card

Plan card. A pricing plan card: name, price, included usage and a call-to-action button.

Page: pricing. Selector: `a pricing plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 520 x 1133.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | h2.pricing-module__lP4odW__sectionTitle: Inter 32px/38.4px 500, #000000, ls -0.64px |
| Transition | none |
| Painted layers | a.pricing-module__lP4odW__button.pricing-module__lP4odW__buttonPrimary 94.1x44.0 bg #000000 r 50px; a.pricing-module__lP4odW__button.pricing-module__lP4odW__buttonSecondary 137.8x44.0 bg #f5f5f5 r 50px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA button. The call-to-action inside a plan card. Pressed is forced; a real press leads to checkout on lab.anam.ai.

Page: pricing. Selector: `a button inside a plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137.81 x 44 | = | = | 133.68 x 42.68 |
| Padding | 12px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #f5f5f5 | #e8e6e6 | = | #e8e6e6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ff6200 offset 3px | = |
| Font | Inter 15px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, transform 0.2s, 0.2s, 0.16s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pricing-module__lP4odW__button.pricing-module__lP4odW__buttonSecondary 137.8x44.0 bg #f5f5f5 r 50px | a.pricing-module__lP4odW__button.pricing-module__lP4odW__buttonSecondary 137.8x44.0 bg #e8e6e6 r 50px | a.pricing-module__lP4odW__button.pricing-module__lP4odW__buttonSecondary 137.8x44.0 bg #f5f5f5 r 50px outline 2px solid #ff6200 offset 3px | a.pricing-module__lP4odW__button.pricing-module__lP4odW__buttonSecondary 133.7x42.7 bg #e8e6e6 r 50px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-item

FAQ item. A question-and-answer row in the pricing FAQ.

Page: pricing. Selector: `an FAQ entry`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 728 x 57 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.08; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | summary: Inter 15px/22.5px 500, #000000, ls -0.32px |
| Transition | none |
| Painted layers | details.pricing-module__lP4odW__faqItem 728.0x57.0 border B:1px solid #000000 @ 0.08; summary::before 12pxx1.5px bg #ff6200; summary::after 12pxx1.5px bg #ff6200 |
| How | at rest |

Crops: `faq-item-default.png`.

### Demo request form

#### demo-title

Demo page title.

Page: get-demo. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 41.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 38px/41.8px 500 |
| Letter spacing | -0.76px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `demo-title-default.png`.

#### demo-form

Demo request form. The get-demo lead form: name, work email and a message box plus a submit. Every field was measured; nothing was filled or sent.

Page: get-demo. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 426 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | label.getDemo-module__Z7GltW__label: Inter 13.5px/20.25px 500, #0a0a0a |
| Transition | none |
| Painted layers | input.getDemo-module__Z7GltW__input 420.0x46.5 bg #f5f5f5 r 11px; input.getDemo-module__Z7GltW__input 420.0x46.5 bg #f5f5f5 r 11px; button.getDemo-module__Z7GltW__select.getDemo-module__Z7GltW__selectBtn 420.0x46.5 bg #f5f5f5 image url(data:…) r 11px; textarea.getDemo-module__Z7GltW__textarea 420.0x69.0 bg #f5f5f5 r 11px; input 153.0x21.0 bg #ffffff border T:2px inset #767676 / R:2px inset #767676 / B:2px inset #767676 / L:2px inset #767676; button.getDemo-module__Z7GltW__btn 420.0x52.5 bg #ff6200 r 50px |
| How | at rest |

Crops: `demo-form-default.png`.

#### form-label

Field label.

Page: get-demo. Selector: `a label inside the form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 20.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 13.5px/20.25px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `form-label-default.png`.

#### form-input

Text field. A text input in the demo form. Sample text was typed and deleted; nothing was submitted.

Page: get-demo. Selector: `the first text input in the form`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 420 x 46.5 | = | = |
| Padding | 12px 14px | = | = |
| Border | none | = | = |
| Radius | 11px | = | = |
| Background | #f5f5f5 | #efefef | #efefef |
| Box shadow | none | #ff6200 @ 0.4 0px 0px 0px 2px | #ff6200 @ 0.4 0px 0px 0px 2px |
| Outline | none | = | = |
| Font | Inter 15px/22.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | background, box-shadow 0.15s, 0.15s ease, ease delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #0a0a0a, opacity 1 | = | = |
| Painted layers | input.getDemo-module__Z7GltW__input 420.0x46.5 bg #f5f5f5 r 11px | input.getDemo-module__Z7GltW__input 420.0x46.5 bg #efefef r 11px shadow #ff6200 @ 0.4 0px 0px 0px 2px | input.getDemo-module__Z7GltW__input 420.0x46.5 bg #efefef r 11px shadow #ff6200 @ 0.4 0px 0px 0px 2px |
| How | at rest | clicked into the field | typed "a voice agent for a clinic", then deleted; nothing sent |

Crops: none.

#### form-input-box

Text field box.

Page: get-demo. Selector: `the input or its padded wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 72.75 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | label.getDemo-module__Z7GltW__label: Inter 13.5px/20.25px 500, #0a0a0a |
| Transition | none |
| Painted layers | input.getDemo-module__Z7GltW__input 420.0x46.5 bg #f5f5f5 r 11px |
| How | at rest |

Crops: `form-input-box-default.png`.

#### form-textarea

Text area. The message box. Clicked into, never filled.

Page: get-demo. Selector: `textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 420 x 69 | = |
| Padding | 12px 14px | = |
| Border | none | = |
| Radius | 11px | = |
| Background | #f5f5f5 | #efefef |
| Box shadow | none | #ff6200 @ 0.4 0px 0px 0px 2px |
| Outline | none | = |
| Font | Inter 15px/22.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | background, box-shadow 0.15s, 0.15s ease, ease delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #0a0a0a, opacity 1 | = |
| Painted layers | textarea.getDemo-module__Z7GltW__textarea 420.0x69.0 bg #f5f5f5 r 11px | textarea.getDemo-module__Z7GltW__textarea 420.0x69.0 bg #efefef r 11px shadow #ff6200 @ 0.4 0px 0px 0px 2px |
| How | at rest | clicked into the field |

Crops: none.

#### form-submit

Submit button. The form’s submit. Measured and hovered, never pressed: a press sends the lead form.

Page: get-demo. Selector: `the submit control in the form`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 420 x 52.5 | = | = |
| Padding | 15px 24px | = | = |
| Border | none | = | = |
| Radius | 50px | = | = |
| Background | #ff6200 | #ff8133 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | Inter 15px/22.5px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | transform, opacity, background 0.04s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.getDemo-module__Z7GltW__btn 420.0x52.5 bg #ff6200 r 50px | button.getDemo-module__Z7GltW__btn 420.0x52.5 bg #ff8133 r 50px | button.getDemo-module__Z7GltW__btn 420.0x52.5 bg #ff6200 r 50px outline 1px auto #005fcc offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `form-submit-default.png`, `form-submit-hover.png`, `form-submit-focus-visible.png`.

### Cards and lists

#### avatar-card-title

Avatar card title.

Page: interactive-avatars. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `avatar-card-title-default.png`.

#### about-card-title

About card title.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 451.88 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `about-card-title-default.png`.

#### research-card-title

Research entry title.

Page: research. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `research-card-title-default.png`.

#### case-card-title

Case study card title.

Page: case-studies. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `case-card-title-default.png`.

#### post-card-title

Blog post card title.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 208.53 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/38.4px 500 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `post-card-title-default.png`.

#### changelog-entry-title

Changelog entry title.

Page: changelog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 535 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `changelog-entry-title-default.png`.

#### tool-card-title

Tool card title.

Page: tools. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 417.59 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `tool-card-title-default.png`.

#### avatar-card

Avatar card. A card in the avatar gallery: a face, its style tag and name.

Page: interactive-avatars. Selector: `the first card on /interactive-avatars`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 222 x 128.91 | = | = |
| Padding | 0px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.framer-text: Inter 13px/16.9px 500, #000000 @ 0.5, ls -0.26px | = | = |
| Transition | none | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.framer-text 51.0x24.0 outline 1px auto #005fcc offset 1px |

Crops: `avatar-card-default.png`, `avatar-card-hover.png`, `avatar-card-focus-visible.png`.

#### about-card

About card. A card on the team/company page.

Page: about. Selector: `the first card on /about`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 222 x 128.91 | = | = |
| Padding | 0px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.framer-text: Inter 13px/16.9px 500, #000000 @ 0.5, ls -0.26px | = | = |
| Transition | none | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.framer-text 51.0x24.0 outline 1px auto #005fcc offset 1px |

Crops: `about-card-default.png`, `about-card-hover.png`, `about-card-focus-visible.png`.

#### research-card

Research entry. A paper or model entry on the research page.

Page: research. Selector: `the first card on /research`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 222 x 128.91 | = | = |
| Padding | 0px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.framer-text: Inter 13px/16.9px 500, #000000 @ 0.5, ls -0.26px | = | = |
| Transition | none | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.framer-text 51.0x24.0 outline 1px auto #005fcc offset 1px |

Crops: `research-card-default.png`, `research-card-hover.png`, `research-card-focus-visible.png`.

#### case-card

Case study card. A customer story card.

Page: case-studies. Selector: `the first card on /case-studies`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 222 x 128.91 | = | = |
| Padding | 0px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.framer-text: Inter 13px/16.9px 500, #000000 @ 0.5, ls -0.26px | = | = |
| Transition | none | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.framer-text 51.0x24.0 outline 1px auto #005fcc offset 1px |

Crops: `case-card-default.png`, `case-card-hover.png`, `case-card-focus-visible.png`.

#### post-card

Blog post card. A post card in the blog index.

Page: blog. Selector: `the first card on /blog`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 222 x 128.91 | = | = |
| Padding | 0px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.framer-text: Inter 13px/16.9px 500, #000000 @ 0.5, ls -0.26px | = | = |
| Transition | none | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.framer-text 51.0x24.0 outline 1px auto #005fcc offset 1px |

Crops: `post-card-default.png`, `post-card-hover.png`, `post-card-focus-visible.png`.

#### changelog-entry

Changelog entry. A release entry on the changelog page.

Page: changelog. Selector: `the first card on /changelog`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 222 x 128.91 | = | = |
| Padding | 0px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.framer-text: Inter 13px/16.9px 500, #000000 @ 0.5, ls -0.26px | = | = |
| Transition | none | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.framer-text 51.0x24.0 outline 1px auto #005fcc offset 1px |

Crops: `changelog-entry-default.png`, `changelog-entry-hover.png`, `changelog-entry-focus-visible.png`.

#### tool-card

Tool card. A card in the tools index.

Page: tools. Selector: `the first card on /tools`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 598 x 506.5 | = | = |
| Padding | 30px | = | = |
| Border | none | = | = |
| Radius | 32px | = | = |
| Background | #fafafa | #f5f5f5 | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #ff6200 offset 4px |
| Font | Inter 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | strong: Inter 10px/10px 600, #000000, ls 0.1px | = | = |
| Transition | background-color, transform 0.4s, 0.4s cubic-bezier(0.44, 0, 0.56, 1), cubic-bezier(0.44, 0, 0.56, 1) delay 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.KUizFa_toolCard.KUizFa_featuredCard 598.0x506.5 bg #fafafa r 32px; div.KUizFa_previewWrap 538.0x303.5 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 12px; div.KUizFa_preview.KUizFa_interviewPreview 536.0x301.5 bg #ffffff; div.KUizFa_previewHeader 536.0x43.0 bg #ffffff border B:1px solid #000000 @ 0.08; div.KUizFa_interviewPortrait 230.5x258.5 bg #e8e6e6; span 210.5x22.0 bg #ffffff @ 0.93 r 50px | a.KUizFa_toolCard.KUizFa_featuredCard 598.0x506.5 bg #f5f5f5 r 32px; div.KUizFa_previewWrap 538.0x303.5 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 12px; div.KUizFa_preview.KUizFa_interviewPreview 540.3x303.9 bg #ffffff; div.KUizFa_previewHeader 540.3x43.3 bg #ffffff border B:1px solid #000000 @ 0.08; div.KUizFa_interviewPortrait 232.3x260.6 bg #e8e6e6; span 212.2x22.2 bg #ffffff @ 0.93 r 50px | a.KUizFa_toolCard.KUizFa_featuredCard 598.0x506.5 bg #fafafa r 32px outline 2px solid #ff6200 offset 4px; div.KUizFa_previewWrap 538.0x303.5 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 12px; div.KUizFa_preview.KUizFa_interviewPreview 536.0x301.5 bg #ffffff; div.KUizFa_previewHeader 536.0x43.0 bg #ffffff border B:1px solid #000000 @ 0.08; div.KUizFa_interviewPortrait 230.5x258.5 bg #e8e6e6; span 210.5x22.0 bg #ffffff @ 0.93 r 50px |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Transform | - | matrix(1, 0, 0, 1, 0, -2) | = |

Crops: `tool-card-default.png`, `tool-card-hover.png`, `tool-card-focus-visible.png`.

### Docs (Mintlify)

#### docs-sidebar

Docs sidebar. The left navigation tree on the Mintlify docs (section groups, page links, POST/GET method badges on the API reference).

Page: docs-api. Selector: `#sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 788 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #77726f |
| Text node | span: Inter 14px/24px 600, #1e1916 |
| Transition | none |
| Painted layers | div.sticky.top-0 256.0x32.0 image linear-gradient(in oklab, #ffffff 0%, #000000 @ 0 100%); a.group.flex 256.0x36.0 bg #ff6200 @ 0.1 r 12px; span.px-1.py-0.5 32.1x15.0 bg #60a5fa @ 0.2 r 6px; span.px-1.py-0.5 25.8x15.0 bg #4ade80 @ 0.2 r 6px; span.px-1.py-0.5 25.8x15.0 bg #4ade80 @ 0.2 r 6px; span.px-1.py-0.5 25.8x15.0 bg #4ade80 @ 0.2 r 6px |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-nav-link

Sidebar link. A page link inside a sidebar group. Measured, never followed.

Page: docs-api. Selector: `a link inside the sidebar`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 256 x 24 | = | - |
| Padding | 0px 0px 0px 16px | = | - |
| Gap | 10px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Inter 14px/24px 600 | = | - |
| Letter spacing | normal | = | - |
| Colour | #1e1916 | = | - |
| Text node | span: Inter 14px/24px 600, #1e1916 | = | - |
| Transition | none | = | - |
| How | at rest | mouse hover | - |
| Error | - | = | keyboard focus could not be moved to the element |

Crops: `docs-nav-link-default.png`, `docs-nav-link-hover.png`.

#### docs-nav-active

Sidebar link, current page. The link for the open page, in its selected style.

Page: docs-api. Selector: `[aria-current=page] in the sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/24px 400 |
| Letter spacing | normal |
| Colour | #77726f |
| Text node | span.min-w-0.max-w-full: Inter 14px/24px 400, #ff6200 |
| Transition | none |
| Painted layers | a.group.flex 256.0x36.0 bg #ff6200 @ 0.1 r 12px |
| How | at rest |

Crops: `docs-nav-active-default.png`.

#### docs-topnav-link

Top nav tab. A section tab in the docs top bar (Documentation / API Reference).

Page: docs-api. Selector: `a top-nav link`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 63.53 x 48 | = | = |
| Padding | 0px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #ff6200 offset 1px |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #57524f | #2d2825 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | div.absolute.bottom-0 63.5x1.5 bg #e6e1de | a.link.nav-tabs-item 63.5x48.0 outline 1px auto #ff6200 offset 1px |

Crops: `docs-topnav-link-default.png`, `docs-topnav-link-hover.png`, `docs-topnav-link-focus-visible.png`.

#### docs-search-btn

Search button. The "Search… ⌘K" pill in the docs bar. Pressed is forced; a real press opens the search dialog.

Page: docs-api. Selector: `the Search button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 269.56 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #ff6200 offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #77726f | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #77726f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #46413e, fill #000000 | 16 x 16, colour #2d2825, fill #000000 | = | 16 x 16, colour #2d2825, fill #000000 |
| Painted layers | button.group/search.flex 269.6x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 269.6x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 269.6x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #ff6200 offset 0px | button.group/search.flex 269.6x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-btn-default.png`, `docs-search-btn-hover.png`, `docs-search-btn-focus-visible.png`, `docs-search-btn-pressed.png`.

#### docs-assistant-btn

Ask Assistant button. Opens the AI assistant panel (⌘I). Pressed is forced; the panel was opened by keyboard for its own entry.

Page: docs-api. Selector: `the Ask Assistant button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 157.77 x 36 | = | = | = |
| Padding | 0px 14px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #ff6200 offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #77726f | = | = | = |
| Text node | span.text-sm.text-gray-500: Inter 14px/20px 400, #77726f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #46413e, fill #000000 | 16 x 16, colour #2d2825, fill #000000 | = | 16 x 16, colour #2d2825, fill #000000 |
| Painted layers | button.group/ai.flex-none 157.8x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/ai.flex-none 157.8x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/ai.flex-none 157.8x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #ff6200 offset 0px | button.group/ai.flex-none 157.8x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #57524f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-assistant-btn-default.png`, `docs-assistant-btn-hover.png`, `docs-assistant-btn-focus-visible.png`, `docs-assistant-btn-pressed.png`.

#### docs-theme-btn

Theme menu button. The "Change theme preference" menu trigger. A local toggle; the dark run pressed it once.

Page: docs-api. Selector: `#theme-preference-menu-trigger`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = |
| Padding | 8px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #ff6200 offset 0px |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #110d0a @ 0.5 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 0 x 0, colour #77726f, fill #000000 | 0 x 0, colour #46413e, fill #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.group.rounded-lg 32.0x32.0 r 8px outline 1px auto #ff6200 offset 0px |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`.

#### docs-toc

On-this-page rail. The sticky right-hand table of contents.

Page: docs-api. Selector: `#content-side-layout`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304 x 748 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #77726f |
| Text node | span: Inter 14px/24px 500, #46413e |
| Transition | none |
| Icon | 12 x 12, colour #46413e, fill #000000 |
| How | at rest |

Crops: `docs-toc-default.png`.

#### docs-toc-link

TOC link.

Page: docs-api. Selector: `a link inside the TOC rail`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 264 x 32 | = | - |
| Padding | 0px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Inter 14px/24px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #57524f | = | - |
| Text node | a.text-primary: Inter 14px/24px 400, #ff6200 | = | - |
| Transition | none | = | - |
| How | at rest | mouse hover | - |
| Error | - | = | keyboard focus could not be moved to the element |

Crops: `docs-toc-link-default.png`, `docs-toc-link-hover.png`.

#### docs-h1

Docs page title. "Anam Documentation" in the docs display type.

Page: docs-overview. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360.47 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #1e1916 |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-body

Body text.

Page: docs-overview. Selector: `a main paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 688.81 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28px 400 |
| Letter spacing | normal |
| Colour | #46413e |
| Transition | none |
| How | at rest |

Crops: none.

#### docs-card

Docs link card. A card linking to another docs page (the "Learn" cards). Measured, never followed.

Page: docs-overview. Selector: `.card in main`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 218.94 x 230 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #110d0a @ 0.1 | 1px solid #ff6200 | = | 1px solid #ff6200 |
| Radius | 16px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 1px auto #ff6200 offset 0px | = |
| Font | Inter 16px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #46413e | = | = | = |
| Text node | h2.not-prose.font-semibold: Inter 16px/24px 600, #2d2825 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #a6a19e, fill #000000 | 0 x 0, colour #ff6200, fill #000000 | = | 0 x 0, colour #ff6200, fill #000000 |
| Painted layers | div.card.block 218.9x230.0 bg #ffffff border T:1px solid #110d0a @ 0.1 / R:1px solid #110d0a @ 0.1 / B:1px solid #110d0a @ 0.1 / L:1px solid #110d0a @ 0.1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:1px solid #ff6200; svg.size-6.m-0! 24.0x24.0 bg #ff6200 | div.card.block 218.9x230.0 bg #ffffff border T:1px solid #ff6200 / R:1px solid #ff6200 / B:1px solid #ff6200 / L:1px solid #ff6200 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:2px solid #ff6200; svg.size-6.m-0! 24.0x24.0 bg #ff6200 | div.card.block 218.9x230.0 bg #ffffff border T:1px solid #110d0a @ 0.1 / R:1px solid #110d0a @ 0.1 / B:1px solid #110d0a @ 0.1 / L:1px solid #110d0a @ 0.1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #ff6200 offset 0px; a 0.0x0.0 border B:1px solid #ff6200; svg.size-6.m-0! 24.0x24.0 bg #ff6200 | div.card.block 218.9x230.0 bg #ffffff border T:1px solid #ff6200 / R:1px solid #ff6200 / B:1px solid #ff6200 / L:1px solid #ff6200 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:1px solid #ff6200; svg.size-6.m-0! 24.0x24.0 bg #ff6200 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-card-default.png`, `docs-card-hover.png`, `docs-card-focus-visible.png`, `docs-card-pressed.png`.

#### docs-breadcrumb

Breadcrumb. The section/page breadcrumb over the title.

Page: docs-overview. Selector: `the breadcrumb row`. States: .

Not found on the page at capture time.

#### docs-api-title

API reference title. "Anam REST API".

Page: docs-api. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 259.33 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #1e1916 |
| Transition | none |
| How | at rest |

Crops: `docs-api-title-default.png`.

#### docs-code-block

Code block. A fenced code sample (the base URL block, a curl example), mono-set over a tinted panel.

Page: docs-api. Selector: `main pre`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 654.81 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Paper Mono 14px/24px 400 |
| Letter spacing | normal |
| Colour | #1f2328 |
| Text node | span: Paper Mono 14px/24px 400, #1f2328 |
| Transition | none |
| Painted layers | pre.shiki.shiki-themes 654.8x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; code 654.8x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 186.7x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 186.7x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 0.0x0.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 0.0x0.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.font-mono.whitespace-pre shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #110d0a; 2 up div.min-w-full!.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #110d0a; 3 up div.size-full.py-3.5 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #110d0a |
| How | at rest |

Crops: `docs-code-block-default.png`.

#### docs-inline-code

Inline code.

Page: docs-api. Selector: `a code span in body text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126.3 x 20 |
| Padding | 2px 8px |
| Border | none |
| Radius | 6px |
| Background | #f5f1ee @ 0.5 |
| Box shadow | none |
| Outline | none |
| Font | Paper Mono 14px/21px 500 |
| Letter spacing | normal |
| Colour | oklch(0.21 0.034 264.665) |
| Transition | none |
| Painted layers | code 126.3x20.0 bg #f5f1ee @ 0.5 r 6px |
| How | at rest |

Crops: none.

#### docs-method-badge

Method badge. The POST/GET verb chip beside an API endpoint in the sidebar.

Page: docs-api. Selector: `a method label in the sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/24px 400 |
| Letter spacing | normal |
| Colour | #46413e |
| Text node | span.px-1.py-0.5: Inter 8.8px/11px 700, #1d4ed8 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.px-1.py-0.5 32.1x15.0 bg #60a5fa @ 0.2 r 6px |
| How | at rest |

Crops: none.

#### docs-dark-main

Docs page, dark. The content column in the dark theme.

Page: docs-dark. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1088 x 1936.55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #a6a19e |
| Text node | span: Inter 14px/24px 500, #d5d1ce |
| Transition | none |
| Icon | 12 x 12, colour #d5d1ce, fill #000000 |
| Painted layers | button.rounded-l-xl.px-3 140.0x34.0 bg #000000 border T:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 12px 0px 0px 12px; button.group.overflow-hidden 34.0x34.0 bg #000000 border T:1px solid #ffffff @ 0.07 / R:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 0px 12px 12px 0px; button.rounded-l-xl.px-3 0.0x0.0 bg #000000 border T:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 12px 0px 0px 12px; button.group.overflow-hidden 0.0x0.0 bg #000000 border T:1px solid #ffffff @ 0.07 / R:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 0px 12px 12px 0px; button.inline-flex.shrink-0 2.0x2.0 bg #171717 @ 0.45 border T:1px solid #ffffff @ 0.25 / R:1px solid #ffffff @ 0.25 / B:1px solid #ffffff @ 0.25 / L:1px solid #ffffff @ 0.25 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 0px 0px 0px 0.5px, #000000 @ 0.45 0px 0.5px 1px 0px, #000000 @ 0.35 0px 1px 2px 0px, #ffffff @ 0.14 0px 0.5px 0px 0px inset; div.size-6.rounded-md 24.0x24.0 bg #000000 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #46413e @ 0.25 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `docs-dark-main-default.png`.

#### docs-dark-sidebar

Sidebar, dark.

Page: docs-dark. Selector: `#sidebar in dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 788 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #a6a19e |
| Text node | span: Inter 14px/24px 600, #e6e1de |
| Transition | none |
| Icon | 16 x 16, colour #ff6200, fill #000000 |
| Painted layers | div.sticky.top-0 256.0x32.0 image linear-gradient(in oklab, #000000 0%, #000000 @ 0 100%); a.group.flex 256.0x36.0 bg #ff6200 @ 0.1 r 12px; svg.size-4.bg-primary 16.0x16.0 bg #ff6200; svg.size-4.bg-gray-400 16.0x16.0 bg #77726f; svg.size-4.bg-gray-400 16.0x16.0 bg #77726f; svg.size-4.bg-gray-400 16.0x16.0 bg #77726f |
| How | at rest |

Crops: `docs-dark-sidebar-default.png`.

#### docs-dark-h1

Docs title, dark.

Page: docs-dark. Selector: `main h1 in dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360.47 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #e6e1de |
| Transition | none |
| How | at rest |

Crops: `docs-dark-h1-default.png`.

#### docs-prev-next

Prev/next link. The page-footer pagination link. Measured, never followed.

Page: docs-api. Selector: `a pagination link`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 154.95 x 20 | = | = |
| Padding | 0px | = | = |
| Gap | 12px | = | = |
| Border | none | = | = |
| Radius | 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #ff6200 offset 2px |
| Font | Inter 14px/20px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #46413e | = | = |
| Text node | div.truncate: Inter 14px/20px 600, #46413e | div.truncate: Inter 14px/20px 600, #1e1916 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 3 x 6, colour #46413e, fill #000000 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.group.flex 155.0x20.0 r 2px outline 2px solid #ff6200 offset 2px |

Crops: `docs-prev-next-default.png`, `docs-prev-next-hover.png`, `docs-prev-next-focus-visible.png`.

#### docs-dark-card

Docs card, dark.

Page: docs-dark. Selector: `a card link in dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 218.94 x 230 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.1 |
| Radius | 16px |
| Background | #000000 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | normal |
| Colour | #a6a19e |
| Text node | h2.not-prose.font-semibold: Inter 16px/24px 600, #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #77726f, fill #000000 |
| Painted layers | div.card.block 218.9x230.0 bg #000000 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:1px solid #ff6200; svg.size-6.m-0! 24.0x24.0 bg #ff6200 |
| How | at rest |

Crops: `docs-dark-card-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile nav bar. The top bar at 390 wide: logo, Sign in and the menu button.

Page: home. Selector: `the mobile top bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 15px/18px 500, #000000 |
| Transition | none |
| Painted layers | div.framer-6RbLx.framer-D3hzf 390.0x75.0 bg #ffffff @ 0; div.framer-WP6gO 60.0x22.0 bg #000000; a.framer-Ey2WY.framer-v-1amifyt 96.6x34.0 bg #f5f5f5 r 50px; div 20.0x2.0 bg #000000 r 10px; div 20.0x2.0 bg #000000 r 10px |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-hero-title

Hero title (mobile).

Page: home. Selector: `h1 at 390 wide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/44px 500 |
| Letter spacing | -0.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-persona-chip

Persona chip (mobile).

Page: home. Selector: `a persona card at 390 wide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 340 x 451 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 2px/2.4px 400, #000000 |
| Transition | transform 0.3s cubic-bezier(0.12, 0.23, 0.5, 1) |
| Transform | matrix(1, 0, 0, 1, -170, -225.5) |
| Cursor | pointer |
| Painted layers | div 340.0x403.0 r 32px shadow #000000 @ 0.01 0px 124px 50px 0px, #000000 @ 0.05 0px 70px 42px 0px, #000000 @ 0.09 0px 31px 31px 0px, #000000 @ 0.1 0px 8px 17px 0px |
| How | at rest |

Crops: `m-persona-chip-default.png`.

#### m-docs-topbar

Docs top bar (mobile).

Page: docs-overview. Selector: `the docs top bar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #77726f |
| Text node | span: Inter 14px/24px 400, #77726f |
| Transition | none |
| Icon | 0 x 0, colour #46413e, fill #000000 |
| Painted layers | div.absolute.w-full 390.0x120.0 bg #ffffff border B:1px solid #77726f @ 0.05; div.h-full.relative 358.0x64.0 border B:1px solid #77726f @ 0.05; button.group/search.flex 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; button.group/ai.flex-none 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a6a19e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.absolute.inset-0 0.0x0.0 bg #ff6200 r 12px; svg.h-4.w-4 16.0x16.0 bg #77726f |
| How | at rest |

Crops: `m-docs-topbar-default.png`.

## Transitions declared in the readable stylesheets

anam.ai is a Framer site whose stylesheets are served cross-origin and unreadable to the CSSOM, so this list holds only what the CSSOM could read on each page (inline styles and same-origin sheets); the per-state Transition rows above are computed values and cover the real rules.

- docs-overview: `background-color 160ms cubic-bezier(0.16, 1, 0.3, 1), border-color 160ms`, `background-color 200ms cubic-bezier(0.16, 1, 0.3, 1)`, `transform 220ms cubic-bezier(0.16, 1, 0.3, 1)`, `none`, `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`

- home: `background-color 160ms cubic-bezier(0.16, 1, 0.3, 1), border-color 160ms`, `background-color 200ms cubic-bezier(0.16, 1, 0.3, 1)`, `transform 220ms cubic-bezier(0.16, 1, 0.3, 1)`, `none`, `color 0.2s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`
