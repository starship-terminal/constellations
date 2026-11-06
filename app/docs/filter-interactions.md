# Catalog filter interactions

Observed in the signed-in Refero web and iOS catalogs on 2026-11-04, by clicking
through the search picker and result modes in the browser.

- Selected products and taxonomy terms appear as typed chips inside the search
  field. Selecting a suggestion clears the draft and closes the picker.
- Empty search opens a taxonomy rail and three-column groups of terms. Web has
  Page Types, Flows, UX Patterns, UI Elements, Categories and Fonts; iOS has
  Screen Types, Flows, UX Patterns, UI Elements and Categories.
- Typing switches to a flat suggestion list. The local app offers keyword search,
  products and taxonomy matches; it does not claim Refero's semantic suggestions.
- Clicking a chip removes it. Backspace in the empty input removes the last chip.
  The trailing X clears all selections. Escape and backdrop clicks dismiss.
- Tab and Shift+Tab cycle taxonomy groups while focus stays in the input. Arrow
  keys navigate suggestions; Enter selects. Reopening starts at the first group.
- Taxonomy selections intersect, including two terms from the same group. Product
  selections form alternatives. Counts describe the platform's whole corpus,
  independent of currently selected products and terms.
- Platform changes map compatible term labels and remove incompatible selections.
  Screens/Flows switching preserves the current selections.
- Web screen results use two columns at normal desktop widths, product captions
  and no additional filter panel, title row, filename row or sort toolbar.

## Local data

SQLite migration v5 stores explicit per-media taxonomy assignments, seeded from
`src/data/media-taxonomy.json`. Regenerate with
`python3 app/scripts/build-media-taxonomy.py`; use `--check` for freshness.
Filename rules are conservative local classifications, not Refero annotations.
Font assignments inherit recorded primary package fonts and exclude fallback
font families. Each assignment records its reason and origin. The seed is imported
once; restarting or regenerating it does not overwrite manual database edits.

This collection has no verified ordered flows. Flows therefore shows an explicit
empty state until actual sequences are imported; individual captures and crops
are not presented as flows.

## Verification

Browser checks covered product autocomplete with Down/Enter, typed taxonomy
selection, immediate closing, Backspace removal, Escape, Tab group switching,
all iOS taxonomy groups, platform switching and Screens/Flows selection retention.
Automated tests cover term intersection, product alternatives, counts, malformed
terms, live classification edits, migration preservation and platform mapping.
