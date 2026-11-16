// POST /api/mcp. One JSON-RPC message, or a batch, in. Replies go out as
// application/json. A body that is only notifications gets 202. There is
// no session, so GET is 405 and DELETE is an empty acknowledgement.
import { handleBatch, MCP_BODY_LIMIT } from "@/server/mcp";
import { isAllowedHost } from "@/server/request-host";

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

export async function POST(request: Request) {
  if (!isAllowedHost(request.headers.get("host"))) return refused();
  const declared = request.headers.get("content-length");
  if (declared && /^\d+$/.test(declared) && Number(declared) > MCP_BODY_LIMIT) {
    return tooLarge();
  }
  const text = await request.text();
  if (text.length > MCP_BODY_LIMIT) return tooLarge();
  let raw: unknown;
  try {
    raw = JSON.parse(text);
  } catch {
    return Response.json(
      {
        jsonrpc: "2.0",
        id: null,
        error: { code: -32700, message: "unparseable JSON" },
      },
      { status: 400 },
    );
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
