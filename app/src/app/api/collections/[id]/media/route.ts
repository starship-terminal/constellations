import { getStore } from "@/server/db";
import { getReferenceMedia } from "@/server/sources";
import {
  hydrateCollectionMedia,
  mediaSelection,
} from "@/server/collections/media";
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
    const id = identifier.parse((await context.params).id);
    const row = await (await getStore()).getCollection(id);
    if (!row) throw new HttpError(404, "Collection not found.");
    return Response.json({
      items: await hydrateCollectionMedia(row.mediaItems),
    });
  });
}
export function POST(request: Request, context: Context) {
  return endpoint(async () => {
    mutationGuard(request);
    const id = identifier.parse((await context.params).id);
    const value = await readBody(request, mediaSelection);
    const store = await getStore();
    if (!(await store.getCollection(id)))
      throw new HttpError(404, "Collection not found.");
    const reference = await getReferenceMedia(value.referenceId);
    const capture = reference?.media.find((item) => item.id === value.mediaId);
    if (!capture) throw new HttpError(404, "Capture not found.");
    if (capture.type !== "image")
      throw new HttpError(
        400,
        "Screenshot boards accept captured images only.",
      );
    await store.putCollectionMedia(id, value.referenceId, value.mediaId);
    return Response.json({ ok: true });
  });
}
export function DELETE(request: Request, context: Context) {
  return endpoint(async () => {
    mutationGuard(request);
    const id = identifier.parse((await context.params).id);
    const params = new URL(request.url).searchParams;
    const value =
      params.has("referenceId") || params.has("mediaId")
        ? mediaSelection.parse({
            referenceId: params.get("referenceId"),
            mediaId: params.get("mediaId"),
          })
        : await readBody(request, mediaSelection);
    const store = await getStore();
    if (!(await store.getCollection(id)))
      throw new HttpError(404, "Collection not found.");
    await store.removeCollectionMedia(id, value.referenceId, value.mediaId);
    return Response.json({ ok: true });
  });
}
