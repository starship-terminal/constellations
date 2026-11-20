// The provider routes' logic, kept free of next/server so the node test
// runner can load it (the route files under app/api/ are thin wrappers).
// server/routes.py answers the same routes with the same rules for the home
// server's Python /api/.
//
//   GET    /api/provider       -> state: where the key comes from, never the key
//   POST   /api/provider       {api, base_url, key_header?, models_url?, model,
//                               name?, api_key?} -> tests a new key, then saves
//   DELETE /api/provider       -> removes the saved provider
//   POST   /api/provider/test  same fields, api_key optional -> {ok, models}
//
// The rules (the owner's stack conventions):
// - A key reaches the server once, is tested with one cheap call (the model
//   list), and only a key that passes is saved. Rotation is the same call: the
//   old key keeps working until the new one passes, then one write swaps them.
// - No response carries a key. State says only where the key comes from:
//   "saved", "env" or "none".
// - Precedence: the saved key, then ANTHROPIC_API_KEY from the environment
//   only while nothing is saved, then nothing (the page asks for setup). A
//   saved key that fails, or a saved file that is broken, is reported as such
//   and never quietly replaced by the env key.
// - A saved key only goes to the endpoint it was saved with. Changing the
//   API, base URL, key header or models URL needs the key again, so nobody
//   can point the saved key at a host of their choosing.
// - Every error text is passed through redact() with the keys in play.
import { baseUrlOf } from "./provider-defaults.ts";
import {
  ENDPOINT_FIELDS,
  loadSaved,
  publicView,
  redact,
  removeSaved,
  saveProvider,
  StoreError,
  updateModel,
  type PublicProvider,
  type SavedProvider,
} from "./provider-store.ts";

export type KeySource = "saved" | "env" | "none";

export interface ModelsResult {
  ok: boolean;
  /** The provider accepted the key: it answered the model list. An endpoint
      with no model list (404 or 405) is `ok` so a model name can be typed,
      but the key was never checked, so `verified` is false. */
  verified?: boolean;
  models?: { id: string; label: string }[];
  note?: string;
  error?: string;
}

/** chat.ts's listModels, injected so tests need no network. */
export type ListModels = (cfg: SavedProvider) => Promise<ModelsResult>;

export interface ApiResult {
  status: number;
  body: Record<string, unknown>;
}

export interface ProviderState {
  source: KeySource;
  /** True when the chat can run: a usable saved key, or the env key. */
  configured: boolean;
  /** The non-secret fields of the provider in use. */
  provider: PublicProvider | null;
  /** Whether ANTHROPIC_API_KEY is set, whatever the source. */
  envAvailable: boolean;
  /** Why the saved provider cannot be used. */
  error?: string;
}

export const ENV_DEFAULT_MODEL = "claude-sonnet-4-5";
const MAX_KEY = 1024;

/** The env provider: ANTHROPIC_API_KEY to Anthropic's own API, nowhere else. */
export function envProvider(): SavedProvider | null {
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return null;
  return {
    api: "anthropic",
    base_url: "https://api.anthropic.com",
    api_key: key,
    model: process.env.DS_CHAT_MODEL || ENV_DEFAULT_MODEL,
    name: "env ANTHROPIC_API_KEY",
  };
}

export async function providerState(): Promise<ProviderState> {
  const env = envProvider();
  const envAvailable = !!env;
  try {
    const saved = await loadSaved();
    if (saved) return { source: "saved", configured: true, provider: publicView(saved), envAvailable };
  } catch (e) {
    if (!(e instanceof StoreError)) throw e;
    return { source: "saved", configured: false, provider: null, envAvailable, error: e.message };
  }
  if (env) return { source: "env", configured: true, provider: publicView(env), envAvailable };
  return { source: "none", configured: false, provider: null, envAvailable };
}

/** The provider the chat runs on, by precedence, or why there is none. */
export async function resolveProvider(): Promise<{ cfg: SavedProvider | null; source: KeySource; error?: string }> {
  try {
    const saved = await loadSaved();
    if (saved) return { cfg: saved, source: "saved" };
  } catch (e) {
    if (!(e instanceof StoreError)) throw e;
    return { cfg: null, source: "saved", error: e.message };
  }
  const env = envProvider();
  return env ? { cfg: env, source: "env" } : { cfg: null, source: "none" };
}

// ---------------------------------------------------------------- input

interface Submitted {
  /** A one-time move of a key an older page kept in the browser: saved only
      when nothing is saved yet, never replacing the server's provider. */
  migrate: boolean;
  api: string;
  base_url: string;
  key_header: string;
  models_url: string;
  model: string;
  name: string;
  api_key: string;
}

