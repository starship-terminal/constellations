import { z } from "zod";
import { endpoint, mutationGuard, readBody } from "@/server/research/http";
import {
  readApiKey,
  readSettings,
  settingsPatch,
} from "@/server/research/settings";
import { discoverModels } from "@/server/research/models";
// The probe may carry unsaved form values, including a key still being tested.
// A probed key authenticates this request only; it is never persisted or
// returned. Without one, the saved credential (then the environment) applies.
const modelProbe = z
  .object({
    provider: z.enum(["openai", "anthropic"]).optional(),
    baseURL: settingsPatch.shape.baseURL,
    apiKey: z.string().trim().min(1).max(320).optional(),
  })
  .strict();
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const probe = await readBody(request, modelProbe);
    const saved = await readSettings();
    const provider = probe.provider ?? saved.provider;
    const baseURL = probe.baseURL === undefined ? saved.baseURL : probe.baseURL;
    const key = probe.apiKey ?? (await readApiKey(provider));
    return Response.json({
      models: await discoverModels({ provider, baseURL }, key),
      provider,
    });
  });
}
