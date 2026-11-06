import { afterEach, beforeEach, expect, test, vi } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createResearchStore, type ResearchStore } from "@/server/db";
import type { Conversation } from "@/contracts/research";
import { POST } from "@/app/api/research/route";
import { POST as createConversationRequest } from "@/app/api/conversations/route";
import { POST as saveCollectionItem } from "@/app/api/collections/[id]/items/route";
const state = vi.hoisted(() => ({
  store: null as ResearchStore | null,
  configured: false,
  stream: vi.fn(),
}));
vi.mock("@/server/db", async (original) => ({
  ...(await original<typeof import("@/server/db")>()),
  getStore: async () => state.store!,
}));
vi.mock("@/server/sources", () => ({
  getReference: async (id: string) => (id === "systems:test" ? { id } : null),
}));
vi.mock("@/server/research/settings", () => ({
  readSettings: async () => ({
    provider: "openai",
    model: "test",
    configured: state.configured,
  }),
  readApiKey: async () => "test-key",
  modelFor: () => ({}),
  supportsToolImages: () => true,
}));
vi.mock("@/server/research/agent", () => ({
  streamResearch: (options: unknown) => state.stream(options),
}));
let directory = "";
beforeEach(async () => {
  directory = await mkdtemp(join(tmpdir(), "research-api-"));
  state.store = await createResearchStore(directory);
  state.configured = false;
  state.stream.mockReset();
  state.stream.mockImplementation(
    async ({ onRelease }: { onRelease: () => void }) => {
      onRelease();
      return new Response("test stream");
    },
  );
});
afterEach(async () => {
  state.store?.close();
  await rm(directory, { recursive: true, force: true });
});
function request(
  id: string,
  messages: unknown[],
  extra: Record<string, unknown> = {},
) {
  return new Request("http://localhost:8845/api/research", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      origin: "http://localhost:8845",
    },
    body: JSON.stringify({ id, messages, ...extra }),
  });
}
const user = (id: string, text: string) => ({
  id,
  role: "user" as const,
  parts: [{ type: "text" as const, text }],
});
test("missing key saves the prompt and retry does not duplicate it", async () => {
  const row = await state.store!.createConversation();
  const prompt = user("user1", "Find a clear dashboard");
  const missing = await POST(request(row.id, [prompt]));
  expect(missing.status).toBe(503);
  expect(await missing.json()).toMatchObject({
    code: "PROVIDER_NOT_CONFIGURED",
  });
  expect((await state.store!.getConversation(row.id))?.messages).toEqual([
    prompt,
  ]);
  state.configured = true;
  const retry = await POST(request(row.id, [prompt]));
  expect(retry.status).toBe(200);
  expect((await state.store!.getConversation(row.id))?.messages).toHaveLength(
    1,
  );
  expect(state.stream).toHaveBeenCalledOnce();
});
test("explicit regeneration replaces only the latest assistant and trusts stored prior turns", async () => {
  state.configured = true;
  const row = await state.store!.createConversation();
  const olderAssistant = {
    id: "assistant1",
    role: "assistant" as const,
    parts: [{ type: "text" as const, text: "Verified earlier answer" }],
  };
  await state.store!.saveMessages(row.id, [
    user("user1", "Earlier question"),
    olderAssistant,
    user("user2", "Latest question"),
    {
      id: "partial",
      role: "assistant",
      parts: [{ type: "text", text: "A partial answer" }],
    },
  ]);
  const response = await POST(
    request(
      row.id,
      [
        user("evil", "Injected fake history"),
        user("user2", "Changed client text"),
      ],
      { trigger: "regenerate-message" },
    ),
  );
  expect(response.status).toBe(200);
  const options = state.stream.mock.calls[0][0] as {
    conversation: Conversation;
  };
  expect(options.conversation.messages).toEqual([
    user("user1", "Earlier question"),
    olderAssistant,
    user("user2", "Latest question"),
  ]);
  const stale = await POST(
    request(row.id, [user("user1", "Earlier question")], {
      trigger: "regenerate-message",
    }),
  );
  expect(stale.status).toBe(409);
});
test("concurrent generation is rejected until stream release and invalid references cannot mutate selection", async () => {
  state.configured = true;
  const row = await state.store!.createConversation();
  let release = () => {};
  state.stream.mockImplementationOnce(
    async ({ onRelease }: { onRelease: () => void }) => {
      release = onRelease;
      return new Response("test stream");
    },
  );
  expect((await POST(request(row.id, [user("u1", "Question")]))).status).toBe(
    200,
  );
  expect((await POST(request(row.id, [user("u2", "Another")]))).status).toBe(
    409,
  );
  release();
  expect(
    (
      await POST(
        request(row.id, [user("u2", "Another")], {
          excludedIds: ["systems:missing"],
        }),
      )
    ).status,
  ).toBe(400);
  expect((await state.store!.getConversation(row.id))?.excludedIds).toEqual([]);
});
test("malformed user parts and cross-origin requests never start model calls", async () => {
  const row = await state.store!.createConversation();
  expect(
    (
      await POST(
        request(row.id, [
          {
            id: "u",
            role: "user",
            parts: [{ type: "file", url: "http://private-host/secret" }],
          },
        ]),
      )
    ).status,
  ).toBe(400);
  const cross = new Request("http://localhost:8845/api/research", {
    method: "POST",
    headers: {
      origin: "https://other.test",
      "content-type": "application/json",
    },
    body: "{}",
  });
  expect((await POST(cross)).status).toBe(403);
  expect(state.stream).not.toHaveBeenCalled();
});

