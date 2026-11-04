import { StyleDetailPage } from "@/features/style-detail";
export default async function Page({
  params,
}: {
  params: Promise<{ source: string; slug: string }>;
}) {
  const { source, slug } = await params;
  return <StyleDetailPage source={source} slug={slug} />;
}
