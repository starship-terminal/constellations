# Exa component measurements

Computed styles read from Exa's public surface on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the three public sites — the exa.ai marketing pages (home, pricing, the Search-API product page), the auth.exa.ai sign-in card dashboard.exa.ai redirects to, and the exa.ai/docs Mintlify docs in both their themes (dark from a prefers-color-scheme context, never the theme menu) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened` is the resting state after the component's own local toggle (the "Products" mega-menu on a real pointer hover, a pricing use-case pill, the mobile hamburger). The home demo's Run-preview arrow, the Get-started/Sign-up actions and the login buttons were never pressed; the demo's query field and the sign-in e-mail were filled with test text and cleared.

## Components

### Marketing chrome

#### mkt-header

Marketing header. The sticky top bar: wordmark, Products/Solutions/Resources hover menus, Docs, Pricing, Sign in, Contact sales and Sign up, under the Exa 3.0 announcement strip.

Page: home. Selector: `div.header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.flex.items-center: ABCDiatype 15px/21px 400, #5f5a54, ls -0.3px |
| Transition | none |
| Icon | 0 x 0, colour #4b5563 |
| Painted layers | div.header.sticky 1425.0x55.0 bg #ffffff; nav.font-inter.h-16 0.0x0.0 bg #ffffff; div.hidden.fixed 0.0x0.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; span.inline-flex.items-center 0.0x0.0 bg #dbeafe r 9999px; div.flex.shrink-0 0.0x0.0 bg #ffffff border T:1px solid #f3f4f6; a.signed-out-only.block 0.0x0.0 bg #ffffff border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 4px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-announce

Announcement strip. The "Introducing Exa 3.0" banner over the header, with a Learn-more link and a dismiss button (never pressed).

Page: home. Selector: `announcement banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 20 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.hidden.text-sm: ABCDiatype 14px/20px 500, #0972d5 |
| Transition | none |
| Ancestor paint | 1 up div.relative.flex bg #eef8ff |
| How | at rest |

Crops: `mkt-announce-default.png`.

#### mkt-logo

Logo. The exa wordmark at the left of the header.

Page: home. Selector: `header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 70.42 x 17 |
| Padding | 0px 16px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/24px 400 |
| Letter spacing | normal |
| Colour | #1f40ed |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### mkt-nav-trigger

Products menu trigger. The header "Products" item; the mega-menu opens on a real pointer hover, never a click.

Page: home. Selector: `div.cursor-pointer Products`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 96.61 x 32 | = |
| Padding | 4px 12px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #f3f4f6 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABCDiatype 15px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #5f5a54 | #000000 |
| Text node | span.flex.items-center: ABCDiatype 15px/21px 400, #5f5a54, ls -0.3px | span.flex.items-center: ABCDiatype 15px/21px 400, #000000, ls -0.3px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #5f5a54 | 12 x 12, colour #000000 |
| How | at rest | mouse hover |
| Painted layers | - | div.flex.h-8 96.6x32.0 bg #f3f4f6 r 4px |

Crops: `mkt-nav-trigger-default.png`, `mkt-nav-trigger-hover.png`.

#### mkt-menu

Products mega-menu. The dropdown the "Products" hover opens: Search/Contents/Agent/Monitors APIs, Exa Snapshot and Library, integrations and use cases — a local toggle, its links never followed.

Page: home. Selector: `div.absolute.top-full`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 485 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.text-[14px].font-medium: Inter 14px/18.2px 500, #111827 |
| Transition | all 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Transform | matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0.19, 0, 1, -0.001, -190, 0, 0, 1) |
| Icon | 18 x 18, colour #374151 |
| Painted layers | div.overflow-hidden.rounded-[8px] 380.0x475.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.08 offset 0px; div.mt-0.5.flex 32.0x32.0 bg #f1f2f4 r 7px; div.mt-0.5.flex 32.0x32.0 bg #f1f2f4 r 7px; div.mt-0.5.flex 32.0x32.0 bg #f1f2f4 r 7px; div.mt-0.5.flex 32.0x32.0 bg #f1f2f4 r 7px; div.mt-0.5.flex 32.0x32.0 bg #f1f2f4 r 7px |
| How | at rest |

Crops: `mkt-menu-default.png`.

#### mkt-menu-item

Mega-menu link. One product link inside the open mega-menu; measured, never followed.

Page: home. Selector: `mega-menu link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 364 x 56.06 |
| Padding | 10px 12px |
| Gap | 12px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f40ed |
| Text node | div.text-[14px].font-medium: Inter 14px/18.2px 500, #111827 |
| Transition | none |
| Cursor | pointer |
| Icon | 18 x 18, colour #374151 |
| Painted layers | div.mt-0.5.flex 32.0x32.0 bg #f1f2f4 r 7px |
| How | at rest |

Crops: `mkt-menu-item-default.png`.

#### mkt-nav-link

Nav link. A marketing header link (Docs/Pricing); measured, never followed.

Page: home. Selector: `header nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f3f4f6 | = | #f3f4f6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | ABCDiatype 15px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5f5a54 | #000000 | = | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.h-8 58.0x32.0 bg #f3f4f6 r 4px | a.flex.h-8 58.0x32.0 r 4px outline 1px auto #101010 offset 1px | a.flex.h-8 58.0x32.0 bg #f3f4f6 r 4px |

Crops: `mkt-nav-link-default.png`, `mkt-nav-link-hover.png`, `mkt-nav-link-focus-visible.png`, `mkt-nav-link-pressed.png`.

#### mkt-signin

Sign-in link. The header "Sign in" link to dashboard.exa.ai; measured, never followed.

Page: home. Selector: `header Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72 x 33 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f3f4f6 | = | #f3f4f6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5f5a54 | #000000 | = | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.signed-out-only.font-inter 72.0x33.0 bg #f3f4f6 r 4px | a.signed-out-only.font-inter 72.0x33.0 r 4px outline 1px auto #101010 offset 1px | a.signed-out-only.font-inter 72.0x33.0 bg #f3f4f6 r 4px |

Crops: `mkt-signin-default.png`, `mkt-signin-hover.png`, `mkt-signin-focus-visible.png`, `mkt-signin-pressed.png`.

#### mkt-sales

Contact-sales link. The bordered "Contact sales" button-link; measured, never followed.

Page: home. Selector: `header Contact sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121 x 33 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #f2f0ef | #e8e6e5 | = | #e8e6e5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #514837 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group-hover-link.font-inter 121.0x33.0 bg #f2f0ef r 4px | a.group-hover-link.font-inter 121.0x33.0 bg #e8e6e5 r 4px | a.group-hover-link.font-inter 121.0x33.0 bg #f2f0ef r 4px outline 1px auto #101010 offset 1px | a.group-hover-link.font-inter 121.0x33.0 bg #e8e6e5 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-sales-default.png`, `mkt-sales-hover.png`, `mkt-sales-focus-visible.png`, `mkt-sales-pressed.png`.

