# Private Studio deployment

Studio has no login. Keep the listener on loopback and publish it only through the existing Tailscale Serve boundary. Do not enable Funnel or put this service behind a public proxy. The legacy app, evidence checkout and media mirror remain available for rollback.

## Exact private origin

Local development accepts only `localhost`, `127.0.0.1` and `[::1]`. A server operator can set `DESIGN_RESEARCH_PRIVATE_ORIGIN` to one exact HTTPS Tailscale hostname and port, without a trailing slash, such as `https://research.tail123.ts.net:8108`. This permits that HTTP Host in addition to loopback. Other hosts, ports and lookalikes remain blocked; forwarded headers never grant access. Mutation requests through that hostname must carry an `Origin` header matching the configured HTTPS origin. One without `Origin` is refused unless it carries `Sec-Fetch-Site: same-origin`, which only a browser on that origin sends. Loopback requests without `Origin`, such as `curl` on the server itself, are still accepted. `POST /api/mcp` is the one exception on the private hostname: MCP clients send neither `Origin` nor `Sec-Fetch-Site`, so a request with neither is accepted there, while a foreign `Origin`, `Sec-Fetch-Site: cross-site` or a body that is not `application/json` is refused on every host. An invalid setting leaves the app loopback-only.

This rule is deliberately stricter than the one `server/routes.py` and `web/proxy.ts` share (`server/front-door-cases.json`), which also accepts any IP literal, any `*.ts.net` host, a configured host list and an empty Host. Studio has no login, so it accepts only loopback and the one configured origin; `app/tests/front-door-subset.test.ts` runs the shared cases and fails if Studio ever accepts a host the other front doors refuse.

The hostname check provides DNS rebinding protection. Tailscale provides network access control. A permitted hostname alone does not authenticate clients, so the listener must remain `127.0.0.1` and the Serve configuration must remain tailnet-only.

## Persistent state and backups

The canonical checkout and Refero mirror are read in place through `DESIGN_SYSTEMS_REPO` and `DESIGN_SYSTEMS_MEDIA`. Do not copy generated gallery data as a replacement for evidence. Compare file counts, hashes and Git LFS hydration before cutover. Keep both copies if media differs; never use a destructive sync.

Set `DESIGN_RESEARCH_DATA_DIR` to a persistent directory outside release folders. Take a consistent SQLite backup with SQLite's backup API, or stop writers before copying the database directory with its WAL. Check `PRAGMA integrity_check`, `PRAGMA user_version` and table counts at both ends. If the destination already has personal state, preserve it and reconcile IDs before activation. The deploy script never transfers, replaces or downgrades databases.

Legacy browser bookmarks live in the old origin's `ds-saved` localStorage. A shared origin retains that browser storage across cutover, so Settings' JSON importer detects and prefills it for one-click import; keep unmatched paths and the original export. Browser data from other ports and hosts needs a separate export of the array. Browser-stored provider credentials are not migrated.

## Linux user service

The existing Nix-managed Node 22.13+ and Corepack/pnpm 10 must be on PATH. No global package installation occurs. Create `~/services/design-research/runtime.env` with mode 0600 before installing:

```sh
DESIGN_SYSTEMS_REPO=/home/USER/dev/constellations
DESIGN_SYSTEMS_MEDIA=/home/USER/services/design-systems/media/refero
DESIGN_RESEARCH_DATA_DIR=/home/USER/services/design-research/data
DESIGN_RESEARCH_PRIVATE_ORIGIN=https://HOST.TAILNET.ts.net:8108
```

`DESIGN_SYSTEMS_MEDIA_BASE` is optional: when the catalog names a media file that is absent from the local mirror, the app prepends this base URL to the path instead of falling back to the upstream host. Point it at the host root of the R2 bucket or of a server whose `/refero-media/` alias holds the mirror, without a trailing `/refero-media`: the catalog paths already start with it.

Add provider keys here only if available from an authorized server-side source. Never log the file or commit it. Stored settings override initial provider/model defaults.

```sh
scripts/studio-deploy.sh install
scripts/studio-deploy.sh stage COMMIT
scripts/studio-deploy.sh activate COMMIT
```

The script deploys into `~/services/design-research` unless
`DESIGN_RESEARCH_SERVICE_HOME` points it elsewhere.

The installer writes a user systemd service on `127.0.0.1:8845` and a disabled update timer. Each release comes from `git archive`, installs the frozen lockfile and builds separately from the running app. Activation atomically switches `current`, restarts the service and checks its settings endpoint. Failure restores the previous release when one exists. No release or state is deleted. Existing unit configuration is backed up before installation.

Stage and activate first, then validate library records, media, document variants, bookmarks, notes, research history and host/origin rejection through the loopback service. The build does not prove media or model connectivity. Check the real browser and make a live provider request only when a credential is configured.

## Private cutover and updates

Save `tailscale serve status --json`, existing proxy/service configuration and the old release before cutover. Keep the legacy service running. Once staged acceptance passes, pause the legacy design-systems deployd entry (its setup script would otherwise restore the old Serve target). On the existing home server, the supported per-service pause flag is `~/services/deployd/state/design-systems.disabled`. Preserve any existing flag and record this change for rollback. Then change only the established HTTPS port's target:

```sh
tailscale serve --bg --https=8108 http://127.0.0.1:8845
```

Verify HTTPS in a tailnet browser, including a same-origin mutation, and confirm Funnel is disabled. Restart Studio once more and check persistent state. Then enable automatic updates:

```sh
systemctl --user enable --now design-research-update.timer
```

Every five minutes, the timer fetches private `origin/main`, refuses tracked edits or a non-main checkout, fast-forwards the canonical checkout and builds/activates a changed release. Untracked legacy evidence stays intact. Keep legacy deployment automation paused after cutover. The Studio timer owns subsequent releases; the old app and nginx remain available for rollback.

## Rollback

For a failed first cutover, restore the old tailnet target, such as `tailscale serve --bg --https=8108 http://127.0.0.1:8108`, and disable the Studio update timer. Remove the legacy deployd pause flag only if this cutover created it. The legacy nginx and app can continue serving without opening the Studio database.

For a subsequent Studio release, disable its timer and activate the prior commit using the same script. Check schema compatibility first. Automatic release rollback only restores binaries; it never restores a database snapshot. Do not run older binaries against an incompatible migrated schema. Restore a consistent database backup only after stopping Studio and saving the current database separately.
