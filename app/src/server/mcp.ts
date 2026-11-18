// The JSON-RPC handler behind POST /api/mcp. The tools are the same ones
// the research chat uses, with no pinned or excluded references. One bad
// call comes back as a tool error so the client's session keeps going.
import { asSchema } from "ai";
import { researchTools } from "@/server/research/agent";
import { readLocalImage } from "@/server/sources/files";
import { readReferenceImage } from "@/server/sources";

export const MCP_BODY_LIMIT = 256_000;
// One image tool can return a few megabytes of base64. A batch of them
// would keep every reply until the last one finished.
export const MCP_BATCH_LIMIT = 8;
export const SERVER_INFO = { name: "constellations", version: "1.0.0" };
export const INSTRUCTIONS =
  "Read-only search over a private Constellations library. " +
  "Measured systems come first. Refero entries are third-party interpretations. " +
  "Media URLs are site-relative. Prefix them with the server origin.";

type Rpc = {
  jsonrpc?: string;
  id?: unknown;
  method?: unknown;
  params?: unknown;
};

type ToolSpec = {
  name: string;
  description?: string;
  inputSchema: unknown;
};

const result = (req: Rpc, value: unknown) =>
  req.id === undefined ? null : { jsonrpc: "2.0", id: req.id, result: value };

const error = (req: Rpc, code: number, message: string) =>
  req.id === undefined
    ? null
    : { jsonrpc: "2.0", id: req.id ?? null, error: { code, message } };

const isObj = (v: unknown): v is Record<string, unknown> =>
  typeof v === "object" && v !== null && !Array.isArray(v);

async function jsonSchema(schema: unknown) {
  try {
    return await asSchema(schema as never).jsonSchema;
  } catch {
    return { type: "object" };
  }
}

export async function toolSpecs(): Promise<ToolSpec[]> {
  const tools = researchTools({ excludedIds: [] }, false);
  return Promise.all(
    Object.entries(tools).map(async ([name, spec]) => ({
      name,
      description:
        typeof spec.description === "string" ? spec.description : undefined,
      inputSchema: await jsonSchema(spec.inputSchema),
    })),
  );
}

async function callTool(name: string, args: Record<string, unknown>) {
  const tools = researchTools({ excludedIds: [] }, true);
  const spec = tools[name as keyof typeof tools];
  if (!spec) {
    return {
      content: [{ type: "text", text: `unknown tool '${name}'` }],
      isError: true,
    };
  }
  const parsed = await asSchema(
    spec.inputSchema as Parameters<typeof asSchema>[0],
  ).validate?.(args);
  if (parsed && !parsed.success) {
    return {
      content: [{ type: "text", text: parsed.error.message.slice(0, 400) }],
      isError: true,
    };
  }
  try {
    const out = await spec.execute(
      (parsed?.value ?? args) as never,
      {
        toolCallId: "mcp",
        messages: [],
        context: undefined,
      } as never,
    );
    const image = await imageBlock(out);
    return {
      content: [
        { type: "text", text: JSON.stringify(out) },
        ...(image ? [image] : []),
      ],
    };
  } catch (e) {
    return {
      content: [
        {
          type: "text",
          text: String(e instanceof Error ? e.message : e).slice(0, 400),
        },
      ],
      isError: true,
    };
  }
}

async function imageBlock(out: unknown) {
  if (!isObj(out) || out.visualEvidence !== "image-supplied") return null;
  const media = isObj(out.media) ? out.media : null;
  const mediaUrl = media && typeof media.url === "string" ? media.url : "";
  if (mediaUrl) {
    const file = await readLocalImage(mediaUrl);
    if (file) {
      return {
        type: "image",
        data: Buffer.from(file.data).toString("base64"),
        mimeType: file.mediaType,
      };
    }
  }
  // inspectReference reports an image without a top-level media field.
  // The screenshot is the first readable one on the reference.
  const reference = isObj(out.reference) ? out.reference : null;
  if (!reference) return null;
  const file = await readReferenceImage(reference as never);
  if (!file) return null;
  return {
    type: "image",
    data: Buffer.from(file.data).toString("base64"),
    mimeType: file.mediaType,
  };
}

async function dispatch(req: Rpc) {
  const method = req.method;
  if (typeof method !== "string") {
    return {
      jsonrpc: "2.0",
      id: req.id ?? null,
      error: { code: -32600, message: "method must be a string" },
    };
  }
  const params = req.params ?? {};
  if (!isObj(params)) return error(req, -32602, "params must be an object");
  if (method === "initialize") {
    return result(req, {
      protocolVersion:
        typeof params.protocolVersion === "string"
          ? params.protocolVersion
          : "2025-03-26",
      capabilities: { tools: { listChanged: false } },
      serverInfo: SERVER_INFO,
      instructions: INSTRUCTIONS,
    });
  }
  if (method === "ping") return result(req, {});
  if (method === "tools/list") return result(req, { tools: await toolSpecs() });
  if (method === "tools/call") {
    const name = typeof params.name === "string" ? params.name : "";
    if (!(await toolSpecs()).some((s) => s.name === name)) {
      return error(req, -32602, `unknown tool '${name}'`);
    }
    const args = params.arguments;
    if (args != null && !isObj(args)) {
      return error(req, -32602, "arguments must be an object");
    }
    return result(req, await callTool(name, args ?? {}));
  }
  if (method.startsWith("notifications/")) return null;
  return error(req, -32601, `no method '${method}'`);
}

async function handle(req: unknown) {
  if (!isObj(req)) {
    return {
      jsonrpc: "2.0",
      id: null,
      error: {
        code: -32600,
        message: "a JSON-RPC request must be an object",
      },
    };
  }
  try {
    return await dispatch(req);
  } catch (e) {
    console.error("mcp:", e);
    return error(req, -32603, "internal error");
  }
}

export async function handleBatch(raw: unknown) {
  if (Array.isArray(raw)) {
    if (!raw.length) {
      return {
        jsonrpc: "2.0",
        id: null,
        error: {
          code: -32600,
          message: "an empty batch is not a valid request",
        },
      };
    }
    if (raw.length > MCP_BATCH_LIMIT) {
      return {
        jsonrpc: "2.0",
        id: null,
        error: {
          code: -32600,
          message: `a batch may contain at most ${MCP_BATCH_LIMIT} calls`,
        },
      };
    }
    // One at a time. An image call reads and encodes a file, and a batch
    // that starts them all at once holds every reply until the last ends.
    const replies = [];
    for (const item of raw) {
      const reply = await handle(item);
      if (reply !== null) replies.push(reply);
    }
    return replies.length ? replies : null;
  }
  return handle(raw);
}
