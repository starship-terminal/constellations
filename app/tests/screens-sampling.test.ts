import { describe, expect, it } from "vitest";
import type { ScreenItem } from "../src/contracts/screens";
import { queryScreens, samplePerProduct } from "../src/server/sources/screens";
import { GET } from "../src/app/api/library/screens/route";
import { libraryItem } from "./helpers";

function screen(slug: string, index: number): ScreenItem {
  const reference = libraryItem(slug, {
    name: slug,
    captured: "2026-11-01",
  });
  const mediaId = `systems/${slug}/screenshots/${index}.png`;
  return {
    id: `${reference.id}:${mediaId}`,
    reference,
    media: {
      id: mediaId,
      path: mediaId,
      name: `home-${index}`,
      kind: "screenshot",
      tags: ["dark"],
      type: "image",
      group: "screenshots/dark",
      url: `/media/${mediaId}`,
    },
  };
}
const names = (items: ScreenItem[]) =>
  items.map(({ reference, media }) => `${reference.slug}:${media.name}`);

describe("per-product sampling", () => {
  const items = [
    ...[0, 1, 2, 3].map((i) => screen("alpha", i)),
    ...[0, 1].map((i) => screen("beta", i)),
    screen("gamma", 0),
  ];

  it("caps each product and interleaves products in first-seen order", () => {
    expect(names(samplePerProduct(items, 2))).toEqual([
      "alpha:home-0",
      "beta:home-0",
      "gamma:home-0",
      "alpha:home-1",
      "beta:home-1",
    ]);
    expect(samplePerProduct(items, 0)).toEqual([]);
    expect(samplePerProduct([], 3)).toEqual([]);
  });

  it("applies before pagination and keeps total as the match count", () => {
    const first = queryScreens(items, { perProduct: 1, limit: 2 });
    expect(names(first.items)).toEqual(["alpha:home-0", "beta:home-0"]);
    expect(first.total).toBe(7);
    // Only the three sampled captures can be paged.
    expect(first.pageable).toBe(3);
    const rest = queryScreens(items, { perProduct: 1, limit: 2, offset: 2 });
    expect(names(rest.items)).toEqual(["gamma:home-0"]);
    expect(queryScreens(items, { limit: 2 }).pageable).toBe(7);
  });

  it("leaves results alone without perProduct", () => {
    expect(queryScreens(items, { limit: 3 }).items).toHaveLength(3);
    expect(
      new Set(
        queryScreens(items, { limit: 3 }).items.map((i) => i.reference.id),
      ).size,
    ).toBe(1);
  });

  it("rejects a malformed perProduct on the route", async () => {
    for (const value of ["0", "-1", "abc", "1.5", ""])
      expect(
        (
          await GET(
            new Request(
              `http://studio.test/api/library/screens?perProduct=${value}`,
            ),
          )
        ).status,
      ).toBe(400);
  });
});
