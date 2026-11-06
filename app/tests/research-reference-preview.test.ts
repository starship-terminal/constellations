import { expect, test, vi } from "vitest";
import { inspectorPreview, fetchReferenceImage } from "@/components/reference";
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

test("remote image downloads fetch a CORS blob without credentials or navigation", async () => {
  const fetchImage = vi.fn(
    async () => new Response(new Blob(["image-bytes"], { type: "image/png" })),
  );
  const blob = await fetchReferenceImage(
    "https://cdn.example.test/screenshot.png",
    fetchImage,
  );
  expect(await blob.text()).toBe("image-bytes");
  expect(fetchImage).toHaveBeenCalledWith(
    "https://cdn.example.test/screenshot.png",
    { mode: "cors", credentials: "omit" },
  );
});
test("download failures reject rather than falling back to a navigable CDN link", async () => {
  await expect(
    fetchReferenceImage(
      "https://cdn.example.test/blocked.png",
      vi.fn(async () => {
        throw new TypeError("CORS denied");
      }),
    ),
  ).rejects.toThrow("CORS denied");
  await expect(
    fetchReferenceImage(
      "/media/missing.png",
      vi.fn(async () => new Response("Missing", { status: 404 })),
    ),
  ).rejects.toThrow("could not be downloaded");
  await expect(
    fetchReferenceImage(
      "https://cdn.example.test/error.png",
      vi.fn(
        async () =>
          new Response("Error page", {
            headers: { "content-type": "text/html" },
          }),
      ),
    ),
  ).rejects.toThrow("did not return an image");
});
