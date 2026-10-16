## Gaps

What could not be captured, and why. Updated 2026-10-17; rows the recapture closed are gone (light theme for the quit dialog, the signed-in phone width, the Settings Premium tab, and button3d hover and pressed, which are now measured).

| Gap | Reason | What stands in |
|---|---|---|
| Toasts | Sonner is mounted, but no look-only action fires a toast; starring a topic or saving a setting would change the account | none |
| Select, checkbox | No reached screen renders one; the stylesheet defines `select-icon`, `checkbox` and `checkbox-indicator` slots | n/a |
| Form validation error | Errors appear only after a submit, and no form was submitted (the login field shows nothing on blur; clearing a settings field was not attempted because it could save) | the stylesheet's invalid rules: `outline-color: border.danger-primary` and `text.danger-primary` |
| In-app paywall | The onboarding paywall auto-advanced in 2026-09 | the same Free vs Premium table on `/subscribe/`, measured headless in both themes |
| Koji prompt suggestion cards | Drawn on a `<canvas>`, so there is no DOM to read | values estimated from screenshot |
| Lesson interactive in the 2026-10 copies | `<custom-interactive>` renders in a shadow root, which a DOM copy does not carry, so lesson copies show an empty frame | the 2026-09 lesson screenshots and `component.lesson.*` tokens |
| Light theme: onboarding, promo, plan, learning path | Onboarding runs once per account | tokens cover both themes; the components reappear on light pages |
| Lesson completion screen, lesson plan steps | Not reached on a new account without answering lessons | none |
| Focus on menu items, segments, text areas, cards, header tabs | The product draws no focus ring there: menu items show `bg.hover`, header tabs and cards fall back to the browser's own ring, segments and the Koji text area show nothing | recorded as measured in the specs |
| Duration tokens | Panda's `trs-dur_fast` and `normal` compile to invalid CSS in production, so no duration variable exists | `duration` lists the durations actually used in transitions |
| High-contrast theme | The product has none; only Auto, Light, Dark and Reduce motion | n/a |
| Proprietary fonts | CoFo Brilliant, CoFo Robert, CoFo Semi Mono are licensed and not committed | the style guide falls back to Figtree and Georgia |
| Legacy pages (`/account/`) | Old Django UI, not on the Panda tokens | documented separately above |
| Cookie banner, bug-report widget | OneTrust and Shake are third party (the lesson's report flag opens Shake's own form) | hidden during capture, not documented |
