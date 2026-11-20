# Components

Measured on the attached preview browser on 2026-11-19. Element crops were not cut because `preview_snapshot` did not produce frames.

| Component | Where | Values |
|---|---|---|
| Button, brand | LOG IN and START BUILDING on parallel.ai | Fill `#fb631b`, label `#ffffff`, 13px FT System Mono, uppercase, letter-spacing 0.16px, radius 4px, height 34px, padding 9px 16px 7px. Transition 150ms `cubic-bezier(0, 0, 0.2, 1)`. Class includes `hover:bg-brand-hover` (`#f4793f`) and `active:scale-[0.98]`. A synthetic mouseover did not change the computed fill. |
| Button, ink | CONTACT and TRY MONITOR | Fill `#434343`, same type and radius as the brand button. CONTACT transition duration was 400ms. |
| Button, ghost | CONTACT US and START FOR FREE | Fill `#ffffff`, ink `#181818`, border 1px `#d6d6d6`, radius 4px, height 34px. |
| Link | Learn more. in the announcement | `#0d6ea5`, 13px Gerstner Programm. Focus outline `#0d6ea5` auto 1px, offset 1px. |
| Badge | POPULAR on pricing | Fill `#fb631b`, label white, 11px mono, uppercase, height 18px, padding 0 7px 1px, radius 2px. FOR GROWTH uses fill `#181818`. |
| Text field | Login email | Fill `#121212`, text white, placeholder `#a3a3a3`, border 1px `#404040`, radius 6px, height 40px, width 360px, 14px. Not submitted. |
| Button, login secondary | Continue with Google, Continue with SSO | Same box as the email field, label white, weight 500. Not clicked. |
| Button, login primary | Continue with email | Fill white, ink `#121212`, radius 6px, height 40px, weight 500. Not clicked. |
| Search | Docs Search... | White fill, ink `#777370`, radius 6px, height 36px, 14px Gerstner Programm. |
| Nav item, selected | Docs Overview | Ink `#fb631b`, tinted orange background, radius 6px, height 36px, 14px. |

## Gaps

Icon button, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, and a validation error were not on the signed-out pages that loaded. The pricing columns are transparent over the page, so there is no raised card fill to record. Hover and pressed fills were not held. No loading state was shown.