#### mkt-signup

Sign-up button. The black "Sign up" pill — the header's one filled action; measured, never followed.

Page: home. Selector: `header Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.05 x 31.59 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #000000 | #1f2937 | = | #1f2937 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.signed-out-only: ABCDiatype 14px/19.6px 500, #ffffff, ls -0.28px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group-hover-link.font-inter 69.0x31.6 bg #000000 r 4px | a.group-hover-link.font-inter 69.0x31.6 bg #1f2937 r 4px | a.group-hover-link.font-inter 69.0x31.6 bg #000000 r 4px outline 1px auto #101010 offset 1px | a.group-hover-link.font-inter 69.0x31.6 bg #1f2937 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-signup-default.png`, `mkt-signup-hover.png`, `mkt-signup-focus-visible.png`, `mkt-signup-pressed.png`.

### Home hero and search demo

#### hero-h1

Hero headline. "The world's data for AI agents" — the ABC Arizona Flare display.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 757.14 x 45.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arizona 63.2px/45.504px 400 |
| Letter spacing | -1.896px |
| Colour | #111827 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero sub. "Search the largest index of public web and private information."

Page: home. Selector: `hero sub`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 757.14 x 25.77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 18.4px/25.76px 400 |
| Letter spacing | -0.368px |
| Colour | #6b7280 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Try-API CTA. The black "Try API for free" button under the hero copy; measured never pressed (it leads to sign-up).

Page: home. Selector: `Try API for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 124.2 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #000000 | #1f2937 | = | #1f2937 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 15px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.signed-out-only: ABCDiatype 15px/21px 500, #ffffff, ls -0.3px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-inter.inline-flex 124.2x40.0 bg #000000 r 4px | a.font-inter.inline-flex 124.2x40.0 bg #1f2937 r 4px | a.font-inter.inline-flex 124.2x40.0 bg #000000 r 4px outline 1px auto #101010 offset 1px | a.font-inter.inline-flex 124.2x40.0 bg #1f2937 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### demo-widget

Search demo widget. The interactive preview card under the hero: query field, Search/Agent modes, latency and category pills, output tabs and a result panel that asks the visitor to sign in when the request cannot run.

Page: home. Selector: `demo widget`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 342 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | textarea.block.w-full: ABCDiatype 16px/24px 400, #111827 |
| Transition | none |
| Icon | 14 x 14, colour #000000 |
| Painted layers | div 700.0x82.0 bg #ffffff r 12px shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.08 offset 0px; textarea.block.w-full 672.0x24.0 outline 2px solid #000000 @ 0 offset 2px; div.relative.inline-flex 180.0x31.6 bg #f2f1f0 r 6px shadow #000000 @ 0.04 0px 0px 0px 1px inset; div.pointer-events-none.absolute 86.0x27.6 bg #ffffff r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px 0px, #000000 @ 0.06 0px 4px 12px 0px; span.exa-agent-shimmer-icon-mask.h-3.5 14.0x14.0 image linear-gradient(90deg, #1f40ed 0%, #1f40ed 35%, #7cc0ff 50%, #1f40ed 65%, #1f40ed 100%); button.flex.h-8 32.0x32.0 bg #f3f4f6 r 8px |
| How | at rest |

Crops: `demo-widget-default.png`.

#### demo-textarea

Demo query field. The "Find anything…" query box, pre-filled with "Latest open source LLMs"; focused and typed into then restored — the preview was never run.

Page: home. Selector: `demo textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 672 x 24 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | ABCDiatype 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.4, opacity 1 | = | = |
| Painted layers | textarea.block.w-full 672.0x24.0 outline 2px solid #000000 @ 0 offset 2px | = | = |
| Ancestor paint | 2 up div bg #ffffff shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.08 | 2 up div bg #ffffff shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.12 | 2 up div bg #ffffff shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.12 |
| How | at rest | clicked into the field | typed "latest research on fusion", then deleted; nothing sent |

Crops: `demo-textarea-default.png`, `demo-textarea-focused.png`, `demo-textarea-filled.png`.

#### demo-mode

Demo mode toggle. The Search/Agent segmented control at the top of the demo; measured, never pressed.

Page: home. Selector: `demo Search/Agent`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86 x 27.59 | = | = | = |
| Padding | 4px 8px 4px 6px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 14px/14px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.block.truncate: ABCDiatype 14px/19.6px 400, #000000, ls -0.28px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #000000 | = | = | = |
| Ancestor paint | 1 up div.relative.inline-flex bg #f2f1f0 shadow #000000 @ 0.04 0px 0px 0px 1px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-mode-default.png`, `demo-mode-hover.png`, `demo-mode-focus-visible.png`, `demo-mode-pressed.png`.

#### demo-pill

Latency pill. A LATENCY pill (Lite 300ms / Auto 1s / Deep ~10s); switching it only re-configures the preview, never fires a request.

Page: home. Selector: `demo latency pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.33 x 22.8 | = | = | = |
| Padding | 3px 7px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.45 | #000000 @ 0.6 | = | #000000 @ 0.6 |
| Text node | span.block.truncate: ABCDiatype 12px/16.8px 400, #000000 @ 0.45, ls -0.24px | span.block.truncate: ABCDiatype 12px/16.8px 400, #000000 @ 0.6, ls -0.24px | = | span.block.truncate: ABCDiatype 12px/16.8px 400, #000000 @ 0.6, ls -0.24px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.relative.inline-flex bg #f2f1f0 shadow #000000 @ 0.04 0px 0px 0px 1px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-pill-default.png`, `demo-pill-hover.png`, `demo-pill-focus-visible.png`, `demo-pill-pressed.png`.

#### demo-category

Category pill. A CATEGORY pill (Full Web / News / Companies / Research / People / Financials); local toggle only.

Page: home. Selector: `demo category pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.66 x 22.8 | = | = | = |
| Padding | 3px 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.04 0px 0px 0px 1px inset, #000000 @ 0.08 0px 1px 2px 0px, #000000 @ 0.06 0px 4px 12px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.truncate: ABCDiatype 12px/16.8px 400, #000000, ls -0.24px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex.min-w-0 72.7x22.8 bg #ffffff r 4px shadow #000000 @ 0.04 0px 0px 0px 1px inset, #000000 @ 0.08 0px 1px 2px 0px, #000000 @ 0.06 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-category-default.png`, `demo-category-hover.png`, `demo-category-focus-visible.png`, `demo-category-pressed.png`.

#### demo-output-tab

Output tab. A Results/Answer/Structured output tab; local toggle only.

