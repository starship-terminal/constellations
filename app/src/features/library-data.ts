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
interface CatalogEntry extends CatalogSnapshot {
  complete: boolean;
  at: number;
}
/** How long a fully loaded catalog is reused across page visits. */
export const CATALOG_TTL_MS = 5 * 60_000;
const catalogs = new Map<string, CatalogEntry>();
export function clearCatalogCache(): void {
  catalogs.clear();
}
/**
 * Load every page of one store's catalog once per CATALOG_TTL_MS and share it
 * between page visits. An incomplete load (a page failed) is fetched again
 * next time, keeping the items it already has.
 */
export async function loadCatalog(
  key: string,
  fetchPage: (offset: number) => Promise<LibraryResponse>,
  onUpdate: (snapshot: CatalogSnapshot) => void,
  onPageError: (error: unknown) => void,
  now = Date.now(),
): Promise<void> {
  const cached = catalogs.get(key);
  if (cached?.complete && now - cached.at < CATALOG_TTL_MS) {
    onUpdate({ items: cached.items, total: cached.total });
    return;
  }
  const entry: CatalogEntry = {
    items: cached?.items || [],
    total: cached?.total ?? 0,
    complete: false,
    at: now,
  };
  catalogs.set(key, entry);
  let failed = false;
  await loadLibraryPages(
    fetchPage,
    (page) => {
      entry.items = mergeLibraryItems(entry.items, page.items);
      entry.total = page.total;
      onUpdate({ items: entry.items, total: entry.total });
    },
    (error) => {
      failed = true;
      onPageError(error);
    },
  );
  entry.complete = !failed;
}
