# Brilliant design reference

A token set and component reference for Brilliant's web app, for building mockups in Figma or Paper that match the product. It was extracted from brilliant.org on 2026-09-25, signed in to a new free account on the Math path, in the app's light and dark themes, at desktop width and (for public pages) at a 390px mobile width.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (174-step palette, 6 font families, 33 type styles, spacing, sizes, breakpoints, radii, border widths, blur, z-index, durations, easings, opacity) plus `light` and `dark` sets of 351 tokens each (semantic colour roles, gradients, shadows and component colours), and a `$themes` list. Every token carries `$extensions.source` naming where it was read. Import with Tokens Studio → Load from file. |
| [style-guide.html](style-guide.html) | One self-contained page that renders every token and component with the real values, in both themes (toggle top right, defaults to the system theme). Open it in a browser, or paste sections into Paper. |
| [components.md](components.md) | The discovery list of every page, view and overlay, one inventory entry per component with crops of the real product, the icon summary, and the Gaps. |
| [components/crops/](components/crops) | 82 per-component crops cut from the screenshots, in both themes where both were captured. |
| [icons/](icons) | 15 app glyphs saved from the signed-in pages (`icons/app/`, named by role and size) and 32 SVGs pulled from the public pages (`icons/public/`, named by hash, indexed in [components.md](components.md#icons)). Brilliant's property, kept for reference only. |
| [screenshots/](screenshots) | 73 `{page}-{theme}-{state}.png` captures of the real product at 2x, `mobile-*` at 390x844. |
| [raw/](raw) | The unprocessed readings: every Panda CSS variable in both themes (`css-vars-public.json`), all 432 colour variables resolved per theme (`colors.tsv`), the 33 text styles (`text-styles.tsv`), per-surface computed styles (`measurements.md`) and the headless dumps of the public and pricing pages. |
| [tools/](tools) | The two builders and the capture kit. See Rebuild. |

## How the values were read

Brilliant styles its app with Panda CSS, which writes every token onto `:root` as a custom property (`--panda-colors-bg-primary`, `--panda-radii-2xl`, `--panda-shadows-elevation-base`) and overrides the colour ones under `[data-theme="dark"]`. The token file is built from a dump of those variables, so every palette step, semantic colour, radius, spacing step, z-index, shadow and gradient traces to a named variable. Type styles come from Panda's `textStyle` rules in the production stylesheet.

Component measurements are computed styles read live in Chrome for each state: hover and focus were held with the pointer or keyboard, selected and disabled states were reached in the product, and pressed states were caught mid-transition. The theme was switched by setting `data-theme` on the page, never in account settings. Values that could only be sampled from a screenshot are marked "estimated from screenshot"; in the token file that is one token, `size.icon-md`, and in the specs it is the canvas-drawn Koji suggestion cards and the iridescent frames on the pricing page.

Panda defines no duration tokens that survive to production (`trs-dur_fast` compiles to invalid CSS), so `core.duration` lists the durations the app's transitions actually use, each with the rule it was read from. Springs are real variables: `--spring-smooth` is `cubic-bezier(.2,1.1,.36,1)` over .833s, with a `linear()` version in `easing-linear`.

The screenshots were converted from the display profile (Display P3 or the external monitor's) to sRGB and stored as 256-colour PNGs to keep the repo small. Flat UI colours are exact, but gradients can band slightly, so read exact values from the tokens, not from the images. The signed-in account's name and email were replaced with "Learner", "Example" and learner@example.com before every capture.

## Fonts

| Family | Weights | Used for |
|---|---|---|
| CoFo Brilliant | 400, 500, 700, with italics | All UI text |
| CoFo Robert | 500, with italic | Display headlines (`display.*` styles), fallback Georgia |
| CoFo Semi Mono | 500, 700 | Lesson interactive tiles |
| Source Code Pro | 400, 500, 700, with italics | Code |
| KaTeX_Main | 400, 700, with italics | Maths |
| Soleil | 400, 600, 700, 400 italic | Legacy Django pages only |

No `font-feature-settings` are set anywhere. The CoFo families are proprietary and are not committed. The style guide looks for them in a local `fonts/` folder next to it (gitignored) and falls back to Figtree and Georgia, showing a notice when it does.

## Do and don't

1. **Do give each screen one filled main button and keep every other action grey, outlined or text.** Home and the course page have one blue "Start"; the lesson pairs its coloured button with a grey "Why?" or "Get help"; the quit dialog sets "Keep learning" over a red text-only "Quit"; Settings has one black "Add another email" under an outlined "Send verification". See [home-light-default](screenshots/home-light-default.png), [lesson-dark-correct](screenshots/lesson-dark-correct.png), [modal-quit-dark](components/crops/modal-quit-dark.png) and [settings-light-account](screenshots/settings-light-account.png).
2. **Do let the main button's colour say what the moment is.** Blue starts a course or lesson, and onboarding and dialogs use the neutral primary (near-white in dark, black in light). After Check, a green "Continue" or a yellow "Try again" arrives with the panel border (green.700 or yellow.700) and Koji's bubble in the same hue. See [lesson-dark-correct](screenshots/lesson-dark-correct.png), [lesson-dark-retryable](screenshots/lesson-dark-retryable.png) and [course-light-default](screenshots/course-light-default.png).
3. **Do keep the blue, pink and yellow iridescent gradient for Premium.** It appears only on the "Go Premium" border, the promo banner, the "Explore" pill, the keys popover's "Unlock all lessons now" and the pricing page; course and lesson buttons are one flat colour. See [home-light-default](screenshots/home-light-default.png), [popover-keys-light](components/crops/popover-keys-light.png) and [pricing-light-fullpage](screenshots/pricing-light-fullpage.png).
4. **Do show the main button disabled until the step can go ahead.** Sign in, onboarding Continue, lesson Check and "Update personal info" sit full width in `bg.disabled` with `text.disabled` and no lift, then fill in place. See [login-light-default](screenshots/login-light-default.png), [onboarding-dark-subject-choice](screenshots/onboarding-dark-subject-choice.png) and [lesson-light-default](screenshots/lesson-light-default.png).
5. **Do mark the learner's place by lighting one step and dimming the rest.** The current path node or tile is in full colour with Koji or a "START HERE" tag on it; later steps get grey discs, dimmed art and `text.tertiary` or `text.disabled` labels. See [course-light-default](screenshots/course-light-default.png), [plan-dark-learning-path](screenshots/plan-dark-learning-path.png) and [home-dark-default](screenshots/home-dark-default.png).
6. **Do keep uppercase for small tags.** "LEVEL 1", "RECOMMENDED", "GR 4–5", "NEW", "START HERE" and "OR" are 12/13.2 700 uppercase with .48px tracking. Headings, buttons, nav and field labels are never uppercase ("Your learning paths", "Personal info", "Keep learning"). See [courses-light-default](screenshots/courses-light-default.png), [settings-light-account](screenshots/settings-light-account.png) and [plan-dark-learning-path](screenshots/plan-dark-learning-path.png).

## Rebuild

```bash
python3 tools/build_tokens.py
```

```bash
python3 tools/build_style_guide.py
```

`build_tokens.py` reads `raw/css-vars-public.json` and `raw/text-styles.tsv` and writes `tokens.json`; component colours and their sources are listed in its `comp()` block. `build_style_guide.py` renders `style-guide.html` from `tokens.json` and `tools/style-guide.template.html`, turning every token into a CSS variable so the page cannot drift from the file. Both are deterministic: re-running them on this commit reproduces both files byte for byte. Edit the raw inputs or the builders, never the generated files.

`tools/capture/` holds the kit the captures came from: the in-page helpers (`helpers.js`), the window screenshot cropper (`shot.sh`, with `wins.swift` to find the Chrome window), the sRGB converter (`srgb.py RAW_DIR SRGB_DIR`, which also writes the 256-colour screenshots), the crop list (`crops.py [SRGB_DIR]`, which writes `components/crops/`), and headless Playwright scripts for the variable dump (`vars.mjs`), public pages (`public.mjs`), pricing (`pricing.mjs`), icons (`icons.mjs`) and the style guide check (`sg.mjs`). They were written for one session: the Playwright scripts write next to this folder and take `PLAYWRIGHT` as the path to a Playwright install when `playwright` is not resolvable, and `shot.sh` needs `SP` pointing at the compiled window lister.

## Use in Figma

Import `tokens.json` with Tokens Studio and choose the Light or Dark theme. Set fonts to CoFo Brilliant (or Figtree as a stand-in) and CoFo Robert (or Georgia) for display headlines.

The component to get right is the 3D button: a pill face lifted 4px over a same-hue darker lip, which drops to 0 on press over 100ms. Cards are flat with a 2px border and large radii (20 to 40). Elevation is a soft, unoffset black glow: `shadow.base` is `0 0 15px` in 10% black on light and 80% black on dark. The lesson's Koji areas stay dark in the light theme. Anything the capture could not reach is listed under Gaps in [components.md](components.md#gaps).
