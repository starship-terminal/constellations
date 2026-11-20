# Delphi patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Public chrome (light)

A 64px top bar (`core.component.topbar-height`, 91.5px wordmark `core.component.logo-width`) floats over the page: a ghost Sign In and the `#fd5400` Create Your Delphi pill (`light.action.accent` → `brand.accent`, white text `light.action.accent-fg`). Every surface paints the light theme signed out: a white page (`light.background.page` → `background.default`), `#21201c` ink (`light.text.ink` → `fg.high`), mid `#63635e` and low `#82827c` text (`light.text.mid`, `light.text.low` → `fg.mid`/`fg.low`), warm `#f7f3f0` cards (`light.background.warm`), `#f9f9f8` secondary surfaces (`light.surface.secondary`), a 1px hairline stroke (`core.border.hairline`) at `rgba(33,32,28,0.09)` (`light.border.hairline`).

## The ask hero

Home and every /discover/<topic> page open with a Delphi Pythia display heading (`core.font.family.display`, `core.font.size.measured.display` 50px, 32px at 390px `core.font.size.measured.mobile-display`) over a wide centered ask field — 664px on search results, 624px on home (`core.component.query-field-width`, `core.component.search-field-width`): a white pill on `light.surface.primary` with a `#dad9d6` border (`light.border.default`) and a microphone control. Under it, a horizontally scrolling row of topic chips on `light.background.chip` that invert to `#f15a24` brand orange (`light.brand.accent`) on the selected topic.

## The card grids

- **Topic cards** (`topic-card`, `disc-card`): ~347px cards (`core.component.topic-card-width`) with a small Delphi glyph and a question in Inter — the card colour is picked per card from the palette scales (maroon, forest, navy…), question text in `light.text.on-dark` `#f0eae4` with a brand-orange accent span.
- **Perspective flip cards** (`persp-flip`): a 272px two-sided card (`core.component.flip-card-width`) — Read flips it locally to the quote side (measured `persp-flip-flipped`), Back returns it. No navigation, no account.
- **Expert strip and knowledge sections** (`home`): cards linking to public profiles with a `light.action.share` tinted control (`rgba(33,32,28,0.1)`), and a promoted knowledge panel whose Create action is the one element that needs an account.

## Search results

/search/<question> renders signed out: the question itself sits in the ask textarea (`srch-field` — the page's heading equivalent; there is no visible h1), followed by a "Top perspectives" section of `blockquote.perspective-bubble` quotes, then 672px expert result cards (`srch-expert-card`, `core.component.expert-card-width`) on `light.surface.primary` with a `span.brand-tag` credential badge on `light.background.badge` (`rgba(33,32,28,0.06)`), Save and Expand actions — measured, never pressed: both need an account.

## The expert profile

/<expert> (captured at /karpathy): a 110px portrait (`core.component.portrait`), name, bio and stats in the profile header, a `main`-scoped Share action (a hidden duplicate exists — the visible one was measured), topic sections, and a promoted Start-chatting pill. All content is expert-authored product content — names, quotes, bios and portraits are evidence, not reusable primitives.

## The chat composer

/<expert>/chat: a header with the expert identity, a thread of perspective bubbles (Pythia quote text on `light.bubble.accent` hints), suggested-question chips, and a 592px bottom composer (`core.component.chat-input-width`) — a white bordered field with a microphone and a 48px send button (`core.component.send-size`) that only exists while the field has text (`chat-send` was measured with text filled, then cleared — never sent).

## Dialogs

Two mounts of the same Sign-In dialog (`signin-dialog`): /auth on home, and /onboarding for signed-out visitors — the create-a-clone flow itself is behind an account. A 448px white card (`core.component.dialog-width` on `light.popover.default`) under `core.shadow.dialog`, over a dimmed/blurred page: Delphi logo, "Sign in to your account", a 400px dark Continue-with-Google pill (`core.component.dialog-button-width`, `light.action.dark-button` → `primary.default` `#21201c`), a bordered Continue-with-Email button, ToS/Privacy links. Measured, never submitted.

## Mobile (390px)

The phone surface is the same light theme: a compact 64px header (`core.component.mobile-topbar-height`), topic cards stacked vertically (`m-topic-card`), and the chat surface with the same composer. No separate mobile tokens — the same light set resolves.

## Motion and focus

Delphi ships a real motion vocabulary in `core.motion.*`: `arrive` entrances (0.3s out-quint, delayed), `lean-in-*` badge loops, `typing-dot`/`typing-dot-wave` indicators, plus `spin`/`pulse`/`ping`; a 0.15s out-quart control transition (`core.motion.control`); durations `enter`/`exit`/`move` and `easing.*` cubic-bezier curves. Focus-visible is an ink ring (`light.ring` declares `#fd5400` — brand orange in the ring role); forced-:active pressed states are recorded as mechanical evidence (DevTools-forced, not real mousedown).
