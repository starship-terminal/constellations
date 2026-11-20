// The JSON-RPC side of POST /api/mcp: initialize, ping, tools/list,
// tools/call and notifications, over the gallery's tool layer. Kept out of the
// route so the node test runner can load it. Mirrors server/mcp.py exactly.
import { call, SPECS, ToolError } from "./chat/library.ts";

export const SERVER_INFO = { name: "design-systems", version: "1.0.0" };
export const INSTRUCTIONS =
  "Read-only search over the design-systems library: measured systems/ " +
  "packages first, refero for breadth. Media url fields are site-relative; " +
  "prefix them with the server origin.";

export type Rpc = { jsonrpc?: string; id?: unknown; method?: unknown; params?: unknown };

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
    // error and keep the caller's loop alive. A ToolError's text is written for
    // the caller (call() strips server detail); anything else is a bug, whose
    // detail goes to the log only, as server/mcp.py's _call does.
    if (e instanceof ToolError) return { content: [{ type: "text", text: e.message.slice(0, 400) }], isError: true };
    console.error(`mcp: ${name}:`, e);
    return { content: [{ type: "text", text: `${name} failed` }], isError: true };
  }
}

const isObj = (v: unknown): v is Record<string, unknown> => typeof v === "object" && v !== null && !Array.isArray(v);

export async function handle(req: Rpc) {
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
