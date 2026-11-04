import { afterEach, expect, test } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createResearchStore, type ResearchStore } from "@/server/db";
const stores: ResearchStore[] = [],
  directories: string[] = [];
async function open() {
  const dir = await mkdtemp(join(tmpdir(), "research-db-"));
  directories.push(dir);
  const store = await createResearchStore(dir);
  stores.push(store);
  return { dir, store };
}
afterEach(async () => {
  for (const store of stores.splice(0)) store.close();
  for (const dir of directories.splice(0))
    await rm(dir, { recursive: true, force: true });
});
test("messages, selection, notes and settings survive reopening the database", async () => {
  const { dir, store } = await open();
  const conversation = await store.createConversation("A durable brief");
  await store.saveMessages(conversation.id, [
    {
      id: "user-1",
      role: "user",
      parts: [{ type: "text", text: "Compare layouts" }],
    },
    {
      id: "assistant-1",
      role: "assistant",
      parts: [
        {
          type: "tool-searchLibrary",
          toolCallId: "tool-1",
          state: "output-available",
          input: { query: "layouts" },
          output: { kind: "candidates", items: [] },
        },
      ],
    },
  ]);
  await store.updateConversation(conversation.id, {
    pinnedIds: ["systems:linear"],
    excludedIds: ["refero:example"],
    archived: true,
  });
  const collection = await store.createCollection("Layouts");
  await store.updateCollection(collection.id, { notes: "A useful pattern" });
  await store.putItem(collection.id, "systems:linear", "Keep the density");
  await store.putItem(collection.id, "systems:linear", "Changed my note");
  await store.saveSettings({ provider: "openai", model: "test-model" });
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const reopened = await createResearchStore(dir);
  stores.push(reopened);
  const saved = await reopened.getConversation(conversation.id);
  expect(saved).toMatchObject({
    title: "A durable brief",
    archived: true,
    pinnedIds: ["systems:linear"],
    excludedIds: ["refero:example"],
  });
  expect(saved?.messages[1].parts[0]).toMatchObject({
    type: "tool-searchLibrary",
    output: { kind: "candidates" },
  });
  const board = await reopened.getCollection(collection.id);
  expect(board?.collection.notes).toBe("A useful pattern");
  expect(board?.items).toHaveLength(1);
  expect(board?.items[0].note).toBe("Changed my note");
  expect(await reopened.getSettings()).toEqual({
    provider: "openai",
    model: "test-model",
  });
});
test("collection items enforce foreign keys and delete cascade", async () => {
  const { store } = await open();
  await expect(
    store.putItem("missing", "systems:linear", "note"),
  ).rejects.toThrow();
  const collection = await store.createCollection("Delete test");
  await store.putItem(collection.id, "systems:linear");
  await store.client.execute({
    sql: "DELETE FROM collections WHERE id=?",
    args: [collection.id],
  });
  expect(
    (await store.client.execute("SELECT * FROM collection_items")).rows,
  ).toHaveLength(0);
});

test("saving a bookmark again preserves its note unless a note is explicitly supplied", async () => {
  const { store } = await open();
  const collection = await store.createCollection("Bookmark notes");
  await store.putItem(collection.id, "systems:linear", "Keep this detail");
  await store.putItem(collection.id, "systems:linear");
  expect((await store.getCollection(collection.id))?.items[0].note).toBe(
    "Keep this detail",
  );
  await store.putItem(collection.id, "systems:linear", "");
  expect((await store.getCollection(collection.id))?.items[0].note).toBe("");
});

test("a conversation and its initial prompt survive reopening as one durable creation", async () => {
  const { dir, store } = await open();
  const row = await store.createConversation(
    "A saved first prompt",
    "Find thoughtful onboarding references",
  );
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const reopened = await createResearchStore(dir);
  stores.push(reopened);
  const saved = await reopened.getConversation(row.id);
  expect(saved?.messages).toHaveLength(1);
  expect(saved?.messages[0]).toMatchObject({
    role: "user",
    parts: [{ type: "text", text: "Find thoughtful onboarding references" }],
  });
  expect(saved?.messages[0].id).toMatch(/^[0-9a-f-]{36}$/);
});
