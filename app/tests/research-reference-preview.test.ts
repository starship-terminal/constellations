import { expect, test } from "vitest";
import { inspectorPreview } from "@/components/reference";
import type { LibraryDetail, LibraryItem } from "@/contracts/library";
const current = {
  id: "systems:brilliant",
  source: "systems",
  slug: "brilliant",
  image:
    "/media/data/thumbs/systems__brilliant__screenshots__home-light-default.jpg",
} as LibraryItem;
const detail = {
  ...current,
  media: [
    {
      type: "image",
      url: "/media/systems/brilliant/screenshots/app-2026-10/courses-dark-default.png",
    },
    {
      type: "image",
      url: "/media/systems/brilliant/screenshots/home-light-default.png",
    },
  ],
} as LibraryDetail;
test("inspector upgrades generated thumbnails to the exact original screen", () => {
  expect(inspectorPreview(current, detail)).toBe(
    "/media/systems/brilliant/screenshots/home-light-default.png",
  );
  const nested = {
    ...current,
    image:
      "/media/data/thumbs/systems__brilliant__screenshots__app-2026-10__courses-dark-default.jpg",
  };
  expect(inspectorPreview(nested, detail)).toBe(detail.media[0].url);
});
test("inspector preserves the clicked thumbnail when no exact original is available", () => {
  expect(
    inspectorPreview(current, { ...detail, media: [detail.media[0]] }),
  ).toBe(current.image);
  expect(inspectorPreview(current, { ...detail, id: "systems:other" })).toBe(
    current.image,
  );
  expect(inspectorPreview(current, null)).toBe(current.image);
  expect(
    inspectorPreview(
      { ...current, image: "/refero-media/shots/example.jpg" },
      detail,
    ),
  ).toBe("/refero-media/shots/example.jpg");
});
