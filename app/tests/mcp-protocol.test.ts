import { afterEach, expect, test, vi } from "vitest";
import { handleBatch } from "@/server/mcp";
import { DELETE, GET, POST } from "@/app/api/mcp/route";

afterEach(() => vi.unstubAllEnvs());
const json = { host: "127.0.0.1:8845", "content-type": "application/json" };
function post(body: BodyInit, headers: Record<string, string> = json) {
  return POST(
    new Request("http://127.0.0.1:8845/api/mcp", {
      method: "POST",
      headers,
      body,
    }),
  );
}
const at = (method: string, host: string) =>
  new Request("http://127.0.0.1:8845/api/mcp", { method, headers: { host } });

test("every method refuses a host that is not loopback or the private origin", async () => {
  const foreign = "attacker.example";
  expect((await post("{}", { ...json, host: foreign })).status).toBe(403);
  expect(GET(at("GET", foreign)).status).toBe(403);
  expect(DELETE(at("DELETE", foreign)).status).toBe(403);
  expect(GET(at("GET", "127.0.0.1:8845")).status).toBe(405);
  expect(DELETE(at("DELETE", "127.0.0.1:8845")).status).toBe(200);
});

test("an empty body is a 400 asking for a body, as the python server answers", async () => {
  const response = await post("");
  expect(response.status).toBe(400);
  expect(await response.json()).toMatchObject({
    error: { code: -32600, message: "a JSON-RPC body is required" },
  });
});

test("a body that is not UTF-8 is unparseable, not decoded and run", async () => {
  const response = await post(
    new Uint8Array([0x7b, 0x22, 0xff, 0xfe, 0x22, 0x3a, 0x31, 0x7d]),
  );
  expect(response.status).toBe(400);
  expect(await response.json()).toMatchObject({ error: { code: -32700 } });
});

test("a body of notifications only is accepted with 202 and no reply", async () => {
  const response = await post(
    JSON.stringify([
      { jsonrpc: "2.0", method: "notifications/initialized" },
      { jsonrpc: "2.0", method: "notifications/cancelled" },
    ]),
  );
  expect(response.status).toBe(202);
  expect(await response.text()).toBe("");
});

test("dispatch errors carry their JSON-RPC codes", async () => {
  expect(
    await handleBatch({ jsonrpc: "2.0", id: 1, method: "tools/destroy" }),
  ).toMatchObject({ id: 1, error: { code: -32601 } });
  expect(await handleBatch({ jsonrpc: "2.0", id: 2, method: 7 })).toMatchObject(
    { id: 2, error: { code: -32600 } },
  );
  expect(
    await handleBatch({ jsonrpc: "2.0", id: 3, method: "ping", params: [] }),
  ).toMatchObject({ id: 3, error: { code: -32602 } });
  expect(
    await handleBatch({
      jsonrpc: "2.0",
      id: 4,
      method: "tools/call",
      params: { name: "searchLibrary", arguments: ["dark"] },
    }),
  ).toMatchObject({
    id: 4,
    error: { code: -32602, message: "arguments must be an object" },
  });
  expect(
    await handleBatch({
      jsonrpc: "2.0",
      id: 5,
      method: "tools/call",
      params: { name: "dropTables", arguments: {} },
    }),
  ).toMatchObject({ id: 5, error: { code: -32602 } });
});

test("a batch answers each member, including one that is not an object", async () => {
  const replies = (await handleBatch([
    { jsonrpc: "2.0", id: 1, method: "ping" },
    "not a request",
    { jsonrpc: "2.0", method: "notifications/initialized" },
  ])) as { id: unknown; result?: unknown; error?: { code: number } }[];
  expect(replies).toHaveLength(2);
  expect(replies[0]).toEqual({ jsonrpc: "2.0", id: 1, result: {} });
  expect(replies[1]).toMatchObject({ id: null, error: { code: -32600 } });
});

test("a tool call with invalid arguments is a tool error, not a protocol error", async () => {
  const reply = (await handleBatch({
    jsonrpc: "2.0",
    id: 9,
    method: "tools/call",
    params: { name: "searchLibrary", arguments: { query: 5 } },
  })) as { result: { isError?: boolean; content: { type: string }[] } };
  expect(reply.result.isError).toBe(true);
  expect(reply.result.content[0].type).toBe("text");
});

test("initialize names this server and keeps the client's protocol version", async () => {
  expect(
    await handleBatch({
      jsonrpc: "2.0",
      id: 1,
      method: "initialize",
      params: { protocolVersion: "2025-06-18" },
    }),
  ).toMatchObject({
    result: {
      protocolVersion: "2025-06-18",
      serverInfo: { name: "constellations" },
    },
  });
});
