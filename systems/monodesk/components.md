# MonoDesk components

Public site only, measured signed out on 2026-11-21. The signed-in app was not entered.

| Component | Where | States captured | Values |
|---|---|---|---|
| Button (CTA) | `a.hero-cta-button` on `/` | default, hover crop | height 40px, padding 8px 16px, radius 100px, fill `#d1ff6e`, text `#026232`, Geist 14/500 |
| Link (nav) | `a.header-nav-link` | default | Geist 14/500, color `rgba(255, 255, 255, 0.85)` |
| Link (login) | header Log in, hero Log in | default | header: same as nav. Hero: 16/400 white on a blue pill (sibling paint; the anchor itself is transparent) |
| Text field | help search `input[type=search]` | default, focused (screenshot), filled with the word "planner" then cleared, not submitted | height 48px, radius 100px, white fill, text `#161616` |
| Menu | `.header-nav-dropdown-menu.mega-menu` | opened by hover and click for Creative Pros, Features, More | light panel over the page. Screenshot `home-dark-menu-features.png` |
| Dialog | video modal from "Watch how it works" | open, close control visible | `home-dark-video-dialog.png` |
| Card | help category cards, pricing plan cards, playground tiles | default | help cards are white on a light band. Pricing Pro card has a highlighter outline and a "Most popular" badge |
| Badge | "Most popular" on `/pricing` | default | green chip on the Pro card |
| Accordion | `button.faq-question` | closed, open ("What is MonoDesk?") | `home-dark-faq.png` |
| Icon button | phone `button.hamburger-btn` | default, opened menu | `mobile-home-dark-menu.png`. More is further down the same sheet: `mobile-home-dark-menu-more.png` |
| Table | pricing comparison | collapsed, expanded (`button.ptable-toggle`) | `pricing-dark-table-open.png` |

## Gaps

- Text area, select, checkbox, radio, switch, tabs, tooltip, toast, list row, avatar: not present on the public pages that were opened.
- Disabled, loading, and error states: not shown on the public surface.
- Focus ring: keyboard focus was applied to the search field (screenshot `help-dark-search` was not a separate file; the focused state is in `raw/components-computed.json` for the search input). A designed focus token was not found. Not captured as a token.
- Pressed state of the CTA: a mouse-down was dispatched during measurement and did not change the fill. Recorded as no visible pressed style on that control.
- Signed-in controls (task board, invoice editor, settings): behind `https://app.monodesk.com/login`. Not captured.
