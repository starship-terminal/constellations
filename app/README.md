# Design research app

A new personal application built beside the existing `web/` app. The original data, capture pipeline and old app remain intact. This app has no accounts, subscriptions or team management.

## Run locally

Requires Node 22.13+ and pnpm 10. Export variants use Node's built-in SQLite reader. From the repository root:

```sh
pnpm --dir app install --frozen-lockfile
pnpm --dir app dev
```

Open http://127.0.0.1:8845. The original app still uses port 8800. The new app accepts loopback hostnames only (`localhost`, `127.0.0.1`, and `[::1]`); every route rejects other HTTP hosts.

For AI responses, copy [`.env.example`](.env.example) to `.env.local` and set an OpenAI or Anthropic API key. Restart the server after changing environment variables. Select the provider and model in Settings. Credentials stay on the server; the settings endpoint only returns whether credentials are configured. Without a key, the real library, style details, collections and exports remain usable; the app reports that AI research needs configuration.

Official OpenAI connections use the Responses API; Anthropic uses its native API. A custom OpenAI base URL uses Chat Completions for compatibility. That mode reports text-only evidence because tool-output images are not supported by that protocol. Official OpenAI and Anthropic can receive bounded, hydrated local reference images; remote media remains text-only unless mirrored locally. No arbitrary remote image fetching happens on the server.

`DESIGN_RESEARCH_PROVIDER`, `DESIGN_RESEARCH_MODEL` and `DESIGN_RESEARCH_BASE_URL` provide initial settings. Provider-specific `OPENAI_MODEL`, `OPENAI_BASE_URL`, `ANTHROPIC_MODEL` and `ANTHROPIC_BASE_URL` are also supported. Stored settings override these defaults; provider keys always come from the environment.

## Boundaries

- `src/app/`: routes and thin API handlers.
- `src/features/`: research, browsing, styles, collections and settings.
- `src/components/`: shared accessible interface and media components.
- `src/design/`: application tokens and motion styles.
- `src/contracts/`: shared data shapes and validated research input.
- `src/server/sources/`: read-only adapters over the existing source stores.
- `src/server/db/`: personal-state database and schema.
- `src/server/research/`: model providers, retrieval and research orchestration.
- `tests/`: source, persistence and research contract tests.

The app does not import legacy UI components. The source catalog and Refero snapshot remain canonical; generated data can be rebuilt with `make build`. Source adapters support `DESIGN_SYSTEMS_REPO` for an explicit checkout. Media may come from the existing mirror or source URLs recorded in the catalog. LFS pointer files are not treated as real images.

Refero document exports accept `variant=compact` or `variant=extended`. Selectable variants require a hydrated `refero/refero.db` (Git LFS) and the existing `tools/refero/generators.js` in that checkout. The app opens the source database read-only and reuses the captured serializers in-process. Extended Markdown preserves the captured `DESIGN.md` verbatim because it resolves text references missing from the raw extraction. Other variants return unavailable when their captured source is missing. Requests without a variant keep returning the existing materialized files unchanged.

Personal state is separate from captured evidence. `DESIGN_RESEARCH_DATA_DIR` selects its directory, otherwise it uses `~/.local/share/design-research/app.db`. Do not commit the personal SQLite database or model credentials. Stop the app before copying the database directory for a backup.

## Design and evidence

The UI follows the approved local Refero mockup and the measured [Refero package](../systems/refero-design/README.md), using that package's [tokens](../systems/refero-design/tokens.json) for the neutral palette, shape, layout and motion. The new app uses its own mark and Lucide controls, with accessible semantics and reduced-motion behavior. Proprietary captured fonts and raw copied page markup are not bundled.

Measured package records and interpreted Refero styles retain separate source identities. The library does not represent the complete live Refero screenshot catalog. A screenshot folder is not presented as an ordered interaction flow without supporting metadata. Research must link recommendations to actual inspected references and acknowledge gaps in its evidence.

## Categorisation

Refero's recorded vocabulary is seeded into the app's SQLite database by migration v4. Web and iOS category headers read `/api/taxonomy` and preserve the original platform-specific labels and order, including categories with no local captures. App-owned assignments retag measured systems without rewriting captured token evidence. See [category migration](docs/category-migration.md) for mapping rationale. JSON files are versioned seed inputs; SQLite owns runtime vocabulary and assignments. Reopening the app preserves manual assignment changes.

## Checks

```sh
pnpm --dir app typecheck
pnpm --dir app test
pnpm --dir app build
```

The repository's existing `make check` and `make test` still validate the source stores and builders. The Research app CI workflow validates this application independently without publishing the private library.
