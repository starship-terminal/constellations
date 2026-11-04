import { z } from "zod";
import { createOpenAI } from "@ai-sdk/openai";
import { createAnthropic } from "@ai-sdk/anthropic";
import { HttpError } from "./http";
import { getStore } from "@/server/db";
import type { ProviderSettings } from "@/contracts/research";
export const settingsPatch = z
  .object({
    provider: z.enum(["openai", "anthropic"]).optional(),
    model: z.string().trim().min(1).max(160).optional(),
    baseURL: z
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
      }, "Use an HTTP(S) URL without credentials, query or fragment.")
      .nullable()
      .optional(),
    // Per-provider keys saved through Settings. A string sets the key, null
    // clears it, an absent entry keeps it. Keys stay server-side: readSettings
    // only reports where each credential comes from.
    apiKeys: z
      .object({
        openai: z.string().trim().min(1).max(320).nullable().optional(),
        anthropic: z.string().trim().min(1).max(320).nullable().optional(),
      })
      .strict()
      .optional(),
  })
  .strict();
export async function readSettings(): Promise<ProviderSettings> {
  const saved = settingsPatch.parse(await (await getStore()).getSettings());
  const provider =
    saved.provider ??
    (process.env.DESIGN_RESEARCH_PROVIDER === "anthropic"
      ? "anthropic"
      : "openai");
  const model =
    saved.model ??
    process.env.DESIGN_RESEARCH_MODEL ??
    (provider === "openai"
      ? process.env.OPENAI_MODEL || "gpt-4.1-mini"
      : process.env.ANTHROPIC_MODEL || "claude-sonnet-4-5");
  const baseURL =
    saved.baseURL !== undefined
      ? saved.baseURL
      : (process.env.DESIGN_RESEARCH_BASE_URL ??
        (provider === "openai"
          ? process.env.OPENAI_BASE_URL
          : process.env.ANTHROPIC_BASE_URL) ??
        null);
  if (baseURL !== null && !settingsPatch.safeParse({ baseURL }).success)
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
  const saved = settingsPatch.parse(await (await getStore()).getSettings());
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
