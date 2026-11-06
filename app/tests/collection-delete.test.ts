import { expect, test } from "vitest";
import { getStore } from "@/server/db";
import { DELETE } from "@/app/api/collections/[id]/route";
import { jsonRequest } from "./helpers";

const context = (id: string) => ({ params: Promise.resolve({ id }) });
const remove = (id: string, headers: Record<string, string> = {}) =>
  DELETE(
    jsonRequest(`/api/collections/${id}`, "DELETE", undefined, headers),
    context(id),
  );

test("deleting a collection removes it with its references and saved media", async () => {
  const store = await getStore();
  const board = await store.createCollection("Doomed board");
  await store.putItem(board.id, "systems:example");
  await store.putCollectionMedia(
    board.id,
    "systems:example",
    "systems/example/screenshots/a.png",
  );
  const response = await remove(board.id);
  expect(response.status).toBe(200);
  expect(await response.json()).toEqual({ deleted: board.id });
  expect(await store.getCollection(board.id)).toBeNull();
  expect(
    await store.mediaCollectionIds(
      "systems:example",
      "systems/example/screenshots/a.png",
    ),
  ).toEqual([]);
  expect((await remove(board.id)).status).toBe(404);
});

test("deleting a collection refuses a cross-origin request", async () => {
  const store = await getStore();
  const board = await store.createCollection("Kept board");
  const response = await remove(board.id, { origin: "https://evil.test" });
  expect(response.status).toBe(403);
  expect(await store.getCollection(board.id)).not.toBeNull();
});
