import { z } from "zod";
import { getStore } from "@/server/db";
import { endpoint, mutationGuard, readBody } from "@/server/research/http";
export const runtime = "nodejs";
export function GET() {
  return endpoint(async () =>
    Response.json({ collections: await (await getStore()).listCollections() }),
  );
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