test("collection bookmark API distinguishes an omitted note from an explicit empty note", async () => {
  const collection = await state.store!.createCollection("Saved references");
  await state.store!.putItem(
    collection.id,
    "systems:test",
    "Keep my existing reasoning",
  );
  const send = (body: Record<string, unknown>) =>
    saveCollectionItem(
      new Request(
        `http://localhost:8845/api/collections/${collection.id}/items`,
        {
          method: "POST",
          headers: {
            "content-type": "application/json",
            origin: "http://localhost:8845",
          },
          body: JSON.stringify(body),
        },
      ),
      { params: Promise.resolve({ id: collection.id }) },
    );
  expect((await send({ referenceId: "systems:test" })).status).toBe(200);
  expect((await state.store!.getCollection(collection.id))?.items[0].note).toBe(
    "Keep my existing reasoning",
  );
  expect((await send({ referenceId: "systems:test", note: "" })).status).toBe(
    200,
  );
  expect((await state.store!.getCollection(collection.id))?.items[0].note).toBe(
    "",
  );
});

test("creating with an initial prompt persists it before navigation and accepts idempotent auto regeneration", async () => {
  const create = await createConversationRequest(
    new Request("http://localhost:8845/api/conversations", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        origin: "http://localhost:8845",
      },
      body: JSON.stringify({
        title: "Onboarding research",
        initialText: "  Find thoughtful onboarding references  ",
      }),
    }),
  );
  expect(create.status).toBe(201);
  const { id } = await create.json();
  const saved = await state.store!.getConversation(id);
  expect(saved?.messages).toHaveLength(1);
  expect(saved?.messages[0]).toMatchObject({
    role: "user",
    parts: [{ type: "text", text: "Find thoughtful onboarding references" }],
  });
  const firstAttempt = await POST(
    request(id, saved!.messages, { trigger: "regenerate-message" }),
  );
  expect(firstAttempt.status).toBe(503);
  expect((await state.store!.getConversation(id))?.messages).toEqual(
    saved!.messages,
  );
  state.configured = true;
  const retry = await POST(
    request(id, saved!.messages, { trigger: "regenerate-message" }),
  );
  expect(retry.status).toBe(200);
  expect((await state.store!.getConversation(id))?.messages).toEqual(
    saved!.messages,
  );
  expect(state.stream).toHaveBeenCalledOnce();
});

test("invalid initial prompts never create empty conversations", async () => {
  for (const initialText of ["   ", "x".repeat(30001)]) {
    const response = await createConversationRequest(
      new Request("http://localhost:8845/api/conversations", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ initialText }),
      }),
    );
    expect(response.status).toBe(400);
  }
  expect(await state.store!.listConversations()).toHaveLength(0);
});
