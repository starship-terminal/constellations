// The transport rules for POST /api/mcp that do not depend on the tool layer,
// kept apart so they are testable without loading the library. Mirrors
// handle_batch() in server/mcp.py and the body cap in server/routes.py.

export const MCP_BODY_LIMIT = 256_000;

export type RpcReply = Record<string, unknown>;

const invalid = (message: string): RpcReply => ({
  jsonrpc: "2.0",
  id: null,
  error: { code: -32600, message },
});

/** The JSON-RPC 413 reply, shared by the proxy (Content-Length) and the route. */
export const tooLarge = (): RpcReply =>
  invalid(`request body exceeds the ${MCP_BODY_LIMIT}-byte limit`);

/** Whether a body of this many bytes is over the cap (the limit itself passes). */
export const overLimit = (bytes: number): boolean => bytes > MCP_BODY_LIMIT;

/** Whether this text, measured in UTF-8 bytes rather than characters, is over the cap. */
export const textOverLimit = (text: string): boolean => overLimit(new TextEncoder().encode(text).length);

/** The 413 response the proxy (Content-Length) and the route (actual body) both send. */
export const tooLargeResponse = (): Response => Response.json(tooLarge(), { status: 413 });

/**
 * The reply body for one parsed payload, or null when there is nothing to send
 * (a lone notification, or a batch of only notifications: HTTP 202). An empty
 * batch is one Invalid Request, and each non-object member of a batch is its
 * own Invalid Request, per JSON-RPC 2.0 section 6.
 */
export async function handleBatch(
  raw: unknown,
  handle: (req: Record<string, unknown>) => Promise<RpcReply | null>,
): Promise<RpcReply | RpcReply[] | null> {
  const one = async (m: unknown) =>
    m && typeof m === "object" && !Array.isArray(m)
      ? handle(m as Record<string, unknown>)
      : invalid("a JSON-RPC request must be an object");
  if (!Array.isArray(raw)) return one(raw);
  if (!raw.length) return invalid("an empty batch is not a valid request");
  const replies: RpcReply[] = [];
  for (const m of raw) {
    const r = await one(m);
    if (r) replies.push(r);
  }
  return replies.length ? replies : null;
}
