import { expect, test } from "vitest";
import type { ScreenItem } from "@/contracts/screens";
import { sampleBrowseScreens } from "@/features/home-browse-data";

const screen = (reference: string, index: number) =>
  ({
    id: `${reference}-${index}`,
    reference: { id: `systems:${reference}` },
    media: { id: `${reference}-${index}` },
  }) as unknown as ScreenItem;
const ids = (items: ScreenItem[]) => items.map((item) => item.id);

test("rotates across products before repeating one, in first-seen order", () => {
  const items = [
    screen("a", 0),
    screen("a", 1),
    screen("a", 2),
    screen("b", 0),
    screen("c", 0),
    screen("c", 1),
  ];
  expect(ids(sampleBrowseScreens(items, 5))).toEqual([
    "a-0",
    "b-0",
    "c-0",
    "a-1",
    "c-1",
  ]);
});

test("stops at the limit mid-round and when every product is used up", () => {
  const items = [screen("a", 0), screen("b", 0), screen("a", 1)];
  expect(ids(sampleBrowseScreens(items, 1))).toEqual(["a-0"]);
  expect(ids(sampleBrowseScreens(items))).toEqual(["a-0", "b-0", "a-1"]);
  expect(sampleBrowseScreens([], 8)).toEqual([]);
  expect(sampleBrowseScreens(items, 0)).toEqual([]);
});
