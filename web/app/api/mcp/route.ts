// POST /api/mcp — the MCP server over streamable HTTP, for coding agents that
// reach a hosted deployment instead of spawning server/mcp.py locally. One
// JSON-RPC message (or a batch) in, the replies as application/json out;
// notification-only bodies get 202. Stateless: no session header, GET gets a
// 405 because there is no SSE stream to open. Mirrors server/mcp.py exactly.
import { call, SPECS } from "@/lib/chat/library";
import { handleBatch, textOverLimit, tooLargeResponse } from "@/lib/mcp-batch";

export const dynamic = "force-dynamic";

const SERVER_INFO = { name: "design-systems", version: "1.0.0" };
const INSTRUCTIONS =
  "Read-only search over the design-systems library: measured systems/ " +
  "packages first, refero for breadth. Media url fields are site-relative; " +
  "prefix them with the server origin.";

type Rpc = { jsonrpc?: string; id?: unknown; method?: unknown; params?: unknown };

const result = (req: Rpc, result: unknown) =>
  req.id === undefined ? null : { jsonrpc: "2.0", id: req.id, result };

const error = (req: Rpc, code: number, message: string) =>
  req.id === undefined ? null : { jsonrpc: "2.0", id: req.id ?? null, error: { code, message } };

async function callTool(name: string, args: unknown) {
  try {
    const out = await call(name, (args as Record<string, unknown>) ?? {});
    const img = (out as { _image?: { url: string; name: string; data: string; media_type: string } })._image;
    if (img)
      return {
        content: [
          { type: "text", text: JSON.stringify({ url: img.url, name: img.name }) },
          { type: "image", data: img.data, mimeType: img.media_type },
        ],
      };
    return { content: [{ type: "text", text: JSON.stringify(out) }] };
  } catch (e) {
    // One malformed call must never end the session: report it as a tool
    // error and keep the caller's loop alive.
    return { content: [{ type: "text", text: String(e instanceof Error ? e.message : e).slice(0, 400) }], isError: true };
  }
}

const isObj = (v: unknown): v is Record<string, unknown> => typeof v === "object" && v !== null && !Array.isArray(v);

async function handle(req: Rpc) {
  // A malformed message (a non-string method, params that are not an object)
  // gets a JSON-RPC error, and anything unexpected inside a handler is -32603,
  // the same contract as server/mcp.py's handle().
  try {
    return await dispatch(req);
  } catch (e) {
    console.error("mcp:", e);
    return error(req, -32603, "internal error");
  }
}

async function dispatch(req: Rpc) {
  const method = req.method;
  // Without a method it is not a notification either, so it is answered even
  // when it carries no id.
  if (typeof method !== "string")
    return { jsonrpc: "2.0", id: req.id ?? null, error: { code: -32600, message: "method must be a string" } };
  const params = req.params ?? {};
  if (!isObj(params)) return error(req, -32602, "params must be an object");
  if (method === "initialize")
    return result(req, {
      protocolVersion: typeof params.protocolVersion === "string" ? params.protocolVersion : "2025-03-26",
      capabilities: { tools: { listChanged: false } },
      serverInfo: SERVER_INFO,
      instructions: INSTRUCTIONS,
    });
  if (method === "ping") return result(req, {});
  if (method === "tools/list")
    return result(req, {
      tools: SPECS.map((s) => ({ name: s.name, description: s.description, inputSchema: s.parameters })),
    });
  if (method === "tools/call") {
    const name = typeof params.name === "string" ? params.name : "";
    if (!SPECS.some((s) => s.name === name)) return error(req, -32602, `unknown tool '${name}'`);
    const args = params.arguments;
    if (args != null && !isObj(args)) return error(req, -32602, "arguments must be an object");
    return result(req, await callTool(name, args));
  }
  if (method.startsWith("notifications/")) return null;
  return error(req, -32601, `no method '${method}'`);
}

export async function POST(req: Request) {
  // web/proxy.ts refuses an oversized Content-Length first; this catches a body
  // that reads larger than it declared.
  const text = await req.text();
  if (textOverLimit(text)) return tooLargeResponse();
  let raw: unknown;
  try {
    raw = JSON.parse(text);
  } catch {
    return Response.json({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "unparseable JSON" } }, { status: 400 });
  }
  const out = await handleBatch(raw, (m) => handle(m as Rpc));
  return out === null ? new Response(null, { status: 202 }) : Response.json(out);
}

export function GET() {
  return Response.json({ error: "streamable HTTP is POST-only on this server" }, { status: 405 });
}

export function DELETE() {
  // Stateless server: session teardown is a no-op acknowledgement.
  return new Response(null, { status: 200 });
}