Page: home. Selector: `demo output tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40.19 x 18.19 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ABCDiatype 13px/18.2px 400 | = | - | = |
| Letter spacing | -0.26px | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Ancestor paint | 2 up div.relative.inline-flex bg #f2f1f0 shadow #000000 @ 0.04 0px 0px 0px 1px inset | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `demo-output-tab-default.png`, `demo-output-tab-hover.png`, `demo-output-tab-pressed.png`.

#### demo-run

Run-preview button. The blue arrow button that would fire the demo request; measured at rest and hovered — never pressed.

Page: home. Selector: `demo run button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 32 x 32 | = |
| Padding | 0px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #d1d5db | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABCDiatype 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | not-allowed | = |
| Icon | 20 x 20, colour #ffffff | = |
| Painted layers | button.hover:scale-103.relative 32.0x32.0 bg #d1d5db r 8px | = |
| Ancestor paint | 3 up div bg #ffffff shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.08 | = |
| How | at rest | mouse hover |

Crops: `demo-run-default.png`, `demo-run-hover.png`.

#### demo-output

Demo output panel. The output area's signed-out state: "We couldn't verify your browser … Sign in to continue" — the widget's honest resting state in a headless browser.

Page: home. Selector: `demo output`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 401 x 32.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 11.5px/16.1px 400 |
| Letter spacing | -0.23px |
| Colour | #000000 @ 0.6 |
| Transition | none |
| How | at rest |

Crops: `demo-output-default.png`.

### Footer

#### mkt-footer

Footer. The marketing footer: link columns, status and social marks.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 1367.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.max-w-2xl.font-serif: Arizona 54.4px/59.84px 400, #000000, ls -1.632px |
| Transition | none |
| Painted layers | div.flex.w-full 1425.0x523.8 bg #ffffff; a.font-inter.inline-flex 124.2x40.0 bg #000000 r 4px; div.flex.items-end 1440.0x900.0 bg #0137e1; div.absolute.inset-x-0 1440.0x844.0 image linear-gradient(#0137e1 0%, #0023bf 100%); div.absolute.inset-0 1440.0x900.0 image url(data:…)'/></svg>"); div.left-0.top-0 1358.2x0.6 bg #006fff |
| How | at rest |

Crops: `mkt-footer-default.png`.

### Pricing

#### plan-card

Plan grid. The pricing plans table (STARTER Free / DEVELOPER Pay as you go / ENTERPRISE Custom): a row-divided grid rather than three independent card divs — the smallest node still holding a tier label and its action.

Page: pricing. Selector: `pricing grid`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1216 x 957.7 |
| Padding | 0px |
| Border | 1px solid #d7d9de @ 0.7 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.m-0.mb-2: ABCDiatype 12.8px/17.92px 500, #ffffff @ 0.85, ls 1.024px |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.grid.w-full 1216.0x957.7 border T:1px solid #d7d9de @ 0.7 / R:1px solid #d7d9de @ 0.7 / B:1px solid #d7d9de @ 0.7 / L:1px solid #d7d9de @ 0.7; article.group.flex 404.7x955.7 bg #ffffff; div.relative.min-h-[12rem] 372.7x192.0 bg #f5f4f1 r 10px; div.absolute.inset-0 372.7x192.0 image linear-gradient(#eaeffc @ 0.6 0%, #3881dd @ 0.6 33%, #0005c4 @ 0.6 69%, #00061f @ 0.6 100%; a.inline-flex.min-w-0 372.7x43.6 bg #000000 r 6px; div.mt-6.border-t 372.7x456.3 border T:1px solid #d7d9de @ 0.7 |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan card's price line ("Free" / "Pay as you go" / "Custom").

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 324.66 x 37.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arizona 37.6px/37.6px 400 |
| Letter spacing | -1.504px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's action ("Start building for free" / "Get an API key" / "Talk to sales"); measured never pressed.

Page: pricing. Selector: `plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 372.66 x 43.61 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #000000 | #1f1f1f | = | #1f1f1f |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | ABCDiatype 14.4px/21.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.min-w-0 372.7x43.6 bg #000000 r 6px | a.inline-flex.min-w-0 372.7x43.6 bg #1f1f1f r 6px | a.inline-flex.min-w-0 372.7x43.6 bg #000000 r 6px outline 1px auto #101010 offset 1px | a.inline-flex.min-w-0 372.7x43.6 bg #1f1f1f r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### pricing-pill

Use-case pill. A pricing scenario pill (Coding agents / Chatbots / …); its own toggle switches the estimate — a local control, never a form post.

Page: pricing. Selector: `pricing use-case pill`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 111.53 x 30.64 | = | = | = | = |
| Padding | 5.44px 9.28px | = | = | = | = |
| Border | 1px solid #111111 @ 0.12 | = | = | = | = |
| Radius | 6px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | GeistMono 11.84px/17.76px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #4b5563 | #000000 | = | #000000 | = |
| Transition | border-color, color 0.14s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.shrink-0.whitespace-nowrap 111.5x30.6 border T:1px solid #111111 @ 0.12 / R:1px solid #111111 @ 0.12 / B:1px solid #111111 @ 0.12 / L:1px solid #111111 @ 0.12 r 6px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | held open by an earlier toggle |

Crops: `pricing-pill-default.png`, `pricing-pill-hover.png`, `pricing-pill-focus-visible.png`, `pricing-pill-pressed.png`, `pricing-pill-opened.png`.

#### pricing-h1

Pricing headline. "Start searching for free" — the pricing page heading.

Page: pricing. Selector: `pricing h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1216 x 47.03 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arizona 48px/47.04px 400 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### faq

FAQ item. A pricing FAQ row if the page ships one.

Page: pricing. Selector: `faq item`. States: .

Not found on the page at capture time.

#### plan-includes

Plan feature row. A checkmarked "Includes:" feature row inside a plan card.

Page: pricing. Selector: `plan includes row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 372.66 x 22.39 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/21.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.text-black.underline: ABCDiatype 16px/22.4px 400, #000000, ls -0.32px |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| How | at rest |

Crops: `plan-includes-default.png`.

### Product pages

#### prod-h1

Product headline. The /products/search page heading.

Page: product. Selector: `product h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 850 x 119.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arizona 52px/59.8px 400 |
| Letter spacing | -1.04px |
| Colour | #111827 |
| Transition | none |
| How | at rest |

Crops: `prod-h1-default.png`.

#### prod-code

Code sample. A code block on the product page (the API examples).

Page: product. Selector: `product pre/code`. States: .

Not found on the page at capture time.

#### prod-cta

Product CTA. A product-page call to action; measured never followed.

