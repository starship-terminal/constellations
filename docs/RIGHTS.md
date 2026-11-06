# Rights and privacy

This repository is private, and stays private. Two reasons.

## Most of it is not ours

Every package describes another company's product. The colours, type scales,
layouts, icons and screenshots are theirs; the packages are study notes for
building our own interfaces, not licences to ship theirs.

| Package | What is someone else's |
|---|---|
| duolingo, brilliant, notebooklm, coursera, gauth, researchrabbit, manus, chatgpt, claude | The whole visual system, every screenshot and crop, every icon (each README says so for its icons). The fonts the products use are proprietary; none is committed |
| linear | The same. Its GUIDE calls it an independent visual study, not an official Linear library. Berkeley Mono and Tiempos Headline are commercial and not included |
| polaris | Polaris code, tokens and icons are under the licences in `systems/polaris/licenses/` (Shopify's, plus React's). Inter is under the OFL (`INTER-OFL.txt`), which is why its font files are committed |

So: borrow structure, proportions and ideas. Do not lift a product's brand
colours, logo, icons or illustrations into something that ships.

## Some of it is private

- Linear's signed-in screenshots showed a real workspace's content. They were
  removed from the tree on 2026-10-11; only anonymised accessibility
  snapshots of the app remain. The original complete audit stays outside
  the repo (the catalog's `source.excluded` lists `linear-complete-audit.zip`)
  and should remain private.
- The signed-in captures (manus, chatgpt, claude, coursera, notebooklm,
  researchrabbit, duolingo, brilliant) come from the owner's own accounts.
  Names and emails were redacted where each README says so, but chat
  titles, course choices and library contents still show. Since
  2026-10-23 the owner's own name, email and chat text may show; what is
  still masked is listed in [AGENTS.md](../AGENTS.md).

## Rules

- Never make this repository public, and never push it to a host other
  than a private GitHub repository.
- Keep proprietary fonts in `systems/<slug>/fonts/`, which is gitignored.
- Raw page copies and redaction lists stay outside the repository
  ([CAPTURE.md](CAPTURE.md)).
- A package that leaves this repo (shared with a client, attached to an
  issue) goes without its `screenshots/`, `components/crops/` and `raw/`.
