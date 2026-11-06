import { afterEach, describe, expect, it, vi } from "vitest";
import { replaceSearch, searchHref } from "@/features/url-state";

describe("URL filter updates", () => {
  afterEach(() => vi.unstubAllGlobals());
  it("builds the href with the query only when there is one", () => {
    expect(searchHref("/library", new URLSearchParams("q=dark"), "#top")).toBe(
      "/library?q=dark#top",
    );
    expect(searchHref("/library", new URLSearchParams(), "#top")).toBe(
      "/library#top",
    );
  });
  it("keeps the current hash when a filter changes", () => {
    const replaceState = vi.fn();
    vi.stubGlobal("window", {
      location: { pathname: "/library/linear", hash: "#files" },
      history: { replaceState },
    });
    replaceSearch(new URLSearchParams("tab=files&file=README.md"));
    expect(replaceState).toHaveBeenCalledWith(
      null,
      "",
      "/library/linear?tab=files&file=README.md#files",
    );
    replaceSearch(new URLSearchParams("theme=dark"), "/styles");
    expect(replaceState).toHaveBeenLastCalledWith(
      null,
      "",
      "/styles?theme=dark#files",
    );
  });
});
