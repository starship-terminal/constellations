import { describe, expect, it } from "vitest";
import { tokenNameParts } from "@/components/reference";

describe("tokenNameParts", () => {
  it("breaks after dots and dashes, never inside a word", () => {
    expect(tokenNameParts("text.primary")).toEqual(["text.", "primary"]);
    expect(tokenNameParts("color-bg_surface/raised")).toEqual([
      "color-",
      "bg_",
      "surface/",
      "raised",
    ]);
    expect(tokenNameParts("plain")).toEqual(["plain"]);
  });
});
