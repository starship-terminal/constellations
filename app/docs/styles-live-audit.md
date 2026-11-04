# Styles live interaction audit

Audited 2026-11-04 against https://styles.refero.design and the local app at
http://127.0.0.1:8845/styles. Browser observations and viewport screenshots are the
primary evidence. The source's current 2,000+ count and this repository's 1,342
snapshot are intentionally different. This audit does not recrawl the corpus.
Authentication, billing, and MCP integration/promotion are excluded.

## Coverage

- Gallery: search submission and clearing, all eight local suggestions, each local
  facet selector, combined filters/video, empty results/reset, source sort tabs,
  local extraction-date ordering, style-card navigation, and return breadcrumb.
- Raycast: video-bearing dark style; five media variants; controlled video playback;
  multi-image lightbox, Next, ArrowRight from the modal Close control, and Escape.
- AATHER: light style with one screenshot and no video; image-only detail and
  disabled Previous/Next in its one-image lightbox.
- Documents: all four local formats in both Compact and Extended; exact clipboard
  content after each selection; source/rendered Markdown, six rendered GFM tables,
  wrapping, download-button activation. The live source's Copy/Download success
  dialogs were observed. Automated download-event capture timed out, so this
  browser audit does not claim filesystem verification of download artifacts.
- Details: original font expansion and local font expansion; local font, spacing,
  and radius clipboard actions. The local screenshot lightbox is an additional
  capability; clicking the live source's preview did not open a lightbox.
- Narrow detail: 390 by 844 CSS pixels, keyboard ArrowRight between document tabs,
  and absence of page-level horizontal overflow after the fix. Temporary viewport
  overrides were reset.

This covers distinct controls and media/document branches, not every one of the
1,342 records. Not exercised here: every facet option, each resource article's
contents, every related-style destination, all capture failure fallbacks, downloads
on all browser engines, touch gestures, or every reconstructed component preview.
Existing data/export tests cover source separation and export safety separately.

## Findings and outcomes

