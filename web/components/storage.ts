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
  error?: string;
}

/** Move a key an older version left in localStorage to the server, once.
    `save` posts the provider to POST /api/provider. The browser copy is
    deleted whether or not the server kept it, and the returned message says
    which happened; null when there was nothing to move. A leftover value
    without a key is deleted silently. */
export async function migrateStoredProvider(save: (body: Record<string, string>) => Promise<SaveReply>): Promise<string | null> {
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
  const body: Record<string, string> = {};
  for (const k of ["api", "base_url", "key_header", "models_url", "model", "name"]) if (p[k]) body[k] = p[k];
  body.api_key = key;
  let reply: SaveReply;
  try {
    reply = await save(body);
  } catch {
    reply = { ok: false, error: "no answer from the server" };
  } finally {
    drop();
  }
  if (reply.ok) return "Moved the API key this browser had saved to the server. This browser no longer stores it.";
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
