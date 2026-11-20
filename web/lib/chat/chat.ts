// The model side of the gallery chat: provider adapters and the tool-use
// loop, ported from server/chat.py.
//
// Two wire shapes are supported, picked by the provider config's `api` field:
//
// - "anthropic": POST {base_url}/v1/messages, x-api-key + anthropic-version.
//   tools as top-level `tools`, tool_use/tool_result content blocks.
// - "openai": POST {base_url}/chat/completions, Authorization: Bearer (or the
//   config's key_header). tools as `tools` function wrappers, role:"tool"
//   replies. Covers OpenAI, xAI/Grok, Gemini's OpenAI-compatible surface and
//   self-hosted compatible endpoints.
//
// The conversation lives in one canonical turn list that each adapter
// serializes per call, so a transcript is provider-agnostic. Tool results pass
// through library.call; `view_media`'s {_image: ...} marker becomes an image
// block in whichever shape the provider takes.
import { call as callTool, SPECS } from "./library";
import "../env";
import { bareHost, PROVIDER_HOSTS_ENV, providerHostAllowed } from "./provider-hosts";

type Obj = Record<string, unknown>;

const ANTHROPIC_VERSION = "2023-06-01";
const MAX_ROUNDS = 8;
const REQUEST_TIMEOUT = 120;
const MODELS_TIMEOUT = 25;

export const SYSTEM = `You are the librarian of a private design-systems library. It holds two stores:

- systems/: the style packages captured and measured from real products. Every
  value carries an evidence label. These are the only values to design from.
- refero/: a snapshot of styles.refero.design (~1,300 styles), third-party
  interpreted data at lower confidence. Breadth for inspiration, never the
  source for a value a systems package holds.

Help the user pick a style. Rank candidates with search_styles, then read the
ones that matter: get_style for the catalogue entry, get_tokens for measured
values, read_doc for the README (which says what to distrust), list_media and
view_media when a question needs eyes (density, layout, mood) that tags cannot
answer. Compare out loud only what you actually looked at.

Answer in markdown, short paragraphs. Name each recommendation by slug and say
why it fits, not just that it matched. The page renders cards for every slug
your tools return, so a bare list adds nothing. When the user settles on one,
offer handoff_prompt. Never invent a slug; the only ones that exist come from
the tools.`;

export class ProviderError extends Error {
  // A failed provider call, surfaced to the page as the reply error.
}

export interface ProviderCfg {
  api: string;
  base_url: string;
  api_key: string;
  model: string;
  name?: string;
  key_header?: string;
  models_url?: string;
}

// The provider a chat runs on comes from lib/provider-api.ts (the server-held
// key, else ANTHROPIC_API_KEY); this module only talks to it.

function headers(cfg: ProviderCfg, keyHeader?: string): Record<string, string> {
  const hdr = keyHeader || cfg.key_header || (cfg.api === "anthropic" ? "x-api-key" : "authorization");
  const out: Record<string, string> =
    hdr === "authorization" ? { authorization: `Bearer ${cfg.api_key}` } : { [hdr]: cfg.api_key };
  if (cfg.api === "anthropic") out["anthropic-version"] = ANTHROPIC_VERSION;
  return out;
}

function isLoopback(host: string): boolean {
  const h = host.toLowerCase().replace(/^\[|\]$/g, "");
  return h === "localhost" || h.endsWith(".localhost") || h === "::1" || /^127\.\d+\.\d+\.\d+$/.test(h);
}

export function checkUrl(url: string): void {
  // https to an allowed provider host, or plain http to a listed loopback host
  // (a self-hosted model). Anything else (file:, data:, http to another host,
  // an unlisted host) is refused before a socket opens, so the endpoint cannot
  // reach internal services.
  let u: URL;
  try {
    u = new URL(url);
  } catch {
    throw new ProviderError("invalid provider URL");
  }
  if (!u.hostname) throw new ProviderError("invalid provider URL");
  if (!(u.protocol === "https:" || (u.protocol === "http:" && isLoopback(u.hostname))))
    throw new ProviderError("provider URL must be https (http only for localhost)");
  if (!providerHostAllowed(u.hostname, process.env[PROVIDER_HOSTS_ENV]))
    throw new ProviderError(`provider host ${bareHost(u.hostname)} is not allowed; add it to ${PROVIDER_HOSTS_ENV}`);
}

