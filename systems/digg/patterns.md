# Digg patterns

How the measured components combine into the public pages. Every value resolves in [tokens.json](tokens.json); the components are in [components.md](components.md), the crops in [components/crops/](components/crops), the full pages in [screenshots/](screenshots).

## The sidebar rail

Every surface carries a fixed left rail over the `#fdfdff` page (`light.background.page`): the digg wordmark, then 231x40 full-pill nav rows (`core.component.sidebar-item`, `core.radius.pill` = `calc(infinity * 1px)`) — Home, Technology, Gaming, Entertainment, World & Business, Science, Sports, AI — at 14px semibold in `#161617` (`light.text.ink`, `{foreground.default}`). The selected row fills `#f0f0f5` (`light.background.fill`, `{sidebar.accent.default}`); the rest ride transparent. Below the scroll: the theme pill (System -> Light -> Dark, 26px control radius), a Log in row and the primary `Sign up` CTA — white text on `#1c66eb` (`light.action.primary`, `{primary.default}`) in the same 231x40 footprint.

## Feed controls

The feed opens with a right-aligned control pair at 36px tall: the `Trending` sort dropdown (`feed-trending`, 105x36, `core.radius.control` 26px, translucent input wash `light.background.input-fill` over a `#e5e5e5` `{input}` border — the opened state is measured) and the `Compact` density toggle (`feed-compact`, 64x36, same recipe). On the category pages the pair trades places with a 30px bold category heading (`cat-title`, `core.font.size.measured.page`).

## The story card

The feed's unit is a 704px card (`post-card`, `core.radius.card` 18px, `core.component.story-card` 183px): a 16px semibold headline (`post-headline`, `core.font.size.measured.headline`, tracking -0.12px) over a 14px muted summary (`post-summary`, `light.text.muted` ink@70%), then the action row — the vote pill (`post-vote`, 32x24, full pill, `#1c66eb` @20% border over the page fill, the count in vt323 odometer digits), the 32x32 comment link (`post-comment`), the 24px source-avatar cluster (`post-avatars`) and the `'N Sources'` link (`post-sources`, 2px tight radius, `light.text.muted`). A 120x80 thumbnail (`post-thumb`, `core.component.thumb`) sits right. Category feeds and `/u/<source>` profiles reuse the identical card (`cat-card`, `pf-card`).

## The right rail

Two white panels ride beside the feed on `rgba(0,0,0,0.08)` hairlines (`light.border.hairline`, `{border.default}`) at 376px wide (`core.component.rail-card`): **Top Contributors** (`rail-contribs`, 376x352) — ranked users with the `#e37b4c` rank-one accent (`light.text.rank-one`, `{rank.one.default}`) — and **Top Posts Yesterday** (`rail-posts`, 376x556) — numbered story rows with mini thumbnails. In dark they repaint `#1c1c1f` (`dark.background.card`, `{card.default}`) on rgba(255,255,255,0.08) hairlines.

## The story page

A story detail page stacks: the tracked-out REPORT kicker (`st-kicker`, 16px), the 36px bold headline (`st-h1`, `core.font.size.measured.display`, 672px column), the 20px muted summary (`st-summary`, `core.font.size.measured.deck`), the 138x44 digg-it pill (`st-vote`, `core.component.digg-it`, `core.radius.vote` 999px — primary-blue @20% border, hover/focus/pressed measured) and the `'N Sources'` meta row. The right column holds the 376x384 stat card (`st-stat` — TODAY'S RANK over COMBINED VIEWS in one panel) and the sources list (`st-srclist`, 376x246) — all white cards on the hairline at 18px. Below, the TLDR label (`st-tldr`, 10px tracked-out caps) over 18px medium paragraphs (`st-para`, `core.font.size.measured.lead`, 31.5px leading) in a 605px measure.

## The auth surface

`/login` and `/sign-up` paint the Clerk card: a 24px semibold heading (`lg-h1`, `core.font.size.measured.card-title`), the Google and X OAuth outline buttons (`lg-google`, `lg-x`, 353x36, full pill, `light.action.oauth-fill` page-fill on hairline), the 8px email and password fields (`lg-email`, `lg-pass`, `core.radius.field`, `#e5e5e5` `{input}` border, the capture's one real shadow — `core.shadow.field` 0 1px 2px rgba(0,0,0,0.05)), the primary `Continue` pill (`lg-continue`, `#1c66eb` on white text, 0.1s auth transition) and the 13px sign-up link (`lg-signup`, `light.text.link` = `{primary.default}`). Focused and filled field states are measured; nothing was ever submitted.

## Dark theme

The sidebar pill cycles System -> Light -> Dark and the whole surface repaints: `#161617` field (`dark.background.default`), `#1c1c1f` cards, `#fdfdff` ink (`dark.text.ink`), ink@70% muted, rgba(255,255,255,0.08) hairlines (`dark.border.hairline`), white@4.5% control washes — the `d-*` components are real measured dark paint. The `#1c66eb` primary is identical in both themes; the focus ring switches `#ababbf` -> `#1c66eb`.

## Mobile

At 390 wide the sidebar collapses to a 107px top bar (`m-bar`, `core.component.mobile-bar`, the page's near-white fill) over the same story card (`m-card`, 390x207) and a muted feed footer (`m-footer`, 358x48). The vote pill keeps its 32x24 footprint (`m-vote`).

## Boundaries

- Voting, commenting, submitting, following and settings need an account and were never reached — the controls gate on sign-in.
- The `'N Sources'` links and story links point at external publications; they were measured, never followed.
- A cookie banner painted on first load; hidden for screenshots only — no consent choice was made.
