import { z } from "zod";
import { createOpenAI } from "@ai-sdk/openai";
import { createAnthropic } from "@ai-sdk/anthropic";
import { HttpError } from "./http";
import { getStore } from "@/server/db";
import type { ProviderSettings } from "@/contracts/research";
// Where a URL may point at all: HTTP(S), no credentials, query or fragment.
const endpointURL = z
  .string()
  .url()
  .refine((value) => {
    const u = new URL(value);
    return (
      ["http:", "https:"].includes(u.protocol) &&
      !u.username &&
      !u.password &&
      !u.search &&
      !u.hash
    );
  }, "Use an HTTP(S) URL without credentials, query or fragment.");
const LOOPBACK_HOSTS = new Set(["localhost", "127.0.0.1", "[::1]"]);
// A key sent over plain HTTP is readable on the network, so a submitted
// endpoint must be HTTPS unless it stays on this machine.
export const submittedBaseURL = endpointURL
  .refine((value) => {
    const u = new URL(value);
    return u.protocol === "https:" || LOOPBACK_HOSTS.has(u.hostname);
  }, "Use HTTPS, or plain HTTP only for localhost, 127.0.0.1 or [::1].")
  .nullable()
  .optional();
function settingsSchema(baseURL: typeof submittedBaseURL) {
  return z
    .object({
      provider: z.enum(["openai", "anthropic"]).optional(),
      model: z.string().trim().min(1).max(160).optional(),
      baseURL,
      // Per-provider keys saved through Settings. A string sets the key, null
      // clears it, an absent entry keeps it. Keys stay server-side:
      // readSettings only reports where each credential comes from.
      apiKeys: z
        .object({
          openai: z.string().trim().min(1).max(320).nullable().optional(),
          anthropic: z.string().trim().min(1).max(320).nullable().optional(),
        })
        .strict()
        .optional(),
    })
    .strict();
}
// What a request may submit.
export const settingsPatch = settingsSchema(submittedBaseURL);
// What may already be stored or set in the environment. Rows saved before the
// HTTPS rule must keep loading, so only the shape is checked here.
export const storedSettings = settingsSchema(endpointURL.nullable().optional());
type Provider = "openai" | "anthropic";
type Stored = z.infer<typeof storedSettings>;
export const OFFICIAL_BASE_URL = {
  openai: "https://api.openai.com/v1",
  anthropic: "https://api.anthropic.com/v1",
} as const;
function resolveProvider(saved: Stored): Provider {
  return (
    saved.provider ??
    (process.env.DESIGN_RESEARCH_PROVIDER === "anthropic"
      ? "anthropic"
      : "openai")
  );
}
// The endpoint a saved row resolves to: the saved one, else the environment's,
// else null for the provider's own API.
function resolveBaseURL(saved: Stored, provider: Provider): string | null {
  return saved.baseURL !== undefined
    ? saved.baseURL
    : (process.env.DESIGN_RESEARCH_BASE_URL ??
        (provider === "openai"
          ? process.env.OPENAI_BASE_URL
          : process.env.ANTHROPIC_BASE_URL) ??
        null);
}
function originOf(url: string) {
  try {
    return new URL(url).origin;
  } catch {
    return null;
  }
}
// A saved or environment key may go to the provider's own API or to the
// endpoint the owner already saved, and nowhere else. Anything new must come
// with its own key.
export function trustsEndpoint(
  provider: Provider,
  baseURL: string | null,
  savedBaseURL: string | null,
) {
  const origin = originOf(baseURL ?? OFFICIAL_BASE_URL[provider]);
  return (
    origin !== null &&
    (origin === originOf(OFFICIAL_BASE_URL[provider]) ||
      (savedBaseURL !== null && origin === originOf(savedBaseURL)))
  );
}
// Apply a validated PATCH to the stored row. When the endpoint moves to an
// origin the stored key was never sent to and the same PATCH brings no new
// key, the stored key for that provider is dropped rather than carried over.
export function applySettingsPatch(
  raw: Record<string, unknown>,
  patch: z.infer<typeof settingsPatch>,
): Stored {
  const saved = storedSettings.parse(raw);
  const previousBaseURL = resolveBaseURL(saved, resolveProvider(saved));
  if (patch.provider && patch.provider !== saved.provider) {
    if (!patch.model) delete saved.model;
    if (patch.baseURL === undefined) delete saved.baseURL;
  }
  const next: Stored = { ...saved, ...patch };
  const keys = { ...saved.apiKeys };
  for (const name of ["openai", "anthropic"] as const) {
    const key = patch.apiKeys?.[name];
    if (key === null) delete keys[name];
    else if (key !== undefined) keys[name] = key;
  }
  if (patch.baseURL !== undefined) {
    const provider = resolveProvider(next);
    if (
      typeof patch.apiKeys?.[provider] !== "string" &&
      !trustsEndpoint(provider, patch.baseURL, previousBaseURL)
    )
      delete keys[provider];
  }
  if (patch.apiKeys || saved.apiKeys) next.apiKeys = keys;
  return next;
}
export async function readSettings(): Promise<ProviderSettings> {
  const saved = storedSettings.parse(await (await getStore()).getSettings());
  const provider = resolveProvider(saved);
  const model =
    saved.model ??
    process.env.DESIGN_RESEARCH_MODEL ??
    (provider === "openai"
      ? process.env.OPENAI_MODEL || "gpt-4.1-mini"
      : process.env.ANTHROPIC_MODEL || "claude-sonnet-4-5");
  const baseURL = resolveBaseURL(saved, provider);
  if (baseURL !== null && !storedSettings.safeParse({ baseURL }).success)
    throw new HttpError(500, "The server provider base URL is invalid.");
  const keySources = {
    openai: credentialSource(saved.apiKeys?.openai, process.env.OPENAI_API_KEY),
    anthropic: credentialSource(
      saved.apiKeys?.anthropic,
      process.env.ANTHROPIC_API_KEY,
    ),
  };
  const providers = {
    openai: keySources.openai !== null,
    anthropic: keySources.anthropic !== null,
  };
  return {
    provider,
    model,
    baseURL,
    configured: providers[provider],
    providers,
    keySources,
  };
}
function credentialSource(
  stored: string | null | undefined,
  env: string | undefined,
): "stored" | "environment" | null {
  return stored ? "stored" : env ? "environment" : null;
}
export async function readApiKey(provider: "openai" | "anthropic") {
  const saved = storedSettings.parse(await (await getStore()).getSettings());
  return (
    saved.apiKeys?.[provider] ||
    (provider === "openai"
      ? process.env.OPENAI_API_KEY
      : process.env.ANTHROPIC_API_KEY) ||
    undefined
  );
}
export function modelFor(settings: ProviderSettings, apiKey?: string) {
  const key =
    apiKey ||
    (settings.provider === "openai"
      ? process.env.OPENAI_API_KEY
      : process.env.ANTHROPIC_API_KEY);
  return settings.provider === "openai"
    ? settings.baseURL
      ? createOpenAI({
          apiKey: key,
          baseURL: settings.baseURL,
        }).chat(settings.model)
      : createOpenAI({
          apiKey: key,
          baseURL: "https://api.openai.com/v1",
        }).responses(settings.model)
    : createAnthropic({
        apiKey: key,
        baseURL: settings.baseURL ?? "https://api.anthropic.com/v1",
      })(settings.model);
}

export function supportsToolImages(
  settings: Pick<ProviderSettings, "provider" | "baseURL">,
) {
  return settings.provider === "anthropic" || !settings.baseURL;
}
