# Measurements

Read on 2026-11-19 with `preview_evaluate` in a T3 preview tab. Viewport 1169 by 731 CSS pixels, devicePixelRatio 2, visualViewport scale 1. `preview_snapshot` failed twice with "The browser is not producing screenshot frames". No PNG was invented.

html font-size on squareup.com computed to 10px, so 1rem is 10px there. Login chrome on app.squareup.com uses px tokens.

## Colour, painted

| Role | Computed | Where |
|---|---|---|
| Page | rgb(255, 255, 255) | body on /us/en and /us/en/pricing |
| Login canvas | rgb(250, 250, 250) | html on /login |
| Login ink | rgb(16, 16, 16) | body and Sign in heading |
| Marketing ink | rgb(0, 0, 0) | body on /us/en |
| Accent | rgb(0, 106, 255) | Action--button ::before, matches --color-blue #006aff |
| Kiosk plate | rgb(0, 75, 255) | .HomePageKioskHero-background |
| Muted | #707070 | --color-text-muted, light mode |
| Border | #cccccc | --color-border, light mode |
| Accent surface | #f7f6f5 | --color-background-accent |
| Field border | #dadada | --field-normal-state-normal-validity-border-color, painted as 1px inset |
| Field focus | #101010 | painted as 2px inset after focus() |
| Critical | #cc0023 | --color-critical and invalid field border |
| Error text | #BF0020 | --field-error-message-text-color, declared, not painted on an error |
| Success | #00b23b | --color-success, declared |
| Passkey face | rgb(240, 240, 240) | .sign-in-passkeys-button |
| Tips slot | rgb(16, 16, 16) | .product-tips-v3-animation-slot |
| Plan card | rgb(255, 255, 255) | .PwNextPricingPlanCards-card |

## Type, computed

| Role | Family | Size | Weight | Line | Tracking |
|---|---|---|---|---|---|
| Body | Square Sans Text VF | 16px | 400 | 24px | normal |
| Marketing h1 | Square Sans Display VF | 64px | 400 | 0px (collapsed metric) | -0.5px |
| Nav | Cash Sans | 15px | 400 | 22.5px | normal |
| Plan title | Cash Sans | 20px | 500 | 24px | -0.2px |
| Feature heading | Exact Block | 56px | 400 | 56px | -2.24px |
| Sign in | Square Sans Display VF | 25px | 700 | 32px | normal |
| Continue | Square Sans Text VF | 16px | 600 | 24px | normal |
| Signup wall h1 | (not isolated) | 36px | 400 | | |

## Controls

Marketing primary face is the ::before of `.Action__content-wrapper`, rgb(0, 106, 255), radius 50px, content padding 10px 20px, height 44px, label weight 500. Alt face is white with label rgb(0, 106, 255).

Login Continue is market-button, face rgb(16, 16, 16), label white, radius 24px, height 48px, inner padding 12px 20px, weight 600. Not clicked.

Login field is market-input-text, 64 by 534.5 px, radius 8px, white. Rest inset shadow rgb(218, 218, 218) 1px. After focus() and two frames, inset shadow rgb(16, 16, 16) 2px. Value stayed empty.

Sign up link in the shadow root of market-link is underline, weight 600, colour rgb(16, 16, 16), href https://app.squareup.com/signup/en-US.

## Not entered

Signup at https://app.squareup.com/signup/en-US showed Email, Password, an agreement checkbox, and Create account. Nothing was typed. Continue was not clicked. Passkey was not clicked. No card, bank, or KYC field was opened.
