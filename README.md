# design-systems

One library of design styles captured from real products, so any project
(and any coding agent working in it) can say "make it look like Linear" and
find measured tokens, components and screenshots in one place instead of in
whichever project first needed them.

Each product is a self-contained package under [systems/](systems). Every
package has design tokens, a page that renders them, a component inventory
and screenshots of the real product, and says where each value came from.

## Browse it

Everything is one [Zensical](https://zensical.org) docs site: the gallery, the
scorecard and the library docs under `docs/`.

```bash
make setup
```

```bash
make serve
```

`make setup` installs the pinned Zensical into `.venv` once. `make serve` builds
the site and serves it at http://127.0.0.1:8800/:

- **Gallery**: one card per package with a cover screenshot, its colour roles and
  fonts, and a detail page with every screenshot, component crop and rendered
  README. Search matches names, uses, tags and themes; press `/` to focus it.
  "Copy agent prompt" copies instructions that point an agent at that package.
- **Scorecard**: every package graded against the checklist in
  [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md), as a heatmap with the evidence
  behind each grade. It is generated from [scorecard/](scorecard) by
  [tools/scorecard.py](tools/scorecard.py).
- **Docs**: the files under [docs/](docs), rendered.

The same site, minus the gallery, is published to GitHub Pages at
https://c-wenlong.github.io/design-systems/ with every page encrypted by
StatiCrypt, so it needs the password in the `STATICRYPT_PASSWORD` repository
secret. `make help` lists the other targets (`make check` validates
[catalog.json](catalog.json) against the packages).

## Catalog

| Package | Good for | Captured | Themes | Start at |
|---|---|---|---|---|
| [duolingo](systems/duolingo) | Gamified learning, lesson flow, chunky buttons, mascot-led brand | 2026-09-25 | light, dark | [README](systems/duolingo/README.md) |
| [brilliant](systems/brilliant) | Interactive lessons, course paths, calm editorial learning UI | 2026-09-25 | light, dark | [README](systems/brilliant/README.md) |
| [notebooklm](systems/notebooklm) | Source-grounded AI workspace, sources panel, chat | 2026-09-25 | light, dark | [README](systems/notebooklm/README.md) |
| [coursera](systems/coursera) | Course catalogue, course and module pages, course cards | 2026-09-29 | light, dark | [README](systems/coursera/README.md) |
| [gauth](systems/gauth) | AI tutor app, lesson players with a tutor panel | 2026-10-04 | light | [README](systems/gauth/README.md) |
| [researchrabbit](systems/researchrabbit) | Interactive graph beside a list | 2026-10-04 | light | [README](systems/researchrabbit/README.md), [graph.md](systems/researchrabbit/graph.md) |
| [manus](systems/manus) | Agent app shell, sidebar, a Library of agent outputs | 2026-10-17 | light, dark | [README](systems/manus/README.md) |
| [chatgpt](systems/chatgpt) | The baseline chat UI: thread, composer, history | 2026-10-04 | light, dark | [README](systems/chatgpt/README.md) |
| [claude](systems/claude) | A quiet chat shell, Artifacts, Projects | 2026-10-04 | light, dark | [README](systems/claude/README.md) |
| [hevy](systems/hevy) | Native iOS workout logging, dense set table, one accent, iOS 26 glass chrome | 2026-10-10 | light, dark | [README](systems/hevy/README.md) |
| [tokentracker](systems/tokentracker) | Local AI usage dashboard: borderless sidebar, rounded panel, hairline cards, one green accent | 2026-10-11 | light, dark | [README](systems/tokentracker/README.md) |
| [linear](systems/linear) | Dense, keyboard-first product UI, plus the marketing site | 2026-10-17 | dark, light | [README](systems/linear/README.md) |
| [polaris](systems/polaris) | Admin and commerce UI from a published component library | 2026-09-25 | light (dark experimental) | [README](systems/polaris/README.md) |

[catalog.json](catalog.json) holds the same list in a form a script or an
agent can read: the entry file, the tokens file, the style guide, the themes,
search tags, how it was captured, and where it was copied from.

## Using a style

1. Read the package's `README.md` (for example
   [systems/claude/README.md](systems/claude/README.md)). It says what was
   captured, how, and what to distrust.
