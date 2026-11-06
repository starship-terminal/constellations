import { describe, expect, it, vi } from "vitest";
import {
  CATALOG_TTL_MS,
  clearCatalogCache,
  loadCatalog,
  loadLibraryPages,
  mergeLibraryItems,
  type LibraryResponse,
} from "../src/features/library-data";
import { libraryItem } from "./helpers";
function deferred<T>() {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((done) => {
    resolve = done;
  });
  return { promise, resolve };
}
const item = (slug: string) => libraryItem(slug, { category: "design" });
const page = (slug: string, total = 600): LibraryResponse => ({
  items: [item(slug)],
  total,
  stats: { systems: total, refero: 0 },
});

describe("progressive library metadata", () => {
  it("publishes first and successful later pages before a slow page finishes, despite another page failing", async () => {
    const slow = deferred<LibraryResponse>(),
      firstPublished = deferred<void>();
    const published: LibraryResponse[] = [],
      onError = vi.fn();
    const fetchPage = vi.fn(async (offset: number) => {
      if (offset === 0) return page("first", 800);
      if (offset === 200) return slow.promise;
      if (offset === 400) throw new Error("Unavailable page");
      return page("later", 800);
    });
    let finished = false;
    const loading = loadLibraryPages(
      fetchPage,
      (value) => {
        published.push(value);
        if (published.length === 1) firstPublished.resolve();
      },
      onError,
    ).then(() => {
      finished = true;
    });
    await firstPublished.promise;
    expect(published[0].items[0].slug).toBe("first");
    expect(finished).toBe(false);
    await vi.waitFor(() => {
      expect(onError).toHaveBeenCalledOnce();
      expect(published.map((value) => value.items[0].slug)).toContain("later");
    });
    expect(finished).toBe(false);
    slow.resolve(page("slow", 800));
    await loading;
    expect(published.map((value) => value.items[0].slug)).toEqual([
      "first",
      "later",
      "slow",
    ]);
    expect(fetchPage.mock.calls.map(([offset]) => offset)).toEqual([
      0, 200, 400, 600,
    ]);
  });
  it("preserves already loaded cards and avoids duplicates during a retry", () => {
    const existing = [item("first"), item("later")];
    const refreshed = { ...item("first"), name: "Updated" };
    const merged = mergeLibraryItems(existing, [refreshed]);
    expect(merged).toHaveLength(2);
    expect(merged[0].name).toBe("Updated");
    expect(merged[1]).toEqual(existing[1]);
    expect(
      mergeLibraryItems(merged, [item("recovered")]).map((value) => value.slug),
    ).toEqual(["first", "later", "recovered"]);
  });
  it("exposes initial page failure so the first load remains retriable", async () => {
    const onPage = vi.fn(),
      onError = vi.fn();
    await expect(
      loadLibraryPages(
        async () => {
          throw new Error("Offline");
        },
        onPage,
        onError,
      ),
    ).rejects.toThrow("Offline");
    expect(onPage).not.toHaveBeenCalled();
  });
});

describe("shared catalog cache", () => {
  const page = (slugs: string[], total: number): LibraryResponse => ({
    items: slugs.map(item),
    total,
    stats: { systems: total, refero: 0 },
  });
  it("reuses a complete catalog across visits until it expires", async () => {
    clearCatalogCache();
    const fetchPage = vi.fn(async () => page(["a", "b"], 2));
    const seen: string[][] = [];
    const onUpdate = (snapshot: { items: LibraryItem[] }) =>
      seen.push(snapshot.items.map((value) => value.slug));
    await loadCatalog("systems", fetchPage, onUpdate, () => {}, 1000);
    await loadCatalog("systems", fetchPage, onUpdate, () => {}, 2000);
    expect(fetchPage).toHaveBeenCalledTimes(1);
    expect(seen).toEqual([
      ["a", "b"],
      ["a", "b"],
    ]);
    await loadCatalog(
      "systems",
      fetchPage,
      onUpdate,
      () => {},
      1000 + CATALOG_TTL_MS,
    );
    expect(fetchPage).toHaveBeenCalledTimes(2);
  });
  it("fetches an incomplete catalog again, keeping the items it had", async () => {
    clearCatalogCache();
    const failing = vi.fn(async (offset: number) => {
      if (offset) throw new Error("page failed");
      return page(["a"], 201);
    });
    const errors: unknown[] = [];
    await loadCatalog(
      "systems",
      failing,
      () => {},
      (e) => errors.push(e),
      0,
    );
    expect(errors).toHaveLength(1);
    const retry = vi.fn(async (offset: number) =>
      page(offset ? ["z"] : ["a"], 201),
    );
    let last: string[] = [];
    await loadCatalog(
      "systems",
      retry,
      (snapshot) => (last = snapshot.items.map((value) => value.slug)),
      () => {},
      1,
    );
    expect(retry).toHaveBeenCalledTimes(2);
    expect(last).toEqual(["a", "z"]);
  });
  it("drops removed items once a refresh completes", async () => {
    clearCatalogCache();
    await loadCatalog(
      "systems",
      async () => page(["a", "gone"], 2),
      () => {},
      () => {},
      0,
    );
    let last: string[] = [];
    await loadCatalog(
      "systems",
      async () => page(["a"], 1),
      (snapshot) => (last = snapshot.items.map((value) => value.slug)),
      () => {},
      CATALOG_TTL_MS,
    );
    expect(last).toEqual(["a"]);
  });
  it("lets a returning visit join the load already running", async () => {
    clearCatalogCache();
    const first = deferred<LibraryResponse>();
    const fetchPage = vi.fn(() => first.promise);
    const seen: number[] = [];
    const one = loadCatalog(
      "refero",
      fetchPage,
      () => {},
      () => {},
      0,
    );
    const two = loadCatalog(
      "refero",
      fetchPage,
      (snapshot) => seen.push(snapshot.items.length),
      () => {},
      0,
    );
    first.resolve(page(["a"], 1));
    await Promise.all([one, two]);
    expect(fetchPage).toHaveBeenCalledTimes(1);
    expect(seen.at(-1)).toBe(1);
  });
  it("shows retained items before retrying, even if the retry fails", async () => {
    clearCatalogCache();
    await loadCatalog(
      "systems",
      async (offset) => {
        if (offset) throw new Error("page failed");
        return page(["a"], 201);
      },
      () => {},
      () => {},
      0,
    );
    let shown: string[] = [];
    await expect(
      loadCatalog(
        "systems",
        async () => {
          throw new Error("offline");
        },
        (snapshot) => (shown = snapshot.items.map((value) => value.slug)),
        () => {},
        1,
      ),
    ).rejects.toThrow("offline");
    expect(shown).toEqual(["a"]);
  });
});
