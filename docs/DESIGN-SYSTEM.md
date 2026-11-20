# What a design system contains

The packages under `systems/` are captures: what could be measured from someone
else's product. This document is the other half. It says what a complete design
system for an app of your own needs, so that a person or an agent can build one,
and so a capture can be graded against the same list.

A design system is five layers. Each one is built from the layer below it.

| Layer | Answers | Lives in |
|---|---|---|
| Principles and voice | Why does it look and read this way? | `README.md` |
| Patterns | How do components combine to do a common job? | `patterns.md` |
| Components | What are the building blocks, and how does each behave? | `components.md` |
| Foundations | What are the named values everything is made of? | `tokens.json` |
| Assets | Which icons, fonts, logos and images may be used? | `assets/` |

Accessibility and theming are not layers of their own. They are requirements on
every layer, listed under each one below.

The checklist is written for the web. A mobile app (iOS, Android) or a desktop
app (macOS, Windows) needs some items in another form: touch has no hover, the
system font needs no fallback stack, and the platform supplies controls and
materials of its own. Each layer below says where mobile and desktop differ,
and the scorecard grades every package against the wording for its platform
(its `platform` in [catalog.json](../catalog.json)). Where nothing is said,
the web wording applies to all three.

## The folder

A design system for an app is one folder, `design-system/`, at the root of the
app's repository:

```
design-system/
  README.md          entry: principles, voice, how to use it, what is unfinished
  tokens.json        foundations, W3C DTCG, same layout as the reference packages
  components.md      one entry per component
  patterns.md        one entry per pattern
  assets/            icons, logo, illustrations, font licences
  style-guide.html   optional: a page that renders tokens.json
```

`tokens.json` is the source of truth. Code reads from it (as CSS custom
properties, a Tailwind theme, a Swift file or whatever the stack uses), and no
component hard-codes a value that a token holds. If a tool wants a `DESIGN.md`
(the format Google Stitch and the `impeccable` skill read), generate it from
this folder; do not keep it by hand beside it.

## Foundations

Two kinds of token, and the difference is the most useful idea in this file.

A **primitive** token is a raw value with a name that says what it is:
`gray.900 = #0b0b0b`. A **semantic** token says what a value is for, and points
at a primitive: `text.primary = {gray.900}`. Components only ever use semantic
tokens. Dark mode is then a second semantic set that points the same names at
different primitives, and no component changes.

In `tokens.json` this is a `core` set of primitives plus one semantic set per
theme (`light`, `dark`), the layout the reference packages here use. The two
audit packages (linear, polaris) name their sets differently; see
[PACKAGE.md](PACKAGE.md).

| Group | Must include |
|---|---|
| Colour, primitives | A ramp per hue you use (neutral first), 10 or so steps from lightest to darkest |
| Colour, semantic | Backgrounds: page, surface, raised, overlay, scrim. Text: primary, secondary, disabled, on-accent, link. Borders: default, strong, focus. Accent: default, hover, pressed. Status (success, warning, danger, info), each with fill, text and border |
| Type | Families with fallback stacks. A scale of 6 to 8 sizes. Weights. Line heights. Named roles built from those: display, heading levels, body, label, caption, code |
| Spacing | A scale on one base unit (4 or 8 px) |
| Shape | Corner radii, border widths |
| Sizing | Control heights per size (sm, md, lg), icon sizes, the focus ring's width and offset |
| Elevation | 3 to 5 shadow levels, each tied to a use (card, popover, dialog) |
| Motion | Durations, easing curves, which properties transition, animations and their keyframes, and what changes under reduced motion ([how the library records it](decisions/0001-motion-tokens.md)) |
| Layout | Breakpoints, content widths, grid columns, z-index layers |

On mobile and desktop, five groups read differently:

| Group | Mobile | Desktop |
|---|---|---|
| Accent | Default and pressed; touch has no hover | As on the web |
| Type | The platform text styles the product uses (Dynamic Type or the Material type scale), with sizes, weights, line heights and named roles. A system font needs no fallback stack | Families, a scale of 6 to 8 sizes, weights, line heights and named roles. A system font needs no fallback stack |
| Sizing | Control heights, icon sizes, and touch targets (44 pt on iOS, 48 dp on Android) | As on the web |
| Elevation | Shadows or materials (blur, glass) in 3 to 5 levels, each tied to a use | Shadows or materials (vibrancy) in 3 to 5 levels, each tied to a use |
| Layout | Screen margins, safe areas, the screen widths supported, and the layers sheets and modals sit on | Window sizes, sidebar and inspector widths, and layers |

Done when: every colour, size and duration in the app's UI code resolves to a
token (check pairs with `python3 tools/catalog.py contrast`); text on its background meets WCAG AA contrast (4.5:1 for body text, 3:1
for large text and for borders and icons that carry meaning); and every
semantic colour exists in each theme the app ships.