Page: product. Selector: `product CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90 x 38.5 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #000000 | #1f2937 | = | #1f2937 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 15px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-inter.inline-flex 90.0x38.5 bg #000000 r 4px | a.font-inter.inline-flex 90.0x38.5 bg #1f2937 r 4px | a.font-inter.inline-flex 90.0x38.5 bg #000000 r 4px outline 1px auto #101010 offset 1px | a.font-inter.inline-flex 90.0x38.5 bg #1f2937 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `prod-cta-default.png`, `prod-cta-hover.png`, `prod-cta-focus-visible.png`, `prod-cta-pressed.png`.

#### prod-feature

Feature section. An alternating feature block ("Search the public web and proprietary data through one API") with its framed visual card.

Page: product. Selector: `feature section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 2496 |
| Padding | 96px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.font-serif.text-[2rem]: Arizona 41.6px/45.76px 400, #181818, ls -1.04px |
| Transition | none |
| Icon | 16 x 16, colour #52525b |
| Painted layers | a.inline-flex.items-center 150.0x40.5 bg #ffffff border T:1px solid #09090b @ 0.14 / R:1px solid #09090b @ 0.14 / B:1px solid #09090b @ 0.14 / L:1px solid #09090b @ 0.14 r 4px; div.Illustration_root__NRGQe.flex 620.0x516.0 bg #f3f3f1 image radial-gradient(#18181b @ 0.07 1px, #000000 @ 0 1px); div.absolute.inset-0 520.0x420.0 bg #f3f3f1 image radial-gradient(#18181b @ 0.07 1px, #000000 @ 0 1px); div.Scene_card__Kth0v.shrink-0 496.0x76.0 bg #ffffff border T:1px solid #e4e4e7 / R:1px solid #e4e4e7 / B:1px solid #e4e4e7 / L:1px solid #e4e4e7 r 8px shadow #18181b @ 0.04 0px 1px 2px 0px, #18181b @ 0.14 0px 12px 32px -12px; div.Scene_card__Kth0v.flex 496.0x310.0 bg #ffffff border T:1px solid #e4e4e7 / R:1px solid #e4e4e7 / B:1px solid #e4e4e7 / L:1px solid #e4e4e7 r 8px shadow #18181b @ 0.04 0px 1px 2px 0px, #18181b @ 0.14 0px 12px 32px -12px; div.flex.h-9 494.0x36.0 border B:1px solid #efeff1 |
| Ancestor paint | 1 up main bg #ffffff |
| How | at rest |

Crops: `prod-feature-default.png`.

### Sign in (auth.exa.ai)

#### auth-card

Login card. The "Start building with Exa" sign-in card on auth.exa.ai: heading, Continue-with-Google and Continue-with-email buttons, the e-mail field, SSO link and a code sample — measured, never submitted.

Page: signin. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 98 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype Unlicensed Trial 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | button.jsx-38cf25ff465a5e1d.h-11: ABC Diatype Unlicensed Trial 16px/32px 400, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #99a1af |
| Painted layers | input.jsx-38cf25ff465a5e1d.placeholder:text-gray-400 360.0x44.0 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px; button.jsx-38cf25ff465a5e1d.h-11 360.0x44.0 bg #1f40ed r 4px |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-heading

Login heading. "Start building with Exa".

Page: signin. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300.28 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Arizona Flare 32px/32px 400 |
| Letter spacing | -0.64px |
| Colour | #1a1a1a |
| Transition | none |
| How | at rest |

Crops: `auth-heading-default.png`.

#### auth-google

Google button. The "Continue with Google" OAuth button; measured never pressed.

Page: signin. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 50 | = | = | = |
| Padding | 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e0e0e0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #f9f9f9 | = | #f9f9f9 |
| Box shadow | #89661a @ 0.2 0px 2px 3px -1px | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype Unlicensed Trial 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.jsx-38cf25ff465a5e1d.text-base: ABC Diatype Unlicensed Trial 16px/24px 500, #000000, ls -0.32px | = | = | = |
| Transition | all 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #171717, fill #000000 | = | = | = |
| Painted layers | button.jsx-38cf25ff465a5e1d.relative 360.0x50.0 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px shadow #89661a @ 0.2 0px 2px 3px -1px | button.jsx-38cf25ff465a5e1d.relative 360.0x50.0 bg #f9f9f9 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px shadow #89661a @ 0.2 0px 2px 3px -1px | = | button.jsx-38cf25ff465a5e1d.relative 360.0x50.0 bg #f9f9f9 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px shadow #89661a @ 0.2 0px 2px 3px -1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-google-default.png`, `auth-google-hover.png`, `auth-google-focus-visible.png`, `auth-google-pressed.png`.

#### auth-email-btn

Email button. The "Continue with email" button; measured never pressed.

Page: signin. Selector: `Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 44 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 4px | = | - | = |
| Background | #1f40ed | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ABC Diatype Unlicensed Trial 16px/32px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Opacity | 0.5 | = | - | = |
| Cursor | default | = | - | = |
| Painted layers | button.jsx-38cf25ff465a5e1d.h-11 360.0x44.0 bg #1f40ed r 4px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `auth-email-btn-default.png`, `auth-email-btn-hover.png`, `auth-email-btn-pressed.png`.

#### auth-email

Email field. The "Email" input; focused and typed into then cleared — never submitted.

Page: signin. Selector: `login email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 360 x 44 | = | = |
| Padding | 12px 16px 12px 40px | = | = |
| Border | 1px solid #e0e0e0 | 1px solid #1f40ed | 1px solid #1f40ed |
| Radius | 4px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | ABC Diatype Unlicensed Trial 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #171717 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #99a1af, opacity 1 | = | = |
| Painted layers | input.jsx-38cf25ff465a5e1d.placeholder:text-gray-400 360.0x44.0 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px | input.jsx-38cf25ff465a5e1d.placeholder:text-gray-400 360.0x44.0 border T:1px solid #1f40ed / R:1px solid #1f40ed / B:1px solid #1f40ed / L:1px solid #1f40ed r 4px | input.jsx-38cf25ff465a5e1d.placeholder:text-gray-400 360.0x44.0 border T:1px solid #1f40ed / R:1px solid #1f40ed / B:1px solid #1f40ed / L:1px solid #1f40ed r 4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `auth-email-default.png`, `auth-email-focused.png`, `auth-email-filled.png`.

#### auth-code

Code sample. The exa.search() snippet the login page shows beside the card.

Page: signin. Selector: `login code sample`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 336 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Mono 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Geist Mono 14px/20px 400, #ffffff |
| Transition | none |
| Ancestor paint | 1 up div.flex.h-full bg #27282c; 2 up div.relative.z-20 bg #ffffff @ 0.6 shadow #000000 @ 0.02 0px 45px 18px 0px, #000000 @ 0.06 0px 25px 15px 0px, #000000 @ 0.11 0px 11px 11px 0px, #000000 @ 0.13 0px 3px 6px 0px |
| How | at rest |

