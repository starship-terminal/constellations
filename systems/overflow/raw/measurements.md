# Component measurements

Read from overflow.io on 2026-11-21 with tools/capture/public/measure.mjs. Desktop 1440x900 at devicePixelRatio 1. Phone menu at 390x844 at devicePixelRatio 2.

States: hover is a real pointer. focus-visible is Tab after Shift+Tab. pressed is CDP `CSS.forcePseudoState` with hover and active, so no link is followed and no form is submitted.

The cookie bar was hidden. Required only and Allow all were not clicked. The newsletter field was not filled.

Source file: [components-computed.json](components-computed.json).

## States

| Component | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| hero-cta | black fill, white text, 56px, 8px radius | translateY about -2px | Tab landed | CDP active, smaller lift |
| nav-cta | black fill, 48px | lift | Tab landed | CDP active |
| nav-link | black 15px | color #259aef | no colour change | color #124b74 |
| nav-signin | transparent | lift | Tab landed | fill rgba(240,240,242,.5) |
| menu-link | white, 12px radius | fill #f5f5f6 | Tab landed, no colour change | fill #f9f9fa |
| plan-cta | same as hero-cta | lift | Tab landed | CDP active |
| download-mac | class btn-gradient, painted black | lift | Tab landed | CDP active |
| faq-item | white opener | no computed change | focus failed | no computed change |
| demo-link | black 14px | color rgba(0,0,0,.6) | focus failed | no computed change |
| m-menu-button | 22px toggler | no computed change | Tab landed, no colour change | no computed change |
