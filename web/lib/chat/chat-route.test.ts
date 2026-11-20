// Drives app/api/chat/route.ts itself (loaded through lib/test/resolve-app.mjs,
// which resolves "@/" and extensionless imports as Next does) against a
// throwaway config folder, with the provider's HTTP API replaced by a stub
// fetch, so no request leaves the machine. Run with `pnpm test`.
import assert from "node:assert/strict";
import { mkdtempSync, promises as fs, rmSync } from "node:fs";
import { register } from "node:module";
import os from "node:os";
import path from "node:path";
import { after, afterEach, before, beforeEach, describe, it, mock } from "node:test";
import { CONFIG_DIR_ENV, providerFile, saveProvider } from "../provider-store.ts";

register("../test/resolve-app.mjs", import.meta.url);

const KEY = "sk-route-test-0123456789abcdef";
const ENV_KEY = "sk-route-env-5555555555";
type Post = (req: Request) => Promise<Response>;
let POST: Post;
let dir = "";
let fetched: { url: string; init?: RequestInit }[] = [];

const call = async (body: unknown) => {
  const res = await POST(
    new Request("http://127.0.0.1/api/chat", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(body),
    }),
  );
  const text = await res.text();
  return { status: res.status, text, json: JSON.parse(text) as Record<string, unknown> };
};

/** The provider's HTTP API: `answer` builds each reply. */
const stubProvider = (answer: (url: string) => Response) =>
  mock.method(globalThis, "fetch", async (input: string | URL | Request, init?: RequestInit) => {
    const url = String(input instanceof Request ? input.url : input);
    fetched.push({ url, init });
    return answer(url);
  });

before(async () => {
  ({ POST } = (await import("../../app/api/chat/route.ts")) as { POST: Post });
});

beforeEach(() => {
  dir = mkdtempSync(path.join(os.tmpdir(), "ds-chat-route-"));
  process.env[CONFIG_DIR_ENV] = path.join(dir, "config");
  delete process.env.ANTHROPIC_API_KEY;
  fetched = [];
  mock.restoreAll();
});

// Each test's own folder goes as soon as it ends, not only the last one.
afterEach(() => {
  mock.restoreAll();
  if (dir) rmSync(dir, { recursive: true, force: true });
  dir = "";
});

after(() => {
  delete process.env[CONFIG_DIR_ENV];
  delete process.env.ANTHROPIC_API_KEY;
});

describe("POST /api/chat", () => {
  it("refuses a body that still carries a key, before any provider call", async () => {
    stubProvider(() => new Response("{}"));
    const r = await call({ messages: [], provider: { api_key: KEY, model: "m" } });
    assert.deepEqual([r.status, r.json.error], [400, "key_in_body"]);
    assert.ok(!r.text.includes(KEY));
    assert.deepEqual(fetched, []);
  });

  it("reports a broken saved provider and never falls back to the env key", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    stubProvider(() => new Response("{}"));
    await fs.mkdir(path.join(dir, "config"), { recursive: true });
    await fs.writeFile(providerFile(), `damaged ${KEY} `.repeat(200));
    const r = await call({ messages: [{ role: "user", content: "hi" }] });
    assert.match(String(r.json.error), /saved provider file cannot be read/);
    assert.deepEqual(fetched, [], "the env key was not used");
    assert.ok(!r.text.includes(KEY) && !r.text.includes(ENV_KEY));
  });

  it("answers no_provider with nothing saved and no env key", async () => {
    stubProvider(() => new Response("{}"));
    const r = await call({ messages: [] });
    assert.equal(r.json.error, "no_provider");
    assert.deepEqual(fetched, []);
  });

  it("redacts the key from a provider error that quotes it", async () => {
    // Saved past the parse rule on purpose, so the error's URL carries the key.
    await saveProvider({ api: "openai", base_url: `https://api.openai.com/v1?k=${KEY}`, model: "m", api_key: KEY }, "replace");
    stubProvider(() => new Response("nope", { status: 401 }));
    const r = await call({ messages: [{ role: "user", content: "hi" }] });
    assert.equal(fetched.length, 1);
    assert.match(String(r.json.error), /\[redacted\].*answered HTTP 401/);
    assert.ok(!r.text.includes(KEY));
  });

  it("uses the saved key over the env key, and never returns it", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    await saveProvider({ api: "openai", base_url: "https://api.openai.com/v1", model: "m", api_key: KEY }, "replace");
    stubProvider(() => Response.json({ choices: [{ message: { content: "Try the linear package." } }] }));
    const r = await call({ messages: [{ role: "user", content: "hi" }] });
    assert.equal(r.status, 200);
    assert.match(String(r.json.raw), /linear package/);
    const auth = new Headers(fetched[0].init?.headers).get("authorization");
    assert.equal(auth, `Bearer ${KEY}`);
    assert.ok(!r.text.includes(KEY) && !r.text.includes(ENV_KEY));
  });

  it("passes a run's own error through without the key", async () => {
    await saveProvider({ api: "openai", base_url: "https://api.openai.com/v1", model: "m", api_key: KEY }, "replace");
    // Every answer asks for a tool that does not exist, so the loop stops at its round limit.
    stubProvider(() =>
      Response.json({ choices: [{ message: { content: null, tool_calls: [{ id: "c1", type: "function", function: { name: "nope", arguments: "{}" } }] } }] }),
    );
    const r = await call({ messages: [{ role: "user", content: "hi" }] });
    assert.match(String(r.json.error), /stopped after \d+ tool rounds/);
    assert.ok(!r.text.includes(KEY));
  });
});