Crops: `auth-code-default.png`.

### Docs (exa.ai/docs) (light)

#### docs-sidebar

Docs sidebar. The docs left rail: search, the theme control and the nav tree (Overview / Get Started / Search / Agent / Other APIs).

Page: docs. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 844 |
| Padding | 0px |
| Border | T: none; R: 1px solid #eeeff5; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #707177 |
| Text node | span.docs-sidebar-search-label: Inter 14px/14px 400, #4f4f57 |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #4f4f57 |
| Painted layers | nav.hidden.sticky 288.0x844.0 border R:1px solid #eeeff5; button.docs-sidebar-search 267.0x36.0 border T:1px solid #09090b @ 0.14 / R:1px solid #09090b @ 0.14 / B:1px solid #09090b @ 0.14 / L:1px solid #09090b @ 0.14 r 6px; kbd 27.0x18.0 bg #09090b @ 0.05 r 4px; kbd 18.0x18.0 bg #09090b @ 0.05 r 4px; a.group.flex 267.0x32.0 bg #f3f3f4 r 6px; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #eeeff5 |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-logo

Docs logo. The exa mark at the top of the docs chrome.

Page: docs. Selector: `img.nav-logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61.39 x 19.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #707177 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `docs-logo-default.png`.

#### docs-search

Search button. The "Search Ctrl K" field-styled button in the docs rail; measured, never opened.

Page: docs. Selector: `button.docs-sidebar-search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 36 | = | = | 258.99 x 34.92 |
| Padding | 0px 10px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #09090b @ 0.14 | 1px solid #09090b @ 0.28 | 1px solid #09090b @ 0.28 | 1px solid #09090b @ 0.28 |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #09090b @ 0.07 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/14px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4f4f57 | #0b0b0d | = | #0b0b0d |
| Text node | span.docs-sidebar-search-label: Inter 14px/14px 400, #4f4f57 | span.docs-sidebar-search-label: Inter 14px/14px 400, #0b0b0d | = | span.docs-sidebar-search-label: Inter 14px/14px 400, #0b0b0d |
| Transition | color, border-color, transform 0.22s, 0.22s, 0.1s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #4f4f57 | 16 x 16, colour #0b0b0d | = | 15.52 x 15.52, colour #0b0b0d |
| Painted layers | button.docs-sidebar-search 267.0x36.0 border T:1px solid #09090b @ 0.14 / R:1px solid #09090b @ 0.14 / B:1px solid #09090b @ 0.14 / L:1px solid #09090b @ 0.14 r 6px; kbd 27.0x18.0 bg #09090b @ 0.05 r 4px; kbd 18.0x18.0 bg #09090b @ 0.05 r 4px | button.docs-sidebar-search 267.0x36.0 border T:1px solid #09090b @ 0.28 / R:1px solid #09090b @ 0.28 / B:1px solid #09090b @ 0.28 / L:1px solid #09090b @ 0.28 r 6px; kbd 27.0x18.0 bg #09090b @ 0.05 r 4px; kbd 18.0x18.0 bg #09090b @ 0.05 r 4px | button.docs-sidebar-search 267.0x36.0 border T:1px solid #09090b @ 0.28 / R:1px solid #09090b @ 0.28 / B:1px solid #09090b @ 0.28 / L:1px solid #09090b @ 0.28 r 6px shadow #09090b @ 0.07 0px 0px 0px 3px; kbd 27.0x18.0 bg #09090b @ 0.05 r 4px; kbd 18.0x18.0 bg #09090b @ 0.05 r 4px | button.docs-sidebar-search 259.0x34.9 border T:1px solid #09090b @ 0.28 / R:1px solid #09090b @ 0.28 / B:1px solid #09090b @ 0.28 / L:1px solid #09090b @ 0.28 r 6px; kbd 26.2x17.5 bg #09090b @ 0.05 r 4px; kbd 17.5x17.5 bg #09090b @ 0.05 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-theme-btn

Theme button. The docs theme preference button; measured, never opened (the dark capture used a prefers-color-scheme context instead).

Page: docs. Selector: `theme button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #26272c @ 0.04 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #1840ed offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0c11 @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 16, colour #505157, fill #000000 | 14 x 16, colour #26272c, fill #000000 | = | 14 x 16, colour #26272c, fill #000000 |
| Painted layers | button.group.disabled:pointer-events-none 30.0x30.0 bg #26272c @ 0.04 r 9999px | = | button.group.disabled:pointer-events-none 30.0x30.0 bg #26272c @ 0.04 r 9999px outline 1px auto #1840ed offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-nav-item

Nav item. A docs sidebar link; measured, never followed.

Page: docs. Selector: `sidebar nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 32 | = | = | = |
| Padding | 6px 12px 6px 16px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f3f3f4 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #1840ed offset -2px | = |
| Font | Inter 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 600, #000000 | = | = | = |
| Transition | background-color, color 0.15s, 0.15s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 267.0x32.0 bg #f3f3f4 r 6px | = | a.group.flex 267.0x32.0 bg #f3f3f4 r 6px outline 1px auto #1840ed offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-nav-item-default.png`, `docs-nav-item-hover.png`, `docs-nav-item-focus-visible.png`, `docs-nav-item-pressed.png`.

#### docs-h1

Page heading. The doc page's h1 ("Start building with Exa").

Page: docs. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310.28 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 32px/42px 500 |
| Letter spacing | -0.64px |
| Colour | #17181e |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-para

Body paragraph. A body paragraph in the doc.

Page: docs. Selector: `docs paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16.6667px/28px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.6 |
| Transition | none |
| How | at rest |

Crops: `docs-para-default.png`.

#### docs-link

Body link. A link inside the doc body; measured, never followed.

Page: docs. Selector: `docs body link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 226 x 41.59 | = | = | = |
| Padding | 10px 12px | = | = | = |
| Border | 1px solid #71665b @ 0.08 | 1px solid #110f0d @ 0.08 | = | 1px solid #110f0d @ 0.08 |
| Radius | 10px | = | = | = |
| Background | #f8f8f9 | #f3f3f4 | = | #f3f3f4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #1840ed offset 1px | = |
| Font | Inter 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.6 | #000000 @ 0.9 | = | #000000 @ 0.9 |
| Text node | span: Inter 14px/19.6px 400, #000000 @ 0.6 | span: Inter 14px/19.6px 400, #000000 @ 0.9 | = | span: Inter 14px/19.6px 400, #000000 @ 0.9 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.link.docs-home-llms 226.0x41.6 bg #f8f8f9 border T:1px solid #71665b @ 0.08 / R:1px solid #71665b @ 0.08 / B:1px solid #71665b @ 0.08 / L:1px solid #71665b @ 0.08 r 10px | a.link.docs-home-llms 226.0x41.6 bg #f3f3f4 border T:1px solid #110f0d @ 0.08 / R:1px solid #110f0d @ 0.08 / B:1px solid #110f0d @ 0.08 / L:1px solid #110f0d @ 0.08 r 10px | a.link.docs-home-llms 226.0x41.6 bg #f8f8f9 border T:1px solid #71665b @ 0.08 / R:1px solid #71665b @ 0.08 / B:1px solid #71665b @ 0.08 / L:1px solid #71665b @ 0.08 r 10px outline 1px auto #1840ed offset 1px | a.link.docs-home-llms 226.0x41.6 bg #f3f3f4 border T:1px solid #110f0d @ 0.08 / R:1px solid #110f0d @ 0.08 / B:1px solid #110f0d @ 0.08 / L:1px solid #110f0d @ 0.08 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-link-default.png`, `docs-link-hover.png`, `docs-link-focus-visible.png`, `docs-link-pressed.png`.

