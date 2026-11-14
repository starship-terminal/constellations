# Explore patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots). All pages were replayed from the archived 2023-02-23 build; the product closed on 2023-04-19.

## Marketing chrome (every public page)

A fixed 60px bar (`component.header.height`, 56px at 390) in the signature mid-grey `color.grey.500` (#9d9d9d) sits at z-index 300 over every public page. It carries the E wordmark (LabilGrotesk-Medium, white), a "Sign in" text link and the yellow "Sign up free" pill (`color.accent.DEFAULT` #ffc60a fill, `color.grey.950` ink, `radius.button` 50px, `component.button.signupPill.height` 38px). At 390 the bar collapses to the wordmark plus the pill — "Sign in" drops away. A fixed alert tray (`z-index.alert` 2000) waits bottom-left for form errors that never fire signed out.

## Home

The hero is a full-bleed grey field (`light.color.background.field`): a small "Welcome" greeting, then the positioning sentence — "Explore is an emotionally intelligent ad-free social media platform for creatives" — in `font.family.display` at `font.size.40`/tight leading, white. Under it, hairline feature tags ("Free", "For creatives", "No ads", "All features") are `radius.card` 7px boxes with a `color.border.on-field` (#b7b7b7) 1px stroke and white text; one of them is a CTA linking to register. Below the fold a feed preview uses the same post cards as Discover.

## Discover

`/discover` opens with a quiet intro line ("Browse inspiring work on Explore curated by our team") then a wrapping row of category pills: 20px-radius chips (`radius.pill`), 6/13/7 padding, 14px text, a `color.grey.100` hairline when idle and a `color.grey.950` ink border when active. The feed is an absolute-positioned 3-up card grid — cards `calc(33.3333% - .5px)` wide with 15px side padding and a 50px row pitch inside a 1640px-max, 20px-gutter column. Each card: rounded media tile (`radius.card`, grey #9d9d9d placeholder where the archive lacks the asset), an author row (28px round avatar, name, optional yellow PRO badge, age in muted grey), an UntitledSansMedium 16px title, and the icon action row (appreciate/comment/save). VueCarousel arrows overlay multi-image posts. Infinite scroll pages in via `last_id` cursors; the capture's full-page shots cap at eight tiles.

## Auth screens

`/login`, `/register` and `/forgot-password` share one split layout: the left half is a darker `#717171` grey panel (`color.grey.700`, not the `#9d9d9d` field) carrying the community welcome quote and a small logo mark; the right half is a white ~424px form column (`component.auth.formWidth`) with the auth heading. Fields are `radius.input` 8px boxes — a `color.grey.150` 1px hairline, 13/17 padding, 16/20 text, `#c1c1c1` placeholders — with a password-visibility eye on the password field. All three submits are the same full-width dark `#262626` button (`color.grey.950`, `radius.card` 7px corners, 47px tall): "Log in" on login, "Sign up" on register, "Reset Password" on forgot. Secondary actions ("Forgot your password?", "Sign up free", the terms/privacy line and the newsletter checkbox on register) sit under the submit as small muted links. Fields were focused and filled for measurement, then cleared; nothing was submitted.

## Server-rendered profiles

Public profiles were server-rendered by the archive era's SSR variant: a profile header (round avatar, display name, handle, follow/subscribe actions) over a post gallery in the same card grammar as the feed. These pages were replayed from the archived SSR HTML with JavaScript disabled so the SPA could not replace the markup — they are the only member-content evidence in the package.

## About and legal

`/about` is a marketing page on the same chrome: a display title, feature blocks (community, "no numbers", "no algorithms", any-dimension media), portfolio and custom-domain pitches, and yellow/dark CTAs. `/terms`, `/privacy` and `/conduct` are legal pages: a legal title and long body copy in the content column under the same header and footer. The footer is a multi-column link list on the white page.

## Mobile

At 390 the chrome drops to 56px and keeps only the wordmark and "Sign up free". The hero sentence shrinks a step, feature tags wrap, the pill row scrolls, and post cards go full width with the same author/title/action anatomy. On the split auth screen the welcome panel does not stack above the form — `@media (max-width:650px)` sets `.auth__left{display:none}`, so only the form column remains.

## Closure announcement

The June 2023 archive snapshot keeps the same shell but carries the shutdown notice — the product closed on 2023-04-19. It is captured as `[announcement-light-*](screenshots)` evidence of the platform's last public state.

## Motion and focus

Everything interactive eases over `duration.fast` 0.2s (`easing.standard`): link colour hovers, pill borders, lazy-loaded media fades (0.5s `opacity`), and Vue view transitions (0.25s fade). Keyboard focus draws the browser's default outline only where an element is natively focusable; several link-styled `div`/`span` controls cannot take focus at all — see the Focus paragraph in [components.md](components.md#shared-values).