2. Take values from the tokens file, never from a screenshot. Screenshots
   are stored as 256-colour PNGs to keep the repo small.
3. Open the package's `style-guide.html` to see every token and component
   rendered with the real values. Most open straight from disk; Polaris's
   fetches data, so open it through `make serve`.
4. Check the evidence label before copying a value: a measured CSS value and
   a reconstruction are not the same thing ([docs/EVIDENCE.md](docs/EVIDENCE.md)).

To point a coding agent in another project at a style, give it the package
path and tell it to read the entry file and `tokens.json` first, or install
the `design-systems` plugin from quiver-hub and ask for the style by name.
To build a design system for an app of your own, start from
[docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md): it lists the five layers a
complete system needs and how the captures here compare. The tokens
are W3C DTCG in Tokens Studio's multi-set layout, which Figma (through Tokens
Studio) and Style Dictionary both read.

## Layout

| Path | What it is |
|---|---|
| [systems/](systems) | One folder per product. Every package has `README.md` and `style-guide.html` at its top; [docs/PACKAGE.md](docs/PACKAGE.md) describes the rest |
| [catalog.json](catalog.json) | The machine-readable index, and the source the gallery is built from |
| [Makefile](Makefile) | `make setup`, `make serve`, `make docs`, `make check`, `make test`, `make clean` and more (`make help`) |
| [tools/catalog.py](tools/catalog.py) | Checks the catalog, builds the gallery, ranks packages for a query (`find`), exports any token file as CSS variables (`export`), checks WCAG contrast between token pairs (`contrast`), finds private text left in a package (`scan`), and writes each package's generated `DESIGN.md` (`design-md`) |
| [tools/redact_images.py](tools/redact_images.py) | Paints private regions out of finished screenshots and crops from a rectangle table per screenshot family, then OCR-checks every image against the redaction patterns. Rules live in [tools/redact-rules/](tools/redact-rules) |
| [tools/kit/](tools/kit) | The capture kit a new package starts from: web (public and signed-in), native iOS through iPhone Mirroring, and the token and style-guide builders |
| [docs/](docs) | The docs site's source: the library docs below, the home page, [docs/gallery/](docs/gallery) (the gallery app; its `data.json` and `thumbs/` are generated and gitignored) and the scorecard pages (generated into `docs/scorecard/`, gitignored) |
| [scorecard/](scorecard) | The scorecard's rubric (`criteria.json`) and one dated file per audit (`audits/<date>.json`, `<date>-2.json` for a second run that day). `make grade` writes a new one with the scripted criteria re-checked ([tools/grade.py](tools/grade.py)) |
| [tools/scorecard.py](tools/scorecard.py) | Writes the scorecard pages and the site's `zensical.toml` from [scorecard/](scorecard) |
| [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) | What a complete design system for your own app contains, layer by layer |
| [docs/PACKAGE.md](docs/PACKAGE.md) | What a package contains, file by file |
| [docs/EVIDENCE.md](docs/EVIDENCE.md) | How every value says where it came from |
| [docs/CAPTURE.md](docs/CAPTURE.md) | How to capture a new product, and the traps that cost time before |
| [docs/RIGHTS.md](docs/RIGHTS.md) | Why this repo stays private, and what is not ours |
| [AGENTS.md](AGENTS.md) | Instructions for coding agents working here |

## Where the packages came from

The nine "reference" packages were built in
[self-learn](https://github.com/c-wenlong/self-learn) under
`docs/design/reference/` for its redesign, and copied here byte for byte at
self-learn commit `84a260ac`. The Linear and Polaris audits were built
alongside a work project's designs and copied the same way, minus
their zip bundles and `node_modules`. [catalog.json](catalog.json) records each
source path. The packages' own prose still mentions the project they were
made for; that is history, and it is left as written.

## Requirements

Git LFS (`brew install git-lfs`, then `git lfs install`) before cloning, since
every image, archive and font is an LFS object. Python 3 to browse the
gallery and rebuild the reference packages; Pillow and Markdown for Linear's
builders; Node for Polaris's; a Playwright install only to capture.
