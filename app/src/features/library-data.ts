import type { LibraryItem } from "@/contracts/library";

export interface LibraryResponse {
  items: LibraryItem[];
  total: number;
  stats: { systems: number; refero: number };
}

export function mergeLibraryItems(
  previous: LibraryItem[],
  incoming: LibraryItem[],
): LibraryItem[] {
  return [
    ...new Map(
      [...previous, ...incoming].map((item) => [item.id, item]),
    ).values(),
  ];
}

/** Publish each completed metadata page without waiting for slower siblings. */
export async function loadLibraryPages(
  fetchPage: (offset: number) => Promise<LibraryResponse>,
  onPage: (page: LibraryResponse) => void,
  onPageError: (error: unknown) => void,
): Promise<void> {
  const first = await fetchPage(0);
  onPage(first);
  const offsets = Array.from(
    { length: Math.max(0, Math.ceil(first.total / 200) - 1) },
    (_, index) => (index + 1) * 200,
  );
  await Promise.all(
    offsets.map(async (offset) => {
      try {
        onPage(await fetchPage(offset));
      } catch (error) {
        onPageError(error);
      }
    }),
  );
}

export interface CatalogSnapshot {
  items: LibraryItem[];
  total: number;
}
interface CatalogListener {
  onUpdate: (snapshot: CatalogSnapshot) => void;
  onPageError: (error: unknown) => void;
}
interface CatalogEntry extends CatalogSnapshot {
  complete: boolean;
  at: number;
  pending?: Promise<void>;
  listeners: Set<CatalogListener>;
}
/** How long a fully loaded catalog is reused across page visits. */
export const CATALOG_TTL_MS = 5 * 60_000;
const catalogs = new Map<string, CatalogEntry>();
export function clearCatalogCache(): void {
  catalogs.clear();
}
const snapshot = (entry: CatalogEntry): CatalogSnapshot => ({
  items: entry.items,
  total: entry.total,
});
/**
 * Load every page of one store's catalog once per CATALOG_TTL_MS and share it
 * between page visits. A caller that arrives while a load is running joins
 * it instead of starting another. Items already held are shown at once; a
 * load that completes replaces them with exactly what it fetched, so removed
 * captures disappear, while a load with a failed page keeps them and is
 * fetched again next time.
 */
export async function loadCatalog(
  key: string,
  fetchPage: (offset: number) => Promise<LibraryResponse>,
  onUpdate: (snapshot: CatalogSnapshot) => void,
  onPageError: (error: unknown) => void,
  now = Date.now(),
): Promise<void> {
  let entry = catalogs.get(key);
  if (entry?.complete && now - entry.at < CATALOG_TTL_MS) {
    onUpdate(snapshot(entry));
    return;
  }
  if (!entry) {
    entry = {
      items: [],
      total: 0,
      complete: false,
      at: now,
      listeners: new Set(),
    };
    catalogs.set(key, entry);
  }
  if (entry.items.length) onUpdate(snapshot(entry));
  const listener = { onUpdate, onPageError };
  entry.listeners.add(listener);
  try {
    if (!entry.pending) {
      const loading = entry;
      loading.pending = refreshCatalog(loading, fetchPage, now).finally(() => {
        loading.pending = undefined;
      });
    }
    await entry.pending;
  } finally {
    entry.listeners.delete(listener);
  }
}
async function refreshCatalog(
  entry: CatalogEntry,
  fetchPage: (offset: number) => Promise<LibraryResponse>,
  now: number,
): Promise<void> {
  const previous = entry.items;
  let fetched: LibraryItem[] = [];
  let failed = false;
  entry.complete = false;
  const publish = () => {
    for (const listener of entry.listeners) listener.onUpdate(snapshot(entry));
  };
  await loadLibraryPages(
    fetchPage,
    (page) => {
      fetched = mergeLibraryItems(fetched, page.items);
      entry.items = mergeLibraryItems(previous, fetched);
      entry.total = page.total;
      publish();
    },
    (error) => {
      failed = true;
      for (const listener of entry.listeners) listener.onPageError(error);
    },
  );
  if (failed) return;
  // fetched is a subset of the merged list, so equal length means equal sets.
  const removed = fetched.length !== entry.items.length;
  entry.items = fetched;
  entry.complete = true;
  entry.at = now;
  if (removed) publish();
}
