# Design research app

A new personal application built beside the existing `web/` app. The original data, capture pipeline and old app remain intact. This app has no accounts, subscriptions or team management.

## Run locally

Requires Node 22.13+ and pnpm 10. Export variants use Node's built-in SQLite reader. From the repository root:

```sh
pnpm --dir app install --frozen-lockfile
pnpm --dir app dev
```

Open http://127.0.0.1:8845. The original app still uses port 8800. The new app accepts loopback hostnames (`localhost`, `127.0.0.1`, and `[::1]`). An optional exact Tailscale origin supports a private server deployment while the listener stays on loopback. See [private deployment](docs/DEPLOYMENT.md) for staging, backups, cutover and rollback.

For AI responses, paste an OpenAI or Anthropic API key in Settings > AI; it saves on the server and is never returned to the UI. Environment variables still work as a fallback: copy [`.env.example`](.env.example) to `.env.local`, set a key there and restart the server. Select the provider and model in Settings. Without a key, the real library, style details, collections and exports remain usable; the app reports that AI research needs configuration.

Official OpenAI connections use the Responses API; Anthropic uses its native API. A custom OpenAI base URL uses Chat Completions for compatibility. That mode reports text-only evidence because tool-output images are not supported by that protocol. Official OpenAI and Anthropic can receive bounded, hydrated local reference images; remote media remains text-only unless mirrored locally. No arbitrary remote image fetching happens on the server.

`DESIGN_RESEARCH_PROVIDER`, `DESIGN_RESEARCH_MODEL` and `DESIGN_RESEARCH_BASE_URL` provide initial settings. Provider-specific `OPENAI_MODEL`, `OPENAI_BASE_URL`, `ANTHROPIC_MODEL` and `ANTHROPIC_BASE_URL` are also supported. Stored settings override these defaults. A key saved in Settings wins over the environment key for that provider.

## Boundaries

- `src/app/`: routes and thin API handlers.
- `src/features/`: research, browsing, styles, collections and settings.
- `src/features/knowledge/`: the docs and scorecard reading UI.
- `src/components/`: shared accessible interface and media components.
- `src/design/`: application tokens and motion styles.
- `src/contracts/`: shared data shapes and validated research input.
- `src/data/`: seed JSON the server loads (media and style taxonomies, system categories).
- `src/server/sources/`: read-only adapters over the existing source stores.
- `src/server/knowledge/`: the library docs and scorecard readers.
- `src/server/collections/`: saved media collections.
- `src/server/taxonomy/`: the library taxonomy.
- `src/server/research/`: model providers, retrieval and research orchestration.
- `src/server/db/`: personal-state database and schema.
- `src/proxy.ts` + `src/server/request-host.ts`: the loopback/Tailscale host allowlist.
- `tests/`: source, persistence and research contract tests.

The app does not import legacy UI components. The source catalog and Refero snapshot remain canonical; generated data can be rebuilt with `make build`. Source adapters support `DESIGN_SYSTEMS_REPO` for an explicit checkout. Media may come from the existing mirror or source URLs recorded in the catalog. LFS pointer files are not treated as real images.

Refero document exports accept `variant=compact` or `variant=extended`. Selectable variants require a hydrated `refero/refero.db` (Git LFS) and the existing `tools/refero/generators.js` in that checkout. The app opens the source database read-only and reuses the captured serializers in-process. Extended Markdown preserves the captured `DESIGN.md` verbatim because it resolves text references missing from the raw extraction. Other variants return unavailable when their captured source is missing. Requests without a variant keep returning the existing materialized files unchanged.

Personal state is separate from captured evidence. `DESIGN_RESEARCH_DATA_DIR` selects its directory, otherwise it uses `~/.local/share/design-research/app.db`. Do not commit the personal SQLite database or model credentials. Stop the app before copying the database directory for a backup.

## Design and evidence

