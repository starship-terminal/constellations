import { afterEach, expect, test, vi } from "vitest";
import { readApiKey, readSettings, modelFor } from "@/server/research/settings";
import { PATCH } from "@/app/api/settings/route";
const state = vi.hoisted(() => ({ saved: {} as Record<string, unknown> }));
vi.mock("@/server/db", () => ({
  getStore: async () => ({
    getSettings: async () => state.saved,
    updateSettings: async (
      mutate: (saved: Record<string, unknown>) => Record<string, unknown>,
    ) => {
      state.saved = mutate(state.saved);
    },
  }),
}));
afterEach(() => {
  state.saved = {};
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

test("an explicit null endpoint clears environment defaults while an absent setting inherits them", async () => {
  vi.stubEnv("DESIGN_RESEARCH_BASE_URL", "https://global-proxy.example/v1");
  vi.stubEnv("OPENAI_BASE_URL", "https://openai-proxy.example/v1");
  state.saved = { provider: "openai" };
  expect((await readSettings()).baseURL).toBe(
    "https://global-proxy.example/v1",
  );
  state.saved = { provider: "openai", baseURL: null };
  expect((await readSettings()).baseURL).toBeNull();
  state.saved = { provider: "anthropic", baseURL: null };
  expect((await readSettings()).baseURL).toBeNull();
});

test("cleared endpoint reaches official SDK endpoints even when SDK environment variables are set", async () => {
  vi.stubEnv("OPENAI_BASE_URL", "https://must-not-be-used.example/v1");
  vi.stubEnv("ANTHROPIC_BASE_URL", "https://must-not-be-used.example/v1");
  vi.stubEnv("OPENAI_API_KEY", "test-only-key");
  vi.stubEnv("ANTHROPIC_API_KEY", "test-only-key");
  const urls: string[] = [];
  vi.stubGlobal("fetch", async (url: string) => {
    urls.push(String(url));
    return new Response("data: [DONE]\n\n", {
      headers: { "content-type": "text/event-stream" },
    });
  });
  for (const provider of ["openai", "anthropic"] as const) {
    state.saved = { provider, baseURL: null };
    const model = modelFor(await readSettings());
    const response = await model.doStream({
      prompt: [
        { role: "user", content: [{ type: "text", text: "Endpoint test" }] },
      ],
      maxOutputTokens: 10,
    });
    await response.stream.cancel();
  }
  expect(urls).toEqual([
    "https://api.openai.com/v1/responses",
    "https://api.anthropic.com/v1/messages",
  ]);
});

test("a stored key overrides the environment and only reports its source", async () => {
  vi.stubEnv("OPENAI_API_KEY", "env-openai");
  vi.stubEnv("ANTHROPIC_API_KEY", "env-anthropic");
  state.saved = { apiKeys: { openai: "stored-openai" } };
  const settings = await readSettings();
  expect(settings.keySources).toEqual({
    openai: "stored",
    anthropic: "environment",
  });
  expect(settings.providers).toEqual({ openai: true, anthropic: true });
  expect(JSON.stringify(settings)).not.toContain("stored-openai");
  expect(await readApiKey("openai")).toBe("stored-openai");
  expect(await readApiKey("anthropic")).toBe("env-anthropic");
  state.saved = {};
  expect((await readSettings()).keySources).toEqual({
    openai: "environment",
    anthropic: "environment",
  });
  vi.stubEnv("OPENAI_API_KEY", "");
  expect(await readApiKey("openai")).toBeUndefined();
});

test("settings PATCH sets, keeps and clears provider keys without returning them", async () => {
  vi.stubEnv("OPENAI_API_KEY", "");
  vi.stubEnv("ANTHROPIC_API_KEY", "");
  const patch = (body: Record<string, unknown>) =>
    PATCH(
      new Request("http://localhost:8845/api/settings", {
        method: "PATCH",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(body),
      }),
    );
  expect((await patch({ apiKeys: { openai: "sk-live" } })).status).toBe(200);
  expect(state.saved.apiKeys).toEqual({ openai: "sk-live" });
  await patch({ apiKeys: { anthropic: "sk-ant" } });
  expect(state.saved.apiKeys).toEqual({
    openai: "sk-live",
    anthropic: "sk-ant",
  });
  const response = await patch({ apiKeys: { openai: null } });
  expect(state.saved.apiKeys).toEqual({ anthropic: "sk-ant" });
  const body = await response.json();
  expect(body.keySources).toEqual({ openai: null, anthropic: "stored" });
  expect(JSON.stringify(body)).not.toContain("sk-ant");
});
