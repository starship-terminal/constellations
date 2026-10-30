# AGENTS.md

Instructions for coding agents working in this repository, or reading it from
another project.

## What this is

A private library of design styles captured from real products, rendered as a
static docs site. Two stores of styles:

- `systems/<slug>/`: the packages, one per product, measured from real
  captures and indexed in [catalog.json](catalog.json). Values here carry
  per-value evidence labels and are the only ones to design from.
- `refero/<slug>/`: a snapshot of styles.refero.design (1,342 styles),
  third-party interpreted data at lower confidence. Breadth for inspiration,
  never the source for a value a package holds.

[README.md](README.md) is the human front door; the docs below hold the
detail. Everything a person browses (gallery, scorecard, library docs) is
the one site built by [tools/site.py](tools/site.py) from this tree.

## Map

```
catalog.json            index of every systems/ package: slug, platform, tags,
                        goodFor, preview paths, capture provenance
systems/<slug>/         the packages (40). Standard parts:
  README.md               Brief (generated) + what was captured + Health (generated)
  tokens.json             every value, evidence-labelled
  DESIGN.md               generated export, one theme, no provenance
  style-guide.html        renders every token, light/dark toggle
  icon.png                the product's app icon, 128 px PNG (LFS)
  components.md, patterns.md, components/, icons/, screenshots/, boards/, raw/
  tools/                  the builders that produced the package; fixes go here
refero/                 third-party style snapshot. refero.db (sqlite, LFS) is
                        the canonical store; <slug>/ holds DESIGN.md, CSS and
                        token exports, meta.json; catalog.json is the flat
                        index. refero/README.md has layout + refresh commands
docs/                   source of the site
  index.md, *.md            the library docs (table below) + TODO.md (open items)
  gallery/                  the gallery app (app.js, index.html, style.css);
                            data.json, thumbs/, refero/, export/ are generated
                            (gitignored) by `tools/catalog.py build`
  scorecard/                generated scorecard pages (gitignored)
  assets/, stylesheets/, site.webmanifest
scorecard/              criteria.json (the rubric, per-platform wording) +
                        audits/<YYYY-MM-DD>.json snapshots
tools/                  the repo's scripts (python3, stdlib only; Pillow/sips
                        for images). Refero pipeline lives in tools/refero/;
                        tools/kit/ is the starter kit for a new package;
                        tools/redact-rules/<slug>.json are per-package masks
scripts/                ops, not library: dev.sh backs `make dev`;
                        deploy_trigger.py + redeploy.sh run on kai-home-server
                        for the self-hosted deployment and media mirror
example/                shallow clones of public design-system repos
                        (gitignored except README.md). References, never
                        a source of values
site/                   generated site output (gitignored)
Makefile                `make help` lists targets; `make dev` is the way in
```

## Find it fast

| You want to | Start at |
|---|---|
| Apply a captured style to another project | `python3 tools/catalog.py find <words>`, then `systems/<slug>/README.md` and `tokens.json` (steps below) |
| Let a person pick a style visually | `make dev`, the gallery tab it opens |
| Add or refresh a product | [docs/CAPTURE.md](docs/CAPTURE.md), copy `tools/kit/` into `systems/<slug>/tools/` |
| Change a package's values or README | the package, then `make design-md` (Brief + DESIGN.md regenerate), `make check` |
| Replace a product's app icon | `systems/<slug>/icon.png` (128 px PNG; `python3 tools/fetch_icon.py <slug>` refetches from the product's site) |
| Work on the gallery or site | `docs/gallery/` + `tools/catalog.py build`, then `make serve` |
| Grade packages / read the rubric | `scorecard/criteria.json` via `python3 tools/grade.py --criteria <slug>`; audits in `scorecard/audits/` |
| Find or refresh a refero style | [refero/README.md](refero/README.md); `tools/refero/fetch.py`, `classify.py`, `check.py` |
| Check a screenshot for banned content | `python3 tools/redact_images.py check systems/<slug> --patterns ~/.design-systems/cleanup-redact.json` |
| Scan a package for private text or check token contrast | `python3 tools/catalog.py scan systems/<slug> --redact <file>` / `contrast systems/<slug>/tokens.json --theme <t> FG:BG...` |
| Deploy or redeploy the site | pushes to `main` run `.github/workflows/pages.yml`; the home-server deployment is `scripts/redeploy.sh` / `deploy_trigger.py` |

