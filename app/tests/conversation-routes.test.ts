import { afterEach, beforeEach, expect, test, vi } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createResearchStore, type ResearchStore } from "@/server/db";
import { GET, PATCH } from "@/app/api/conversations/[id]/route";
import { GET as taxonomy } from "@/app/api/taxonomy/route";

const state = vi.hoisted(() => ({ store: null as ResearchStore | null }));
vi.mock("@/server/db", async (original) => ({
  ...(await original<typeof import("@/server/db")>()),
  getStore: async () => state.store!,
}));
vi.mock("@/server/sources", () => ({
  getReference: async (id: string) =>
    ["systems:one", "systems:two"].includes(id) ? { id } : null,
}));
let directory = "";
beforeEach(async () => {
  directory = await mkdtemp(join(tmpdir(), "conversation-routes-"));
  state.store = await createResearchStore(directory);
});
afterEach(async () => {
  state.store?.close();
  await rm(directory, { recursive: true, force: true });
});

const context = (id: string) => ({ params: Promise.resolve({ id }) });
const read = (id: string) =>
  GET(
    new Request(`http://localhost:8845/api/conversations/${id}`),
    context(id),
  );
function patch(
  id: string,
  body: unknown,
  origin = "http://localhost:8845",
): Promise<Response> {
  return PATCH(
    new Request(`http://localhost:8845/api/conversations/${id}`, {
      method: "PATCH",
      headers: { "content-type": "application/json", origin },
      body: JSON.stringify(body),
    }),
    context(id),
  );
}

test("GET returns a stored conversation, 404 for an unknown one and 400 for a malformed ID", async () => {
  const row = await state.store!.createConversation("Dashboards");
  const found = await read(row.id);
  expect(found.status).toBe(200);
  expect(await found.json()).toMatchObject({
    id: row.id,
    title: "Dashboards",
    messages: [],
    pinnedIds: [],
    excludedIds: [],
  });
  expect((await read("not-a-conversation")).status).toBe(404);
  expect((await read("../secret")).status).toBe(400);
});

test("PATCH renames and archives, and rejects unknown fields and missing rows", async () => {
  const row = await state.store!.createConversation("Draft");
  const renamed = await patch(row.id, {
    title: "  Calm layouts ",
    archived: true,
  });
  expect(renamed.status).toBe(200);
  expect(await renamed.json()).toMatchObject({
    id: row.id,
    title: "Calm layouts",
    archived: true,
  });
  expect((await patch(row.id, { messages: [] })).status).toBe(400);
  expect((await patch(row.id, { title: "" })).status).toBe(400);
  expect((await patch("not-a-conversation", { title: "x" })).status).toBe(404);
  expect((await state.store!.getConversation(row.id))?.title).toBe(
    "Calm layouts",
  );
});

test("PATCH keeps the other reference list and validates the combined lists", async () => {
  const row = await state.store!.createConversation();
  expect((await patch(row.id, { excludedIds: ["systems:two"] })).status).toBe(
    200,
  );
  const pinned = await patch(row.id, { pinnedIds: ["systems:one"] });
  expect(await pinned.json()).toMatchObject({
    pinnedIds: ["systems:one"],
    excludedIds: ["systems:two"],
  });
  // Pinning what is already excluded is a conflict with the stored list.
  const conflict = await patch(row.id, { pinnedIds: ["systems:two"] });
  expect(conflict.status).toBe(400);
  expect((await conflict.json()).error).toContain("both pinned and excluded");
  const unknown = await patch(row.id, { pinnedIds: ["systems:missing"] });
  expect(unknown.status).toBe(400);
  expect((await unknown.json()).error).toContain("systems:missing");
  expect(await state.store!.getConversation(row.id)).toMatchObject({
    pinnedIds: ["systems:one"],
    excludedIds: ["systems:two"],
  });
});

test("PATCH from another origin changes nothing", async () => {
  const row = await state.store!.createConversation("Original");
  const response = await patch(
    row.id,
    { title: "Hijacked" },
    "http://evil.test",
  );
  expect(response.status).toBe(403);
  expect((await state.store!.getConversation(row.id))?.title).toBe("Original");
});

test("GET /api/taxonomy lists every snapshot's groups in snapshot order", async () => {
  const response = await taxonomy();
  expect(response.status).toBe(200);
  const body = await response.json();
  expect(body.version).toBe(1);
  expect(body.snapshots.length).toBeGreaterThan(0);
  expect(body.groups).toEqual(
    body.snapshots.flatMap(
      (snapshot: { groups: unknown[] }) => snapshot.groups,
    ),
  );
  expect(body.groups.map((group: { id: string }) => group.id)).toContain(
    "web-categories",
  );
});
