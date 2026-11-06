import { getStore } from "@/server/db";
import {
  endpoint,
  mutationGuard,
  readBody,
  conversationPatch,
  HttpError,
  identifier,
} from "@/server/research/http";
import { validateReferences } from "@/server/research/references";
type Context = { params: Promise<{ id: string }> };
export const runtime = "nodejs";
export function GET(_: Request, context: Context) {
  return endpoint(async () => {
    const id = identifier.parse((await context.params).id);
    const row = await (await getStore()).getConversation(id);
    if (!row) throw new HttpError(404, "Conversation not found.");
    return Response.json(row);
  });
}
export function PATCH(request: Request, context: Context) {
  return endpoint(async () => {
    mutationGuard(request);
    const id = identifier.parse((await context.params).id);
    const patch = await readBody(request, conversationPatch);
    const store = await getStore();
    const row = await store.getConversation(id);
    if (!row) throw new HttpError(404, "Conversation not found.");
    await validateReferences(
      patch.pinnedIds ?? row.pinnedIds,
      patch.excludedIds ?? row.excludedIds,
    );
    await store.updateConversation(id, {
      ...patch,
      ...(patch.pinnedIds || patch.excludedIds
        ? {
            pinnedIds: patch.pinnedIds ?? row.pinnedIds,
            excludedIds: patch.excludedIds ?? row.excludedIds,
          }
        : {}),
    });
    return Response.json(await store.getConversation(id));
  });
}
