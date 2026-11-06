import { z } from "zod";
import { getStore } from "@/server/db";
import { getReference } from "@/server/sources";
import {
  endpoint,
  mutationGuard,
  readBody,
  HttpError,
  identifier,
} from "@/server/research/http";
const selection = z
  .object({ referenceId: identifier, mediaId: z.string().min(1).max(2000) })
  .strict();
export const runtime = "nodejs";
export function GET() {
  return endpoint(async () => {
    const rows = await (await getStore()).listSavedMedia();
    const cache = new Map<string, Awaited<ReturnType<typeof getReference>>>();
    const items = [];
    for (const row of rows) {
      if (!cache.has(row.referenceId))
        cache.set(row.referenceId, await getReference(row.referenceId));
      const reference = cache.get(row.referenceId);
      const media = reference?.media.find((m) => m.id === row.mediaId);
      items.push({
        ...row,
        name: reference?.name ?? row.referenceId,
        media: media ?? null,
      });
    }
    return Response.json({ items });
  });
}
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const value = await readBody(request, selection);
    const reference = await getReference(value.referenceId);
    if (!reference?.media.some((m) => m.id === value.mediaId))
      throw new HttpError(404, "Screenshot not found.");
    await (await getStore()).saveMedia(value.referenceId, value.mediaId);
    return Response.json({ saved: true });
  });
}
export function DELETE(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const value = await readBody(request, selection);
    await (await getStore()).removeSavedMedia(value.referenceId, value.mediaId);
    return Response.json({ saved: false });
  });
}
