import { describe, expect, it, vi } from "vitest";
import {
  loadLibraryPages,
  mergeLibraryItems,
  type LibraryResponse,
} from "../src/features/library-data";
import type { LibraryItem } from "../src/contracts/library";
function deferred<T>() {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((done) => {
    resolve = done;
  });
  return { promise, resolve };
}
const item = (slug: string): LibraryItem => ({
  id: `systems:${slug}`,
  slug,
  source: "systems",
  name: slug,
  description: "",
  platform: "web",
  themes: [],
  tags: [],
  category: "design",
  image: null,
  icon: null,
  video: null,
  evidence: "measured",
  captured: null,
});
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
