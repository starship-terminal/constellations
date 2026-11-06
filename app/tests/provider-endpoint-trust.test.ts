import { afterEach, beforeEach, expect, test, vi } from "vitest";
import { PATCH } from "@/app/api/settings/route";
import { POST } from "@/app/api/models/route";
import { readSettings } from "@/server/research/settings";

// Saved and environment keys may reach only the provider's own API or the
// endpoint the owner saved. Every key below is an invented test value.
const state = vi.hoisted(() => ({
  saved: {} as Record<string, unknown>,
  probes: [] as { baseURL: string | null; key: string | undefined }[],
}));
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
vi.mock("@/server/research/models", () => ({
  discoverModels: async (
    settings: { baseURL: string | null },
    key: string | undefined,
  ) => {
    state.probes.push({ baseURL: settings.baseURL, key });
    return ["test-model"];
  },
}));
// Never let the developer's own provider environment leak into a case.
beforeEach(() => {
  for (const name of [
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "OPENAI_BASE_URL",
    "ANTHROPIC_BASE_URL",
    "DESIGN_RESEARCH_BASE_URL",
    "DESIGN_RESEARCH_PROVIDER",
  ])
    vi.stubEnv(name, undefined);
});
afterEach(() => {
  state.saved = {};
  state.probes = [];
  vi.unstubAllEnvs();
});
function send(
  handler: (request: Request) => Promise<Response>,
  method: string,
  path: string,
  body: unknown,
) {
  return handler(
    new Request(`http://localhost:8845${path}`, {
      method,
      headers: { "content-type": "application/json" },
      body: JSON.stringify(body),
    }),
  );
}
const probe = (body: unknown) => send(POST, "POST", "/api/models", body);
async function patch(body: unknown) {
  const response = await send(PATCH, "PATCH", "/api/settings", body);
  // No PATCH response ever echoes a submitted key.
  expect(await response.clone().text()).not.toMatch(/test-key-/);
  return response;
}

test("a probe to a new endpoint without its own key is refused before any request", async () => {
  state.saved = {
    provider: "openai",
    apiKeys: { openai: "test-key-stored" },
  };
  const response = await probe({ baseURL: "https://elsewhere.example/v1" });
  expect(response.status).toBe(400);
  expect(await response.text()).not.toContain("test-key-stored");
  expect(state.probes).toEqual([]);
});

test("an environment key is not sent to a new endpoint either", async () => {
  vi.stubEnv("OPENAI_API_KEY", "test-key-env");
  state.saved = { provider: "openai" };
  expect(
    (await probe({ baseURL: "https://elsewhere.example/v1" })).status,
  ).toBe(400);
  expect(state.probes).toEqual([]);
});

test("a probe that brings its own key may test a new endpoint", async () => {
  state.saved = { provider: "openai", apiKeys: { openai: "test-key-stored" } };
  const response = await probe({
    baseURL: "https://elsewhere.example/v1",
    apiKey: "test-key-probe",
  });
  expect(response.status).toBe(200);
  expect(state.probes).toEqual([
    { baseURL: "https://elsewhere.example/v1", key: "test-key-probe" },
  ]);
});

test("the saved endpoint and the provider's own API use the saved or environment key", async () => {
  vi.stubEnv("ANTHROPIC_API_KEY", "test-key-env");
  state.saved = {
    provider: "openai",
    baseURL: "https://proxy.example/v1",
    apiKeys: { openai: "test-key-stored" },
  };
  expect((await probe({ baseURL: "https://proxy.example/v1" })).status).toBe(
    200,
  );
  expect((await probe({})).status).toBe(200);
  expect((await probe({ baseURL: null })).status).toBe(200);
  expect((await probe({ baseURL: "https://api.openai.com/v1" })).status).toBe(
    200,
  );
  expect(
    (
      await probe({
        provider: "anthropic",
        baseURL: "https://api.anthropic.com/v1",
      })
    ).status,
  ).toBe(200);
  expect(state.probes.map((entry) => entry.key)).toEqual([
    "test-key-stored",
    "test-key-stored",
    "test-key-stored",
    "test-key-stored",
    "test-key-env",
  ]);
});

