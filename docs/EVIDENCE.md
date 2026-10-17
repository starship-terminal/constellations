# Evidence

A design reference is only as useful as your ability to tell a measured
value from a guess. Every package says, value by value, where each number
came from, so a reader can decide how far to trust it.

## The rule

Read values from the product's own CSS, computed styles or published
packages. Never sample a colour from a screenshot when the CSS can be read.
When sampling is the only way in (a signed-in app that cannot be inspected,
a canvas), say so on the value.

## The labels

The two source projects used slightly different words for the same ideas.
New packages use the left column.

| Label | Meaning | How the reference packages say it | How the audits say it |
|---|---|---|---|
| Measured | Read from a declared custom property or a computed style on a real element, in a stated state, theme and width | `$extensions.source` naming the file, selector, dump or element | Measured CSS |
| Derived | Worked out from measured values (a rem converted to px, an alias resolved, a scale completed) rather than read directly | "derived, not captured" | (inside Reconstruction) |
| Sampled | A flat colour read off a screenshot pixel. A displayed sRGB value, not proof of the token behind it | "estimated from screenshot" | Sampled pixels |
| Observed | A component or state is visible in a capture, with no values read from it | listed in `components.md` with a crop | Observed |
| Reconstruction | A redraw or a suggested value, made to be usable. Dimensions and behaviour may differ from the product | (not used; the reference packages do not redraw) | Reconstruction |
| Not captured | Out of reach, not enabled, or left out on purpose | the Gaps section of `components.md` | Not inspected |

## Where to find it

| Package shape | Per value | Per package |
|---|---|---|
| Reference | `$extensions.source` on every token in `tokens.json`; values DTCG cannot hold under `$extensions.notTokenised` | README "How the values were read", the Gaps in `components.md`, everything under `raw/` |
| Audit | The label column in `README.md`'s tables | Linear: `raw/coverage.json`, `raw/validation.json`, `raw/capture-manifest.json`. Polaris: `raw/token-parity.json` |

## Things the packages already warn about

- Linear's app colours are sampled pixels from dark screenshots; only the
  public site's values are measured CSS, and no light app theme exists.
- Claude's code blocks keep the dark theme's inline colours in the light
  renders; read code colours from the dark captures.
- Screenshots everywhere are 256-colour PNGs. Flat UI colours survive
  exactly, but read values from the tokens, not the images.
- Polaris live specimens use React package 13.9.5 while the archive declares
  13.10.1; the token values match the archive with zero differences.
