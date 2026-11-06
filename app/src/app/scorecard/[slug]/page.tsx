import { PackageScorecard } from "@/features/knowledge/scorecard";
export const dynamic = "force-dynamic";
export const metadata = { title: "Package audit" };
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  return <PackageScorecard slug={slug} />;
}
