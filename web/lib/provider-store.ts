// The chat's model provider, held server-side. The browser submits a key
// once (Settings > Model provider); the server tests it, writes it here and
// never sends it back. server/provider_store.py reads and writes the same file
// with the same rules, so the gallery and the home server's Python /api/
// share one saved provider.
//
// Where: $DESIGN_SYSTEMS_CONFIG_DIR/provider.json, default
// ~/.config/design-systems/provider.json. Outside the checkout, so no key
// can be committed; tests point the variable at a throwaway folder. The
// folder is created 0700 and the file is written 0600, through a temporary
// file and a rename, so a reader never sees half a key and a rotation swaps
// the old key for the new one in one step.
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";

export const CONFIG_DIR_ENV = "DESIGN_SYSTEMS_CONFIG_DIR";
export const FILE_NAME = "provider.json";

/** The provider fields that are safe to show: everything but the key. */
export const PUBLIC_FIELDS = ["api", "base_url", "key_header", "models_url", "model", "name"] as const;
/** The fields that say where the key is sent. A saved key only ever goes to
    the endpoint it was saved with; changing any of these needs the key again. */
export const ENDPOINT_FIELDS = ["api", "base_url", "key_header", "models_url"] as const;

export type PublicProvider = Partial<Record<(typeof PUBLIC_FIELDS)[number], string>>;
export type SavedProvider = PublicProvider & { api: string; base_url: string; model: string; api_key: string };

export class StoreError extends Error {
  // The saved file exists but cannot be used. Never carries the file's text.
}

export function configDir(): string {
  const dir = process.env[CONFIG_DIR_ENV];
  return path.resolve(dir && dir.trim() ? dir : path.join(os.homedir(), ".config", "design-systems"));
}

export const providerFile = (): string => path.join(configDir(), FILE_NAME);

const isObj = (v: unknown): v is Record<string, unknown> => typeof v === "object" && v !== null && !Array.isArray(v);

/** The saved provider, or null when none is saved. Throws StoreError when the
    file is there but unreadable or malformed: that is a broken saved key, and
    the env key must not quietly stand in for it. */
export async function loadSaved(): Promise<SavedProvider | null> {
  let text: string;
  try {
    text = await fs.readFile(providerFile(), "utf8");
  } catch (e) {
    if ((e as NodeJS.ErrnoException).code === "ENOENT") return null;
    throw new StoreError("The saved provider file cannot be read.");
  }
  let raw: unknown;
  try {
    raw = JSON.parse(text);
  } catch {
    throw new StoreError("The saved provider file is not valid JSON.");
  }
  if (!isObj(raw)) throw new StoreError("The saved provider file is not an object.");
  const out: Record<string, string> = {};
  for (const k of [...PUBLIC_FIELDS, "api_key"]) if (typeof raw[k] === "string" && raw[k]) out[k] = raw[k] as string;
  if (!out.api_key || !out.api || !out.base_url || !out.model)
    throw new StoreError("The saved provider file is missing its key, endpoint or model.");
  return out as SavedProvider;
}

/** Write the provider (key included) in one atomic step, mode 0600. */
export async function writeSaved(cfg: SavedProvider): Promise<void> {
  const dir = configDir();
  await fs.mkdir(dir, { recursive: true, mode: 0o700 });
  const out: Record<string, string> = {};
  for (const k of [...PUBLIC_FIELDS, "api_key"] as const) {
    const v = cfg[k];
    if (typeof v === "string" && v) out[k] = v;
  }
  const tmp = path.join(dir, `.${FILE_NAME}.${process.pid}.${Date.now()}.${Math.random().toString(36).slice(2)}.tmp`);
  const fh = await fs.open(tmp, "wx", 0o600);
  try {
    await fh.writeFile(JSON.stringify(out, null, 2) + "\n");
    await fh.sync();
  } finally {
    await fh.close();
  }
  try {
    // A umask cannot widen 0600, but an existing file's mode is not ours to trust.
    await fs.chmod(tmp, 0o600);
    await fs.rename(tmp, providerFile());
  } catch (e) {
    await fs.rm(tmp, { force: true });
    throw e;
  }
}

/** Delete the saved provider. True when there was one. */
export async function removeSaved(): Promise<boolean> {
  try {
    await fs.unlink(providerFile());
    return true;
  } catch (e) {
    if ((e as NodeJS.ErrnoException).code === "ENOENT") return false;
    throw new StoreError("The saved provider file cannot be removed.");
  }
}

/** The fields of a provider that may leave the server. */
export function publicView(cfg: PublicProvider | null | undefined): PublicProvider | null {
  if (!cfg) return null;
  const out: PublicProvider = {};
  for (const k of PUBLIC_FIELDS) if (typeof cfg[k] === "string" && cfg[k]) out[k] = cfg[k];
  return out;
}

/** `text` with every occurrence of each key replaced. Provider errors name a
    URL, and a URL or an upstream message can echo the key back. */
export function redact(text: string, ...keys: (string | undefined | null)[]): string {
  let out = text;
  for (const k of keys) if (k && k.length >= 4) out = out.split(k).join("[redacted]");
  return out;
}
