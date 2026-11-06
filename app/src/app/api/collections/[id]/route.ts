import { z } from "zod";
import { getStore } from "@/server/db";
import { getReferenceSummary } from "@/server/sources";
import { hydrateCollectionMedia } from "@/server/collections/media";
import {
  endpoint,
  mutationGuard,
  readBody,
  HttpError,
  identifier,
} from "@/server/research/http";
type Context = { params: Promise<{ id: string }> };
export const runtime = "nodejs";
export function GET(_: Request, context: Context) {
  return endpoint(async () => {
    const row = await (
      await getStore()
    ).getCollection(identifier.parse((await context.params).id));
    if (!row) throw new HttpError(404, "Collection not found.");
    return Response.json({
      ...row,
      mediaItems: await hydrateCollectionMedia(row.mediaItems),
      items: await Promise.all(
        row.items.map(async (item) => ({
          ...item,
          // The board shows cards; the inspector loads full detail itself.
          reference: await getReferenceSummary(item.referenceId),
        })),
      ),
    });
  });
}
export function PATCH(request: Request, context: Context) {
  return endpoint(async () => {
    mutationGuard(request);
    const id = identifier.parse((await context.params).id);
    const patch = await readBody(
      request,
      z
        .object({
          name: z.string().trim().min(1).max(160).optional(),
          notes: z.string().max(50000).optional(),
        })
        .strict(),
    );
    const store = await getStore();
    if (!(await store.getCollection(id)))
      throw new HttpError(404, "Collection not found.");
    await store.updateCollection(id, patch);
    return Response.json((await store.getCollection(id))!.collection);
  });
}
export function DELETE(request: Request, context: Context) {
  return endpoint(async () => {
    mutationGuard(request);
    const id = identifier.parse((await context.params).id);
    const store = await getStore();
    if (!(await store.getCollection(id)))
      throw new HttpError(404, "Collection not found.");
    await store.deleteCollection(id);
    return Response.json({ deleted: id });
  });
}
