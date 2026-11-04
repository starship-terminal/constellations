import { DocsReader } from "@/features/knowledge/docs";
export const dynamic = "force-dynamic";
export const metadata = { title: "Library docs" };
export default async function Page({
  params,
}: {
  params: Promise<{ path: string[] }>;
}) {
  const { path } = await params;
  return <DocsReader slug={path.join("/")} />;
}
