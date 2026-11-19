# Readings

Host confirmed: https://o-p-e-n.com/ returned 200, title "Guided Meditation | Mindfulness | Breathwork | Open Breathwork & Meditation". No Cloudflare challenge in the T3 preview tab or in headless Chromium.

Preview viewport for CSS readings: innerWidth 1169, innerHeight 731, devicePixelRatio 2, visualViewport scale 1.

Screenshots: headless Chromium, 1440x900 and 390x844, deviceScaleFactor 2. The T3 preview browser did not produce screenshot frames.

## Palette utilities

Read from the entry stylesheet, selectors `.color-*` and `.bg-*`.

| Name | RGB | Hex |
|---|---|---|
| black | 0 0 0 | #000000 |
| cream | 238 236 231 | #eeece7 |
| steel-blue | 72 127 127 | #487f7f |
| copper | 191 125 65 | #bf7d41 |
| sage | 142 142 118 | #8e8e76 |
| gray | 190 190 192 | #bebec0 |
| mauve | 195 143 145 | #c38f91 |
| piper | 210 94 43 | #d25e2b |
| sepia | 122 55 0 | #7a3700 |
| sweet-corn | 249 214 133 | #f9d685 |
| toast | 223 219 210 | #dfdbd2 |
| white | 255 255 255 | #ffffff |
| citrus | 162 184 51 | #a2b833 |
| sapphire | 76 122 240 | #4c7af0 |
| 60-cream | 143 142 139 | #8f8e8b |
| 40-cream / 60-black | 95 94 92 | #5f5e5c |
| 20-cream | 48 47 46 | #302f2e |
| 10-cream | 24 24 23 | #181817 |
| darkest-gray | 77 77 77 | #4d4d4d |
| dark-gray | 167 167 167 | #a7a7a7 |
| red | 216 40 40 | #d82828 |

## Type utilities

| Selector | Family | Size | Line height | Tracking |
|---|---|---|---|---|
| .typo-display-mono | Semi-Mono | 60px | 56px | uppercase |
| .typo-display-l | | 80px | 73.6px | -2.4px |
| .typo-display | | 60px | 56px | |
| .typo-title-l | Regular | 48px | 48px | |
| .typo-title-s | Regular | 24px | 24px | letter-spacing 1% in the sheet |
| .typo-title-xs-mono | Semi-Mono | 14px | 20px | uppercase |
| .typo-bodycopy | | | 20px | -0.01em |
| .typo-tag-s-mono | | 12px | 1.15 | |
| .typo-tag-xs-mono | | 10px | 1 | |

Computed title (`.typo-title`, hero nav) was 36px / 36px / -0.36px. That size is not in the `.typo-display` rule.

## Space utilities

`.p-3xl` 160, `.p-2xl` 120, `.p-xl` 80, `.p-lg` 60, `.p-md` 40, `.p-sm` 20, `.p-xs` 10, `.p-6` 6, `.p-4` 4, `.p-2` 2, `.p-0` 0. Margin utilities match.

## Motion

Declared, not probed with `motion-probe.mjs` because the T3 tab could not screenshot and the probe was not run. Durations in tokens are from the stylesheet rules named in tokens.json. `@media (prefers-reduced-motion: reduce)` exists for `.skeleton-block` and the featured carousel. A page-level reduce verdict was not measured. Gap.

## Not entered

No email submitted. No Apple sign-in. No phone number. No card. No credit pack. No booking. No class playback.
