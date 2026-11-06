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
