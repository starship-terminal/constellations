import { afterEach, expect, test, vi } from "vitest";
import { readSettings, modelFor } from "@/server/research/settings";
const state = vi.hoisted(() => ({ saved: {} as Record<string, unknown> }));
vi.mock("@/server/db", () => ({
  getStore: async () => ({ getSettings: async () => state.saved }),
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