## The docs

| Document | Read it when |
|---|---|
| [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) | You are building a design system for an app, or grading what a package covers |
| [docs/PACKAGE.md](docs/PACKAGE.md) | You need to know which file in a package holds what |
| [docs/EVIDENCE.md](docs/EVIDENCE.md) | You are about to copy a value and need to know how far to trust it |
| [docs/CAPTURE.md](docs/CAPTURE.md) | You are adding or refreshing a product; start from [tools/kit/](tools/kit) |
| [docs/RIGHTS.md](docs/RIGHTS.md) | Anything might leave this repo |
| [docs/TODO.md](docs/TODO.md) | You are picking up open work; the list is newest first |
| [refero/README.md](refero/README.md) | You are working with the refero snapshot: its layout, provenance, refresh and media mirror |
| [example/README.md](example/README.md) | You want a public reference: the DESIGN.md spec, unverified DESIGN.md files for brands not captured here, capture ideas, or how a large token set is organised. Never a source of values |

## Using a style from another project

1. Find the package in [catalog.json](catalog.json) by `slug`, `category`,
   `platform` (`web`, `mobile` or `desktop`), `goodFor` or `tags` (platform, density, mood and layout words such as
   `ios`, `dense`, `chat`, `sidebar`). `python3 tools/catalog.py find dark
   dense` ranks them for you. Every package lives at `systems/<slug>/`.
2. Read its `README.md` in full before anything else, starting with its
   `## Brief`: the principles, colour roles, scales, component pointers,
   contrast and focus values, generated from the package's own data. The
   rest lists what was captured and what is known to be wrong. Every package
   has one, whatever its shape.
3. Take values from its `tokens` file. Use the semantic sets (`light`,
   `dark`) for colour roles and `core` for scales. Never read a colour off a
   screenshot; most are 256-colour PNGs, and none is a measurement. `python3 tools/catalog.py export
   <slug>` prints every token with aliases resolved, as CSS custom properties
   (light on `:root`, other themes under `[data-theme]`) or `--format json`.
   A tool that only reads DESIGN.md can be pointed at the package's
   generated `DESIGN.md`, which holds one theme.
4. Look at `screenshots/` and `components/crops/` (or `components/` and
   `boards/` in an audit) for layout and proportion, not for values.
   `style-guide.html` renders every token. For a person choosing between
   styles, `make dev` serves the site and opens a gallery of all of them.
5. Say which package and which tokens you used in your summary, so the
   choice can be checked.

The `design-systems` plugin in quiver-hub wraps this: its `apply-style`
skill follows the steps above, and `author-system` builds an app's own
system against [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md). Both find this
repository through `DESIGN_SYSTEMS_HOME`.

Borrow structure and proportions. Do not copy a product's logo, icons,
illustrations or brand colours into something that ships
([docs/RIGHTS.md](docs/RIGHTS.md)).

## Working in this repository

- **Packages are copied evidence. Do not edit their contents casually.**
  The nine reference packages are byte-identical to self-learn at commit
  `84a260ac`, and linear and polaris to their original work-project sources apart from the
  2026-10-10 move of their builders into `tools/` (and `GUIDE.md`,
  `index.html` renamed to `README.md`, `style-guide.html`), Linear's app
  evidence, anonymised on 2026-10-11, and the 2026-10-17 move into the
  standard layout (`tokens.json` at the top, readings in `raw/`, component
  material in `components.md`). A fix to a
  package goes through its builders (everything under the package's
  `tools/`), and the builders' output must be committed with the input that
  changed it.
- **A rebuild that changes nothing is the check.** From a reference package,
  run its builders and confirm `git status --short .` is empty. Do this
  after touching anything under `tools/` or `raw/`. Two known exceptions,
  present since the packages were copied: Linear's builders rewrite
  `raw/validation.json`, `boards/04-components.svg` and
  `components/issue-composer.svg`, and Polaris's `build_vectors.py` measures
  text with whatever Pillow and font versions are installed, so its SVG
  widths drift. Compare against a rebuild from before your change, not
  against the committed files.
- **Every image, archive and font is a Git LFS object** (see
  [.gitattributes](.gitattributes)). Run `git lfs install` once per
  machine. Never commit a binary type that is not covered; add the pattern
  to `.gitattributes` first.
