import { describe, expect, it, vi } from "vitest";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import {
  alphaCropBounds,
  coverCrop,
  originalMobilePreview,
  MobileCatalogPreview,
  readCachedCrop,
} from "@/features/mobile-catalog-preview";

describe("mobile catalog capture rendering", () => {
  it("allows crop dimensions to exceed the global responsive image width cap", () => {
    const html = renderToStaticMarkup(
      createElement(MobileCatalogPreview, {
        image: "/original.png",
        fallback: "/thumbnail.jpg",
        name: "Example",
      }),
    );
    expect(html).toContain("max-width:none");
  });
  it("reuses measured hover frames and bounds cache memory", () => {
    const cache = new Map();
    const measure = vi.fn(() => ({
      bounds: { x: 15, y: 76, width: 782, height: 1688 },
      width: 812,
      height: 1780,
      source: "frame",
    }));
    const first = readCachedCrop(cache, "frame", measure);
    readCachedCrop(cache, "other-frame", measure);
    expect(readCachedCrop(cache, "frame", measure)).toBe(first);
    expect(measure).toHaveBeenCalledTimes(2);
    for (let i = 0; i < 30; i++) readCachedCrop(cache, `frame-${i}`, measure);
    expect(cache.size).toBeLessThanOrEqual(16);
    expect(cache.has("frame")).toBe(false);
  });
  it("removes differing transparent capture margins while retaining white app pixels", () => {
    const pixels = new Uint8ClampedArray(8 * 10 * 4);
    // Real white app content must survive. Only alpha, never RGB, defines trim.
    for (let y = 3; y < 9; y++)
      for (let x = 1; x < 7; x++)
        pixels.set([255, 255, 255, 255], (y * 8 + x) * 4);
    expect(alphaCropBounds(pixels, 8, 10)).toEqual({
      x: 1,
      y: 3,
      width: 6,
      height: 6,
    });
    const different = new Uint8ClampedArray(6 * 8 * 4);
    for (let y = 1; y < 7; y++)
      for (let x = 2; x < 6; x++)
        different.set([0, 0, 0, 255], (y * 6 + x) * 4);
    expect(alphaCropBounds(different, 6, 8)).toEqual({
      x: 2,
      y: 1,
      width: 4,
      height: 6,
    });
  });
  it("covers the inset with the alpha crop using uniform scale and no letterbox", () => {
    const crop = { x: 15, y: 76, width: 782, height: 1688 };
    const result = coverCrop(crop, 812, 1780, 342, 744);
    const scale = result.width / 812;
    expect(result.height / 1780).toBeCloseTo(scale);
    expect(crop.width * scale).toBeGreaterThanOrEqual(342);
    expect(crop.height * scale).toBeGreaterThanOrEqual(744);
    expect(result.left + crop.x * scale).toBeLessThanOrEqual(0);
    expect(result.top + crop.y * scale).toBeLessThanOrEqual(0);
    expect(result.left + (crop.x + crop.width) * scale).toBeGreaterThanOrEqual(
      342,
    );
    expect(result.top + (crop.y + crop.height) * scale).toBeGreaterThanOrEqual(
      744,
    );
  });
  it("retains opaque captures without treating white as an added mat", () => {
    const pixels = new Uint8ClampedArray(3 * 4 * 4).fill(255);
    expect(alphaCropBounds(pixels, 3, 4)).toEqual({
      x: 0,
      y: 0,
      width: 3,
      height: 4,
    });
    expect(alphaCropBounds(new Uint8ClampedArray(3 * 4 * 4), 3, 4)).toEqual({
      x: 0,
      y: 0,
      width: 3,
      height: 4,
    });
  });
  it("recovers the existing PNG original from a generated measured thumbnail URL", () => {
    expect(
      originalMobilePreview(
        "/media/data/thumbs/systems__gemini__screenshots__dark__01-onboarding-sign-in-gate.jpg",
      ),
    ).toBe(
      "/media/systems/gemini/screenshots/dark/01-onboarding-sign-in-gate.png",
    );
    expect(
      originalMobilePreview(
        "/media/systems/hevy/screenshots/light/01-home.png",
      ),
    ).toBe("/media/systems/hevy/screenshots/light/01-home.png");
    expect(originalMobilePreview("https://example.com/image.jpg")).toBe(
      "https://example.com/image.jpg",
    );
  });
});