| Control or page            | Live source behavior                                             | Local outcome                                                                                                                     | Priority/status                 | Evidence                                                        |
| -------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------- |
| Detail opening             | Preview above title and description; serif 48px heading          | Moved media first; title now uses existing serif, 48px desktop                                                                    | P1 fixed                        | reference-raycast.jpg, clone-raycast-after.jpg                  |
| Default document           | Highlighted Markdown source                                      | Source now opens by default; rendered reading view remains available                                                              | P1 fixed                        | reference-raycast.jpg, clone-raycast-after.jpg                  |
| Document tabs              | DESIGN.md, Tailwind v4, CSS Variables, Design Tokens             | Same order; arrow/Home/End navigation retained                                                                                    | P2 fixed                        | clone-raycast-after.jpg                                         |
| Document typography        | 13px monospace, 21.125px line height                             | Matched measured font size and line height using existing mono font                                                               | P2 fixed                        | reference-tokens.jpg, clone-tokens.jpg, clone-raycast-after.jpg |
| Font and type-scale values | Copyable font names and specimen samples                         | Added copy controls; samples use captured family or first captured font fallback                                                  | P1 fixed                        | Browser clipboard: SF Pro                                       |
| Font expansion             | First three fonts, Show all four on Raycast                      | Added Show all / Show fewer fonts                                                                                                 | P2 fixed                        | Browser state and clipboard checked                             |
| Type-scale order           | Large specimens first; 19 current source measurements            | Local semantic scale now largest first; retained eight captured rows                                                              | P2 fixed within snapshot limits | Source/live content differs; no values invented                 |
| Spacing and radii          | Clicking values copies exact text                                | Added copy controls with accessible status                                                                                        | P1 fixed                        | Browser clipboard: 1200px, 99999px                              |
| Color group order          | Brand, Accent, Neutrals                                          | Same ordering while retaining captured tokens and roles                                                                           | P2 fixed                        | Browser DOM comparison                                          |
| Detail panels              | Equal desktop panes, independent scrolling                       | Preserved existing split and independent scrolling                                                                                | Passed                          | clone-raycast-after.jpg                                         |
| Narrow detail              | Separate narrow presentation                                     | Local stacked detail, scrollable tab row and wrapping toolbar; fixed hidden feedback element causing 28px overflow                | P1 fixed                        | clone-mobile-detail.jpg; 390px viewport/document width          |
| Gallery width              | Three broad cards, 1,514px content at 1,707px viewport           | Increased content container to match observed width                                                                               | P2 fixed                        | clone-gallery-after.jpg                                         |
| Sort tabs                  | Trending, Popular, Newest                                        | Added Name A–Z and honest Newest capture based on extracted_at; no source popularity ranks available                              | P2 partial                      | clone-gallery-after.jpg; canonical catalog is alphabetical      |
| Search prompts             | Eight changing suggestions drawn from a larger pool              | Fixed observed labels now run representative canonical-facet searches                                                             | Deliberate difference           | reference-gallery-search.jpg                                    |
| Gallery hero               | Rotating headline and color animation                            | Same four observed phrases cycle with measured gradient stops and 3s sweeps; reduced-motion setting keeps the first phrase static | P3 fixed                        | reference-headline.jpg, clone-headline-animated.jpg             |
| Gallery taxonomy           | Current source does not expose local facet rows                  | Local theme/type/style/industry/tag/video filters retained                                                                        | Deliberate local capability     | clone-gallery-after.jpg                                         |
| Source preview             | Looping scrolling recording above title                          | Manual screenshot/video/detail/poster choices retained                                                                            | Deliberate local capability     | reference-raycast.jpg, clone-raycast-after.jpg                  |
| Lightbox keyboard          | Source preview does not open a lightbox in observed click        | Added ArrowLeft/ArrowRight/Home/End to local lightbox; Escape and focus restoration retained                                      | P2 fixed                        | Browser verified image 1 to 2, then Escape                      |
| Single image               | AATHER exposes still preview, no recording                       | Only Screenshot choice, Previous/Next disabled                                                                                    | Passed                          | reference-still-only.jpg, clone-still-only.jpg                  |
| Export actions             | Copy/download succeeds then shows MCP promotion                  | Local copies raw bytes; downloads without MCP promotion                                                                           | Passed, promotion excluded      | All eight clipboard variants verified                           |
| Resource footer            | Links to DESIGN.md examples, AI design resources, Design prompts | No equivalent local article pages                                                                                                 | P3 open                         | Initial live gallery accessibility inventory                    |

## Export verification

Clipboard character lengths on Raycast, after loading each selected variant:

| Format        | Compact | Extended |
| ------------- | ------: | -------: |
| DESIGN.md     |  15,792 |   31,167 |
| Tailwind v4   |   1,005 |    4,244 |
| CSS Variables |   1,020 |    4,952 |
| Design Tokens |   5,149 |   25,403 |

Both scrolling and detail videos reached readyState 4 without media errors. Pressing
Space on the scrolling video started playback (36.1 second duration).

Evidence directory outside the repository:
`/Users/kaichen/.codex/visualizations/2026/11/04/01a1a46a-864d-7642-b38b-a9be7ab0f58f/full-audit/styles/`.

Validation: focused style-data and export tests passed (11 tests), app typecheck
passed after concurrent feature files landed, and changed source files passed
Prettier. An earlier full test run passed all 95 tests before the added capture
ordering test.

## Headline follow-up

The live rendered stylesheet supplied the sweep colors, stops, 110-degree outgoing
and -70-degree incoming angles, and three-second transition keyframes. The local
headline now uses those measured values and all four observed phrases. The six-second
cycle interval is a local implementation choice; the live transition duration was
measured, but its hold interval was not separately instrumented. Hidden measuring
phrases keep layout height stable, and assistive technology receives one fixed
heading. A reduced-motion preference disables the timer and sweep, including changes
to that preference while the page is open. This preference path was reviewed in code;
the browser used for screenshots reported reduced motion off.

Search suggestions now show the observed eight-label set. The local snapshot uses
canonical facet queries for semantic labels such as Non-boring enterprise (corporate)
and Chalk & charcoal (monochrome); suggestions remain deterministic across renders.
The Retro web nostalgia control was verified to set q=retro in the URL and search
field. No live popularity metrics were inferred.
