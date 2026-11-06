import { beforeEach, expect, test, vi } from "vitest";
const mocks = vi.hoisted(() => ({
  collection: vi.fn(),
  put: vi.fn(),
  remove: vi.fn(),
  reference: vi.fn(),
  collections: vi.fn(),
  memberships: vi.fn(),
}));
vi.mock("@/server/db", () => ({
  getStore: async () => ({
    getCollection: mocks.collection,
    putCollectionMedia: mocks.put,
    removeCollectionMedia: mocks.remove,
    listCollections: mocks.collections,
    mediaCollectionIds: mocks.memberships,
  }),
}));
vi.mock("@/server/sources", () => ({ getReference: mocks.reference }));
import { GET, POST, DELETE } from "@/app/api/collections/[id]/media/route";
import { GET as detail } from "@/app/api/collections/[id]/route";
import { GET as list } from "@/app/api/collections/route";
import { GET as exportBoard } from "@/app/api/collections/[id]/export/route";
const mediaId = "systems/example/screenshots/details.png";
const context = { params: Promise.resolve({ id: "board-a" }) };
function request(method: string, body?: unknown, query = "") {
  return new Request(
    `http://localhost:8845/api/collections/board-a/media${query}`,
    {
      method,
      headers: {
        origin: "http://localhost:8845",
        "content-type": "application/json",
      },
      ...(body === undefined ? {} : { body: JSON.stringify(body) }),
    },
  );
}
beforeEach(() => {
  vi.clearAllMocks();
  mocks.collection.mockResolvedValue({
    collection: { id: "board-a", name: "Board A", notes: "Keep this" },
    items: [],
    mediaItems: [
      {
        collectionId: "board-a",
        referenceId: "systems:example",
        mediaId,
        addedAt: 12,
      },
    ],
  });
  mocks.reference.mockResolvedValue({
    id: "systems:example",
    source: "systems",
    slug: "example",
    name: "Example",
    media: [
      {
        id: mediaId,
        kind: "screenshot",
        name: "Details",
        type: "image",
        url: `/media/${mediaId}`,
      },
    ],
    measured: { privateLargeManifest: true },
  });
  mocks.collections.mockResolvedValue([
    { id: "board-a", name: "Board A", mediaCount: 1, referenceCount: 0 },
  ]);
  mocks.memberships.mockResolvedValue(["board-a"]);
});
test("adding media validates the actual package asset and rejects invented or mismatched identities", async () => {
  expect(
    (
      await POST(
        request("POST", { referenceId: "systems:example", mediaId }),
        context,
      )
    ).status,
  ).toBe(200);
  expect(mocks.put).toHaveBeenCalledExactlyOnceWith(
    "board-a",
    "systems:example",
    mediaId,
  );
  mocks.put.mockClear();
  for (const invalid of [
    "https://unknown.invalid/screen.png",
    "systems/other/screenshots/details.png",
    "systems/example/raw/private.png",
  ])
    expect(
      (
        await POST(
          request("POST", { referenceId: "systems:example", mediaId: invalid }),
          context,
        )
      ).status,
    ).toBe(404);
  expect(mocks.put).not.toHaveBeenCalled();
  mocks.collection.mockResolvedValue(null);
  expect(
    (
      await POST(
        request("POST", { referenceId: "systems:example", mediaId }),
        context,
      )
    ).status,
  ).toBe(404);
});
test("board detail and media listing hydrate exact assets without embedding full package manifests", async () => {
  const listed = await (await GET(request("GET"), context)).json();
  expect(listed.items[0]).toMatchObject({
    id: `board-a:systems:example:${mediaId}`,
    name: "Example",
    media: { id: mediaId },
  });
  expect(listed.items[0].reference).not.toHaveProperty("measured");
  expect(listed.items[0].reference).not.toHaveProperty("media");
  const board = await (await detail(request("GET"), context)).json();
  expect(board.mediaItems).toEqual(listed.items);
  expect(board.items).toEqual([]);
  mocks.reference.mockResolvedValue(null);
  expect(
    (await (await GET(request("GET"), context)).json()).items[0],
  ).toMatchObject({ name: "systems:example", media: null, reference: null });
});
test("removing media only changes the selected board membership, using query or JSON identity", async () => {
  expect(
    (
      await DELETE(
        request(
          "DELETE",
          undefined,
          `?referenceId=systems%3Aexample&mediaId=${encodeURIComponent(mediaId)}`,
        ),
        context,
      )
    ).status,
  ).toBe(200);
  expect(mocks.remove).toHaveBeenCalledWith(
    "board-a",
    "systems:example",
    mediaId,
  );
  expect(
    (
      await DELETE(
        request("DELETE", { referenceId: "systems:example", mediaId }),
        context,
      )
    ).status,
  ).toBe(200);
  expect(mocks.remove).toHaveBeenCalledTimes(2);
});
test("collection listing includes separate reference/media counts and selected media memberships", async () => {
  const response = await list(
    new Request(
      `http://localhost:8845/api/collections?referenceId=systems%3Aexample&mediaId=${encodeURIComponent(mediaId)}`,
    ),
  );
  expect(await response.json()).toEqual({
    collections: [
      { id: "board-a", name: "Board A", mediaCount: 1, referenceCount: 0 },
    ],
    mediaCollectionIds: ["board-a"],
  });
  expect(
    (
      await list(
        new Request(
          "http://localhost:8845/api/collections?referenceId=systems%3Aexample",
        ),
      )
    ).status,
  ).toBe(400);
});
test("board export includes the exact saved capture and its local viewer URL", async () => {
  const response = await exportBoard(request("GET"), context);
  const text = await response.text();
  expect(text).toContain("## Captured screens");
  expect(text).toContain(`Media ID: ${mediaId}`);
  expect(text).toContain(
    `/library/example?tab=screenshots&media=${encodeURIComponent(mediaId)}`,
  );
});
test("board export sends measured packages to the package route", async () => {
  mocks.collection.mockResolvedValue({
    collection: { id: "board-a", name: "Board A", notes: "" },
    items: [{ referenceId: "systems:example", note: "", addedAt: 12 }],
    mediaItems: [],
  });
  const text = await (await exportBoard(request("GET"), context)).text();
  expect(text).toContain("Local reference: /library/example");
  expect(text).not.toContain("/styles/systems/");
});
test("screenshot boards reject videos the image viewer cannot display", async () => {
  mocks.reference.mockResolvedValue({
    id: "refero:example",
    source: "refero",
    slug: "example",
    name: "Example",
    media: [
      {
        id: "video",
        name: "Preview",
        type: "video",
        url: "https://example.com/preview.mp4",
      },
    ],
  });
  const response = await POST(
    request("POST", { referenceId: "refero:example", mediaId: "video" }),
    context,
  );
  expect(response.status).toBe(400);
  expect(mocks.put).not.toHaveBeenCalled();
});