- **New packages follow the layout** in
  [docs/PACKAGE.md](docs/PACKAGE.md#layout), with the README in its outline,
  and label every value ([docs/EVIDENCE.md](docs/EVIDENCE.md)). Add each one
  to [catalog.json](catalog.json), with `platform`, `tags`, a `preview`
  block and a `capture` block (the extraction's provenance:
  [docs/CAPTURE.md](docs/CAPTURE.md)), in the same commit
  ([docs/PACKAGE.md](docs/PACKAGE.md) has the steps).
- **Each package has an app icon** at `systems/<slug>/icon.png`: a 128 px PNG
  in Git LFS, named by the catalog entry's `preview.icon`, shown on the
  gallery cards and the README catalog table. `python3 tools/fetch_icon.py
  <slug>` fetches or refreshes it from the product's site (`--host`, `--url`,
  `--all`); a supplied file only needs the resize.
- **The Brief is generated.** Every package README's `## Brief` section is
  written by `make brief` ([tools/brief.py](tools/brief.py)) from the
  package's catalog entry, tokens file and README. Read it first when you use
  a style. Never edit it by hand: change its sources, then run `make brief`
  (`make design-md` runs it too); `make check` fails on a stale one.
- **Health is generated.** Every package README's `## Health` section and the
  catalog table in [README.md](README.md) are written by `make grade`
  ([tools/health.py](tools/health.py)) from the newest scorecard snapshot and
  the package's folder. Never edit them by hand; `make check` fails on a stale
  one. Read a package's Health section before recapturing it: it is the list
  of what the last review found open.
- **`DESIGN.md` is generated.** Every package has one, written by
  `make design-md` from its tokens file and `README.md` in Google's DESIGN.md
  format for tools that read it. Never hand-edit it and never take a value
  from it that the tokens file holds: it carries one theme and no provenance.
  After changing a package's tokens or README, run `make design-md` and commit
  the result with the change; `make check` fails on a stale one.
  [docs/PACKAGE.md](docs/PACKAGE.md#designmd) has the mapping and the lint
  rules it is allowed to fail.
- **The docs site is generated.** [tools/site.py](tools/site.py) builds
  [docs/](docs) into `site/` (gitignored): every markdown page rendered with the
  gallery's own chrome. [docs/gallery/](docs/gallery) holds the gallery app;
  [tools/catalog.py](tools/catalog.py) writes its `data.json`,
  `thumbs/`, `refero/` and `export/` from [catalog.json](catalog.json) and the
  refero store. [tools/scorecard.py](tools/scorecard.py)
  writes `docs/scorecard/` from [scorecard/](scorecard). All
  of those are gitignored; never hand-edit them, and never list a package in
  the gallery any other way. A new audit is a new
  `scorecard/audits/<YYYY-MM-DD>.json`; `make scorecard` validates it.
  After changing a package, run `make grade`: it re-grades the criteria a
  script can check (F15 contrast, F16 provenance, K2 Do and don't, K3
  DESIGN.md) and refreshes the package details from `catalog.json` into a new
  snapshot, carrying every reviewed grade over unchanged. `make check` fails
  while those are stale, and warns when a package was captured after its
  reviewed grades were set: re-review that package against
  `scorecard/criteria.json` and merge the result with
  `python3 tools/grade.py --write --review <slug>=<grades.json>`, adding `--method "<text>"` to say how the review was done (it replaces the carried-over account, so cover every review still in the scorecard). Criteria marked `optional` in `scorecard/criteria.json` (C5,
  V1, V2) are graded only where the product publishes them (Polaris's
  component guidance, say), with that source as evidence; otherwise leave
  them out of a review and they become not applicable, never missing. Never
  infer them from screenshots.
- **Refero is a separate store, refreshed by its own pipeline.** `refero/`
  mirrors styles.refero.design: `refero.db` is canonical, the `<slug>/`
  folders and `catalog.json` are materialised from it, and
  `tools/refero/check.py` (part of `make check`) fails when the three
  disagree. Fetch, label and verify with `tools/refero/fetch.py`,
  `classify.py` and `check.py`; screenshots and videos are mirrored
  host-side by `tools/refero/mirror_media.py` into
  `~/services/design-systems/media/refero/` (outside git; the videos are
  gigabytes). [refero/README.md](refero/README.md) has the detail. Prefer
  `systems/` values wherever both hold one.
- **Grade a package against its platform's wording.** Each catalog entry has a
  `platform` (`web`, `mobile` or `desktop`). In `scorecard/criteria.json` a
  criterion's `doneWhen` is the web wording, and `platforms` holds the mobile
  or desktop wording where it differs; a platform not listed uses `doneWhen`.
  `python3 tools/grade.py --criteria <slug>` prints the wording a reviewer of
  that package grades against. Each snapshot records the platform a package's
  reviewed grades were set against, and `make check` warns when that wording
  differs from the wording for its platform now, until a `--review` sets them
  again. Change a wording only with a rubric version bump, and re-review every
  package whose platform it touches: a wording edit on its own does not raise
  that warning.
- **The published site never includes the gallery.** The Pages workflow builds
  with `tools/site.py --publish`, which leaves the gallery, its nav links and
  its home-page card out (a guard step still removes `site/gallery/`), and
  encrypts every page with StatiCrypt before it deploys, and fails if readable
  text or a search index entry remains. `make check` runs first in the same
  job, so a commit that skipped `make brief`/`make grade` fails the deploy.
  Search and instant navigation stay off for that reason. Never publish
  `systems/`, screenshots or the gallery, and never commit `.env` (it holds
  the site password).
- **Only credentials and personally identifiable data are masked.** The
  owner agreed on 2026-10-23 that these may show in screenshots and crops,
  because the repository stays private:
  - the owner's own account profile (name, email, handle, avatar,
    initials), their chat, document and project text, and their time zone;
  - other people's names, usernames and profile pictures as the app shows
    them (leaderboards, friends, coworkers, comments, share sheets);
  - anything the product itself publishes: marketing pages, staff and
    instructor names, testimonials, promo photos, stock and sample images.

  Masked or left out, and nothing else:
  - credentials: passwords, one-time and recovery codes, API keys, tokens
    and session cookies, signed URLs;
  - personally identifiable data: phone numbers, street addresses, precise
    locations, dates of birth, government, payment-card and bank numbers,
    and the email or other contact details of anyone but the owner.

  An account profile (name, email, handle, avatar) is not personally
  identifiable data under this rule, and neither are figures such as body
  weight or a usage total. Raw page copies, redaction lists and
  proprietary fonts stay outside the repo too; `systems/*/fonts/` is
  gitignored for this reason.

  Images count: `python3 tools/redact_images.py check systems/<slug> --patterns
  ~/.design-systems/cleanup-redact.json` must report no match before a commit
  that touches a signed-in package's screenshots or crops
  ([docs/CAPTURE.md](docs/CAPTURE.md)). That pattern file lists only what is
  still banned, so it holds no names or titles, and its `email_allow` list
  names the owner's addresses, which the check's email detector would
  otherwise flag.
  `check` also loads the package's own `tools/redact-rules/<slug>.json` when
  one exists (its `email_allow` and `wrap_ignore`) and prints which file it
  used; `--rules` picks another. `apply` does not guess: it edits images in
  place, so it still needs `--rules`.