## Components

One entry per component in `components.md`. The set most apps need first:
button, icon button, link, text field, text area, select, checkbox, radio,
switch, tabs, menu, tooltip, dialog, toast, card, list row, table, avatar, badge.

A mobile app needs its own set of 19: button, icon button, link, text field,
text area, select or picker, checkbox or toggle, radio or segmented control,
switch, tab bar, navigation bar, menu or action sheet, sheet, dialog or alert,
toast or banner, card, list row, avatar, badge. A desktop app needs the web set,
plus a toolbar, context menu and inspector when it has them. The scorecard
counts a package complete at 17 of its platform's 19.

Each entry covers:

| Part | What it says |
|---|---|
| Anatomy | The named pieces (label, icon, container, helper text) |
| Variants | The visual kinds and when to use each (primary, secondary, quiet, danger) |
| Sizes | Each size and its height, padding and type role |
| States | Default, hover, focus-visible, pressed, selected, disabled, loading, error, as each applies |
| Tokens | Which semantic tokens it uses, per state |
| Behaviour | Keyboard and screen-reader behaviour, and what happens on click, submit or dismiss |
| Do and don't | Two or three real misuses to avoid |

Done when: every state is specified, not only the default one; the focus ring
is visible on every interactive component; touch targets are at least 44 pt on
iOS, 48 dp on Android and 24 px on the web; and nothing in an entry is a raw
value instead of a token.

On mobile, touch has no hover or focus-visible, so the states to specify are
pressed, selected, disabled, loading and error, as each applies. A visible
focus state is needed on text inputs, and on keyboard focus where the platform
shows it. Desktop follows the web.

## Patterns

A pattern is a recurring job that several components do together. One entry
per pattern in `patterns.md`, each with when to use it, the components it uses,
the layout, and an example screen.

The patterns most apps need: the app shell (navigation, header, page layout);
forms and validation (where errors appear, when they appear, how to recover);
empty, loading and error states for every list and page; confirming destructive
actions; feedback after an action (toast, inline, none); search and filtering;
data display (list or table, sorting, pagination); onboarding and first run.

Done when: every page in the app can be described as patterns from this file,
and every list says what it shows when it is empty, loading, and failed.

## Principles and voice

Three to five principles in `README.md`. A principle earns its place by
deciding a real trade-off: "Dense over spacious: experts scan 50 rows at once"
settles arguments; "Simple and delightful" settles nothing. Give each one an
example of a choice it made.

Voice covers tone, capitalisation (sentence case or title case, applied
everywhere), the app's own vocabulary (one word per concept), and a formula for
messages: what happened, why, and what to do next.

Done when: two people designing the same new screen would make the same calls
on density, emphasis and wording.

## Assets

The icon set (one family, its sizes, its stroke width, how icons pair with
text), the logo and its clear space, the illustration or imagery style if
there is one, and the licence for every font and icon set used.

Done when: every asset in the app comes from `assets/` or a named, licensed
source, and nothing is borrowed from a captured product ([RIGHTS.md](RIGHTS.md)).

On mobile and desktop, naming the system icon set (SF Symbols, Material
Symbols) can take the place of an index of icons by role. Fonts are still named
with their licence or fallback.

## Building one in stages

A complete system is a lot to write at once. Build it in this order and use
the app at the end of each stage:

1. **Foundations and five components.** `tokens.json` with light and dark,
   plus button, text field, card, dialog and toast with all their states.
   Enough to build real screens without inventing values.
2. **The rest of the components**, as screens need them.
3. **Patterns and principles**, once there are enough screens to see what
   repeats and which trade-offs keep coming up.

Starting from a captured package is a good way to get stage 1 quickly: take
its foundations as a starting point, then change the brand colours, logo and
type to your own. Its structure and proportions are fine to borrow; its brand
is not.

## How the captured packages compare

The packages here record what was observable, so they are strong on
foundations and thin on the layers a product does not publish.

| Layer | What a package has |
|---|---|
| Foundations | Strong. Every token names its source; most are measured CSS, but some are sampled from screenshots or reconstructed (Linear's app colours, for one), so check the label before copying ([EVIDENCE.md](EVIDENCE.md)) |
| Components | Partial. Crops of real components and some states; no behaviour specs |
| Patterns | Screenshots of whole pages, but no written patterns |
| Principles and voice | Almost none. A capture cannot see the reasons |
| Assets | Icons where licensing allowed; no fonts |

When the scorecard grades a capture, three criteria are **optional**:
principles (V1), voice (V2) and per-component behaviour (C5). They count when
the product publishes them (a design-system site, a content guide) and are
otherwise graded not applicable, never missing, because a capture records how
a product looks, not why. Every other criterion is required. For a design
system of your own, all of them are required.

Polaris is the exception, because Shopify published its system. Read its
package to see what the upper layers look like when they are written down.
