import { describe, expect, it } from "vitest";
import {
  enterSearchAction,
  screenCountScope,
  verticalChoiceIndex,
} from "@/features/catalog-search-behavior";

describe("catalog picker keyboard and count behavior", () => {
  it("reopens on Enter after dismissal instead of applying a stale highlighted or typed option", () => {
    expect(enterSearchAction(false, "", 4)).toBe("open");
    expect(enterSearchAction(false, "button", 1)).toBe("open");
    expect(enterSearchAction(true, "", -1)).toBe("open");
    expect(enterSearchAction(true, "", 4)).toBe("choose");
    expect(enterSearchAction(true, "button", -1)).toBe("choose");
  });
  it("keeps vertical navigation in the same column in the responsive two-column grid", () => {
    const positions = Array.from({ length: 6 }, (_, index) => ({
      index,
      x: 50 + (index % 2) * 100,
      y: Math.floor(index / 2) * 40,
    }));
    expect(verticalChoiceIndex(positions, 1, 1)).toBe(3);
    expect(verticalChoiceIndex(positions, 3, -1)).toBe(1);
    expect(verticalChoiceIndex(positions, 5, 1)).toBe(1);
    expect(verticalChoiceIndex(positions, 0, -1)).toBe(4);
  });
  it("follows rendered rows across uneven subgroup grids", () => {
    const positions = [
      { index: 0, x: 50, y: 0 },
      { index: 1, x: 150, y: 0 },
      { index: 2, x: 250, y: 0 },
      { index: 3, x: 50, y: 40 },
      { index: 4, x: 150, y: 40 },
      { index: 5, x: 50, y: 120 },
      { index: 6, x: 150, y: 120 },
      { index: 7, x: 250, y: 120 },
    ];
    expect(verticalChoiceIndex(positions, 0, 1)).toBe(3);
    expect(verticalChoiceIndex(positions, 3, 1)).toBe(5);
    expect(verticalChoiceIndex(positions, 4, 1)).toBe(6);
    expect(verticalChoiceIndex(positions, 7, -1)).toBe(4);
  });
  it("requests and caches crop counts separately from screenshots on the same platform", () => {
    const crop = screenCountScope("web", "crop"),
      screenshots = screenCountScope("web", "screenshot"),
      mobile = screenCountScope("mobile", "crop");
    expect(crop.key).not.toBe(screenshots.key);
    expect(crop.key).not.toBe(mobile.key);
    expect(crop.query.get("kind")).toBe("crop");
    expect(screenshots.query.get("kind")).toBe("screenshot");
    expect(crop.query.get("platform")).toBe("web");
    expect(crop.query.get("limit")).toBe("0");
  });
});
