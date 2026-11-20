# Readings

Measured 2026-11-19 from the live T3 preview tab. The preview tab could not produce screenshot frames (`The browser is not producing screenshot frames`). Screenshots were taken later in headless Playwright against public pages that had already loaded with no Cloudflare challenge. Login was not screenshotted in Playwright.

Viewport when the marketing values were read: `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2, visual viewport scale 1. An earlier read at 1169 by 731 is not the source of the numbers below.

## Marketing, https://www.replo.app/

- `html` computed `color-scheme`: dark. No theme switch on the page.
- `body` background `rgb(0, 0, 0)`, color `rgb(245, 250, 217)`, font `archivo, "archivo Fallback", Arial, sans-serif`, 16px / 24px, weight 400.
- `header` height 60px, sticky, transparent.
- `h1` 56px, weight 500, line-height 59.36px, letter-spacing -1.96px, color `rgb(245, 250, 217)`, family archivo.
- Lead paragraph 20px, weight 400, line-height 30px, color `rgba(245, 250, 217, 0.7)`.
- `h2` "What is Replo?" 24px, weight 500, line-height 30px, letter-spacing -0.48px, color `rgb(245, 250, 217)`.
- Nav link (Customers, Pricing, Log in): 14px / 20px, padding 8px 12px, color `rgb(245, 250, 217)`, radius pill, transparent, `transition-colors`.
- Start for free: background `rgb(245, 250, 217)`, color `rgb(18, 18, 18)`, height 36px, padding 0 16px, radius 9999px, border `1px solid rgba(18, 18, 18, 0.2)`, shadow `rgba(0, 0, 0, 0.055) 0px 0px 0px 1px` plus inset highlights.
- Book a demo: background `rgb(0, 0, 0)`, color `rgb(245, 250, 217)`, height 36px, padding 0 16px, radius 9999px, border `1px solid rgba(245, 250, 217, 0.24)`.
- Get started for free: same cream face, height 44px, padding 0 24px, 16px / 16px, gap 8px.
- Learn more: color `rgba(245, 250, 217, 0.5)`, 16px, no background.
- Product menu, opened by click: panel `rgb(17, 17, 17)`, radius 14px, border `1px solid rgba(255, 255, 255, 0.1)`, shadow `rgba(0, 0, 0, 0.5) 0px 18px 50px 0px`, width up to 1040px, height 420px. Link text 14px cream.
- Font variables resolved on the root: `--font-archivo` is `"archivo", "archivo Fallback", Arial, sans-serif`. `--font-instrument-sans` and `--font-space-mono` are declared. Archivo is the painted family.

Declared on `:root, :host` and resolved to hex (not every one is painted on a control):

| Name | Value |
|---|---|
| `--color-replo-cream` | `#f5fad9` |
| `--color-replo-button` | `#eef5c5` |
| `--color-replo-button-fg` | `#121212` |
| `--color-replo-panel` | `#0f1010` |
| `--color-ink` | `#f5fad9` |
| `--color-ink-muted` | `#f5fad9b3` |
| `--color-ink-faint` | `#f5fad980` |
| `--color-surface-card` | `#0b0b0b` |
| `--color-surface-glass` | `#161616` |
| `--color-accent-green` | `#b7feae` |
| `--color-accent-pink` | `#ffb3c3` |
| `--color-accent-magenta` | `#ef196e` |
| `--color-accent-purple` | `#8b32a8` |
| `--color-accent-blue` | `#5b9dff` |
| `--radius-inner` | `10px` |
| `--radius-card` | `16px` |
| `--radius` (shadcn, `:root`) | `.625rem` |
| `--spacing` | `.25rem` |
| `--spacing-section` | `5rem` |
| `--spacing-section-lg` | `7rem` |
| `--spacing-gutter` | `clamp(1rem, .2rem + 1.6vw, 3rem)` |
| `--spacing-header` | `3rem` |
| `--transition-duration-fast` | `.15s` |
| `--transition-duration-base` | `.3s` |
| `--transition-duration-slow` | `.5s` |
| `--transition-duration-reveal` | `.7s` |
| `--ease-standard` | `cubic-bezier(.4, 0, .2, 1)` |
| `--ease-emphasized` | `cubic-bezier(.16, 1, .3, 1)` |

Under `prefers-reduced-motion: reduce`, `--transition-duration-slow` and `--transition-duration-reveal` are `0s`. That rule was read from the stylesheet, not from an emulated reduce pass. The preview tab cannot emulate media.

`h1` animation: `mount-rise 0.7s cubic-bezier(0.16, 1, 0.3, 1)`. Glass button transition: color, background-color, border-color and box-shadow, each `0.3s cubic-bezier(0.4, 0, 0.2, 1)`.

Shadcn tokens on `:root` (`--background: #fff`, `--foreground: #0a0a0a`, `--primary: #171717`, `--destructive: #e40014`, `--border: #e5e5e5`) resolve to light lab colours. They are not the painted marketing theme. They are recorded as declared, not as the page.

## Pricing, https://www.replo.app/pricing

Same body. `h1` same 56px / 500 / -1.96px display style.

