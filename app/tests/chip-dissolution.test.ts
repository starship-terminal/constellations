import { afterEach, expect, test, vi } from "vitest";
import {
  cancelChipDissolutions,
  dissolveChip,
} from "@/features/chip-dissolution";

// The suite runs in Node: give the module only the browser surface each early
// return touches, so any further DOM work fails loudly instead of passing.
afterEach(() => vi.unstubAllGlobals());
const chip = (width: number, height: number) =>
  ({
    getBoundingClientRect: () => ({ width, height, left: 0, top: 0 }),
  }) as unknown as HTMLButtonElement;

test("reduced motion skips the effect without measuring or touching the DOM", () => {
  vi.stubGlobal("window", {
    matchMedia: (query: string) => ({
      matches: query === "(prefers-reduced-motion: reduce)",
    }),
  });
  const measure = vi.fn();
  const cleanUp = dissolveChip({
    getBoundingClientRect: measure,
  } as unknown as HTMLButtonElement);
  expect(measure).not.toHaveBeenCalled();
  expect(() => cleanUp()).not.toThrow();
});

test("a chip with no size gets no copy", () => {
  vi.stubGlobal("window", { matchMedia: () => ({ matches: false }) });
  for (const [width, height] of [
    [0, 20],
    [40, 0],
  ]) {
    const cleanUp = dissolveChip(chip(width, height));
    expect(() => cleanUp()).not.toThrow();
  }
  expect(() => cancelChipDissolutions()).not.toThrow();
});
