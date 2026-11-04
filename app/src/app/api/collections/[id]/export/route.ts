import { getStore } from "@/server/db";
import { getReference } from "@/server/sources";
import { endpoint, HttpError, identifier } from "@/server/research/http";
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
    for (const item of row.items) {
      const ref = await getReference(item.referenceId);
      chunks.push(
        `### ${ref?.name ?? item.referenceId}`,
        `Reference ID: ${item.referenceId}`,
        `Evidence: ${ref?.evidence ?? "Source unavailable"}`,
        ref?.sourceUrl ? `Original source: ${ref.sourceUrl}` : "",
        `Local reference: /styles/${item.referenceId.split(":").map(encodeURIComponent).join("/")}`,
        item.note,
      );
    }
    return new Response(chunks.filter(Boolean).join("\n\n") + "\n", {
      headers: {
        "Content-Type": "text/markdown; charset=utf-8",
        "Content-Disposition": `attachment; filename="research-${id}.md"`,
      },
    });
  });
}