- Billing track: `rgba(255, 255, 255, 0.05)` background, border `1px solid rgba(255, 255, 255, 0.08)`, height 44px, padding 4px, pill radius.
- Monthly, unselected: transparent, color `rgba(245, 250, 217, 0.5)`, height 34px, padding 0 16px, 14px.
- Annual, selected (`aria-pressed=true`): background `oklab(0.999994 0.0000455678 0.0000200868 / 0.1)`, color `rgb(245, 250, 217)`, height 34px.
- Plan card: background `rgb(11, 11, 11)`, border `1px solid rgba(255, 255, 255, 0.08)`, radius 16px, about 292 by 768 CSS pixels.
- Plan name (Free, Starter, Pro, Custom): editorialNew, 24px, weight 400, color `rgb(245, 250, 217)`.
- Price `$0`: archivo, 40px, weight 500.
- Most popular badge: editorialNew, 14px, padding 0 10px, height 36px, pill, border `1px solid rgba(124, 127, 186, 0.4)`, color cream.
- Plan CTA Start for free: cream face, height 44px, width 242px, 16px.
- Custom CTA Book a call / Book a demo: black face, cream text, border `1px solid rgba(245, 250, 217, 0.24)`, height 44px.
- FAQ row: padding 20px 24px, radius 16px, 16px cream, transparent.

Prices read on the annual state: Free `$0`, Starter `$99` (was `$119`), Pro `$499` (was `$599`). Monthly prices were not read as computed text after the toggle; the monthly screenshot shows `$119` and `$599`.

## Contact, https://www.replo.app/contact

- `h1` 40px, weight 500, letter-spacing -1px, archivo, cream.
- Text field wrapper: background `oklab(0.999994 0.0000455678 0.0000200868 / 0.04)`, border `1px oklab(... / 0.1)`, radius 10px, height 50px, 16px. Placeholder "Enter your first name". The form was not submitted.

## Customers, https://www.replo.app/case-studies

Loaded in Playwright. Title "Replo case studies". Search field, Newest menu and filter chips (All selected as a cream pill) are in the screenshot. Chip computed styles were not read in the preview tab. Recorded as a gap for exact chip metrics.

## 404, https://www.replo.app/this-page-does-not-exist-capture

HTTP 404. `h1` "Page not found", 56px, weight 500, letter-spacing -1.96px, cream. Body still `rgb(0, 0, 0)` in the computed style. The screenshot shows a starfield behind that text. Return to homepage is the cream pill.

## Login, https://dashboard.replo.app

`https://dashboard.replo.app` redirected to `https://dashboard.replo.app/auth/signup`. A click on "Already have a Replo account? Sign in" moved to `https://dashboard.replo.app/auth/login`. Nothing was typed. Nothing was submitted. Google was not clicked. Shopify Theme Builder was not clicked. Forgot password was not followed.

- `body` background `oklch(0.16 0.0046 72)`, font Inter, "Helvetica Neue", Arial, sans-serif, 16px / 24px. Computed `color` on body is `rgb(0, 0, 0)` while painted text is light. Text colour is taken from the heading, not from body.
- Marketing line: 20px, weight 500, line-height 27.5px, letter-spacing -0.2px, color `oklch(0.986 0.0031 72)`, opacity 0.45.
- Sign-in `h1` "Welcome back to Replo": 24px, weight 600, letter-spacing -0.48px, color `oklch(0.986 0.0031 72)`.
- Field wrapper: background `oklch(0.23 0 72)`, border `1px solid oklch(0.986 0.0031 72)`, radius 8px, height 40px, padding 8px 12px. Input itself is transparent, 14px / 20px, color `oklch(0.986 0.0031 72)`, placeholder `you@company.com`.
- Continue / Sign in: background `oklch(0.922 0.0275 72)`, color `oklch(0.13 0.006 72)`, radius 8px, height 40px, border 0.5px transparent, 14px / 20px. Focus ring declared as `focus-visible:ring-3` on the class. The ring was not forced.
- Continue with Google: background `oklch(0.195 0.0046 72)`, color `oklch(0.83 0.0054 72)`, border `0.5px solid oklch(0.3 0.0046 72)`, radius 8px, height 40px.
- Forgot password: 14px, weight 500, color `oklch(0.986 0.0031 72)`, no underline. Href `/auth/password/reset/init`. Not followed.

Brand colours declared on the dashboard and not painted on this form: `--color-brand-seashell #f5fad9`, `--color-brand-light-green #b7feae`, `--color-brand-light-pink #ffb3c3`, `--color-brand-magenta #ef196e`, `--color-brand-purple #8b32a8`, `--color-brand-blue #274ae2`, `--color-brand-yellow #ffeb80`, `--color-brand-dark-green #03ab8c`.

## What was not entered

- No email, password, name, or website was typed.
- No signup, sign-in, Google, Shopify, password reset, payment, or plan checkout.
- Docs at docs.replo.app were not opened.
- The contact form, search field, and FAQ rows were not submitted or expanded.
- Hover, focus-visible, pressed, disabled, error, and loading were not forced.
- No reduced-motion emulation. The reduce rule is from the stylesheet only.