class BadRequest extends Error {}

const FIELDS = ["api", "base_url", "key_header", "models_url", "model", "name", "api_key"] as const;

const URL_KEY = "Put the API key in the API key field only, not in the base URL, models URL, label or model.";

/** Whether `value` holds `key`, as typed or percent-encoded. */
function carriesText(value: string, key: string): boolean {
  if (!value || key.length < 4) return false;
  let decoded = value;
  try {
    decoded = decodeURIComponent(value);
  } catch {}
  return value.includes(key) || decoded.includes(key) || value.includes(encodeURIComponent(key));
}

/** Validate and normalise a posted provider object. Throws BadRequest with a
    message that never quotes the submitted values. */
function parse(body: unknown): Submitted {
  if (typeof body !== "object" || body === null || Array.isArray(body)) throw new BadRequest("Send a JSON object.");
  const b = body as Record<string, unknown>;
  if (b.migrate !== undefined && typeof b.migrate !== "boolean") throw new BadRequest("migrate must be true or false.");
  const s: Record<string, string> = {};
  for (const k of FIELDS) {
    const v = b[k];
    if (v === undefined || v === null) s[k] = "";
    else if (typeof v === "string") s[k] = v.trim();
    else throw new BadRequest("Provider fields must be strings.");
  }
  const api = s.api || "openai";
  if (api !== "anthropic" && api !== "openai") throw new BadRequest("API must be anthropic or openai.");
  if (s.api_key.length > MAX_KEY || /[\s\u0000-\u001f\u007f]/.test(s.api_key))
    throw new BadRequest("That API key has characters a key cannot hold.");
  if (s.key_header && !/^[A-Za-z0-9-]{1,64}$/.test(s.key_header)) throw new BadRequest("Key header must be a header name.");
  if (s.model.length > 160 || s.name.length > 80) throw new BadRequest("Model or label is too long.");
  // The URLs are shown back on the page; a key inside one would be too.
  if (s.api_key && [s.base_url, s.models_url, s.name, s.model].some((v) => carriesText(v, s.api_key)))
    throw new BadRequest(URL_KEY);
  return {
    migrate: b.migrate === true,
    api,
    base_url: baseUrlOf({ api, base_url: s.base_url }).replace(/\/+$/, ""),
    key_header: s.key_header.toLowerCase(),
    models_url: s.models_url.replace(/\/+$/, ""),
    model: s.model,
    name: s.name,
    api_key: s.api_key,
  };
}

/** The header a provider sends its key in when none is named: chat.ts's rule. */
const defaultHeader = (api: string) => (api === "anthropic" ? "x-api-key" : "authorization");

/** Where a key goes, normalised: a blank key header is its API's default, so
    a provider saved without one matches the same endpoint named explicitly. */
const endpointOf = (p: PublicProvider): string => {
  const api = (p.api ?? "").trim() || "openai";
  return JSON.stringify(
    ENDPOINT_FIELDS.map((k) => {
      const v = (p[k] ?? "").trim();
      if (k === "api") return api;
      if (k === "key_header") return (v || defaultHeader(api)).toLowerCase();
      return v.replace(/\/+$/, "");
    }),
  );
};

const sameEndpoint = (a: PublicProvider, b: PublicProvider) => endpointOf(a) === endpointOf(b);

const toCfg = (s: Submitted, api_key: string): SavedProvider => {
  const out: SavedProvider = { api: s.api, base_url: s.base_url, model: s.model, api_key };
  if (s.key_header) out.key_header = s.key_header;
  if (s.models_url) out.models_url = s.models_url;
  if (s.name) out.name = s.name;
  return out;
};

async function test(cfg: SavedProvider, listModels: ListModels): Promise<ModelsResult> {
  let r: ModelsResult;
  try {
    r = await listModels(cfg);
  } catch (e) {
    r = { ok: false, error: e instanceof Error ? e.message : "Test failed." };
  }
  const out: ModelsResult = { ok: !!r.ok, verified: !!r.ok && !r.note };
  if (Array.isArray(r.models)) out.models = r.models;
  if (r.note) out.note = redact(String(r.note), cfg.api_key);
  if (r.error) out.error = redact(String(r.error), cfg.api_key);
  return out;
}

/** A handler wrapper: bad input is a 400, a broken store a 500 with its own
    safe message, anything else a generic 500. Nothing is logged but the
    error's type, so no key can reach the server log. */