#### docs-code

Code block. A code block or inline code span in the doc (Paper Mono).

Page: docs. Selector: `docs pre/code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 685 x 269.13 |
| Padding | 17px 19px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | GeistMono 14px/19.6px 400 |
| Letter spacing | -0.14px |
| Colour | #1f2328 |
| Text node | span: GeistMono 14px/19.6px 400, #cf222e, ls -0.14px |
| Transition | none |
| Painted layers | pre.shiki.shiki-themes 685.0x269.1 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; code 647.0x235.1 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 173.0x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 31.5x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 62.9x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 47.2x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.font-mono.whitespace-pre shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0a0c11; 2 up div.min-w-full!.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0a0c11; 3 up div.size-full.rounded-[inherit] shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0a0c11 |
| How | at rest |

Crops: `docs-code-default.png`.

#### docs-tab

Code-language tab. A Python/JavaScript/cURL language tab in the docs; local toggle only.

Page: docs. Selector: `docs language tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43 x 18 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 13px/18px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0b0b0d | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `docs-tab-default.png`, `docs-tab-hover.png`, `docs-tab-pressed.png`.

#### docs-cta

CTA banner. The blue "Add Exa to your agent" banner with Get-Started and Get-API-Key actions — the actions measured, never followed.

Page: docs. Selector: `docs CTA banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 224.92 x 65.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.docs-home-quickstart-title: ABCDiatype 24px/42px 500, #ffffff, ls -0.48px |
| Transition | none |
| Ancestor paint | 1 up div.docs-home-quickstart bg #002f96 |
| How | at rest |

Crops: `docs-cta-default.png`.

#### docs-assistant

Assistant field. The "Ask a question…" assistant input; focused and typed into then cleared — never sent.

Page: docs. Selector: `textarea.chat-assistant-input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 54 x 50 | = | = |
| Padding | 10px 40px 0px 14px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #17181e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #505157, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "what is neural search", then deleted; nothing sent |

Crops: none.

#### docs-topbar-cta

Topbar CTA. The "API Dashboard" button in the docs topbar; measured, never followed.

Page: docs. Selector: `#topbar-cta-button a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 36 | = | = | 134.83 x 34.92 |
| Padding | 8px 8px 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #1840ed offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #707177 | = | = | = |
| Text node | span.text-white: Inter 14px/20px 500, #ffffff | = | = | = |
| Transition | transform 0.1s cubic-bezier(0.2, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #ffffff @ 0.9, fill #000000 | = | = | 11.64 x 11.64, colour #ffffff @ 0.9, fill #000000 |
| Painted layers | span.absolute.inset-0 139.0x36.0 bg #000000 r 6px | = | a.group.pl-3 139.0x36.0 outline 1px auto #1840ed offset 1px; span.absolute.inset-0 139.0x36.0 bg #000000 r 6px | span.absolute.inset-0 134.8x34.9 bg #000000 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `docs-topbar-cta-default.png`, `docs-topbar-cta-hover.png`, `docs-topbar-cta-focus-visible.png`, `docs-topbar-cta-pressed.png`.

### Docs (exa.ai/docs) (dark)

#### d-docs-sidebar

Docs sidebar. The docs left rail: search, the theme control and the nav tree (Overview / Get Started / Search / Agent / Other APIs).

Page: docsdark. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 844 |
| Padding | 0px |
| Border | T: none; R: 1px solid #ffffff @ 0.1; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #9fa0a5 |
| Text node | span.docs-sidebar-search-label: Inter 14px/14px 400, #bababf |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #bababf |
| Painted layers | nav.hidden.sticky 288.0x844.0 border R:1px solid #ffffff @ 0.1; button.docs-sidebar-search 267.0x36.0 border T:1px solid #fafafa @ 0.16 / R:1px solid #fafafa @ 0.16 / B:1px solid #fafafa @ 0.16 / L:1px solid #fafafa @ 0.16 r 6px; kbd 27.0x18.0 bg #fafafa @ 0.08 r 4px; kbd 18.0x18.0 bg #fafafa @ 0.08 r 4px; a.group.flex 267.0x32.0 bg #ffffff @ 0.08 r 6px; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1 |
| How | at rest |

Crops: `d-docs-sidebar-default.png`.

#### d-docs-logo

Docs logo. The exa mark at the top of the docs chrome.

Page: docsdark. Selector: `img.nav-logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61.39 x 19.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #9fa0a5 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `d-docs-logo-default.png`.

#### d-docs-search

Search button. The "Search Ctrl K" field-styled button in the docs rail; measured, never opened.

