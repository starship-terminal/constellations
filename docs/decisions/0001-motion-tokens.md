# 0001: Motion is recorded as tokens, plus a reduced-motion probe

Status: accepted by the owner on 2026-11-14, in [issue 74](https://github.com/starship-terminal/constellations/issues/74).

## Context

The library bootstraps apps from measured styles, and the Motion row of
[DESIGN-SYSTEM.md](../DESIGN-SYSTEM.md) asks for durations, easing curves and what
changes under reduced motion. In practice the packages answer it unevenly.
Claude and Linear have a duration scale from their own variables; most packages
have nothing, or a few numbers read off one hover. Nothing records which
properties transition, which animations and `@keyframes` a product ships, or
whether the product honours `prefers-reduced-motion` at all: the capture kit
never turned it on (the scorecard's F13 is capped at "partly" for that reason,
see [TODO.md](../TODO.md)). The issue asked how to define and reuse fluid and
motion animation in the design systems.

Three routes were open: record motion as tokens, record it as video, or both.

## Decision

Every package records motion as tokens, and the capture kit runs a
`prefers-reduced-motion` pass. No video recordings.

1. **Tokens.** A package that has run the probe carries a `core.motion` group in
   `tokens.json`: `duration` (ms), `easing` (cubic-bezier control points),
   `transition` (one DTCG composite per property, duration and easing seen on a
   real element), `animation` (one per animation name, with the properties its
   `@keyframes` set), and `$extensions` for which properties transition, the
   motion custom properties the product names, and keyframes it declares but no
   element used. Each token carries `$extensions.source = {evidence, capture}`
   with a label from [EVIDENCE.md](../EVIDENCE.md): Measured for a computed
   style, a rule or a custom property; Derived for a keyword expanded to its
   control points (`ease-out` to `0, 0, 0.58, 1`).
2. **Reduced-motion probe.** The kit's `motion-probe.mjs` reads every element's
   motion at rest with `page.emulateMedia({ reducedMotion: 'no-preference' })`,
   switches to `'reduce'`, and reads the same elements again. It records, per
   element, whether each transition and animation was removed (at or under 1 ms,
   the usual `0.01ms` reset), shortened, kept or changed, and a verdict for the
   page: `honours`, `partial`, `ignores` or `no-motion`. The product's own
   `@media (prefers-reduced-motion)` rules are copied beside it. The page's own
   `matchMedia` answer is stored for both passes, so a pass that did not take is
   visible.
3. **Shape of the readings.** Raw readings go to `raw/motion.json`; the product-free
   `tools/kit/build/motion.py` turns them into the token group, so every package
   gets the same shape and `build_tokens.py` only imports it. Values pass through
   the kit's `noUrl` before they are written, like every other computed value.

## Consequences

- A designer or agent can lift a product's motion the same way it lifts its
  colours: by token, with a label saying how far to trust it. The catalog export
  turns durations and easings into CSS custom properties; the composites
  (`transition`, `animation`) have no single CSS form and are listed as skipped,
  like typography.
- DTCG has no animation type. `$type: "animation"` is this library's extension,
  and `transition` is DTCG's composite with an extra `$extensions.property`.
  Consumers that do not know a type ignore it.
- Computed transitions are read at rest, so a duration declared only on `:hover`
  is not seen running. The probe also reads the stylesheets' own rules, and those
  durations appear in the group as Measured values marked declared, not seen at rest.
- A package captured before this decision keeps its own `core.duration` and
  `core.easing`. It gains `core.motion` the next time it is recaptured; nothing in
  `systems/` is rewritten for this decision.
- The scorecard's F13 wording is unchanged. A later rubric version could require
  the probe's readings (a `core.motion` group and a stated reduce verdict) for
  `meets`; that needs a rubric version bump and a re-review of every package, so it
  is left for its own change.
- Native iOS and desktop routes read screenshots, not CSS, and record motion as
  Not captured unless the app is an Electron one the probe can open.

## Out of scope

- **Video or screen recordings** of animations. They are large, cannot be diffed,
  and say nothing about the values; the owner ruled them out.
- **Spring physics and `linear()` curves** as tokens. DTCG's `cubicBezier` cannot
  carry them; the probe records the curve text under `notTokenised` and nothing
  more. JavaScript-driven animation (a spring library, the Web Animations API,
  canvas, Lottie) is not visible to computed styles and is not read.
- **Scroll-driven and view-transition animation**, other than `scroll-behavior`.
- **Naming the tokens by role.** The probe names durations by value (`200ms`) or
  by the product's own custom property; mapping them to roles (press, sheet, page)
  is the package's own `build_tokens.py`, as for colour.
- **Changing the rubric, the existing packages or the style guide's layout** beyond
  letting its Motion section read `core.motion` when present.
