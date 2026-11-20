import { afterEach, expect, test, vi } from "vitest";
import { handleBatch, MCP_BATCH_LIMIT, MCP_BODY_LIMIT } from "@/server/mcp";
import { POST } from "@/app/api/mcp/route";

test("tools/list advertises argument names and defaults", async () => {
  const reply = await handleBatch({
    jsonrpc: "2.0",
    id: 1,
    method: "tools/list",
  });
  const tools = (
    reply as {
      result: {
        tools: {
          name: string;
          inputSchema: {
            properties: Record<string, { default?: unknown }>;
            required?: string[];
          };
        }[];
      };
    }
  ).result.tools;
  const read = tools.find((tool) => tool.name === "readPackageDocument");
  const media = tools.find((tool) => tool.name === "listReferenceMedia");
  expect(read?.inputSchema.properties.path.default).toBe("README.md");
  expect(read?.inputSchema.properties.offset.default).toBe(0);
  expect(read?.inputSchema.required).toEqual(["referenceId"]);
  expect(media?.inputSchema.required).toEqual(["referenceId"]);
});

test("a batch over the cap is one error, not a pile of image calls", async () => {
  const raw = Array.from({ length: MCP_BATCH_LIMIT + 1 }, (_, i) => ({
    jsonrpc: "2.0",
    id: i,
    method: "ping",
  }));
  const reply = await handleBatch(raw);
  expect(reply).toMatchObject({
    error: {
      code: -32600,
      message: expect.stringContaining(String(MCP_BATCH_LIMIT)),
    },
  });
});

test("a body without Content-Length stops at the byte cap", async () => {
  const body = new Uint8Array(MCP_BODY_LIMIT + 8);
  const request = new Request("http://127.0.0.1/api/mcp", {
    method: "POST",
    headers: { host: "127.0.0.1", "content-type": "application/json" },
    body,
    duplex: "half",
  } as RequestInit);
  const response = await POST(request);
  expect(response.status).toBe(413);
});

afterEach(() => vi.unstubAllEnvs());
const ping = JSON.stringify({ jsonrpc: "2.0", id: 1, method: "ping" });
function post(headers: Record<string, string>) {
  return POST(
    new Request("http://127.0.0.1:8845/api/mcp", {
      method: "POST",
      headers,
      body: ping,
    }),
  );
}

test("an MCP client with no Origin or Sec-Fetch-Site gets its reply", async () => {
  const response = await post({
    host: "127.0.0.1:8845",
    "content-type": "application/json",
  });
  expect(response.status).toBe(200);
  expect(await response.json()).toEqual({ jsonrpc: "2.0", id: 1, result: {} });
});

test("a page on another site cannot start tool calls", async () => {
  const json = { host: "127.0.0.1:8845", "content-type": "application/json" };
  // A no-preflight form or text/plain POST.
  expect(
    (await post({ host: "127.0.0.1:8845", "content-type": "text/plain" }))
      .status,
  ).toBe(415);
  expect((await post({ host: "127.0.0.1:8845" })).status).toBe(415);
  expect((await post({ ...json, "sec-fetch-site": "cross-site" })).status).toBe(
    403,
  );
  expect(
    (await post({ ...json, origin: "https://attacker.example" })).status,
  ).toBe(403);
  expect(
    (await post({ ...json, origin: "http://127.0.0.1:8845" })).status,
  ).toBe(200);
});

test("the private origin accepts originless MCP clients and refuses foreign pages", async () => {
  const origin = "https://research.tail123.ts.net:8108";
  vi.stubEnv("DESIGN_RESEARCH_PRIVATE_ORIGIN", origin);
  const json = {
    host: "research.tail123.ts.net:8108",
    "content-type": "application/json",
  };
  expect((await post(json)).status).toBe(200);
  expect((await post({ ...json, origin })).status).toBe(200);
  expect(
    (await post({ ...json, origin: "https://attacker.example" })).status,
  ).toBe(403);
  expect((await post({ ...json, "sec-fetch-site": "cross-site" })).status).toBe(
    403,
  );
});
