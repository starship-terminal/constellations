import { getStore } from "@/server/db";
import {
  applySettingsPatch,
  readSettings,
  settingsPatch,
} from "@/server/research/settings";
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
    await store.updateSettings((raw) => applySettingsPatch(raw, patch));
    return Response.json(await readSettings());
  });
}