- **Do not make this repository public**, and do not push it anywhere but
  its private GitHub remote.
- Run Python as `python3`.

## Checks before a commit

```bash
make check
```

It confirms every folder under `systems/` has a catalog entry, every entry's
files exist, every package has `README.md`, `style-guide.html` and `tools/`,
every `preview` path (cover, `icon.png`) and token path resolves, every package's `DESIGN.md` matches a
fresh generation, every README's Brief matches a fresh write, the scorecard's scripted grades are current, every
README's Health section matches the scorecard, and the three refero stores
(`refero/refero.db`, the `refero/<slug>/` folders, `refero/catalog.json`)
agree (`tools/refero/check.py`; skips the db side on a clone without
`git lfs pull`).

```bash
make test
```

It runs the top-level `tools/` tests, then every package's own
`systems/<slug>/tools/test_*.py` through
[tools/package_tests.py](tools/package_tests.py), each package in its own
interpreter from its `tools/` folder. A package test that needs Pillow is
reported as skipped when the interpreter lacks it; run
`make test PYTHON=<a python3 with Pillow>` to cover those too.

```bash
git lfs status
```

```bash
git ls-files -s | awk '$1=="100644"' | cut -f2 | grep -Ei '\.(png|jpe?g|gif|webp|zip|gz|woff2?|ttf|otf|fig|mp4|mov)$' | xargs -I{} sh -c 'git check-attr filter -- "{}" | grep -q "filter: lfs" || echo "not in LFS: {}"'
```
