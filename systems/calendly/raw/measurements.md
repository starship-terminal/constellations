# Component measurements

Computed styles read from calendly.com on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's two surfaces: the Astro/Tailwind marketing pages (light, with .dark islands) and the invitee booking app on /calendly-demo. The OneTrust/Ketch consent banners and the Intercom launcher were hidden (never answered). The tables are written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky marketing header: wordmark, the Product/Solutions/Resources dropdowns, Pricing, Talk to sales, Log In and the dark Get-started pill.

Page: home. Selector: `header#site-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfbf8 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.group.inline-flex: Geist 14px/19.6px 500, #071a31 |
| Transition | box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 32 x 32, colour #000000 |
| Painted layers | header.w-full.bg-surface-bg-primary 1440.0x68.0 bg #fcfbf8; a.inline-flex.items-center 94.3x48.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px; a.inline-flex.items-center 73.3x48.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 16px; a.inline-flex.items-center 158.7x48.0 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px; a.inline-flex.items-center 0.0x0.0 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Calendly wordmark anchor.

Page: home. Selector: `header a:first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 156.28 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 32 x 32, colour #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Product button that opens the header mega-menu; toggled, never followed.

Page: home. Selector: `header button "Product"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.66 x 35.59 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #071a31 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.group.relative bg #f5f3ee | 1 up div.group.relative bg #f5f3ee outline 2px solid #6bb1ff | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Pricing header link.

Page: home. Selector: `header nav a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61.72 x 35.59 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.group.relative bg #f5f3ee | 1 up div.group.relative outline 2px solid #6bb1ff | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-sales

Sales link. The Talk-to-sales header action; measured never followed.

Page: home. Selector: `header a "Talk to sales"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94.34 x 48 | = | = | = |
| Padding | 8px 4px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #6bb1ff | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | #5f6d77 | = | #1e5ea7 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 94.3x48.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px | = | a.inline-flex.items-center 94.3x48.0 border T:2px solid #6bb1ff / R:2px solid #6bb1ff / B:2px solid #6bb1ff / L:2px solid #6bb1ff r 16px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-sales-default.png`, `nav-sales-hover.png`, `nav-sales-focus-visible.png`, `nav-sales-pressed.png`.

#### nav-login

Login link. The Log-In header action (outlined pill); measured never followed.

Page: home. Selector: `header a "Log In"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.33 x 48 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #071a31 | = | 1px solid #000000 @ 0 | 1px solid #0e396a |
| Radius | 16px | = | = | = |
| Background | transparent | #071a31 | = | #0e396a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6bb1ff offset -2px | = |
| Font | Geist 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | #fcfbf8 | = | #fcfbf8 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 73.3x48.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 16px | a.inline-flex.items-center 73.3x48.0 bg #071a31 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 16px | a.inline-flex.items-center 73.3x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px outline 2px solid #6bb1ff offset -2px | a.inline-flex.items-center 73.3x48.0 bg #0e396a border T:1px solid #0e396a / R:1px solid #0e396a / B:1px solid #0e396a / L:1px solid #0e396a r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The Get-started-for-free dark pill; measured never followed.

Page: home. Selector: `header a "Get started for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 158.73 x 48 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #6bb1ff | = |
| Radius | 16px | = | = | = |
| Background | #071a31 | #0e396a | = | #1e5ea7 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfbf8 | = | = | = |
| Text node | span.hidden.mbl:inline: Geist 14px/19.6px 400, #fcfbf8 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 158.7x48.0 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px | a.inline-flex.items-center 158.7x48.0 bg #0e396a border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px | a.inline-flex.items-center 158.7x48.0 bg #071a31 border T:2px solid #6bb1ff / R:2px solid #6bb1ff / B:2px solid #6bb1ff / L:2px solid #6bb1ff r 16px | a.inline-flex.items-center 158.7x48.0 bg #1e5ea7 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav dropdown. The Product mega-menu panel, opened by its own trigger.

