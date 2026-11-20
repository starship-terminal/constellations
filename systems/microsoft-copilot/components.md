# Components

Measured on the public signed-out page at https://copilot.com/ on 2026-11-19, desktop 1440x900, `html[data-cc-theme=dark]` unless a row says otherwise. Crops are 256-colour PNGs. Read values from [tokens.json](tokens.json), not from the crops.

| Component | States | Crop | Values |
|---|---|---|---|
| Button, primary | default, hover, focus-visible, pressed | [button-primary-default.png](components/crops/button-primary-default.png) | `a.newexp-btn-primary-bebop`. Default background `light.background.action` inverted in dark: white `#ffffff`, text `#242424`, 15px semibold, padding 12px 24px, radius `core.radius.lg` (16px), height 50px. Hover goes transparent with a white border and white text, plus the declared lift shadow. Pressed (CDP `active`) is `#3a3a3a`. |
| Button, secondary | default, hover, focus | [button-secondary-default.png](components/crops/button-secondary-default.png) | `button.faq-expand-all`. Transparent face, 2px `#858585` border, radius 8px, padding 12px 24px, 14px semibold. Hover fills white with `#242424` text. |
| Button, download | default, hover | [button-download-default.png](components/crops/button-download-default.png) | `a.module-download-cta`. White face, `#242424` text, radius 10px, padding 10px 14px, height 39px, shadow `0 1px 0 rgba(0,0,0,.12)`. Hover drops the white fill. |
| Tab | default, hover, selected | [tab-selected.png](components/crops/tab-selected.png) | `button.copilotcom-tab`. Pill radius 200px, padding 8px 24px, 15px semibold, height 42px. Selected is white with `#242424` text. Idle is transparent. Hover of an idle tab is `#343434`. |
| Link | default | [link-default.png](components/crops/link-default.png) | `.module-cta` "Go to Chat". 15px, transparent, text `rgba(255,255,255,.87)`, gap 8px, transition `all 200ms ease`. The parent `.module-actions` colour is the lilac `#9e9eff`. |
| Card | default, hover | [card-default.png](components/crops/card-default.png) | `a.module-card`. Background `#1f1f1f`, 1px border `rgba(255,255,255,.282)`, radius 24px. Hover background `#343434`. |
| Accordion | collapsed, expanded | [accordion-collapsed.png](components/crops/accordion-collapsed.png) | `button.faq-question-button`. No radius, white question text. Expanded answer is 16px `rgba(255,255,255,.87)`. |
| Heading | hero, section | [heading-hero.png](components/crops/heading-hero.png) | Hero is Segoe Serif Display, 72px at 1440 (declared `clamp(52px, 5vw, 72px)`), weight 400, colour `rgba(255,255,255,.87)`. Section title is 40px, line-height 48px, letter-spacing -1.2px. |
| Text | hero subtitle | [text-hero-subtitle.png](components/crops/text-hero-subtitle.png) | 21.6px, colour `rgba(255,255,255,.631)`. |
| Nav | default, menu open | [nav-link-default.png](components/crops/nav-link-default.png) | Header is 54px, background `#1f1f1f`, padding-inline about 58px at 1440, Segoe UI 13px. Features menu is `uhf-popout` at `#2b2b2b`. |
| Footer | default | [footer-default.png](components/crops/footer-default.png) | `#1f1f1f` background, `#dedede` text, 14px, top border `rgba(255,255,255,.282)`, padding 24px 58px. |
| Field | default, on the Microsoft sign-in card only | [field-email-default.png](components/crops/field-email-default.png) | `#i0116` on login.microsoftonline.com. 15px Segoe UI Webfont, padding 6px 10px 6px 0, height 36px, transparent background, no radius. Nothing was typed. |
| Button, Next | default, Microsoft account chrome | [button-next-default.png](components/crops/button-next-default.png) | `#idSIButton9`. Background `#0067b8`, white text, 15px, padding 4px 12px, height 32px, radius 0. Not a Copilot marketing button. |

## Gaps

- Chat composer, message list, sidebar, and the signed-in app were not reached. Sign-in redirects to a Microsoft account page that asks for a personal Microsoft account. The capture inbox was not used to create one.
- Checkbox, radio, switch, select, textarea, toast, dialog, tooltip, table, avatar, and badge do not appear on the public signed-out page.
- Disabled and error states are declared for the primary button (`aria-disabled`, colour `#858585`) and were not shown live.
- Loading state was not shown.
- The link hover crop was not saved. The download and secondary buttons have hover crops.
- Light theme: `prefers-color-scheme: light` cleared `data-cc-theme` and the primary button computed black with white text. A full light component pass was not measured.
- Focus ring: the light sheet declares `outline: #000 solid 2px` on `.copilotcom-tab:focus-visible`. The dark focus crop of the primary button did not show a separate outline.
