// The JSON-RPC handler behind POST /api/mcp. The tools are the same ones
// the research chat uses, with no pinned or excluded references. One bad
// call comes back as a tool error so the client's session keeps going.
import { asSchema } from "ai";
import { researchTools } from "@/server/research/agent";

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

// The tool set never changes while the server runs, so its JSON schemas are
// built once rather than on every tools/list and tools/call.
let specs: Promise<ToolSpec[]> | undefined;
export function toolSpecs(): Promise<ToolSpec[]> {
  specs ??= Promise.all(
    Object.entries(researchTools({ excludedIds: [] }, false)).map(
      async ([name, spec]) => ({
        name,
        description:
          typeof spec.description === "string" ? spec.description : undefined,
        inputSchema: await jsonSchema(spec.inputSchema),
      }),
    ),
  );
  return specs;
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
    const input = parsed?.value ?? args;
    const out = await spec.execute(
      input as never,
      {
        toolCallId: "mcp",
        messages: [],
        context: undefined,
      } as never,
    );
    const image = await imageBlock(spec, input, out);
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

// The image comes from the tool's own model output, which reuses the file
// execute() already read and encoded to decide visualEvidence.
async function imageBlock(
  spec: { toModelOutput?: unknown },
  input: unknown,
  out: unknown,
) {
  if (!isObj(out) || out.visualEvidence !== "image-supplied") return null;
  if (typeof spec.toModelOutput !== "function") return null;
  const model = (await spec.toModelOutput({
    toolCallId: "mcp",
    input,
    output: out,
  })) as { type?: string; value?: unknown };
  if (model?.type !== "content" || !Array.isArray(model.value)) return null;
  for (const part of model.value) {
    if (
      isObj(part) &&
      part.type === "file" &&
      isObj(part.data) &&
      part.data.type === "data" &&
      typeof part.data.data === "string" &&
      typeof part.mediaType === "string"
    )
      return { type: "image", data: part.data.data, mimeType: part.mediaType };
  }
  return null;
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
