import { beforeEach, expect, test, vi } from "vitest";
const mocks = vi.hoisted(() => ({
  save: vi.fn(),
  get: vi.fn(),
  remove: vi.fn(),
}));
vi.mock("@/server/db", () => ({
  getStore: async () => ({
    saveMedia: mocks.save,
    removeSavedMedia: mocks.remove,
  }),
}));
vi.mock("@/server/sources", () => ({ getReference: mocks.get }));
import { POST as importMedia } from "@/app/api/saved-media/import/route";
import { POST as saveMedia } from "@/app/api/saved-media/route";
function request(path: string, body: unknown) {
  return new Request(`http://localhost:8845${path}`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      origin: "http://localhost:8845",
    },
    body: JSON.stringify(body),
  });
}
beforeEach(() => {
  vi.clearAllMocks();
  mocks.get.mockResolvedValue({
    media: [{ id: "systems/example/screenshots/a.png" }],
  });
});
test("saved media rejects invented IDs instead of storing arbitrary URLs", async () => {
  const response = await saveMedia(
    request("/api/saved-media", {
      referenceId: "systems:example",
      mediaId: "https://unknown.invalid/private.png",
    }),
  );
  expect(response.status).toBe(404);
  expect(mocks.save).not.toHaveBeenCalled();
});
test("legacy import deduplicates and matches only recorded media", async () => {
  const response = await importMedia(
    request("/api/saved-media/import", {
      paths: [
        "/media/systems/example/screenshots/a.png",
        "/media/systems/example/screenshots/a.png",
        "/media/systems/example/raw/private.png",
        "https://unknown.invalid/image.png",
      ],
    }),
  );
  expect(await response.json()).toMatchObject({
    imported: 1,
    skipped: [
      "/media/systems/example/raw/private.png",
      "https://unknown.invalid/image.png",
    ],
  });
  expect(mocks.save).toHaveBeenCalledExactlyOnceWith(
    "systems:example",
    "systems/example/screenshots/a.png",
  );
});

test("legacy Refero image bookmarks match canonical media across local and mirror URLs", async () => {
  mocks.get.mockResolvedValue({
    media: [
      { id: "shot", path: "/refero-media/shots/linear.jpg" },
      { id: "detail_poster", path: "/refero-media/detail-posters/linear.jpg" },
    ],
  });
  const response = await importMedia(
    request("/api/saved-media/import", {
      paths: [
        "/media/refero-media/shots/linear.jpg",
        "https://media.example.com/refero-media/detail-posters/linear.jpg",
        "/media/refero-media/posters/linear.jpg",
      ],
    }),
  );
  expect(await response.json()).toEqual({
    imported: 2,
    skipped: ["/media/refero-media/posters/linear.jpg"],
  });
  expect(mocks.save).toHaveBeenCalledWith("refero:linear", "shot");
  expect(mocks.save).toHaveBeenCalledWith("refero:linear", "detail_poster");
});