function sameOrigin(a: string, b: string): boolean {
  try {
    return new URL(a).origin === new URL(b).origin;
  } catch {
    return false;
  }
}

async function request(
  method: string,
  url: string,
  cfg: ProviderCfg,
  body: unknown,
  timeout: number,
  keyHeader?: string,
): Promise<Obj> {
  // Errors name the URL and status only: the upstream body is never echoed
  // back, and redirects are refused so a 3xx cannot walk the request (with its
  // key) to a host nobody checked.
  checkUrl(url);
  let resp: Response;
  try {
    resp = await fetch(url, {
      method,
      headers: { "content-type": "application/json", ...headers(cfg, keyHeader) },
      body: body === null ? undefined : JSON.stringify(body),
      redirect: "manual",
      signal: AbortSignal.timeout(timeout * 1000),
    });
  } catch {
    throw new ProviderError(`${url} unreachable`);
  }
  const text = await resp.text();
  if (resp.type === "opaqueredirect" || (resp.status >= 300 && resp.status < 400))
    throw new ProviderError(`${url} answered HTTP ${resp.status || 302} (redirects are not followed)`);
  if (!resp.ok) throw new ProviderError(`${url} answered HTTP ${resp.status}`);
  try {
    return JSON.parse(text) as Obj;
  } catch {
    throw new ProviderError(`${url} returned invalid JSON`);
  }
}

// ---------------------------------------------------------------- models list

function parseModels(resp: Obj): { id: string; label: string }[] {
  // Normalise the three list shapes: OpenAI's {data:[{id}]}, Anthropic's
  // {data:[{id,display_name}]}, Gemini's {models:[{name:'models/x',displayName}]}.
  const out: { id: string; label: string }[] = [];
  for (const m of Array.isArray(resp.data) ? resp.data : [])
    if (isObj(m) && m.id) out.push({ id: String(m.id), label: String(m.display_name || m.id) });
  for (const m of Array.isArray(resp.models) ? resp.models : [])
    if (isObj(m) && m.name) {
      const name = String(m.name);
      const id = name.split("/").slice(1).join("/") || name;
      out.push({ id, label: String(m.displayName || id) });
    }
  return out;
}

export async function listModels(cfg: ProviderCfg): Promise<{
  ok: boolean;
  models?: { id: string; label: string }[];
  note?: string;
  error?: string;
}> {
  // The provider's models, for the settings page's gated combobox. A reachable
  // host with no models endpoint still passes so the field unlocks for typing.
  const base = (cfg.base_url || "").replace(/\/+$/, "");
  const url = cfg.api === "anthropic" ? `${base}/v1/models` : cfg.models_url || `${base}/models`;
  // models_url exists for Gemini, whose list lives beside its OpenAI-compatible
  // base; it may not point anywhere base_url does not.
  if (!sameOrigin(url, base)) return { ok: false, error: "models_url must share base_url's origin" };
  let resp: Obj;
  try {
    resp = await request("GET", url, cfg, null, MODELS_TIMEOUT, cfg.key_header);
  } catch (e) {
    // Only a 404 or 405 means "the provider is real but lists no models";
    // auth failures, unreachable hosts and server errors all fail the test.
    const msg = e instanceof Error ? e.message : String(e);
    if (msg.includes("HTTP 404") || msg.includes("HTTP 405"))
      return { ok: true, models: [], note: "no model list at this endpoint; type the model name" };
    return { ok: false, error: msg };
  }
  return { ok: true, models: parseModels(resp) };
}

// ---------------------------------------------------------------- wire adapters

const isObj = (v: unknown): v is Obj => typeof v === "object" && v !== null && !Array.isArray(v);
const asArr = (v: unknown): unknown[] => (Array.isArray(v) ? v : []);

const anthropicTools = (): Obj[] =>
  SPECS.map((s) => ({ name: s.name, description: s.description, input_schema: s.parameters }));

const openaiTools = (): Obj[] =>
  SPECS.map((s) => ({
    type: "function",
    function: { name: s.name, description: s.description, parameters: s.parameters },
  }));

const imageAnthropic = (img: Obj): Obj[] => [
  { type: "text", text: JSON.stringify({ url: img.url, name: img.name }) },
  { type: "image", source: { type: "base64", media_type: img.media_type, data: img.data } },
];