Page: home. Selector: `header product panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304 x 398.5 |
| Padding | 32px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.mb-lg-fixed.block: Geist 12px/12px 500, #5f6d77, ls 1px |
| Transition | none |
| Icon | 36 x 36, colour #000000 |
| Painted layers | div.min-w-0.bg-white 304.0x398.5 bg #ffffff; span.w-fit.inline-flex 42.4x20.8 bg #071a31 @ 0.05 r 8px |
| Ancestor paint | 2 up div.Sp-BGW_dropdownPanel.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #5f6d77 @ 0.04 0px 4px 5px 0px, #5f6d77 @ 0.04 0px 10px 15px 0px, #5f6d77 @ 0.1 0px 40px 50px 0px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A feature link inside the opened mega-menu.

Page: home. Selector: `header menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 240 x 56.5 | = | = | - |
| Padding | 8px | = | = | - |
| Gap | 8px | = | = | - |
| Border | none | = | = | - |
| Radius | 24px | = | = | - |
| Background | transparent | #f5f3ee | = | - |
| Box shadow | none | = | = | - |
| Outline | none | = | 2px solid #6bb1ff offset 0px | - |
| Font | Geist 16px/16px 400 | = | = | - |
| Letter spacing | normal | = | = | - |
| Colour | #000000 | = | = | - |
| Text node | span.min-w-0.truncate: Geist 16px/22px 500, #071a31 | = | = | - |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | - |
| Cursor | pointer | = | = | - |
| Icon | 36 x 36, colour #000000 | = | = | - |
| How | at rest | mouse hover | Shift+Tab, Tab | - |
| Painted layers | - | a.keyboard-focus-before.group 240.0x56.5 bg #f5f3ee r 24px | a.keyboard-focus-before.group 240.0x56.5 r 24px outline 2px solid #6bb1ff offset 0px | = |
| Error | - | = | = | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('header a').filter({ hasText: /Scheduling/Callie/Notetaker/Routing/Payments/i }).filter({ visible: true }).first().filter({ |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`.

### Home hero

#### hero-title

Hero headline. The 72px Calendly-Sans display headline inside the dark hero island.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 158.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Calendly Sans 72px/79.2px 500 |
| Letter spacing | -2px |
| Colour | #fcfbf8 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero copy. The 18px lede under the headline, Geist on the dark island.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 50.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 18px/25.2px 400 |
| Letter spacing | normal |
| Colour | #fcfbf8 |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### signup-google

Google signup button. The light Sign-up-with-Google pill in the dark hero; measured never followed.

Page: home. Selector: `button "Sign up with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224.03 x 50 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #fcfbf8 | 1px solid #c1defe | 1px solid #6bb1ff | 1px solid #6bb1ff |
| Radius | 20px | = | = | = |
| Background | #fcfbf8 | #c1defe | = | #6bb1ff |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 16px/22.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 224.0x50.0 bg #fcfbf8 border T:1px solid #fcfbf8 / R:1px solid #fcfbf8 / B:1px solid #fcfbf8 / L:1px solid #fcfbf8 r 20px | button.inline-flex.items-center 224.0x50.0 bg #c1defe border T:1px solid #c1defe / R:1px solid #c1defe / B:1px solid #c1defe / L:1px solid #c1defe r 20px | button.inline-flex.items-center 224.0x50.0 bg #fcfbf8 border T:1px solid #6bb1ff / R:1px solid #6bb1ff / B:1px solid #6bb1ff / L:1px solid #6bb1ff r 20px | button.inline-flex.items-center 224.0x50.0 bg #6bb1ff border T:1px solid #6bb1ff / R:1px solid #6bb1ff / B:1px solid #6bb1ff / L:1px solid #6bb1ff r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-email

Email signup link. The underlined Sign-up-with-email link under the OAuth buttons; measured never followed.

Page: home. Selector: `"Sign up with email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.77 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6bb1ff offset 0px | = |
| Font | Geist 12px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfbf8 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |
| Painted layers | - | = | a.keyboard-focus-before.underline 100.8x16.0 r 8px outline 2px solid #6bb1ff offset 0px | = |

Crops: `signup-email-default.png`, `signup-email-hover.png`, `signup-email-focus-visible.png`, `signup-email-pressed.png`.

#### hero-card

Hero card. The painted island behind the hero (the .dark section card).

Page: home. Selector: `first painted ancestor of h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 920 x 408.84 |
| Padding | 48px |
| Border | none |
| Radius | 48px |
| Background | #fcfbf8 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.font-calendly-sans.font-medium: Calendly Sans 16px/16px 500, #071a31 |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | div.relative.z-10 920.0x408.8 bg #fcfbf8 r 48px; a.inline-flex.items-center 100.6x38.1 border B:1px solid #071a31; div.aspect-[278/172.314].w-full 448.0x289.1 bg #c3dffe r 20px; span.w-fit.inline-flex 42.4x24.8 bg #071a31 @ 0.05 r 8px; a.inline-flex.items-center 100.6x38.1 border B:1px solid #071a31; div.aspect-[278/172.314].w-full 448.0x289.1 bg #c3dffe r 20px |
| How | at rest |

Crops: `hero-card-default.png`.

### Home

#### h2-serif

Section heading (serif). A 48px Wulkan-Text section heading in the light sections.

Page: home. Selector: `h2.font-wulkan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 118.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 36px/39.6px 500 |
| Letter spacing | -1px |
| Colour | #071a31 |
| Transition | none |
| How | at rest |

Crops: `h2-serif-default.png`.

#### badge

Badge. A "Beta"/"New" chip (rounded-ui-xxs).

Page: home. Selector: `badge chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.38 x 24.8 | = | - | = |
| Padding | 4px 8px | = | - | = |
| Gap | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | #071a31 @ 0.05 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Geist 12px/16.8px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #3d464e | = | - | = |
| Transition | none | = | - | = |
| Painted layers | span.w-fit.inline-flex 42.4x24.8 bg #071a31 @ 0.05 r 8px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `badge-default.png`, `badge-hover.png`, `badge-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The pricing page display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 105.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Calendly Sans 48px/52.8px 500 |
| Letter spacing | -2px |
| Colour | #071a31 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### billing-radio

Billing toggle. A Billed-monthly/Billed-yearly radio label; the yearly option was toggled for the screenshot state, never checked out.

Page: pricing. Selector: `label "Billed yearly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108.27 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.type-body-sm.font-medium!: Geist 14px/19.6px 500, #071a31 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.flex.size-5 20.0x20.0 bg #ffffff border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 3.35544e+07px; span.size-3.rounded-full 12.0x12.0 bg #071a31 r 3.35544e+07px | = | span.flex.size-5 20.0x20.0 bg #ffffff border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px; span.size-3.rounded-full 12.0x12.0 bg #071a31 r 3.35544e+07px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-radio-default.png`, `billing-radio-hover.png`, `billing-radio-focus-visible.png`, `billing-radio-pressed.png`.

#### plan-name

Plan name. A plan card's name (h3, Calendly Sans).

Page: pricing. Selector: `h3 plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 66.78 x 39.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Calendly Sans 36px/39.6px 500 |
| Letter spacing | -1px |
| Colour | #071a31 |
| Transition | none |
| Ancestor paint | 3 up div.relative.z-1 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #5f6d77 @ 0.04 0px 4px 5px 0px, #5f6d77 @ 0.03 0px 8px 15px 0px, #5f6d77 @ 0.06 0px 15px 30px 0px |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card's price figure.

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 67.97 x 52.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Wulkan Text 48px/52.8px 500 |
| Letter spacing | -2px |
| Colour | #071a31 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's Get-started action; measured never followed.

Page: pricing. Selector: `button "Get started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 218 x 50 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #071a31 | = | 1px solid #000000 @ 0 | 1px solid #0e396a |
| Radius | 20px | = | = | = |
| Background | transparent | #071a31 | = | #0e396a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6bb1ff offset -2px | = |
| Font | Geist 16px/22.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | #fcfbf8 | = | #fcfbf8 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #071a31 | 24 x 24, colour #fcfbf8 | = | 24 x 24, colour #fcfbf8 |
| Painted layers | button.inline-flex.items-center 218.0x50.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 20px | button.inline-flex.items-center 218.0x50.0 bg #071a31 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 20px | button.inline-flex.items-center 218.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px outline 2px solid #6bb1ff offset -2px | button.inline-flex.items-center 218.0x50.0 bg #0e396a border T:1px solid #0e396a / R:1px solid #0e396a / B:1px solid #0e396a / L:1px solid #0e396a r 20px |
| Ancestor paint | 2 up div.relative.z-1 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #5f6d77 @ 0.04 0px 4px 5px 0px, #5f6d77 @ 0.03 0px 8px 15px 0px, #5f6d77 @ 0.06 0px 15px 30px 0px; 3 up div.w-full.min-w-0 bg #fcfbf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #5f6d77 @ 0.04 0px 4px 5px 0px, #5f6d77 @ 0.03 0px 8px 15px 0px, #5f6d77 @ 0.08 0px 30px 50px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-card

Plan card. A pricing plan card (the painted ancestor of the plan name).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 266 x 300.98 |
| Padding | 24px |
| Gap | 48px |
| Border | none |
| Radius | 40px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #5f6d77 @ 0.04 0px 4px 5px 0px, #5f6d77 @ 0.03 0px 8px 15px 0px, #5f6d77 @ 0.06 0px 15px 30px 0px |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.font-calendly-sans.type-h3-fixed: Calendly Sans 36px/39.6px 500, #071a31, ls -1px |
| Transition | none |
| Icon | 24 x 24, colour #071a31 |
| Painted layers | div.relative.z-1 266.0x301.0 bg #ffffff r 40px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #5f6d77 @ 0.04 0px 4px 5px 0px, #5f6d77 @ 0.03 0px 8px 15px 0px, #5f6d77 @ 0.06 0px 15px 30px 0px; button.inline-flex.items-center 218.0x50.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 20px |
| Ancestor paint | 1 up div.w-full.min-w-0 bg #fcfbf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #5f6d77 @ 0.04 0px 4px 5px 0px, #5f6d77 @ 0.03 0px 8px 15px 0px, #5f6d77 @ 0.08 0px 30px 50px 0px |
| How | at rest |

Crops: `plan-card-default.png`.

#### icon-button

Icon button. A round icon-only expander (bg-iconbutton-bg).

Page: pricing. Selector: `button.iconbutton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #071a31 @ 0.05 | = | 1px solid #000000 @ 0 | = |
| Radius | 8px | = | = | = |
| Background | #071a31 @ 0.05 | #071a31 @ 0.1 | = | #071a31 @ 0.2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6bb1ff offset 0px | = |
| Font | Geist 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #071a31 | = | = | = |
| ::after | 722px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/ib.inline-flex 32.0x32.0 bg #071a31 @ 0.05 border T:1px solid #071a31 @ 0.05 / R:1px solid #071a31 @ 0.05 / B:1px solid #071a31 @ 0.05 / L:1px solid #071a31 @ 0.05 r 8px | button.group/ib.inline-flex 32.0x32.0 bg #071a31 @ 0.1 border T:1px solid #071a31 @ 0.05 / R:1px solid #071a31 @ 0.05 / B:1px solid #071a31 @ 0.05 / L:1px solid #071a31 @ 0.05 r 8px | button.group/ib.inline-flex 32.0x32.0 bg #071a31 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #6bb1ff offset 0px | button.group/ib.inline-flex 32.0x32.0 bg #071a31 @ 0.2 border T:1px solid #071a31 @ 0.05 / R:1px solid #071a31 @ 0.05 / B:1px solid #071a31 @ 0.05 / L:1px solid #071a31 @ 0.05 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `icon-button-default.png`, `icon-button-hover.png`, `icon-button-focus-visible.png`, `icon-button-pressed.png`.

#### feature-tip

Feature tooltip link. A dotted-underline feature name (opens a tooltip on hover, never clicked).

Page: pricing. Selector: `dotted-underline feature`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 274 x 39.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.cursor-pointer.underline: Geist 14px/19.6px 400, #071a31 | = | = | = |
| Transition | none | = | = | = |
| Icon | 28 x 8.5, colour #071a31 | = | = | = |
| Painted layers | span.bg-midnight.text-magnolia 240.0x49.6 bg #071a31 r 16px shadow #476788 @ 0.04 0px 4px 5px 0px, #476788 @ 0.03 0px 8px 15px 0px, #476788 @ 0.06 0px 15px 30px 0px | = | span.cursor-pointer.underline 274.0x39.2 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px; span.bg-midnight.text-magnolia 240.0x49.6 bg #071a31 r 16px shadow #476788 @ 0.04 0px 4px 5px 0px, #476788 @ 0.03 0px 8px 15px 0px, #476788 @ 0.06 0px 15px 30px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feature-tip-default.png`, `feature-tip-hover.png`, `feature-tip-focus-visible.png`, `feature-tip-pressed.png`.

### Booking (invitee flow)

#### bk-panel

Booking panel. The invitee page's centred panel (booking-kit), Proxima Nova.

Page: booking. Selector: `.booking-kit_main-panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1058 x 698 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Proxima Nova 14px/21px 400 |
| Letter spacing | normal |
| Colour | #0a2540 |
| Text node | h1.booking-kit_name_421eda97.booking-kit_name-is-tablet-up_60da3a87: Proxima Nova 16px/24px 700, #476788 |
| Transition | all 0.22s ease-out |
| Painted layers | a.p5OOZEP33JytcHx09AGf.Y1etSIf8jWSCgzZ8N4ug 360.0x200.0 border T:1px solid #d4e0ed / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.E6A3_hj2CTqFJYH9gG_X.XNmY6Nya_0DuJwssmiqi 30.0x30.0 bg #4a91e9 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50%; div.eqojUiBHZecMmRsj7EyU.S1Tx6TrN8K5ZDJ4UvvxY 16.0x16.0 border T:8px solid #000000 @ 0 / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #0a2540; button.uvkj3lh.b15h8fme 99.1x22.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px |
| Ancestor paint | 1 up div.DBKEjqt4IKCsNgnjbfTn.WZCebKno5lyab4hdps3i bg #ffffff shadow #000000 @ 0.08 0px 1px 8px 0px |
| How | at rest |

Crops: `bk-panel-default.png`.

#### bk-poweredby

Powered-by badge. The "POWERED BY Calendly" badge link; measured never followed.

Page: booking. Selector: `a "POWERED BY"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105 x 105 | 109.2 x 109.2 | 109.2 x 109.2 | 109.2 x 109.2 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Proxima Nova 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | div.vRuCIUPukscALsuTGtnz.qRpE9F04VChlQTAAGFkZ: Proxima Nova 8px/9.6px 700, #ffffff | = | = | = |
| Transition | all 0.1s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 6px x 6px, absolute, bg #505960, radius 0px | 8px x 8px, absolute, bg #000000, radius 0px | 8px x 8px, absolute, bg #000000, radius 0px | 8px x 8px, absolute, bg #000000, radius 0px |
| ::after | 6px x 6px, absolute, bg #505960, radius 0px | 8px x 8px, absolute, bg #000000, radius 0px | 8px x 8px, absolute, bg #000000, radius 0px | 8px x 8px, absolute, bg #000000, radius 0px |
| Painted layers | a::before.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 6pxx6px bg #505960; a::after.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 6pxx6px bg #505960; div.wKVnbiJhcPutKB97Xm9w.FBx2fW8zQAzwOYlGYw3k 142.4x142.4 bg #505960 shadow #000000 @ 0.2 0px 2px 4px 0px | a::before.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px bg #000000; a::after.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px bg #000000; div.wKVnbiJhcPutKB97Xm9w.FBx2fW8zQAzwOYlGYw3k 148.1x148.1 bg #40474c shadow #000000 @ 0.2 0px 2px 4px 0px | a::before.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px bg #000000; a::after.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px bg #000000; div.wKVnbiJhcPutKB97Xm9w.FBx2fW8zQAzwOYlGYw3k 148.1x148.1 bg #40474c shadow #000000 @ 0.2 0px 2px 4px 0px | a::before.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px bg #000000; a::after.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px bg #000000; div.wKVnbiJhcPutKB97Xm9w.FBx2fW8zQAzwOYlGYw3k 148.1x148.1 bg #40474c shadow #000000 @ 0.2 0px 2px 4px 0px |
| Ancestor paint | 1 up div.DBKEjqt4IKCsNgnjbfTn.WZCebKno5lyab4hdps3i bg #ffffff shadow #000000 @ 0.08 0px 1px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.04, 0, 0, 1.04, 0, 0) | matrix(1.04, 0, 0, 1.04, 0, 0) | matrix(1.04, 0, 0, 1.04, 0, 0) |

Crops: `bk-poweredby-default.png`, `bk-poweredby-hover.png`, `bk-poweredby-focus-visible.png`, `bk-poweredby-pressed.png`.

#### bk-event

Event link. An event-type link in the invitee list; measured, never opened by a press (the event page was navigated to directly).

Page: booking. Selector: `booking event link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 199.97 | = | = | = |
| Padding | 20px | = | = | = |
| Border | T: 1px solid #d4e0ed; R: 1px solid #000000 @ 0; B: 1px solid #000000 @ 0; L: 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #e7edf6 | #e7edf6 | #e7edf6 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Proxima Nova 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a2540 | = | = | = |
| Text node | p.c1auvngn.cg4c1by: Proxima Nova 16px/22.4px 700, #0a2540 | = | = | = |
| Transition | border-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.p5OOZEP33JytcHx09AGf.Y1etSIf8jWSCgzZ8N4ug 360.0x200.0 border T:1px solid #d4e0ed / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.E6A3_hj2CTqFJYH9gG_X.XNmY6Nya_0DuJwssmiqi 30.0x30.0 bg #4a91e9 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50%; div.eqojUiBHZecMmRsj7EyU.S1Tx6TrN8K5ZDJ4UvvxY 16.0x16.0 border T:8px solid #000000 @ 0 / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #0a2540 | a.p5OOZEP33JytcHx09AGf.Y1etSIf8jWSCgzZ8N4ug 360.0x200.0 bg #e7edf6 border T:1px solid #d4e0ed / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.E6A3_hj2CTqFJYH9gG_X.XNmY6Nya_0DuJwssmiqi 30.0x30.0 bg #4a91e9 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50%; div.eqojUiBHZecMmRsj7EyU.S1Tx6TrN8K5ZDJ4UvvxY 16.0x16.0 border T:8px solid #000000 @ 0 / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #0a2540 | a.p5OOZEP33JytcHx09AGf.Y1etSIf8jWSCgzZ8N4ug 360.0x200.0 bg #e7edf6 border T:1px solid #d4e0ed / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.E6A3_hj2CTqFJYH9gG_X.XNmY6Nya_0DuJwssmiqi 30.0x30.0 bg #4a91e9 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50%; div.eqojUiBHZecMmRsj7EyU.S1Tx6TrN8K5ZDJ4UvvxY 16.0x16.0 border T:8px solid #000000 @ 0 / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #0a2540 | a.p5OOZEP33JytcHx09AGf.Y1etSIf8jWSCgzZ8N4ug 360.0x200.0 bg #e7edf6 border T:1px solid #d4e0ed / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.E6A3_hj2CTqFJYH9gG_X.XNmY6Nya_0DuJwssmiqi 30.0x30.0 bg #4a91e9 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50%; div.eqojUiBHZecMmRsj7EyU.S1Tx6TrN8K5ZDJ4UvvxY 16.0x16.0 border T:8px solid #000000 @ 0 / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #0a2540 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bk-event-default.png`, `bk-event-hover.png`, `bk-event-focus-visible.png`, `bk-event-pressed.png`.

#### bk-calendar

Calendar. The month grid on the event page.

Page: event. Selector: `calendar grid`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 399 x 452.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Proxima Nova 14px/21px 400 |
| Letter spacing | normal |
| Colour | #0a2540 |
| Text node | div.booking-kit_title-text_2dda76c3.booking-kit_static-title_b43ef470: Proxima Nova 14px/21px 700, #0a2540 |
| Transition | none |
| Icon | 24 x 24, colour #a6bbd1 |
| Painted layers | button.ukre8r9.u1rh2s45 40.0x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.ukre8r9.bosxatq 40.0x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; div.booking-kit_generated-7_cad3d51e 4.0x4.0 bg #0a2540 r 50%; button.ukre8r9.booking-kit_button_ce747ff0 44.0x44.0 bg #f4f8ff r 50%; button.ukre8r9.booking-kit_button_ce747ff0 44.0x44.0 bg #f4f8ff r 50%; button.ukre8r9.booking-kit_button_ce747ff0 44.0x44.0 bg #f4f8ff r 50% |
| How | at rest |

Crops: none.

#### bk-month-nav

Month nav button. A previous/next-month arrow button; measured, never pressed.

Page: event. Selector: `button "Go to next month"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Gap | 4px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 9999px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Proxima Nova 14px/21px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #a6bbd1 | = | - | = |
| Transition | none | = | - | = |
| Cursor | default | = | - | = |
| Icon | 24 x 24, colour #a6bbd1 | = | - | = |
| Painted layers | button.ukre8r9.u1rh2s45 40.0x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

#### bk-day

Day cell. An enabled day button in the calendar grid; one was selected for the times-panel state, never booked.

Page: event. Selector: `calendar day button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #f4f8ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0099ff offset 2px | = |
| Font | Proxima Nova 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #004eba | = | = | = |
| Text node | span: Proxima Nova 14px/21px 400, #004eba | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ukre8r9.booking-kit_button_ce747ff0 44.0x44.0 bg #f4f8ff r 50% | = | button.ukre8r9.booking-kit_button_ce747ff0 44.0x44.0 bg #f4f8ff r 50% outline 2px solid #0099ff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### bk-day-selected

Day cell, selected. The picked day in its selected state (solid #006bff, locked disabled once picked).

Page: event. Selector: `button.booking-kit_button-selected`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 50% |
| Background | #006bff |
| Box shadow | none |
| Outline | none |
| Font | Proxima Nova 14px/21px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Proxima Nova 14px/21px 400, #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | button.ukre8r9.u1rh2s45 44.0x44.0 bg #006bff r 50% |
| How | at rest |

Crops: none.

#### bk-timeslot

Time slot. An available time button in the revealed column; measured, never pressed (Next is never reached).

Page: event. Selector: `time slot button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 278.39 x 52 | = | = | = |
| Padding | 13px 10px | = | = | = |
| Border | 1px solid #006bff | 2px solid #006bff | 2px solid #006bff | 2px solid #006bff |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0099ff offset 2px | = |
| Font | Proxima Nova 16px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #004eba | = | = | = |
| Text node | div.booking-kit_time_ca93b78d: Proxima Nova 16px/10px 700, #004eba | = | = | = |
| Transition | width, transform 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 276.391px x 64px, absolute, bg #000000 @ 0, radius 0px | 274.391px x 62px, absolute, bg #000000 @ 0, radius 0px | 274.391px x 62px, absolute, bg #000000 @ 0, radius 0px | 274.391px x 62px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | button.ukre8r9.booking-kit_generated-2_c4274312 278.4x52.0 border T:1px solid #006bff / R:1px solid #006bff / B:1px solid #006bff / L:1px solid #006bff r 8px | button.ukre8r9.booking-kit_generated-2_c4274312 278.4x52.0 border T:2px solid #006bff / R:2px solid #006bff / B:2px solid #006bff / L:2px solid #006bff r 8px | button.ukre8r9.booking-kit_generated-2_c4274312 278.4x52.0 border T:2px solid #006bff / R:2px solid #006bff / B:2px solid #006bff / L:2px solid #006bff r 8px outline 2px solid #0099ff offset 2px | button.ukre8r9.booking-kit_generated-2_c4274312 278.4x52.0 border T:2px solid #006bff / R:2px solid #006bff / B:2px solid #006bff / L:2px solid #006bff r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### bk-timezone

Timezone control. The timezone dropdown under the calendar (its list was never opened).

Page: event. Selector: `timezone control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 245.34 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0099ff offset 2px | = |
| Font | Proxima Nova 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a2540 | = | = | = |
| Text node | div.booking-kit_name_1537fc93: Proxima Nova 14px/21px 400, #0a2540 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0a2540 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.booking-kit_container_40b6f8c2 bg #0a2540 @ 0.1 | = | = |
| Painted layers | - | = | button.ukre8r9.booking-kit_dropdown-button_72cb6101 245.3x21.0 outline 2px solid #0099ff offset 2px | = |

Crops: none.

#### bk-day-today

Day cell, today. Today's cell (aria-current="date"), an unavailable day here.

Page: event. Selector: `button[aria-current="date"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 50% |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Proxima Nova 14px/21px 400 |
| Letter spacing | normal |
| Colour | #0a2540 |
| Text node | span: Proxima Nova 14px/21px 400, #0a2540 |
| Transition | none |
| Cursor | default |
| Painted layers | div.booking-kit_generated-7_cad3d51e 4.0x4.0 bg #0a2540 r 50% |
| How | at rest |

Crops: none.

### Log in and sign up

#### login-card

Login card. The centred login card; never filled or submitted.

Page: login. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 464 x 500.36 |
| Padding | 32px 48px |
| Gap | 64px |
| Border | none |
| Radius | 48px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.font-calendly-sans.type-h3: Calendly Sans 36px/39.6px 500, #071a31, ls -1px |
| Transition | none |
| Icon | 16 x 16, colour #071a31 |
| Painted layers | div.surface-light.bg-white 464.0x500.4 bg #ffffff r 48px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; input.peer.w-full 368.0x48.4 bg #ffffff border T:1px solid #c6ccd2 / R:1px solid #c6ccd2 / B:1px solid #c6ccd2 / L:1px solid #c6ccd2 r 16px; button.inline-flex.items-center 368.0x50.4 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 20px; hr.flex-1.border-border-subtle 152.5x1.0 border T:1px solid #d8dce0; hr.flex-1.border-border-subtle 152.5x1.0 border T:1px solid #d8dce0; button.inline-flex.items-center 368.0x50.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 20px |
| How | at rest |

Crops: `login-card-default.png`.

#### email-field

Email field. The email input; sample text was typed and deleted, nothing sent.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 368 x 48.39 | = | = |
| Padding | 12px 16px | = | = |
| Border | 1px solid #c6ccd2 | 1px solid #6bb1ff | 1px solid #6bb1ff |
| Radius | 16px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | Geist 16px/22.4px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #071a31 | = | = |
| Transition | border-color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0, opacity 1 | = | = |
| Painted layers | input.peer.w-full 368.0x48.4 bg #ffffff border T:1px solid #c6ccd2 / R:1px solid #c6ccd2 / B:1px solid #c6ccd2 / L:1px solid #c6ccd2 r 16px | input.peer.w-full 368.0x48.4 bg #ffffff border T:1px solid #6bb1ff / R:1px solid #6bb1ff / B:1px solid #6bb1ff / L:1px solid #6bb1ff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | input.peer.w-full 368.0x48.4 bg #ffffff border T:1px solid #6bb1ff / R:1px solid #6bb1ff / B:1px solid #6bb1ff / L:1px solid #6bb1ff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### continue-btn

Continue button. The Continue-with-email submit; measured, never pressed (a press would submit).

Page: login. Selector: `button "Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 50.39 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #6bb1ff | = |
| Radius | 20px | = | = | = |
| Background | #071a31 | #0e396a | = | #1e5ea7 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Geist 16px/22.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfbf8 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 368.0x50.4 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 20px | button.inline-flex.items-center 368.0x50.4 bg #0e396a border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 20px | button.inline-flex.items-center 368.0x50.4 bg #071a31 border T:2px solid #6bb1ff / R:2px solid #6bb1ff / B:2px solid #6bb1ff / L:2px solid #6bb1ff r 20px | button.inline-flex.items-center 368.0x50.4 bg #1e5ea7 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `continue-btn-default.png`, `continue-btn-hover.png`, `continue-btn-focus-visible.png`, `continue-btn-pressed.png`.

#### sso-btn

SSO button. A Continue-with-Google/Microsoft button; measured, never followed.

Page: login. Selector: `button "Continue with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 50 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #071a31 | = | 1px solid #000000 @ 0 | 1px solid #0e396a |
| Radius | 20px | = | = | = |
| Background | transparent | #071a31 | = | #0e396a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6bb1ff offset -2px | = |
| Font | Geist 16px/22.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #071a31 | #fcfbf8 | = | #fcfbf8 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 368.0x50.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 20px | button.inline-flex.items-center 368.0x50.0 bg #071a31 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 20px | button.inline-flex.items-center 368.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px outline 2px solid #6bb1ff offset -2px | button.inline-flex.items-center 368.0x50.0 bg #0e396a border T:1px solid #0e396a / R:1px solid #0e396a / B:1px solid #0e396a / L:1px solid #0e396a r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-btn-default.png`, `sso-btn-hover.png`, `sso-btn-focus-visible.png`, `sso-btn-pressed.png`.

#### signup-card

Signup card. The centred create-account card; never filled or submitted.

Page: signup. Selector: `signup card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 912 x 579.55 |
| Padding | 32px 48px |
| Gap | 64px |
| Border | none |
| Radius | 48px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.font-calendly-sans.type-h3: Calendly Sans 36px/39.6px 500, #071a31, ls -1px |
| Transition | none |
| Icon | 16 x 16, colour #071a31 |
| Painted layers | div.surface-light.bg-white 912.0x579.5 bg #ffffff r 48px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; input.peer.w-full 368.0x48.4 bg #ffffff border T:1px solid #c6ccd2 / R:1px solid #c6ccd2 / B:1px solid #c6ccd2 / L:1px solid #c6ccd2 r 16px; button.inline-flex.items-center 368.0x50.4 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 20px; hr.flex-1.border-border-subtle 152.5x1.0 border T:1px solid #d8dce0; hr.flex-1.border-border-subtle 152.5x1.0 border T:1px solid #d8dce0; button.inline-flex.items-center 368.0x50.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 20px |
| How | at rest |

Crops: `signup-card-default.png`.

#### signup-field

Signup email field. The signup email input; focused only, never filled or submitted.

Page: signup. Selector: `signup input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 368 x 48.39 | = |
| Padding | 12px 16px | = |
| Border | 1px solid #c6ccd2 | 1px solid #6bb1ff |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | Geist 16px/22.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #071a31 | = |
| Transition | border-color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0, opacity 1 | = |
| Painted layers | input.peer.w-full 368.0x48.4 bg #ffffff border T:1px solid #c6ccd2 / R:1px solid #c6ccd2 / B:1px solid #c6ccd2 / L:1px solid #c6ccd2 r 16px | input.peer.w-full 368.0x48.4 bg #ffffff border T:1px solid #6bb1ff / R:1px solid #6bb1ff / B:1px solid #6bb1ff / L:1px solid #6bb1ff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6bb1ff @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `signup-field-default.png`, `signup-field-focused.png`.

### Footer

#### footer

Footer. The footer card (a .dark island): link columns, legal and social.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1037.66 |
| Padding | 24px |
| Border | none |
| Radius | 0px |
| Background | #fcfbf8 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.font-sans.text-text-primary: ui-sans-serif 60px/66px 500, #fcfbf8, ls -2px |
| Transition | none |
| Icon | 52 x 52, colour #000000 |
| Painted layers | footer.flex.w-full 1440.0x1037.7 bg #fcfbf8; div.relative.flex 1392.0x989.7 bg #071a31 r 64px; span.w-fit.inline-flex 85.4x20.8 bg #6bb1ff @ 0.6 r 8px; div.flex.flex-col 1200.0x211.0 border T:1px solid #0c2d54; a.keyboard-focus-after.inline-flex 48.0x48.0 bg #fcfbf8 @ 0.05 border T:1px solid #fcfbf8 @ 0.1 / R:1px solid #fcfbf8 @ 0.1 / B:1px solid #fcfbf8 @ 0.1 / L:1px solid #fcfbf8 @ 0.1 r 12px; a.keyboard-focus-after.inline-flex 48.0x48.0 bg #fcfbf8 @ 0.05 border T:1px solid #fcfbf8 @ 0.1 / R:1px solid #fcfbf8 @ 0.1 / B:1px solid #fcfbf8 @ 0.1 / L:1px solid #fcfbf8 @ 0.1 r 12px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.91 x 19.59 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6bb1ff offset 0px | = |
| Font | Geist 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfbf8 @ 0.698 | #fcfbf8 | = | #fcfbf8 |
| Text node | span: Geist 14px/19.6px 400, #fcfbf8 @ 0.698 | span: Geist 14px/19.6px 400, #fcfbf8 | = | span: Geist 14px/19.6px 400, #fcfbf8 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.keyboard-focus-before.inline-flex 71.9x19.6 r 4px outline 2px solid #6bb1ff offset 0px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfbf8 |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.mbl:hidden: Geist 14px/19.6px 500, #fcfbf8 |
| Transition | box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 32 x 32, colour #000000 |
| Painted layers | header.w-full.bg-surface-bg-primary 390.0x64.0 bg #fcfbf8; a.inline-flex.items-center 0.0x0.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px; a.inline-flex.items-center 0.0x0.0 border T:1px solid #071a31 / R:1px solid #071a31 / B:1px solid #071a31 / L:1px solid #071a31 r 16px; a.inline-flex.items-center 102.4x39.6 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px; a.inline-flex.items-center 0.0x0.0 bg #071a31 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header menu toggle.

Page: mobile. Selector: `header menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The header menu panel opened by its own toggle.

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 780 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.keyboard-focus-before.[--kb-focus-offset:-1px]: Geist 16px/22.4px 500, #000000 |
| Transition | opacity, visibility 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 24 x 24, colour #000000 |
| Painted layers | button.absolute.inset-0 390.0x780.0 bg #071a31 @ 0.2; div.absolute.top-0 390.0x780.0 bg #fcfbf8 border T:1px solid #071a31 @ 0.1; div._90SS5G_scrollFadeTop 390.0x40.0 image linear-gradient(#fcfbf8, #000000 @ 0); button.keyboard-focus-before.[--kb-focus-offset:-1px] 390.0x57.0 border B:1px solid #071a31 @ 0.1; div.border-b.border-divider 390.0x651.0 bg #ffffff border B:1px solid #071a31 @ 0.1; span.w-fit.inline-flex 42.4x20.8 bg #071a31 @ 0.05 r 8px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened header menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 57 | = | = | = |
| Padding | 8px 8px 8px 24px | = | = | = |
| Border | T: none; R: none; B: 1px solid #071a31 @ 0.1; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6bb1ff offset -1px | = |
| Font | Geist 16px/22.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| Painted layers | button.keyboard-focus-before.[--kb-focus-offset:-1px] 390.0x57.0 border B:1px solid #071a31 @ 0.1 | = | button.keyboard-focus-before.[--kb-focus-offset:-1px] 390.0x57.0 border B:1px solid #071a31 @ 0.1 outline 2px solid #6bb1ff offset -1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Calendly Sans 40px/44px 500 |
| Letter spacing | normal |
| Colour | #fcfbf8 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

calendly.com serves its Astro CSS bundles same-origin (the booking bundle comes from assets.calendly.com and was read from network responses), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- booking: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `background-color 0.15s, color 0.15s, border-color 0.15s`, `opacity 0.15s`, `transform 0.15s linear`, `none`, `0.2s ease-in`, `0.4s`

- event: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `background-color 0.15s, color 0.15s, border-color 0.15s`, `opacity 0.15s`, `transform 0.15s linear`, `none`, `0.2s ease-in`, `0.4s`

- home: `none`, `width 0.5s ease-in-out, box-shadow 0.18s ease-in-out`, `width 0.5s ease-in-out`, `opacity 0.2s`, `padding 0.2s ease-in-out, margin-left 0.2s ease-in-out, margin-right 0.2s ease-in-out`, `transform 0.3s ease-out, opacity 0.3s ease-out`, `transform 0.3s ease-in, opacity 0.15s ease-in 0.15s`, `0.1s`, `300ms ease-in`, `background-color 0.15s, color 0.15s, border-color 0.15s`, `opacity 0.15s`, `transform 0.15s linear`

- login: `none`, `width 0.5s ease-in-out, box-shadow 0.18s ease-in-out`, `width 0.5s ease-in-out`, `opacity 0.2s`, `padding 0.2s ease-in-out, margin-left 0.2s ease-in-out, margin-right 0.2s ease-in-out`, `transform 0.3s ease-out, opacity 0.3s ease-out`, `transform 0.3s ease-in, opacity 0.15s ease-in 0.15s`, `0.1s`, `300ms ease-in`, `background-color 0.15s, color 0.15s, border-color 0.15s`, `opacity 0.15s`, `transform 0.15s linear`

- pricing: `none`, `width 0.5s ease-in-out, box-shadow 0.18s ease-in-out`, `width 0.5s ease-in-out`, `opacity 0.2s`, `padding 0.2s ease-in-out, margin-left 0.2s ease-in-out, margin-right 0.2s ease-in-out`, `transform 0.3s ease-out, opacity 0.3s ease-out`, `transform 0.3s ease-in, opacity 0.15s ease-in 0.15s`, `0.1s`, `300ms ease-in`, `background-color 0.15s, color 0.15s, border-color 0.15s`, `opacity 0.15s`, `transform 0.15s linear`
