import { z } from "zod";
import { getStore } from "@/server/db";
import { endpoint, mutationGuard, readBody } from "@/server/research/http";
export const runtime = "nodejs";
export function GET() {
  return endpoint(async () =>
    Response.json({
      conversations: await (await getStore()).listConversations(),
    }),
  );
}
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const body = await readBody(
      request,
      z
        .object({
          title: z.string().trim().min(1).max(160).optional(),
          initialText: z.string().trim().min(1).max(30000).optional(),
        })
        .strict(),
    );
    return Response.json(
      await (await getStore()).createConversation(body.title, body.initialText),
      { status: 201 },
    );
  });
}
