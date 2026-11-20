// POST /api/mcp. One JSON-RPC message, or a batch, in. Replies go out as
// application/json. A body that is only notifications gets 202. There is
// no session, so GET is 405 and DELETE is an empty acknowledgement.
import { handleBatch, MCP_BODY_LIMIT } from "@/server/mcp";
import { isAllowedHost } from "@/server/request-host";
import { HttpError, mutationGuard } from "@/server/research/http";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

function refused() {
  return Response.json(
    {
      error:
        "This personal research app only accepts loopback hosts or its configured private origin.",
    },
    { status: 403 },
  );
}

function tooLarge() {
  return Response.json(
    {
      jsonrpc: "2.0",
      id: null,
      error: {
        code: -32600,
        message: `request body exceeds the ${MCP_BODY_LIMIT}-byte limit`,
      },
    },
    { status: 413 },
  );
}

// Counts bytes as they arrive and cancels past the cap, so a request
// without Content-Length cannot fill memory before the size check.
async function readBody(request: Request) {
  const reader = request.body?.getReader();
  if (!reader) return "";
  const parts: Uint8Array[] = [];
  let total = 0;
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    total += value.byteLength;
    if (total > MCP_BODY_LIMIT) {
      await reader.cancel();
      return null;
    }
    parts.push(value);
  }
  const body = new Uint8Array(total);
  let offset = 0;
  for (const part of parts) {
    body.set(part, offset);
    offset += part.byteLength;
  }
  // Invalid UTF-8 is refused like unparseable JSON, as server/routes.py does,
  // rather than decoded to U+FFFD and run.
  try {
    return new TextDecoder("utf-8", { fatal: true }).decode(body);
  } catch {
    return undefined;
  }
}

function rpcError(status: number, code: number, message: string) {
  return Response.json(
    { jsonrpc: "2.0", id: null, error: { code, message } },
    { status },
  );
}

export async function POST(request: Request) {
  if (!isAllowedHost(request.headers.get("host"))) return refused();
  // Tool calls run server-side, so a page on another site must not be able
  // to start them with a no-preflight POST. MCP clients send no Origin or
  // Sec-Fetch-Site and still pass; they must send application/json.
  try {
    mutationGuard(request, { originlessClients: true });
  } catch (error) {
    if (!(error instanceof HttpError)) throw error;
    return Response.json({ error: error.message }, { status: error.status });
  }
  const declared = request.headers.get("content-length");
  if (declared && /^\d+$/.test(declared) && Number(declared) > MCP_BODY_LIMIT) {
    return tooLarge();
  }
  const text = await readBody(request);
  if (text === null) return tooLarge();
  if (text === "") return rpcError(400, -32600, "a JSON-RPC body is required");
  let raw: unknown;
  try {
    if (text === undefined) throw new Error("invalid UTF-8");
    raw = JSON.parse(text);
  } catch {
    return rpcError(400, -32700, "unparseable JSON");
  }
  const out = await handleBatch(raw);
  return out === null
    ? new Response(null, { status: 202 })
    : Response.json(out);
}

export function GET(request: Request) {
  if (!isAllowedHost(request.headers.get("host"))) return refused();
  return Response.json(
    { error: "streamable HTTP is POST-only on this server" },
    { status: 405 },
  );
}

export function DELETE(request: Request) {
  if (!isAllowedHost(request.headers.get("host"))) return refused();
  return new Response(null, { status: 200 });
}
