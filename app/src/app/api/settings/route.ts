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
    const saved = settingsPatch.parse(await store.getSettings());
    if (patch.provider && patch.provider !== saved.provider) {
      if (!patch.model) delete saved.model;
      if (patch.baseURL === undefined) delete saved.baseURL;
    }
    await store.saveSettings({ ...saved, ...patch });
    return Response.json(await readSettings());
  });
}
