import { z } from "zod";
import {
  endpoint,
  HttpError,
  mutationGuard,
  readBody,
} from "@/server/research/http";
import {
  readApiKey,
  readSettings,
  readTrustedBaseURL,
  submittedBaseURL,
  trustsEndpoint,
} from "@/server/research/settings";
import { discoverModels } from "@/server/research/models";
// The probe may carry unsaved form values, including a key still being tested.
// A probed key authenticates this request only; it is never persisted or
// returned. Without one, the saved credential (then the environment) applies,
// and only toward the provider's own API or the saved endpoint.
const modelProbe = z
  .object({
    provider: z.enum(["openai", "anthropic"]).optional(),
    baseURL: submittedBaseURL,
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
    if (
      !probe.apiKey &&
      !trustsEndpoint(provider, baseURL, await readTrustedBaseURL(provider))
    )
      throw new HttpError(
        400,
        "Enter an API key to test this endpoint. A saved key is only sent to the provider's own API or the saved endpoint.",
      );
    const key = probe.apiKey ?? (await readApiKey(provider));
    return Response.json({
      models: await discoverModels({ provider, baseURL }, key),
      provider,
    });
  });
}
