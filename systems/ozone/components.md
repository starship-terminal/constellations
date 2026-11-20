# Components

Public marketing only, read from the Wayback replay of ozone.pro on 2026-11-19. No crop PNGs: `preview_snapshot` returned "The browser is not producing screenshot frames" twice, and no screenshot was invented. Values are computed styles. See [raw/computed-home.json](raw/computed-home.json).

## Button

Primary, named `Primary` in the Framer tree. Label "Try For Free". Fill `{dark.accent}`, label `{dark.on-accent}` at `{core.typography.label}`, padding 8px 14px, radius `{core.radius.pill}`, height 36px in the nav (48px on the later instance). Shadow `{core.shadow.control}` plus an inset highlight `rgba(255, 255, 255, 0.4) 0 0 6px`. Href was `https://app.ozone.tech/register`, which does not resolve.

Secondary, named `Secondary`. Label "Watch Trailer". Fill `{dark.button-secondary}`, padding 16px 22px, radius `{core.radius.pill}`, height 52px. Same label style and shadow.

Tertiary, named `Tertiary`. Label "Try For Free". Fill `{dark.page}`, padding 16px 22px, radius `{core.radius.pill}`, height 52px. Same label style.

Hover, focus-visible, pressed, disabled and loading were not captured. The replay was read at rest.

## Link

Nav links Home, Blog, Careers, Login. Family `{core.font.family.nav}`, 14px, weight 400, line-height 16.8px, colour `{dark.text}`, no background, no radius. Login pointed at `https://app.ozone.tech/login`. That host was not opened.

## Chip

Funding line "Ozone raised $7.1M seed round". Fill `{dark.chip}`, radius `{core.radius.chip}`, padding 4px 8px, label in `{core.font.family.nav}` at 14px, colour `{dark.text}`.

## Tag

Prompt chips on the feature cards ("Robot sleeping in bed"). Fill `{dark.tag}`, radius `{core.radius.pill}`, padding 7px 11px, type `{core.typography.tag}`, colour `{dark.text}`.

## Card

Feature tiles named Feature 1, Feature 3, Feature 4, Feature 5. Fill `{dark.page}`, radius `{core.radius.card}`. Feature 3 and later also carried the control shadow. Feature 2's own background was transparent; the page behind it is black.

The hero frame is a card-sized region, not a repeated component: fill `{dark.hero}`, radius `{core.radius.hero}`, 1408 by 1080 at 1440 CSS px.

## Demo panel

A painted product demo, not the signed-in app. Comment panel fill `{dark.surface}`, radius `{core.radius.panel}`, 200 by 369. Compose strip `{dark.surface-raised}`, radius `0 0 6px 6px`. Tab bar `{dark.surface-tabs}`. The "Add a comment..." line is a text node, not an `input`. No text field, text area, select, checkbox, radio or switch was in the DOM.

## Closing band

A full-width link, fill `{dark.accent}`, radius `{core.radius.band}`, padding 64px, shadow `rgb(0, 0, 0) 0 32px 50px` plus an inset highlight. It contains the words "Try For Free".

## Gaps

- No hover, focus-visible, pressed, disabled, loading or error state was measured.
- No form control exists on the marketing page. Login and register live on app.ozone.tech, which has no DNS record, so they were not opened.
- Blog "Read More" matches tertiary (black pill, 16px 22px, radius 100px) on the 2024-02-27 replay. "Join Waitlist" matches primary. See [raw/computed-blog.json](raw/computed-blog.json).
- Icon extraction was not run. Inline marks are in the uncaptured screenshots.
