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
type Context = { params: Promise<{ id: string }> };
export const runtime = "nodejs";
export function POST(request: Request, context: Context) {
  return endpoint(async () => {
    mutationGuard(request);
    const id = identifier.parse((await context.params).id);
    const body = await readBody(
      request,
      z
        .object({
          referenceId: identifier,
          note: z.string().max(20000).optional(),
        })
        .strict(),
    );
    const store = await getStore();
    if (!(await store.getCollection(id)))
      throw new HttpError(404, "Collection not found.");
    if (!(await getReference(body.referenceId)))
      throw new HttpError(400, "Unknown reference.");
    await store.putItem(id, body.referenceId, body.note);
    return Response.json({ ok: true });
  });
}
export function DELETE(request: Request, context: Context) {
  return endpoint(async () => {
    mutationGuard(request);
    const id = identifier.parse((await context.params).id);
    const referenceId = identifier.parse(
      new URL(request.url).searchParams.get("referenceId"),
    );
    const store = await getStore();
    if (!(await store.getCollection(id)))
      throw new HttpError(404, "Collection not found.");
    await store.removeItem(id, referenceId);
    return Response.json({ ok: true });
  });
}
