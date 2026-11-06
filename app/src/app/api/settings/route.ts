import { getStore } from "@/server/db";
import { readSettings, settingsPatch } from "@/server/research/settings";
import { endpoint, mutationGuard, readBody } from "@/server/research/http";
export const runtime = "nodejs";
export function GET() {
  return endpoint(async () => Response.json(await readSettings()));
}
export function PATCH(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const patch = await readBody(request, settingsPatch);
    const store = await getStore();
    await store.updateSettings((raw) => {
      const saved = settingsPatch.parse(raw);
      if (patch.provider && patch.provider !== saved.provider) {
        if (!patch.model) delete saved.model;
        if (patch.baseURL === undefined) delete saved.baseURL;
      }
      const next = { ...saved, ...patch };
      if (patch.apiKeys) {
        const merged = { ...saved.apiKeys };
        for (const name of ["openai", "anthropic"] as const) {
          const key = patch.apiKeys[name];
          if (key === null) delete merged[name];
          else if (key !== undefined) merged[name] = key;
        }
        next.apiKeys = merged;
      }
      return next;
    });
    return Response.json(await readSettings());
  });
}