const imageOpenai = (img: Obj): Obj[] => [
  { type: "text", text: JSON.stringify({ url: img.url, name: img.name }) },
  { type: "image_url", image_url: { url: `data:${img.media_type};base64,${img.data}` } },
];

interface ToolCallRec {
  id: string;
  name: string;
  args: Obj;
}

// One canonical turn list; each adapter serializes it per call.
type Turn =
  | { role: "user"; text: string }
  | { role: "assistant"; text: string | null; calls: ToolCallRec[] }
  | { role: "tool"; id: string; result: Obj };

function anthropicMessages(turns: Turn[]): Obj[] {
  // Canonical turns -> Anthropic messages. Consecutive tool results merge
  // into one user message, as the API requires.
  const out: Obj[] = [];
  for (const t of turns) {
    if (t.role === "user") {
      out.push({ role: "user", content: [{ type: "text", text: t.text }] });
    } else if (t.role === "assistant") {
      const content: Obj[] = t.text ? [{ type: "text", text: t.text }] : [];
      for (const c of t.calls) content.push({ type: "tool_use", id: c.id, name: c.name, input: c.args });
      out.push({ role: "assistant", content });
    } else {
      const content = "_image" in t.result ? imageAnthropic(t.result._image as Obj) : [{ type: "text", text: JSON.stringify(t.result) }];
      const block = { type: "tool_result", tool_use_id: t.id, content };
      const last = out[out.length - 1];
      const lastContent = last ? (last.content as Obj[] | undefined) : undefined;
      if (last?.role === "user" && Array.isArray(lastContent) && lastContent.length && isObj(lastContent[0]) && lastContent[0].type === "tool_result")
        lastContent.push(block);
      else out.push({ role: "user", content: [block] });
    }
  }
  return out;
}

function openaiMessages(turns: Turn[]): Obj[] {
  const out: Obj[] = [{ role: "system", content: SYSTEM }];
  let pendingImages: Obj[] = [];
  for (let i = 0; i < turns.length; i++) {
    const t = turns[i];
    if (t.role === "user") {
      out.push({ role: "user", content: t.text });
    } else if (t.role === "assistant") {
      const msg: Obj = { role: "assistant", content: t.text || null };
      if (t.calls.length)
        msg.tool_calls = t.calls.map((c) => ({
          id: c.id,
          type: "function",
          function: { name: c.name, arguments: JSON.stringify(c.args) },
        }));
      out.push(msg);
    } else {
      let content: string;
      if ("_image" in t.result) {
        const img = t.result._image as Obj;
        // OpenAI tool messages take text parts only; the image rides in a
        // user message right after the run of tool replies it belongs to.
        content = JSON.stringify({ url: img.url, name: img.name, note: "image follows as a user message" });
        pendingImages.push(img);
      } else {
        content = JSON.stringify(t.result);
      }
      out.push({ role: "tool", tool_call_id: t.id, content });
      if (pendingImages.length && (i + 1 >= turns.length || turns[i + 1].role !== "tool")) {
        out.push({ role: "user", content: pendingImages.flatMap(imageOpenai) });
        pendingImages = [];
      }
    }
  }
  return out;
}

async function complete(cfg: ProviderCfg, turns: Turn[]): Promise<{ text: string | null; calls: ToolCallRec[] }> {
  // One provider call -> {text, calls:[{id,name,args}]}.
  if (cfg.api === "anthropic") {
    const resp = await request(
      "POST",
      `${cfg.base_url}/v1/messages`,
      cfg,
      { model: cfg.model, max_tokens: 2048, system: SYSTEM, tools: anthropicTools(), messages: anthropicMessages(turns) },
      REQUEST_TIMEOUT,
    );
    const blocks = asArr(resp.content).filter(isObj);
    const text = blocks
      .filter((b) => b.type === "text")
      .map((b) => String(b.text ?? ""))
      .join("");
    const calls = blocks
      .filter((b) => b.type === "tool_use")
      .map((b) => ({ id: String(b.id), name: String(b.name), args: isObj(b.input) ? b.input : {} }));
    return { text: text.trim() || null, calls };
  }
  const resp = await request(
    "POST",
    `${cfg.base_url}/chat/completions`,
    cfg,
    { model: cfg.model, messages: openaiMessages(turns), tools: openaiTools(), tool_choice: "auto" },
    REQUEST_TIMEOUT,
  );
  const choice = asArr(resp.choices)[0];
  const msg = isObj(choice) && isObj(choice.message) ? choice.message : {};
  const calls = asArr(msg.tool_calls).map((c, i) => {
    const o = isObj(c) ? c : {};
    const fn = isObj(o.function) ? o.function : {};
    return { id: o.id ? String(o.id) : `call_${i}`, name: String(fn.name), args: jsonArgs(fn.arguments) };
  });
  return { text: (msg.content ? String(msg.content) : "").trim() || null, calls };
}

