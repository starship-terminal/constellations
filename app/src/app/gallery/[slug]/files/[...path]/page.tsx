import { redirect } from "next/navigation";
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string; path: string[] }>;
}) {
  const { slug, path } = await params;
  const relative =
    path[0] === "systems" && path[1] === slug ? path.slice(2) : path;
  redirect(
    `/library/${encodeURIComponent(slug)}?tab=files&file=${encodeURIComponent(relative.join("/"))}`,
  );
}
