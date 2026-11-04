import { z } from "zod";
import { endpoint, mutationGuard, readBody } from "@/server/research/http";
import { readSettings, settingsPatch } from "@/server/research/settings";
import { discoverModels } from "@/server/research/models";
// The probe may carry unsaved form values; the credential always stays in the
// server environment and only the resolved provider picks which key is used.
const modelProbe = z
  .object({
    provider: z.enum(["openai", "anthropic"]).optional(),
    baseURL: settingsPatch.shape.baseURL,
  })
  .strict();
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const probe = await readBody(request, modelProbe);
    const saved = await readSettings();
    const provider = probe.provider ?? saved.provider;
    const baseURL = probe.baseURL === undefined ? saved.baseURL : probe.baseURL;
    const key =
      provider === "openai"
        ? process.env.OPENAI_API_KEY
        : process.env.ANTHROPIC_API_KEY;
    return Response.json({
      models: await discoverModels({ provider, baseURL }, key),
      provider,
    });
  });
}
