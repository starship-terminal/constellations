# web/: the gallery app

The Next.js app that browses the library: gallery, refero, scorecard, docs,
the librarian chat and Settings. `make dev` runs it on 127.0.0.1:8800;
`make web-build` builds it for production. The repo's
[AGENTS.md](../AGENTS.md) has the map; this file covers what the app keeps
for itself.

## The model provider key

Settings > Model provider sets the model the chat talks to. The key never
lives in the browser:

1. The page sends the key once, to `POST /api/provider`.
2. The server tests it with one model-list call. A key that fails is not
   saved, and the previous key, if any, keeps working. That is also how a
   key is replaced: save a new one and it swaps in only once it passes. An
   endpoint with no model list cannot check a key, so such a key is saved
   only when no other key is saved, and the page says it was not checked.
3. The server writes the provider to a one-row SQLite database,
   `$DESIGN_SYSTEMS_CONFIG_DIR/provider.db`, default
   `~/.config/design-systems/provider.db`: outside the checkout, folder mode
   0700, file mode 0600. The variable must be an absolute path outside the
   checkout; both servers expand a leading `~/` themselves and refuse a
   relative path or a folder inside the checkout, which the chat then
   reports, so they can never end up holding two different keys. "Inside
   the checkout" compares real paths too, so a symlink into it counts, and
   it ignores letter case where the disk does (tested on the disk, not
   assumed from the platform); it applies only when the server's root
   really is a checkout (it holds `catalog.json` or `.git`), so a process
   started from `/` is not refused everything. A refused or unreadable
   folder also turns off `ANTHROPIC_API_KEY`: the variable says where a
   saved key is meant to live, so running on the env key would spend a key
   the operator may not mean to and hide the mistake. The chat shows the
   error until the variable is fixed. The existing part of the folder's
   path is resolved to its real path, so the file is opened by that path,
   and a `provider.db`, side file or lock that is itself a symbolic link is
   refused (to anywhere: a linked database has no use here, and it could
   carry the key into the checkout). Neither runtime's SQLite binding can
   ask SQLite not to follow links, so each open is checked before (no link,
   and a new file is created with `O_EXCL` and `O_NOFOLLOW`) and after: the
   path SQLite reports in `PRAGMA database_list`, which it resolves when it
   opens the file, must be the expected one. Every change is one statement,
   so SQLite's own locking makes it atomic across both servers, and a
   crashed process never leaves a lock behind. A model change applies only
   while the saved key and endpoint are the ones the page was editing. The
   database uses SQLite's rollback journal with `secure_delete` on, not
   WAL, so a replaced or removed key is overwritten in place and no copy
   lingers in a `-wal` file (an exception to the stack conventions' WAL
   default: one row, rare writes). Remove deletes a file SQLite reports as
   damaged, and saving a key the provider accepted replaces one; a busy or
   unreadable file is reported and never deleted.

   Deleting a damaged file and writing its replacement is the one step that
   is not a single statement, so it runs under a recovery lock both servers
   take: `BEGIN EXCLUSIVE` on `provider.lock`, an empty SQLite file next to
   the database that never holds a table. SQLite was chosen over a lock file
   made with `O_EXCL`: its lock is a POSIX lock, which both runtimes already
   speak, which excludes other processes and other connections in the same
   process alike, and which the operating system drops when its holder
   dies, so a crash never blocks the store and there is no stale-lock rule
   (age, owner pid) to get wrong. A lock file left behind is simply taken.
   Inside the lock a recovery deletes only the file the damage was seen on:
   the path must still have that file's device and inode, and SQLite must
   still call it damaged (`PRAGMA quick_check`); otherwise another request
   has recovered it already and a newer save is left alone. Side files are
   deleted before the database, since no new database can appear at the
   path while the damaged one is still there. A recovery waits up to ten
   seconds for one already running, then reports that the file is being
   repaired. The gallery's recovery never awaits while it holds the lock, so
   no other request in its process runs in between.
4. No answer carries the key. `GET /api/provider` and `GET /api/status` say
   only where it comes from, shown on the page as a badge: saved on the
   server, from the server environment, or no key.