test("plain HTTP endpoints are accepted only for loopback hosts", async () => {
  for (const baseURL of [
    "http://localhost:1234/v1",
    "http://127.0.0.1:1234/v1",
    "http://[::1]:1234/v1",
  ]) {
    expect((await probe({ baseURL, apiKey: "test-key-probe" })).status).toBe(
      200,
    );
    expect((await patch({ baseURL })).status).toBe(200);
  }
  for (const baseURL of [
    "http://elsewhere.example/v1",
    "http://192.168.1.20:1234/v1",
  ]) {
    expect((await probe({ baseURL, apiKey: "test-key-probe" })).status).toBe(
      400,
    );
    expect((await patch({ baseURL })).status).toBe(400);
  }
  expect(state.probes).toHaveLength(3);
});

test("an endpoint stored before the HTTPS rule still loads", async () => {
  state.saved = { provider: "openai", baseURL: "http://192.168.1.20:1234/v1" };
  expect((await readSettings()).baseURL).toBe("http://192.168.1.20:1234/v1");
});

test("moving the endpoint to a new origin without a new key drops that provider's stored key", async () => {
  state.saved = {
    provider: "openai",
    apiKeys: { openai: "test-key-openai", anthropic: "test-key-anthropic" },
  };
  const response = await patch({ baseURL: "https://elsewhere.example/v1" });
  expect(response.status).toBe(200);
  expect(state.saved.apiKeys).toEqual({ anthropic: "test-key-anthropic" });
  expect((await response.json()).keySources.openai).toBeNull();
});

test("moving the endpoint with a new key in the same PATCH stores that key", async () => {
  state.saved = { provider: "openai", apiKeys: { openai: "test-key-old" } };
  expect(
    (
      await patch({
        baseURL: "https://elsewhere.example/v1",
        apiKeys: { openai: "test-key-new" },
      })
    ).status,
  ).toBe(200);
  expect(state.saved.apiKeys).toEqual({ openai: "test-key-new" });
});

test("the same origin, the provider's own API and a bare save keep the stored key", async () => {
  state.saved = {
    provider: "openai",
    baseURL: "https://proxy.example/v1",
    apiKeys: { openai: "test-key-stored" },
  };
  await patch({ baseURL: "https://proxy.example/other/v1" });
  await patch({ model: "test-model" });
  await patch({ baseURL: "https://proxy.example/v1" });
  await patch({ baseURL: null });
  expect(state.saved.apiKeys).toEqual({ openai: "test-key-stored" });
});

test("switching provider to a new endpoint drops only the target provider's key", async () => {
  state.saved = {
    provider: "openai",
    apiKeys: { openai: "test-key-openai", anthropic: "test-key-anthropic" },
  };
  await patch({
    provider: "anthropic",
    baseURL: "https://elsewhere.example/v1",
  });
  expect(state.saved.apiKeys).toEqual({ openai: "test-key-openai" });
});

test("a saved endpoint for one provider does not vouch for the other provider's key", async () => {
  state.saved = {
    provider: "openai",
    baseURL: "https://proxy.example/v1",
    apiKeys: { openai: "test-key-openai", anthropic: "test-key-anthropic" },
  };
  expect((await probe({ provider: "anthropic" })).status).toBe(400);
  expect(
    (
      await probe({
        provider: "anthropic",
        baseURL: "https://proxy.example/v1",
      })
    ).status,
  ).toBe(400);
  expect(state.probes).toEqual([]);
  await patch({ provider: "anthropic", baseURL: "https://proxy.example/v1" });
  expect(state.saved.apiKeys).toEqual({ openai: "test-key-openai" });
});

test("a provider-only switch keeps the key when the endpoint becomes the provider's own or the environment's", async () => {
  state.saved = {
    provider: "openai",
    baseURL: "https://proxy.example/v1",
    apiKeys: { openai: "test-key-openai", anthropic: "test-key-anthropic" },
  };
  await patch({ provider: "anthropic" });
  expect(state.saved.apiKeys).toEqual({
    openai: "test-key-openai",
    anthropic: "test-key-anthropic",
  });
  vi.stubEnv("ANTHROPIC_BASE_URL", "https://operator-proxy.example/v1");
  await patch({ provider: "openai" });
  await patch({ provider: "anthropic" });
  expect(state.saved.apiKeys).toEqual({
    openai: "test-key-openai",
    anthropic: "test-key-anthropic",
  });
});