Page: docsdark. Selector: `button.docs-sidebar-search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 36 | = | = | 258.99 x 34.92 |
| Padding | 0px 10px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #fafafa @ 0.16 | 1px solid #fafafa @ 0.32 | 1px solid #fafafa @ 0.32 | 1px solid #fafafa @ 0.32 |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #fafafa @ 0.09 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/14px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #bababf | #f5f5f6 | = | #f5f5f6 |
| Text node | span.docs-sidebar-search-label: Inter 14px/14px 400, #bababf | span.docs-sidebar-search-label: Inter 14px/14px 400, #f5f5f6 | = | span.docs-sidebar-search-label: Inter 14px/14px 400, #f5f5f6 |
| Transition | color, border-color, transform 0.22s, 0.22s, 0.1s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #bababf | 16 x 16, colour #f5f5f6 | = | 15.52 x 15.52, colour #f5f5f6 |
| Painted layers | button.docs-sidebar-search 267.0x36.0 border T:1px solid #fafafa @ 0.16 / R:1px solid #fafafa @ 0.16 / B:1px solid #fafafa @ 0.16 / L:1px solid #fafafa @ 0.16 r 6px; kbd 27.0x18.0 bg #fafafa @ 0.08 r 4px; kbd 18.0x18.0 bg #fafafa @ 0.08 r 4px | button.docs-sidebar-search 267.0x36.0 border T:1px solid #fafafa @ 0.32 / R:1px solid #fafafa @ 0.32 / B:1px solid #fafafa @ 0.32 / L:1px solid #fafafa @ 0.32 r 6px; kbd 27.0x18.0 bg #fafafa @ 0.08 r 4px; kbd 18.0x18.0 bg #fafafa @ 0.08 r 4px | button.docs-sidebar-search 267.0x36.0 border T:1px solid #fafafa @ 0.32 / R:1px solid #fafafa @ 0.32 / B:1px solid #fafafa @ 0.32 / L:1px solid #fafafa @ 0.32 r 6px shadow #fafafa @ 0.09 0px 0px 0px 3px; kbd 27.0x18.0 bg #fafafa @ 0.08 r 4px; kbd 18.0x18.0 bg #fafafa @ 0.08 r 4px | button.docs-sidebar-search 259.0x34.9 border T:1px solid #fafafa @ 0.32 / R:1px solid #fafafa @ 0.32 / B:1px solid #fafafa @ 0.32 / L:1px solid #fafafa @ 0.32 r 6px; kbd 26.2x17.5 bg #fafafa @ 0.08 r 4px; kbd 17.5x17.5 bg #fafafa @ 0.08 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `d-docs-search-default.png`, `d-docs-search-hover.png`, `d-docs-search-focus-visible.png`, `d-docs-search-pressed.png`.

#### d-docs-theme-btn

Theme button. The docs theme preference button; measured, never opened (the dark capture used a prefers-color-scheme context instead).

Page: docsdark. Selector: `theme button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #5f7cff offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 16, colour #cecfd5, fill #000000 | 14 x 16, colour #eeeff5, fill #000000 | = | 14 x 16, colour #eeeff5, fill #000000 |
| Painted layers | button.group.disabled:pointer-events-none 30.0x30.0 bg #ffffff @ 0.1 r 9999px | = | button.group.disabled:pointer-events-none 30.0x30.0 bg #ffffff @ 0.1 r 9999px outline 1px auto #5f7cff offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-theme-btn-default.png`, `d-docs-theme-btn-hover.png`, `d-docs-theme-btn-focus-visible.png`, `d-docs-theme-btn-pressed.png`.

#### d-docs-nav-item

Nav item. A docs sidebar link; measured, never followed.

Page: docsdark. Selector: `sidebar nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 32 | = | = | = |
| Padding | 6px 12px 6px 16px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff @ 0.08 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #5f7cff offset -2px | = |
| Font | Inter 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f5f5f6 | = | = | = |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 600, #f5f5f6 | = | = | = |
| Transition | background-color, color 0.15s, 0.15s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 267.0x32.0 bg #ffffff @ 0.08 r 6px | = | a.group.flex 267.0x32.0 bg #ffffff @ 0.08 r 6px outline 1px auto #5f7cff offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-nav-item-default.png`, `d-docs-nav-item-hover.png`, `d-docs-nav-item-focus-visible.png`, `d-docs-nav-item-pressed.png`.

#### d-docs-h1

Page heading. The doc page's h1 ("Start building with Exa").

Page: docsdark. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310.28 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 32px/42px 500 |
| Letter spacing | -0.64px |
| Colour | #dfe0e5 |
| Transition | none |
| How | at rest |

Crops: `d-docs-h1-default.png`.

#### d-docs-para

Body paragraph. A body paragraph in the doc.

Page: docsdark. Selector: `docs paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16.6667px/28px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.6 |
| Transition | none |
| How | at rest |

Crops: `d-docs-para-default.png`.

#### d-docs-link

Body link. A link inside the doc body; measured, never followed.

Page: docsdark. Selector: `docs body link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 226 x 41.59 | = | = | = |
| Padding | 10px 12px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.14 | = | 1px solid #ffffff @ 0.14 |
| Radius | 10px | = | = | = |
| Background | #ffffff @ 0.03 | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #5f7cff offset 1px | = |
| Font | Inter 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.72 | #ffffff | = | #ffffff |
| Text node | span: Inter 14px/19.6px 400, #ffffff @ 0.72 | span: Inter 14px/19.6px 400, #ffffff | = | span: Inter 14px/19.6px 400, #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.link.docs-home-llms 226.0x41.6 bg #ffffff @ 0.03 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 10px | a.link.docs-home-llms 226.0x41.6 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.14 / R:1px solid #ffffff @ 0.14 / B:1px solid #ffffff @ 0.14 / L:1px solid #ffffff @ 0.14 r 10px | a.link.docs-home-llms 226.0x41.6 bg #ffffff @ 0.03 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 10px outline 1px auto #5f7cff offset 1px | a.link.docs-home-llms 226.0x41.6 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.14 / R:1px solid #ffffff @ 0.14 / B:1px solid #ffffff @ 0.14 / L:1px solid #ffffff @ 0.14 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-link-default.png`, `d-docs-link-hover.png`, `d-docs-link-focus-visible.png`, `d-docs-link-pressed.png`.

#### d-docs-code

Code block. A code block or inline code span in the doc (Paper Mono).

Page: docsdark. Selector: `docs pre/code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 685 x 269.13 |
| Padding | 17px 19px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | GeistMono 14px/19.6px 400 |
| Letter spacing | -0.14px |
| Colour | #d4d4d4 |
| Text node | span: GeistMono 14px/19.6px 400, #c586c0, ls -0.14px |
| Transition | none |
| Painted layers | pre.shiki.shiki-themes 685.0x269.1 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; code 647.0x235.1 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 173.0x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 31.5x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 62.9x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 47.2x18.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.font-mono.whitespace-pre shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f3f4fa; 2 up div.min-w-full!.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f3f4fa; 3 up div.size-full.rounded-[inherit] shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f3f4fa |
| How | at rest |

Crops: `d-docs-code-default.png`.

#### d-docs-tab

Code-language tab. A Python/JavaScript/cURL language tab in the docs; local toggle only.

Page: docsdark. Selector: `docs language tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43 x 18 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 13px/18px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #f5f5f6 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `d-docs-tab-default.png`, `d-docs-tab-hover.png`, `d-docs-tab-pressed.png`.

#### d-docs-cta

CTA banner. The blue "Add Exa to your agent" banner with Get-Started and Get-API-Key actions — the actions measured, never followed.

Page: docsdark. Selector: `docs CTA banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 224.92 x 65.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.docs-home-quickstart-title: ABCDiatype 24px/42px 500, #ffffff, ls -0.48px |
| Transition | none |
| Ancestor paint | 1 up div.docs-home-quickstart bg #002f96 |
| How | at rest |

Crops: `d-docs-cta-default.png`.

#### d-docs-assistant

Assistant field. The "Ask a question…" assistant input; focused and typed into then cleared — never sent.

Page: docsdark. Selector: `textarea.chat-assistant-input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 54 x 50 | = | = |
| Padding | 10px 40px 0px 14px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #eeeff5 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #cecfd5, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "what is neural search", then deleted; nothing sent |

