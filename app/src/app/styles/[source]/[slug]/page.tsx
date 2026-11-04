import { redirect } from "next/navigation";
import { StyleDetailPage } from "@/features/style-detail";
export default async function Page({
  params,
}: {
  params: Promise<{ source: string; slug: string }>;
}) {
  const { source, slug } = await params;
  if (source === "systems") redirect(`/library/${slug}`);
  return <StyleDetailPage source={source} slug={slug} />;
}
