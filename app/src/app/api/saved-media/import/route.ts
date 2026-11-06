import { z } from "zod";
import { getStore } from "@/server/db";
import { getReference } from "@/server/sources";
import { endpoint, mutationGuard, readBody } from "@/server/research/http";
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const { paths } = await readBody(
      request,
      z.object({ paths: z.array(z.string().max(2000)).max(5000) }).strict(),
    );
    const store = await getStore();
    const cache = new Map<string, Awaited<ReturnType<typeof getReference>>>();
    let imported = 0;
    const skipped: string[] = [];
    for (const path of new Set(paths)) {
      let canonical: string;
      try {
        canonical = decodeURIComponent(
          new URL(path, "http://local.invalid").pathname,
        ).replace(/^\/(?:media\/)?/, "");
      } catch {
        skipped.push(path);
        continue;
      }
      const match = /^systems\/([a-z0-9-]+)\//.exec(canonical);
      const referoMatch =
        /^refero-media\/(shots|posters|detail-posters|favicons)\/([a-z0-9-]+)\.(?:jpg|jpeg|png|webp)$/.exec(
          canonical,
        );
      if (!match && !referoMatch) {
        skipped.push(path);
        continue;
      }
      const id = match ? `systems:${match[1]}` : `refero:${referoMatch![2]}`;
      if (!cache.has(id)) cache.set(id, await getReference(id));
      const media = cache
        .get(id)
        ?.media.find((item) =>
          match
            ? item.id === canonical
            : item.path?.replace(/^\/(?:media\/)?/, "") === canonical,
        );
      if (!media) {
        skipped.push(path);
        continue;
      }
      await store.saveMedia(id, media.id);
      imported++;
    }
    return Response.json({ imported, skipped });
  });
}
