# GitHub public design

Hand-written from [tokens.json](tokens.json) on 2026-11-22. Not produced by `make design-md`, because that command rewrites the catalog. `catalog.json` was left alone.

## Colour

Marketing pages paint light. The page is `#ffffff`. Body text is `#1f2328`. The display heading is `#000000`. Muted text is `#59636e`. Accent is `#0969da`. The quiet surface is `#f6f8fa`. The default border is `#d1d9e0`. Focus outline is `#0969da`.

Two greens sit next to each other. Primer's primary button rest colour is `#1f883d`, with hover `#1c8139` and active `#197935` as stylesheet variables. The hero "Sign up for GitHub" button paints `#08792b`. The header "Sign up" pill paints `#000000` with white text.

Danger emphasis is `#cf222e`. Success text is `#1a7f37`. Attention text is `#9a6700`.

The login wall paints dark when the colour scheme is dark. Page `#0d1117`, text `#f0f6fc`, muted `#9198a1`, accent emphasis `#1f6feb`, border `#3d444d`, inset `#010409`. The same dark page colour was read on a dark-forced public repository. Marketing pages were not forced dark. There is no theme toggle in the marketing header.

## Type

Display: Mona Sans, 56px, weight 440, line-height 61.6px. The homepage heading reads "Software still starts with you".

UI and body: Mona Sans VF, 14px, weight 400, line-height 21px.

Nav: Mona Sans, 14px, weight 400, line-height 24px. The Pricing link paints a 24px radius.

The header Sign up pill is Mona Sans VF, 16px, weight 400.

Neither font file is in this package.

## Space and size

The desktop header is 68px tall. The phone header is 52px tall. The header Sign up pill is 32px tall and 78px wide, padding `0 12px`. The search control is 36px tall. The hero Sign up button is 43px tall.

Spacing steps used here are 4, 8, 12, 16, 24, and 32px, from Primer's base size scale at 16px, except 12px which is the measured pill padding.

## Radius

Small 3px, medium 6px, large 12px. The header pill, the hero button, and the search control use 6px. The hero email field uses 8px. The Pricing nav link uses 24px.

## Components at rest

The header is a white bar: octocat, four menus, Pricing, Search, Sign in, and the black Sign up pill.

The hero is a black display heading, an empty email field (placeholder "you@domain.com"), a green "Sign up for GitHub" button, and a quiet "Download GitHub Copilot app" button on `rgba(0, 0, 0, 0.06)`.

Menus are white panels under the header. Search is a dialog with the placeholder "Search or jump to...". The phone menu is a full-screen white drawer with a black Sign up button and a Search field at the bottom.

The login wall is a card titled "Sign in to GitHub" with an empty username field and an empty password field. Identity buttons were not clicked.

## What this file does not claim

Hover, pressed, disabled, and loading were not photographed. Signup fields were not reached. Signed-in chrome was not captured.