5. The chat uses the saved key; `ANTHROPIC_API_KEY` (from the environment
   or the repo's `.env`) only while nothing is saved; with neither, the
   chat asks for setup. A saved file that is broken or unreadable (a
   permission change, say) is reported, never quietly replaced by the env
   key.
6. A saved key only goes to the endpoint it was saved with. Changing the
   API, base URL, key header or models URL needs the key again; the model
   and label change without it. Remove (`DELETE /api/provider`) deletes the
   file, and the env key, if set, applies again.
7. Error texts are scrubbed of the key before they are returned, and the
   routes log only an error's type.

An older version stored the whole provider, key included, in the browser's
`localStorage` under `ds-provider`. On the first page load after the update
the app sends that key to the save route as a migration, which the server
accepts only into a store that has never held a provider (one saved and
later removed counts), so an old browser never replaces a newer key and
never brings back one the user removed. The page deletes the browser copy once the server has
decided: it saved the key, kept its own, refused the body or failed the
key's test. When the server does not answer, answers 5xx or answers with a
page that is not JSON (a proxy's 502 while the API restarts), the browser
copy stays and a later visit tries again. Either way the page says what
happened (a toast, then a note on Settings).
Tabs take turns, and the other open tabs pick up the change.

The logic lives in [lib/provider-api.ts](lib/provider-api.ts) and
[lib/provider-store.ts](lib/provider-store.ts), tested by
`lib/provider-api.test.ts` and `components/storage.test.ts` (`pnpm test`).
The Python `/api/` server for the docs site applies the same rules to the
same file ([server/provider_store.py](../server/provider_store.py),
tested by `tools/test_routes.py`).

The app has no login, so anyone who can reach it can replace or remove the
saved key and spend it through the chat, as with the env key before. Nobody
can read it back.

## The docs site's Settings page

The published docs site ([tools/site.py](../tools/site.py)) has the same
Model provider section. Where a server answers its `/api/` (the home
server's `server/api.py` behind nginx), it uses the routes above. On a copy
with no server, such as GitHub Pages (its `/api/` answers 404), the section
says so, stores nothing, and deletes a key an older version left in that
browser without sending it anywhere. Any other failure to reach `/api/`
keeps that key, as in the gallery.

## On the home server

These steps are for the owner; nothing in this repo contacts the host.

1. Pick the folder that holds the saved provider, outside the clone. The
   gallery's unit (`next start` from the clone) and the Python API unit
   (`server/api.py`) must see the same one: either both run as the same user
   with the same `HOME` (then `~/.config/design-systems/` is shared and
   nothing needs setting), or set `DESIGN_SYSTEMS_CONFIG_DIR` to the same
   absolute path for both, in each unit's environment or the clone's `.env`
   (`~/...` is fine: the app expands it, though systemd does not).
2. If the gallery runs from the [Dockerfile](../Dockerfile) image, mount a
   volume at that folder and set `DESIGN_SYSTEMS_CONFIG_DIR` to the mount
   point; otherwise a saved key is lost when the container is recreated.
3. Make sure the folder belongs to the user the units run as. The app
   creates it 0700 and the database 0600 itself; an existing folder keeps its
   mode, so check it is not readable by others. A save takes group and other
   access off an existing database but never adds any, so a database made
   read-only (0400, or a read-only volume) keeps serving the chat, and Save
   and Remove report that it is read-only. Keep it on a local disk, not
   a network share, since both units lock the same SQLite files (the
   database and `provider.lock`) and a network share's locks are not
   reliable. Do not make `provider.db` or the files next to it symbolic
   links: the store refuses them (a linked folder is fine; it is
   resolved). Back it up,
   if at all, with `sqlite3 provider.db ".backup <copy>"`, never `cp`.
4. Restart the API unit once after this change deploys: `server/api.py`
   itself changed (it now passes `DELETE /api/provider` to the routes), and
   only the route modules reload per request. The gallery unit picks the
   change up with its usual rebuild.
5. Check that nginx's `/api/` location passes every method (no
   `limit_except`), so `DELETE /api/provider` reaches the API.
6. Open Settings > Model provider in each browser that had a key saved: the
   page moves it to the server and deletes the browser copy. Or save the key
   once from any browser, since the saved key now serves them all.
