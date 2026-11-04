# Catalog and screenshot interaction audit

Audited Refero and the local app on 2026-11-04. Chrome showed the public catalog; a signed-in in-app browser supplied the actual screenshot viewer and board controls. Authentication, pricing, MCP, and account changes were excluded. The original account and boards were read only.

| Interaction        | Original Refero                                                  | App result                                                                                                  |
| ------------------ | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| App directory      | Categories and product cards open app-filtered screen results    | Cards open `view=screens&referenceId=…`; Package details retains measured documentation                     |
| Screen search      | Screens, active taxonomy chips, counts and sorting               | Actual capture search, removable filters, counts, Latest and Name sorting                                   |
| Filters            | Page Types, Flows, UX Patterns, UI Elements, Categories, Fonts   | Actual capture platform, theme, tag, group and UI element crops; media-only scope searches capture metadata |
| Screenshot viewer  | Full viewport, image left, metadata right, independent scrolling | Same structure with recorded capture tags/group, product information and package links                      |
| Viewer movement    | Previous/next, keyboard arrows, count, Escape                    | Preserved result set, qualified URL selection, reset image scroll, opener focus restored                    |
| Save screenshot    | Save-to picker selects named boards and creates a board          | Named-board picker, membership/count feedback, Create & save, Cancel, board screen grid and removal         |
| Existing saves     | Boards contain screens                                           | Package references and independent flat screenshot bookmarks remain available                               |
| Inspector metadata | Clickable metadata opens filtered results                        | Measured package chips open genuine Screens filters; Package details opens the measured package             |

The captured corpus does not record Refero’s original screen classifications, ordered flows, or popularity ranking. The app uses the available capture metadata and sorting fields. Measured packages and interpreted styles remain separate sources.

## Live checks

- Original: category selection, directory scroll, Claude app results, Dashboard taxonomy selection (110 pages to 2), Trending sort, Screens/Flows switch, public flow arrows/Escape, signed-in screenshot detail, Save-to picker, Bookmarks, Create New Board and Cancel.
- App: platform/category filtering, query/clear, package access, Screens and crop views, capture tag filtering (24 captures to 7), Name sorting, removable chips, viewer button/keyboard navigation, Escape/focus restoration, flat save/unsave, named-board save/membership/count, board viewer and association removal.
- Nested board dialog: board-name arrow keys keep the outer screenshot unchanged; Escape closes only the picker and restores its trigger focus. Cancel creates no board. Closing clears unfinished creation fields.
- Local save tests restored prior flat bookmarks and board contents. The existing board retained its original package reference.

## Recovery checks

Screen identities retain both package and asset identity. Pagination preserves earlier pages, retries the failed page, and cannot skip a failed page through Show more. Filter changes clear old results, including media-only scope changes. A selected screen outside the first loaded page recovers through the exact-screen API; missing selections expose retry and dismiss controls. Package document hashes tolerate malformed encoding.

Final targeted verification passed: TypeScript and 23 tests across package details, library loading, screen queries, saved media, and inspector previews. The parent change runs the complete app tests and production build.

Screenshots and the detailed audit are stored outside the repository in the task’s `full-audit/catalog` evidence folder. The evidence includes original catalog/taxonomy/viewer/save picker captures and app screen-grid/filter/viewer/board-save/board-detail captures.
