# Components

Measured on 2026-11-19 from computed styles. No component crops: the preview browser did not produce screenshot frames.

| Component | Where | States read | Values |
|---|---|---|---|
| Button, primary | Nav "Start for Free", hero "Book a Demo", pricing "Buy Now" | Default. Hover is a stylesheet rule, not a held state | Background #5727e7, text white, radius 12px, nav height 50px, hero and Buy Now height 48px. Hover rule sets background #000 |
| Button, secondary | Nav "Login", "Book a Demo" | Default. Hover is a stylesheet rule | Transparent fill, 1px black border, black text, radius 12px, height 50px. Hover rule sets fill #5727e7 and white text |
| Button, outline | Hero "Try it Free" | Default. Hover is a stylesheet rule | White fill, 1px black border, radius 12px, height 48px. Hover rule sets fill and border to --primary-1 |
| Button, continue | Login "Continue" | Default. Not clicked | Fill #5b5bf5, white text, radius 12px, height 56px, width 360px. Not disabled |
| OAuth button | Login Google and Apple | Default. Not clicked | Google: transparent, 1px #d2d2d7 border, ink #1d1d1f, height 48px. Apple: black fill, white text, height 48px |
| Link | Header nav, newsbar, reCAPTCHA legal | Default | Header links are black, 18px, weight 700. Newsbar link is white on #5727e7. reCAPTCHA links are #2a96fc at 12px |
| Text field | Login email | Focused (focus() was called). Unfocused border was not isolated. Empty, not submitted | Height 48px, radius 12px, padding 4px 16px, border 1px #5727e7, text #060612, placeholder "example@mail.com" |
| Text area | Not present on the captured pages | | |
| Select | Not present. Pricing uses tabs, not a native select | | |
| Checkbox | Not present | | |
| Radio | Not present | | |
| Switch | Pricing Monthly / Yearly control | In the DOM with height 0 at rest. Not toggled | Declared tag styles only: white fill, 1px #16a34a border, radius 6px, padding 8px 16px |
| Tabs | Pricing product tabs | Selected and idle | Selected: fill #5727e7, white text, radius 12px, height 56px, shadow 0 1px 2px rgba(0,0,0,0.06). Idle: white fill, black text. Community tab fill #ffb7c5 |
| Menu | Header dropdowns | Closed. A synthetic click left `.w-dropdown-list` at display none, background rgb(221, 221, 221) | Open menu colours were not read |
| Tooltip | Not present | | |
| Dialog | Book a Demo, a Tally modal hash | Not opened | --modal-bg is #000000b3 on :root. Not applied to an open dialog |
| Toast | Not present | | |
| Card | Pricing plan card `.pricing-tab-item` | Default | White, 1px #e5e7eb border, radius 12px, padding 16px, width 397px at 1440 and 350px at 390 |
| List row | Not present on these pages | | |
| Table | Not present | | |
| Avatar | Not present | | |
| Badge | Header "New" tag | Default | Fill #5727e7, white text, radius 8px, padding 6px 10px, 14px type |

## Gaps

- Hover, pressed, disabled, loading, and error were not held on a live element. Primary and secondary hover colours come from stylesheet rules.
- The email field was already focused when its border was read, so the resting border is a gap.
- No validation error was triggered. The form was not submitted.
- No dark theme was applied. Login stylesheets declare `--dash-bg` light `#ffffff` and dark `#0e0f11`, but those variables were not the computed style of the login root.
- Screenshots and crops are absent because the preview browser returned "The browser is not producing screenshot frames".
