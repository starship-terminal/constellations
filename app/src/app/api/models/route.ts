import { endpoint, mutationGuard } from "@/server/research/http";
import { readSettings } from "@/server/research/settings";
import { discoverModels } from "@/server/research/models";
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const settings = await readSettings();
    const key =
      settings.provider === "openai"
        ? process.env.OPENAI_API_KEY
        : process.env.ANTHROPIC_API_KEY;
    return Response.json({
      models: await discoverModels(settings, key),
      provider: settings.provider,
    });
  });
}
