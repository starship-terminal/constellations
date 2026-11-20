"use client";

// Readers for the browser-saved values more than one component needs.
// Every read tolerates a missing, blocked or malformed localStorage.
const readJSON = (key: string): unknown => {
  try {
    return JSON.parse(localStorage.getItem(key) || "null");
  } catch {
    return null;
  }
};

/** The model provider an older version of the app saved in this browser
    ("ds-provider"), or null. Only string fields are kept (a number or boolean
    becomes its text): a hand edit or an older schema can leave `{"model": 1}`
    or `null` there. Read only by migrateStoredProvider, which moves it to the
    server and deletes it; nothing writes it any more. */
export const readStoredProvider = (): Record<string, string> | null => {
  const p = readJSON("ds-provider");
  if (!p || typeof p !== "object" || Array.isArray(p)) return null;
  const out: Record<string, string> = {};
  for (const [k, v] of Object.entries(p)) {
    if (typeof v === "string") out[k] = v;
    else if (typeof v === "number" || typeof v === "boolean") out[k] = String(v);
  }
  return out;
};

export const LEGACY_PROVIDER_KEY = "ds-provider";
/** sessionStorage: the migration's notice, for Settings to repeat. No key in it. */
export const PROVIDER_NOTICE_KEY = "ds-provider-notice";

export interface SaveReply {
  ok: boolean;
  /** The server already had a saved provider and kept it. */
  existing?: boolean;
  /** The server answered and decided: a JSON reply with a status below 500
      (a save, a kept provider, a refused body or a failed key test). False
      for a 5xx, a reply that is not JSON or no answer at all, when the
      browser copy is the only copy and must stay. */
  definite?: boolean;
  error?: string;
}

/** Read POST /api/provider's answer: `json` is the parsed body, or null when
    it was not JSON. Only a JSON answer below 500 is the server's decision; a
    proxy's 502 page or a busy store's 500 is not. */
export function saveReplyOf(status: number, json: unknown): SaveReply {
  const d = json !== null && typeof json === "object" ? (json as Record<string, unknown>) : null;
  return {
    ok: !!d?.ok,
    existing: d?.existing === true,
    definite: d !== null && status < 500,
    error: typeof d?.error === "string" ? d.error : status >= 200 && status < 300 ? undefined : `HTTP ${status}`,
  };
}

let inflight: Promise<string | null> | null = null;

/** Move a key an older version left in localStorage to the server, once.
    `save` posts the provider to POST /api/provider with `migrate: true`, which
    the server only saves when it has no provider yet, so an old browser never
    replaces a newer key. The browser copy is deleted once the server has
    decided (it saved the key, kept its own, refused the body or failed the
    key's test) and kept when the server did not answer, answered 5xx or
    answered with something that is not JSON, so a restarting API never
    costs the only copy; a later page load tries again. The returned message
    says which happened; null when there was nothing to move. A leftover value without a key is deleted
    silently. Calls in one page share one run (React runs a mount effect
    twice in development), and tabs take turns through a Web Lock where the
    browser has one, each reading localStorage again once it holds it. */
export function migrateStoredProvider(save: (body: Record<string, string | boolean>) => Promise<SaveReply>): Promise<string | null> {
  if (inflight) return inflight;
  const run = () => migrateOnce(save);
  const locks = typeof navigator !== "undefined" ? (navigator as Navigator & { locks?: LockManager }).locks : undefined;
  const p: Promise<string | null> = (locks ? (locks.request("ds-provider-migration", run) as unknown as Promise<string | null>) : run()).finally(
    () => {
      inflight = null;
    },
  );
  inflight = p;
  return p;
}

async function migrateOnce(save: (body: Record<string, string | boolean>) => Promise<SaveReply>): Promise<string | null> {
  let raw: string | null = null;
  try {
    raw = localStorage.getItem(LEGACY_PROVIDER_KEY);
  } catch {
    return null;
  }
  if (raw === null) return null;
  const p = readStoredProvider();
  const drop = () => {
    try {
      localStorage.removeItem(LEGACY_PROVIDER_KEY);
    } catch {}
  };
  if (!p || !p.api_key) {
    drop();
    return null;
  }
  const key = p.api_key;
  const body: Record<string, string | boolean> = { migrate: true };
  for (const k of ["api", "base_url", "key_header", "models_url", "model", "name"]) if (p[k]) body[k] = p[k];
  body.api_key = key;
  let reply: SaveReply;
  try {
    reply = await save(body);
  } catch {
    reply = { ok: false, definite: false };
  }
  if (!reply.ok && !reply.existing && !reply.definite)
    return "The server did not answer, so the API key this browser had saved stays here for now. It moves to the server on a later visit.";
  drop();
  if (reply.ok) return "Moved the API key this browser had saved to the server. This browser no longer stores it.";
  if (reply.existing)
    return "Deleted the API key this browser had saved. The server already has, or had, its own saved key, so it kept its own setting.";
  const why = (reply.error || "it did not say why").split(key).join("[redacted]");
  return `Deleted the API key this browser had saved. The server did not keep it (${why}), so enter it again in Settings > Model provider.`;
}

/** Saved media paths ("ds-saved"). */
export const readSavedPaths = (): string[] => {
  const v = readJSON("ds-saved");
  return Array.isArray(v) ? v.filter((x): x is string => typeof x === "string") : [];
};

export const writeSavedPaths = (paths: Iterable<string>) => {
  try {
    localStorage.setItem("ds-saved", JSON.stringify([...paths]));
  } catch {}
};
