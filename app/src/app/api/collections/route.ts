import { z } from "zod";
import { getStore } from "@/server/db";
import { endpoint, mutationGuard, readBody } from "@/server/research/http";
import { mediaSelection } from "@/server/collections/media";
export const runtime = "nodejs";
export function GET(request?: Request) {
  return endpoint(async () => {
    const params = request
      ? new URL(request.url).searchParams
      : new URLSearchParams();
    const selected =
      params.has("referenceId") || params.has("mediaId")
        ? mediaSelection.parse({
            referenceId: params.get("referenceId"),
            mediaId: params.get("mediaId"),
          })
        : null;
    const store = await getStore();
    return Response.json({
      collections: await store.listCollections(),
      ...(selected
        ? {
            mediaCollectionIds: await store.mediaCollectionIds(
              selected.referenceId,
              selected.mediaId,
            ),
          }
        : {}),
    });
  });
}
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const { name } = await readBody(
      request,
      z.object({ name: z.string().trim().min(1).max(160) }).strict(),
    );
    return Response.json(await (await getStore()).createCollection(name), {
      status: 201,
    });
  });
}