function jsonArgs(raw: unknown): Obj {
  try {
    const out = JSON.parse(typeof raw === "string" && raw ? raw : "{}");
    return isObj(out) ? out : {};
  } catch {
    return {};
  }
}

// ---------------------------------------------------------------- the loop

export interface ChatResult {
  reply: string;
  error?: string;
  results: Obj[];
  media: Obj[];
  calls: string[];
}

const setdef = (m: Map<string, Obj>, k: string, v: Obj) => {
  if (!m.has(k)) m.set(k, v);
};

export async function runChat(messages: { role: string; content: string }[], provider: ProviderCfg): Promise<ChatResult> {
  // Drive the tool loop for one page-side conversation. Returns the reply
  // plus the artifacts the page renders: result slugs and media URLs.
  const turns: Turn[] = [];
  for (const m of messages.slice(-24)) {
    if ((m.role === "user" || m.role === "assistant") && m.content) {
      const text = String(m.content).slice(0, 8000);
      turns.push(m.role === "user" ? { role: "user", text } : { role: "assistant", text, calls: [] });
    }
  }
  if (!turns.length || turns[turns.length - 1].role !== "user") turns.push({ role: "user", text: "Help me pick a design style." });

  const results = new Map<string, Obj>();
  const media = new Map<string, Obj>();
  const callsLog: string[] = [];
  for (let round = 0; round < MAX_ROUNDS; round++) {
    const step = await complete(provider, turns);
    if (!step.calls.length) {
      if (step.text) turns.push({ role: "assistant", text: step.text, calls: [] });
      return { reply: step.text ?? "", results: [...results.values()], media: [...media.values()], calls: callsLog };
    }
    turns.push({ role: "assistant", text: step.text, calls: step.calls });
    for (const c of step.calls) {
      callsLog.push(c.name);
      let result: Obj;
      try {
        result = await callTool(c.name, c.args);
      } catch (e) {
        result = { error: (e instanceof Error ? e.message : String(e)).slice(0, 400) };
      }
      collect(c.name, c.args, result, results, media);
      turns.push({ role: "tool", id: c.id, result });
    }
  }
  return {
    reply: "",
    error: `stopped after ${MAX_ROUNDS} tool rounds`,
    results: [...results.values()],
    media: [...media.values()],
    calls: callsLog,
  };
}

function collect(name: string, args: Obj, result: unknown, results: Map<string, Obj>, media: Map<string, Obj>): void {
  // Pull page-renderable artifacts out of a tool result. Error payloads are
  // skipped so a failed call never turns the whole turn into a 500.
  if (!isObj(result) || "error" in result) return;
  if (name === "search_styles") {
    for (const h of asArr(result.hits))
      if (isObj(h)) setdef(results, `${h.store}:${h.slug}`, { store: h.store, slug: h.slug, name: h.name });
  } else if (name === "get_style") {
    setdef(results, `${result.store ?? "systems"}:${result.slug}`, {
      store: result.store ?? "systems",
      slug: result.slug,
      name: result.name,
    });
  } else if (name === "list_media") {
    for (const i of asArr(result.items))
      if (isObj(i)) setdef(media, String(i.url), { url: i.url, name: `${result.slug}/${i.name}` });
  } else if (name === "view_media" && "_image" in result) {
    const img = result._image as Obj;
    setdef(media, String(img.url), { url: img.url, name: img.name });
  } else if (name === "handoff_prompt" && result.prompt) {
    setdef(results, `prompt:${result.slug}`, {
      store: "prompt",
      slug: result.slug,
      name: "Agent prompt",
      prompt: result.prompt,
    });
  }
}
