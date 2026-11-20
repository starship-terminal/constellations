import { expect, test } from "vitest";
import { browseParams, browseSections } from "@/features/home-browse-data";

test("no search shows up twice for the same kind of capture", () => {
  const seen = new Set<string>();
  for (const section of browseSections)
    for (const choice of section.choices) {
      const key = `${section.kind}:${choice}`;
      expect(seen.has(key), key).toBe(false);
      seen.add(key);
    }
});

test("the server samples the eight cards; the page shows them as sent", () => {
  const params = browseParams(browseSections[0], "Settings", "mobile");
  expect(Object.fromEntries(params)).toEqual({
    q: "Settings",
    kind: "screenshot",
    scope: "media",
    limit: "8",
    perProduct: "2",
    platform: "mobile",
  });
  expect(browseParams(browseSections[2], "Menu").has("platform")).toBe(false);
});