The UI follows the approved local Refero mockup and the measured [Refero package](../systems/refero-design/README.md), using that package's [tokens](../systems/refero-design/tokens.json) for the neutral palette, shape, layout and motion. The new app uses its own mark and Lucide controls, with accessible semantics and reduced-motion behavior. Proprietary captured fonts and raw copied page markup are not bundled.

Measured package records and interpreted Refero styles retain separate source identities. The library does not represent the complete live Refero screenshot catalog. A screenshot folder is not presented as an ordered interaction flow without supporting metadata. Research must link recommendations to actual inspected references and acknowledge gaps in its evidence.

## MCP endpoint

`POST /api/mcp` serves the research tools to coding agents over MCP (streamable HTTP, JSON replies, no session); Settings > Agents shows the commands that add it. It differs from the two other MCP servers in this repository, `web/app/api/mcp/` and `server/mcp.py`, on purpose:

- It announces itself as `constellations` and serves the research chat's tools, so a client configured for the `design-systems` servers needs its own entry.
- A batch holds at most 8 calls, because one image tool reply can be several megabytes of base64; the other two have no cap.
- A body without `Content-Length` is accepted and counted as it streams, refused past the 256 KB cap; `web/` refuses such a request with 411.

Empty bodies (400, -32600) and bodies that are not UTF-8 or not JSON (400, -32700) are refused as `server/routes.py` refuses them. Before reading the body, the endpoint checks the Host header like every route and runs the same guard as the app's other writes: a foreign `Origin` or `Sec-Fetch-Site: cross-site` is refused (403), and the body must be sent as `Content-Type: application/json` (415 otherwise), so a page on another site cannot start tool calls with a no-preflight form or `text/plain` POST. MCP clients send no `Origin` or `Sec-Fetch-Site`, so they pass, through the private origin too ([private deployment](docs/DEPLOYMENT.md)).

## Categorisation

Refero's recorded vocabulary is seeded into the app's SQLite database by migration v4. Web and iOS category headers read `/api/taxonomy` and preserve the original platform-specific labels and order, including categories with no local captures. App-owned assignments retag measured systems without rewriting captured token evidence. See [category migration](docs/category-migration.md) for mapping rationale. JSON files are versioned seed inputs; SQLite owns runtime vocabulary and assignments. Reopening the app preserves manual assignment changes. Seed rows added later (a new package in `system-categories.json` or `media-taxonomy.json`) reach an existing database on its next open: a seed ledger records which packages and media each database has been offered, so no per-package migration is needed and a label the user cleared is never restored.

When a package leaves the library, the regenerated seed files drop it, and the next open removes what the seed gave it, in the same transaction as the rest of the open: its curated category and media labels, and the ledger keys that held only those labels, so the package is seeded afresh if it comes back. Only keys in the ledger of a reference neither seed file names are touched. A category the user set by hand stays, and so does a cleared label's ledger key, so either choice survives the package's return. Collections, notes, saved media and conversations that name the package are never changed; they show the entry as no longer available. Reopening removes nothing more.

## Docs

- [Private deployment](docs/DEPLOYMENT.md): staging, backups, cutover and rollback.
- [Legacy feature migration](docs/MIGRATION.md): how the `web/` features map into this app, with the [gallery](docs/gallery-migration.md), [styles](docs/styles-migration.md) and [workflow](docs/workflow-migration.md) detail.
- [Category migration](docs/category-migration.md): the taxonomy mapping.
- [Catalog filter interactions](docs/filter-interactions.md): how Refero's search picker and result modes behave.
- Audit logs, 2026-11-04: [catalog and screenshots](docs/catalog-live-audit.md), [Refero interactions](docs/refero-interaction-audit.md) and [styles](docs/styles-live-audit.md).

## Checks

```sh
pnpm --dir app typecheck
pnpm --dir app test
pnpm --dir app build
```

The repository's existing `make check` and `make test` still validate the source stores and builders. The Research app CI workflow validates this application independently without publishing the private library.