Crops: none.

#### d-docs-topbar-cta

Topbar CTA. The "API Dashboard" button in the docs topbar; measured, never followed.

Page: docsdark. Selector: `#topbar-cta-button a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 36 | = | = | 134.83 x 34.92 |
| Padding | 8px 8px 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #5f7cff offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9fa0a5 | = | = | = |
| Text node | span.text-white: Inter 14px/20px 500, #ffffff | = | = | = |
| Transition | transform 0.1s cubic-bezier(0.2, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #ffffff @ 0.9, fill #000000 | = | = | 11.64 x 11.64, colour #ffffff @ 0.9, fill #000000 |
| Painted layers | span.absolute.inset-0 139.0x36.0 bg #000000 r 6px | = | a.group.pl-3 139.0x36.0 outline 1px auto #5f7cff offset 1px; span.absolute.inset-0 139.0x36.0 bg #000000 r 6px | span.absolute.inset-0 134.8x34.9 bg #000000 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `d-docs-topbar-cta-default.png`, `d-docs-topbar-cta-hover.png`, `d-docs-topbar-cta-focus-visible.png`, `d-docs-topbar-cta-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The top bar at 390: wordmark, hamburger and the Sign-up action.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #4b5563 |
| Painted layers | div.header.sticky 390.0x64.0 bg #ffffff; nav.font-inter.h-16 390.0x64.0 bg #ffffff; div.hidden.fixed 0.0x0.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; span.inline-flex.items-center 0.0x0.0 bg #dbeafe r 9999px; div.flex.shrink-0 0.0x0.0 bg #ffffff border T:1px solid #f3f4f6; a.signed-out-only.block 0.0x0.0 bg #ffffff border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 4px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hamburger

Hamburger. The mobile nav toggle; opened to reveal the drawer — a local toggle, its links never followed.

Page: mobile. Selector: `Toggle menu button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = | = |
| Padding | 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #f3f4f6 | = | #f3f4f6 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #4b5563 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.rounded-lg.p-1.5 32.0x32.0 bg #f3f4f6 r 8px | = | button.rounded-lg.p-1.5 32.0x32.0 bg #f3f4f6 r 8px | = |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-focus-visible.png`, `m-hamburger-pressed.png`, `m-hamburger-opened.png`.

#### m-drawer

Mobile nav drawer. The full-height nav the hamburger opens (div.fixed inset-x-0 inside the header).

Page: mobile. Selector: `mobile nav drawer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.font-['ABCDiatype'].text-base: ABCDiatype 16px/24px 500, #111827, ls -0.32px |
| Transition | none |
| Icon | 20 x 20, colour #6b7280 |
| Painted layers | div.block.fixed 390.0x844.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; span.inline-flex.items-center 78.1x20.0 bg #dbeafe r 9999px; div.flex.shrink-0 390.0x143.0 bg #ffffff border T:1px solid #f3f4f6; a.signed-out-only.block 166.0x50.0 bg #ffffff border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 4px; a.block.flex-1 164.0x50.0 bg #000000 r 4px; a.block.rounded 342.0x48.0 bg #f3f4f6 r 4px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Hero headline (mobile). "The world's data for AI agents" at 390 wide.

Page: mobile. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arizona 38.4px/42px 400 |
| Letter spacing | -1.152px |
| Colour | #111827 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-demo-textarea

Demo query field (mobile). The demo query box at 390; focused and typed into then restored — the preview was never run.

Page: mobile. Selector: `demo textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 330 x 24 | = | 330 x 48 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | ABCDiatype 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.4, opacity 1 | = | = |
| Painted layers | textarea.block.w-full 330.0x24.0 outline 2px solid #000000 @ 0 offset 2px | = | textarea.block.w-full 330.0x48.0 outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 2 up div bg #ffffff shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.08 | 2 up div bg #ffffff shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.12 | 2 up div bg #ffffff shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #000000 @ 0.12 |
| How | at rest | clicked into the field | typed "latest research on fusion", then deleted; nothing sent |

Crops: `m-demo-textarea-default.png`, `m-demo-textarea-focused.png`, `m-demo-textarea-filled.png`.

## Transitions declared in the readable stylesheets

exa.ai, auth.exa.ai and exa.ai/docs serve their stylesheets same-origin and read through the CSSOM, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`, `color var(--motion-duration) var(--motion-easing-standard)`

- docsdark: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`, `color var(--motion-duration) var(--motion-easing-standard)`

- home: `width var(--resize-dur) var(--resize-ease),height var(--resize-dur) var(--resize-ease)`, `left var(--resize-dur) var(--resize-ease)`, `none`, `grid-template-rows var(--acc-collapse) var(--acc-ease)`, `grid-template-rows var(--acc-expand) var(--acc-ease)`, `opacity var(--acc-collapse) var(--acc-ease),filter var(--acc-collapse) var(--acc-ease)`, `opacity var(--acc-expand) var(--acc-ease),filter var(--acc-expand) var(--acc-ease)`, `transform var(--acc-chevron) var(--acc-ease)`, `background-color 0.15s`, `transform var(--text-swap-dur) var(--text-swap-ease),             filter var(--text-swap-dur) var(--text-swap-ease),             opacity var(--text-swap-dur) var(--text-swap-ease)`

- pricing: `width var(--resize-dur) var(--resize-ease),height var(--resize-dur) var(--resize-ease)`, `left var(--resize-dur) var(--resize-ease)`, `none`, `grid-template-rows var(--acc-collapse) var(--acc-ease)`, `grid-template-rows var(--acc-expand) var(--acc-ease)`, `opacity var(--acc-collapse) var(--acc-ease),filter var(--acc-collapse) var(--acc-ease)`, `opacity var(--acc-expand) var(--acc-ease),filter var(--acc-expand) var(--acc-ease)`, `transform var(--acc-chevron) var(--acc-ease)`

- product: `width var(--resize-dur) var(--resize-ease),height var(--resize-dur) var(--resize-ease)`, `left var(--resize-dur) var(--resize-ease)`, `none`, `grid-template-rows var(--acc-collapse) var(--acc-ease)`, `grid-template-rows var(--acc-expand) var(--acc-ease)`, `opacity var(--acc-collapse) var(--acc-ease),filter var(--acc-collapse) var(--acc-ease)`, `opacity var(--acc-expand) var(--acc-ease),filter var(--acc-expand) var(--acc-ease)`, `transform var(--acc-chevron) var(--acc-ease)`

- signin: none
