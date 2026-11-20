# Patterns

The only surfaces that rendered were the public marketing home and the public blog, both as Wayback replays. The live hosts do not serve the product. See [raw/host-check.md](raw/host-check.md).

## Home

Replay: https://web.archive.org/web/20240506015935/https://ozone.pro/

Read at `window.innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1. Page fill `{dark.page}`. A sticky nav (`data-framer-name="Desktop"`) sits on `{dark.nav}` with `backdrop-filter: blur(10px)`, height 68px, padding `0 16px`. Links are Home, Blog, Careers, Login, then a primary "Try For Free".

Under that, a hero frame (`{dark.hero}`, radius 32px, 1408 by 1080) holds a funding chip, the h1 "Supercharge your video creation" at `{core.typography.display}`, the lede at `{core.typography.lede}`, then secondary "Watch Trailer" and tertiary "Try For Free". A painted comment panel sits in the hero. It is a demo, not the app.

Further down: feature cards on the black page, a "Save hours" section at `{core.typography.title}`, investor logos, a footer with an eyebrow "USEFUL" and a giant wordmark in `{core.font.family.wordmark}` at 500px. Scroll height was 5725.

At 390 CSS px the same h1 computed to 40px / 48px, and the nav was 390 by 36. The desktop nav variant (`hidden-afnmq6`) computed to `display: none`. No separate phone screenshot exists.

## Blog

Replay: https://web.archive.org/web/20240227223658/https://www.ozone.pro/blog

Read at the fill viewport, 1169 by 731, not a requested 1440. Visible h1 "Blog" at 40px PolySans Bulky Wide. Intro at 18px / 500. One post, dated Nov 8, 2023, title at 32px / 40px PolySans Slim Wide. "Read More" is a black pill. The nav CTA on this older replay says "Join Waitlist" and uses the same blue pill as "Try For Free".

## Not reached

| Pattern | Why |
|---|---|
| App shell, editor, list, table | Behind app.ozone.tech, which has no DNS record. |
| Sign-in, sign-up, form error | Login and register URLs were not opened. |
| Pricing, checkout | Not linked from the home nav. Not entered. |
| Light theme | The page is one dark theme. `color-scheme` on the root was `normal`. No toggle was in the DOM. |
| Screenshots of these patterns | `preview_snapshot` did not produce frames. |