async function guarded(fn: () => Promise<ApiResult>): Promise<ApiResult> {
  try {
    return await fn();
  } catch (e) {
    if (e instanceof BadRequest) return { status: 400, body: { ok: false, error: e.message } };
    if (e instanceof StoreError) return { status: 500, body: { ok: false, error: e.message } };
    console.error(`provider route failed: ${e instanceof Error ? e.name : typeof e}`);
    return { status: 500, body: { ok: false, error: "internal error" } };
  }
}

// ---------------------------------------------------------------- handlers

export const handleGet = (): Promise<ApiResult> =>
  guarded(async () => ({ status: 200, body: { ok: true, ...(await providerState()) } }));

/** Test a key against an endpoint. With no key in the body, test the key
    already held (saved, else env), and only against the endpoint it is held for. */
export const handleTest = (body: unknown, listModels: ListModels): Promise<ApiResult> =>
  guarded(async () => {
    const s = parse(body);
    if (s.api_key) return { status: 200, body: { ...(await test(toCfg(s, s.api_key), listModels)) } };
    const held = await resolveProvider();
    if (held.error) return { status: 200, body: { ok: false, error: held.error } };
    if (!held.cfg) return { status: 400, body: { ok: false, error: "Enter an API key to test." } };
    if (!sameEndpoint(held.cfg, s))
      return { status: 400, body: { ok: false, error: "The held key only goes to its own endpoint; enter a key for this one." } };
    return { status: 200, body: { ...(await test({ ...held.cfg, model: s.model || held.cfg.model }, listModels)) } };
  });

const EXISTING = "The server already has a saved provider, so it kept that one.";
const UNCHECKED =
  "This endpoint has no model list, so the new key could not be checked and the saved key was kept. Remove the saved key first to save this one unchecked.";

/** Save the provider. A new key is tested first and saved only when the test
    passes; with no key, only the model and label of the saved provider change.
    Each write is one statement in the store, atomic across both servers. */
export const handleSave = (body: unknown, listModels: ListModels): Promise<ApiResult> =>
  guarded(async () => {
    const s = parse(body);
    if (!s.model) return { status: 400, body: { ok: false, error: "Pick a model before saving." } };
    if (s.api_key) {
      const cfg = toCfg(s, s.api_key);
      // A migration that cannot be saved is not worth a provider call.
      if (s.migrate && (await loadSaved().catch(() => null)))
        return { status: 200, body: { ok: false, saved: false, existing: true, error: EXISTING } };
      const r = await test(cfg, listModels);
      if (!r.ok) return { status: 200, body: { ...r, ok: false, saved: false } };
      // One statement decides and writes, so a concurrent save or removal on
      // either server cannot slip in between: a migration only fills an empty
      // slot, and a key the provider could not check only replaces itself.
      const written = await saveProvider(cfg, s.migrate ? "create" : r.verified ? "replace" : "same-key");
      if (!written && s.migrate)
        return { status: 200, body: { ok: false, saved: false, existing: true, error: EXISTING } };
      if (!written) return { status: 200, body: { ok: false, saved: false, error: UNCHECKED } };
      return {
        status: 200,
        body: { ok: true, saved: true, verified: !!r.verified, models: r.models ?? [], ...(await providerState()) },
      };
    }
    if (s.migrate) return { status: 400, body: { ok: false, error: "Nothing to move: no key was sent." } };
    let saved: SavedProvider | null;
    try {
      saved = await loadSaved();
    } catch (e) {
      if (e instanceof StoreError) return { status: 400, body: { ok: false, error: `${e.message} Remove it and save a key again.` } };
      throw e;
    }
    if (!saved) return { status: 400, body: { ok: false, error: "Enter an API key to save." } };
    if (!sameEndpoint(saved, s))
      return { status: 400, body: { ok: false, error: "Changing the endpoint needs the API key again." } };
    // Applies only while the row still holds the key and endpoint just read,
    // so it can never write back a key another request removed or replaced.
    if (!(await updateModel(saved, s.model, s.name)))
      return { status: 409, body: { ok: false, error: "The saved provider changed meanwhile; reload and try again." } };
    return { status: 200, body: { ok: true, saved: true, ...(await providerState()) } };
  });

export const handleRemove = (): Promise<ApiResult> =>
  guarded(async () => {
    const removed = await removeSaved();
    return { status: 200, body: { ok: true, removed, ...(await providerState()) } };
  });

/** Whether a posted chat body still carries a key (an older page): refused,
    so a key never rides along with every message again. */
export const carriesKey = (body: unknown): boolean => {
  if (typeof body !== "object" || body === null) return false;
  const p = (body as Record<string, unknown>).provider;
  return typeof p === "object" && p !== null && "api_key" in p && !!(p as Record<string, unknown>).api_key;
};

export { redact };
