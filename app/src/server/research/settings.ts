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
    saved.baseURL ??
    process.env.DESIGN_RESEARCH_BASE_URL ??
    (provider === "openai"
      ? process.env.OPENAI_BASE_URL
      : process.env.ANTHROPIC_BASE_URL) ??
    null;
  if (baseURL !== null && !settingsPatch.safeParse({ baseURL }).success)
    throw new HttpError(500, "The server provider base URL is invalid.");
  const providers = {
    openai: Boolean(process.env.OPENAI_API_KEY),
    anthropic: Boolean(process.env.ANTHROPIC_API_KEY),
  };
  return {
    provider,
    model,
    baseURL,
    configured: providers[provider],
    providers,
  };
}
export function modelFor(settings: ProviderSettings) {
  return settings.provider === "openai"
    ? settings.baseURL
      ? createOpenAI({
          apiKey: process.env.OPENAI_API_KEY,
          baseURL: settings.baseURL,
        }).chat(settings.model)
      : createOpenAI({ apiKey: process.env.OPENAI_API_KEY }).responses(
          settings.model,
        )
    : createAnthropic({
        apiKey: process.env.ANTHROPIC_API_KEY,
        baseURL: settings.baseURL ?? undefined,
      })(settings.model);
}

export function supportsToolImages(
  settings: Pick<ProviderSettings, "provider" | "baseURL">,
) {
  return settings.provider === "anthropic" || !settings.baseURL;
}
