# Components

Measured on the signed-out Suno marketing site on 2026-11-19, color-scheme dark, CSS viewport 1169 by 731, device pixel ratio 2. Values are computed styles. No crops: the preview browser did not produce screenshot frames. See [raw/gaps.json](raw/gaps.json).

## Button

The marketing nav uses three button shapes.

| State | Where | Values |
|---|---|---|
| Primary, resting | "Join Suno for free" on the home nav | background `#f7f4ef`, text `#101012`, padding 8px 16px, height 40px, radius pill, Neue Montreal 15px weight 500 |
| Secondary, resting | "Log in" on the home nav | background transparent, text `#fcfbf9`, padding 8px 16px, height 40px, radius pill |
| Aura, resting | Hero "Create" | background `#000000`, text `#ffffff`, padding 8px 16px, height 40px, radius pill. The aura variables (`--aura-primary` `#4d33b7`, `--aura-secondary` `#bc4e00`) did not paint this control's computed background |
| Large primary | "See open positions" on `/careers` | background `#f7f4ef`, text `#101012`, padding 16px 32px, height 56px, Neue Montreal 17px weight 500, radius pill |
| Nav link | "Pricing" | transparent, text `#f7f4ef`, padding 6px 12px, height 36px, Neue Montreal 15px weight 500, radius pill |
| Provider | Sign-in dialog, "Continue with Google" | background `#252529`, text `#f7f4ef`, padding 12px 16px, height 48px, width 350px, radius 12px |

Hover, focus-visible, pressed, disabled and loading were not forced.

## Link

Footer and feature links use Neue Montreal, foreground primary, no underline at rest. "Apply now" on `/careers` is 14px weight 500. The job links go to `jobs.ashbyhq.com` and were not opened.

## Text field

The home prompt is a textarea, placeholder "Chat to make music". Computed: Neue Montreal Book 18px, line-height 32px, weight 400, color `#ffffff`, background transparent, padding 0 4px, radius 12px, width 719px. The placeholder class is `placeholder:text-white/40`. Nothing was typed into it.

No text area beyond that prompt, and no select, checkbox, radio or switch, appeared on the pages that were read.

## Dialog

"Log in" opens a dialog on the same URL. Title "Welcome to Suno", Neue Montreal 24px weight 500. Shell: background `#1c1c1f`, border 1px solid `rgba(255, 255, 255, 0.1)`, radius 32px, width 400px, height 366px. Overlay: `oklab(0 0 0 / 0.6)`, padding inline 16px, animation duration 150ms. Close is a 40px pill, text `#a3a3a3`.

The dialog offers Continue with Google, Apple, Phone, Discord, Facebook and Microsoft. No email field was shown. None of those paths were followed. The dialog was closed.

## Card

Pricing cards on the home `#pricing-section`, yearly selected:

| Card | Background | Border | Radius | Padding | Width |
|---|---|---|---|---|---|
| Free, Pro, Platinum | `rgba(255, 255, 255, 0.04)` (`--color-plan-card`) | 1px solid `rgba(255, 255, 255, 0.1)`, or transparent on the featured cards | 24px | 20px | 273px |
| Premier | `oklab(0.678433 0.232037 -0.0156413 / 0.03)` | transparent | 24px | 20px | 273px |

Plan name is Neue Montreal Book 24px weight 600, color `#fcfbf9`. Price is 30px weight 500. "Most Popular" is a pill, background `#fcfbf9`, text `#101012`, 11px weight 600, padding 4px 10px. "Save up to 20%" is 12px weight 500, color `#02d95c`, background the green accent at 15% opacity, radius 6px, padding 2px 6px.

The Monthly / Yearly control is a pill, height 40px, border 1px solid `rgba(255, 255, 255, 0.1)`. The active indicator is `rgba(255, 255, 255, 0.1)`. Yearly was the resting selection. The switch was not clicked.

Song tiles carry a Remix chip: height 28px, background black at 40% opacity, text white, 12px weight 500, padding 0 10px, radius pill. Those links go to `/create` and were not followed.

## Badge

See the plan badges above. No other badge was measured.

## List row

`/careers` lists roles as text links (for example "Creative Director, Marketing Campaigns") with an "Apply now" link. Row chrome was not isolated beyond the link styles.

## Gaps

- Hover, focus-visible, pressed, disabled, loading and error states were not forced.
- No select, checkbox, radio, switch, tabs (beyond the billing pill), tooltip, toast, table or avatar was on the pages that were read.
- No component crops. The preview browser did not produce screenshot frames.
- The signed-in creator, Studio, and checkout were not entered.
- A 390px width was not measured. The viewport stayed at 1169px.
- Light theme was not shown. Light token names exist as declarations only.
