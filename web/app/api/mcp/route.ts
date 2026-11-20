// POST /api/mcp — the MCP server over streamable HTTP, for coding agents that
// reach a hosted deployment instead of spawning server/mcp.py locally. One
// JSON-RPC message (or a batch) in, the replies as application/json out;
// notification-only bodies get 202. Stateless: no session header, GET gets a
// 405 because there is no SSE stream to open. The JSON-RPC handling lives in
// lib/mcp-rpc.ts and mirrors server/mcp.py exactly.
import { handleBatch, textOverLimit, tooLargeResponse } from "@/lib/mcp-batch";
import { handle, type Rpc } from "@/lib/mcp-rpc";

export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  // web/proxy.ts refuses an oversized Content-Length first; this catches a body
  // that reads larger than it declared.
  const text = await req.text();
  if (textOverLimit(text)) return tooLargeResponse();
  // An empty body is an invalid request, not a parse error, as in server/routes.py.
  if (text === "")
    return Response.json({ jsonrpc: "2.0", id: null, error: { code: -32600, message: "a JSON-RPC body is required" } }, { status: 400 });
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
