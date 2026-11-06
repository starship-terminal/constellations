import { getStore } from "@/server/db";
import { getReferenceSummary } from "@/server/sources";
import { endpoint, HttpError, identifier } from "@/server/research/http";
import { hydrateCollectionMedia } from "@/server/collections/media";
import { mediaDetailHref } from "@/features/package-detail-data";
type Context = { params: Promise<{ id: string }> };
export const runtime = "nodejs";
export function GET(_: Request, context: Context) {
  return endpoint(async () => {
    const id = identifier.parse((await context.params).id);
    const row = await (await getStore()).getCollection(id);
    if (!row) throw new HttpError(404, "Collection not found.");
    const chunks = [
      `# ${row.collection.name}`,
      row.collection.notes,
      "## References",
    ];
    const refs = await Promise.all(
      row.items.map((item) => getReferenceSummary(item.referenceId)),
    );
    for (const [index, item] of row.items.entries()) {
      const ref = refs[index];
      chunks.push(
        `### ${ref?.name ?? item.referenceId}`,
        `Reference ID: ${item.referenceId}`,
        `Evidence: ${ref?.evidence ?? "Source unavailable"}`,
        ref?.sourceUrl ? `Original source: ${ref.sourceUrl}` : "",
        ref
          ? `Local reference: ${ref.source === "systems" ? `/library/${encodeURIComponent(ref.slug)}` : `/styles/refero/${encodeURIComponent(ref.slug)}`}`
          : "Local reference unavailable",
        item.note,
      );
    }
    if (row.mediaItems.length) {
      chunks.push("## Captured screens");
      for (const item of await hydrateCollectionMedia(row.mediaItems)) {
        const href =
          item.reference?.source === "systems" && item.media
            ? mediaDetailHref(item.reference.slug, item.media)
            : item.reference
              ? `/styles/${item.reference.source}/${item.reference.slug}`
              : "";
        chunks.push(
          `### ${item.name}: ${item.media?.name || item.mediaId}`,
          `Reference ID: ${item.referenceId}`,
          `Media ID: ${item.mediaId}`,
          href ? `Local capture: ${href}` : "Source unavailable",
        );
      }
    }
    return new Response(chunks.filter(Boolean).join("\n\n") + "\n", {
      headers: {
        "Content-Type": "text/markdown; charset=utf-8",
        "Content-Disposition": `attachment; filename="research-${id}.md"`,
      },
    });
  });
}
